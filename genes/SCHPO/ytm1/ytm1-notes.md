# ytm1 notes

## 2026-10-17

- Deep research did not complete: the Falcon wrapper fell back to the lightweight
  provider but the fresh provider environment had no `agentapi` credentials on
  `PATH`. I therefore used cached primary literature and manual PubMed follow-up.
- `ytm1` is in the same `PTHR19855:SF11` WDR12/Ytm1 subfamily as budding-yeast
  YTM1. The three IBA rows are all correct transfers from the fungal
  `PANTHER:PTN000458086` node, not weak pairwise transfers from a sparse
  donor list.
- Ugolini et al. place fission-yeast Ytm1 in early nascent 60S particles:
  "the biogenesis complex Ytm1-Erb1-Ppp1 (Ytm1-Erb1-Nop7 in S. cerevisiae) is
  incorporated" [PMID:36423630]. This directly supports the generic
  `GO:0030684 preribosome` row being replaced by `GO:0030687 preribosome,
  large subunit precursor`, and it also supports the PAINT large-subunit
  biogenesis row.
- The same 2022 study directly adjudicates the chromatin calls: "In wild-type
  cells, Ytm1 is not detectable on chromatin" [PMID:36423630]. That supports
  accepting the PomBase NOT chromatin row and removing the older abstract-only
  high-throughput positive chromatin row from PMID:22146723.
- The original PomBase nucleolar IDA row cites the Rbin/Mdn1 paper. Its cached
  full text only exposes the Ytm1-GFP nucleolar quantitation in the methods, but
  it is consistent with later cryo-EM recovery of Ytm1 in nucleolar nascent
  60S particles.
- I did not propose the S. cerevisiae `GO:0110136 protein-RNA complex
  remodeling` row de novo for fission yeast. The Rea1/Mdn1-Ytm1 mechanism is
  conserved, but the existing PomBase surface already captures the direct
  fission-yeast evidence at the more conservative large-subunit-assembly level.
