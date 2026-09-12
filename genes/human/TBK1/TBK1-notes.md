# TBK1 (TANK-binding kinase 1) review notes

UniProt Q9UHD2, 729 aa. Non-canonical IKK-related serine/threonine kinase. Domain architecture:
N-terminal protein kinase domain, a ubiquitin-like domain (ULD), a scaffold/dimerization domain,
and a C-terminal coiled-coil region mediating homodimerization
[file:human/TBK1/TBK1-uniprot.txt "and a C-terminal coiled-coil region mediating homodimerization"].
Cytoplasmic [file:human/TBK1/TBK1-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"]. Activated by
trans-autophosphorylation at Ser172. Ubiquitous, higher in testis.

## Core molecular function: protein Ser/Thr kinase

Extensively documented IDA/EXP protein serine/threonine kinase activity (GO:0004674, GO:0106310,
GO:0004672). [file:human/TBK1/TBK1-uniprot.txt "Serine/threonine kinase that plays an essential
role in regulating inflammatory responses to foreign agents"]. ATP binding (GO:0005524) is part of
the catalytic mechanism. This is the unambiguous core MF — ACCEPT all kinase-activity and ATP-binding
annotations (collapse redundant evidence; the EXP/IDA ones are the strongest).

## Core BP 1: innate antiviral immunity / type I IFN induction

TBK1 phosphorylates the innate adaptor proteins MAVS, STING1 (TMEM173), and TICAM1/TRIF on their
pLxIS motif, recruiting and then phosphorylating IRF3 (and IRF7), driving IFN-alpha/IFN-beta
[file:human/TBK1/TBK1-uniprot.txt "acts by first phosphorylating innate adapter proteins MAVS, STING1
and TICAM1 on their pLxIS motif, leading to recruitment of IRF3, thereby licensing IRF3 for
phosphorylation by TBK1"]. [PMID:25636800 "Phosphorylation of innate immune adaptor proteins MAVS,
STING, and TRIF induces IRF3 activation"]. [PMID:14703513] Ser-386 of IRF3 (IDA kinase activity +
antiviral innate immune response + positive regulation of type I IFN production). [PMID:22394562]
STING specifies IRF3 phosphorylation by TBK1 in the cytosolic DNA pathway. cGAS/STING signaling
(GO:0140896, TAS). Core: ACCEPT antiviral innate immune response (GO:0140374), positive regulation
of type I IFN production (GO:0032481), positive regulation of IFN-alpha/IFN-beta production
(GO:0032727/GO:0032728), activation of innate immune response (GO:0002218), cGAS/STING pathway.

## Core BP 2: selective autophagy / mitophagy / xenophagy via autophagy-receptor phosphorylation

TBK1 phosphorylates OPTN/optineurin on Ser177, enhancing LC3 binding and antibacterial autophagy
[PMID:21617041 "The protein kinase TANK binding kinase 1 (TBK1) phosphorylated optineurin on
serine-177, enhancing LC3 binding affinity and autophagic clearance of cytosolic Salmonella"].
[PMID:27035970 "Phosphorylation of OPTN by TBK1 enhances its binding to Ub chains and promotes
selective autophagy of damaged mitochondria"] — mitophagy via OPTN/NDP52/TAX1BP1/SQSTM1.
TBK1 phosphorylates SMCR8 (C9orf72-SMCR8 complex) promoting autophagosome maturation
[file:human/TBK1/TBK1-uniprot.txt "Phosphorylates SMCR8 component of the C9orf72-SMCR8 complex,
promoting autophagosome maturation"]. Phosphorylates ATG8s MAP1LC3C and GABARAPL2 to prevent
delipidation [PMID:31709703]. [PMID:22921120] autophagy-mediated antimicrobial defense / autophagosome
maturation. [PMID:28871090] TRIM23-mediated virus-induced autophagy via TBK1. Core: ACCEPT
positive regulation of macroautophagy (GO:0016239), positive regulation of autophagy (GO:0010508),
positive regulation of xenophagy (GO:1904417), macroautophagy (GO:0016236).

## Core BP 3: NF-kappaB activation (the original "TANK-binding kinase")

Original identification as IKK-related kinase activating NF-kappaB via a TRAF2-TANK-TBK1 complex
[PMID:10581243 "NF-kappaB activation by a signaling complex containing TRAF2, TANK and TBK1, a novel
IKK-related kinase"]. [PMID:10783893 "NAK is an IkappaB kinase-activating kinase"]. Under particular
conditions TBK1 phosphorylates NFKBIA, IKBKB, or RELA. [PMID:12761501] IEP positive regulation of
canonical NF-kappaB. canonical NF-kappaB signal transduction (GO:0007249, TAS). These are real
but more context-specific than the dominant IRF3/IFN and autophagy axes; treat NF-kappaB BP terms as
ACCEPT (well-established) or KEEP_AS_NON_CORE for the most generic.

## Secondary / pleiotropic roles -> KEEP_AS_NON_CORE

- mTOR signaling: activates mTORC1 in response to growth factors (GO:1904263 pos reg TORC1,
  PMID:29150432) but also limits mTORC1 via RPTOR Ser877 (GO:1904262 neg reg TORC1, PMID:31530866);
  positive regulation of TORC2 (GO:1904515, ISS/IEA); positive regulation of TOR signaling
  (GO:0032008, IEA). Context-dependent, pleiotropic -> KEEP_AS_NON_CORE.
- AKT1 phosphorylation (PMID:21464307) -> reflected in kinase activity EXP annotation.
- T follicular helper cell differentiation (GO:0061470, PMID:27135603) -> developmental/pleiotropic,
  KEEP_AS_NON_CORE.
- TLR4 signaling (GO:0034142, PMID:28747347), TLR-pathway -> KEEP_AS_NON_CORE (upstream context).
- inflammatory response (GO:0006954), response to virus (GO:0009615), defense response (GO:0006952),
  response to other organism (GO:0051707) -> generic parents, KEEP_AS_NON_CORE.
- positive regulation of transcription by RNA Pol II (GO:0045944, PMID:16127453) -> indirect
  (via IRF activation), KEEP_AS_NON_CORE.
- peptidyl-serine/threonine phosphorylation (GO:0018105/GO:0018107), protein phosphorylation
  (GO:0006468) -> generic MF-process parents of the specific substrate phosphorylations,
  KEEP_AS_NON_CORE.
- RAB7 phosphorylation in TNBC (PMID:31662325) -> kinase activity EXP.
- regulation of RIPK1-mediated cell death (RIPK1 T189, Reactome) -> not a standalone GOA BP here.

## Localization

Cytoplasm/cytosol is the core compartment (many EXP/IDA/IBA/TAS). ACCEPT cytoplasm/cytosol
is_active_in/located_in (collapse the dozens of redundant Reactome cytosol located_in to
KEEP_AS_NON_CORE as generic pathway-step localizations, but they are correct).
GO:0005654 nucleoplasm (IDA, GO_REF:0000052 immunofluorescence/HPA) — a minor pool; TBK1 is
predominantly cytoplasmic and acts there. KEEP_AS_NON_CORE.

## protein binding / interaction annotations

Dozens of IPI GO:0005515 "protein binding" annotations record interactions with adaptors (TANK,
AZI2/NAP1, SINTBAD/TBKBP1, OPTN, STING, MAVS, TRAF3, DDX3X, SIKE, IFIT3, RIOK3, etc.), regulators,
and numerous viral antagonists (HCV NS2/NS3/NS4B, SARS-CoV/CoV-2 M/nsp6/nsp13, MERS M, Ebola VP35,
vaccinia C6, rotavirus NSP1, gammaherpesvirus ORF11, etc.). Functionally important but bare
protein binding is uninformative -> KEEP_AS_NON_CORE for all GO:0005515.

Specific informative interaction MFs:
- GO:0061629 RNA Pol II transcription factor binding (PMID:22412986, IRF5) -> KEEP_AS_NON_CORE
  (records substrate/IRF binding; the kinase activity is the core).
- GO:0051219 phosphoprotein binding (PMID:14530355) -> KEEP_AS_NON_CORE.
- GO:0019903 protein phosphatase binding (IEA/ISS) -> KEEP_AS_NON_CORE.
- GO:0042802 identical protein binding (IEA, homodimerization) -> KEEP_AS_NON_CORE (real homodimer
  but uninformative term; the coiled-coil mediates homodimerization).

## REMOVE candidates (clearly-wrong electronic over-propagations)

- GO:0003676 nucleic acid binding (IEA, GO_REF:0000107 Ensembl ortholog): TBK1 is a protein kinase;
  there is no evidence it is a sequence-nonspecific nucleic-acid-binding protein. This looks like an
  erroneous orthology-based electronic transfer. MARK_AS_OVER_ANNOTATED (or REMOVE) — choose
  MARK_AS_OVER_ANNOTATED to be conservative since it is electronic, not experimental.
- GO:0010629 negative regulation of gene expression (IEA, GO_REF:0000107 ortholog): overly generic,
  not the documented TBK1 role (TBK1 positively drives IFN/antiviral gene expression). Electronic
  ortholog transfer -> MARK_AS_OVER_ANNOTATED.

Both are IEA (no experimental basis) so safe to flag; not experimental annotations.

## Disease relevance (context for description, not GO actions)

Familial ALS/FTD (haploinsufficiency, PMID:25803835), normal-tension/POAG glaucoma (GLC1P, OPTN
axis, PMID:18307994), herpes simplex encephalopathy (IIAE8), autoinflammation (AIARV). These
underscore the autophagy/innate-immunity core functions.
</content>
