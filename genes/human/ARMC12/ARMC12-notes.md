# ARMC12 review notes

## Sources
- Affinage: trust gates clear. Checked against:
  - PMID:33536340 (mouse Armc12, full text): peripheral mitochondrial membrane adherence factor; VDAC2/3 with TBC1D21.
  - PMID:35534203 (human biallelic loss, abstract): absent mitochondrial sheath.
  - PMID:30026490 (neuroblastoma, full text): nuclear, RBBP4/PRC2.
- The nucleus IBA node PTN001438055 is seeded only by human ARMC12's own neuroblastoma IDA.

## Decisions
- ACCEPT:
  - Mitochondrial outer membrane (IEA, ISS) and mitochondrion (IDA, HPA).
  - Sperm mitochondrial sheath assembly (IMP human; IEA/ISS mouse).
- KEEP_AS_NON_CORE:
  - Nucleus (IBA, IEA, IDA, HDA): tumour and sperm-nucleus proteome.
  - Flagellated sperm motility, which is secondary to the sheath defect.
  - Positive regulation of cell growth (neuroblastoma).
- REMOVE: RBBP4, SUZ12 and EZH2 protein binding (policy).
- NEW: protein-macromolecule adaptor activity (ISO from mouse) for VDAC2/3-mediated mitochondrial linking.
