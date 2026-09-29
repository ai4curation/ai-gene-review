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

The `SGD:S000005042` donor that appears in the `GO:0005886` and `GO:0003924`
`WITH/FROM` sets is RAS2 itself. That is expected for target-seeded PAINT nodes: the
direct yeast SGD evidence helped place the IBD at `PTN000631348`, and the resulting
IBA records that plasma-membrane localization and GTPase activity are inherited
Ras-family properties rather than lineage-specific RAS2 observations.

`PTN000631348` also carries `GO:0007264 small GTPase mediated signal transduction`,
the parent of `GO:0007265 Ras protein signal transduction`; RAS2 currently inherits
the more specific child from `PTN008393310` without a redundant GO:0007264 IBA row in
the fetched GOA snapshot.

All four IBA rows are biologically sound for RAS2, so the YAML now keeps them as `ACCEPT`
and records `propagation_review.root_cause: NO_FAILURE_CORE` with the PTN ancestral node,
not the extant `WITH/FROM` genes, as the source entity. The full GOA `WITH/FROM` sets were
copied into `supporting_entities` for traceability.

The newer-paper search did not turn up a post-2023 primary paper that changes these RAS2
core function calls. Recent hits were pathway-level or engineering papers about yeast
Ras/cAMP/PKA signaling rather than new direct evidence for Ras2 itself.
