# Worked example: `benchmarks/human-goa-2025-06/`

The example has 24 human proteins, 51 targets and 72 decoys. Its baseline is the
2025-06-01 GO release and its current release is 2026-08-05. For the 20
main-draw items, every supporting paper was published on or after 2025-06-01.
The four pseudoenzyme items use their own paper floor of 2023-01-01. The full report is
`human-goa-2025-06-check-report.md`.

| check | pass | info | warn | fail |
|---|---|---|---|---|
| novelty | 51 | 0 | 0 | 0 |
| present_in_current | 51 | 0 | 0 | 0 |
| date_window | 45 | 0 | 6 | 0 |
| prior_prediction | 43 | 0 | 7 | 0 |
| homolog_leakage | 44 | 6 | 0 | 0 |
| near_duplicate | 33 | 15 | 2 | 0 |
| uniprot_leakage | 49 | 48 | 5 | 0 |
| reference_recency | 0 | 153 | 51 | 0 |
| header_leakage | 45 | 0 | 6 | 0 |
| decoy | 72 | 0 | 0 | 0 |
| review_agreement | 12 | 6 | 0 | 0 |
| feature_label | 3 | 0 | 1 | 0 |
| balance | 0 | 0 | 1 | 0 |

## What it taught

- **GAF dates are re-stamped** (an IPI from a 2021 paper is dated 20260725).
  Newness comes from absence in the baseline release, never from the date.
- **About 15,000 IDA rows became EXP** between the two releases, so novelty is
  keyed on the term, not the evidence code.
- **New to GO is not new knowledge.** 10,771 rows on 4,420 proteins were new to GO.
  393 rows on 182 proteins rest wholly on papers from 2025-06 or later, and 10 rows
  on 6 proteins on papers from 2026-06 or later. All 51 targets therefore predate the
  June 2026 cutoff of the agent-review model. The example is a pipeline test, not
  a fair test of that model.
- **UniProt-query labels are not literature checks.** ULK4 and PLD5 are genuine
  pseudoenzymes. WHR1 (formerly STK19) qualifies only through an AltName. KLK11,
  an active protease, matched only through its cleavage-chain names and is
  wrong; `feature_label` flags it. An earlier draw had SMARCA1, which matched
  only on isoform-2 text.
- **One paper can tie items together.** PMID:40446798 supplies 10 targets to
  three items (`balance` WARN).
- **The FULL header can give the answer away.** TGDS's name contains its target
  activity (`header_leakage`).
