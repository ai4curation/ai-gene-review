# SWI3 curation notes

## 2026-09-29 - IBA source alignment

- Rechecked the three SWI3 IBA rows against the current `PTHR12802` PAINT snapshot.
  `PTN000301253` still carries `GO:0016514` SWI/SNF complex, and `PTN000301254`
  carries `GO:0045893` positive regulation of DNA-templated transcription and
  `GO:0042393` histone binding.
- Kept SWI/SNF complex membership, positive transcriptional regulation, and histone
  binding as supported core calls. The histone-binding IBD is seeded by direct SGD
  evidence from the current PTHR12802 PAINT snapshot.
- Converted the legacy `GO:0005515` protein binding IPI rows to `REMOVE`. The underlying
  interactions are real, but SWI/SNF complex membership and histone binding represent the
  relevant partner classes more specifically.
- Searched 2025+ PubMed for `SWI3`, `TYE2`, and `YJL176C` with `Saccharomyces cerevisiae`
  and found no new exact matches; broader SWI/SNF 2025-2026 hits did not change the
  SWI3 PAINT calls.
