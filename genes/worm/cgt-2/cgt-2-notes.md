# cgt-2 review notes

## 2026-10-28 initial review

- fetch-gene resolved G5EC84 (Swiss-Prot, WBGene00017625, GeneID 181790) as expected.
- GOA has 10 rows, all IBA/IEA; no experimental GO annotation exists for cgt-2.
- PMID:23705068 (Zhu et al. 2013 eLife; requested as key paper) was read in full: it
  studies cgt-1(tm1027) and cgt-3(tm504) only and never mentions cgt-2. It supports the
  pathway context (GlcCer synthesis required for postembryonic development, upstream of
  TORC1) but not any cgt-2-specific claim.
- Enzyme activity for CGT-2 itself: PMID:21325339 ["Each gene product showed active
  enzymatic activity when expressed in GM95 cells deficient in glycosphingolipids (GSLs)."]
- cgt-2 is a minor isozyme in vivo [PMID:38704027 "deficiency of cgt-3 but not cgt-1 or
  cgt-2 markedly decreased the abundance of all GlcCers quantified in C. elegans"] and is
  not required for larval development [PMID:38704027 "cgt-3;cgt-2 or cgt-1;cgt-2 double
  mutants did not"].
- ARBA rows for nematode larval development and regulation of protein localization to
  basolateral plasma membrane derive from cgt-1/cgt-3 phenotypes (PMID:23705068,
  PMID:21926990); neither is cgt-2-specific, and both are downstream pleiotropic effects of
  lipid supply rather than activities of the enzyme.
- Decisions: ACCEPT GO:0008120 and GO:0006679 (core); MODIFY glycosyltransferase activity
  and sphingolipid metabolic process to those terms; ACCEPT membrane (no finer evidence);
  MARK_AS_OVER_ANNOTATED larval development; REMOVE basolateral localization regulation.
- No NEW terms proposed: Golgi membrane is plausible from mammalian UGCG but only one line
  of evidence (orthology) exists for the worm protein.
- Full texts not available: PMID:11443131, PMID:19240113, PMID:21325339 (abstracts only).
