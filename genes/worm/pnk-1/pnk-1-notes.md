# pnk-1 review notes

## 2026-10-28 initial review

- fetch-gene resolved H2KYP7 (GeneID 172327, WBGene00004068) as requested; GOA keyed to H2KYP7, 8 rows.
- Key issue: PANTHER places PNK-1 in PTHR12280:SF20 (PANK4 subfamily), so PAINT propagated
  NOT pantothenate kinase activity (PTN000957966) and phosphatase activity (PTN000957966 + human PANK4).
  Own alignment (pnk-1-bioinformatics/RESULTS.md) shows PNK-1 retains the PANK catalytic Glu/Arg
  (E214/R281 vs PANK3 E138/R207) and lacks the PANK4 C-terminal DUF89 phosphatase region. The PANK4-type
  inactivation is amniote-specific [PMID:30927326 "all amniote PANK4s, including human PANK4, encode
  Glu138Val and Arg207Trp substitutions which are predicted to inactivate kinase activity"]; in worm the
  pseudo-kinase is PNK-4 (Ala at the Glu position; KO viable with normal CoA [PMID:42523442]).
- Decisions: REMOVE NOT-kinase IBA and phosphatase IBA (over-propagation; source_defects to GO_CENTRAL);
  NEW pantothenate kinase activity (IC); ACCEPT CoA biosynthesis (IBA, IEA), ATP binding, cytosol;
  MODIFY cytoplasm -> cytosol; MARK_AS_OVER_ANNOTATED nucleus (isoform-specific mammalian property).
- Phenotypes (mmBCFA levels, proteostasis, lifespan, lethality) are necessity evidence and were not
  turned into NEW process terms.
