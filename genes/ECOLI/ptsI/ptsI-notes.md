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
