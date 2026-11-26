# Conditions: export, run, score

1. Run `just benchmark-export benchmarks/<id>/<id>.yaml`. It writes `run-inputs/`,
   which is git-ignored:
   - `<id>.fasta`, with UniProt-style headers;
   - `<id>-claims.tsv`, with one `ask-function` claim per target, NOT target and decoy;
   - `baseline-goa/<ACC>-goa.tsv`, the baseline-release annotations used to seed
     agent-review runs.
2. Run peptalk once per context, the stub first:
   `peptalk ask run-inputs/<id>.fasta --claims run-inputs/<id>-claims.tsv --context blind --shuffle-control --provider stub > runs/blind.jsonl`.
   Ask the user before you rerun with a paid `-m <model>`. Use `--context organism`
   and `--context full` for the other two peptalk conditions.
3. For the agent-review condition, review each gene with its GOA file replaced
   by the exported baseline file, and keep the agent away from post-cutoff
   UniProt, QuickGO and PubMed. Existing repository reviews saw current GOA, so
   they do not count as an agent-review run.
4. Score with
   `just benchmark-score benchmarks/<id>/<id>.yaml --peptalk runs/blind.jsonl --peptalk runs/organism.jsonl --peptalk runs/full.jsonl --reviews-dir <seeded genes folder>`.
   The `ScoreReport` gives yes, no, uncertain and missing counts per condition
   and role (target, NOT target, decoy, shuffled), overall and per item.
