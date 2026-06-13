# RNF170 review notes

UniProt: Q96K19 (RN170_HUMAN), 258 aa, gene RNF170. HGNC:25358. Chromosome 8. Multi-pass ER membrane protein.

## Core identity
RNF170 is a multi-pass ER-membrane RING-type E3 ubiquitin ligase (EC 2.3.2.27). C3HC4 RING domain (ZN_FING 87-130; catalytic residues Cys-102/His-104; C102S/H104A double mutant completely abolishes ligase activity). Three transmembrane helices (25-45, 202-222, 224-244) anchor it in the ER membrane with a large cytoplasmic loop (46-201) carrying the RING.

[file:human/RNF170/RNF170-uniprot.txt "E3 ubiquitin-protein ligase that plays an essential role in stimulus-induced inositol 1,4,5-trisphosphate receptor type 1 (ITPR1) ubiquitination and degradation"]
[file:human/RNF170/RNF170-uniprot.txt "MUTAGEN 102 ... C->S: Complete loss of E3 ligase activity; when associated with A-104"]

## Primary role: IP3R/ITPR1 ERAD with the ERLIN1/ERLIN2 complex
RNF170 is essential for stimulus-induced ubiquitination and ERAD-mediated degradation of the inositol 1,4,5-trisphosphate receptor (ITPR1/IP3R), and also for ITPR1 turnover in resting cells. It is constitutively associated with the ERLIN1/ERLIN2 complex and interacts with activated ITPR1. This is the founding/defining function (Lu et al. 2011, PMID:21610068).

[file:human/RNF170/RNF170-uniprot.txt "Also involved in ITPR1 turnover in resting cells"]
[file:human/RNF170/RNF170-uniprot.txt "Constitutively associated with the ERLIN1/ERLIN 2 complex. Interacts with activated ITPR1"]

Note: This IP3R/ERLIN role is NOT explicitly represented in the current GOA (the GOA has no ITPR1-ERAD term). It is captured here in description, core_functions, and a proposed_new_term, with provenance from the UniProt record / PMID:21610068. PMID:21610068 is not in the cached publications/ folder; supporting text is taken verbatim from the UniProt file.

## Secondary role: TLR3 degradation / innate immunity
RNF170 binds TLR3 and mediates K48-linked polyubiquitination of K766 in the TLR3 TIR domain, promoting proteasomal degradation and selectively inhibiting TLR3-triggered innate immune responses (Song et al. 2020, PMID:31076723; mainly murine cells). This is the source of the K48 ubiquitination, negative regulation of TLR3 signaling, and IDA ligase-activity / ER-membrane annotations in the GOA.

[PMID:31076723 "RNF170 mediated the K48-linked polyubiquitination of K766 in the TIR domain of TLR3 and promoted the degradation of TLR3 through the proteasome pathway"]
[PMID:31076723 "The genetic ablation of RNF170 selectively augmented TLR3-triggered innate immune responses both in vitro and in vivo"]

## Disease
Mutations cause autosomal dominant sensory ataxia (SNAX1; R199C) and autosomal recessive hereditary spastic paraplegia (SPG85; e.g. C102R, C107W). RING-region (C102) variants link the ligase activity to neurodegeneration, consistent with its role in IP3R/ER calcium-channel homeostasis.

## Localization
ER membrane (PMID:21610068, PMID:31076723), multi-pass. This is the core compartment.

## Annotation review decisions (summary)
- ubiquitin protein ligase activity (GO:0061630): CORE, ACCEPT (IDA PMID:31076723, EC 2.3.2.27; RING C102S/H104A abolishes).
- ER membrane (GO:0005789): CORE location, ACCEPT (IDA + IEA).
- protein K48-linked ubiquitination (GO:0070936): ACCEPT (IDA, degradative topology on TLR3; also used on ITPR1).
- negative regulation of TLR3 signaling pathway (GO:0034140): KEEP_AS_NON_CORE (real, but secondary immunity role; the core role is IP3R ERAD).
- protein ubiquitination (GO:0016567, IEA UniPathway): KEEP_AS_NON_CORE (generic parent).
- protein binding (GO:0005515, IPI x2): KEEP_AS_NON_CORE (uninformative; includes PSMA6 proteasome subunit and isoform-5 interactome partners).
- proposed_new_term: ITPR1/IP3R ERAD + ERLIN complex membership (the defining function, currently missing from GOA).

## Falcon deep-research findings (incorporated 2026-06)

- Recessive (biallelic) RNF170 variants cause autosomal recessive HSP (SPG85), established in four unrelated families with functional validation in patient fibroblasts, mutant SH-SY5Y cells, and zebrafish knockdown [PMID:31636353 "mutations in the ubiquitin E3 ligase gene RNF170, which targets inositol 1,4,5-trisphosphate receptors for degradation, are the likely cause of autosomal recessive HSP in four unrelated families"]. Added as a reference; previously the SPG85 link was only in description without a cited primary genetics paper.
- That genetics study mechanistically ties disease to failure of the RNF170-mediated ITPR1/IP3R ERAD pathway and altered ER Ca2+ release signaling [PMID:31636353 "Activated inositol 1,4,5-trisphosphate receptors are then rapidly degraded by the endoplasmic reticulum-associated degradation pathway"], reinforcing the existing core IP3R-ERAD function annotation (added PMID:31636353 id to that NEW annotation's supported_by).
- Falcon reports patient-derived fibroblasts fail to show stimulus-dependent IP3R-3 degradation and RNF170-KO SH-SY5Y cells show elevated basal IP3R-1 with rescue by WT RNF170 (Wagner 2019); consistent with RNF170 constraining IP3R abundance [DOI:10.1038/s41467-019-12620-9].
- ERLIN1/2 SPFH scaffolds bind a conserved luminal N-terminal motif shared by RNF170 and TMUB1-L, bridging them in cholesterol-rich ER nanodomains (already in review as PMID:38782601) [DOI:10.26508/lsa.202402620].
- Falcon also surfaced the ERLIN1 SPG62 cohort (Cogan 2024, n=13) and a Trends Neurosci review (Van de Vondel 2024) framing the ERLIN1/2-RNF170-IP3R module as a recurrent neurogenetic mechanism; these are about ERLIN1/pathway context rather than RNF170 directly, so not added as RNF170 references [DOI:10.1007/s00439-024-02702-0; DOI:10.1016/j.tins.2024.01.004].
- Song 2020 TLR3 study (already PMID:31076723) and the Lu 2011 founding IP3R-ERAD paper (already PMID:21610068) were re-confirmed by Falcon; no change.
