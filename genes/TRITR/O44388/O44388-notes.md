# O44388 notes

## 2026-11-23

- Started the TRITR beta-tubulin review with UniProt `O44388`, a Swiss-Prot
  444 aa T. trichiura beta-tubulin sequence traced to EMBL `AF034219` and
  protein `AAB99949.1` from Bennett et al. 1999 [PMID:10514087 A
  beta-tubulin gene from Trichuris trichiura., "A beta-tubulin gene from
  Trichuris trichiura."].
- `just paint-losses TRITR O44388` reported that `O44388` is in PANTHER
  `PTHR11588` but not as a leaf of the cached PAINT tree, and found no IRD or
  IKR loss on the gene lineage.
- Live UniProt and QuickGO, release 2026_04, show seven GOA rows on `O44388`:
  the beta-tubulin molecular and microtubule rows, a broad
  GO_REF:0000044 `cytoskeleton` row, a GO_REF:0000108 `cytoskeleton
  organization` inference, and a broad InterPro `microtubule-based process`
  row.
- Reading the local `O44388-uniprot.txt` `SQ` block gives Phe167, Glu198 and
  Phe200. In the 161-200 segment, `DRIMTTFSVV` places Phe at position 167 and
  `QLVENTDETF` places Glu198 and Phe200.
- The Bennett et al. PMID is abstractless in PubMed and has no PMC record in the
  cache, so the review uses it only as publication provenance for the T.
  trichiura beta-tubulin gene and relies on the Swiss-Prot record's free-text
  beta-tubulin synthesis plus InterPro/SMART/Pfam signatures for function.
