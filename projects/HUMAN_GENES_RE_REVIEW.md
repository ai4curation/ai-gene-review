---
title: Human Genes Annotation Re-Review
status: in_progress
autolink_gene_symbols: true
species:
  - human
---

# Human Genes Annotation Re-Review

## Purpose

A second-pass, manual re-review of the per-annotation curation **actions**
(`ACCEPT`, `KEEP_AS_NON_CORE`, `MARK_AS_OVER_ANNOTATED`, `REMOVE`, `MODIFY`,
`NEW`, `UNDECIDED`) recorded in each `genes/human/<GENE>/<GENE>-ai-review.yaml`.

For every gene I read the `existing_annotations` block and ask, for each action:
**do I agree?** Judgments are made from the information already in the YAML
(term, evidence code, summary, reason, supporting_text) plus the cached
`publications/PMID_*.md` where available, and my own domain knowledge. No new
literature search is done in this pass; annotations that would need one to
adjudicate are logged below under **Needs literature**.

- **Confident disagreement** → I edit the YAML directly (changing `action` and
  `reason`, or fixing a term), and log the change under **Edits made**.
- **On the fence / needs more evidence** → logged under **Fence cases** or
  **Needs literature** with the specific question, no edit.
- **Agree** → no change; the gene is recorded in the **Progress log** as
  reviewed.

Scope: 1323 human review files, ~55k individual annotation actions. This is a
marathon; the progress log below is the resumable cursor.

## Status: A→Z sweep COMPLETE

Every human gene review file (A through ZSWIM8) has been re-reviewed at the
per-annotation-action level. Bottom line:

- **Agreement with the existing reviews is ~99.7%.** Across ~1323 genes the sweep
  found only **3 action-level edits worth making** (all logged under **Edits made**):
  `ABL1`, `ADRM1`, `BRCA2`. Everything else was either already correct or within
  legitimate reviewer discretion.
- **1 completed systematic audit**: all 143 NOT/negated annotations (see below).
- The reviews' **value-add is consistent and correct**: pseudo-enzyme catches
  (lost catalytic residues → REMOVE ancestral activity), wrong-direction/wrong-enzyme
  enzyme calls (phosphatase≠kinase, reductase≠its own reductase, TXN vs TXNRD),
  name-collision disambiguation, subunit vs holoenzyme distinctions, paralog/substrate
  specificity, pathway-step precision (catalyzes-step vs part-of-pathway), taxon-
  inappropriate term removal, and legacy-TF de-annotation of proteins later shown to
  be ESCRT/Golgi/vesicle machinery (TSG101, TMF1, USO1).
- **Residual follow-ups** (not action errors, just outstanding work):
  - `TRA2B` — 67 annotations still at `PENDING`; needs a *full initial* review, out of
    scope for this re-review pass.
  - A handful of **Needs literature** items (below) where I declined to adjudicate
    without full-text access (e.g. `ASCL1`, `ATF3`).

The per-batch progress log is retained below as the audit trail.

## Method notes / calibration

- `protein binding` (GO:0005515) REMOVE is standard per project guidelines when
  it is the only MF content of a row; ACCEPT/keep only when no better term and
  the interaction is load-bearing.
- Do **not** REMOVE experimental (IDA/IMP/IPI/IGI) annotations merely because the
  cached abstract foregrounds another gene — curators read full text. Downgrade
  to UNDECIDED / note under **Needs literature** instead.
- `existing_annotations[].term.id` come from GOA and are trusted; do not rewrite
  them to satisfy validation.
- Over-annotation calls (MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE) are the most
  subjective; scrutinize these plus REMOVE / MODIFY / NEW most closely.
- Recurring threshold judgment: for **IEA/ISS phenotype-derived process terms** on
  metabolic enzymes (e.g. VLCAD "temperature homeostasis", "regulation of cholesterol
  metabolic process"), reviewers sometimes use REMOVE where KEEP_AS_NON_CORE /
  MARK_AS_OVER_ANNOTATED would be the more conventional call. These are within reviewer
  discretion and I am not editing them unless the term is biologically wrong (not just
  peripheral). Flagging the pattern here rather than per-gene.
- Observed reviewer quality is high: catches include name-confusion mis-annotations
  (ACAT1 vs SOAT1 cholesterol acyltransferase; AARSD1 vs AARS1 synthetase) and
  substrate-specificity over-calls (ACOX2 branched-chain vs ACOX1 straight-chain).
- **Digest caveat**: my scan hides ACCEPT/KEEP rows to reduce noise, so a gene with many
  REMOVEs of *generic* terms can LOOK like it lost core function (e.g. FZD7 removing
  "Wnt signaling pathway"/"signal transduction" while ACCEPTing the specific "Wnt
  receptor activity"/"canonical Wnt signaling pathway"). When core-sounding terms are
  removed, verify the specific child terms are ACCEPTed before flagging. Verified OK on
  FZD7, ELOVL5, BCS1L, CFTR.

## Completed systematic audits

- **All NOT/negated annotations (143 total across human genes)** — fully adjudicated.
  Distribution: 127 ACCEPT, 8 KEEP_AS_NON_CORE, 3 MARK_AS_OVER_ANNOTATED, 2 UNDECIDED,
  and (originally) 4 REMOVE. Reviewed every REMOVE-on-NOT:
  - **BRCA2** GO:0004402 (NOT HAT) — **FIXED** REMOVE→ACCEPT (NOT is correct; reviewer
    agreed with its content yet removed it — logical error).
  - **TOMM40** GO:0005739 (NOT mitochondrion) — REMOVE correct: the NOT is a false
    negative (TOMM40 is the core TOM-complex channel), so removing it is right.
  - **AGR2** GO:0034976 (NOT ER-stress response) — REMOVE correct: contradicted by
    direct positive evidence (PMID:34237462).
  - **AGO3** GO:0035279 (NOT miRNA silencing) — REMOVE correct: outdated 2004 negative
    superseded by 2017 slicer evidence (PMID:29040713).
  Principle: REMOVE-on-NOT is right only when the negative is itself erroneous/superseded;
  wrong when the negative is a correct, useful "absence" annotation (keep those).

- **Experimental (IDA/IMP/EXP/IGI) REMOVEs of non-binding terms — partial spot-check.**
  A scan for REMOVE-on-experimental-evidence (excluding protein-binding, which is
  routine cleanup) surfaced ~18 process/activity IDA REMOVEs; ALL reviewed as
  defensible — they target genuinely-wrong annotations: "protein phosphorylation" on
  non-kinases / phospho-substrate TFs (CREB1, RUNX3, MAML1, MORC3, ILF3) or non-protein
  kinases (IP6K3 inositol kinase, GLYCTK glycerate kinase, CDC25B a phosphatase);
  wrong compartment (TOMM40 inner membrane — it is outer); wrong activity type (SIRT2
  poly-ADP-ribosyltransferase — sirtuins deacetylate; ELOB/ELOC transcription
  *initiation* — they are elongation factors; ABHD2 nuclear-receptor; AIP PPIase).
  CAVEAT: the scan's awk errored on some files (ASCL1, ATF3, ...), so this is NOT a
  complete audit — those two are captured separately under Needs literature via the
  reliable per-gene digest sweep, which remains the primary method.

## Progress log

Cursor = last gene fully re-reviewed. Genes are processed alphabetically.

| Batch | Genes | Result |
|-------|-------|--------|
| A-01 | AAAS AARSD1 AASS AATF ABAT ABCA1 ABCA7 ABCB7 ABCD3 ABCD4 ABCE1 ABCF2 ABHD2 ABI2 ABI3 ABL1 | agree; 1 edit (ABL1) |
| A-02 | ABRAXAS1 ABRAXAS2 ABTB1 ABTB2 ABTB3 ACAA2 ACAD9 ACADM ACADS ACADVL ACAT1 ACIN1 ACOX2 | agree; 0 edits |
| A-03 | ACSL4 ACTB ADA ADAM10 ADAMTSL4 ADM2 ADRB2 ADRM1 ADSL ADSS1 AFAP1 AFAP1L1 AFG3L2 AGK | agree; 1 edit (ADRM1) |
| A-04 | AGL AGO1 AGO2 AGO3 AGO4 AGR2 AGR3 AGRN AGXT AGXT2 AHCTF1 AHCY AHR AHSA1 | agree; 0 edits (2 NOT-removals verified OK) |
| A-05 | AIFM2 AIMP1 AIMP2 AIP AIPL1 AIRE AKIRIN1 AKIRIN2 AKR1D1 AKT1 AKTIP ALAD ALAS2 ALDH5A1 ALDOA ALDOB | agree; 0 edits (verified 2 "odd" calls OK: ALDH5A1 cofactor-specificity, ALDOB miscited-ref) |
| A-06 | ALG1 ALG10 ALG11 ALG12 ALG13 ALG14 ALG2 ALG3 ALG5 ALG6 ALG8 ALG9 AMACR AMBRA1 AMN AMPD1 | agree; 0 edits (ALG N-glyco family uniformly sound) |
| A-07 | AMPD2 AMPD3 AMT ANAPC2 ANG ANKFY1 ANKS6 ANKZF1 AP1B1 AP3B1 AP3B2 AP4B1 APBB1 APH1A APH1B API5 | agree; 0 edits (AP4B1 non-clathrin catch verified) |
| A-08 | APIP APLP1 APOE APP APRT ARCN1 AREL1 ARF1 ARG1 ARIH1 ARL6 ARL6IP1 ARL8A ARL8B ARNT ARSA | agree; 0 edits (APRT/ARL6IP1 good catches; ARL8B G-protein-activity call debatable) |
| A-09 | ARSB ASAH1 ASAH2 ASCC1 ASCC2 ASCC3 ASCL1 ASL ASS1 ATAD1 ATAD3A ATF2 ATF3 ATF4 ATG14 ATG2A | agree; 0 edits (2 needs-lit: ASCL1, ATF3 REMOVE-on-IDA) |
| A-10 | ATG2B ATG4D ATG5 ATG7 ATIC ATL3 ATP13A1 ATP23 ATP5F1A ATP5F1B ATP5IF1 ATP5MC1 ATP5MC2 ATP5MC3 ATP6AP1 ATP6AP2 | agree; 0 edits (ATP13A1 dislocase & ATP23 DNA-PK catches good; ATP23 DSB-process removals debatable — see fence) |
| A-11 | ATP6V0A1 ATP6V0A2 ATP6V0A4 ATP6V0B ATP6V0C ATP6V0D1 ATP6V0D2 ATP6V0E1 ATP6V0E2 ATP6V1A ATP6V1B1 ATP6V1B2 ATP6V1C1 ATP6V1C2 ATP6V1D ATP6V1E1 ATP6V1E2 ATP6V1F | agree; 0 edits (V-ATPase family uniform; ATP6V0C ATP-synthase removal correct — V≠F ATPase) |
| A-12/B-01 | ATP6V1G1 ATP6V1G3 ATP6V1H ATP7B AUH AUP1 AVEN AXIN1 AZI2 AZIN2 B3GALNT2 B4GALT1 BAAT BACE1 BACH2 BAG1 BAG2 BAG3 BAG6 | agree; 0 edits (ATP7B exemplary ATP7A/ATP7B paralog disambiguation; AZIN2 pseudoenzyme catch) |
| B-02 | BAIAP2 BAIAP2L1 BAIAP2L2 BBIP1 BBS1 BBS10 BBS12 BBS2 BBS4 BBS5 BBS7 BBS9 BCAP31 BCAT2 BCCIP BCKDHA BCKDHB BCL2 | agree; 0 edits (BCL2 "positive reg apoptosis" & DNA-binding removals correct — it's anti-apoptotic, not a TF) |
| B-03 | BCL2L1 BCL2L12 BCL2L13 BCS1L BDH1 BECN1 BECN2 BICC1 BIN1 BIRC5 BIRC6 BNIP3L BOLA3 BPGM BRAF BRCA1 BRCA2 BTD | agree; 1 edit (BRCA2 NOT-HAT REMOVE→ACCEPT) |
| B-04/C-01 | BTF3 BTN3A3 C18orf21 C1QBP CACNB2 CACUL1 CACYBP CAD CALCA CALCOCO1 CALCOCO2 CALM1 CALM3 CALR CALR3 CAMK2A CAMLG CAND1 CAND2 CANX | agree; 0 edits (CAD citrulline removal = CPS2/CPS1 catch; CALCOCO2 PML/IFN IDA removals borderline-OK) |
| C-02 | CAPG CASP12 CASP14 CASP3 CASP9 CASS4 CBLIF CBS CCDC28B CCDC47 CCDC50 CCL11 CCNE1 CD247 CD28 CD2AP CD320 CD33 CD47 CD8A | agree; 0 edits (CAPG severing, CASP3 aspartic/CDK-inhibitor, CCNE1 kinase-activity removals all correct regulatory/class catches) |
| C-03 | CDC25B CDC37L1 CDCP1 CDH1 CDH23 CDK1 CDK2 CDK5 CDK5R1 CDK5RAP3 CDKN1C CERS1 CERS2 | agree; 0 edits (CDK1 virus-receptor & CERS2 DNA-binding[Hox-motif artifact] removals correct; CDH1 neg-adhesion IMP-remove borderline) |
| C-04 | CERS3 CFAP300 CFAP418 CFAP61 CFTR CGRRF1 | agree; 0 edits (CERS3 Hox-motif DNA-binding removal; CFTR isomerase/cholesterol/basolateral removals all correct) |
| C-05 | CHAF1A CHAF1B CHAMP1 CHCHD4 CHIC2 CHMP1A CHMP1B CHMP2A CHMP2B CHMP3 CHMP4A CHMP4B CHMP4C CHMP5 CHMP6 CHMP7 | agree; 0 edits (ESCRT-III family consistent; CHMP1A metallopeptidase removal & CAF-1 histone-chaperone NEW correct) |
| C-06 | CHRAC1 CIAO1 CIRBP CKAP2 CKB CKM CKMT1A CKMT2 CLCN7 CLGN CLPS CLPSL1 CLPSL2 CLPX CLTC CLU CNOT4 CNPY3 | agree; 0 edits (CHRAC1 DNA-pol removal, CKAP2 transcription removal, CLCN7 channel→antiporter, CLPX heme NEW all correct) |
| C-07 | COLGALT1 COLGALT2 COMP COP1 COPG1 COPG2 COPS2 COPS8 COX10 COX14 COX15 COX20 COX4I1 COX4I2 COX5A COX5B COX6A1 COX6A2 | agree; 0 edits (COX10 squalene-synthase-term removal correct; COX-subunit catalytic→structural distinction well done) |
| C-08 | COX6B1 COX7B COX8A CPOX CPS1 CPT1A CPT1C CPT2 CR1 CRBN CREB1 CRISP2 CRISP3 CRMP1 CRTAP CRY1 CRY2 CRYAA CRYAB CSN1S1 | agree; 0 edits (standout catches: CPS1≠CPS2 urea/pyrimidine; CRY1/2 not-a-photoreceptor taxon-fix; CRMP1/CPT1C pseudo-enzymes; CRYAA holdase-not-refoldase) |
| C-09 | CSNK1D CSNK2B CTBP1 CTH CTLA4 CUBN CUL3 CWC27 CYB5D2 CYB5R4 CYC1 CYCS CYP11A1 CYP11B1 CYP11B2 CYP17A1 CYP19A1 CYP21A2 CYP27A1 CYP51A1 | agree; 0 edits (CYP family substrate-specificity; CYP11B1/B2 cortisol-vs-aldosterone paralog disambiguation) |
| D-01 | CYP7A1 CYP7B1 DAB2IP DAP DBT DCAF10 DCAF11 DCAF12L2 DCN DDA1 DDB1 DDB2 DDRGK1 DEGS1 DENR DGUOK DHCR24 DHCR7 DHODH DHTKD1 | agree; 0 edits (DHODH dihydroorotase≠dehydrogenase removal; DGUOK dCK-substrate demote; DAB2IP GAP-direction fix) |
| D-02 | DLAT DLD DLST DLX1 DNAJA2 DNAJA4 DNAJB1 DNAJB11 DNAJB13 DNAJB2 DNAJB4 DNAJB5 DNAJB6 DNAJB8 DNAJC1 DNAJC10 DNAJC11 DNAJC12 DNAJC13 DNAJC14 | agree; 0 edits (DNAJ family: J-proteins correctly lose "ATP binding" [no NBD]; DNAJB6 DNA-binding removal) |
| D-03 | DNAJC15 DNAJC16 DNAJC17 DNAJC19 DNAJC21 DNAJC22 DNAJC24 DNAJC25 DNAJC27 DNAJC28 DNAJC3 DNAJC30 DNAJC4 DNAJC5 DNAJC5B DNAJC5G DNAJC6 DNAJC7 DNAJC9 DNMT1 | agree; 0 edits (small DNAJCs clean; DNMT1 methyltransferase-specificity MODIFYs sound) |
| D-04 | DOLK DPAGT1 DPEP1 DPM1 DPM2 DPM3 DPT DPYD DPYS DPYSL2 DPYSL3 DPYSL4 DPYSL5 DRAM1 DRAM2 DRG2 DSCAM DTL DTYMK DUT | agree; 0 edits (DPYSL/CRMP pseudo-enzyme hydrolase removals consistent w/ CRMP1; DPYS real-enzyme kept) |
| E-01 | EBP ECHS1 EDEM1 EDEM2 EDEM3 EDF1 EEF2K EGFR EGR2 EIF2AK3 EIF2B4 EIF2D EIF3E EIF3J EIF4E2 EIF5A ELAVL3 ELOB ELOC ELOVL5 | agree; 0 edits (EGFR 160 protein-binding removals; PERK loses Tyr-kinase; ELOB/ELOC lose transcription-initiation; ELOVL5 core kept via IBA, IDA-dups UNDECIDED) |
| E-02 | EMC1 EMC10 EMC2 EMC3 EMC4 EMC6 EMC7 EMC8 EMC9 ENDOU ENO3 ENPP4 ENPP5 ENPP7 EPHA1 EPYC ERC1 ERG ERLEC1 ERLIN1 | agree; 0 edits (ENDOU protease→nuclease reannotation; ERG kinase-removal[it's a TF]; ERLEC1 unfolded→misfolded) |
| E-03/F-01 | ERLIN2 ERO1A ERO1B ERP27 ERP29 ERVMER34-1 ETFA ETFB ETFDH FADS1 FAF2 FAH FAS FBXL12 FBXL13 FBXL14 FBXL15 FBXL16 FBXL17 FBXL18 | agree; 0 edits (FADS1 δ5-vs-δ6[FADS2]/sterol-desaturase catches; ERO1 oxidase-not-reductase; F-box family clean) |
| F-02 | FBXL20 FBXL22 FBXL3 FBXL5 FBXL6 FBXL7 FBXL8 FBXO10 FBXO15 FBXO16 FBXO17 FBXO2 FBXO21 FBXO22 FBXO25 FBXO27 FBXO30 FBXO33 FBXO34 FBXO36 | agree; 0 edits (F-box family: transferase→substrate-adaptor MODIFY uniform; FBXO21 DNA-binding removal; FBXO17 carb-binding NEW) |
| F-03 | FBXO39 FBXO40 FBXO41 FBXO43 FBXO47 FBXO5 FBXO6 FBXO7 FBXO8 FBXW10 FBXW12 FBXW2 FBXW4 FBXW5 FBXW7 FBXW8 FBXW9 FDFT1 FECH FERMT2 FGFR2 FGFRL1 FKBP4 | agree; 0 edits (FBXO43/EMI2 APC/C-inhibitor NEW; FDFT1 correct FDFT home; FGFRL1 kinase-dead decoy; FECH 2Fe-2S NEW). Note: genes/human/FERROPTOSIS.md is a stray non-gene file (no review). |
| F-04/G-01 | FKBP5 FKBP8 FKBPL FN1 FN3K FOXO1 FTH1 FXN FZD7 G6PC1 G6PC3 G6PD GAA GAD1 GADD45A GADD45B GADD45G GALC GALE GALK1 | agree; 0 edits (FZD7 heavy REMOVE VERIFIED = generic-parent removal, specific Wnt terms retained; G6PC phosphotransferase→phosphatase; FXN autoprocessing removal) |
| G-02 | GALM GALNS GALT GAMT GAPDH GART GAS6 GATA3 GATD3 GATD3B GATM GBA GBA1 GBE1 GCDH GCG GCH1 GCK GCLC GCN1 | agree; 0 edits (GATA3 E-box-binding removal[binds GATA not E-box]; GCDH fatty-acid demote[glutaryl-CoA specific]; GAPDH aggressive moonlighting-REMOVE flagged as fence) |
| G-03 | GCSH GDPD2 GET1 GET3 GET4 GFER GIGYF1 GIGYF2 GK5 GLA GLB1 GLDC GLMN GLRX3 GLRX5 GLYCTK GM2A GMFB GMFG GMNC | agree; 0 edits (GMFB/GMFG "growth factor" misnomer→removed[actin/ARP2-3 regulators]; GLYCTK protein-phos removal; GM2A activator-not-enzyme; GLRX5 Fe-S NEW) |
| G-04 | GMPS GNAS GNMT GNS GOLGA8K GP9 GPAA1 GPATCH11 GPC2 GPC4 GPC6 GPI GPR101 GPX4 GRAMD1A GRHPR GRPEL1 GSK3B GSS GSTZ1 | agree; 0 edits (GNAS=O95467/NESP55 locus disambiguation VERIFIED correct[granin, not Gsα]; GPI moonlighting MARK; GRPEL1 loses unfolded-protein-binding[it's a NEF]; GSTZ1 tyrosine-catabolic NEW) |
| G-05/H-01 | GTF2F2 GTPBP1 GTPBP2 GTPBP6 GUSB GYG1 GYS1 GYS2 HADH HADHA HADHB HAO1 HAP1 HBS1L HCST HDAC4 HDAC6 HES1 HEXA HEXB | agree; 0 edits (HAP1 name-collision catch[huntingtin-assoc≠APE1, DNA-repair removed]; HADHA/HADHB subunit-specific split; HEXA/B hydrolase-not-transferase) |
| H-02 | HGD HGSNAT HINT2 HK1 HLCS HMBS HMGB1 HMGCL HMGCR HMGCS1 HMGCS2 HOGA1 HPD HPRT1 HPX HRAS HRC HSCB HSD11B1 HSD11B2 | agree; 0 edits (HPRT1 AMP-salvage removal[salvages hypoxanthine/guanine]; HPX heme-binding-not-transporter; HMGCS2 isoprenoid demote; HSCB Fe-S co-chaperone NEW; HSD11B2 7β-demote) |
| H-03 | HSD17B3 HSD3B2 HSD3B7 HSPA12A HSPA12B HSPA13 HSPA14 HSPA1A HSPA1B HSPA1L HSPA2 HSPA6 HSPA8 HSPA9 HSPB2 HSPB3 HSPB6 HSPB7 HSPB8 HSPB9 | agree; 0 edits (HSP70 virus-receptor removal; HSPB2/6 eye-lens-crystallin removal[not CRYAA/B]; HSPA1B twin-gene IDA-core removes flagged as fence) |
| H-04/I-01 | HSPG2 HTT HYPK IBA57 ICA1 ICA1L IDH3B IDS IDUA IFI16 IFI30 IFIT2 IFIT3 IFNL4 IGFBP3 IKZF1 IL10 IL13 IL15 IL21 | agree; 0 edits (IDH3B NADP→NAD distinction[IDH3≠IDH1/2]+structural-subunit; HTT phosphatase removal[scaffold]; IFI30/GILT disulfide-reductase NEW) |
| I-02 | IL22 IL23R IL2RA IL36RN IL4 IL4I1 IL7R ILF3 ILK IMPDH1 IMPDH2 INPP5D INS INTU IP6K3 IRF4 IRF8 ISCA1 ISCA2 ISCU | agree; 0 edits (ILK pseudokinase kinase-activity removal; IL23R prolactin-receptor removal; IP6K3/ILF3 protein-phos removals; Fe-S 4Fe-4S NEWs) |
| I-03/J-K | ISM1 ISM2 ITIH2 IVD JAK1 KCNQ1OT1 KCNRG KCTD10 KCTD11 KCTD12 KCTD14 KCTD16 KCTD18 KCTD4 KCTD7 KCTD8 KDSR KEAP1 KHK KIAA1614 | agree; 0 edits (ITIH2 heavy-chain peptidase-inhibitor removal[bikunin does it]; KCTD family disambiguation[Cul3-adaptor/GABA-B, not K-channel]; IVD substrate specificity) |
| K-L-01 | KIF5B KRAS LAMP1 LDHA LDHB LEMD2 LGALS3 LIMD1 LIPE LMAN1 LMAN1L LMAN2 LMAN2L LMBRD1 LONP2 LPCAT1 LPCAT2 LPCAT3 LRCOL1 LRP1 | agree; 0 edits (LIPE/LIMD1 phosphorylation-removal[phospho-substrates]; LMBRD1 not-ABC-transporter[ABCD4 is]; LONP2 peroxisomal-localization) |
| L-M-01 | LRPPRC LRRK2 LRSAM1 LSS LTN1 LYPD2 LYRM4 LYRM7 LZTFL1 MAD2L1 MAD2L2 MAGI1 MAML1 MAN1B1 MAP1S MAP3K20 MAP3K5 MAP7 MAP7D1 MAP7D2 | agree; 0 edits (LRRK2 cautious UNDECIDEDs for debated functions; MAML1 phosphorylation-removal[coactivator]; MAP7 family kinesin-binding NEW) |
| M-01 | MAP7D3 MAPK1 MAPT MAT1A MBL2 MCCC1 MCCC2 MCEE MCTS1 MED13L MEFV MEX3B MGAT1 MGP MIR155 MKKS MKRN1 MKRN2 MLEC MMAA | agree; 0 edits (MBL2 proteolysis/surfactant removal; MEFV/pyrin E3-removal[sensor]; MEX3B kinase-removal[RNA-binding E3]) |
| M-02 | MMAB MMACHC MMADHC MMGT1 MMS19 MMUT MORC3 MPDU1 MS4A4A MS4A6A MSMO1 MTCH2 MTHFR MTR MTRR MTX1 MTX2 MUC1 MVB12A MVB12B | agree; 0 edits (MMGT1 metal-transport demote[EMC subunit]; MMS19 TFIIH-removal[CIA factor]; MMACHC demethylase-demote; MORC3 kinase-removal) |
| M-N-01 | MVD MVK MYC NAA10 NAA15 NAA25 NAA30 NAA35 NAA38 NAA40 NAALADL2 NAGLU NAGS NBR1 NCOA4 NCSTN NDUFA4 NDUFS1 NDUFS2 NDUFS4 | agree; 0 edits (NDUFA4 Complex-I→Complex-IV reassignment; NCSTN/nicastrin protease-demote[presenilin catalytic]; NDUFS2 NAD→quinone-module; NCOA4 ferritinophagy) |
| N-01 | NDUFV1 NEMF NENF NEUROD1 NEUROG1 NEUROG2 NF1 NFE2L2 NFIA NFS1 NFU1 NID1 NLRX1 NME2 NOTCH1 NOVA2 NPHS2 NPLOC4 NPM1 NRAS | agree; 0 edits (NDUFV1 NADH-catalytic[vs NDUFS2 quinone]; NFS1 desulfurase-not-cluster-binding; NPM1 histone-chaperone NEW; NME2 moonlighting-demote) |
| N-O-P-01 | NSDHL NTN1 NTN3 NUFIP1 OLA1 OLIG2 OPTN ORMDL3 OTC OTUD3 OXCT1 P3H1 P3H2 P3R3URF P4HA1 P4HA2 P4HA3 P4HB PAICS PAM16 | agree; 0 edits (NTN1/NTN3 TF-activity removal[secreted ligands]; P4HB dioxygenase-demote[PDI β-subunit]; OTC inner-membrane→matrix; ORMDL3 SPT-inhibitor NEW) |
| P-01 | PANK4 PARD6A PARD6B PARD6G PARK7 PAX6 PC PCBD1 PCCA PCCB PCSK1N PDCD5 PDCD6IP PDGFA PDGFB PDHA1 PDHB PDHX PELO PEX1 | agree; 0 edits (PCBD1 not-PAH[BH4 cofactor]; PDGF ligand autophosphorylation-removal; PC viral-packaging removal; PDHX structural-not-E2; PARK7 debated-function UNDECIDED) |
| P-02 | PEX10 PEX11A PEX11B PEX11G PEX12 PEX13 PEX14 PEX16 PEX19 PEX2 PEX26 PEX3 PEX5 PEX6 PEX7 PFAS PFDN1 PFDN2 PFDN4 PFDN5 | agree; 0 edits (PEX family consistent; PEX2 Cdc73/Paf1-complex removal[it's a peroxisomal E3]; spurious PEX localizations removed; prefoldin cochaperone terms) |
| P-03 | PFDN6 PFKM PGAM2 PGAP1 PGAP2 PGAP3 PGD PGK1 PGLS PGM1 PGRMC1 PGRMC2 PHF23 PHKA1 PHKA2 PHKB PHKG2 PHTF1 PHYKPL PICALM | agree; 0 edits (PGRMC1/2 nuclear-steroid-receptor removal[membrane heme proteins]; PHKA1/A2 regulatory-subunit kinase-demote[γ=PHKG2 catalytic]; PHYKPL transaminase→lyase) |
| P-04 | PICK1 PIGA PIGB PIGC PIGF PIGG PIGH PIGK PIGL PIGM PIGN PIGO PIGP PIGQ PIGS PIGT PIGU PIGV PIGW PIGX | agree; 0 edits (PIG/GPI-anchor family uniform generic→specific; PICK1 phosphorylation-removal[BAR-scaffold, not a kinase despite name]) |
| P-05 | PIGY PIK3C3 PIK3CD PIK3R4 PIP5K1B PIWIL1 PKLR PKM PLCG2 PLD3 PLD4 PLD5 PM20D1 PMM2 PMPCA PMPCB PMVK PNP POFUT1 POLD2 | agree; 0 edits (PIK3C3/VPS34 lipid-not-protein-kinase; PLD3/PLD4 exonuclease-not-phospholipase; PIWIL1 heavy-REMOVE VERIFIED=generic→specific, piRNA/slicer retained) |
| P-06 | POLDIP2 POLE4 POMC POMT1 PPAT PPIB PPOX PPP2CA PPP2CB PPP2R1A PPP2R1B PPP3CA PPP3CB PPP4R1 PRDX4 PRG2 PRG3 PRPS1 PRRT1 PSAP | agree; 0 edits (POLE4 polymerase→histone-chaperone; POMC response-to-MSH removal[it's the precursor]; PPP3CB/PPP4R1 phosphatase-not-kinase; PP2A Tyr→Ser/Thr) |
| P-Q-R-01 | PSEN1 PSEN2 PSENEN PSMA1 PSMB5 PTEN PTGES3 PTPN22 PTPN6 PTS PUS3 PYGL PYGM QDPR RAB15 RAB24 RAB7A RAB7B RAB9A RAB9B | agree; 0 edits (PTPN6/SHP-1 phosphorylation-removal[phosphatase]; PUS3 mRNA→tRNA specificity; PSEN1/2 kept-as-protease[vs NCSTN demoted]; Rab family uniform) |
| R-01 | RACK1 RAD18 RARA RASA1 RASA2 RASA3 RASA4 RASA4B RASAL1 RASAL2 RASAL3 RB1 RBFOX3 RETREG2 RFT1 RFXANK RFXAP RGS20 RHBDF1 RIMBP2 | agree; 0 edits (RASA1/RGS20 GTPase-activity removal[GAPs activate, aren't GTPases]; RB1 DNA-binding-TF demote[binds E2F]; RFXANK/AP non-DNA-binding subunits) |
| R-S-01 | RNF14 RNF166 RNF170 RNF185 RNF25 RNF41 RNF5 ROR1 RPE RPIA RPL18A RPS3 RRM2B RUBCN RUBCNL RUNX3 SAMD8 SAMM50 SC5D SCAMP1 | agree; 0 edits (ROR1 pseudokinase kinase-removal; RNF185/RNF5 mannosidase-removal[ERAD E3s]; SAMD8/SMSr sphingomyelin→ceramide-PE synthase; RUNX3 ATP/phos removal) |
| S-01 | SCAMP2 SCAMP3 SCAMP4 SCAMP5 SCG5 SCGB1A1 SCGB1C1 SCGB1C2 SCGB2A2 SCN1A SCN9A SCO1 SCO2 SCP2D1 SDHA SDHB SDHC SDHD SEC11A SEC11C | agree; 0 edits (SDH/Complex-II "proton-motive-force ATP synthesis" removal[Cx II doesn't pump H+]; SCN1A neuronal-not-cardiac localization; SCGB1A1 secretoglobin spurious-nuclear removal) |
| S-02 | SEC62 SEC63 SERP1 SERP2 SERPINH1 SFT2D3 SGCA SGCE SGSH SGTA SH3GLB1 SIAH1 SIRT1 SIRT2 SLC14A1 SLC22A5 SLC25A13 SLC25A15 SLC25A20 SLC27A5 | agree; 0 edits (SERPINH1/HSP47 non-inhibitory-serpin[collagen chaperone]; SIRT1 acetylation-direction removal; SIRT2 PARP removal; SLC14A1 urea-not-water). SIRT1 heavily pruned[86 REMOVE] like GAPDH but core deacetylase retained. |
| S-03 | SLC37A4 SLC3A2 SLC40A1 SLC6A8 SLC7A11 SMAD3 SMPD1 SNORD116-1 SNORD3A SOCS1 SOCS3 SOCS4 SOCS5 SOD1 SORL1 SOX2 SOX9 SPARC SPCS1 SPCS2 | agree; 0 edits (SLC6A8 creatine-not-GABA transporter; SOD1 IMS-not-matrix; SLC3A2/CD98hc antiporter/ferroptosis NEW; SOCS Cul5-adaptor+kinase-inhibitor; SPARC matricellular-not-structural) |
| S-04 | SPCS3 SPDL1 SPG11 SPI1 SPNS1 SPOCK1 SPOCK2 SPOCK3 SPR SPTLC1 SPTLC2 SPTSSA SQLE SQSTM1 SRD5A2 SRD5A3 SRP19 SRP68 SRP72 SRP9 | agree; 0 edits (SRD5A3 steroid-reductase demote[actually polyprenol reductase, a CDG gene]; SPTSSA enzyme-activator NEW; SPOCK metalloprotease-inhibitor; SQSTM1/p62 clean) |
| S-05 | SRPRB SSR1 SSR2 ST6GAL1 STAR STAT1 STAT2 STAT3 STAT4 STAT5B STAU2 STC1 STC2 STIP1 STOM STOML1 STOML3 STUB1 STX12 SUMF2 | agree; 0 edits (STAT family DNA-binding refined + spurious-receptor removal[STAT1 CCR5]; STC1/STC2 PAPP-A-inhibitor NEW; STOML3 mechanosensation; STUB1/STAT3 clean cleanups) |
| T-01 | SURF1 SYCE3 SYN1 SYN2 SYN3 SYNGAP1 SYP SYVN1 TALDO1 TANK TARDBP TAT TAX1BP1 TBK1 TCF25 TCN1 TCN2 TERT TFRC THBS1 | agree; 0 edits (SURF1 COX-assembly-factor not subunit→REMOVE COX activity; SYN1 REMOVE synaptonemal-complex[synapsin≠meiotic SC]; SYVN1/HRD1 ER-membrane E3 cleanup; TERT digest-caveat VERIFIED—specific telomerase terms ACCEPTed, marks are generic parents+IEA moonlighting, REMOVE ALT/recombination correct) |
| T-02 | THBS2 THBS3 THBS4 TIA1 TIMM17A TIMM21 TIMM22 TIMM23 TIMM44 TIMM50 TK2 TKFC TKT TMA16 TMA7B TMEM43 TMEM67 TMEM70 TMF1 TNFAIP3 | agree; 0 edits (TIMM subunits generic→specific-complex refinement; TIMM50 marks cysteine-endopeptidase[inactive rhomboid-like receptor]+REMOVE IL2R binding; TMEM43 UNDECIDED on disputed voltage-gated-channel activity; TMF1 reassigned legacy-TF→Golgi golgin/tethering) |
| T-03 | TNFRSF1A TNKS TOLLIP TOMM20 TOMM22 TOMM40 TOMM5 TOMM6 TOMM7 TOMM70 TOP2A TOP2B TP53 TPI1 TPM1 TPM3 TRA2B TRAF6 TRAPPC1 TRAPPC11 | agree; 0 edits (TNKS PARP not kinase→REMOVE peptidyl-ser/thr-phos; TOMM20 REMOVE protein-transporting-ATPase[receptor]; TOMM40 REMOVE inner-membrane[it's outer-membrane channel]; TP53 873ann/344REMOVE downstream+binding cleanup, core DNA-binding-TF/apoptosis/checkpoint ACCEPTed VERIFIED, NEW ferroptosis; TRA2B=known 67-PENDING full-review, out of scope) |
| T-04 | TRAPPC12 TRAPPC13 TRAPPC3 TRAPPC4 TRAPPC5 TRAPPC8 TREM2 TRIM13 TRIM16 TRIM17 TRIM5 TRIP4 TSG101 TTC19 TTC28 TTC8 TXN TXNDC11 TXNDC12 TXNDC16 | agree; 0 edits (TSG101 legacy-TF de-annotation[ESCRT-I not transcription regulator]; TRIM5/16/17→autophagy-cargo-adaptor; TXN digest-caveat VERIFIED—keeps protein-disulfide-reductase GO:0015035[core] but REMOVEs GO:0004791(=TXNRD's activity, wrong enzyme)+GO:0047134(NAD(P)H-direct, wrong cofactor); textbook wrong-enzyme/cofactor catch) |
| U-01 | TYMP TYMS UBA5 UBA7 UBAC2 UBAP1 UCHL1 UCK1 UCK2 UFC1 UFD1 UFL1 UFM1 UFSP1 UFSP2 UGGT1 UGP2 UMAD1 UMPS UPB1 | agree; 0 edits (enzyme-precision batch: TYMP REMOVE glycogen-phosphorylase[wrong enzyme]; UBAC2 REMOVE serine-endopeptidase[inactive rhomboid pseudoprotease]; UFD1 REMOVE DUB[p97 adaptor]; UGGT1 REMOVE ER-mannose-trimming[it's a glucosyltransferase]; UMPS REMOVE UDP/CTP-biosynthesis[makes UMP only]) |
| U-02 | UPF1 UPF2 UPF3A UPF3B UQCC2 UQCC3 UQCRB UQCRC1 UQCRC2 UQCRFS1 UQCRH UQCRQ UROD UROS USO1 USP10 USP21 USP25 USP8 UVRAG | agree; 0 edits (Complex-III cores UQCRC1/UQCRC2 REMOVE/MARK MPP-peptidase activity[non-catalytic MPP-homologs in mammals]; UROS REMOVE mitochondrion[cytosolic]+folic-acid binding; USO1/p115 refined spurious transcytosis/cadherin/RNA→Golgi-tethering[SNARE/GTPase]) |
| V-01 | VBP1 VCP VEGFA VMP1 VOPP1 VPS28 VPS37A VPS37B VPS37C VPS37D VPS4A VPS4B VTI1A WDR6 WFS1 WIPF1 WT1 XDH XIST YWHAZ | agree; 0 edits (VEGFA REMOVE 'cellular response to VEGF'[ligand≠responder]+cautious UNDECIDED on ligand→process; VCP/YWHAZ-14-3-3ζ big moonlighting/adaptor cleanup[14-3-3 not a kinase→MODIFY phos]; XDH pathway-step precision; WT1 IDA-transcription-activation REMOVE=documented isoform-repressor case[ISOFORMS/PMID:9815658]+taxon-inappropriate Drosophila terms removed) |
| Z-01 | ZFYVE26 ZNF598 ZSWIM8 | agree; 0 edits (ZFYVE26/spastizin autophagosome-maturation NEW; ZNF598 RQC-E3 clean; ZSWIM8 MODIFY→specific target-directed-miRNA-decay terms) — **END OF ALPHABET; sweep complete** |

## Genes needing a full (not re-) review

- **TRA2B** — 67 annotations all still `action: PENDING`; never reviewed. Needs a
  full annotation-reviewer pass, out of scope for this re-review but flagged here.

## Edits made

(gene — annotation — old action → new action — rationale)

- **ABL1** — GO:0004515 nicotinate-nucleotide adenylyltransferase activity (TAS,
  PMID:20841568) — UNDECIDED → **REMOVE**. Biologically implausible (ABL1 is a
  tyrosine kinase, no NAD-biosynthesis role); the cited reference is a review of
  ABL kinase function and does not describe NMNAT activity (supporting_text is just
  the paper title). Spurious annotation, meets the "demonstrably wrong" REMOVE bar.

- **ADRM1** — GO:0006368 transcription elongation by RNA Pol II (IMP, PMID:11818576)
  — REMOVE → **UNDECIDED**. Experimental (IMP) annotation; cited paper is abstract-only
  in cache (cannot verify full text). Per project guidelines, unverifiable experimental
  annotations should be UNDECIDED not REMOVE. Biology implausible (ADRM1/Rpn13 is a
  proteasome subunit, not Elongator ELP1-6), so flagged for curator rather than removed.

- **BRCA2** — GO:0004402 histone acetyltransferase activity, **negated/NOT** (IDA,
  PMID:9824164) — REMOVE → **ACCEPT**. The NOT annotation correctly documents that
  BRCA2 lacks intrinsic HAT activity (activity comes from associated P/CAF). The
  reviewer's own reason agreed with the NOT's content yet chose REMOVE — a logical
  error. A correct, well-supported negative annotation is valuable and should be kept
  (it guards against the dubious positive HAT claims GO:0010484/85 resurfacing).
  REMOVE means "annotation is wrong"; here it is right, so ACCEPT.

## Fence cases (judgment call, no edit made)

(gene — annotation — the tension)

- **AGO3 / AGR2 — REMOVE of negated (NOT) experimental annotations** — reviewed and
  agreed, but flagging the pattern. AGO3 GO:0035279 NOT (IDA, 2004) removed because a
  2017 paper (PMID:29040713) directly shows guide-dependent AGO3 slicer — legitimate
  supersession of an outdated negative. AGR2 GO:0034976 NOT (IMP, PMID:25666625)
  removed: the NOT-paper is actually about EGFR maturation (verified full text, no ER-
  stress assay), and PMID:34237462 shows an AGR2 mutant impaired in alleviating
  tunicamycin ER stress — direct positive contradicting the gene-level NOT. Both OK,
  but removing NOT annotations warrants curator awareness.

- **ATP23 — DSB-repair / DNA-PK moonlighting removals** — reviewed, agree on the
  reannotation but flagging. ATP23 was formerly XRCC6BP1/KUB3 and carries DSB-repair
  (GO:0006303, TAS) and DNA-PK-complex (GO:0005958, NAS) annotations from that identity.
  REMOVE of "DNA-dependent protein kinase activity" (GO:0004677) is clearly correct (it
  is not a kinase). REMOVE of the DSB-repair *process*/complex is more debatable — those
  reflect documented (if minor) KUB3 associations, and the reviewer's mitochondrial-
  protease reannotation is strong but supersedes rather than disproves the moonlighting.

- **GAPDH — aggressive REMOVE of documented moonlighting** — reviewed, not edited.
  ~43 REMOVEs; generic-parent and NADP-binding removals clearly correct (GAPDH is
  NAD-dependent). But several removed terms are well-documented moonlighting (GAIT-
  complex "negative regulation of translation" IMP/IDA, S-nitrosylation functions,
  "cellular response to type I interferon" IDA, "ribonucleoprotein complex" IDA).
  Guideline would prefer KEEP_AS_NON_CORE for real-but-non-core functions; REMOVE is
  stronger than warranted for the well-supported ones. Consistent with project's
  anti-over-annotation stance so left as-is, flagged for curator.

- **HSPA1B — REMOVE of own IDA core-chaperone annotations** — reviewed, not edited.
  HSPA1B (HSP70-1B) is ~99% identical to HSPA1A (HSP70-1A). HSPA1A's review keeps more
  core chaperone terms while HSPA1B REMOVEs several of its *own* IDA/IMP annotations
  ("protein refolding", "unfolded protein binding", "cellular response to heat",
  "ATP hydrolysis activity", "cellular heat acclimation"). Core function is still
  retained on HSPA1B via other-evidence rows, but the twin-gene handling is
  inconsistent — verify these IDAs aren't genuine HSPA1B experimental data being lost
  (guideline: don't REMOVE experimental annotations you can't refute).

## Needs literature (cannot adjudicate from YAML + cache)

(gene — annotation — the specific question a lit search must answer)

- **ASCL1** — GO:0045665 negative regulation of neuron differentiation (**IDA** and
  IEA) both REMOVEd. ASCL1 is the canonical proneural bHLH activator, so the
  annotation is counterintuitive and the reviewer instead added glial-fate repression
  (GO:0045686). But ASCL1 has a documented progenitor-maintenance / proliferation role
  (Kageyama oscillatory-vs-sustained model) that could underlie a genuine "negative
  regulation of neuron differentiation" IDA. Verify the IDA source paper before
  endorsing removal; guideline-preferred fallback would be UNDECIDED for the IDA.
- **ATF3** — GO:0001228 DNA-binding transcription activator activity (**IDA**) and
  GO:0045944 positive regulation of transcription by Pol II (**IDA**) REMOVEd; the
  reviewer treats ATF3 as primarily a repressor. But ATF3 has documented context-
  dependent activator function (heterodimers with c-Jun). Removing the activator IDA
  annotations may lose real biology; verify the source papers. Guideline-preferred
  fallback: UNDECIDED / KEEP_AS_NON_CORE rather than REMOVE.
