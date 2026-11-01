# Anxa2 (rat) review notes

- 2026-10-26: Created review. fetch-gene resolved Q07936 (ANXA2_RAT); 103 GOA rows
  (mostly ISO from human P07355 / mouse MGI:88246, plus 18 rat experimental rows).
- No deep-research API keys; manual synthesis in `Anxa2-deep-research-manual.md`.
- Key rat paper PMID:19193640 (full text): Rat-1 R1LA29 cells; supports ruffle, cell
  cortex, macropinosome, Rab11-positive perinuclear vesicles (recycling endosome),
  and IMP for v-Src plasma membrane targeting
  [PMID:19193640 "annexin 2 is absolutely required for the association of activated v-Src with this compartment"].
  The "positive regulation of fibroblast proliferation" IMP is based on
  anchorage-independent growth of v-Src transformed cells in soft agar, an indirect
  readout; marked as over-annotation rather than removed.
- PMID:14734570: PI(4,5)P2 binding (recombinant protein; RBL cells for in vivo
  co-localization) [PMID:14734570 "recombinant annexin 2 binds to phosphatidylinositol 4,5-bisphosphate"].
- Phospholipase A2 inhibitor annotations: classical annexin "lipocortin" activity is
  generally attributed to substrate (phospholipid) sequestration in vitro; treated as
  over-annotation.
- Basement membrane (UniProt SubCell from PMID:1618851, not cached): the same UniProt
  record notes "In the lamina beneath the plasma membrane", i.e. sub-membranous
  cortex; flagged as over-annotation.
- Transcription-related ISO terms (RNA pol II) are weak/peripheral; marked over-annotated.
- No NEW terms proposed; candidate "negative regulation of actin filament
  polymerization" (PMID:16601677) lacks rat-specific evidence and was not added.
