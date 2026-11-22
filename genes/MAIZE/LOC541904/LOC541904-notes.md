# LOC541904 notes

## 2026-10-28 initial review

- Fetched A0A804NBL1 (TrEMBL). Confirmed it is ZmEXPA1 / GeneID 541904 (NCBI Gene
  "alpha expansin 1", alias GRMZM2G339122; RefSeq NP_001105040.1 shared with legacy
  entry Q94KT7, gene name expA1). GOA is keyed to A0A804NBL1 (4 IEA rows).
- The task named PMID:17225858 as a key paper. Full text read: it is about the
  beta-expansin EXPB1 (Zea m 1d) mutant and pollen competition
  [PMID:17225858 "a maize line containing a Mu transposon insertion in EXPB1 (GenBank Accession AY197353)"].
  No EXPA1 data. Kept in references with relevance LOW / MISCITED as a gene-specific source.
- Gene-specific literature is expression only [PMID:11351085; PMID:24758373;
  PMID:34612535; PMID:39936861]. Function is inferred from family membership and the
  well-characterized EXPA mechanism [PMID:16356276; PMID:26057089; PMID:38724021].
- Decisions:
  - extracellular region -> MODIFY to plant-type cell wall (GO:0009505, is_a/part_of
    descendant of GO:0005576 checked with OAK).
  - plant-type cell wall organization -> MODIFY to plant-type cell wall loosening
    (GO:0009828, descendant, checked with OAK).
  - plant-type cell wall loosening -> ACCEPT.
  - membrane (UniProt SubCell "Peripheral membrane protein") -> MARK_AS_OVER_ANNOTATED,
    source defect query to UniProt for the RU365023 subcellular location statement.
- No GO MF term describes nonenzymatic wall loosening (GO:0009936 "expansin" is
  obsolete); proposed a new MF term.
