# CEK1 curation notes

## 2026-10-10

- Fetched the `CANAL/CEK1` review, GOA, UniProt, and nine cached GOA PMIDs for the
  fungal PTHR24055 MAPK PAINT project.
- Deep research via Falcon with `perplexity-lite` fallback could not run in this
  environment because no research provider API keys were configured, so the review
  was based on the cached primary publications, UniProt, the local PAINT export,
  and a fresh literature search.
- Accepted the broad `PANTHER:PTN000622075` IBA placements for
  `GO:0004674`, `GO:0005634`, and `GO:0005737`; this ancestor transfers only
  shared MAPK catalytic activity and broad nucleo-cytoplasmic activity.
- Accepted the narrower fungal `PANTHER:PTN001172087`
  `GO:0071507` pheromone response MAPK cascade IBA. CEK1 is not the only Candida
  mating MAPK, but the MAPK node placement is supported by the direct mating
  defect of `cek1` and the stronger defect of the `cek1 cek2` double mutant.
- Kept direct Candida phenotypes separate from core MAPK function:
  starvation/serum filamentation and cell-wall mannan defects were retained as
  major Cek1 outputs, the zebrafish phagocytosis phenotype was kept as non-core,
  and the 2007 CaFT xenobiotic row was left `UNDECIDED` because Table S1 is not
  cached and the article body does not mention `CEK1`.
- Removed the 2025 Num11-backed `cell wall modification` row from CEK1. That
  paper uses phospho-Cek1 as a downstream readout of a `NUM11` deletion and
  supports the upstream Num11-to-Cdc42/Cek1 model, not an IMP annotation on CEK1.
- A fresh search surfaced 2025 small-molecule and Num11 papers that mention CEK1
  pathway expression or phosphorylation; no newer primary CEK1 loss/add-back
  paper was found that should supersede the cached GOA evidence.
