# elo-5 review notes

## Session 1

- Fetched with `just fetch-gene worm elo-5`; UniProt Q20300 (ELO5_CAEEL)
  confirmed. 12 GOA rows (7 IBA, 4 IEA, 1 IMP).
- Key papers read in full: PMID:15340492 (Kniazeva 2004), PMID:23705068
  (Zhu 2013), PMID:38704027 (Luo 2024, cached this session).
- Core function: ELO-family 3-ketoacyl-CoA synthase making iso-branched C15
  and C17 fatty acyl-CoAs (mmBCFAs) [PMID:15340492 "utilizes the long-chain
  fatty acid elongation enzymes ELO-5 and ELO-6 to produce two mmBCFAs, C15ISO
  and C17ISO"]. C15ISO feeds the d17iso sphingoid base [PMID:23705068;
  PMID:38704027].

## Decisions

- GO:1902321 methyl-branched FA biosynthesis (IMP): ACCEPT, core.
- GO:0009922 fatty acid elongase activity (IBA + IEA): ACCEPT, core MF.
- GO:0019367 elongation, saturated FA (IBA): iso-branched FAs are saturated;
  KEEP_AS_NON_CORE (true but the methyl-branched term is the informative one,
  and the IBA was placed for straight-chain elongases).
- GO:0034625 / GO:0034626 mono-/polyunsaturated elongation (IBA):
  MARK_AS_OVER_ANNOTATED; Kniazeva 2004 attributes PUFA elongation to
  elo-1/elo-2; elo-5 RNAi does not reduce PUFA.
- GO:0042761 VLCFA biosynthesis (IBA): GO defines VLCFA as >C22; ELO-5 products
  are C15/C17. MARK_AS_OVER_ANNOTATED.
- GO:0030148 sphingolipid biosynthesis (IBA): ACCEPT. ELO-5 synthesises the
  C15iso acyl chain that SPT condenses into the d17iso sphingoid base, so
  ELO-5 catalyses an early biosynthetic step (the same role ELOVL/yeast ELO
  enzymes play for ceramide acyl chains). Worm-specific evidence agrees.
- GO:0005789 ER membrane (IBA): ACCEPT (family-wide, plausible; no direct
  worm data).
- GO:0016020 membrane (IEA): MODIFY -> GO:0005789.
- GO:0006629 lipid metabolic process (IEA ARBA): TOO_GENERAL.
- GO:0006633 fatty acid biosynthetic process (IEA UniPathway): MODIFY ->
  GO:1902321.
- No NEW process terms: L1 developmental arrest / glucose stress phenotypes are
  downstream consequences of mmBCFA/sphingolipid deficiency, not processes
  ELO-5 performs.
