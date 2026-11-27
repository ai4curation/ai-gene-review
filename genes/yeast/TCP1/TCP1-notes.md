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
