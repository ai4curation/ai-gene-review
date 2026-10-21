# Executed DYRK1A extraction

The saved-input replay and independent projection comparison passed. All results below come from the fixed source snapshots, with no retrieval, new quotations or annotation decisions.

| Dataset/view | Target incident/context rows | Selected rows |
|---|---:|---:|
| AP-MS graph | 9 | 2 |
| OpenCell | 5 | 1 |
| Table S3, data | 124 | 124 |
| mmc4, Datasets_Summary | 2 | 0 |
| mmc4, Interactor_Lists | 3589 | 24 |
| mmc4, Interactor_Frequency | 604 | 12 |
| mmc4, Interaction_Annotations | 604 | 12 |

Table S3 preserves 31 columns per target row and the exact source labels: DYRK1A: 75, DYRK1A delta polyHis: 46, DYRK1A isoforme 3: 3. These are distinct assay labels, not a claim that all records assayed the same product.

The mmc4 dataset summary retains the two source labels; the partner filters select 12 names. All 3,589 list-context rows, 604 frequency-context rows and 604 annotation-context rows remain in the machine-readable output. No repeated source view is promoted into an independent experiment.

## Selected AP-MS records

| Edge | Source endpoint | Target endpoint |
|---:|---|---|
| 607530 | LZTS2 | DYRK1A |
| 588788 | DCAF7 | DYRK1A |

The original endpoint and node bait attributes are retained in RESULTS.json. The graph has 7543 nodes and 36842 edges; no missing identifier is invented.

## Selected OpenCell record

| Physical line | Data index | Bait | Interactor | pval field | Enrichment |
|---:|---:|---|---|---|---|
| 7906 | 7904 | DYNLL1 | DYRK1A | 14.7930205375584 | 3.12288558273414 |

The complete accession group and both stoichiometry fields are retained in RESULTS.json; no isoform assignment or statistical transformation is made.

## Selected mmc4 annotation view

| Worksheet row | Index protein | Interactor | logFCs | InWeb | BioPlex |
|---:|---|---|---:|---|---|
| 394 | DYRK1A | DCAF7 | 0.972 | True | True |
| 417 | DYRK1A | DYNLL1 | 0.918 | True | True |
| 426 | DYRK1A | ELAVL2 | 0.86 | False | False |
| 427 | DYRK1A | ELAVL3 | 0.856 | False | False |
| 442 | DYRK1A | FAM53C | 1.96 | True | True |
| 445 | DYRK1A | FMR1 | 0.743 | False | False |
| 506 | DYRK1A | IGF2BP1 | 1.09 | False | False |
| 507 | DYRK1A | IGF2BP2 | 0.963 | False | False |
| 508 | DYRK1A | IGF2BP3 | 0.883 | False | False |
| 739 | DYRK1A | SATB1 | 1.31 | False | False |
| 817 | DYRK1A | TRIP12 | 0.602 | False | False |
| 869 | DYRK1A | ZMYND8 | 0.99 | False | False |

These flags and values are copied from source cells, without imposing a new interpretation. Full list/frequency/annotation cells and all 124 Table S3 rows are in RESULTS.json.

## Execution checks

The original saved graph/CSV projections match exactly. The 124 Table S3 rows and all headers, target rows, selected rows and counts in all four mmc4 sheets match the independent owner projections. Extraction never reads those projections. A relocated replay passed. Empty partner filters returned zero selected graph/CSV/mmc4 partner rows while preserving incident context; a changed input was rejected by its hash. No canonical validation suite or source mutation was performed.
