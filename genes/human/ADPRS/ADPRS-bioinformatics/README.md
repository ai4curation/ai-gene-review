# ADPRS computed evidence

Two scripts. `verify_adprs_claims.py` is stdlib only; `audit_row_quotes.py` needs PyYAML.

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

## `audit_row_quotes.py` — the quote-relevance guard

```bash
uv run python audit_row_quotes.py            # audit ADPRS-ai-review.yaml
uv run python audit_row_quotes.py --self-test
```

The repo's reference validator checks that a `supporting_text` is a **verbatim substring**
of its cited paper. It does not check that the sentence is *about the row it sits under* —
so a mitochondrial-matrix quote under a `nucleus` row passes every automated gate while
supporting nothing. Nine such rows shipped in commit `aa019d486` and were caught in review.

This guard requires, per row, either a quote matching a topic pattern declared for that
GO id (or for its `proposed_replacement_terms`, since a MODIFY row's quote should support
the term it is moving *to*), or a `full_text_unavailable: true` marker **and** an explicit
limitation in `reason` — both halves, or the escape hatch becomes a bypass.

Break-test F runs it against the YAML at `aa019d486`, the version that actually shipped
the defect. What it cannot do is judge whether an on-topic sentence actually *entails* the
claim; that is a reading task, and the docstring says so.

Deliberate limitation, also stated inside the script and in `RESULTS.md`: the judgement
that `PMID:33769608` contains no poly(ADP-ribose) experiment is a reading of the full
text. What is mechanised is only that the sentence the review quotes is present verbatim
in the cached copy. A phrase-presence check cannot prove the absence of an experiment.
