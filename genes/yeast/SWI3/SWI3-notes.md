# SWI3 curation notes

## 2026-09-29 - IBA source alignment

- Rechecked the three SWI3 IBA rows against the current `PTHR12802` PAINT snapshot.
  `PTN000301253` still carries `GO:0016514` SWI/SNF complex, and `PTN000301254`
  carries `GO:0045893` positive regulation of DNA-templated transcription and
  `GO:0042393` histone binding.
- Kept SWI/SNF complex membership, positive transcriptional regulation, and histone
  binding as supported core calls. The histone-binding IBD is seeded by direct SGD
  evidence from the current PTHR12802 PAINT snapshot.
- Converted most legacy `GO:0005515` protein binding IPI rows to `REMOVE`. The
  underlying interactions are real, but SWI/SNF complex membership and histone binding
  represent the relevant partner classes more specifically; the two low-throughput
  complex-architecture rows from PMID:12805231 and PMID:8127913 instead become
  `MODIFY` calls for `GO:0005198` structural molecule activity.
- Searched 2025+ PubMed for `SWI3`, `TYE2`, and `YJL176C` with `Saccharomyces cerevisiae`
  and found no new exact matches; broader SWI/SNF 2025-2026 hits did not change the
  SWI3 PAINT calls.

## 2026-10-01 - current GOA refresh

- Re-fetched GOA, UniProt, the cached SWI3 references, and `PTHR12802` PAINT.
  The three IBA rows remain current and correctly trace to ancestral PAINT nodes:
  `PTN000301253` for `GO:0016514` SWI/SNF complex and `PTN000301254` for
  `GO:0045893` positive regulation of DNA-templated transcription plus `GO:0042393`
  histone binding.
- Resolved the 2026 GOA refresh rows: accepted the new exact ARBA DNA-binding row,
  accepted the ComplexPortal SWI/SNF-complex row, accepted the additional exact
  SGD histone-binding rows from PMID:17496903, removed five generic exact
  `GO:0005515` protein-binding rows, and modified the new PMID:8127913
  Snf2-interaction row to `GO:0005198` structural molecule activity.
- Retired four exact rows no longer present in current GOA: the old GO_REF:0000120
  DNA-binding row, the broad GO_REF:0000043 transcription row, and stale generic
  protein-binding rows from PMID:12805231 and PMID:16554755.
- Searched PubMed and the web for 2025-2026 SWI3/Swi3/SWI/SNF papers. The only
  direct hits from the SWI3/Swi3 query were Toxoplasma SWI/SNF papers rather than
  Saccharomyces SWI3 studies, and broader 2026 yeast SWI/SNF papers did not change
  the Swi3 IBA or core-function calls.
