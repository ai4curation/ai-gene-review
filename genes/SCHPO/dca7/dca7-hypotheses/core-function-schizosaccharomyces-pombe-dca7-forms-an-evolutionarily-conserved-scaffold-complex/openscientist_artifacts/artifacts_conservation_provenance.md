# Provenance: Dca7 DCAF7/WDR68-family conservation & interaction concordance

Computed during Iteration 3 (all values retrieved/computed programmatically; no fabrication).

## 1. Sequence conservation (global Needleman–Wunsch, BLOSUM62, gap −11/−1)

| Pair | UniProt accessions | % identity | Aligned columns | Score |
|------|--------------------|-----------|-----------------|-------|
| Dca7 (S. pombe) vs DCAF7/WDR68 (human) | O74763 (435 aa) vs P61962 (342 aa) | 44.2% | 328 | 481 |
| Dca7 (S. pombe) vs YPL247C (S. cerevisiae) | O74763 vs Q12523 (523 aa) | 37.5% | 413 | 430 |
| DCAF7 (human) vs YPL247C (S. cerevisiae) | P61962 vs Q12523 | 42.7% | 328 | 361 |

Interpretation: ~38–44% identity across the shared ~330-aa WD40 β-propeller core (InterPro IPR045159 "DCAF7-like") among three species separated by ~1 Gy — well above chance — confirms genuine orthology. Length differences reflect N/C-terminal extensions.

## 2. Domain / family assignment

- Dca7 (O74763): InterPro IPR045159 (DCAF7-like), IPR001680 WD40 repeat, PF00400 WD40, Gene3D 2.130.10.10 (7-bladed β-propeller). PomBase 1:1 orthologs: human DCAF7 (HGNC:30915), Sc YPL247C.
- ppk15 (SPAC823.03): catalytic domain CDD cd14212 **PKc_YAK1**; PANTHER IPR050494 Ser/Thr dual-specificity kinase. Orthologs: human DYRK1A (HGNC:3091), DYRK1B (HGNC:3092), Sc Yak1 (YJL141C).

## 3. Interaction concordance across lineages

| Species | Scaffold | Kinase | Evidence | Score/subscore |
|---------|----------|--------|----------|----------------|
| Human | DCAF7/WDR68 | DYRK1A/DYRK1B | Direct co-IP/mapping (PMID 21777625) | qualitative direct |
| S. cerevisiae | YPL247C | Yak1 | STRING v12 aggregate | combined 0.996 / exp 0.979 |
| S. pombe | dca7 | ppk15 | Binary Y2H (PMID 26771498) + STRING | combined 0.933 / exp 0.873 |

## 4. GO annotation state (QuickGO, O74763)

- MF root GO:0003674 = ND (GO_REF:0000015) — no experimental MF.
- BP root GO:0008150 = ND (GO_REF:0000015) — no experimental BP.
- CC GO:0080008 Cul4-RING E3 ubiquitin ligase complex = ISS (ECO:0000250) from human DCAF7 (UniProtKB:P61962).
- CC GO:0005634 nucleus = IBA (ECO:0000318, GO_Central).
- CC GO:0005737 cytoplasm, GO:0005794 Golgi = IEA (UniProtKB-SubCell).

## Methods / sources
UniProt REST (sequences, domains), PomBase API v1 (orthologs, interactions, phenotypes), STRING v12 REST network API, EBI QuickGO annotation API, NCBI eSummary (PMID titles). Alignment implemented in numpy (Gotoh affine-gap NW with BLOSUM62). AlphaFold static PDB URLs returned 404 (DB versioning); pLDDT not reported to avoid an unverified value.
