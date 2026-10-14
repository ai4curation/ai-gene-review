---
title: "Are PDB structure papers overlooked by GO/MOD curation?"
species: [ARATH, human]
---
# Are PDB structure papers overlooked by GO/MOD curation?

Per (gene, structure-paper) status: is the structure's primary publication cited in the gene's GOA REFERENCE column?

- Structure papers assessed (gene x PMID pairs): **1668** across **573** genes
- **CITED** by GOA: **317** (19%)
- **GAP_OPPORTUNITY** (not cited; gene curated experimentally after the structure's year): **1051** (63%)
- **GAP_LAG** (not cited; structure newer than latest GOA annotation): **61** (4%)
- **GAP_NO_EXP_CURATION** (not cited; gene has no experimental GO annotations at all): **236** (14%)
- NO_GOA_FILE (could not assess): **3**

Genes where **no** structure paper is cited by GOA: **353** / 573.

## Interpretation

`GAP_OPPORTUNITY` is the headline signal: the structure's paper existed while the gene was being experimentally curated, yet no GO annotation references it. These are the strongest candidates for structural evidence that curation overlooked. `GAP_LAG` is excusable curation latency; `GAP_NO_EXP_CURATION` reflects genes that received only electronic annotation (a different problem). Caveat: 'not cited' means the structural study is absent from the evidence trail, not necessarily that the function is unannotated.

## Top GAP_OPPORTUNITY structure papers (by number of deposited structures)

Genes with many deposited structures sharing an uncited primary publication, despite later experimental GO curation -- the best targets to fold structural evidence into review.

| gene | organism | structure paper | paper yr | # structures | latest exp. curation |
| --- | --- | --- | --- | --- | --- |
| IMPDH1 | human | PMID:35013599 | 2022 | 12 | 2025 |
| IMPDH2 | human | PMID:31999252 | 2020 | 10 | 2026 |
| COP1 | ARATH | PMID:31304983 | 2019 | 9 | 2025 |
| GCH1 | human | PMID:33229582 | 2020 | 9 | 2025 |
| MCCC1 | human | PMID:39223421 | 2025 | 9 | 2026 |
| ACLY | human | PMID:28777081 | 2017 | 8 | 2026 |
| AP1S3 | human | PMID:36269825 | 2022 | 8 | 2026 |
| ATP5F1E | human | PMID:37244256 | 2023 | 8 | 2026 |
| ATP5PO | human | PMID:37244256 | 2023 | 8 | 2026 |
| CPS1 | human | PMID:25111069 | 2014 | 8 | 2026 |
| BIRC5 | human | PMID:22357620 | 2012 | 7 | 2026 |
| CASP3 | human | PMID:15115390 | 2004 | 7 | 2026 |
| FDPS | human | PMID:16892359 | 2006 | 7 | 2026 |
| FTH1 | human | PMID:17070541 | 2007 | 7 | 2025 |
| HTT | human | PMID:19748341 | 2009 | 7 | 2025 |
