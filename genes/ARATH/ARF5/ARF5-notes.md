# ARF5 / MONOPTEROS (MP) — Curation Notes

UniProt: P93024 (ARFE_ARATH). Gene: ARF5; synonyms IAA24, MP; locus At1g19850. 902 aa.

## Overview

ARF5/MONOPTEROS is a B3-domain AUXIN RESPONSE FACTOR (ARF) transcription factor that functions as a
sequence-specific transcriptional **activator**. It binds auxin response elements (AuxREs; the
5'-TGTCTC-3' motif) in the promoters of auxin-responsive genes and activates their transcription.
ARF5 is one of only ~5 of the 23 Arabidopsis ARFs that act as transcriptional activators (the rest are
repressors) [PMID:21734647 "sequence analysis and transient assays suggest that most of the 23 ARFs act as transcriptional repressors, while only 5 (ARF5, 6, 7, 8 and 19) of them are activators"].

It is essential for embryonic apical-basal axis (body axis) formation, root meristem initiation, and
vascular patterning, and acts post-embryonically in vascular development, leaf vascular patterning,
flower primordium initiation, and meristem maintenance.

## Domain architecture (UniProt features)

- DNA-binding TF-B3 domain: aa 158-260 (binds AuxRE).
- PB1 domain (formerly domains III/IV): aa 793-877 — mediates dimerization with Aux/IAA proteins and
  ARF-ARF dimerization. Disordered middle region (Q-rich) drives transcriptional activation.
- Crystal structures: 4LDU (DBD, 1-390), 4CHK and 6L5K (PB1/C-terminal).

## Molecular function

- DNA-binding transcription factor activity (activator). UniProt: "Auxin response factors (ARFs) are
  transcriptional factors that bind specifically to the DNA sequence 5'-TGTCTC-3' found in the
  auxin-responsive promoter elements (AuxREs). Seems to act as transcriptional activator."
- Cloning paper established MP encodes a TF with NLS and a DBD similar to auxin-promoter-binding domain
  [PMID:9482737 "The predicted protein product contains functional nuclear localization sequences and a DNA binding domain highly similar to a domain shown to bind to control elements of auxin inducible promoters"].
- Structural basis: ARF DBDs homodimerize for cooperative DNA binding, critical for in vivo function
  [PMID:24485461 "We show that ARF DNA-binding domains also homodimerize to generate cooperative DNA binding, which is critical for in vivo ARF5/MP function"]. ARF5 homodimer binds AuxRE pairs with characteristic spacing ("molecular caliper" model).
- Direct in vivo target binding: ChIP shows MP binds AuxRE-containing fragments in the DRN promoter
  [PMID:19369397 "Chromatin immunoprecipitation experiments show that MP binds in vivo to two AuxRE-spanning fragments in the DRN promoter"]. Other direct targets include LFY, ANT, AIL6, FIL, TMO3.
- cis-regulatory binding in Y1H network for secondary cell wall genes (e.g. IRX14/AT1G71930)
  [PMID:25533953].

## Protein-protein interactions (PB1/CTD domains III & IV)

ARF5 forms homodimers and heterodimers with Aux/IAA repressors.
- Interacts with IAA12/BODENLOS (BDL) — Y2H, inhibits MP in root meristem initiation
  [PMID:12101120 "BODENLOS and MONOPTEROS interact in the yeast two-hybrid assay and the two genes are coexpressed in early embryogenesis, suggesting that BODENLOS inhibits MONOPTEROS action in root meristem initiation"].
- Interacts with IAA17/AXR3 (heterodimerization via domain III) [PMID:11283339 "heterodimerization of the revertant forms of IAA17/AXR3 with IAA3/SHY2, another Aux/IAA protein, and ARF1 or ARF5/MP proteins is affected only by changes in domain III"].
- IntAct: IAA1 (P49677), IAA12 (Q38830), IAA13 (Q38831), IAA14 (Q38832), IAA19 (O24409), self (P93024).
- Large-scale interactome confirms ARF5 interacts with many Aux/IAAs and homodimerizes [PMID:22096563 "the transcription activator ARF5 stood out among the tested ARFs to interact with 10 Aux/IAA proteins"; PMID:21734647].
- IAA19 (MSG2) interaction reported in [PMID:14729917] context (ARF-Aux/IAA interaction via CTD; this paper is primarily on ARF7/NPH4 but IntAct used it for ARF5-IAA19).
- IAA14/SLR interaction context [PMID:16236149] (IntAct, Q38832).
- Self-dimerization / identical protein binding [PMID:24485461 (structural homodimer), PMID:21734647, PMID:22096563].

Note: GO:0005515 "protein binding" annotations all derive from these IntAct/TAIR interaction datasets.
These are mostly Aux/IAA repressors. Per curation guidelines, bare "protein binding" is uninformative;
the informative MF is GO:0140297 "DNA-binding transcription factor binding" (ARF5 binds Aux/IAA
transcriptional repressors / co-binds with chromatin remodelers) and GO:0042802 "identical protein
binding" (homodimerization is functionally meaningful for DNA binding per PMID:24485461).

PMID:26460543 protein-binding annotation: MP recruits SWI/SNF chromatin remodeling ATPases (BRM/SYD)
[PMID:26460543 "the MONOPTEROS transcription factor recruits SWI/SNF chromatin remodeling ATPases to increase accessibility of the DNA for induction of key regulators of flower primordium initiation"]. The TAIR annotation links AT2G28290 (SYD) and AT2G46020 (BRM).

## Regulation by Aux/IAA / auxin

In low auxin, Aux/IAA proteins (e.g. BDL/IAA12) bound to the MP C-terminal domain recruit TOPLESS
co-repressor and HDA19 histone deacetylase, blocking activation; auxin triggers Aux/IAA degradation,
freeing MP and allowing SWI/SNF recruitment [PMID:26460543]. MP autoregulates its own expression and
that of BDL [PMID:21478855 "the Arabidopsis ARF protein MONOPTEROS (MP) controls its own expression and the expression of its AUX/IAA inhibitor BODENLOS (BDL)"].

## Biological processes (mostly developmental, pleiotropic)

- Embryonic body/longitudinal axis formation; root meristem initiation [PMID:9482737, PMID:8904808, PMID:12101120].
- Vascular strand formation / xylem & phloem patterning [PMID:8904808 "the vascular strands in all analyzed organs are distorted"; PMID:9482737]; leaf vascular tissue pattern formation.
- Cell axialization / cell file formation [PMID:8904808 "the MP gene promotes cell axialization and cell file formation at multiple stages of plant development"].
- Embryo & meristem development, antagonism with AMP1 [PMID:17553903 "auxin-derived positional information through MP carves out meristematic niches by locally overcoming a general differentiation-promoting activity involving AMP1"].
- Flower primordium initiation [PMID:26460543]; flower development [PMID:17553903].
- Response to auxin (auxin-activated signaling) — UniProt keyword "Auxin signaling pathway".

GO:0009942 (longitudinal axis specification) and GO:0010051 (xylem/phloem pattern formation) are the
classic mp loss-of-function phenotypes (Przemeck 1996) — strong IMP support.

## Core function synthesis

Core MF: sequence-specific DNA-binding transcriptional activator acting at AuxRE elements (auxin-activated).
Core BP: auxin-activated signaling pathway controlling embryonic axis/vascular/meristem patterning.
Core CC: nucleus.

## Action decisions summary

- GO:0003700 DNA-binding transcription factor activity (ISS x2, TAS) — ACCEPT (core MF; well supported).
- GO:0003677 DNA binding (IEA) — MODIFY to GO:0003700 (too general for a known TF; but DNA binding is parent — actually keep as accept-but-general; chosen MODIFY -> GO:1990837 sequence-specific double-stranded DNA binding / GO:0003700). Given a more specific TF activity term already annotated, mark the bare "DNA binding" as redundant/over-general: MARK_AS_OVER_ANNOTATED is reasonable, but MODIFY to a specific term is preferred per instructions.
- GO:0000976 transcription cis-regulatory region binding (IDA PMID:19369397; IPI PMID:25533953) — ACCEPT (direct AuxRE/promoter binding).
- GO:0005634 nucleus (IEA/ISM/ISS) — ACCEPT (location).
- GO:0006355 regulation of DNA-templated transcription (IEA, IEP) — ACCEPT / acceptable broad BP.
- GO:0009725 response to hormone (IEA) — MARK_AS_OVER_ANNOTATED (too general; response to auxin is specific).
- GO:0009733 response to auxin (IEP) — ACCEPT (core; auxin-activated).
- GO:0005515 protein binding (many) — REMOVE (uninformative) in favor of GO:0140297 / GO:0042802.
- GO:0042802 identical protein binding (homodimer) — ACCEPT/KEEP (functionally relevant for DNA binding).
- Developmental BPs (embryo dev, flower dev, root dev, meristem dev, leaf vascular patterning, longitudinal axis, xylem/phloem patterning) — KEEP_AS_NON_CORE (pleiotropic downstream developmental roles) except those most directly tied to vascular/axis which represent the canonical mp phenotype.

NEW: GO:0140297 DNA-binding transcription factor binding (binds Aux/IAA repressors); GO:0001228 / activator-class
RNA Pol II activity considered but GO:0003700 already captures activator TF activity. Add
GO:0009734 auxin-activated signaling pathway (in UniProt DR line, IEA:UniProtKB-KW) — but this is not in GOA tsv,
so add as NEW with KW support.
