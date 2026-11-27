# Conditions and predictors: export, run, import, score

A condition is what a predictor may see (BLIND, ORGANISM, FULL, AGENT_REVIEW).
A predictor is whatever answers: an LLM tool, a sequence tool, an agent review,
a curator. Scoring reads only generic `Prediction` records.

1. Run `just benchmark-export benchmarks/<id>/<id>.yaml`. It writes `run-inputs/`,
   which is git-ignored:
   - `<id>.fasta`, with UniProt-style headers (a runner withholds the header for
     BLIND and keeps only OS=/OX= for ORGANISM);
   - `<id>-claims.yaml`, a `ClaimSet`: one claim per target, NOT target and decoy,
     without its role;
   - `baseline-goa/<ACC>-goa.tsv`, the baseline-release annotations used to seed
     agent-review runs.
   Add `--for peptalk` to also write the claims as a `peptalk ask` TSV.
2. Run each predictor under each condition the spec lists. Ask the user before
   any paid model call, and test with a free or stub mode first. For example,
   with peptalk (one example LLM predictor):
   `peptalk ask run-inputs/<id>.fasta --claims run-inputs/<id>-claims.peptalk.tsv --context blind --shuffle-control --provider stub -o runs/blind.jsonl`.
3. For the agent-review condition, review each gene with its GOA file replaced
   by the exported baseline file, and keep the agent away from post-cutoff
   UniProt, QuickGO and PubMed. Existing repository reviews saw current GOA, so
   they do not count as an agent-review run.
4. Convert each native output to predictions with an importer, or have the
   predictor write `Prediction` records itself:
   `just benchmark-import benchmarks/<id>/<id>.yaml runs/blind.jsonl --from peptalk -o benchmarks/<id>/predictions/blind-peptalk-<model>.jsonl`
   `just benchmark-import benchmarks/<id>/<id>.yaml <seeded genes folder> --from reviews --condition agent-review --predictor ai-gene-review:<model> --model <model> -o benchmarks/<id>/predictions/agent-review-<model>.jsonl`
   A new tool needs only a small module in `packages/aigr-benchmark/src/aigr_benchmark/importers/`.
5. Score all prediction files together:
   `just benchmark-score benchmarks/<id>/<id>.yaml -p benchmarks/<id>/predictions/<file> -p ...`
   (add `--threshold` for predictors that give scores without verdicts).
   The `ScoreReport` gives yes, no, uncertain and missing counts per condition,
   predictor and role (target, NOT target, decoy, shuffled), overall and per item.
   Commit the prediction files and the score report; never commit `runs/`.
