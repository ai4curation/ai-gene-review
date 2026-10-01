# EPS1 curation notes

## 2026-10-01 current-GOA / IBA review

- Refreshed EPS1 from current UniProt/GOA before editing. Current GOA has 15
  live rows after the header; the refresh materialized three additional
  partner-specific `GO:0005515 protein binding` rows from PMID:16002399 and a
  broad ARBA `GO:0005783 endoplasmic reticulum` row.
- Checked the current PAINT export cached in `.cache/panther/IBD.gaf`. All
  three EPS1 IBA rows descend from `PANTHER:PTN005231188`, which carries
  `GO:0003756 protein disulfide isomerase activity`, `GO:0005783 endoplasmic
  reticulum`, and `GO:0006457 protein folding`.
- The IBA rows are consistent with Eps1's placement in `PTHR45672` and with
  direct yeast evidence for an ER-membrane PDI-family ERAD factor. I retained
  all three and recorded `NO_FAILURE_CORE` propagation reviews against the
  PAINT node rather than treating the individual source genes as pairwise
  donors.
- The refreshed GOA no longer emits the earlier ARBA cytoplasm and endomembrane
  rows, the broad UniProt keyword `GO:0016853 isomerase activity`, or the
  obsolete direct `GO:0051082 unfolded protein binding` row. I preserved all
  four as retired rows.
- All current `GO:0005515 protein binding` rows from PMID:16002399 were
  changed to `REMOVE`. The interactions with PDI/chaperone partners are
  biologically meaningful, but the root protein-binding term adds no specific
  molecular-function information.
- Fetched full text for PMID:25437863 after the literature search surfaced the
  2014 Eps1p structural paper. The structures support retaining PDI-family
  chemistry with a noncanonical-mechanism caveat; they do not justify an
  additional GO row.
