# rheb-1 (P34443, F54C8.5) manual literature research

No deep-research provider was available for this session, so this file was compiled
by hand from cached publications (`publications/PMID_*.md`), PubMed searches
("rheb-1 elegans", 9 hits) and the UniProt record. Every claim carries its source.

## Identity and family

- rheb-1 (F54C8.5, WBGene00010038) encodes a 207-aa small GTPase of the Rheb family
  [file:worm/rheb-1/rheb-1-uniprot.txt "Belongs to the small GTPase superfamily. Rheb family."].
- G-box residues (GTP binding at 25-27, 42, 45, 126, 129, 157) and the Mg2+ site are
  assigned by similarity to human RHEB (Q15382); the C-terminal CAAX box (C204-S-I-S)
  is predicted to be farnesylated and carboxymethylated, with residues 205-207 removed
  [file:worm/rheb-1/rheb-1-uniprot.txt "S-farnesyl cysteine"].
- UniProt protein existence level is 3 (inferred from homology); no biochemical
  assay of GTP binding or hydrolysis has been published for the worm protein.
- C. elegans lacks TSC1/TSC2, the canonical Rheb GAP
  [PMID:24389102 "C. elegans expresses orthologs for the Rheb and RalA/B GTPases and for RalGAPα/β, but not Tsc1/2"].

## Localization

- CRISPR-tagged endogenous mKate2::RHEB-1 is ubiquitously expressed and colocalizes
  with DAF-15/Raptor and with the lysosomal membrane marker CTNS-1::GFP in the
  hypodermis [PMID:32041790 "mK2::RHEB-1 also colocalized with CTNS-1::GFP ( Fig. 1 B,D,E), which marks the lysosomal membrane in the hypodermis"];
  [PMID:32041790 "Tagged endogenous RHEB-1 and Raptor/DAF-15 colocalize at the lysosome."].
- No published evidence places worm RHEB-1 at the plasma membrane. The UniProt
  "Cell membrane" location is ECO:0000305 (curator inference).

## RHEB-1 activates TORC1 in vivo (genetics)

- rheb-1 null (re242 full deletion) arrests at L3, phenocopying daf-15/Raptor and
  let-363/TOR deletion [PMID:32041790 "We observed that deletion of RHEB-1 similarly conferred L3 arrest."];
  intestinal expression of mNG::RHEB-1 substantially rescues this arrest.
- A GTP-locked rheb-1(Q71L Q72D) transgene acts as a TORC1-activating transgene and
  lets mmBCFA-deficient elo-5 animals bypass L1 arrest, while rheb-1(RNAi) reverses
  the nprl-3 suppression [PMID:23705068 "we also tested a third TORC1-activating transgene, rheb-1Q71LQ72D, and found that it also permitted 41.4% of elo-5(−) animals to grow beyond the L1 stage"];
  [PMID:23705068 "the suppression dramatically decreased when raga-1(RNAi) or rheb-1(RNAi) were applied to the elo-5(−) nprl-3(ku540) double mutant"].
  Q71/Q72 of P34443 lie in the DTAGQQ switch II motif (residues 67-72), the position
  of the catalytic glutamine (Q64 in human RHEB).
- RHEB-1 is required for intermittent-fasting longevity; its inhibition mimics
  caloric restriction [PMID:19079239 "RHEB-1 is required for the IF-induced longevity, whereas inhibition of RHEB-1 mimics the caloric-restriction effects"] (abstract only).
- Transient-hypoxia longevity needs intestinal RHEB-1/TOR
  [PMID:25284791 "The Ras-related small G-protein RHEB-1 is an upstream activator of TORC1 signaling"].
- The Dbl-family GEF homolog CGEF-1 binds RHEB-1 (split-ubiquitin Y2H and co-IP in
  HEK293T) and acts in the same longevity pathway; cgef-1 loss reduces 4E-BP
  phosphorylation [PMID:29515755 "elegans RHEB-1 and CGEF-1 physically interact"].
- RHEB-1 loss induces the mitochondrial UPR reporter phenotype (DVE-1 nuclear
  redistribution) in a genome-wide RNAi screen [PMID:17925224, via UniProt DISRUPTION PHENOTYPE];
  this is an indirect phenotype.
- Reviews: Rheb-TORC1 in worm development, metabolism and aging [PMID:31594908];
  RHEB-1 regulation by GDI-1/ATX-2 [PMID:27854154] (both abstract-only here).
- Preprint: worm proteomics found GATOR1 (NPRL-2/3) as RHEB-1 interactor, validated
  for nucleotide-free human Rheb [PMID:41509360] (not cached; preprint).

## Synthesis

RHEB-1 is the single C. elegans Rheb: a farnesylated small GTPase that sits on
lysosomal membranes with TORC1 and, in its GTP-bound state, is the essential
activator of TORC1. Organismal phenotypes (L3 arrest, lifespan, dietary-restriction
and hypoxia responses, L1 growth control by sphingolipids) are downstream
consequences of TORC1 activation, not separate activities of RHEB-1.
