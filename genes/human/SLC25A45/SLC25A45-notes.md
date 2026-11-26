# SLC25A45 notes

## Setup

- `just fetch-gene human SLC25A45` created the UniProt record, a header-only GOA
  table, and the initialized review file. The current GOA cache has no rows for
  Q8N413, so all asserted GO rows in this review are `NEW`.
- `just fetch-gene-pmids human SLC25A45` found no PMID-backed GOA rows.
- `just deep-research-falcon human SLC25A45 --fallback perplexity-lite` could not
  run because `agentapi` was not on `PATH` and the configured fallback provider
  was unavailable. I used the cached full text for PMID:41075794 and PMID:41075780
  and the freshly fetched UniProt entry for Q8N413 instead.

## Curation decisions

- Added `GO:7770026` for N(6),N(6),N(6)-trimethyl-L-lysine transport because
  isolated mitochondria expressing SLC25A45-8xHis imported labeled TML while
  matched controls did not [PMID:41075794, "Expression of SLC25A45-8xHis was
  essential for the uptake of deuterium-labeled trimethyllysine [2H9]-TML by
  isolated mitochondria"].
- Added `GO:7770027` for dimethylarginine transport because the same isolated
  mitochondria assay showed SLC25A45-dependent uptake of both ADMA and SDMA
  [PMID:41075794, "SLC25A45 was also required for the mitochondrial uptake of the
  deuterium-labeled dimethylarginine isomers, asymmetric dimethylarginine
  ([2H6]-ADMA) and symmetric dimethylarginine ([2H6]-SDMA)"].
- Added `GO:0005743` mitochondrial inner membrane. SLC25A45-FLAG colocalized
  with mitochondria and SLC25A45 pull-downs recovered mitochondrial inner-membrane
  proteins, which is also the expected location for an SLC25 transporter
  [PMID:41075794, "WT SLC25A45-FLAG and SLC25A45R285C-FLAG interacted with IMM
  proteins"].
- Added `GO:0045329` carnitine biosynthetic process. This is a direct participation
  row: SLC25A45 is the transporter that supplies mitochondrial TML to TMLHE, not
  just a perturbation whose loss changes carnitine abundance. Dias et al. showed
  that BBOX1 plus SLC25A45 restored labeled carnitine production in AsPC-1 cells
  and that SLC25A45 loss or siRNA limited labeled carnitine production in OVCAR-3
  and Kuramochi cells [PMID:41075794, "Together, these results show that SLC25A45
  is required for the de novo biosynthesis of carnitine in BBOX1-expressing cells"].

## GO-CAM 69169b7400000023 consistency

- Once this review merges, the SLC25A45 activity in
  `gocams/69169b7400000023/69169b7400000023-review.yaml` can move from
  `NO_GENE_REVIEW` to `CONSISTENT`: the model already uses `GO:7770026` in the
  mitochondrial inner membrane and places the transported trimethyllysine in the
  matrix for TMLHE.
- Running issue for the final GO-CAM consistency PR: the model locates the
  pre-import trimethyllysine input in broad `GO:0005737` cytoplasm. This should
  be sharpened to cytosol or mitochondrial intermembrane space if the GO-CAM
  molecule-location pattern supports the distinction.
