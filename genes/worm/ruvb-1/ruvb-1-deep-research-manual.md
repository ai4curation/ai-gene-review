# ruvb-1 (C27H6.2, O17607) manual literature review

No deep-research API was available, so this summary was compiled by hand from
the cached publications, the UniProt record and PubMed searches
(query "ruvb-1 elegans" returned PMIDs 36798316, 24346701, 18804378, 17720918).

## Identity and family

- RUVB-1 is the *C. elegans* ortholog of human RUVBL1 (pontin/TIP49), a member
  of the RuvB family of AAA+ ATPases (PANTHER PTHR11093, Pfam TIP49 and
  TIP49_C). UniProt: "Belongs to the RuvB family." The Walker A ATP-binding
  motif lies at residues 89-96 (UniProt FT BINDING).
- UniProt (By similarity to human Q9Y265): "Forms homohexameric rings. May form
  a dodecamer with ruvb-2 made of two stacked hexameric rings." The worm
  RUVB-1/RUVB-2 interaction is supported by yeast two-hybrid data (IntAct;
  PMID:12445390, PMID:19123269).

## Biochemistry (from the human ortholog)

- Purified human RuvBL1 forms ADP-bound hexamers, but "we could only detect a
  marginal activity with the purified protein"; domain II is a DNA/RNA-binding
  domain absent from bacterial RuvB [PMID:17060327].
- The RuvBL1/RuvBL2 dodecamer with truncated domain II "is competent for
  helicase activity", and "DNA unwinding of the human RuvBL proteins can be
  auto-inhibited by domain II" [PMID:21933716]. DNA helicase activity of the
  full-length proteins is therefore weak and contested; ATP hydrolysis is the
  well-established activity, and it is stronger in the heterocomplex.
- The UniProt EC 3.6.4.12 and the RHEA ATP hydrolysis reaction are attributed
  "By similarity" to E. coli RuvB (P0A812), a distant bacterial Holliday-junction
  branch-migration helicase, rather than to the eukaryotic RUVBL proteins.

## C. elegans experimental work

- Updike & Mango 2007 [PMID:17720918, abstract only]: a screen for suppressors of
  partial loss of pha-4/FoxA identified "the predicted AAA+ helicase ruvb-1"
  (allele px34, E371K).
- Sheaffer, Updike & Mango 2008 [PMID:18804378, full text]: "ruvb-1 is a
  component of the Target of Rapamycin (TOR) pathway in C. elegans (CeTOR).
  Both ruvb-1 and let-363/TOR control nucleolar size and promote localization
  of box C/D snoRNPs to nucleoli". FIB-1 (fibrillarin) "levels were reduced,
  and FIB-1 failed to localize to the nucleolus in the majority of ruvb-1 mutant
  larvae". ruvb-1(RNAi) reduced 35S incorporation by about 20%, as did fib-1 and
  pha-4 RNAi. ruvb-1 mutants arrest at L3 with perturbed vulval development and
  blocked gonadogenesis; the L3 arrest was independent of daf-16. ruvb-1 RNAi
  from L4 "did not cause a reproducible extension of lifespan".
- Kato et al. 2014 [PMID:25437307, full text]: human LINKIN (ITFG1) co-purifies
  RUVBL1 and RUVBL2; in worms ruvb-1 RNAi phenocopies the lnkn-1 gonadal
  leader-cell detachment phenotype. An affinity-purified anti-RUVB-1 antibody
  shows "Strong staining for both RUVB-1 and RUVB-2 ... in the cytoplasm and
  nucleus of gonadal cells", and the staining is lost after RNAi. LNKN-1
  expression and localization do not depend on RUVB-1.
- Tan et al. 2023 [PMID:36798316, bioRxiv preprint] follows up the LINKIN
  interactome; it adds no new ruvb-1 data.
- Kniazeva et al. 2004 [PMID:15340492, full text]: C27H6.2 was one of 25 genes
  whose expression changed in elo-5(RNAi) animals; "C27H6.2(RNAi) does not cause
  significant changes in mmBCFA but results in an elevation of straight-chain
  monounsaturated FA and C18:1 n7". The authors speculate that it "may be part of
  a mechanism that senses and tunes physical properties of membranes". This is
  an RNAi/GC screen result with no mechanism; no GO annotation is derived from it.
- Shibata et al. 2014 [PMID:24346701, abstract only] concerns HTZ-1/H2A.z and
  MYS-1 in somatic gonad fate; its abstract does not mention ruvb-1.

## Synthesis

RUVB-1 is best understood as the worm RUVBL1: an AAA+ ATPase that, with RUVB-2,
forms the hexameric/dodecameric RUVBL scaffold of conserved chromatin-remodeling
(INO80, SRCAP/SWR1, TIP60/NuA4) and assembly-chaperone (R2TP) complexes. The only
mechanistic worm data concern box C/D snoRNP accumulation in the nucleolus, which
matches the conserved role of RUVBL1/2 in snoRNP biogenesis. Developmental,
translational, lipid and TOR-pathway phenotypes are downstream consequences.
