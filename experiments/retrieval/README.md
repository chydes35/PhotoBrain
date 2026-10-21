# PB-006 retrieval bake-off

Status: **incomplete** — the pinned-corpus keyword baseline ran; no embedding run was possible with the preinstalled tools.

## Reproduce

From the PhotoBrain repository root, run `python3 experiments/retrieval/run.py`. The standard-library runner reads only tracked Markdown under `chapters/` and `references/`, plus `INDEX.md`, directly from base commit `6a7f30e21a10618601e4f987e3759b714e08baf5`; it does not index this experiment or working-tree edits. The source files are split into one chunk per Markdown heading (with preamble chunks where applicable). Twelve fixed, manually labeled natural-language queries and expected relevant section IDs are in [`queries.json`](queries.json). The generated [`keyword-results.json`](keyword-results.json) records the exact corpus file list, results, timings and aggregate metrics.

## Baseline result

SQLite FTS5 BM25, SQLite `3.53.4`, Python `3.14.7`, returned 52 chunks for the 12 queries. Query tokens are quoted and OR-combined to avoid exposing raw query punctuation to the FTS5 parser. Top five results were compared against the hand-labeled relevant section IDs.

| Metric | Result |
| --- | ---: |
| Recall@5 (mean per query) | 0.826 |
| MRR@5 (mean reciprocal rank) | 0.628 |
| Expected claim-ID coverage in top 5 | 13 / 22 (0.591) |
| Mean measured query latency (this saved run) | 0.186 ms |

The latency is one local run per query, not a controlled performance benchmark, and varies slightly on rerun. The labels are section-level and hand-authored; a future comparison should freeze them before running either system and ideally use more than one reviewer. Q09–Q11 include multiple answer-bearing chunks after independent review. Q10 asks what the local summary states and does not claim the summary enumerates every permitted PNG type/bit-depth combination. The small, two-topic corpus does not establish retrieval quality for unrepresented PhotoBrain topics. FTS5's OR match favors recall and can return broad false positives. MRR and Recall@5 measure only the supplied labels, not answer correctness. Expected claim-ID coverage asks whether the specified claim ID strings occur anywhere in returned top-five text, including registry chunks; it does not establish that the claim is supported or that a citation is complete.

## Embedding path

No embedding result is reported. Local inspection found no installed embedding library or compatible model endpoint; the installed Ollama text model's `/api/embed` path returned HTTP 501. A separate Ollama availability check was blocked by the execution sandbox. No model, package, data, or remote service was installed or used. The next valid comparison requires an explicitly approved local embedding model and its version/license record. The [Ollama embed API](https://docs.ollama.com/api/embed) documents the expected embedding endpoint, but API support alone does not make a model available locally.

No external vector database is justified by this experiment. The corpus is small and the neural comparison is incomplete, so no method-adoption or product-performance decision is made.
