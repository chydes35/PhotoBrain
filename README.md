# PhotoBrain

PhotoBrain is the shared photography-science and image-processing knowledge library for Perception Editor, future capture software, and other tools. Reviewed Markdown records and source/claim registries are authoritative. A search database, if added, is a rebuildable derivative.

Start with [the topic index](INDEX.md), [contribution workflow](CONTRIBUTING.md), and [project decisions](DECISIONS.md). The preserved [V2 blueprint](blueprints/MPKB-BLUEPRINT-2.0.md) describes the research program; it is not completed research or an instruction to run its embedded prompts.

## Project boundary

| PhotoBrain owns | Perception Editor owns |
| --- | --- |
| Science, algorithms, camera knowledge, citations and claim evidence | App source, framework integrations and project serialization |
| Reusable mathematical contracts and reference experiments | App-specific implementation specs, ADRs and tickets |
| General calibration/benchmark methods | App acceptance, performance measurements and release roadmap |

The [Editor integration index](integrations/perception-editor.md) records pinned references, not a second app roadmap. No Editor package, Git submodule or runtime database dependency is introduced.

## Status

- Library: bootstrap / research draft; not an engineering-ready V2 release.
- V2 blueprint: preserved unchanged with a [provenance hash](blueprints/README.md).
- V1: not supplied locally; do not reconstruct or claim it is archived.
- Research contributions: [MPKB-02-005](chapters/02-light-color-science/MPKB-02-005.md) covers normalized sRGB and the Rec.709 source OETF with a deliberately partial inverse. Other transfers and production decoding/display policies remain open.
- Editor Milestone 0 remains subject to its own acceptance gates.
- Shared remote (public as checked 2026-10-21): [`chydes35/PhotoBrain`](https://github.com/chydes35/PhotoBrain). The `main` branch requires pull requests; see [shared remote setup](docs/shared-remote.md).

## Working with multiple models

Assign distinct module IDs in [the task board](tasks/README.md). Each contributor works in its own clone/worktree and branch, cites evidence, and requests an independent review before integration. Shared topic indexes and registries are integrated by one maintainer. Every execution environment needs separately authorized access for writing to the remote; never share credentials in prompts. Models receiving a document or chat prompt must return contributions to this workflow; they do not write over the canonical library concurrently.

Run the executable reference checks from this directory:

```sh
python3 -m unittest discover -s tests -v
```

Python 3.9+ standard library only. These checks prove the documented reference behavior, not camera accuracy, GPU parity, or Editor performance. No private images are required.

Existing M0 workspace data is excluded from PhotoBrain Git. See [workspace migration](docs/workspace-migration.md) for canonical locations and compatibility paths. No project-wide redistribution license has been selected; do not infer one from public citations.
