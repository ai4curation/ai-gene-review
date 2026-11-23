# ggt1 (SPAC664.09, UniProt Q9US04) – notes

Gamma-glutamyl transpeptidase I; paralog of ggt2. Module: vacuolar GGT variant in `glutathione_synthesis_gamma_glutamyl_cycle`. S. cerevisiae ortholog ECM38/CIS2 (review: genes/yeast/ECM38).

## Evidence
- Activity: [PMID:15052323 "The S. pombe cells harboring the cloned GGT gene showed about twofold higher GGT activity in the exponential phase than the cells harboring the vector only, indicating that the cloned GGT gene was functional."] (abstract only).
- Induction by SN/BSO via Pap1 [PMID:15052323 "Involvement of Pap1 in the induction of the GGT gene by SN and BSO was observed."]; by nitrogen starvation and non-fermentable carbon, Pap1-independent [PMID:15765057 "Nitrogen starvation also gave rise to induction of GGTI gene expression in a Pap1-independent manner."].
- Type II membrane protein, TM 50-70, proenzyme autocleaved at Thr441 (by similarity) [UniProt:Q9US04].
- Location: ORFeome HDA = ER [PMID:16823372]; UniProt ER membrane (ECO:0000305) derives from this. No vacuolar data for Ggt1 itself; Ggt2 is vacuolar (HDA) and Ecm38 is vacuolar-membrane [PMID:11672438 "is a glycoprotein that is bound to the vacuolar membrane."]. Core location set to fungal-type vacuole by family inference; ER flagged as possible transit/overexpression artefact.

## Decisions
- Plasma membrane IBA removed (animal cell-surface node; same as ECM38 review).
- GO-CAM 68b0f0d000008341: ggt1 enables GO:0036374, no occurs_in. Consistent.
