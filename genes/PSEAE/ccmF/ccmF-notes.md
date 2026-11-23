# ccmF (PA1480, Q9I3N2) notes

## Literature (own research, 2026-11-05)

- System I cytochrome c maturation: CcmF with CcmH is the heme lyase; CcmF accepts heme from holo-CcmE [PMID:19629033 "Given the published interaction of holoCcmE with CcmF"]. E. coli CcmF is a b-type cytochrome and quinol:heme oxidoreductase [PMID:19629033 "CcmF, shown to have 13 TMDs, is therefore a cytochrome b , and we show that it acts in vitro as a quinol:haem oxidoreductase"]; [PMID:19629033 "A completely conserved histidine in TMD5 of CcmF is an axial ligand to this haem"].
- P. aeruginosa ccmF insertion mutant: milder pleiotropic phenotypes than ccmC [PMID:18174132 "The ccmC mutant, and to a lesser extent the ccmF mutant, showed a range of other phenotypic changes."]; reduced [Fe-S] clusters in both.
- All five PseudoCAP IMP rows (pyoverdine, catalase, twitching, swimming, swarming) cite PMID:16824107 (Feissner et al. 2006, CcmABC/holo-CcmE release; abstract does not mention CcmF). Same mis-keying as on ccmC (genes/PSEAE/ccmC); re-key to PMID:18174132, PROBABLE (abstract-only).
- Treatment follows the ccmC review: catalase REMOVE (CONFIRMED WRONG_TERM), pyoverdine and swimming MARK_AS_OVER_ANNOTATED, twitching and swarming REMOVE (PROBABLE).
- PMID:16824107 and PMID:18174132 are abstract-only; full text not retrievable this session.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN009171456 | GO:0016491 oxidoreductase activity | 2 | 67 (36 taxa) | GO:0004096 catalase activity, IMP, PMID:16824107 | INDIRECT-PHENOTYPE | Loss of catalase activity in a cytochrome c maturation mutant reflects heme supply to the heme catalases; CcmF is not a catalase. Also keyed to the wrong paper. | E. coli CcmF P33927 (GO:0016679 quinol:heme oxidoreductase, IDA PMID:19629033) | Yes; the E. coli seed directly supports an oxidoreductase activity, which is correct for CcmF |

PseudoCAP defects: WRONG_TERM (catalase, CONFIRMED), WRONG_TERM (twitching, swarming; PROBABLE), WRONG_REFERENCE REPOINT PMID:16824107 -> PMID:18174132 (PROBABLE), WRONG_REFERENCE CHECK on swimming (SUSPECTED). No GO_CENTRAL defect: the IBD is right for the clade for a different reason than its PseudoCAP seed. The IBA row is MODIFIED to GO:0016679 for granularity. The ccmC plasma-membrane node (PTN000768541) is unaffected.

## Action counts

ACCEPT 3, MODIFY 3, KEEP_AS_NON_CORE 1, MARK_AS_OVER_ANNOTATED 3, REMOVE 4.
