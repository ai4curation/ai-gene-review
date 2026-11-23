# oprE (OccK8, G3XDA5) review notes

No deep-research provider was available. Literature: Europe PMC search "OccK8" and "OprE AND aeruginosa"
(2026-11-05); fetched PMID:33481046 (abstract). Cached PMID:2120174 (abstract only).

## Function

- OccK-subfamily Occ channel; native protein forms channels [PMID:33481046 "OccK8 (also known as OprE), was investigated using single-channel"].
- Originally protein E1 [PMID:2120174 "decreased amounts of outer membrane proteins C, D2, E1, and E2 lowered the"].
- Physiological substrates not established.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002160747 | GO:0015288 porin activity | 3 | 24 (6 taxa) | GO:0015288, IMP, PMID:2120174 (PseudoCAP) | INDIRECT-PHENOTYPE | Same paper and same problem as the oprD row: four OM proteins lost together, porin role assigned to "at least one". The term is correct for OprE by single-channel data (PMID:33481046). PSEUDOCAP WRONG_EVIDENCE_CODE/CHECK, PROBABLE. | OprD (P32722), OpdP (Q9HVS0) | Yes; stands on OprD (see oprD notes). No GO_CENTRAL defect. |

The PseudoCAP IDA outer membrane row from the same paper is plausible (OM-protein profiles) and is
MODIFIED to cell outer membrane (GO:0009279).
