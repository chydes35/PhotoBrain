# Open-source ecosystem for PhotoBrain

Version: 0.1.0
Date: 2026-10-21
Author/model: Codex; model version not exposed
Base revision: `901d9db3fe310d31a3e7ec5ae23a64616eb8f042`
Evidence boundary: public project documentation and license files checked on the date above. Capabilities and license identifiers below are source claims, not a legal review or a PhotoBrain performance result.

## Summary

[I] PhotoBrain should keep reviewed Markdown and its source/claim records authoritative. Any retrieval index should be generated from a pinned knowledge revision and retain source IDs, review status, and the indexed revision. Begin with keyword search and compare it with pretrained embeddings on a small, hand-checked query set before adding an external database or training a model.

## Knowledge retrieval and document handling

| ID | Project | [V] Upstream capability / license | [I] Fit and limitation |
|---|---|---|---|
| SRC-PB004-01 | [Docling](https://github.com/docling-project/docling) | Document conversion and structured extraction with Markdown/JSON output; MIT project code. Its project documentation calls out separate model licenses. | Extract candidate text from approved manuals and papers while preserving page/section references for human checking. Extraction does not validate claims or equations. |
| SRC-PB004-02 | [Sentence Transformers](https://github.com/huggingface/sentence-transformers) | Text embeddings, semantic search, reranking and fine-tuning; Apache-2.0 library. The previous `UKPLab/sentence-transformers` URL redirects here. | Best first neural retrieval test. Check the terms of each selected model separately and compare retrieval against keyword search. |
| SRC-PB004-03 | [LlamaIndex](https://github.com/run-llama/llama_index) | Data ingestion and retrieval framework; MIT. | Optional orchestration if a small local pipeline proves too limited; it is not needed for the current Markdown library. |
| SRC-PB004-04 | [Qdrant](https://github.com/qdrant/qdrant) | Vector database with metadata filters and hybrid retrieval; Apache-2.0. | Consider only if measurements show a need for a persistent search service. Keep an export/rebuild path tied to a knowledge commit. |
| SRC-PB004-05 | [LightRAG](https://github.com/HKUDS/LightRAG) | Graph and vector retrieval framework; MIT. | Research candidate for relationship queries. LLM-extracted edges remain unverified until reviewed against sources. Upstream quality claims are not PhotoBrain benchmarks. |
| SRC-PB004-06 | [Microsoft GraphRAG](https://github.com/microsoft/graphrag) | Graph-oriented retrieval framework; MIT. | Reference implementation only for now: current upstream README says the project is largely in maintenance mode and warns that indexing may be expensive. |

## Imaging science, metadata and tools

| ID | Project | [V] Upstream capability / license | [I] Fit and limitation |
|---|---|---|---|
| SRC-PB004-07 | [Colour](https://github.com/colour-science/colour) | Python colour-science algorithms and datasets; BSD-3-Clause. Includes colorimetry, colour models, adaptation and transfer-related tools. | Strong reference implementation for extending the light/color topics. Compare against primary standards and explicit vectors; library output is not itself proof of a camera profile. |
| SRC-PB004-08 | [Lensfun](https://github.com/lensfun/lensfun) | Lens correction algorithms and lens database. Library/docs LGPL-3.0; apps GPL-3.0; database CC BY-SA 3.0. | Useful structured lens-profile source and correction reference. Profile presence alone does not establish calibration quality; track database provenance/version and share-alike terms. |
| SRC-PB004-09 | [ExifTool](https://github.com/exiftool/exiftool) | Perl modules and command-line tools read and write metadata across many formats, including maker notes. README offers Perl Artistic or GPL terms. | Reference metadata tags for format/camera chapters. Do not summarize its license solely from GitHub’s GPL badge. |
| SRC-PB004-10 | [LibRaw](https://github.com/LibRaw/LibRaw) | Reads digital-camera RAW formats; COPYRIGHT offers LGPL-2.1 or CDDL-1.0 and identifies additional incorporated components. | Useful reference for RAW format and decoding research. Decoding support does not establish rendering accuracy or app compatibility. |
| SRC-PB004-11 | [OpenColorIO](https://github.com/AcademySoftwareFoundation/OpenColorIO) | Color-management framework for visual-effects pipelines; BSD-3-Clause code. Documentation and third-party components have separate notices. | Reference for color-management pipelines and LUTs. Record provenance and terms for configurations/LUTs independently. |
| SRC-PB004-12 | [OpenImageIO](https://github.com/AcademySoftwareFoundation/OpenImageIO) | Format-agnostic image I/O/processing, metadata tools, image comparisons, and Python bindings. Main project code Apache-2.0 with separate documentation/third-party notices. | Possible basis for reproducible format and image-comparison experiments. Inspect component notices before bundling any part. |
| SRC-PB004-13 | [ACES Core](https://github.com/aces-aswf/aces-core) | Core CTL functions for rendering, tone/gamut/chroma operations, matrices, transfer functions and adaptation; current project Apache-2.0. Former `ampas/aces-dev` URL redirects to this repository. | Strong reference for cinema color research. Pin the version/tag because historical snapshots may have different context and terms. |
| SRC-PB004-14 | [Netflix VMAF](https://github.com/Netflix/vmaf) | Perceptual video-quality assessment; BSD-2-Clause-Patent. | Relevant to video compression/artifact studies, not a general still-photo quality score. |

## Neural imaging references and research datasets

| ID | Project/data | [V] Upstream capability / license | [I] Fit and limitation |
|---|---|---|---|
| SRC-PB004-15 | [Restormer](https://github.com/swz30/Restormer) | Transformer-based restoration research for denoising, deblurring and deraining; MIT code. | Reference implementation for bounded restoration studies. Check model weights and datasets independently. |
| SRC-PB004-16 | [BasicSR](https://github.com/XPixelGroup/BasicSR) | PyTorch image/video restoration toolbox; Apache-2.0 project license, with additional component acknowledgements. | Experiment framework for comparing published restoration methods. Dataset and checkpoint rights remain separate. |
| SRC-PB004-17 | [OpenCLIP](https://github.com/mlfoundations/open_clip) | MIT implementation of image/text embedding models. | Candidate for text-to-image retrieval experiments over approved, nonprivate examples. Model/checkpoint and training-data terms are separate. |
| SRC-PB004-18 | [SIDD](https://abdokamel.github.io/sidd/) and [simple-camera-pipeline](https://github.com/AbdoKamel/simple-camera-pipeline) | Official SIDD page says dataset and associated code repositories are MIT. Includes noisy/ground-truth smartphone RAW and sRGB pairs; the pipeline has MATLAB and Python implementations. | Relevant to real-noise, denoising, and RAW-to-sRGB research. It is smartphone evidence, not LUMIX sensor characterization. |
| SRC-PB004-19 | [Google HDR+ burst dataset](https://hdrplusdata.org/dataset.html) | 3,640 RAW bursts / 28,461 images with aligned/merged RAW intermediates and final JPEGs; CC BY-SA 4.0. Official page lists a 37 GiB subset and 765 GiB full collection. | Valuable burst/computational-photography reference. Start with the published descriptions; any data acquisition needs deliberate storage and dataset-use planning. Its Android phones do not establish LUMIX performance. |

## Suggested adoption order

1. [I] Use Colour, Lensfun, ExifTool, and ACES as cited references for specific PhotoBrain chapter questions. Treat every source as a lead: extract claims into PhotoBrain’s own claim/source format and independently check them against primary standards or measurement evidence.
2. [I] Evaluate keyword search against Sentence Transformers embeddings using a small fixed question set. Record expected source/claim IDs, top-k results, misses, false positives, model/version, and the knowledge commit used to build the index.
3. [I] If retrieval needs persist beyond a local rebuildable index, compare a lightweight LlamaIndex pipeline and Qdrant using that same query set. Keep graph RAG deferred until relationship queries show a measurable gap.
4. [I] Use SIDD or a small HDR+ subset only for focused method experiments, with separate data records and storage plans. Do not infer LUMIX sensor noise, dynamic range, color response, or camera-specific processing from these smartphone datasets.

## Open questions

- [U] Which PhotoBrain chapter will first benefit from semantic retrieval: color science, RAW/metadata, optics, or computational photography?
- [U] What is the initial query set and what retrieval quality would justify adding embeddings or a database?
- [U] Are model weights, shared LUT/config files, and dataset subsets in scope for later evaluation, given their separate terms and storage costs?
- [U] Which project versions should a later reference topic pin, and which primary sources independently validate each borrowed algorithm or dataset field?
