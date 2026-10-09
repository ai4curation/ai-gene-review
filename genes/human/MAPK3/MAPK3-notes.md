# MAPK3 (ERK1, P27361) curation notes

## Identity and core molecular function

- MAPK3 encodes ERK1/p44-MAPK, a CMGC-family proline-directed Ser/Thr kinase; the
  paralog MAPK1 encodes ERK2/p42. [file:human/MAPK3/MAPK3-deep-research-falcon.md
  "MAPK3 is an ATP-dependent, proline-directed protein serine/threonine kinase."]
- UniProt function: [file:human/MAPK3/MAPK3-uniprot.txt "Serine/threonine kinase which
  acts as an essential component of the MAP kinase signal transduction pathway"]
- Activation by MEK1/2 on the TEY motif: [file:human/MAPK3/MAPK3-uniprot.txt
  "Phosphorylated by MAP2K1/MEK1 and MAP2K2/MEK2 on Thr-202 and Tyr-204 in response to
  external stimuli like insulin or NGF. Both phosphorylations are required for activity."]
- Direct biochemical evidence with human ERK1: [PMID:8388392 "The purified MEK2 protein
  stimulated threonine and tyrosine phosphorylation on ERK1 and concomitantly activated
  ERK1 kinase activity more than 100-fold."]; cloned human erk1 has MBP kinase activity
  [PMID:7687743 "it exhibited a relatively high level of myelin basic protein
  phosphotransferase activity"].
- ERK1-specific substrate evidence: DEPTOR S235 [PMID:35216969 "An in vitro kinase
  assay confirmed the ability of recombinant activated ERK1 to directly phosphorylate
  DEPTOR on S235"]; MED1 [PMID:18391015 "phosphorylation of MED1 by mitogen-activated
  protein kinase-extracellular signal-regulated kinase (MAPK-ERK) promotes its
  association with Mediator"]; PARP1 [PMID:16627622 "restored by incubation with active
  ERK1 or ERK2"]; PD-1 [PMID:37208329 "ERK1 was the most potent kinase to elevate PD-1
  protein abundance in cells"].
- Autophosphorylation is minor/in vitro only: [PMID:7687743 "It underwent further
  autophosphorylation in vitro (up to 0.01 mol of P per mol) at the regulatory Tyr-204
  site"]; [file:human/MAPK3/MAPK3-deep-research-falcon.md "ERKs have negligible
  basal/autophosphorylation activity under ordinary conditions and normally depend on
  upstream MAP2Ks."] -> peptidyl-tyrosine autophosphorylation treated as over-annotation.

## Localization

- Dynamic cytoplasm/cytosol <-> nucleus shuttling; resting cells cytoplasmic
  [file:human/MAPK3/MAPK3-deep-research-falcon.md "In resting cells, ERK is commonly
  cytoplasmic because of anchoring by MEK and proteins such as PEA-15."].
- Nuclear accumulation on stimulation [file:human/MAPK3/MAPK3-uniprot.txt
  "Autophosphorylation at Thr-207 promotes nuclear localization"].
- ERK1-specific (rat ortholog) caveola and focal adhesion (GIT1-dependent) are in UniProt;
  kept as non-core. Endosome/Golgi/mitochondrion/cytoskeleton rows come from the Yao &
  Seger 2009 review (PMID:19565474) and ARBA rules; these are compartment-restricted pools,
  treated as over-annotations, consistent with MAPK1 review.
- Nuclear envelope IDA (PMID:20455999) is an insulin/caveolin-2-specific event
  ["insulin-activated extracellular signal-regulated kinase (ERK) is translocated to the
  nuclear envelope by caveolin-2 (cav-2)"] -> non-core.

## Processes

- Core: ERK1 and ERK2 cascade (GO:0070371) / MAPK cascade, protein phosphorylation,
  intracellular signal transduction.
- Many downstream process rows rely on pan-ERK1/2 inhibitors (PD98059, U0126) or phospho-ERK
  readouts, not ERK1-specific perturbation [file:human/MAPK3/MAPK3-deep-research-falcon.md
  "pan-ERK inhibition or total ERK output should not be reannotated as MAPK3-specific"].
  These are kept as non-core or marked as over-annotated.
- IEA transfers from mouse Erk1 (Q63844 / ENSMUSP00000051619): mouse Erk1-null data
  underlie myelination/Schwann cell, pain, synaptic transmission, cholesterol efflux; kept
  as non-core (consistent with mouse Mapk3 review).
- PMID:11096076 (QRS-ASK1, glutamine deprivation) abstract does not mention ERK; IDA rows
  for amino acid starvation set UNDECIDED; stress-activated MAPK cascade is a JNK/p38 term
  and marked over-annotated.
- PMID:24854121 is a BBB permeability paper; it supports EGFR-ERK1/2 signaling but the
  abstract does not discuss neuroinflammation -> positive regulation of neuroinflammatory
  response IDA set UNDECIDED.
- PMID:21531765 RNAi telomerase screen highlights ERK8 (MAPK15) in abstract; MAPK3 row kept
  as over-annotation (full text not available).
- PMID:19593445 (BAD / prostate cancer): documented batch miscitation for GO:0071260
  (see projects/MISCITATIONS.md) -> UNDECIDED; reference relevance NONE, MISCITED.

## Protein binding (GO:0005515) policy

Replacement MF terms follow the MAPK1 review choices:
- phosphatases (DUSP1, DUSP6, PTPRR, PTPRB, PTPRJ) -> GO:0019903 protein phosphatase binding
  [file:human/MAPK3/MAPK3-uniprot.txt "Dephosphorylated by PTPRJ at Tyr-204."]
- kinases (MAPK14, DAPK1) -> GO:0019901 protein kinase binding
- MAP2K1 -> GO:0031434 mitogen-activated protein kinase kinase binding
- transcription factors (ELK1, HSF1, KLF4, ZNF263) -> GO:0140297
- scaffolds (PEA15, SCRIB) -> GO:0097110 scaffold protein binding
- substrates/high-throughput partners without an informative MF (DHPS, TPR, RPS3, Eps8,
  Nsmf/Jacob, PKM, CDKN2AIP, PNKD, UNG, FAM135B, OTUD7B, MRFAP1L1, KLHL32, CD248, PADI3)
  -> REMOVE (removal does not mean the interaction is false).
