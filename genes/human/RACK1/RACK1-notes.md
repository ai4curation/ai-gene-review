# RACK1 (GNB2L1 / P63244) review notes

## Identity / core
RACK1 = "Receptor for Activated C Kinase 1"; a seven-bladed WD40 beta-propeller protein.
It is now classified as an integral component of the small (40S) ribosomal subunit
("Small ribosomal subunit protein RACK1", RACK1/RPS27A-family naming per Ban et al. 2014
nomenclature, PMID:24524803). It sits on the head of the 40S near the mRNA exit channel.

UniProt FUNCTION: "Component of the 40S ribosomal subunit involved in translational
repression (PubMed:23636399). Involved in the initiation of the ribosome quality control
(RQC), a pathway that takes place when a ribosome has stalled during translation, by
promoting ubiquitination of a subset of 40S ribosomal subunits (PubMed:28132843)."
[file:human/RACK1/RACK1-uniprot.txt]

## Ribosome / RQC core function (best-supported, the curation focus)
- Structural: integral 40S component, seen in 80S cryo-EM [PMID:23636399 "Structures of the
  human and Drosophila 80S ribosome"; PMID:25901680 "Structure of the human 80S ribosome"].
- RQC: RACK1 is required to resolve poly(A)-induced stalled ribosomes by regulating 40S
  ribosomal ubiquitylation [PMID:28132843 "the 40S ribosomal protein RACK1 help to resolve
  poly(A)-induced stalled ribosomes"; "RACK1 regulates RPS2, RPS3, and RPS20 ubiquitylation"].
  Loss of RACK1 (or ZNF598) causes defective resolution of stalled ribosomes and readthrough
  of poly(A) stall sequences. RACK1 thus acts upstream/alongside the ZNF598 E3 ligase as the
  ribosomal scaffold for collision-sensing and regulatory 40S ubiquitylation.
- IBA transfers from yeast Asc1: rescue of stalled cytosolic ribosome (GO:0072344), negative
  regulation of translational frameshifting (GO:2001125), ribosome binding (GO:0043022),
  negative regulation of translation (GO:0017148). These are well supported by the yeast Asc1
  literature and human RQC work => core/QC.

## Moonlighting / signaling roles (well-documented but many are scaffold-context-specific)
RACK1 is a classic signaling scaffold. UniProt lists dozens of partners. These reflect a
genuine adaptor/scaffold activity but most individual BP annotations are context-specific
(single-study, single pathway). Per batch curation rules I keep the genuine scaffold MF
(molecular adaptor / PKC binding) but mark individual pathway BP transfers as non-core or
over-annotation when supported only by a single moonlighting study, and demote the dozens of
bare "protein binding" (GO:0005515) IPI interactome hits to non-core (they record real
interactions but are uninformative as MF).

Notable: binds/stabilizes active PKC (GO:0005080 protein kinase C binding, IDA PMID:11279199);
inhibits SRC-family kinases (GO:0030292 protein tyrosine kinase inhibitor activity IDA
PMID:9584165); promotes HIF1A and CLEC1B ubiquitin-dependent degradation; scaffold for many
GPCR/channel trafficking events. These are bona fide but peripheral to the ribosomal core.

## Localization
Overwhelmingly cytoplasmic/ribosome-associated (cytosol, 40S subunit). Reported nuclear,
plasma membrane, perinuclear, dendrite, mitochondrion, exosome localizations are context- or
moonlighting-specific; cytosol/small ribosomal subunit are the core compartments. Mitochondrion
(IMP PMID:19767770) and extracellular exosome (HDA) are over-annotations relative to core.

## Curation decisions summary
- Core MF: structural constituent of ribosome (40S) + ribosome binding; RQC scaffold.
- Core BP: rescue of stalled cytosolic ribosome (RQC); cytoplasmic translation / translational
  repression kept non-core (broad).
- Signaling scaffold MF (molecular adaptor activity, PKC binding) kept but non-core.
- Bare protein binding IPI (interactome): KEEP_AS_NON_CORE (real interactions, uninformative MF).
- Single-study moonlighting BP/CC: KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED.
