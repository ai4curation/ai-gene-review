# Agentic steps (frontier models only)

Both steps call for judgement about biology and evidence. Run them only on a
frontier model (Claude Opus or Fable class). On a smaller model, do the
deterministic steps and report that these steps were skipped.

## Review-derived build

1. Draw candidates with a `GOA_TIME_SPLIT` build whose `size` is larger than
   needed.
2. Review each candidate gene with the normal workflow: `just fetch-gene`, deep
   research, and the `review` skill. Keep within the six-workstream limit in
   `CLAUDE.md`, with one PR per gene review.
3. Set `mode: REVIEW_DERIVED` and run
   `uv run ai-gene-review benchmark build <spec> -o benchmarks/<id> --reviews genes/<org>/<G>/<G>-ai-review.yaml ...`.
   The targets are the reviews' ACCEPT and NEW rows that are also absent from the
   baseline release.
4. Run the check as usual.

## Agent evaluation

1. Read the benchmark and its check report. Prefer an agent that did not build
   the benchmark. If yours did, say so in `evaluator`.
2. Write `benchmarks/<id>/<id>-agent-evaluation.yaml` (class `AgentEvaluation`).
   Each finding needs a `category`, a `severity`, an `explanation` and a
   `proposed_check`: a deterministic test that would confirm the finding.
3. If you could have settled an objection by running a check, run the check
   instead of writing the objection down. Text-only judgement barely separates
   flawed items from sound ones.
4. When a finding shows that the code lacks a check, say so in the PR. Do not
   patch targets by hand.

The example is `benchmarks/human-goa-2025-06/human-goa-2025-06-agent-evaluation.yaml`.
