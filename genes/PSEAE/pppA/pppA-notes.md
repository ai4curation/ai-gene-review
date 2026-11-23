# pppA (PA0075, Q9I757) review notes

## Literature

Search (Europe PMC REST, 2026-11-05: `TITLE:PppA AND aeruginosa`) returned
PMID:31208722 (crystal structure) and PMID:17085567 (an unrelated E. coli yghJ-pppA
prepilin peptidase gene, a symbol collision, not used). The PubMed search API was
returning errors that day.

1. Mougous et al. 2007 [PMID:17558395], abstract only (no PMC copy). PpkA is required for
   H1-T6SS assembly and Hcp1 secretion [PMID:17558395 "We show that a serine-threonine
   kinase, PpkA, is required for assembly of the H-T6SS and for secretion of Hcp1."];
   PppA antagonises it [PMID:17558395 "PpkA activity is antagonized by PppA, a Ser-Thr
   phosphatase."]; both act on Fha1.
2. Wu et al. 2019 [PMID:31208722], abstract only. 2.10 A crystal structure (PDB 6JKV):
   PPM core, flexible flap, two Mn ions [PMID:31208722 "PppA harbors a catalytic pocket
   containing two manganese ions"].
3. UniProt Q9I757: PPM-type phosphatase domain 8-241 (PROSITE PS51746), PANTHER PTHR13832
   (PP2C), Mn-binding residues from PDB 6JKV.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000352745 | GO:0004722 protein serine/threonine phosphatase activity | 35 | 1913 (121 taxa) | GO:0004722, IDA, PMID:17558395 (PseudoCAP) | SOUND | Abstract names PppA as the Ser-Thr phosphatase antagonising PpkA on Fha1; PPM fold and dinuclear Mn centre (PMID:31208722) fit the activity. Abstract-only reading, but no defect is claimed. | 34 others: yeast PTC1-7, S. pombe ptc1-4, Arabidopsis PP2Cs (ABI1-like etc.), human/mouse/rat PPM1 family, M. tuberculosis PstP (P9WHW5), Plasmodium, Dictyostelium, C. elegans FEM-2 | Yes; the node is overwhelmingly seeded by characterised PP2Cs. The node term suits a PP2C clade. No GO_CENTRAL defect. |

The signal transduction IBD at the same node is seeded by plant/mammalian PP2Cs, not by
PppA; it is appropriate for PppA as well.

## Annotation decisions

- GO:0004722 (IBA, IDA, IEA): ACCEPT; core.
- GO:0007165 IBA: ACCEPT (as precise as GO allows).
- GO:0046872 IEA: MODIFY to GO:0030145 manganese ion binding (structure).
- GO:0050709 IMP: ACCEPT; no T6SS-specific regulation term exists.
- ppkA (partner kinase) is reviewed in a later batch; check consistency there.
