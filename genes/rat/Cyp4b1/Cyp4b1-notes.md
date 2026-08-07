# Cyp4b1 review notes

## Evidence summary
- [UniProtKB:P15129] UniProt describes Cyp4b1 as a microsomal heme-thiolate monooxygenase oxidizing steroids, fatty acids, and xenobiotics.
- [PMID:2229008] The fetched GOA file uses this publication for specific Cyp4b1 monooxygenase/lipid oxidation activity.

## Curation decisions
- Specific catalytic activities and direct metabolic processes were accepted.
- Broad parent, localization, binding, and stimulus-response annotations were modified, kept non-core, or marked over-annotated according to support.

## 2026-08-07 compliance pass
- `core_functions` was a single entry keyed on the generic `GO:0004497 monooxygenase activity`. Split into two entries so the specific IDA-supported chemistry is not hidden behind the family parent:
  1. `GO:0140981 medium-chain fatty acid omega-hydroxylase activity` (IDA), `directly_involved_in` `GO:0019395 fatty acid oxidation` (IEA + ISS, previously accepted but absent from `core_functions`).
  2. `GO:0004497 monooxygenase activity` retained for the xenobiotic branch, `directly_involved_in` `GO:0006805` and `GO:0018879`.
  Both `GO:0140981` and the sibling `GO:0120503 medium-chain fatty acid omega-1 hydroxylase activity` were confirmed non-obsolete via OLS; labels used verbatim.
- `GO:0120503` (omega-1, IDA) is left out of `core_functions` because the schema allows one `molecular_function` per entry and the omega regiochemistry is the CYP4-defining activity. The omega vs omega-1 ratio for the *rat* enzyme is not established in the cached evidence — the ω/ω-1 ratios in the falcon report (23 for C7, 1.6 for C10) are **rabbit** CYP4B1 [file:rat/Cyp4b1/Cyp4b1-deep-research-falcon.md "n-alkane turnover from ~11 min−1 (C10) to ~33 min−1 (C7); ω/ω-1 ratio 23 for C7 and 1.6 for C10"]. Raised as suggested question 1 and experiment 1.
- Species caveat worth keeping in view: [file:rat/Cyp4b1/Cyp4b1-deep-research-falcon.md "native human CYP4B1 has <1% of rabbit 4-IPO activity"]. Rat-vs-rabbit equivalence is *not* established either, so the 4-IPO bioactivation claim in `core_functions` rests on the rat lung/liver microsome evidence, not on the rabbit kinetics.
- `description` rewritten to remove curation commentary per CLAUDE.md; `suggested_questions` and `suggested_experiments` added (both were absent).
