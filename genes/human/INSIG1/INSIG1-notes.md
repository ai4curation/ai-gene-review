# INSIG1 (O15503) review notes

## Deep research status

- 2026-10-18: `just deep-research human INSIG1 --provider falcon` was tried once and failed
  at login ("Exception: Failed to authenticate"; the Falcon/Edison key is not authorised).
  No deep-research file was generated. These notes are built from cached primary literature
  (`publications/`), the UniProt record and GOA instead.

## Identity and family

- INSIG1 (insulin-induced gene 1, rat CL-6) is a polytopic ER membrane protein, PANTHER
  PTHR15301:SF11 (family PTHR15301, INSIG). The human gene is on 7q36
  [PMID:9268630 "Rat CL-6 is the most highly insulin-induced gene in a liver cell line"].
- INSIG1 and INSIG2 are 59% identical paralogs with six transmembrane helices
  [PMID:12242332 "The sequences of human insig-1 and -2 are 59% identical. Both proteins are predicted to contain six transmembrane helices."].
- Distant bacterial homolog MvINS (Mycobacterium) gives the six-TM fold
  [PMID:26160948 "Each protomer comprises six transmembrane segments (TMs), with TM3 and TM4 contributing to homotrimerization."].

## Core function 1: sterol-dependent ER retention of SCAP-SREBP

- Discovery: INSIG1 binds the sterol-sensing domain of SCAP and retains SCAP/SREBP in the ER
  [PMID:12202038 "we identify INSIG-1 as an ER protein that binds the sterol-sensing domain of SREBP cleavage-activating protein (SCAP) and facilitates retention of the SCAP/SREBP complex in the ER"].
- Sterols induce the SCAP-INSIG1 interaction; SCAP(Y298C) cannot bind and escapes regulation
  [PMID:12202038 "Mutant SCAP(Y298C) fails to bind INSIG-1 and is resistant to sterol-mediated inhibition of ER exit."].
- Mechanism: INSIG is required for sterol inhibition of Sar1-dependent Sec23/24 (COPII) binding to the
  MELADL signal of SCAP [PMID:15899885 "This in vitro inhibition is dependent on the presence of Insig-1"];
  sterols and Insig render MELADL inaccessible [PMID:17428919 "Cholesterol and oxysterols block COPII binding to MELADL by binding to different intracellular receptors, cholesterol to Scap and oxysterols to Insig."].
- Insigs lower the cholesterol concentration needed for the SCAP conformational change
  [PMID:12963821 "Insig proteins reduce the concentration of cholesterol needed in vitro to produce the conformational change in SCAP"].
- Feedback: INSIG1 transcription needs nuclear SREBPs (unlike INSIG2)
  [PMID:12242332 "production of insig-1, but not insig-2, in cultured mammalian cells requires nuclear SREBPs"];
  at high expression INSIG1 (not INSIG2) blocks SCAP movement even without exogenous sterols
  [PMID:12242332 "at high levels of expression, insig-1, but not insig-2, can block SCAP movement in the absence of exogenous sterols"].
- Free INSIG1 is ubiquitinated (Lys156/158) and degraded upon sterol depletion; binding to SCAP protects it
  [PMID:16399501 "Upon sterol deprivation, the Scap/SREBP complex dissociates from Insig-1, which is then ubiquitinated on lysines 156 and 158 and degraded in proteasomes."].
- Asp205 (juxtamembrane, TM4) is required for SCAP binding and HMGCR degradation
  [PMID:16606821 "When Asp-205 was mutated to alanine, the mutant Insig-1 lost the ability to bind to Scap"].
- PAQR3 competes with INSIG1 for SCAP and tethers SCAP-SREBP to Golgi
  [PMID:26311497 "increasing expression of Insig-1 reduced SREBP-2 processing"].

## Core function 2: oxysterol sensing

- Oxysterols (25-hydroxycholesterol) act by binding Insigs; TM3/TM4 are important
  [PMID:17428920 "Here, we show that oxysterols act by binding to Insigs, causing Insigs to bind to Scap."].
- Structure of human SCAP-INSIG2-25HC (paralog) shows 25HC sandwiched between SCAP S4-S6 and Insig TM3/4
  [PMID:33446483 "A 25HC molecule is sandwiched between the S4 to S6 segments in Scap and TMs 3 and 4 in Insig-2 in the luminal leaflet of the membrane."].
- PCK1 (single lab, HCC cells) phosphorylates INSIG1 Ser207, which reduces sterol binding and releases SCAP
  [PMID:32322062 "This phosphorylation reduces the binding of sterols to INSIG1 and INSIG2 and disrupts the interaction between INSIG proteins and SCAP"].
  The IDA rows for oxysterol binding/retention from this paper are consistent with the Brown-Goldstein work.

## Core function 3: adaptor for sterol-accelerated ERAD of HMGCR (and ACAT2)

- INSIG1 binds the HMGCR sterol-sensing domain and triggers its degradation
  [PMID:12535518 "degradation of HMG CoA reductase is accelerated by the sterol-induced binding of its sterol-sensing domain to the ER protein insig-1"].
- INSIG1 bridges gp78/AMFR (E3) and VCP to HMGCR
  [PMID:16168377 "Insig-1 as a bridge between gp78/VCP and the reductase substrate"].
- Both Insigs bind TRC8/RNF139; gp78 binds INSIG1 but not INSIG2
  [PMID:22143767 "Insig-1, but not Insig-2, coimmunoprecipitated with gp78"].
- RNF145 also binds INSIG1/2 [PMID:29374057 "RNF145 interacts with Insig-1 and -2 proteins and ubiquitinates HMGCR"].
- Insigs are adaptors recruiting ACAT2 to gp78 [PMID:28604676 "Insigs work as adaptors to recruit substrates including ACAT2 and HMGCR24."].
- GO: GO:1990756 ubiquitin-like ligase-substrate adaptor activity fits; there is no GO process term for
  regulated (non-quality-control) ERAD of a native enzyme. GO:0036503 "ERAD quality control pathway"
  is defined for misfolded/aberrant proteins, so it was not proposed.

## Annotation decisions (summary)

- protein binding: SCAP rows MODIFY -> GO:0140311; AMFR/HMGCR rows MODIFY -> GO:1990756; P450
  (PGRMC1 study) and HuRI Y2H rows REMOVE (uninformative).
- ER (GO:0005783): MODIFY -> ER membrane (GO:0005789), all rows, same in INSIG2.
- cholesterol biosynthetic process / cholesterol metabolic process: MODIFY -> GO:0045541 negative
  regulation of cholesterol biosynthetic process (INSIG does not perform the synthesis). Same in INSIG2.
- cellular response to insulin stimulus IBA: MARK_AS_OVER_ANNOTATED. The node's donor is rat Insig1
  IEP (expression induction, PMID:19299314 per QuickGO); insulin regulates INSIG1/2 transcription in
  opposite directions (INSIG2a is repressed, PMID:12624180), so it is not a conserved protein function. Same in INSIG2.
- regulation of transcription by RNA pol II NAS: MARK_AS_OVER_ANNOTATED (indirect, via SREBP processing).
- Core: GO:0140311, GO:0008142, GO:0036316, GO:1901303, GO:0032937, GO:0005789; GO:1990756 (HMGCR ERAD).
- GO-CAM 6205c24300000880 models INSIG1 as oxysterol binding + protein sequestering activity in
  GO:0036316 at the ER membrane, consistent with this review.
