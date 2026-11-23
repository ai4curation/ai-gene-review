# mcrA (Q58256, MCRA_METJA) — Methanocaldococcus jannaschii MCR alpha

Part of the cross-clade MCR review (`projects/ARCHAEA/mcrA-across-clades.md`);
Methanococcales representative.

## Literature search

No deep-research provider key is configured (checked 2026-11-13); hand-written notes.
PubMed searched for "methyl coenzyme M reductase Methanocaldococcus jannaschii": the
hits are YcaO/TfuA thioamidation studies (PMID:29507203, 31139720, 33707784), sulfite
reductase and physiology papers. No purification or assay of M. jannaschii MCR was found.

## Evidence

- Autotrophic methanogen [PMID:8688087 "an autotrophic archaeon, Methanococcus
  jannaschii"]; converts H2/CO2 to methane at high rates [PMID:33674723 "Methanocaldococcoccus
  jannaschii are high-pressure CH4 cell factories"] (source spelling).
- Methanococcales MCR structures (other species) have virtually identical active sites
  [PMID:28559298 "virtually identical active site architectures"].
- Residue comparison (`projects/ARCHAEA/mcrA-across-clades/RESULTS.md`): all 13 reference
  positions of P11558 conserved; F430 axial ligand is Gln150.

## Review decisions (2026-11-13)

- IEA/ISS GO:0050524 and cytoplasm: ACCEPT.
- GO:0015948 -> MODIFY GO:0019386.
- NEW (ISS from P11558): GO:0044674 complex, GO:0046906 tetrapyrrole binding.
- Open: which MCR type (Wagner 2017 scheme) McrA and MrtA (MJ0083) belong to.

## 2026-11-23: merge with the round 5 review (PR #6211)

This gene was reviewed twice in parallel: in ARCHAEA round 5 (PR #6211) and in the
cross-clade review above (PR #6335, merged first). Both reached the same decisions on
every GOA row and on the core function; the cross-clade version also adds tetrapyrrole
binding, so it is kept as the review. One item only the round 5 review had is carried
over: the UniProt source defect asking for MOD_RES 448 thioglycine on Q58256, with its
two references (PMID:31139720, the YcaO thioamidation of the MjMcrA peptide at Gly448;
PMID:17725644, the thioxo peptide bond in MCRs of all methanogens examined).
