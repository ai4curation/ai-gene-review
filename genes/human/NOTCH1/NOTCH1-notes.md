# NOTCH1 review notes

## 2026-07-14 — cerebellum-module quality audit

- Audited the existing complete human NOTCH1 review rather than reseeding it. All 378
  GOA-derived annotations have explicit review actions and none remains `PENDING`.
  The project-independent description and three core-function units were retained.
- Added structured propagation metadata to the removed axon-guidance IBA annotation.
  Inspection of the recorded PANTHER node and GOA support traced the inference to
  SLIT-family donors rather than a conserved NOTCH-family function, supporting the
  existing removal decision.
- NOTCH1 is intentionally not an annoton in the cerebellum-development module. The
  original DNER study proposed a DNER–NOTCH1 mechanism, but a later full-text direct
  replication found no DNER binding or activation of NOTCH1
  [PMID:27622512 "DNER is not a Notch ligand and its true function remains unknown."].
  This module-specific evidence correction does not alter NOTCH1's well-supported
  canonical receptor activities elsewhere in the gene review.

