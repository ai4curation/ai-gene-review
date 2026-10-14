# guca1d notes (Danio rerio, guanylate cyclase activator 1d, zGCAP4; UniProt Q6ZM98)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 4, random TGD_tree sample)

**Deep research:** not available (Edison 402 Payment Required; OpenAI key invalid). Not attempted, per
instructions. Literature found by hand through Europe PMC; shared literature and name mapping in
`../guca1c/guca1c-notes.md`; pair analysis in `../guca1c/guca1c-bioinformatics/RESULTS.md`.

Accession Q6ZM98 (TrEMBL, 185 aa), ZFIN:ZDB-GENE-040724-231 (alias gcap4), Ensembl ENSDARG00000044629, chr21.

### Expression
- Cones, strongest in double and long single cones:
  [PMID:15486694 "The digoxigenin-labeled zGCAP4 antisense RNA probe hybridized specifically to the myoid region of double cones and long single cones protrude above the external limiting membrane."]
  [PMID:15486694 "Only minimal signal was observed in short single cones."]
- Retina-specific by RT-PCR: [PMID:15486694 "The results show that all GCAPs and GCIP are strongly expressed in the zebrafish retina, while other tissues (except brain) did not express detectable levels, similarly to observations in human ( Subbaraya et al. 1994 )."]
- Onset 3-4 dpf with zGCAP3 and zGCAP7 (PMID:19168097).
- Adult scRNA-seq reanalysis: in 80-98% of cones of each type, 3.5-6.8 CP10K (lowest in UV cones), about a tenth
  of guca1c; rod signal at ambient level.

### Function
- [PMID:18777180 "zGCAP4 was a strong activator of membrane-bound guanylate cyclases from bovine and zebrafish retina, showing half-maximal activation at 520-570 nM free Ca(2+) concentration."]
- Low-sensitivity group with zGCAP5 and zGCAP7 (PMID:21829700, IC50 about 400 nM vs about 30 nM for zGCAP3).
- No mutant or morphant data for guca1d.

### Annotation decisions
- All Ca2+ binding rows and all GO:0008048 rows ACCEPT; GO:0009966 KEEP_AS_NON_CORE (deep NCS node, very general).
