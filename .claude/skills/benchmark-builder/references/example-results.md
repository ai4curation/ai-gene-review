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
| homolog_leakage | 3 | 47 | 0 | 0 |
| near_duplicate | 33 | 15 | 2 | 0 |
| uniprot_leakage | 49 | 48 | 5 | 0 |
| reference_recency | 0 | 153 | 153 | 0 |
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
- **The same-species homolog check rarely applies.** Most human PANTHER
  subfamilies have one human member, so `homolog_leakage` could check only 3 of
  the 51 targets (the other 47 are INFO, not checked). Cross-species ortholog
  knowledge enters through IBA, ISS and ISO rows (`prior_prediction`).
- **The FULL header can give the answer away.** TGDS's name contains its target
  activity (`header_leakage`).

## Pipeline-test model run (2026-11-26)

These are `peptalk ask` runs on the 123 claims (50 targets, 1 NOT target, 72
decoys), with shuffled copies of each sequence in the blind conditions, all at
high effort. The scores are in `human-goa-2025-06-scores.{yaml,md}`; the raw
JSONL lives in the git-ignored `runs/`. Actual spend was $22.04 by peptalk's
log, canaries included: Fable 5.2 blind $12.79, Fable 5.2 organism $4.15, Opus
5.5 blind $3.11, Opus 5.5 organism $1.95. The calls were direct API calls. Batch
was not used because `peptalk batch submit` takes one parameter set for every
sequence, while each item here has its own claims.

| condition | targets yes | decoys yes | shuffled targets yes | NOT target yes |
|---|---|---|---|---|
| blind, Fable 5.2 | 32/50 | 1/72 | 4/50 (5 uncertain, 2 refused) | 1/1 |
| organism, Fable 5.2 | 31/50 (1 refused) | 1/72 | n/a | 1/1 |
| blind, Opus 5.5 | 28/50 (5 uncertain) | 3/72 (6 uncertain) | 0/50 (10 uncertain) | 1/1 |
| organism, Opus 5.5 | 28/50 (7 uncertain) | 6/72 (3 uncertain) | n/a | 1/1 |

**This is a pipeline test, not a fair evaluation.** Every target paper predates
the models' training cutoffs (all 51 targets WARN on `reference_recency` for
Opus 5.5; Fable 5.2's cutoff is not recorded). The blind reads may therefore
draw on recalled knowledge of the protein, which peptalk's blind read
explicitly allows. In the LRP4 canary, for example, the model said the
sequence "looks like LRP4". With 50 targets, the blind-versus-organism
differences (8 items change by one target) are within noise. Both models
answered yes to TGDS's one NOT target (dTDP-glucose 4,6-dehydratase activity).
The bio classifier refused five Fable calls. Four were on shuffled sequences:
two on target terms, which score as missing (the 2 refused above), and two on
decoy terms, which are not scored for shuffled sequences. The fifth was on an
organism-condition target (LRP4 virus receptor activity), which also scores
as missing. Opus refused none.

## Agent-review run (2026-11-26)

The AGENT_REVIEW condition was run on all 24 items with Opus 5.5 at high
effort, each gene in a sandbox holding only the baseline GOA, the UniProt entry
version of the baseline date and pre-baseline cached papers, for $14.33. It
found 10 of the 50 targets. A review must name a term unprompted, while the
peptalk runs are asked about each target, so compare the two with care. The
method, the leakage audit and the comparison table are in
`projects/SEQFUN_BENCHMARK.md`.
