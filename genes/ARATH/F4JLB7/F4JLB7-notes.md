# F4JLB7 notes

## 2026-10-14 — UNDECIDED rows resolved (ARATH corpus project, PR #5024)

Three experimental rows from PMID:11752391 (RIC7: protein binding IPI, pollen tube
growth IMP, apical plasma membrane IDA) were set to REMOVE as attributed to the
wrong locus. The basis is sequence evidence, not the abstract's gene focus:

- The published RIC7 cloning primers map to the adjacent, oppositely oriented CRIB
  locus AT4G28556 (UniProtKB:Q1G3K8), not to F4JLB7; see
  `genes/ARATH/Q1G3K8/Q1G3K8-bioinformatics/RESULTS.md`.
- F4JLB7 has no CRIB motif, which the paper reports as required for Rop1 binding.
- The function is not lost: the Q1G3K8 review already carries ROP binding, pollen
  tube growth and plasma membrane from PMID:11752391.

The remapping should be reported to TAIR curators. The chloroplast ISM row was also
removed (contradicted by the signal peptide, LRR receptor architecture and accepted
plasma-membrane IBA).
