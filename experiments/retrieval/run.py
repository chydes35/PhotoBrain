#!/usr/bin/env python3
"""Rebuild/run PB-006's keyword baseline from a pinned Git commit."""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import subprocess
import time
from pathlib import Path

BASE = "6a7f30e21a10618601e4f987e3759b714e08baf5"
HERE = Path(__file__).resolve().parent
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
WORD = re.compile(r"[^\W_]+", re.UNICODE)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True)


def corpus_files() -> list[str]:
    paths = [p for p in git("ls-tree", "-r", "--name-only", BASE, "chapters", "references").splitlines() if p.endswith(".md")]
    paths.append("INDEX.md")
    return sorted(paths)


def chunks(path: str, text: str) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    current_title = "(preamble)"
    body: list[str] = []

    def flush() -> None:
        content = "\n".join(body).strip()
        if content:
            result.append({"id": f"{path}#{current_title}", "title": current_title, "path": path, "body": content})

    for line in text.splitlines():
        match = HEADING.match(line)
        if match:
            flush()
            current_title = match.group(2)
            body = []
        else:
            body.append(line)
    flush()
    return result


def load_chunks() -> list[dict[str, str]]:
    result = []
    for path in corpus_files():
        source = git("show", f"{BASE}:{path}")
        result.extend(chunks(path, source))
    return result


def run_keyword(documents: list[dict[str, str]], queries: list[dict], top_k: int = 5) -> dict:
    db = sqlite3.connect(":memory:")
    db.execute("CREATE VIRTUAL TABLE docs USING fts5(doc_id UNINDEXED, title, body, path UNINDEXED)")
    db.executemany("INSERT INTO docs(doc_id,title,body,path) VALUES(:id,:title,:body,:path)", documents)
    rows = {}
    for query in queries:
        started = time.perf_counter()
        # Feed plain token phrases to FTS5, not raw natural-language punctuation.
        fts_query = " OR ".join(f'"{token}"' for token in WORD.findall(query["query"]))
        hits = db.execute(
            "SELECT doc_id, bm25(docs) AS score FROM docs WHERE docs MATCH ? ORDER BY score LIMIT ?",
            (fts_query, top_k),
        ).fetchall()
        elapsed_ms = (time.perf_counter() - started) * 1000
        rows[query["id"]] = {"hits": [{"id": doc_id, "score": score} for doc_id, score in hits], "latency_ms": elapsed_ms}
    db.close()
    return rows


def metrics(queries: list[dict], results: dict) -> dict:
    recalls, reciprocal_ranks = [], []
    expected_ids_total = expected_ids_found = 0
    doc_map = {d["id"]: d["body"] for d in load_chunks()}
    for q in queries:
        relevant = set(q["relevant"])
        hits = results[q["id"]]["hits"]
        got = [hit["id"] for hit in hits]
        recalls.append(len(relevant.intersection(got)) / len(relevant) if relevant else 1.0)
        rank = next((i for i, doc_id in enumerate(got, start=1) if doc_id in relevant), None)
        reciprocal_ranks.append(1 / rank if rank else 0.0)
        if q["expected_ids"]:
            expected_ids_total += len(q["expected_ids"])
            returned_text = "\n".join(doc_map.get(doc_id, "") for doc_id in got)
            expected_ids_found += sum(cid in returned_text for cid in q["expected_ids"])
    return {
        "recall_at_5": sum(recalls) / len(recalls),
        "mrr_at_5": sum(reciprocal_ranks) / len(reciprocal_ranks),
        "expected_claim_id_coverage_at_5": expected_ids_found / expected_ids_total if expected_ids_total else None,
        "expected_claim_ids_total": expected_ids_total,
        "expected_claim_ids_found": expected_ids_found,
        "mean_latency_ms": sum(row["latency_ms"] for row in results.values()) / len(results),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / "keyword-results.json")
    args = parser.parse_args()
    queries = json.loads((HERE / "queries.json").read_text())
    documents = load_chunks()
    results = run_keyword(documents, queries)
    report = {
        "method": "SQLite FTS5 BM25",
        "corpus_commit": BASE,
        "sqlite_version": sqlite3.sqlite_version,
        "document_count": len(documents),
        "corpus_files": corpus_files(),
        "query_count": len(queries),
        "metrics": metrics(queries, results),
        "queries": results,
    }
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("method", "corpus_commit", "document_count", "query_count", "metrics")}, indent=2))


if __name__ == "__main__":
    main()
