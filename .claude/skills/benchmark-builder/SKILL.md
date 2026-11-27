---
name: benchmark-builder
description: >
  Build, check, export or score a time-split, leakage-checked benchmark of
  protein function annotations (GO terms with evidence, reference, date,
  provenance, split and difficulty). Use when someone asks for "protein
  annotations for a benchmark" with constraints such as species, recency window,
  GO aspect or branch, evidence types, size, or pseudoenzymes and other
  catalytically dead paralogs, or wants to compare a blind sequence-only read
  with organism, full-header and agent-review conditions. Do not use for
  reviewing one gene's annotations (use review) or for judging one prediction
  file (use review-function-prediction).
compatibility: >
  The deterministic steps (spec, build, check, export, score) run on any model
  with Bash and network access to release.geneontology.org, rest.uniprot.org and
  eutils.ncbi.nlm.nih.gov. The agentic steps (REVIEW_DERIVED builds and agent
  evaluation) need a frontier model (Claude Opus or Fable class).
metadata:
  short-description: Time-split GO annotation benchmarks with leakage checks
  agentic-steps: frontier-models-only
---

# Benchmark builder

When this skill is invoked, build the benchmark the user asked for, with the
deterministic steps below. Do the agentic steps only when the user asks for them.

## When to use, and when not

- **Use** to make a new benchmark, to extend or recheck one under `benchmarks/`,
  to export inputs for a condition run, or to score condition results.
- **Do not use** to review a gene (use `review`), to judge one set of
  predictions (use `review-function-prediction`), or to run paid model calls
  without the user's go-ahead.

## Steps

1. **Write the spec.** Copy `benchmarks/human-goa-2025-06/human-goa-2025-06-spec.yaml`
   to `benchmarks/<id>/<id>-spec.yaml` and change only what the request fixes.
   Choose the releases, the cutoff and `min_reference_date` as described in
   [references/spec-choices.md](references/spec-choices.md). Tell the user each
   choice. Never guess a model's training cutoff: leave it out instead.
   Validate the spec with
   `uv run ai-gene-review benchmark validate <spec> --class BenchmarkSpec`.
2. **Build.** Run `just benchmark-build benchmarks/<id>/<id>-spec.yaml`. If the
   draw comes up short of the requested size or feature quota, report the counts.
   Do not widen the window or the query without asking. Never hand-edit drawn
   targets: change the spec and rebuild.
3. **Check.** Run `just benchmark-check benchmarks/<id>/<id>.yaml`. Any FAIL must be
   fixed, by changing the spec, before you go on. Report the summary table, the
   `reference_recency` counts per condition (which models the benchmark is fair
   for), `feature_label` warnings, reference concentration, and the difficulty mix.
4. **Agentic steps, only if asked** (frontier models only; otherwise stop and
   say so): a review-derived build, and an agent evaluation. Follow
   [references/agentic-steps.md](references/agentic-steps.md).
5. **Export and score, only if asked.** Follow
   [references/conditions-and-scoring.md](references/conditions-and-scoring.md).
   Ask before any paid model call, and test with `--provider stub` first.
6. **Deliver.** Run `just validate-benchmarks` and `uv run pytest tests/test_benchmark.py`.
   Commit the spec, the benchmark, the check report and any agent evaluation.
   Never commit `run-inputs/`, `runs/` or `.cache/benchmark/`. In the PR, state
   the purpose (blind versus combined reasoning, per item), the counts that limited
   the draw, and the models the benchmark is and is not fair for.

## Addenda

- [references/spec-choices.md](references/spec-choices.md): how to set each spec field.
- [references/agentic-steps.md](references/agentic-steps.md): the review-derived build and agent evaluation.
- [references/conditions-and-scoring.md](references/conditions-and-scoring.md): export, peptalk runs and scoring.
- [references/example-results.md](references/example-results.md): the worked example's check report and what it taught.
- [docs/benchmarks.md](../../../docs/benchmarks.md): design rationale, the full list of checks, related practice (CAFA, fs2f, "A Society of AI Scientists") and limits.
