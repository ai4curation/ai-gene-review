# DeepTMHMM2 local runtime results

Measured 2026-11-02 on Apple M1 Max, 64 GiB RAM, macOS 26.3, with CPU
inference and eight threads. Python 3.12.9, PyTorch 2.10.0, DeepTMHMM2
0.1.0 at commit `526f6c60f93c0868c7315413da8e669d12373cc3`.

## Cost

With models already loaded, inference is inexpensive for these two proteins:

| Input | Residues | Basic inference, two repeats | With marginals, one run |
|---|---:|---:|---:|
| SPTLC2 / O15270 | 562 | 1.36, 1.33 s | 2.09 s |
| DPM1 / O60762 | 260 | 0.63, 0.71 s | 0.99 s |

These are the corrected API runs in `results/basic/timings.json` and
`results/marginals/timings.json`. The full five-member ensemble is used;
each repeat recomputes the ESM-2 embedding. The API processes proteins singly.

- Cached model loading: 5.0–6.7 seconds, plus 2.3–2.7 seconds for Python imports.
- Unmodified CLI, both proteins with batch size 1: **16.85 seconds total**,
  including startup and export; its internal processing timer reports 8.24 seconds.
  API and CLI have different embedding/execution paths and were measured separately.
- Peak process RSS: **4.93–5.25 GiB** for the CLI and corrected API runs.
  No swaps were reported by `/usr/bin/time`. RSS is cumulative per process,
  not memory attributable to a particular protein. Small memory differences
  between runs should not be interpreted as marginals reducing memory use.
- Model files: **2,735,638,986 bytes (2.55 GiB)** total; ESM-2 accounts for
  2,604,537,549 bytes, with about 125 MiB for task checkpoints.
- Isolated environment: approximately 611 MiB on disk, excluding package
  manager caches and source clones. Model files plus environment are about 3.2 GiB.
- First run: **171.46 seconds** wall time, including initially uncached imports,
  ESM-2 download/model loading (143.74 seconds), and four predictions. This
  excludes environment installation and checkpoint cloning. The initial run
  exposed the API bug below and is retained only as setup/runtime provenance.

Practical assessment: a few genes are easy to run locally on this machine.
Keep the model loaded for repeated use to amortize startup. These short inputs
do not establish performance for long proteins or whole proteomes; batching,
sequence length, other workstation activity, and accelerator hardware matter.
The authors report about 65 minutes for the human proteome on an RTX 8000 GPU,
excluding titin ([preprint, Ensemble prediction](https://doi.org/10.64898/2026.08.24.746435)).
Apple MPS was not tested because the authors explicitly advise against it.

## Predictions and software finding

The unmodified CLI and locally adapted API agree exactly on topology strings,
segment boundaries, and protein types for both proteins:

- SPTLC2: interfacial helix at **72–87**, no predicted membrane-spanning helix.
- DPM1: interfacial helices at **160–175** and **246–259**, no predicted
  membrane-spanning helix.

Coordinates are one-based and inclusive. Both receive the software's coarse
`Globular` type and no membrane-type assignment: upstream code suppresses
membrane assignments for non-TM proteins even when interfacial segments are
present. Empty membrane assignments are therefore not evidence against ER
association. These predictions alone do not revise existing gene reviews.

The pinned Python API fails to unbatch `predict_single_model` outputs before
ensemble aggregation and segment parsing. Its original output gave both
proteins a single segment spanning residue 1 only; SPTLC2's interfacial
prediction was also lost through incorrect ensemble aggregation. The benchmark
option `--unbatch-api` unwraps the singleton topology and marginals before
postprocessing. No model or installed package was modified. The unmodified
CLI already performs the required unbatching and is the reference output.
Original API outputs in `results/api-unpatched-*` must not be interpreted
biologically. The successful adapted API runs supersede them.

## Verification and provenance

- [x] Scripts accept input/output paths rather than hardcoding proteins or results.
- [x] The same scripts were exercised on a second input, DPM1.
- [x] CLI and adapted API analyses completed successfully.
- [x] Direct outputs, timings, and process resource logs are retained in `results/`.
- [x] Repeat predictions agree; adapted API topologies and segments match the CLI.
- [x] Input sequence hashes, checkpoint hashes, hardware, versions, parameters,
  and source commit are recorded in the timing files and `results/provenance.json`.

Canonical sequences came from existing cached UniProt flat files, without
editing those sources. Dependencies are locked in `uv.lock`. Model checkpoints,
source checkout, and virtual environment are excluded from version control.
