# ADPRS computed evidence

One script, stdlib only, no third-party dependencies.

```bash
uv run python verify_adprs_claims.py --fetch      # query APIs -> results.json + RESULTS.md
uv run python verify_adprs_claims.py --render     # results.json -> RESULTS.md
uv run python verify_adprs_claims.py --check      # assert RESULTS.md reproduces (gate this)
uv run python verify_adprs_claims.py --self-test  # break-test the guards
```

`RESULTS.md` is generated from `results.json`; do not hand-edit it. `--check` exits
non-zero if the two disagree, so a hand-edit to the report is caught rather than silently
reverted on the next run.

What it recomputes, and which claim in `ADPRS-ai-review.yaml` each supports:

| section | supports |
|---|---|
| 1. PANTHER node reach, fully paginated | the `NO_FAILURE_CORE` propagation reviews on all six IBA rows, and the non-confirmation of a paralog-specificity leak |
| 2. `GO:0071451` vs `GO:0070301` | the three `MODIFY` actions on `cellular response to superoxide` |
| 3. cell-death term definitions | the two `MODIFY` actions on `GO:0060546` |
| 4. Reactome compartments and containment | `MARK_AS_OVER_ANNOTATED` on `GO:0006287`, and `ACCEPT` on the two `R-HSA-8952903` rows |
| 5. GO branch placement of the ADP-ribosyl hydrolases | the ontology question in `suggested_questions` |
| 6. IntAct HuRI records and partner promiscuity | `MARK_AS_OVER_ANNOTATED` on both `GO:0005515` rows |
| 7. retraction/erratum scan | the `reference_review` notes on `PMID:30045870` and `PMID:30100084` |

Deliberate limitation, also stated inside the script and in `RESULTS.md`: the judgement
that `PMID:33769608` contains no poly(ADP-ribose) experiment is a reading of the full
text. What is mechanised is only that the sentence the review quotes is present verbatim
in the cached copy. A phrase-presence check cannot prove the absence of an experiment.
