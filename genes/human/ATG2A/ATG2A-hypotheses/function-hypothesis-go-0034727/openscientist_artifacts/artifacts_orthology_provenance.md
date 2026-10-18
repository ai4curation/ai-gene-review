# Provenance: orthology of PMN-defining machinery + IBA annotation source

Queried Iteration 2. Tools: EBI QuickGO REST, UniProtKB REST, PANTHER v19 ortholog API.

## A. Source of the human ATG2A GO:0034727 annotation (QuickGO)
Endpoint: `QuickGO/services/annotation/search?geneProductId=UniProtKB:Q2TAZ0&goId=GO:0034727`
- hits: 1
- **evidence: IBA** | assignedBy: **GO_Central** | reference: **GO_REF:0000033** (PAINT/phylogenetic)
- **withFrom: PANTHER:PTN000324023 and SGD:S000005186 (yeast ATG2)**

=> The annotation is a phylogenetic (PAINT/IBA) propagation from yeast ATG2, matching the seed's stated PANTHER node exactly. No experimental (EXP/IDA/IMP/IGI/IPI) support in human.

## B. Accession verification (UniProtKB, reviewed, S. cerevisiae 559292)
| Gene | Correct accession | Protein name |
|---|---|---|
| ATG2 | P53855 | Autophagy-related protein 2 |
| NVJ1 | **P38881** | Nucleus-vacuole junction protein 1 |
| VAC8 | P39968 | Vacuolar protein 8 |
| SEC17 | P32602 | Alpha-soluble NSF attachment protein |

Note: an initial run mistakenly used P32602 for NVJ1; P32602 is actually **SEC17 (α-SNAP)**, which spuriously mapped to human NAPA/NAPB. Corrected below.

## C. PANTHER v19 ortholog test (yeast 559292 -> human 9606)
Endpoint: `pantherdb/ortholog/matchortho?geneInputList=<acc>&organism=559292&targetOrganism=9606`

| Yeast gene | Accession | Human ortholog(s) | Type |
|---|---|---|---|
| **ATG2** (positive control) | P53855 | **ATG2A** (Q2TAZ0), **ATG2B** (Q96BY7) | LDO / O |
| **NVJ1** | P38881 | **none** | — |
| **VAC8** | P39968 | **none** | — |

Positive control validates the method (yeast ATG2 correctly recovers human ATG2A as least-diverged ortholog).

## Interpretation
The lipid-supply/tether component (ATG2) is conserved yeast→human, but the two proteins that **define** the PMN nucleus–vacuole junction (Nvj1, Vac8) have **no human ortholog**. Combined with the absence of a vacuole in mammals, this is a **demonstrated mechanistic lineage restriction** of the GO:0034727 route — not merely an absence of experiments. The human ATG2A PMN annotation is therefore an IBA over-propagation of a fungal-specific process.
