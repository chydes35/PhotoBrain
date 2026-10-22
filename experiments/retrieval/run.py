#!/usr/bin/env python3
"""Run PB-006 retrieval methods against the same pinned Git corpus."""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import sqlite3
import subprocess
import time
import urllib.request
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


def ollama_post(base_url: str, endpoint: str, payload: dict) -> dict:
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}{endpoint}",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        return json.load(response)


def ollama_get(base_url: str, endpoint: str) -> dict:
    with urllib.request.urlopen(f"{base_url.rstrip('/')}{endpoint}", timeout=60) as response:
        return json.load(response)


def run_embedding(documents: list[dict[str, str]], queries: list[dict], model: str, base_url: str, top_k: int = 5) -> tuple[dict, dict]:
    document_vectors = []
    started = time.perf_counter()
    for doc in documents:
        text = f"search_document: {doc['title']}\n{doc['body']}"
        response = ollama_post(base_url, "/api/embed", {"model": model, "input": text})
        document_vectors.append(response["embeddings"][0])
    document_encoding_ms = (time.perf_counter() - started) * 1000

    rows = {}
    for query in queries:
        started = time.perf_counter()
        response = ollama_post(base_url, "/api/embed", {"model": model, "input": f"search_query: {query['query']}"})
        query_vector = response["embeddings"][0]
        query_norm = math.sqrt(sum(value * value for value in query_vector))
        scored = []
        for doc, vector in zip(documents, document_vectors):
            doc_norm = math.sqrt(sum(value * value for value in vector))
            similarity = sum(a * b for a, b in zip(query_vector, vector)) / (query_norm * doc_norm)
            scored.append((doc["id"], similarity))
        scored.sort(key=lambda item: item[1], reverse=True)
        elapsed_ms = (time.perf_counter() - started) * 1000
        rows[query["id"]] = {"hits": [{"id": doc_id, "score": score} for doc_id, score in scored[:top_k]], "latency_ms": elapsed_ms}

    details = ollama_post(base_url, "/api/show", {"name": model})
    tags = ollama_get(base_url, "/api/tags")
    model_row = next((item for item in tags.get("models", []) if item.get("name") == model), {})
    return rows, {
        "model": model,
        "digest": model_row.get("digest", "not exposed"),
        "model_info": details.get("model_info", {}),
        "document_encoding_total_ms": document_encoding_ms,
        "document_encoding_mean_ms": document_encoding_ms / len(documents),
    }


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
    parser.add_argument("--method", choices=("keyword", "embedding"), default="keyword")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--model", default="nomic-embed-text:v1.5")
    parser.add_argument("--ollama-url", default=os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434"))
    args = parser.parse_args()
    ollama_url = args.ollama_url if "://" in args.ollama_url else f"http://{args.ollama_url}"
    output = args.output or HERE / ("keyword-results.json" if args.method == "keyword" else "embedding-results.json")
    queries = json.loads((HERE / "queries.json").read_text())
    documents = load_chunks()
    model_details = None
    if args.method == "keyword":
        results = run_keyword(documents, queries)
        method = "SQLite FTS5 BM25"
    else:
        results, model_details = run_embedding(documents, queries, args.model, ollama_url)
        method = "Nomic Embed Text v1.5 cosine similarity via local Ollama"
    report = {
        "method": method,
        "corpus_commit": BASE,
        "sqlite_version": sqlite3.sqlite_version,
        "document_count": len(documents),
        "corpus_files": corpus_files(),
        "query_count": len(queries),
        "metrics": metrics(queries, results),
        "queries": results,
    }
    if model_details:
        report["model_details"] = model_details
        report["ollama_url"] = ollama_url
    output.write_text(json.dumps(report, indent=2) + "\n")
    summary = {k: report[k] for k in ("method", "corpus_commit", "document_count", "query_count", "metrics")}
    if model_details:
        summary["model_details"] = model_details
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
