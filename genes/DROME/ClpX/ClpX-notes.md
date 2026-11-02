# ClpX (CG4538, A0A0B4LID7) notes

## 2026-10-09 review session (module dmel_mitochondrial_clpxp)

- Deep research falcon: first attempt rate-limited (HTTP 429), rerun pending at review time.
- UniProt entry is an unreviewed isoform record ("Caseinolytic protease chaperone subunit, isoform C").
- Matsushima et al. 2017:
  - [PMID:28814717 "Moreover, we showed that ClpX, which recognize the protein substrates of ClpXP, physically interacts with DmLRPPRC1 in the cells (Fig."]
  - [PMID:28814717 "Here, we showed that knockdown of ClpX or ClpP results in an increase of DmLRPPRC1 protein without an increase in the corresponding mRNA (Figs 2 and S4)."]
  - [PMID:28814717 "ClpXP and Lon localize to the matrix space whereas the m-AAA protease is anchored in the membrane with its catalytic site exposed to the matrix space."]

## Decisions
- Core: ATP hydrolysis activity, contributing to ATP-dependent peptidase activity of ClpXP, in the
  mitochondrial endopeptidase Clp complex (matrix).
- protein folding / ATP-dependent protein folding chaperone (InterPro IEA): KEEP_AS_NON_CORE. ClpX is
  primarily an unfoldase for ClpP; ClpP-independent chaperone roles are known for yeast/mammalian
  orthologs but untested in flies.
