# folP (PA4750, Q9HV49) review notes

No deep-research provider was available; notes compiled from the UniProt entry (unreviewed) and the cached abstract.

- DHPS family (TIGR01496, PROSITE PS00792/PS00793, pterin-binding domain). No P. aeruginosa-specific biochemical paper on PA4750 was found in the cache.
- PseudoCAP seed reference: [PMID:1657875 "were purified to homogeneity from crude extracts of Escherichia coli MC4100"]. The paper is about E. coli HPPK and DHPS.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | other seeds | IBD stands without this seed? | verdict | rationale |
|---|---|---|---|---|---|---|---|---|
| PTN000468650 | GO:0004156 dihydropteroate synthase activity | 6 | 118 (98 taxa) | GO:0004156, IDA, PMID:1657875 (PseudoCAP) | E. coli FolP P0AC13, S. pneumoniae SulA P59655, M. tuberculosis FolP1 P9WND1, yeast FOL1 (SGD:S000005200), Arabidopsis AT1G69190 | Yes | WRONG | The cited paper purified DHPS from E. coli MC4100 (stated in the abstract); no P. aeruginosa protein. The claim is still true for PA4750 by family conservation. Node term suits a DHPS clade. |

Defects: PSEUDOCAP WRONG_REFERENCE (CONFIRMED, abstract names E. coli). No GO_CENTRAL defect. Actions: 6 ACCEPT, 2 TOO_GENERAL.
