# Q25022 notes

## 2026-11-23

- Started the HAECO beta-tubulin review with UniProt `Q25022`, a 448 aa
  full-length sequence traced by UniProt to EMBL `M76491` and protein
  `AAA29168.1`. The UniProt gene name `tub12-16` corresponds to the beta 12-16
  cDNA cloned by Geary et al. in their three-cDNA H. contortus beta-tubulin
  study [PMID:1741017 Three beta-tubulin cDNAs from the parasitic nematode
  Haemonchus contortus., "We have cloned and sequenced three beta-tubulin cDNAs
  from this organism, beta 12-16, beta 12-164, and beta 8-9."].
- `just paint-losses HAECO Q25022` reported that `Q25022` is in PANTHER
  `PTHR11588` but not as a leaf of the cached PAINT tree, and found no IRD or
  IKR loss on the gene lineage.
- The review treats `Q25022` as the full-length beta 12-16 cDNA, distinct from
  the beta 12-164 and beta 8-9 cDNAs in the same paper and from the later
  `A2TF56` resistant-isolate isotype-1 allele. Live UniProt and QuickGO, release
  2026_04, show seven GOA rows on `Q25022`: the beta-tubulin molecular and
  microtubule rows plus a broad GO_REF:0000108 `cytoskeleton organization`
  inference.
- Reading the local `Q25022-uniprot.txt` `SQ` block gives Phe167, Glu198 and
  Phe200, so this cDNA carries the F/E/F pattern at the three common
  beta-tubulin benzimidazole-resistance positions. In the 161-200 segment,
  `DRIMSSFSVV` places Phe at position 167 and `QLVENTDETF` places Glu198 and
  Phe200.
- Reused the A2TF56 ungapped beta-tubulin mapper under
  `Q25022-bioinformatics/benzimidazole_resistance/`. The run mapped Q25022
  against A2TF56, Geary et al.'s full-length tub8-9 cDNA, a short susceptible
  isotype-1 fragment, and C. elegans BEN-1. Q25022 aligns without indels to
  A2TF56 and tub8-9 but is only 421/448 and 420/448 identical to them,
  respectively, so the review keeps it as the beta 12-16 cDNA and records the
  modern isotype/locus assignment as unresolved.
- Updated the review to foreground Geary et al.'s population conclusion:
  beta 12-16-like sequences were detected in both benzimidazole-sensitive and
  resistant H. contortus populations, while a beta 8-9-related product was the
  possible resistant-population difference. The Q25022 suggested question now
  asks which modern beta-tubulin locus or isotype class, if any, corresponds to
  beta 12-16 rather than presupposing that beta 12-16 is the
  benzimidazole-resistance isotype.
