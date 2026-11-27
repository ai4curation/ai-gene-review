# aigr-benchmark

Build, check, export and score time-split, leakage-checked benchmarks of protein
function annotations. A target is a GO annotation that is in a later GO release
and absent from a baseline release on or before a cutoff date. Deterministic
checks then test the targets for leakage, near-duplication and balance. Any
predictor (an LLM tool, a sequence tool, an agent review, a curator) answers
generic `Claim` records with generic `Prediction` records, and `score` tallies
them per condition, predictor, role and item.

This package was split out of
[ai-gene-review](https://github.com/ai4curation/ai-gene-review), where it is
developed as a uv workspace member (`packages/aigr-benchmark/`). It is
the code behind `ai-gene-review benchmark`, with only five small
dependencies (jsonschema, pydantic, PyYAML, requests, Typer).
The full guide is
[docs/benchmarks.md](https://github.com/ai4curation/ai-gene-review/blob/main/docs/benchmarks.md),
and a worked example is
[benchmarks/human-goa-2025-06](https://github.com/ai4curation/ai-gene-review/tree/main/benchmarks/human-goa-2025-06).

## Install

The package is not on PyPI yet. Install it from Git:

```bash
uv add "aigr-benchmark @ git+https://github.com/ai4curation/ai-gene-review@<commit>#subdirectory=packages/aigr-benchmark"
```

uv fetches only what it needs to build this subdirectory, but it still clones the
repository. Pin a commit for reproducibility.

## Command line

```bash
aigr-benchmark build    <id>-spec.yaml -o benchmarks/<id>    # draw items -> <id>.yaml
aigr-benchmark check    benchmarks/<id>/<id>.yaml             # -> <id>-check-report.{yaml,md}
aigr-benchmark export   benchmarks/<id>/<id>.yaml             # -> run-inputs/ (FASTA, claims, baseline GOA)
aigr-benchmark import   benchmarks/<id>/<id>.yaml runs/blind.jsonl --from peptalk -o predictions.jsonl
aigr-benchmark score    benchmarks/<id>/<id>.yaml -p predictions.jsonl
aigr-benchmark validate benchmarks/<id>/<id>.yaml --class Benchmark
```

`ai-gene-review benchmark <command>` is the same Typer app.

## Library

```python
from aigr_benchmark.checks import validate_schema, feature_label, uniprot_leakage
from aigr_benchmark.predictions import read_prediction_set, verdicts
from aigr_benchmark.run import score
from aigr_benchmark.datamodel.benchmark_model import Benchmark, Prediction
```

## Schema

The data model is a LinkML schema, `aigr_benchmark/schema/benchmark.yaml`. Two
files are generated from it and committed, and both ship in the wheel:

- `aigr_benchmark/schema/benchmark.schema.json`: a closed JSON Schema. `validate_schema`
  and `aigr-benchmark validate` use it, so validation needs no LinkML at run time.
- `aigr_benchmark/datamodel/benchmark_model.py`: a Pydantic model.

After editing the schema, regenerate both with `just gen-benchmark-models` from the
repository root. A test fails if either is stale.

## Releasing

Releases are tagged `aigr-benchmark-vX.Y.Z`, so they cannot collide with the
repository's own `vX.Y.Z` tags. `uv-dynamic-versioning` reads the version from that
tag. Creating a GitHub release with such a tag runs
`.github/workflows/aigr-benchmark-publish.yaml`, which builds this package and
publishes it to PyPI by trusted publishing. Before the first release, register the
`aigr-benchmark` project on PyPI with a trusted publisher: repository
`ai4curation/ai-gene-review`, that workflow, and environment `release`.
