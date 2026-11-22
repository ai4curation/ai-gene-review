# APC11 (S. cerevisiae, Q12157) - review notes

## Identity
- YDL008W / APC11; 165 aa; RING-H2 finger (UniProt ZN_FING 52..95, "RING-type; atypical"); InterPro IPR024991 (RING-H2_APC11), IPR051031 (RING-box E3 ligase family), Pfam PF12861. Ortholog of human ANAPC11 and pombe apc11; paralogous to the SCF RING subunit Hrt1/Rbx1.
- Inputs used: UniProt record, GOA tsv (29 rows), falcon/Edison deep research (`APC11-deep-research-falcon.md`), cached publications. Full text in cache: PMID:10888670 (Leverson 2000), PMID:16481473 (Thornton 2006), PMID:11114178 (Cooper 2000), PMID:19822757 (Williamson 2009, used for the Ubc4/Ubc1 K48 statement), PMID:39401078 (Vazquez-Fernandez 2024 yeast APC/C cryo-EM). Abstract-only: PMID:9469814 (Zachariae 1998), PMID:12477395 (Yoon 2002), PMID:30358795 (Wang 2018). Cited only through the deep-research file: Arnold et al. 2015 MBoC (nuclear APC/C-Cdh1 degron reporters), McLean et al. 2011 review.
- Founding identification: Apc11 was found by tandem MS in the purified yeast APC/C particle [PMID:9469814 "Apc2p, Apc5p, and the RING-finger protein Apc11p are conserved from yeast to humans."]; Yoon et al. 2002 TAP/DALPC extended the yeast APC to 13 subunits [PMID:12477395 "Our data increase the total number of identified APC subunits to 13 in both yeasts and indicate that previous approaches were biased against the identification of small subunits."].

## Molecular role (Leverson et al. 2000, the key paper)
- Apc11 alone is the minimal ligase: [PMID:10888670 "Here, we provide evidence that the Saccharomyces cerevisiae RING-H2 finger protein Apc11 defines the minimal ubiquitin ligase activity of the APC."]
- Direct E2 binding: [PMID:10888670 "Using purified, recombinant proteins we showed that Apc11p interacted directly with the Ubc4 ubiquitin conjugating enzyme (E2)."]; W81A severely reduces Ubc4 binding and is nonfunctional in vivo; C91A abolishes binding [PMID:10888670 "demonstrating that the integrity of the Apc11p RING-H2 finger is required for strong E2 binding."]
- E3 activity in a purified system, including polyubiquitination of Clb2 (also the D-box-deleted Clb2): [PMID:10888670 "His-Apc11p mediated the polyubiquitination of Clb2p in the presence of Ubc4p, but not Cdc34p (Figure 5 D, compare lanes 2 and 4)."]; metal-binding cysteine mutants are dead [PMID:10888670 "However, Apc11p bearing mutations in putative metal-binding cysteines (C41, C44, or C91) showed little or no activity in this assay (Figure 5 A, lanes 3, 4, and 9), demonstrating that the RING-H2 finger is absolutely required for its E3 activity."]
- Apc2 not needed in the minimal assay: [PMID:10888670 "The ability of Apc11p to act as an E3 was dependent on the integrity of the RING-H2 finger, but did not require the presence of the cullin-like APC subunit Apc2p."]; in vitro no direct GST-Apc11 / Apc2-CHD(471-853) interaction was detected [PMID:10888670 "While genetic evidence suggested that Apc11p and Apc2p are binding partners, we were unable to detect direct interactions between GST-Apc11p and a C-terminal fragment (residues 471–853) of Apc2p containing the cullin homology domain (our unpublished results)."] - but see Thornton 2006 below.
- No substrate specificity: [PMID:10888670 "These data indicate that, while Apc11p probably does not confer specificity toward destruction box-containing substrates, it is capable of mediating ubiquitin transfer from E2 to proteins other than itself, at least in vitro."]
- RING mutants still assemble into the APC/C: [PMID:10888670 "Perhaps surprisingly, all of the mutants were found to coimmunoprecipitate Cdc16p and Cdc27p as efficiently as wild-type Apc11p."] - so the essential defect is catalytic, not assembly.
- Mechanism: RING E3s are bridges, not thioester carriers [PMID:10888670 "Our work, and that of others, indicates that RING-based E3s do not act as ubiquitin carriers that form thioester intermediates, but instead act as bridges between E2s and substrates that provide a favorable environment for the transfer of ubiquitin."]
- C-terminal acidic tail 104-165 dispensable (APC11 delta104-165 spores are not ts).

## Architecture (Thornton et al. 2006)
- Apc2/Apc11/Doc1 form the catalytic subcomplex bridged by Apc1 to the TPR subcomplex [PMID:16481473 "one that contains Apc2 (Cullin), Apc11 (RING), and Doc1/Apc10, and another that contains the three TPR subunits (Cdc27, Cdc16, and Cdc23)"].
- apc2 delta loses Apc11 completely; apc11 delta only partially reduces Apc2/Doc1 [PMID:16481473 "These data suggest that Apc2 independently tethers Doc1 and Apc11."] - in vivo evidence that Apc2 (a cullin-family protein) is the Apc11 anchor, supporting the cullin-binding IBA despite the negative in vitro result of Leverson 2000.
- Only cdc27 delta APC retains any Pds1-ubiquitination activity; apc11 delta APC has none [PMID:16481473 "Of the mutant complexes, only cdc27 Δ APC displayed detectable activity against Pds1"]; [PMID:16481473 "Since Apc2 and Apc11 are thought to form the catalytic core of the APC, the enzyme should lack all activity and should be resistant to Cdh1 m11 ."]
- Securin and B-type cyclins are the only obligatory targets [PMID:16481473 "Previously, we showed that the only obligatory targets of the APC for cell cycle progression are securin and the B-type cyclins"].

## Phenotype
- apc11-13 / apc11-22 ts alleles arrest with 2n DNA, large buds, short spindles [PMID:10888670 "Immunofluorescence staining demonstrated that, for both mutants, >70% of the cells arrested with large buds, short mitotic spindles, and DAPI-staining masses at the bud-neck (Figure 1 B)."]; RING essential for viability [PMID:10888670 "Thus, the Apc11p RING-H2 finger performs a crucial function that is essential for cell viability."]
- UniProt MUTAGEN: S10R (apc11-13, G2/M arrest at 37 C), C41A, C44A, W81A, C91A loss of function.

## E2 usage / chain linkage
- Yeast APC/C: Ubc4 initiates, Ubc1 elongates, K48-linked chains; no Ube2S ortholog [PMID:19822757 "However, Ubc4 and Ubc1 function sequentially to assemble K48-linked ubiquitin chains, whereas human UbcH10 and Ube2S most likely bind APC/C at the same time."]. Human UbcH10 binds Apc11 + Apc2 [PMID:19822757 "UbcH10 binds the RING subunit Apc11 and the cullin subunit Apc2"].
- Deep research (Vazquez-Fernandez 2024, via deep-research file): in yeast apo-APC/C the Apc2-Apc11 module is already in an E2-competent position; RING ~30 A from substrate.

## Meiosis
- Ama1 is the meiosis-specific coactivator of the same core APC/C [PMID:11114178 "In conclusion, this study indicates that Ama1p directs a meiotic APC/C that functions solely outside mitotic cell division."]; Ama1 co-IPs with the APC/C [PMID:11114178 "First, coimmunoprecipitation assays indicate that Ama1p associates with the APC/C in vivo."]. No Apc11-specific meiotic experiment exists; the ComplexPortal NAS rows (CPX-762) are complex-level.

## Localisation
- UniProt has no subcellular-location line for Apc11 and SGD lists no direct nucleus annotation; the nucleus IBA rests on family-level evidence plus the fact that APC/C-Cdh1 proteolysis is nuclear in yeast (Arnold 2015 via deep research: nuclear degron reporters degraded, cytoplasmic ones stabilised) and that the TPR subunits function in the nucleus [PMID:10888670 "Cdc16p/APC6, Cdc23p/APC8, Cdc27p/APC3, and APC7 were identified as tetratricopeptide repeat (TPR)- containing proteins, which function in the nucleus"]. Accepted as the site of activity; noted as a knowledge gap (no direct Apc11 imaging).

## Curation decisions (summary)
- All GO:0005680 rows (IBA, IDA, IEA, IPI, NAS x2): ACCEPT - defining complex.
- GO:0061630 (IBA, IDA PMID:10888670, IEA): ACCEPT; `enables` is right because Apc11 alone has activity in the purified system.
- GO:0097602 cullin family protein binding (IBA, IEA): ACCEPT - Apc2 is the cullin-family anchor of Apc11 in vivo (Thornton 2006); the negative in vitro GST result with the CHD fragment does not overturn the in vivo dependency.
- GO:0008270 zinc ion binding (IEA, RCA): ACCEPT - RING-H2 metal-coordinating cysteines are required for activity.
- GO:0016567 (IBA, IDA, IEA, IMP, NAS x2), GO:0031145 (IDA, IEA, IMP, NAS x2), GO:0006511 IBA, GO:0045842 IBA, GO:0005634 IBA: ACCEPT.
- GO:0007346 regulation of mitotic cell cycle (ComplexPortal NAS): MODIFY -> GO:0007091 + GO:0010458, mirroring the APC2 review; the APC/C executes the metaphase/anaphase transition and mitotic exit rather than "regulating" the cycle.
- GO:0051445 regulation of meiotic cell cycle (NAS): KEEP_AS_NON_CORE, mirroring APC2 (coactivator-defined developmental context; no Apc11-specific data).
- Considered and rejected a NEW row for GO:0031624 ubiquitin conjugating enzyme binding (direct Ubc4 pull-down): comparator check shows human ANAPC11, RBX1, pombe apc11 and yeast Apc2 carry no such term (QuickGO, 2026-09-27); GO treats E2 engagement as part of ubiquitin protein ligase activity for RING E3s. Raised as a suggested question instead.

## 2026-10-01 IBA alignment
- Forced GOA/UniProt refresh: APC11 still has 29 current GOA annotations; no rows needed retirement and no newly seeded rows were created.
- Cached the 2024 yeast APC/C cryo-EM paper as PMID:39401078 and moved the Apc2-Apc11 active-conformation support from the Falcon summary to that primary paper.
- PubMed title/abstract search for 2025-2026 APC11/Apc11/YDL008W yeast updates found no newer direct Saccharomyces APC11 papers; the sole hit was a 2026 Entamoeba histolytica Apc11a study.
- Added IBA propagation reviews for all seven live PAINT rows: PTN000129805 for the broad RING-box family transfers and PTN000129916 for the APC11-specific anaphase-promoting complex and metaphase/anaphase transition transfers.
