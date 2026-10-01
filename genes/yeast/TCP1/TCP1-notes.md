# TCP1 curation notes

## 2026-09-29 - IBA source alignment

- Rechecked the three TCP1 IBA rows against the current `PTHR11353` PAINT snapshot.
  `PTN000144020` still carries `GO:0005832` chaperonin-containing T-complex on the
  CCT-alpha/TCP1 branch, and `PTN004253040` still carries `GO:0006457` protein folding
  on the broad TRiC/CCT paralog node.
- The older `GO:0051082` unfolded protein binding IBA no longer appears on the current
  `PTN004253040` PAINT node. The existing `MODIFY` to `GO:0140662` ATP-dependent
  protein folding chaperone remains the right repair for TCP1 as a TRiC/CCT subunit.
- Converted the legacy `GO:0005515` protein binding IPI rows to `REMOVE`. The
  interactors are compatible with chaperonin substrates or TAP-MS co-complex recovery,
  but the generic term adds no information beyond TRiC/CCT complex membership and
  ATP-dependent folding activity.
- Searched 2025-2026 PubMed and the broader web for `TCP1`, `CCT1`, `YDR212W`, and
  yeast TRiC/CCT papers. The newer hits did not provide peer-reviewed
  S. cerevisiae TCP1 evidence that changes the existing CCT-alpha curation.

## 2026-10-01 - Current GOA refresh

- Forced a current GOA and UniProt refresh. Current GOA has 16 rows; these collapse
  to 15 live review rows because the SGD and ComplexPortal `PMID:16762366`
  `GO:0006457` rows have the same term, evidence code, and reference signature.
- Kept the two live PAINT assertions aligned to current `PTHR11353`: `PTN000144020`
  still supports CCT-alpha membership in `GO:0005832`, and `PTN004253040` still
  supports conserved CCT/TRiC `GO:0006457` protein folding.
- Marked the obsolete `GO:0051082` rows, the old GO_REF:0000043 nucleotide-binding
  row, the stale GO_REF:0000120 ATP-binding row, and five large-scale IntAct
  `GO:0005515` rows that disappeared from GOA as retired historical assertions.
- Reviewed the two newly seeded current rows: the current InterPro2GO
  `GO:0005524` ATP-binding row and the new ComplexPortal `PMID:21701561`
  `GO:0005832` CCT-complex row.
- Searched for newer TCP1/CCT1/YDR212W yeast TRiC papers and cached
  `PMID:40070846`, a 2025 yeast TRiC ring-opening cryo-EM paper. It supports
  subunit-specific CCT1 movement late in ring opening, but does not require a
  new GO assertion.
