# nrdA (PA1156, Q9I4I1) notes

No deep-research provider was available. Literature: PMID:16829681 (abstract only).

## Biology

- Class Ia RNR R1 subunit [PMID:16829681 "The RNR of this study (class Ia) is a complex of the NrdA
  protein harboring the active site and the allosteric sites and the NrdB protein harboring a tyrosyl
  radical necessary to initiate catalysis."].
- Duplicated ATP-cone, only the first functional [PMID:16829681 "The N-terminal ATP-cone (ATP-c1) is
  allosterically functional, whereas the internal ATP-cone lacks allosteric activity."].
- Complex [PMID:16829681 "The P. aeruginosa wild type NrdA and NrdB proteins form an extraordinarily
  tight complex with a suggested alpha4beta4 composition."].
- P. aeruginosa also has class II (nrdJab; genes/PSEAE/nrdJa) and class III RNRs.

### Annotation decisions

- GO:0004748 (IBA, IEA), GO:0005524 (IBA, IEA), GO:0005971 (IBA, IDA), GO:0009263 (IBA, IEA): ACCEPT.
- GO:0000166 (IEA): TOO_GENERAL (ATP binding accepted). The earlier nrdJa review used MODIFY to ATP
  binding for the same row; this batch follows the tier-2 is_a convention (TOO_GENERAL when an accepted
  descendant is present).
- Action counts: ACCEPT 8, TOO_GENERAL 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000171388 | GO:0005971 ribonucleoside-diphosphate reductase complex | 9 | 186 (118 taxa) | GO:0005971, IDA, PMID:16829681 (PseudoCAP) | SOUND | Abstract states purified NrdA and NrdB form a tight alpha4beta4 complex. | E. coli NrdA P00452 and NrdE P39452, M. tuberculosis NrdE P9WH75, human RRM1 P23921, mouse Rrm1, yeast RNR1/RNR3, S. pombe cdc22, Dictyostelium rnrA | Yes; eight other class I R1 seeds, and the complex term suits the class I R1 clade |

No PSEUDOCAP or GO_CENTRAL defect.
