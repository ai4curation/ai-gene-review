# PIWIL4 review notes

- Deep research: SKIPPED (falcon times out in this environment; perplexity-lite not installed). No deep-research file was generated or fabricated.
- Evidence sources: cached publications (`just fetch-gene-pmids human PIWIL4`), the UniProt record (PIWIL4-uniprot.txt), and additional mouse/fly
  primary papers fetched with `just fetch-pmid` (e.g. PMID:18922463, PMID:22020280, PMID:29437694, PMID:20011505, PMID:22902557).
- Reviewed as an exemplar for a generalized animal piRNA silencing module.

## Key points
- Nuclear, slicer-dispensable effector directing de novo TE DNA methylation [PMID:22020280 "Surprisingly, homozygous Miwi2(DAH) mice are fertile, transposon silencing is established normally and no defects in secondary piRNA biogenesis are observed."].
- In somatic cancer cells Hiwi2 is mostly cytoplasmic and binds tRNA-derived piRNAs [PMID:25038252 "the bulk of somatic Hiwi2 resides in the cytoplasm"].
- RNA endonuclease IBA marked over-annotated (FUNCTIONAL_DIVERGENCE); NOT-endonuclease ISS accepted. The validator's same-term consistency warning is expected (positive vs NOT row).
