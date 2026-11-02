# ruvb-1 review notes

- 2026-10-28: Created review. fetch-gene resolved O17607 (Swiss-Prot, WormBase
  WBGene00007784, GeneID 179388), 23 GOA rows.
- No deep-research provider was available; see ruvb-1-deep-research-manual.md.
- PMID:15340492 (Kniazeva 2004) was read in full. It is an mmBCFA paper whose
  RNAi/GC screen found that C27H6.2(RNAi) raises monounsaturated fatty acids
  ["C27H6.2(RNAi) does not cause significant changes in mmBCFA but results in an
  elevation of straight-chain monounsaturated FA and C18:1 n7"]. It has no GOA
  row for this gene and does not justify a NEW process term (phenotype only).
- Key decisions:
  - Core activity: ATP hydrolysis (human RuvBL1 has marginal activity alone,
    stronger in the RUVBL1/2 complex [PMID:17060327, PMID:21933716]).
  - DNA helicase activity (IBA + IEA EC) and ATP-dependent activity acting on DNA:
    marked as over-annotated. Helicase activity of full-length RUVBL1/2 is weak and
    auto-inhibited by domain II [PMID:21933716]; the UniProt EC is borrowed from
    E. coli RuvB.
  - box C/D snoRNP assembly: accepted (IMP, FIB-1 nucleolar accumulation
    [PMID:18804378], plus IBA).
  - Positive regulation of translation: over-annotation; the 20% drop in 35S
    incorporation is an indirect consequence of the snoRNP defect.
  - TOR signaling and larval development: kept as non-core.
  - Protein binding IPI rows (RUVB-2 Y2H): removed per the protein-binding policy.
