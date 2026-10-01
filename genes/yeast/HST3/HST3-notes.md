# HST3 review notes

## 2026-10-01 GOA/IBA refresh

- Forced a current GOA refresh and reconciled HST3 to the 19 live GOA rows.
  The previous local review carried three stale UniProt keyword rows from
  GO_REF:0000043: GO:0006351 DNA-templated transcription, GO:0016740 transferase
  activity, and GO:0046872 metal ion binding. All three disappeared from
  current GOA and were retained as `retired: true`; the underlying biology is
  now represented by more specific live rows, including the direct
  PMID:31167142 transcription rows, the live NAD-dependent deacetylase chemistry
  rows, and the specific GO:0008270 zinc ion binding RCA row.

- Rechecked all live PTHR11085 PAINT assertions against the current
  PTHR11085-paint.tsv export. PTN008492176 still emits the broad sirtuin-family
  nucleus annotation, PTN008718612 still emits GO:0017136 NAD-dependent histone
  deacetylase activity, and PTN000119247 still emits the rDNA heterochromatin
  process. HST3 self-donors on the GO:0017136 row are valid descendant evidence
  rather than circular support.

- Kept the GO:0017136 IBA as MODIFY to GO:0140765 because current PAINT still
  asserts a biologically true parent term while HST3's direct yeast evidence
  supports the H3K56-specific child. Marked the GO:0000183 rDNA heterochromatin
  IBA as a bad transfer because PTN000119247 is seeded by the S. cerevisiae
  paralog HST2 and a PomBase Sir2-family source, while the cached HST3 literature
  supports H3K56 deacetylation and telomeric/2-micron silencing rather than
  HST3-specific rDNA heterochromatin formation.

- Searched for 2025-2026 HST3/YOR025W literature. The only specific new hit
  was a 2026 bioRxiv preprint on H3K56ac and origin licensing; it further uses
  Hst3/Hst4 as the known S-phase-exit H3K56 deacetylases but does not change
  the reviewed GO action set and was not used as annotation evidence.
