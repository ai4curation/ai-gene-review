# PA5498 (ZnuA, Q9HT75) review notes

No deep-research provider was available. Sources: UniProt Q9HT75 (unreviewed), cached PMID:26290475
(full text), PMID:24086521 (full text), PMID:9680209 (abstract).

## Function

- High-affinity zinc solute-binding protein of ZnuABC [PMID:26290475 "ZnuA is the high affinity, zinc-specific binding protein"].
- Delta-znuA: [PMID:26290475 "Metal accumulation analyses revealed a significant 59.6% decrease in cellular Zn2+ due to loss of the SBP"].
- Binding: [PMID:26290475 "titration with increasing concentrations of ZnuA revealed a KD for Zn2+ of 22.6 ± 6.4 nM"].
- Growth under zinc depletion: [PMID:24086521 "the inability to express the putative znuA, znuB, or znuC genes resulted in decreased growth at 18 hours"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000767207 | GO:0006829 zinc ion transport | 2 | 24 (20 taxa) | GO:0006829, IMP, PMID:26290475 (PseudoCAP) | SOUND | Full text: ICP-MS shows a 60% zinc loss in Delta-znuA with other metals unchanged, and purified ZnuA binds zinc at nM affinity; the binding protein is a working part of the importer. Node term suits a ZnuA clade. | E. coli ZnuA (P39172; Patzer & Hantke 1998) | Yes. No defect. |

The rows on this gene for zinc ion transport are marked TOO_GENERAL only because zinc ion
transmembrane transport (GO:0071577) is accepted; the claim itself is sound.

Non-seed PseudoCAP rows with defects: ISS GO:0000006 (enables a transmembrane transporter activity;
should be contributes_to GO:0015633, WRONG_QUALIFIER, PROBABLE) and IMP GO:0010043 response to zinc ion
(indirect growth phenotype; DELETE_ROW, PROBABLE).

## Consistency with np20 (Zur)

np20 (PA5499) represses znuA; its review's nodes (PTN002112386, PTN002112441) are not shared with
PA5498. No node-level coordination needed.
