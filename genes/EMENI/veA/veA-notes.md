# veA (Aspergillus nidulans) — curation notes

UniProt C8VTV4 (VEA_EMENI). Founding velvet-superfamily member; light-dependent
coordinator of development and secondary metabolism. Velvet tier of the
`conidiation_regulatory_cascade` module.

- In the dark VeA bridges VelB and LaeA to form the velvet complex. [PMID:21152013 "In the dark, VeA bridges VelB and LaeA to form the VelB-VeA-LaeA (velvet) complex"]; [PMID:21152013 "VeA is the founding member of the velvet superfamily of fungal regulatory proteins"].
- Light-dependent nucleocytoplasmic partitioning (nuclear in dark): many EXP
  nucleus/cytoplasm annotations, all ACCEPT.
- Regulation of secondary metabolic process ACCEPT (velvet complex). Regulation of
  sulfur metabolic process (IEA/ARBA) kept non-core (unconfirmed for VeA).
- No molecular_function asserted: VeA's characterized role is complex-bridging /
  light response rather than a defined enzymatic or DNA-binding activity.

## 2026-10-01 re-review (GOA refresh)

- Two ARBA IEA rows (GO_REF:0000117) disappeared from the current GOA snapshot and were
  marked `retired: true` (reviews kept): GO:0042762 regulation of sulfur metabolic process
  (was KEEP_AS_NON_CORE) and GO:0043455 regulation of secondary metabolic process (was ACCEPT).
  Retirement records disappearance from GOA, not a biological judgment.
- Because GO:0043455 is a core process for VeA, added a NEW row (IMP, PMID:18556559, with
  PMID:20816830 corroboration) so the core function remains grounded in experimental literature.
- Added verbatim supporting text to the nucleus/cytoplasm EXP rows from PMID:20816830 and
  PMID:23341778 (both full text cached).
