# GATA1 external target evidence

This file preserves small target subsets and source-specific interpretation from original supplementary tables. It supplements the publication caches; gene-level or fusion-protein experiments are not promoted to physiological binding or exact natural-isoform specificity.

## HI-II-14 interaction network — PMID:25416956

[Original article and supplementary data](https://pmc.ncbi.nlm.nih.gov/articles/PMC4266588/). The retained original supplementary Table S2 workbook has SHA256 `0a7157f64a1dd4006f3f0081b9c6c82f793985065cad98049a09454a27bc840c`. Sheet `2G` rows 1869–1877 contain the following literal fields (spreadsheet row numbers are one-based):

| Row | entrez_gene_ida | entrez_gene_idb | gene_symbol_a | gene_symbol_b | screens_found |
|---:|---:|---:|---|---|---:|
| 1869 | 2623 | 3198 | GATA1 | HOXA1 | 2 |
| 1870 | 2623 | 5565 | GATA1 | PRKAB2 | 1 |
| 1871 | 2623 | 10817 | GATA1 | FRS3 | 1 |
| 1872 | 2623 | 55698 | GATA1 | RADIL | 1 |
| 1873 | 2623 | 83899 | GATA1 | KRTAP9-2 | 1 |
| 1874 | 2623 | 85302 | GATA1 | FBF1 | 1 |
| 1875 | 2623 | 124790 | GATA1 | HEXIM2 | 1 |
| 1876 | 2623 | 149473 | GATA1 | CCDC24 | 1 |
| 1877 | 2623 | 386680 | GATA1 | KRTAP10-5 | 1 |

The available Table S2, sheet `2B`, GATA1 library clone ORF6313 (row 17321; 1,008 nucleotides including its stop codon) translates to 335 residues, exactly matching current P15976-2. Sheet `2G` records genes rather than a clone assignment for each pair, so this library observation does not establish per-pair isoform specificity. Original Results 15–16, Methods 45 and supplementary Methods §3 describe human ORFs assayed as yeast fusion proteins. Every published positive pair underwent individual quadruplicate retesting, requiring at least 3/4 positive results, absence of autoactivation on counterselection and sequence-confirmed identities. The `screens_found` column counts discovery screens, not technical retests. No pair-specific S2C orthogonal validation was identified for these nine pairs. These validated binary contacts support partner-class binding terms for HOXA1 and HEXIM2; generic sibling removals concern informativeness rather than rejection of their positive assays.

The retained later HuRI accession/ORF crosswalk corroborates eight incoming partner identities. This is an identity crosswalk, not a second independent interaction experiment:

| Incoming accession | Retained later accession | ORF | 2B header row | Entrez gene |
|---|---|---:|---:|---:|
| O43559 | uniprotkb:O43559 | 2917 | 11369 | 10817 |
| O43741 | uniprotkb:O43741-1 | 11857 | 26171 | 5565 |
| P49639 | uniprotkb:P49639 | 10057 | 23775 | 3198 |
| P60370 | uniprotkb:P60370 | 56518 | 5773 | 386680 |
| Q8N4L8 | uniprotkb:Q8N4L8-1 | 9921 | 23553 | 149473 |
| Q96JH8 | uniprotkb:Q96JH8-4 | 54154 | 2437 | 55698 |
| Q96MH2 | uniprotkb:Q96MH2 | 12696 | 27265 | 124790 |
| Q9BYQ4 | uniprotkb:Q9BYQ4 | 53991 | 2233 | 83899 |

The retained main [UniProt Q8TES7 record](https://www.uniprot.org/uniprotkb/Q8TES7/entry) directly identifies human FBF1, GeneID 85302/HGNC 24674, and declares Q8TES7-6 via VSP_041555/VSP_040770. Its interaction section explicitly lists that isoform with GATA1/P15976 (IntAct EBI-10244131/EBI-3909284). The exact retained record is Git blob `44f7089e7dd2765736b4d3fa1fd50347f14f88fb` at `genes/human/FBF1/FBF1-uniprot.txt`, entry 163 dated 2026-09-02, SHA256 `6924de9cd43e7cf1d4e0e7dc7424782155c41247017c997a27c3da4dbe5ed701`. This direct identity matches Table S2G row 1874; it is not an assignment by elimination. Exact sequence equivalence between the pair-specific 2014 clone and Q8TES7-6 remains unproven. The original accession suffix and positive assay remain intact when generic protein binding is removed. The current Q96JH8 context is conserved separately from the later Q96JH8-4/ORF54154 mapping to RADIL.

## NRF2 binary screen — PMID:32911434

[Original article](https://pubmed.ncbi.nlm.nih.gov/32911434/), supplementary workbook `mmc2.xlsx`, retained SHA256 `80b0e2e34d005ab91f461577a05a945ee23861110e6b753a0519465310577e97`. Table S1 row 2 contains:

| Binary Partner | Gene ID | Prediction Source | Y2H Positive |
|---|---:|---|---|
| GATA1 | 2623 | C. elegans interolog, CCSB | Yes |

Table S2 lists `pACTBE-B-GATA1` at row 41 and `pCMV-mCherry-GATA1` at row 122. Selected Results 2.1 and Methods 4.3.1–4.3.2 describe human partner ORFs, NRF2 full-length/fragments, autoactivation exclusion and independent ADE2/HIS3 readouts. The GATA1 Y2H result is directly recorded. Aggregate co-immunoprecipitation, FCCS or DULIP validation counts are not assigned to GATA1 without a specific result. Table S3 gene–disease entries are computational annotations rather than additional interaction experiments.

## Mutant SPOP interaction — PMID:35512704

[Original article and supplementary data](https://pubmed.ncbi.nlm.nih.gov/35512704/). Supplement 9 SHA256 `b096e65923582a67bcebb87762f37afb256e016e27f59dc4f9b76ab7b7ed6823`, sheet `S3B_SPOPF133L GoPPI evaluation`, row 8 contains:

| prot1 | prot2 | GST-PD_HEK293T | NanoPCA_HCT116 | flag-SPOP-F133L semi-IP_LNCaP C4-2 cells | endogenous-coIP |
|---|---|---|---|---|---|
| SPOP-F133L | GATA1 | positive | positive | N/A | N/A |

Supplement 10 SHA256 `7a66534eb262ed6c7c6940bc077c57fc18f6150024fd4f99f42dfd7c5bd7e19c`, sheet `SPOP-F133L_LNCaP C4-2 cells`, row 8 records signal 1992.75, controls 24 and 534.75, fold change 3.72650771388499, P = 0.000204235385344806, q = 0.000379294287068926, SS = 1 and HC = 1. These are engineered mutant-context NanoPCA/lysate pulldown results. The experiment does not establish wild-type SPOP binding, a purified binary affinity or GATA1 ubiquitin-ligase function. The positive detection is retained even though uninformative generic protein binding is removed.
