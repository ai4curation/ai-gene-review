# RDR2 review notes

## Session 1 (create review)
- fetch-gene resolved O82504 (Swiss-Prot RDR2_ARATH, TAIR AT4G11130, GeneID 826714) as expected.
- 25 GOA rows. Full text read for PMID:34903670, 23142082 (added, cited by UniProt), 15024409, 17785412,
  22242006, 22302148, 22772985. Abstract only: PMID:34941388 (Science), 16839878 (Cell), 26119694.
- PMID:22772985 (IBM1) concerns epigenetic control of RDR2 expression; it is not the source of any GOA row
  and gives only background on RDR2 function [PMID:22772985 "RDR2 is responsible for the production of
  dsRNA precursors from single-stranded RNA transcripts"].
- Core MF: RNA-directed RNA polymerase activity (recombinant enzyme active alone [PMID:34903670]). RDR2 has
  its own catalytic Asp triad, so the MF goes in molecular_function, not contributes_to.
- Rhea-derived 5'-3' RNA polymerase activity row is a true parent of GO:0003968 (checked with OAK) -> MODIFY.
- ARBA GO:0031047 -> MODIFY to GO:0080188 (gene silencing by siRNA-directed DNA methylation; checked is a
  descendant). Comparator check: other siRNA-biogenesis-phase RdDM proteins (NRPD2, CLSY2-4, FDM2-5)
  carry GO:0080188; DCL3 does not. RDR2 performs the dsRNA-synthesis step of the siRNA-biogenesis phase,
  which GO:0080188's definition names as part of the process.
- DNA/RNA hybrid binding: PMID:34903670 measures transcription of partially hybridized RNA, not hybrid
  binding; fully paired hybrids are not used. MARK_AS_OVER_ANNOTATED.
- GO:0010495 IMP from PMID:34941388 (abstract-only structural paper) cannot be checked; the claim itself is
  supported by PMID:17785412, so both rows kept as non-core.
- Open question: UniProt MISCELLANEOUS "RDR2 is non-functional in the absence of associated Pol IV"
  (PMID:23142082) vs recombinant RDR2 activity on ssRNA in PMID:34903670 - likely template-specific
  (bipartite Pol IV template) rather than a contradiction; raised as a suggested question.
