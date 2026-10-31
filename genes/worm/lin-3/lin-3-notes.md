# lin-3 Notes

## 2026-09-30 PENDING annotation review

Provider deep research was not available for this pass: Falcon required
`agentapi` on `PATH`, and API-key fallbacks were unavailable. The review
therefore used the seeded GOA annotations in `lin-3-ai-review.yaml`, the
UniProtKB Q03345 record in `lin-3-uniprot.txt`, all 12 cached cited PMIDs, and
the local GO-CAM/Reactome cache. No LIN-3-specific GO-CAM or Reactome record was
found locally.

Reviewed all 26 seeded annotations. The main decisions were to accept the
LIN-3/LET-23 ligand and EGFR-signaling evidence, keep broad developmental
outputs as non-core, modify the older `growth factor activity` NAS row to
`receptor ligand activity`, mark egg-laying behavior as over-annotated because
the cached evidence supports vulval induction rather than the egg-laying motor
program itself, and leave two ovulation rows undecided where the cached
abstracts did not expose LIN-3-specific evidence.
