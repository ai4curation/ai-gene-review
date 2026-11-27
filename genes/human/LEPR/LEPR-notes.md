# LEPR (P48357) — curation notes

Deep research: the client failed in this session (`just deep-research-falcon human LEPR` timed out
after 600 s with "agentapi not found in PATH"), so the literature work below was done manually
from PubMed and the cached `publications/` entries. The provider finished afterwards and
`LEPR-deep-research-falcon.md` is committed; it was checked against this review on 2026-10-11.

- It agrees on the core annotation: a class-I cytokine receptor for leptin with no intrinsic
  kinase activity, the long LEPRb isoform being the signalling-competent form, activating
  receptor-associated JAK2 through Box1/Box2, with Tyr1138-STAT3 the dominant route (and the
  inducer of SOCS3 feedback), Tyr985 giving SOCS3 recruitment and SHP2-GRB2-ERK, and Tyr1077-STAT5
  biochemically real but much less consequential for energy balance.
- It supports the blood-brain-barrier call as now restated in the review. The short isoform ObRa
  has long been proposed as the shuttle, and that is the claim the direct experiments refute:
  endothelial ObR is not the primary leptin transporter at the human BBB [PMID:27037668], and the
  LEPRa-LRP1 transcytosis model rests on a 2023 preprint using mouse and rat cells, not human
  in vivo data.
- It adds the Saxton 2023 cryo-EM activation mechanism: leptin binds CRH2 at a higher-affinity
  interface and the Ig-like region at a lower-affinity one, giving an asymmetric assembly in which
  one leptin bridges two receptor chains. The purified structural complex used mouse proteins;
  signalling was tested separately with human leptin and full-length human LEPR.
- It notes SEL1L-HRD1 ER-associated degradation controls LEPRb maturation and surface delivery,
  with the obesity-associated human C604S receptor folding-defective. The ER is a biogenesis and
  quality-control compartment, not a signalling site, which is how this review treats it.

## Identity and architecture

- LEPR (OB-R, LEP-R, CD295) was cloned from mouse choroid plexus by expression screening with a
  leptin-alkaline phosphatase fusion; it is a single-pass receptor of the class I cytokine receptor
  family, closest to gp130
  [PMID:8548812 "OB-R is a single membrane-spanning receptor most related to the gp130
  signal-transducing component of the IL-6 receptor"], and the gene maps to the mouse *db* locus.
- Expression is not confined to choroid plexus
  [PMID:8548812 "OB-R mRNA is expressed not only in choroid plexus, but also in several other
  tissues, including hypothalamus"].
- Alternative splicing gives the long signalling isoform (LEPRb), short isoforms (OB-Ra etc.) and a
  soluble isoform E that antagonises ligand binding and endocytosis
  [file:human/LEPR/LEPR-uniprot.txt "Antagonizes Isoform A and isoform B-mediated LEP"].
- The signalling-competent isoform is scarce relative to the inactive short isoforms, which is part
  of why the activation mechanism was contested
  [PMID:36959263 "the signaling-competent isoform of LEP-R is only lowly abundant amid several
  inactive short LEP-R isoforms"].

## Ligand binding and receptor assembly

- The leptin-binding domain (CRH2) structure was solved in complex with the blocking Fab 9F8
  [PMID:22405007 "We have crystallized the Fab fragment of a leptin-blocking monoclonal antibody
  (9F8), both in its uncomplexed state and bound to the leptin-binding domain (LBD) of human ObR"].
- Crystallography, cryo-EM and single-molecule imaging show leptin-induced higher-order assemblies
  rather than simple 2:2 dimers
  [PMID:36959263 "Leptin induces type I cytokine receptor assemblies featuring 3:3 stoichiometry"],
  and obesity-linked mutations abolish the site III contact that drives them.

## Signalling

- LEPRb signals through JAK2/STAT3 with additional MAPK/FOS arms
  [file:human/LEPR/LEPR-uniprot.txt "the activation of different signaling pathways such as
  JAK2/STAT3 and"], as expected for a class I cytokine receptor
  [PMID:18042720 "OB-R belongs to the class I cytokine receptor family, which typically uses the
  JAK/STAT signaling pathwa"].
- The STAT3 arm specifically carries the energy-balance and melanocortin outputs
  [file:human/LEPR/LEPR-uniprot.txt "Control of energy homeostasis and melanocortin"], i.e. POMC
  induction and AgRP repression — the step that places LEPR upstream of PCSK1/POMC/MC4R.
- LEPROT/OB-RGRP negatively regulates surface receptor levels
  [PMID:18042720 "We provide in vitro evidence that OB-RGRP controls OB-R function by negatively
  regulating its cell surface expression"]; this is a function of LEPROT, not of LEPR, so the
  corresponding `protein binding` row was removed rather than retermed.

## Human genetics

- A homozygous splice mutation producing a receptor without transmembrane and intracellular domains
  caused morbid obesity with absent puberty and reduced GH/TSH secretion
  [PMID:9537324 "results in a truncated leptin receptor lacking both the transmembrane and the
  intracellular domains"].
- Systematic sequencing of 300 severely obese children found pathogenic LEPR mutations in 3%
  [PMID:17229951 "All missense mutations resulted in impaired receptor signaling";
  PMID:17229951 "Affected subjects were characterized by hyperphagia, severe obesity, alterations in
  immune function, and delayed puberty due to hypogonadotropic hypogonadism"].
- POMC-neuron-restricted receptor deletion in mice gives mild obesity and altered hypothalamic
  neuropeptide expression, so POMC neurons carry part but not all of the signal
  [PMID:15207242 "Mice lacking leptin signaling in POMC neurons are mildly obese, hyperleptinemic,
  and have altered expression of hypothalamic neuropeptides"].

## Annotations that needed downgrading

- **Blood-brain barrier transport (GO:0150104, two NAS review citations).** Marked over-annotated.
  Direct testing in a human BBB model found leptin translocation unaffected by blocking the
  leptin-receptor interface [PMID:27037668 "it was not inhibited by pre-treatment with 9F8"], and
  OB-Ra overexpression did not increase permeation whereas OB-Rb did
  [PMID:20977476 "ObRb over-expression in C6 cells increased leptin permeation whereas ObRa
  over-expression showed no effect"]. The widely repeated short-isoform-as-transporter claim is
  therefore not securely attributable to LEPR.
- **`protein binding` rows.** Four were removed as uninformative (SNX6 trafficking, a high-throughput
  SH3 peptide array hit for GRB2, LEPROT, and downstream SRC/integrin association); three whose
  partner is leptin itself (P41159) were retermed to leptin receptor activity.
- **GO:0043235 signaling receptor complex (IDA, PMID:23382219).** The cached full text of that
  PX-FERM sorting-nexin paper does not mention the leptin receptor, so the specific supporting
  experiment cannot be re-checked here. Per repo policy the curator's experimental call is accepted
  (the location is independently correct from the assembly structures) rather than removed.
- Peripheral outputs (angiogenesis, T-cell differentiation and autophagy, bone remodelling and
  growth, glucose homeostasis, cold-induced thermogenesis, reproduction, inflammatory cytokine
  production, soluble/basolateral localisations) were kept as non-core: real, but downstream of or
  peripheral to the receptor's energy-balance role
  [PMID:28270795 "this adipocyte-derived hormone also directs peripheral processes, including
  immunity, reproduction, and bone metabolism"].
- ARBA-generated `system development` and `animal gross anatomical part developmental process`, and
  the TAS `multicellular organism development`, were removed as uninformative; the developmental
  phenotypes of receptor deficiency are endocrine consequences.

## Alignment with dismech

dismech `Congenital_Leptin_Deficiency` and `Obesity_Due_to_MC4R_Pathway_Disruption` model the
dysfunction side. The normal functions asserted here — leptin receptor activity (GO:0038021) at the
plasma membrane, the leptin-mediated signalling pathway (GO:0033210) via STAT (GO:0097696), and
regulation of feeding behaviour / energy homeostasis in the arcuate nucleus — are the functions those
entries mark as lost or reduced.
