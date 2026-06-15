# Are PDB structure papers overlooked by GO/MOD curation?

Per (gene, structure-paper) status: is the structure's primary publication cited in the gene's GOA REFERENCE column?

- Structure papers assessed (gene x PMID pairs): **737** across **247** genes
- **CITED** by GOA: **110** (15%)
- **GAP_OPPORTUNITY** (not cited; gene curated experimentally after the structure's year): **478** (65%)
- **GAP_LAG** (not cited; structure newer than latest GOA annotation): **21** (3%)
- **GAP_NO_EXP_CURATION** (not cited; gene has no experimental GO annotations at all): **128** (17%)
- NO_GOA_FILE (could not assess): **0**

Genes where **no** structure paper is cited by GOA: **174** / 247.

## Interpretation

`GAP_OPPORTUNITY` is the headline signal: the structure's paper existed while the gene was being experimentally curated, yet no GO annotation references it. These are the strongest candidates for structural evidence that curation overlooked. `GAP_LAG` is excusable curation latency; `GAP_NO_EXP_CURATION` reflects genes that received only electronic annotation (a different problem). Caveat: 'not cited' means the structural study is absent from the evidence trail, not necessarily that the function is unannotated.

## Top GAP_OPPORTUNITY structure papers (by number of deposited structures)

Genes with many deposited structures sharing an uncited primary publication, despite later experimental GO curation -- the best targets to fold structural evidence into review.

| gene | organism | structure paper | paper yr | # structures | latest exp. curation |
| --- | --- | --- | --- | --- | --- |
| GCH1 | human | PMID:33229582 | 2020 | 9 | 2025 |
| COP1 | ARATH | PMID:31304983 | 2019 | 8 | 2025 |
| BIRC5 | human | PMID:22357620 | 2012 | 7 | 2026 |
| CASP3 | human | PMID:15115390 | 2004 | 7 | 2026 |
| FTH1 | human | PMID:17070541 | 2007 | 7 | 2025 |
| HTT | human | PMID:19748341 | 2009 | 7 | 2025 |
| PNO1 | yeast | PMID:32943521 | 2020 | 7 | 2025 |
| Cftr | mouse | PMID:14685259 | 2004 | 6 | 2025 |
| EIF2AK3 | human | PMID:25587754 | 2015 | 6 | 2026 |
| MAP3K5 | human | PMID:23776076 | 2013 | 6 | 2025 |
| PUS3 | human | PMID:38996458 | 2024 | 6 | 2024 |
| SPR | human | PMID:31244106 | 2019 | 6 | 2025 |
| AIPL1 | human | PMID:28739921 | 2017 | 5 | 2026 |
| CCT7 | yeast | PMID:31492816 | 2019 | 5 | 2025 |
| CCT7 | yeast | PMID:36921056 | 2023 | 5 | 2025 |
