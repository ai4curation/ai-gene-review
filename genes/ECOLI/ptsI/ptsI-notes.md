# ptsI (enzyme I, P08839) notes

Reviewed 2026-11-11 as the enzyme I partner of FPr in the split-relay variant of the
generic fructose PTS module (`modules/fructose_pts_uptake_and_catabolism.yaml`).

Deep research: no provider deep-research file was generated for this gene in this
session; the review rests on the cached publications (abstract-only) and the UniProt
record, whose function, kinetics and location lines cite experimental papers.

- Core: PEP-protein phosphotransferase activity (EC 2.7.3.9) [PMID:12705838
  "EI(C502A) is 10 000 times less active than wild-type EI [EI(wt)] with PEP as the
  substrate"]; dimeric three-domain structure [PMID:17053069].
- All bare protein-binding IPI rows (HPr, BglG, TmaR) removed per policy.
- GO:0015764 N-acetylglucosamine transport marked as over-annotation: true in principle
  for the general enzyme I, but the comparator HPr (P0AA04) carries only GO:0009401 and no
  sugar-specific transport term in GOA (QuickGO query, 2026-11-11), and the node is rated
  TOO_DEEP in the PTHR46244 family review. Same action as Xanthomonas FruB; EI(Ntr) PtsP
  removes it because EI(Ntr) is not a sugar-PTS enzyme.
- Cytoplasm rows refined to cytosol (HDA cytosolic fraction), following E. coli ptsN.

## 2026-11-24 re-review of the over-annotated IBA row

- GO:0015764 N-acetylglucosamine transport (IBA) changed from MARK_AS_OVER_ANNOTATED to
  KEEP_AS_NON_CORE. The PAINT IBD is at the family root PTN000532509 (43 leaves) with one seed,
  P. aeruginosa PA3760 (Q9HXN5; QuickGO: involved_in GO:0015764 IMP PMID:18833300, PseudoCAP).
  The seed and ptsI are both in the 14-leaf clade PTN001879016, so the target is inside the seeded
  clade, and the term is true of the general enzyme I. "One sugar out of many" is about how specific
  the term is, not a ground for doubt. The node is still too deep for EI(Ntr) (PtsP), as the
  PTHR46244 family review says; that is a PAINT placement question and does not change this row.
