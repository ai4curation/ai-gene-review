# Hif1a (rat) review notes

## Setup (2026-10-28)
- `just fetch-gene rat Hif1a` resolved O35800 (HIF1A_RAT, RGD:61928, GeneID 29560);
  GOA file keyed to O35800, 247 rows.
- `just fetch-gene-pmids rat Hif1a` cached 51 papers; PMID:21335549 fetched (full text).
  Also cached donor papers PMID:11818497, PMID:23401859, PMID:19528298, PMID:11063749 to
  check questionable ISO rows.
- No deep-research provider available; literature synthesis in
  `Hif1a-deep-research-manual.md`.

## Core picture
HIF-1alpha is the oxygen-regulated subunit of the HIF-1 alpha/ARNT bHLH-PAS
heterodimer. It binds HREs (5'-RCGTG-3' core) with ARNT and activates RNA polymerase II
transcription through NTAD/CTAD, recruiting CBP/p300 [PMID:15084519 "Co-immunoprecipitation
experiments indicated that Ref-1/Ape present in nuclear extract interacted with HIF-1
and p300 but not ATF/CREB."]. Stability and CTAD activity are controlled by PHD/FIH
hydroxylation (PMID:21335549). Rat-specific validation: functional rat cDNA
(PMID:11237857), TH promoter HRE (PMID:12675925), frataxin HRE ChIP (PMID:26071548),
ARNT2 dimerisation (PMID:11029639).

## Decisions worth flagging
- GO:0062029 positive regulation of cytoplasmic stress granule assembly (IMP
  PMID:30404558): the full text attributes the shRNA phenotype to RNAi itself, with no
  effect in Hif1a knockout cells. REMOVE, with a source_defects entry to RGD.
- GO:0045722 positive regulation of gluconeogenesis (IMP PMID:24177414): abstract
  describes HNF4alpha siRNA, not a Hif1a perturbation; abstract-only so UNDECIDED +
  source_defects CHECK.
- GO:0044877 protein-containing complex binding (three rat rows): MODIFY to the specific
  activity each paper shows (ARNT2 heterodimerisation; HRE DNA binding; coactivator
  binding), with WRONG_TERM source_defects.
- GO:0140537 transcription regulator activator activity (ISO from human DisProt IPI with
  EP300): HIF1A is the DNA-binding factor that recruits p300, not an activator of p300;
  MODIFY to transcription coactivator binding, source defect recorded.
- Axonal transport of mitochondrion and the derived axon cytoplasm IEA rest on HUMMR
  induction by HIF-1 (PMID:19528298): indirect, MARK_AS_OVER_ANNOTATED.
- Regulation of protein neddylation (PMID:23401859): HIF1A is the substrate whose
  engagement with VHL recruits DCNL1; MARK_AS_OVER_ANNOTATED.
- Motile cilium: mouse sperm midpiece signal for a mouse-specific Hif1a I.1 isoform
  (PMID:11818497); not established for rat, MARK_AS_OVER_ANNOTATED.
- IEP "response to X" rows: kept as non-core where HIF-1alpha induction is the mechanism
  of the cellular response (hypoxia mimetics, ROS, cytokine/insulin/lipid activation
  with demonstrated HIF-1 activity or HIF dependence); marked over-annotated where only
  an expression change was recorded.
- No NEW rows proposed.
