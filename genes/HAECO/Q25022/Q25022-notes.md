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
  Phe200, so this cDNA carries the wild-type residues at the three canonical
  benzimidazole-resistance positions. In the 161-200 segment, `DRIMSSFSVV`
  places Phe at position 167 and `QLVENTDETF` places Glu198 and Phe200.
