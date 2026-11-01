# Pck2 (rat) review notes

## 2026-10-28 session

- `just fetch-gene rat Pck2` resolved UniProt F1LQJ7, not the requested B2RYG2. Both entries are
  Pck2, RGD:1311112 (B2RYG2 also lists GeneID 361042); GOA (34 rows) is keyed to F1LQJ7, and B2RYG2 is
  an MGC cDNA fragment. Reviewed F1LQJ7.
- No deep-research provider; literature notes in Pck2-deep-research-manual.md.
- Key paper PMID:19635791 (Stark et al. 2009, full text) read: PEPCK-M is the only PEPCK in rat
  INS-1 832/13 cells and islets, mitochondrial (GDH-controlled fractionation), contributes 30-41% of
  PEP, and its siRNA knockdown abolishes GSIS [PMID:19635791 "Silencing the PEPCK-M gene completely inhibited GSIS underscoring its central role in mitochondrial metabolism-mediated insulin secretion."].
- Added PMID:24497630 (rat ASO knockdown, gluconeogenesis), PMID:24177027 (review), PMID:38720107
  (human PCK2 kinase activity on ACSL4).

## Decisions

- GO:0004611 rows -> MODIFY to GO:0004613 (GTP-specific child, already on the gene).
- Whole-liver PEPCK IDA rows (PMID:11440903, PMID:4353083; abstract-only) probably measure mostly
  PCK1 activity [PMID:6049928 "more than 90% of the activity is in the cytoplasm"]. Not overruled;
  flagged as SUSPECTED WRONG_GENE_PRODUCT CHECK for RGD.
- GO:0042866 pyruvate biosynthetic process (IMP, PMID:19635791): PCK2 makes PEP; pyruvate kinase
  makes the pyruvate. Over-annotation; source defect WRONG_TERM CHECK (no PEP biosynthesis term in GO).
- GO:0017076 purine nucleotide binding -> MODIFY to GO:0005525 GTP binding.
- Kinase activity / ferroptosis (ISO/IEA from human, one study) kept as non-core.
- IEP rows kept as non-core.
- Sequence note: F1LQJ7 starts at "TLLPSPP..." without Met; rat Met28 aligns to the human start.
