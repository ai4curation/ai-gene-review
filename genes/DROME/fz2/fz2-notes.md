# fz2 review notes

## Session 1 (initial review)

- fetch-gene resolved Q9VVX3 (Swiss-Prot FRIZ2_DROME, FlyBase FBgn0016797, GeneID 40090); 70 GOA rows.
- No deep-research provider available; manual synthesis in `fz2-deep-research-manual.md`.
- GO-CAM 6086f4f200000223 ("canonical Wnt signaling pathway via wg-fz2") models fz2 as Wnt receptor
  activity in the plasma membrane, consistent with this review.
- Core: Wnt receptor activity (Wg, Wnt4, Wnt5) at the plasma membrane; canonical Wnt signalling with
  Arrow; non-canonical Frizzled Nuclear Import pathway at the NMJ [PMID:16311339 "The C terminus of
  DFrizzled2 is cleaved and translocated into the nucleus"].
- Decisions: generic terms (membrane, transmembrane signaling receptor activity, cell surface receptor
  signaling pathway, Wnt signaling pathway) MODIFIED to specific descendants; protein binding (Grip)
  MODIFIED to PDZ domain binding [PMID:16682643]. Developmental process rows kept as non-core.
- UNDECIDED: Wnt signalosome IDA (PMID:12711303; abstract does not mention Fz2) and regulation of
  hemocyte proliferation IMP (PMID:20688956; abstract does not mention frizzled; full text not cached).
- PMID:22530061: the gene-trap line BG01711 that BDGP mapped to fz2 actually splices into CG8771 per
  3' RACE, so its olfactory phenotype is not attributable to fz2. No annotation proposed from it.
- NEW: postsynaptic membrane (IDA, PMID:16311339 "We show that DFrizzled2 is endocytosed from the
  postsynaptic membrane and transported to the nucleus."). No NEW process terms proposed.
