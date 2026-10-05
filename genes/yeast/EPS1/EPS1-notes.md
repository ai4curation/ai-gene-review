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

## 2026-10-05 PR #3748 reviewer follow-up

- Changed the broad `GO:0006457 protein folding` IBA from `ACCEPT` to
  `KEEP_AS_NON_CORE` and marked the PAINT propagation as `NO_FAILURE_NON_CORE`;
  the row is defensible for a membrane ER quality-control chaperone but
  overstates the core process if read as generic oxidative protein folding.
- Changed `GO:0019153 glutathione-dependent protein disulfide reductase
  activity` from `REMOVE` to `UNDECIDED`. The cached PMID:16002399 abstract
  says the reductive activities were measured in an earlier paper, while the
  Eps1p-specific "undetectable" result visible in the cache refers to oxidative
  refolding rather than to the glutathione-dependent reductase assay behind the
  SGD IDA row.
- Moved the core molecular function to the more specific `GO:0044183 protein
  folding chaperone`, updated stale `GO:0036503` labels to `ERAD quality
  control pathway`, and kept EPS1's core biological process focused on
  substrate-specific ERAD rather than broad `GO:0006457 protein folding`.
- Recorded the tension in PMID:11157982: its CXXC genetic result supports
  retaining SGD's PDI-activity IMP row, but its broad PDI-paralog deletion
  assays showed no significant effect on ER-associated degradation, so EPS1's
  ERAD evidence still rests on the Pma1-D378N substrate-recognition work.
