# piwi review notes

- Deep research: SKIPPED (falcon times out in this environment; perplexity-lite not installed). No deep-research file was generated or fabricated.
- Evidence sources: cached publications (`just fetch-gene-pmids DROME piwi`), the UniProt record (piwi-uniprot.txt), and additional mouse/fly
  primary papers fetched with `just fetch-pmid` (e.g. PMID:18922463, PMID:22020280, PMID:29437694, PMID:20011505, PMID:22902557).
- Reviewed as an exemplar for a generalized animal piRNA silencing module.

## Key points
- Nuclear co-transcriptional TE silencer; slicer dispensable [PMID:22902557 "Mature Piwi-RISC triggers TE silencing by an unknown mechanism that requires Piwi’s nuclear localization but not its slicer activity"].
- 14 generic protein-binding IPIs removed as uninformative (partners Papi, Vret, Panx, Nxf2, Nup358 etc.).
- Chromatin DNA binding (DamID) marked over-annotated: the paper itself notes RNA- not DNA-mediated chromatin contact.
