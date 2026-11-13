# parC (PA4964, Q9HUK1) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HUK1 --alias parC`; accession matches the worklist.
No deep-research provider was used; PubMed esearch unavailable. Seed paper PMID:10049263 full
text (PMC89156) cached and read. parE (PA4967) is being reviewed in parallel.

### Literature

- PMID:10049263 (Akasaka et al. 1999): parC and parE cloned from PAO1 (69 and 75% identity to
  E. coli ParC/ParE); MBP-fusion ParC and ParE purified separately; [PMID:10049263 "Enzymatic
  activity was dependent on ATP, Mg 2+ (data not shown), and the presence of both subunits"];
  decatenation and relaxation, no supercoiling; topo IV is less quinolone-sensitive than gyrase.
- Background in the same paper: [PMID:10049263 "GyrA is responsible for the DNA strand binding,
  cleavage, and rejoining, and GyrB is responsible for ATPase activity."]

### Annotation decisions

- GO:0003918 (IDA, IEA), GO:0006265 (IBA, IDA seed, IEA), GO:0009340 (IDA seed),
  GO:0007059 (IBA, IEA): ACCEPT. Core function records GO:0003918 as contributes_to (holoenzyme).
- GO:0009330 (IBA, IEA), GO:0003916, GO:0006259, GO:0005886 (IEA): TOO_GENERAL.
- GO:0003677 (IBA, IEA), GO:0005694, GO:0005737, GO:0019897: KEEP_AS_NON_CORE.
- GO:0005524 ATP binding (IBA, IEA): REMOVE. The ATP site of type IIA topoisomerases is in the
  B subunit (ParE/GyrB). GO_CENTRAL defect on the PTN001607041 ATP-binding IBD (PROBABLE).
- Action counts: ACCEPT 8, TOO_GENERAL 5, KEEP_AS_NON_CORE 5, REMOVE 2.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001607041 | GO:0006265 DNA topological change | 5 | 105 (75 taxa) | GO:0006265, IDA, PMID:10049263 (PseudoCAP) | SOUND | Full text read: reconstituted ParC+ParE decatenates and relaxes DNA. Term suits the GyrA/ParC clade. | E. coli ParC P0AFI2 and GyrA P0AES4, M. tuberculosis GyrA P9WG47, P. falciparum gyrase A Q8I0X3 | Yes |
| PTN001607041 | GO:0009330 DNA topoisomerase type II (ATP-hydrolyzing) complex | 3 | 105 (75 taxa) | GO:0009340 topo IV complex, IDA, PMID:10049263 (PseudoCAP) | SOUND | Activity needs both subunits, so the ParC-ParE complex is shown functionally; the generic type II complex term is right for a node covering gyrase A and ParC. | E. coli ParC P0AFI2, A. aeolicus GyrA O67108 | Yes |

Other IBD at the same node, not seeded by parC: GO:0005524 ATP binding (seeds P9WG47, Q8I0X3).
The node term does not suit an A-subunit clade; GO_CENTRAL WRONG_TERM defect recorded on the
GO:0005524 IBA row, PROBABLE (seed papers not read).

Shared node check with parE: parE's IBAs come from PTN000018885 (GyrB/ParE family); parC's come
from PTN001607041, PTN000018855 and PTN000018879. parC and parE share no PTN node, so no
node defect needs coordinating with the parE review. No PSEUDOCAP defect on parC.
