# thiF (P30138) notes, E. coli K-12

Deep research providers were not available in this session, so no `-deep-research-<provider>.md`
file was generated. This review is built from the UniProt record, the PTHR10953 PAINT table and
family review, the paralog review `genes/ECOLI/moeB`, and cached publications (mostly abstract-only).

## Identity

- UniProt P30138, sulfur carrier protein ThiS adenylyltransferase, EC 2.7.7.73 (RHEA:43344); b3992.
  HesA/MoeB/ThiF family, PANTHER PTHR10953:SF240; single ThiF (PF00899) domain, no rhodanese domain.

## Function

- ThiS adenylation [PMID:9632726 "ThiF catalyzes the adenylation by ATP of the carboxyl-terminal glycine of ThiS."].
- Sequence after adenylation [PMID:16388576 "ThiF catalyzes the adenylation of the carboxy terminus of ThiS and the subsequent displacement of AMP catalyzed by ThiI-persulfide to give a ThiS-ThiI acyl disulfide. Disulfide interchange, involving Cys184 on ThiF, then generates the ThiS-ThiF acyl disulfide, which functions as the sulfur donor for thiazole formation."].
- Cys184 conjugate is an acyl-disulfide, not a thioester [PMID:11438688 "This ThiF/ThiS conjugate is the first characterized example of a unique acyldisulfide intermediate in a biosynthetic system."]. C184S does not support growth.
- Structural zinc, homodimer (UniProt COFACTOR/SUBUNIT, PMID:15896804, PMID:16388576).
- thiF mutants need thiazole [PMID:8432721 "The thiE, thiF, thiG, and thiH gene products are required for synthesis of the thiazole."].

## GO term choice

- Local GO (go.db) has no term for EC 2.7.7.73 / ThiS adenylation. Children of GO:0070566
  adenylyltransferase activity include GO:0061605 (MoaD, EC 2.7.7.80) and GO:0070733 AMPylase
  (Ser/Thr/Tyr protein AMPylation), neither of which fits. Core MF = GO:0070566; proposed new term
  "sulfur carrier protein ThiS adenylyltransferase activity" (is_a GO:0070566).
- GO:0008641 requires an ATP-dependent thiolester: not met (adenylate + acyl-disulfide formed by
  disulfide interchange). REMOVE, consistent with moeB.
- AMPylase (IDA) -> MODIFY to GO:0070566 (mis-specified child).
- GO:1990228 sulfurtransferase complex (NAS) -> MARK_AS_OVER_ANNOTATED: sulfur transfer onto ThiS is
  by IscS/ThiI; ThiF-ThiS is the adenylyltransferase complex.

## PAINT reading (PTHR10953)

- PTN000102040: GO:0016779 (sound, general -> MODIFY GO:0070566); GO:0004792 seeded by Uba4 only
  (rhodanese domain -> REMOVE); GO:0005737 (MODIFY to cytosol).
- PTN000102608: GO:0005829 (ACCEPT); GO:0008146 seeded by MoeZ only (REMOVE).
- Actions mirror genes/ECOLI/moeB.
