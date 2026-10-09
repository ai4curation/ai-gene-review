# PIWIL2 review notes

- Deep research: SKIPPED (falcon times out in this environment; perplexity-lite not installed). No deep-research file was generated or fabricated.
- Evidence sources: cached publications (`just fetch-gene-pmids human PIWIL2`), the UniProt record (PIWIL2-uniprot.txt), and additional mouse/fly
  primary papers fetched with `just fetch-pmid` (e.g. PMID:18922463, PMID:22020280, PMID:29437694, PMID:20011505, PMID:22902557).
- Reviewed as an exemplar for a generalized animal piRNA silencing module.

## Key points
- Slicer-competent cytoplasmic PIWI in nuage/pi-bodies; feeds ping-pong and loads PIWIL4 [PMID:29437694 "The slicer activity of MILI is essential for secondary piRNA biogenesis and the ping‐pong cycle"].
- Mili DAH knock-in: loss of amplification, LINE1 derepression, sterility [PMID:22020280 "The defective piRNA pathway in Mili(DAH) mice results in spermatogenic failure and sterility."].
- MIWI2 nuclear entry depends on MILI [PMID:18922463 "MIWI2, whose nuclear localization and association with piRNAs depend upon MILI"].
- Nucleus IDA (PMID:28025795) is from an abstract-only paper on HIWI2/PIWIL4; kept as non-core, not overruled.
