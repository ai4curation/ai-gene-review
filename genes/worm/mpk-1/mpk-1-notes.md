# mpk-1 curation notes

## 2026-09-30 seeded GOA review

Provider deep research was unavailable for this pass. The seeded GO annotations
were reviewed from the local UniProt and GOA snapshots, the twelve cached PMID
records cited by GOA, the reviewed human MAPK1 comparison in this repository, and
local GO-CAM/Reactome checks.

Local GO-CAM search found `gocams/62e3212700001956/62e3212700001956-src.yaml`
mentioning `WB:WBGene00003401` as part of a PAINT/IBA descendant list in a human
NLRP1/ZAKalpha model, but no C. elegans mpk-1-specific production model for the
LET-60/Ras/MPK-1 module. Local Reactome caches did not contain `P39745` or
`WBGene00003401`.

The review keeps the MAP kinase catalytic rows, ATP binding, cytoplasmic/nuclear
activity, the MAPK-cascade row, Ras protein signal transduction, cell-surface
receptor signaling, and generic intracellular signal transduction as core ERK/MAPK
biology. Oocyte maturation, vulval development, ubiquitin-proteasome regulation,
ilys-3 transcriptional activation, and Gram-positive defense rows are supported
outputs of MPK-1 signaling and were marked `KEEP_AS_NON_CORE`. The two IntAct
`protein binding` rows to GLA-3 were marked `REMOVE` because the cited interactome
maps support high-throughput physical interactions rather than a more informative
MPK-1 molecular function.
