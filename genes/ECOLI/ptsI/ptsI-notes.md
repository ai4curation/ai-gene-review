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
- GO:0015764 N-acetylglucosamine transport kept as non-core: true via HPr/NagE for the
  general enzyme I, unlike EI(Ntr) PtsP where the same IBA was removed.
