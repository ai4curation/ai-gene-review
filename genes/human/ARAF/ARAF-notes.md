# ARAF (human, UniProt P10398) - curation notes

## Identity

- UniProt P10398 (ARAF_HUMAN), 606 aa, "Serine/threonine-protein kinase A-Raf", EC 2.7.11.1;
  synonyms ARAF1, PKS, PKS2 [file:human/ARAF/ARAF-uniprot.txt].
- PANTHER PTHR44329 (official name "SERINE/THREONINE-PROTEIN KINASE TNNI3K-RELATED"), subfamily
  PTHR44329:SF55 "SERINE_THREONINE-PROTEIN KINASE A-RAF" [file:human/ARAF/ARAF-uniprot.txt].
- Isoform 2 (DA-Raf1) lacks the kinase domain and acts as a dominant-negative RAS antagonist
  [file:human/ARAF/ARAF-uniprot.txt "Has a wider tissue distribution than isoform 1, and acts as
  a dominant-negative antagonist"].
- No GO-CAM model in `gocams/index.tsv` contains P10398.

## Molecular function

- RAF-family MAP3K: RAS-GTP recruits ARAF to the membrane; ARAF homo/heterodimerises with BRAF/CRAF and
  phosphorylates MEK1/MEK2 [file:human/ARAF/ARAF-deep-research-falcon.md "ARAF can form homodimers and
  heterodimers with BRAF or CRAF."; "Wild-type ARAF immunoprecipitates generated phosphorylated MEK1"].
- Weakest RAF paralog under most conditions (BRAF > CRAF > ARAF), but not a pseudokinase
  [file:human/ARAF/ARAF-deep-research-falcon.md].
- Direct MEK2 binding via the ARAF kinase domain [PMID:11909642 "A-Raf was identified as a novel partner
  that interacts with MEK2"; "regions critical for this interaction were located between residues 255 and
  606 that represent the kinase domain of A-Raf"].
- Other reported direct substrates are secondary: BAD (RAF kinases generally) [PMID:19667065 "Our results
  indicate that RAF kinases represent, besides protein kinase A, PAK, and Akt/protein kinase B, in vivo
  BAD-phosphorylating kinases"], PFKFB2 in vitro [PMID:36402789 "In vitro kinase assays using recombinant
  proteins confirmed that BRAF, and to some extent ARAF but not CRAF, phosphorylated PFKFB2S483"].

## Regulation

- Inactive RAFs bound by 14-3-3 at S214/S582 in ARAF [Reactome:R-HSA-5672951 "S214 and S582 in ARAF"].
- S214 dephosphorylated by PP2A/PP1 and by the SHOC2-MRAS-PP1C complex [Reactome:R-HSA-5672961;
  PMID:35768504 "NTpS from ARAF, BRAF and CRAF ... were dephosphorylated with a significantly higher
  catalytic efficiency by the complex"].
- RAS binding: the N-terminal regulatory region (RBD + CRD) binds HRAS / RRAS2 in Y2H
  [PMID:12620389]; RAS-GTP effector [PMID:24441586].
- HSP90/CDC37 client kinase [PMID:22939624 "Unexpectedly, many more kinases than transcription factors bound
  HSP90."].

## Localization

- Cytosol (inactive, 14-3-3-bound) and plasma membrane (active, RAS-bound); mitochondria (MST2
  sequestration; TOM/TIM partners in Y2H) [file:human/ARAF/ARAF-deep-research-falcon.md "ARAF also has
  important non-catalytic functions, particularly sequestration of the pro-apoptotic kinase MST2 at
  mitochondria."].

## Processes

- MAPK (ERK1/2) cascade: core.
- Galpha12-ARAF-MEK-ERK axis upregulates RFFL, which ubiquitinates PRR5L, promoting mTORC2-dependent
  PKCdelta HM phosphorylation [PMID:22609986 "LPA acts preferentially through Gα12 to regulate RFFL
  expression, PRR5L polyubiquitination, and PKCδ HM phosphorylation through an ARAF-MEK-ERK pathway."].
  This is an indirect downstream output of ARAF MAP3K activity -> non-core.
- Anti-apoptotic (BAD phosphorylation, MST2 sequestration) -> non-core.

## Annotation decisions (summary)

- Kinase MF rows (IEA/TAS/IDA/IBA) accepted; GO:0004709 is the core MF.
- 59 GO:0005515 protein binding rows split by partner class (per BRAF conventions):
  MEK2 -> GO:0031434; 14-3-3 (SFN, YWHAE, YWHAZ) -> GO:0071889; BRAF -> GO:0046982;
  HRAS/RRAS2 -> GO:0031267; HSP90AB1 -> GO:0051879. Partners without informative function
  (Y2H preys such as TIMM44, TIMM50, PRPF6, NUDT14, ASS1, CPS1, RABGGTB, EFEMP1, NELFCD, PBK, COPS3;
  innate immune AP-MS TIRAP/IRAK2/IRF7; SMAD4; HERC2) -> REMOVE (uninformative; interaction not
  asserted false).
- GO:0033138 positive regulation of peptidyl-serine phosphorylation (BAD) -> MODIFY to GO:0018105
  (ARAF performs, not regulates, the phosphorylation), consistent with BRAF review.
- GO:0036211 protein modification process (TAS) -> MODIFY to GO:0006468 protein phosphorylation.
- PMID:19593445 (known batch miscitation) is not present in the ARAF GOA set.
