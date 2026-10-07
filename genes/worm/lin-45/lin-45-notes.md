# lin-45 Notes

## 2026-09-30 PENDING annotation review

Provider deep research was not available for this pass: Falcon required
`agentapi` on `PATH`, and API-key fallbacks were unavailable. The review
therefore used the seeded GOA annotations in `lin-45-ai-review.yaml`, the
UniProtKB Q07292 record in `lin-45-uniprot.txt`, the four cached cited PMIDs,
and the local GO-CAM/Reactome cache. No LIN-45-specific GO-CAM or Reactome
record was found locally.

Reviewed all 22 seeded annotations. The main decisions were to accept the core
C. elegans RAF biology, modify broad kinase and signal-transduction terms to
specific RAF/ERK-cascade terms, keep vulval, larval, cell-fate, and
Gram-positive bacterium defense rows as non-core pathway outputs, and accept the
LET-60/Ras small-GTPase-binding IPI row as biologically correct while using Hsu
et al. 2002 as additional support because the cached PMID:9674433 abstract did
not expose the full original IPI evidence.
