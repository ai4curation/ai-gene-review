# cgt-1 review notes

## 2026-10-28 session
- fetch-gene resolved O18037 (Swiss-Prot, WormBase WBGene00011517, GeneID 188169). 14 GOA rows.
- Full text read: PMID:23705068 (eLife 2013), PMID:26115433 (PLoS One 2015), PMID:37090153.
  Abstract only: PMID:19240113 (PMC full text not returned by PMC API), PMID:21325339, PMID:7651085.
- Core: ceramide glucosyltransferase (GO:0008120), glucosylceramide biosynthesis (GO:0006679),
  membrane (TM helices; Golgi by homology only - not asserted).
  [PMID:21325339 "Each gene product showed active enzymatic activity when expressed in GM95 cells
  deficient in glycosphingolipids (GSLs)."]
- Decisions:
  - GO:0016757 glycosyltransferase, GO:0006665 sphingolipid metabolic -> MODIFY to the specific
    terms the gene already carries.
  - GO:0002119 nematode larval development: KEEP_AS_NON_CORE. Product d17iso-GlcCer is an
    upstream signal for intestinal TORC1-dependent L1 development (PMID:23705068); the double
    mutant L1 arrest is the reported phenotype. Not core.
  - GO:1904508 regulation of protein localization to basolateral PM: MARK_AS_OVER_ANNOTATED.
    The only evidence is suppression of the sgk-1 null MIG-14::GFP defect by cgt-1/3 double RNAi
    (PMID:26115433); a genetic interaction in a sensitized background, consistent with altered
    membrane lipid composition, not a regulatory role of CGT-1.
  - IGI GO:0006679 from PMID:26115433: the paper does not measure GlcCer; it restates prior work
    ([46]). Term is correct (enzyme activity shown in PMID:21325339), so ACCEPT, with a CHECK
    source defect on the reference/evidence.
- No NEW terms proposed (oocyte/cytokinesis/lifespan phenotypes are necessity evidence only).
