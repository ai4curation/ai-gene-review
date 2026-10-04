# ANKRA2 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKRA2 (Q9H9E1) is an ankyrin-repeat reader of PxLPxI/L motifs (crystal structures, PMID:22649097). Partners: class IIa HDACs, megalin (PMID:11095640), RFX5/RFX7 (PMID:31864703), and CCDC8 of the 3M complex (PMID:25752541).
- **NEW GO:0003714 transcription corepressor activity** (ISS, PMID:17949687, mouse MEFs).
  - ANKRA2 knockdown relieves AhRR repression, and AhRR/Arnt recruits ANKRA2, HDAC4 and HDAC5 to the CYP1A1 promoter.
  - Participation: ANKRA2 bridges the repressor to the HDACs via the motif reader. This is also the core MF.
- **IPIs:**
  - HDAC4 and HDAC5 (×3) → MODIFY to histone deacetylase binding.
  - RFX7 (×2) → MODIFY to GO:0061629 Pol II-specific DNA-binding TF binding.
  - CCDC8, TSHZ3, SAMD4A → REMOVE.
- **Kept as non-core:** NEK6 kinase binding, ubiquitin ligase binding and 3M complex (via CCDC8), complex assembly, generic protein-containing complex, plasma membrane (HPA), cytoskeleton (SubCell).
- **Accepted:** HDAC binding, megalin (LDL receptor) binding, regulation of gene expression (IBA), and nucleus, cytoplasm, cytosol and membrane locations.
- **PAINT:** PTHR24124 has 2 annotated PTN nodes. The nucleus and regulation-of-gene-expression IBAs come from PTN001538048 (Eukaryota), seeded by RFXANK and mouse genes. Family files committed.
