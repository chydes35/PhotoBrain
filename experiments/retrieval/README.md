# PB-006 retrieval bake-off

Status: **complete for this bounded comparison** — both local keyword and embedding retrieval ran over the pinned corpus and fixed judgments. Results do not justify an application or database adoption decision.

## Reproduce

From the PhotoBrain repository root, run `python3 experiments/retrieval/run.py` for FTS5. For the embedding run, first start a dedicated local Ollama server with its model directory on the external SSD: `OLLAMA_MODELS="$PWD/.ollama-models" OLLAMA_HOST=127.0.0.1:11435 ollama serve`; then run `python3 experiments/retrieval/run.py --method embedding --ollama-url http://127.0.0.1:11435`. The standard-library runner reads only tracked Markdown under `chapters/` and `references/`, plus `INDEX.md`, directly from base commit `6a7f30e21a10618601e4f987e3759b714e08baf5`; it does not index this experiment or working-tree edits. The source files are split into one chunk per Markdown heading (with preamble chunks where applicable). Twelve fixed, manually labeled natural-language queries and expected relevant section IDs are in [`queries.json`](queries.json). The generated [`keyword-results.json`](keyword-results.json) and [`embedding-results.json`](embedding-results.json) record the exact corpus file list, results, timings and aggregate metrics.

## Baseline result

SQLite FTS5 BM25, SQLite `3.53.4`, Python `3.14.7`, returned 52 chunks for the 12 queries. Query tokens are quoted and OR-combined to avoid exposing raw query punctuation to the FTS5 parser. Top five results were compared against the hand-labeled relevant section IDs.

| Metric | SQLite FTS5 BM25 | Nomic Embed Text v1.5 + cosine |
| --- | ---: | ---: |
| Recall@5 (mean per query) | 0.826 | 0.708 |
| MRR@5 (mean reciprocal rank) | 0.628 | 0.597 |
| Expected claim-ID presence in top 5 | 13 / 22 (0.591) | 16 / 22 (0.727) |
| Mean measured query latency | 0.189 ms | 52.99 ms |

Embedding all 52 documents took 11.94 seconds in this run (mean 229.6 ms/document); document encoding time is separate from query latency. Embedding scores use cosine similarity over the 768-dimensional model vectors. Nomic's documented `search_document:` and `search_query:` prefixes were used. The GGUF model is Apache-2.0 per its [model card](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF); it was downloaded through Ollama and stored under `.worktrees/pb-006/.ollama-models` on the external SSD. Ollama version was `0.33.2`; model digest `0a109f422b47e3a30ba2b10eca18548e944e8a23073ee3f3e947efcf3c45e59f`; model-reported context length 2,048 tokens. The [Ollama environment configuration](https://github.com/ollama/ollama/blob/main/envconfig/config.go) supports redirecting model storage with `OLLAMA_MODELS`.

The embedding run has higher expected claim-ID presence but lower section Recall@5 and MRR than FTS5 on this query set; that is a descriptive result over 12 questions, not evidence that either method is generally better. Latency is one local run per query, not a controlled performance benchmark, and varies slightly on rerun. Timed query search includes FTS query execution for keywords, and local HTTP embedding plus cosine scoring/sorting for embeddings; initial index setup is excluded. Embedding document-encoding time is reported separately; keyword index-build time was not measured. The labels are section-level and hand-authored; an independent reviewer checked their scope and recalculated metrics. Q09–Q11 include multiple answer-bearing chunks after review. Q10 asks what the local summary states and does not claim it enumerates every permitted PNG type/bit-depth combination. The small, two-topic corpus does not establish retrieval quality for unrepresented PhotoBrain topics. FTS5's OR match favors recall and can return broad false positives. MRR and Recall@5 measure only the supplied labels, not answer correctness. Expected claim-ID presence counts whether specified claim ID strings occur anywhere in returned top-five text, including registry chunks; it does not establish that the claim is supported or that a citation is complete. The model context is limited to 2,048 tokens in this run; the benchmark does not separately tokenize/report each chunk length, so long-chunk truncation is an open limitation.

## Scope and interpretation

No external vector database is justified by this experiment. The small two-topic corpus and 12-query judged set are sufficient only for this initial comparison. Keep keyword retrieval as the baseline; consider embeddings only if more queries reveal a material semantic-retrieval benefit and verify that long chunks are handled correctly. Generated results remain pointers into reviewed Markdown rather than a new authority.
