# EXG1 review notes

## 2026-10-10

- Seeded the current `yeast/EXG1` review from GOA. The file contains 19 current
  GOA rows covering the exact exo-1,3-beta-glucanase activity, extracellular and
  cell-wall localization, broad InterPro hydrolase/process parents, a SWAT
  vacuole HDA row, and three PTHR31297 PAINT rows.
- Tried the default `falcon` deep-research provider with `perplexity-lite`
  fallback. Both providers failed because no deep-research credentials are
  configured in this environment, so this review used cached GOA publications,
  UniProt, PTHR31297 PAINT data, and a manual PubMed search instead.
- PTHR31297 splits the current PAINT calls over three relevant nodes. The exact
  `GO:0004338 glucan exo-1,3-beta-glucosidase activity` assertion is on the
  Saccharomycetes `PTN001262687` node seeded by CGD XOG1 and multiple SGD
  glucanases, including EXG1. `GO:0005576 extracellular region` and
  `GO:0070879 fungal-type cell wall beta-glucan metabolic process` sit at the
  slightly broader fungal `PTN001262686` node. Broad `GO:0009251 glucan
  catabolic process` sits at a much broader node, `PTN001262628`, seeded only by
  Aspergillus SF34/SF39 exgB/exgD-like members in the local PAINT cache and is
  over-scoped for yeast EXG1.
- The direct recombinant-enzyme paper, PMID:11471729, is abstract-only in the
  cache and supports exo-beta-1,3-glucanase activity plus a broad in vitro
  substrate profile. It confirms beta-1,6-linked substrate activity but does not
  establish an endo-1,6 mode in the cached abstract, so the SGD
  `GO:0046557 glucan endo-1,6-beta-glucosidase activity` row is marked as
  over-annotated.
- Searched PubMed for newer `EXG1`, `YLR300W`, and `SCW6` papers. The main
  newer direct biochemical hit is PMID:41439696, a 2026 full-text ScEXG1 study
  showing that His-tagged ScEXG1 hydrolyzes beta-1,3 glucan and can form
  beta-1,6-containing transglycosylation products from laminaribiose in vitro.
  Several other post-2016 hits delete EXG1 as an endogenous glycosidase during
  natural-product engineering or report proteomic abundance changes; they do not
  alter EXG1's core GO function.
- The 2016 SWAT paper, PMID:26928762, is full text in the cache, but the
  extracted text does not include the supplementary EXG1 localization row behind
  the SGD `GO:0000324 fungal-type vacuole` assignment. Because mature Exg1 has a
  cleaved signal peptide and direct evidence for secretion to the extracellular
  region/cell wall, the vacuole row was marked as over-annotated rather than as
  a core site of action.
