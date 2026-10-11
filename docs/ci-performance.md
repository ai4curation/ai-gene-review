# CI validation performance

## Measurements (2026-10-11)

The successful [DANRE audit run](https://github.com/ai4curation/ai-gene-review/actions/runs/38122109159)
spent 28m55s executing, after roughly four hours queued. Its major steps were:

| Step | Time |
| --- | ---: |
| Family validation | 21m36s |
| Disk cleanup | 2m01s |
| Changed gene validation | 1m50s |
| Checkout | 1m49s |
| History validation and tests | 55s |
| Dependency installation | 9s |

The [CNOT1 run](https://github.com/ai4curation/ai-gene-review/actions/runs/38122081872)
showed the same pattern: family validation took 21m30s, while changed gene
validation took 21s. The ontology cache restored in 14s and PANTHER cache in 5s.
Downloads and dependency installation were not the dominant cost in these runs.

Every gene-review edit triggers the family checks because gene residue claims
and family assessments must agree. That coverage is intentional. Within the
DANRE run's family step, the schema phase took 6m21s and the term phase 14m36s:
each started a new validator process for each of 281 family reviews. Reference
validation was already batched; residue checks and cross-checks together took
about 20s.

## Changes

Following dismech's
[`validate-disorders` recipe](https://github.com/monarch-initiative/dismech/blob/main/project.justfile),
`validate-families` now runs one schema invocation and one term invocation over
all family files. `validate-modules` likewise batches its schema phase. Schema
generation, Python imports, and ontology initialization can be reused within
each process. All existing files, validation phases, and blocking exit statuses
are retained. Quoted Bash arrays preserve filenames containing spaces.

As in dismech's
[CI workflow](https://github.com/monarch-initiative/dismech/blob/main/.github/workflows/main.yaml),
the unconditional disk cleanup is replaced with a capacity report. Our sampled
runner already had 86 GB free before spending two minutes deleting SDKs and
Docker images. Revisit this if runner capacity or repository size changes.

Local checks on this checkout passed for all 283 family reviews (14.54s schema,
42.77s terms) and all 450 module schemas (12.33s). These are local timings, not
post-change GitHub runner measurements. Regression tests exercise failures in
each recipe phase and verify that the real schema and term validators reject an
invalid second file after a valid first file.

A same-machine comparison on the first ten sorted family reviews isolates the
batching effect (both modes passed with the same schema, flags, and inputs):

| Phase | One process per file | One batch |
| --- | ---: | ---: |
| Schema | 9.73s | 0.85s |
| Terms | 20.32s | 2.11s |

## Remaining opportunities

- Queue pressure is distinct from execution time. The separate
  [superseded-run cancellation PR #4883](https://github.com/ai4curation/ai-gene-review/pull/4883)
  addresses obsolete PR runs holding runners. Faster validation should also
  reduce queue occupancy.
- Changed gene validation still runs the external validators per gene through
  the CLI. Batching those phases would help large curation PRs, but must retain
  per-file diagnostics, reference preprocessing, and gene-specific checks.
- Infrastructure changes intentionally trigger full-corpus validation; ordinary
  review PR timings do not predict that cost.
- Checkout and repo-wide history checks remain measurable costs. Reassess them
  after observing the batched family phase in CI.

Dismech additionally uses cache-bound reference checks, offline term checks in
selected CI lanes, and cached generated JSON Schema for single-file validation.
Those policies were not copied here: the measured family bottleneck can be
removed without changing reference fetching or ontology freshness behavior.

To reproduce the family phase timings, run these separately under `time`:

```bash
uv run linkml-validate --schema src/ai_gene_review/schema/family_review.yaml \
  --target-class FamilyReview interpro/panther/PTHR*/PTHR*-review.yaml
uv run linkml-term-validator validate-data interpro/panther/PTHR*/PTHR*-review.yaml \
  -s src/ai_gene_review/schema/family_review.yaml -t FamilyReview \
  --labels -c conf/oak_config.yaml
```

For end-to-end timing, use `time just validate-families` with warm PANTHER and
UniProt caches, as in the sampled CI runs. Cold-cache network time is a separate
measurement.
