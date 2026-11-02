# EMENI/mpkC Notes

## 2026-11-02

- Fetched the seeded `EMENI/mpkC` review for UniProt `Q9HG11`.
- Tried Falcon deep research with `perplexity-lite` fallback. Falcon failed in
  this sparse checkout because `templates/gene_research_go_focused.md` was not
  materialized, and the Perplexity fallback was unavailable because
  `agentapi` is not installed.
- Searched for newer A. nidulans `mpkC`/`AN4668`/`PbsB`/`HogA` literature and
  cached the direct papers most relevant to the current GOA rows:
  `PMID:15882418`, `PMID:16998074`, `PMID:25820520`, `PMID:30405576`, and
  `PMID:34436163`.
- The key 2005 result is that PbsB can activate MpkC in A. nidulans, but the
  same abstract explicitly says that `mpkC` is dispensable in osmoadaptation.
  The 2018 MpkC::GFP study resolves this apparent tension: MpkC is a
  PbsB-regulated HOG1-subfamily stress MAPK whose nuclear accumulation responds
  to osmotic and oxidative stress, but SakA/HogA and MpkC have distinct and
  sometimes opposing developmental and stress roles.
- Kept the `PTN001172058` IBA rows for `stress-activated MAPK cascade`,
  `osmosensory signaling pathway`, and `cellular response to oxidative stress`.
  The PAINT node is the fungal HOG/Sty1 stress-MAPK node, and A. nidulans MpkC
  is in the inherited SakA/MpkC branch.
- Accepted the SGD:HOG1 ISA to `cellular hyperosmotic response`, but with a
  caution in the rationale: MpkC is a minor PbsB-dependent stress branch, not
  the principal A. nidulans osmoadaptation MAPK.
