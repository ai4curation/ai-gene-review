# CANAL EXG2 notes

## 2026-10-10

- Seeded `CANAL/EXG2` from GOA. The review has 12 rows: four
  exo-1,3-beta-glucosidase activity rows, two broad InterPro parent rows,
  PAINT extracellular and fungal-type cell wall beta-glucan rows, a broad
  family-root glucan catabolism IBA, a UniProt extracellular mapping, and
  plasma-membrane rows from UniProt and the Cabezon et al. plasma-membrane
  proteome.
- Tried the default `falcon` deep-research provider with `perplexity-lite`
  fallback. Both providers failed because no deep-research credentials are
  configured in this environment, so this review used cached GOA and UniProt
  publications, UniProt, PTHR31297 PAINT data, the sibling XOG1/EXG1/SPR1
  reviews, and manual literature searches instead.
- PTHR31297 places C. albicans Exg2 in `PTHR31297:SF1`, the same subfamily as
  C. albicans Xog1 and budding-yeast Exg1/Spr1. The exact
  `GO:0004338 glucan exo-1,3-beta-glucosidase activity` IBD is placed on
  `PANTHER:PTN001262687`, while `GO:0005576 extracellular region` and
  `GO:0070879 fungal-type cell wall beta-glucan metabolic process` are placed
  one node higher at `PANTHER:PTN001262686`.
- The broad `GO:0009251 glucan catabolic process` row inherits from
  `PANTHER:PTN001262628`, the PTHR31297 family-root node that is seeded by
  Aspergillus SF34/SF39 exgD/exgB-like branches as well as the SF1
  Saccharomycetes glucanases. This is the same over-scoped root IBA flagged in
  EXG1 and SPR1.
- The direct PMID:19824013 row reports a C. albicans plasma-membrane proteome
  enriched for GPI-anchored membrane proteins, but the cached abstract does not
  name EXG2. Because UniProt predicts a C-terminal GPI anchor and maps Exg2 to
  both cell membrane and secreted locations, the plasma-membrane assignment is
  plausible, but the review should be explicit that the PMID:19824013 row is
  only abstract-verifiable in the local cache.
- PubMed/web searches for `Candida albicans EXG2`, `CaO19.2952`,
  `CAALFM_C102630CA`, and `Exg2p` did not find newer EXG2-specific biochemistry
  that would override the PAINT/ISS inheritance. PMID:21713010 constructed
  `EXG2` deletion strains while dissecting XOG1/LL-37 adhesion and found that
  XOG1, not EXG2, dominated cellular exoglucanase activity, adhesion, and
  LL-37 binding; this argues against adding an adhesion process for EXG2.
