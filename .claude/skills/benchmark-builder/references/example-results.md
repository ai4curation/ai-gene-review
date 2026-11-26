# Worked example: `benchmarks/human-goa-2025-06/`

The example has 24 human proteins, 68 targets and 72 decoys. Its baseline is the
2025-06-01 GO release, its current release is 2026-08-05, and every target paper
was published on or after 2025-06-01. Four items are pseudoenzymes, drawn with
their own paper floor of 2023-01-01. The full report is
`human-goa-2025-06-check-report.md`.

| check | pass/info | warn | fail |
|---|---|---|---|
| novelty | 68 | 0 | 0 |
| present_in_current | 68 | 0 | 0 |
| date_window | 62 | 6 | 0 |
| prior_prediction | 59 | 8 | 0 |
| homolog_leakage | 66 | 1 | 0 |
| near_duplicate | 63 | 4 | 0 |
| uniprot_leakage | 125 | 11 | 0 |
| reference_recency | 204 | 68 | 0 |
| header_leakage | 63 | 5 | 0 |
| decoy | 72 | 0 | 0 |
| review_agreement | 12 | 0 | 0 |
| feature_label | 3 | 1 | 0 |
| balance | 1 | 0 | 0 |

## What it taught

- **GAF dates are re-stamped** (an IPI from a 2021 paper is dated 20260725).
  Newness comes from absence in the baseline release, never from the date.
- **About 15,000 IDA rows became EXP** between the two releases, so novelty is
  keyed on the term, not the evidence code.
- **New to GO is not new knowledge.** 10,771 rows on 4,420 proteins were new to GO.
  476 rows on 202 proteins rest on papers from 2025-06 or later, and 11 rows on 7
  proteins on papers from 2026-06 or later. All 68 targets therefore predate the
  June 2026 cutoff of the agent-review model. The example is a pipeline test, not
  a fair test of that model.
- **UniProt-query labels are not literature checks.** ULK4 and PLD5 are genuine
  pseudoenzymes. WHR1 (formerly STK19) qualifies only through an AltName. SMARCA1
  matched only on isoform-2 text and is wrong; `feature_label` flags it.
- **The FULL header can give the answer away.** TGDS's name contains its target
  activity (`header_leakage`).
