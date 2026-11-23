# A2TF56 notes

## 2026-11-23

- Started the HAECO beta-tubulin review with UniProt `A2TF56`, the 448 aa
  full-length sequence traced by UniProt to EMBL `EF198865` and protein
  `ABM92348.1`. The UniProt submission title identifies the source as a
  benzimidazole-resistant India isolate beta-tubulin isotype-1 gene.
- `just paint-losses HAECO A2TF56` reported that `A2TF56` is in PANTHER
  `PTHR11588` but not as a leaf of the cached PAINT tree, and found no IRD or
  IKR loss on the gene lineage.
- The review treats `A2TF56` as a complete H. contortus beta-tubulin
  isotype-1 sequence, not as the older beta 12-16, beta 12-164 or beta 8-9
  cDNAs cloned in the Geary et al. 1992 study [PMID:1741017 Three
  beta-tubulin cDNAs from the parasitic nematode Haemonchus contortus., "We
  have cloned and sequenced three beta-tubulin cDNAs from this organism, beta
  12-16, beta 12-164, and beta 8-9."].
- Kwa et al. 1993 supports H. contortus beta-tubulin isotype-1 as a key
  benzimidazole-resistance locus: resistant populations usually retained one
  beta-tubulin isotype-1 gene and the retained selected fragments were
  transcribed and SL1-spliced [PMID:8366887 Molecular characterisation of
  beta-tubulin genes present in benzimidazole-resistant populations of
  Haemonchus contortus., "There was a reduction in beta-tubulin isotype 1
  genes to usually one, in BZ-resistant populations."]. This supports the
  anthelmintic-target lane, but it does not directly assay the later `A2TF56`
  allele.
- A2TF56's direct GenBank record does not assign a community gene symbol beyond
  "beta tubulin isotype 1", so the review keeps the UniProt accession as
  `gene_symbol`. The 1993 isotype-1 genomic clone was `gru-1`, and the older
  tub8-9 cDNA was the nearest full-length H. contortus isotype-1-like
  comparator for the A2TF56 sequence.
- Added a reproducible alignment under `A2TF56-bioinformatics/` to check the
  benzimidazole-resistance codons. A2TF56 maps without indels to the Geary
  tub8-9 cDNA and maps the partial susceptible isotype-1 fragment MF034043.1 to
  residues 152-245; A2TF56 retains Phe167 and Glu198 and carries Tyr200 where
  the susceptible fragment and tub8-9 encode Phe. This makes A2TF56 an F200Y
  resistant-isolate allele by sequence, although direct benzimidazole binding
  or polymerization assays on this exact submitted allele were not reported.
