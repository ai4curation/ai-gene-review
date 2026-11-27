# edd (P0ADF6, b1851) notes

## Session 2026-11-13

Deep research was not generated: the falcon provider failed for the sister review
(BACSU gpmI) in this offline environment, so it was not retried here. The review rests
on the cached publications and the UniProt record.

Literature checked (cached in `publications/`, all abstract-only): PMID:1846355,
PMID:17102132, PMID:5337844, PMID:1624451. Full text of PMID:17102132 (PMC5136138)
could not be retrieved (Europe PMC 500, publisher 403).

### Identity

- UniProt P0ADF6 EDD_ECOLI, edd, b1851/JW1840, 603 aa, E. coli K-12.
- PANTHER PTHR43661 (D-XYLONATE DEHYDRATASE), subfamily PTHR43661:SF1
  (PHOSPHOGLUCONATE DEHYDRATASE). IlvD/Edd family; NCBIfam TIGR01196 edd; HAMAP MF_02094.
- Two [4Fe-4S] cluster cysteines (Cys154, Cys221) inferred from IlvD (P05791) and HAMAP.

### Function

- First enzyme of the Entner-Doudoroff pathway: 6-phospho-D-gluconate ->
  2-dehydro-3-deoxy-6-phospho-D-gluconate (KDPG) + H2O.
  [PMID:5337844 "A mutant lacking gluconate-6-phosphate dehydrase (the first enzyme of the
  Entner-Doudoroff pathway) was isolated"]
- Oxidant-labile iron-sulfur enzyme. [PMID:1846355 "The O2(-)-sensitive target site is
  proposed to be an iron-sulfur cluster which is readily destroyed by oxidation."]
- [4Fe-4S] dehydratases are damaged by micromolar H2O2 (PMID:17102132); UniProt cites
  this paper with ECO:0000269 for the Edd catalytic activity and activity regulation.

### Physiology

- edd mutant: gluconate carbon goes only through the oxidative pentose phosphate pathway;
  slower growth on gluconate, normal growth on glucose and fructose.
  [PMID:5337844 "Thus, in E. coli, the Entner-Doudoroff pathway is used for gluconate
  metabolism but not for glucose metabolism."]
- edd-eda operon induced on gluconate (GntR, promoter P1). [PMID:1624451]

### Annotation decisions (summary)

- Phosphogluconate dehydratase activity (EXP, IBA, IDA, IEA, IMP): ACCEPT, core.
- Catalytic activity IEA and hydro-lyase activity IEA (ARBA): MODIFY to GO:0004456.
- 4 iron, 4 sulfur cluster binding IEA: ACCEPT (catalytic cofactor; oxidant sensitivity
  and iron chelator inactivation support an Fe-S cluster).
- Cytosol IBA: ACCEPT.
- Entner-Doudoroff pathway IEA: ACCEPT, core process.
