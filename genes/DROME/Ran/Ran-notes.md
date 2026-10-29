# Ran (DROME) review notes

## Session 2026-10-28

- `just fetch-gene DROME Ran` resolved Q9VZ23 (RAN_DROME, FlyBase FBgn0020255, GeneID 44072),
  40 GOA rows. Accession matches the task.
- Cached PMIDs: 12121620, 12653959, 17287812 (abstract only); 22024168, 22100918, 31626769
  (full text). Added PMID:16481399 (Silverman-Gavrila & Wilde 2006, abstract only) for
  mitotic context.
- No deep-research API; manual synthesis in `Ran-deep-research-manual.md`.

### Key decisions

- GTPase activity / GTP binding: ACCEPT (core MF; RanGTP is the switch read by importins,
  exportins and Canoe RA domains [PMID:22024168 "the Canoe RA domains can interact directly
  with GTP-loaded Ran"]).
- Nucleocytoplasmic transport terms (protein import/export, nuclear export, ribosome
  subunit export): ACCEPT/KEEP_AS_NON_CORE. Ran is the directionality determinant.
- poly(A)+ mRNA export IBA: MARK_AS_OVER_ANNOTATED; seeded by yeast only, metazoan bulk
  mRNA export via NXF1 is largely Ran independent.
- nuclear pore (part_of, IBA): MARK_AS_OVER_ANNOTATED; Ran transits the pore but is not a
  subunit.
- NLS-dependent protein nuclear import complex (NAS): REMOVE + source_defect; the complex is
  importin alpha/beta(+cargo), which RanGTP disassembles.
- intracellular protein transport (TAS): MODIFY to protein import into nucleus and protein
  export from nucleus.
- mitotic spindle microtubule (IDA, PMID:12121620, abstract only): MODIFY to mitotic spindle;
  abstract says Ran localizes "around the spindle", not on microtubules.
- cell cortex (IDA, PMID:22024168): MARK_AS_OVER_ANNOTATED; cortical Ran was induced by an
  engineered Ed:CnoRA tether in S2 cells, not endogenous cortical localization.
- regulation of mitotic cell cycle (IDA, PMID:12121620): MARK_AS_OVER_ANNOTATED; abstract
  reports localization only, the documented role is in spindle assembly.
- Protein binding rows (Canoe, Tamo): REMOVE per policy; no informative Ran-side MF term.
- No NEW rows. Mitotic spindle assembly (PMID:16481399) is plausible but Ran acts by
  releasing spindle assembly factors from importins; raised as a question rather than
  asserted.
