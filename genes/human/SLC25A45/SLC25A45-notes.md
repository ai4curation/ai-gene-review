# SLC25A45 notes

## Setup

- `just fetch-gene human SLC25A45` initially created the UniProt record, a
  header-only GOA table, and the initialized review file. After GOA caught up
  with the 2025-2026 SLC25A45 curation, `just fetch-gene human SLC25A45
  --force` fetched 19 rows for Q8N413; all rows in the refreshed GOA cache are
  now adjudicated as existing annotations.
- `just fetch-pmid 41505503` cached the Banks et al. Science 2026 record cited
  by UniProt; no PMC record was available, so only the PubMed abstract is used.
- The first `just fetch-gene-pmids human SLC25A45` run found no PMID-backed GOA
  rows because it was run before the GOA refresh.
- `just deep-research-falcon human SLC25A45 --fallback perplexity-lite` could not
  run because `agentapi` was not on `PATH` and the configured fallback provider
  was unavailable. I used the cached full text for PMID:41075794 and PMID:41075780
  and the freshly fetched UniProt entry for Q8N413 instead.

## Curation decisions

- Accepted `GO:7770026` for N(6),N(6),N(6)-trimethyl-L-lysine transport because
  isolated mitochondria expressing SLC25A45-8xHis imported labeled TML while
  matched controls did not [PMID:41075794, "Expression of SLC25A45-8xHis was
  essential for the uptake of deuterium-labeled trimethyllysine [2H9]-TML by
  isolated mitochondria"], and both Khan et al. and Banks et al. independently
  support SLC25A45 as a mitochondrial TML carrier.
- Accepted `GO:7770027` for dimethylarginine transport because the same isolated
  mitochondria assay showed SLC25A45-dependent uptake of both ADMA and SDMA
  [PMID:41075794, "SLC25A45 was also required for the mitochondrial uptake of the
  deuterium-labeled dimethylarginine isomers, asymmetric dimethylarginine
  ([2H6]-ADMA) and symmetric dimethylarginine ([2H6]-SDMA)"].
- Accepted `GO:0005743` mitochondrial inner membrane. SLC25A45-FLAG colocalized
  with mitochondria and SLC25A45 pull-downs recovered mitochondrial inner-membrane
  proteins, which is also the expected location for an SLC25 transporter
  [PMID:41075794, "WT SLC25A45-FLAG and SLC25A45R285C-FLAG interacted with IMM
  proteins"].
- Accepted `GO:0045329` carnitine biosynthetic process. This is a direct participation
  row: SLC25A45 is the transporter that supplies mitochondrial TML to TMLHE, not
  just a perturbation whose loss changes carnitine abundance. Dias et al. showed
  that BBOX1 plus SLC25A45 restored labeled carnitine production in AsPC-1 cells
  and that SLC25A45 loss or siRNA limited labeled carnitine production in OVCAR-3
  and Kuramochi cells [PMID:41075794, "Together, these results show that SLC25A45
  is required for the de novo biosynthesis of carnitine in BBOX1-expressing cells"].
- Accepted the `GO:0005739` mitochondrial root rows rather than modifying them to
  `GO:0005743`: under the root-organelle policy, mitochondrion is an informative
  location even when the inner-membrane sublocation is also asserted.
- Marked `GO:0022857`, `GO:0031966`, `GO:0055085`, and `GO:0003333` as
  `TOO_GENERAL` because the refreshed review now carries substrate-specific
  transporter activities, `GO:1902475` L-alpha-amino acid transmembrane
  transport, and mitochondrial inner-membrane rows.
- The two FlyBase-assigned human IMP rows from PMID:41505503 are biologically
  supported but have a `SUSPECTED` `CHECK` source-defect query on their unusual
  `Assigned_By` value.

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
