# RAS2 curation notes

## 2026 IBA re-review

Re-checked the four current RAS2 IBA annotations against GOA and the cached PANTHER
`PTHR24070` PAINT table:

- `GO:0005886 plasma membrane` and `GO:0003924 GTPase activity` both trace to
  `PANTHER:PTN000631348`, a Ras-family node that has current IBDs for membrane localization
  and the core Ras catalytic activity.
- `GO:0007163 establishment or maintenance of cell polarity` traces to
  `PANTHER:PTN000631919`, an opisthokont node whose polarity assertion is compatible with
  the yeast Ras2 role in Cdc42/MAPK-dependent filamentous growth and Lte1 bud-cortex
  recruitment.
- `GO:0007265 Ras protein signal transduction` traces to `PANTHER:PTN008393310`, matching
  the conserved Ras GTPase switch role that Ras2 performs upstream of Cyr1/cAMP/PKA in
  budding yeast.

All four IBA rows are biologically sound for RAS2, so the YAML now keeps them as `ACCEPT`
and records `propagation_review.root_cause: NO_FAILURE_CORE` with the PTN ancestral node,
not the extant `WITH/FROM` genes, as the source entity. The full GOA `WITH/FROM` sets were
copied into `supporting_entities` for traceability.

The newer-paper search did not turn up a post-2023 primary paper that changes these RAS2
core function calls. Recent hits were pathway-level or engineering papers about yeast
Ras/cAMP/PKA signaling rather than new direct evidence for Ras2 itself.
