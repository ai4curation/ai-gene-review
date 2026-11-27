# CAC2 curation notes

## 2026-10-01 update: GOA refresh and PTHR15271 IBA review

- Force-refreshed CAC2 from QuickGO and UniProt. Current GOA still has 21
  rows, all already represented in the review, so no new live rows or stale
  source rows needed resolution.
- Re-read cached PTHR15271 PAINT. All three live IBA rows, `GO:0005634`
  nucleus, `GO:0006334` nucleosome assembly, and `GO:0033186` CAF-1 complex,
  trace to `PANTHER:PTN000392175`, the eukaryotic CAF-1 subunit B/Cac2 node,
  and all are sound transfers for the yeast CAF-1 p60 subunit.
- Searched for newer CAC2/CAF-1 literature. The 2024 yeast CAF-1/PCNA
  structural paper, PMID:38969056, resolves the Cac1 PIP-motif interaction
  with PCNA; it supports the existing CAF-1 replication-coupling model but does
  not add a distinct Cac2 molecular function.
- Left all existing action calls unchanged. The three generic `GO:0005515`
  Cac2-Msi1/Cac3 rows are already `REMOVE`, the nucleosome and broad
  DNA-replication rows are already scoped down, and the two conservative `NEW`
  proposals for H3-H4 chaperone contribution and subtelomeric heterochromatin
  remain supported by cached primary literature.
