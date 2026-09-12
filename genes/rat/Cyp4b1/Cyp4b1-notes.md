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
- `GO:0120503` (omega-1, IDA) was initially left out of `core_functions` on the grounds that the rat regiochemistry was unestablished. **That rationale was wrong and has been corrected** (PR #2377 review): the rat abstract states *both* activities are high — [PMID:2229008 "P450 L-2 had high lauric acid omega- and (omega-1)-hydroxylation activities, but low prostaglandin A1 omega- and (omega-1)-hydroxylation activities."]. Two equally IDA-supported, equally specific sibling activities should not have one promoted over the other, so `GO:0120503` now has its own `core_functions` entry alongside `GO:0140981`.
- What genuinely *is* unestablished for rat is the **relative** contribution of the two regiochemistries. The ω/ω-1 ratios in the falcon report (23 for C7, 1.6 for C10) are **rabbit** CYP4B1 [file:rat/Cyp4b1/Cyp4b1-deep-research-falcon.md "n-alkane turnover from ~11 min−1 (C10) to ~33 min−1 (C7); ω/ω-1 ratio 23 for C7 and 1.6 for C10"], and the chain-length-dependence clause has been dropped from the rat `core_functions` description. Suggested question 1 and experiment 1 are scoped to the ratio, not to whether both occur.
- Species scope in `description` tightened: medium-chain fatty acid ω/ω-1 hydroxylation is rat-demonstrated (PMID:2229008), whereas fatty alcohol and n-alkane hydroxylation is family/rabbit evidence, explicitly labelled "Mostly non-rat evidence" in the falcon report [file:rat/Cyp4b1/Cyp4b1-deep-research-falcon.md "Rabbit CYP4B1 hydroxylates medium-chain fatty acids, n-alkanes, and fatty alcohols"]. The YAML now attributes it to the rabbit orthologue rather than to the rat enzyme.
- The two IDA `existing_annotations` (`GO:0120503`, `GO:0140981`) previously quoted the purification sentence of PMID:2229008, which establishes the protein but not the activity. Both now quote the activity sentence, as does `core_functions`.
- `GO:0120502 fatty acid omega-1 hydroxylase activity` (IEA, GO_REF:0000116) changed `ACCEPT` → `MODIFY` with replacement `GO:0120503`. It is the over-general parent of a term the same record already carries by IDA, and its previous supporting text was rabbit-derived; this now matches how the other over-general parent in this file (`GO:0016705`) was handled.
- OLS pass on the xenobiotic branch MF (review suggestion 5): searched GO for `arylamine N-hydroxylase activity` and `amine N-hydroxylase` — no such term exists (hits are unrelated specific monooxygenases such as GO:0018670, GO:0019135, GO:0004500). `GO:0004497 monooxygenase activity` is therefore retained for that entry as the closest non-invented term.
- Species caveat worth keeping in view: [file:rat/Cyp4b1/Cyp4b1-deep-research-falcon.md "native human CYP4B1 has <1% of rabbit 4-IPO activity"]. Rat-vs-rabbit equivalence is *not* established either, so the 4-IPO bioactivation claim in `core_functions` rests on the rat lung/liver microsome evidence, not on the rabbit kinetics.
- `description` rewritten to remove curation commentary per CLAUDE.md; `suggested_questions` and `suggested_experiments` added (both were absent).
