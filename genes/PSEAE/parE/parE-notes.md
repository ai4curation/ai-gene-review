# parE (PA4967, Q9HUJ8) notes

## Literature

No deep-research provider was available. PubMed E-utilities returned HTTP 500
on 2026-11-05. The review rests on the full text of PMID:10049263 (cached) and
HAMAP MF_00938.

- ParC and ParE purified separately as MBP fusions [PMID:10049263 "The putative
  ParC and ParE proteins were overexpressed and separately purified by use of a
  fusion system with a maltose-binding protein"].
- Reconstituted enzyme activities [PMID:10049263 "The reconstituted enzyme had
  ATP-dependent decatenation activity, which is the main catalytic activity of
  bacterial topoisomerase IV, and relaxing activities but had no supercoiling
  activity."].
- A secondary fluoroquinolone target, less sensitive than gyrase.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000018885 | GO:0009330 DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) complex | 3 | 117 (78 taxa) | GO:0009340 DNA topoisomerase IV complex, IDA, PMID:10049263 (PseudoCAP) | SOUND | Full text read. Activity reconstituted from purified ParC + ParE; the seed term is a descendant of the node term, which is valid IBD evidence. | E. coli GyrB P0AES6, Aquifex GyrB O67137 | Yes. The generic type II complex term suits a GyrB/ParE node, and E. coli gyrase is a well-characterised complex. |
| PTN000018885 | GO:0006265 DNA topological change | 2 | 117 (78 taxa) | GO:0006265, IDA, PMID:10049263 (PseudoCAP) | SOUND | Decatenation and relaxation are catalysed by the reconstituted enzyme. | E. coli GyrB P0AES6 | Yes. E. coli GyrB alone grounds it. |
| PTN000018885 | GO:0003918 DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) activity | 5 | 116 (77 taxa) | GO:0003918, IDA, PMID:10049263 (PseudoCAP) | SOUND | ATP-dependent decatenation and relaxation by the reconstituted enzyme meets the definition. | E. coli GyrB P0AES6, M. tuberculosis GyrB P9WG45, Arabidopsis AT5G04130, P. falciparum Top2 Q8I528 | Yes. Several directly assayed seeds. |

No PSEUDOCAP and no GO_CENTRAL defect.

## Other decisions

- GO:0009330 IBA: TOO_GENERAL, because GO:0009340 is accepted.
- GO:0007059 chromosome segregation (IEA): ACCEPT; decatenation is the
  segregation step the enzyme performs.
- GO:0051276, GO:0003677, GO:0005524, GO:0005694: KEEP_AS_NON_CORE.
