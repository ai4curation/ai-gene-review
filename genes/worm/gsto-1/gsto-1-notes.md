# gsto-1 review notes

## 2026-10-28 session

- fetch-gene resolved UniProt P34345 (GSTO1_CAEEL, WormBase WBGene00016204, GeneID 183000),
  as expected. GOA: 19 rows, seeded as 17 (duplicate IDA rows from WB and UniProt merged).
- Literature: see gsto-1-deep-research-manual.md. Key papers: PMID:17901115 (abstract only
  cached), PMID:23593298 (full text), PMID:25284791 (full text), PMID:10783391 (abstract).
- Decisions:
  - Core MF: GO:0045174 DHAR activity (highest Vmax, KM 184 uM) [PMID:17901115 "displayed
    significant thiol oxidoreductase and dehydroascorbate reductase activity"].
  - GO:0004364 GST activity: true (CDNB KM/Vmax measured) but "minimal" per authors ->
    KEEP_AS_NON_CORE on all four rows.
  - GO:0050610 methylarsonate reductase (EXP + IEA): UNDECIDED. UniProt CATALYTIC ACTIVITY
    cites PMID:17901115 at ECO:0000269 while its FUNCTION text says "(By similarity)";
    abstract silent; no MMA kinetics. Recorded a CHECK source defect against UniProt.
  - GO:0061687 detoxification of inorganic compound (IDA): UNDECIDED; rests on arsenite
    RNAi sensitivity (abstract) that the 2013 screen did not reproduce
    (arsenite survival 86.5 vs 90.0 control).
  - Response to oxidative stress / superoxide: KEEP_AS_NON_CORE (phenotype-level).
  - GO:0098869 cellular oxidant detoxification: ACCEPT (DHAR-derived; peroxide resistance
    on overexpression; measurable cumene hydroperoxide activity).
  - No NEW terms: lifespan/hypoxia phenotypes are necessity evidence only.
- Thioltransferase (HEDS) activity would map to GO:0015038, an ancestor of GO:0045174
  already carried, so not proposed separately.
