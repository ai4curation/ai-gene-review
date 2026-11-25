# rab-11.1 (C. elegans, UniProt O01803) - manual literature synthesis

No deep-research provider was run for this gene (no API keys available in the
review environment). This file is a manual synthesis written by the reviewer from
the cached publications in `publications/` and the curated UniProt record
(`rab-11.1-uniprot.txt`). Every claim carries inline provenance.

## Identity and family

- RAB-11.1 (F53G12.1, WBGene00004274) is a 211-aa Rab GTPase of the Rab11 subfamily
  [file:worm/rab-11.1/rab-11.1-uniprot.txt "Belongs to the small GTPase superfamily. Rab family."].
- C. elegans has two Rab11 subfamily members, RAB-11.1 and RAB-11.2 (W04G5.1); RNAi of
  rab-11.2 also lowers RAB-11.1 levels, so phenotypes are generally attributed to
  RAB-11.1 [PMID:24843160 "C. elegans has two RAB-11 subfamily members called RAB-11.1 and RAB-11.2"];
  [PMID:10588660 "We found a second gene (W04G5.1) homologous to rab11"].
- GTP-binding P-loop/switch residues are annotated by similarity to human RAB11A (P62491),
  and C-terminal Cys208/Cys209 are predicted geranylgeranylation sites
  (UniProt FT BINDING / LIPID, ECO:0000250).

## Nucleotide cycle and regulators

- REI-1 (and REI-2), homologs of human SH3BP5, are RAB-11 GEFs that lack a canonical
  Rab-GEF domain [PMID:26506309 "they exhibited strong GEF activity toward Rab11 in vitro"].
- REI-1 co-localizes with RAB-11 on late-Golgi membranes and is needed to target RAB-11
  to the late Golgi and recycling endosomes; loss of REI-1 reduces RAB-11 at the
  cleavage furrow and delays cytokinesis [PMID:26506309 "The loss of REI-1 specifically impaired the targeting of RAB-11 to the late-Golgi compartment and the recycling endosomes in embryos and further reduced the RAB-11 distribution to the cleavage furrow, which resulted in cytokinesis delay"].
- UniProt: "The GDP-form preferentially binds to rei-1 and rei-2" (ECO:0000269, PMID:26506309).

## Localization

- Recycling endosomes: "RAB-11 is a small GTPase enriched in recycling endosomes" [PMID:18385514].
  In the early embryo, RAB-11::GFP and anti-RAB-11 mark cytoplasmic puncta around
  centrosomes and at the periphery of the spindle, overlapping extensively with ER
  [PMID:18385514 "The GFP signal localized to cytoplasmic puncta, around centrosomes, and at the periphery of the mitotic spindle"].
  RACK-1/dynactin recruit RAB-11 recycling endosomes to the pericentrosomal region
  [PMID:19158384 "the recruitment of RAB-11-labeled recycling endosomes to the pericentrosomal region and spindle"].
  Interpretation: centrosome/spindle signals are recycling endosomes clustered near
  these structures, not centrosome or spindle components.
- Oocytes: RAB-11-positive endocytic recycling compartment holds the VAB-1 MSP/Eph
  receptor [PMID:18472420]; RAB11.1::GFP-labelled recycling endosomes reach the
  oocyte plasma membrane [PMID:23840591 "RAB11.1::GFP labeled recycling endosomes reached the plasma membrane normally in gbf-1(RNAi) oocytes compared to control oocytes"].
- Cortical granules: GFP::RAB-11 accumulates transiently on cortical granules during
  ovulation [PMID:18765566 "GFP::RAB-11 accumulates transiently on the cortical granules during ovulation, immediately prior to fertilization"].
- Late Golgi / trans-Golgi: co-localizes with REI-1 [PMID:26506309].
- Intestine: apically enriched, mostly cytosolic, recycling endosomes in the
  subapical region [PMID:24843160 "GFP::RAB-11 is still apically enriched, is primarily cytosolic, and is excluded from pathogen tissue"];
  [PMID:22634595 "Apically enriched Rab11-positive recycling endosomes (Rab11-REs) are important for establishing and maintaining epithelial polarity."].
  No study reviewed here shows RAB-11 resident in the apical plasma membrane itself.

## Processes

1. Endocytic recycling. RAB-11.1 is described as the Rab essential for endosome-to-
   plasma-membrane recycling in oocytes [PMID:23840591 "RAB-11.1, which is the Rab GTPase essential for recycling from endosomes to the plasma membrane"].
   rab-11 RNAi mildly reduces yolk uptake and mislocalizes the yolk receptor RME-2,
   consistent with defective receptor recycling rather than defective internalization
   [PMID:10588660 "The Ce-rab11 (RNAi) phenotype was consistent with a role for receptor recycling in yolk endocytosis"].
   rab-11.1 RNAi lowers meiotic maturation rate in a vab-1-dependent manner
   [PMID:18472420 "Inactivation of the endosomal recycling regulators rme-1 or rab-11.1 causes a vab-1-dependent reduction in the meiotic-maturation rate in the presence of MSP/sperm"].
2. Cortical granule exocytosis and eggshell formation. RAB-11 and the t-SNARE SYN-4
   are required for exocytosis of cortical granules that deliver chondroitin
   proteoglycans to the eggshell [PMID:18765566 "the small GTPase RAB-11 and the target-SNARE SYN-4 are required for cortical granule excoytosis after fertilization"].
3. Cytokinesis. RAB-11 depletion causes cytokinesis failure in early embryos
   [PMID:18385514 "All embryos lacking the transgene failed cytokinesis at the first division"];
   RAB-11 is delivered to the cleavage furrow in a REI-1-dependent manner [PMID:26506309].
   Part of the cytokinesis defect may be secondary to the eggshell/ECM defect
   [PMID:18765566 "producing a phenotype very similar to that observed after blockade of chondroitin synthesis"].
4. Spindle alignment / astral microtubule length in the one-cell embryo
   [PMID:18385514 "We hypothesize that RAB-11, in conjunction with the ER, acts to regulate cell cycle-specific changes in astral microtubule length"].
   Mechanism unknown; likely indirect.
5. Polarized exocytosis of microsporidian (N. parisii) spore-containing compartments
   at the intestinal apical membrane [PMID:24843160 "RAB-11 localizes to apical spores, is required for spore-containing compartments to fuse with the apical plasma membrane, and is required for spore exit"].
6. Embryonic lethality after RNAi [PMID:10588660 "all embryos produced by Ce-rab11 (RNAi) hermaphrodites died before hatching"].

## Papers named by UniProt but not cached here

PMID:21320697 (membrane repair after pore-forming toxin), PMID:22992455 (RAB-6.1/RAB-11
cortical granule exocytosis), PMID:20116245 (furrow/midbody localization),
PMID:18354496 (yolk endocytosis). These are recorded only through the UniProt
FUNCTION text and were not read directly.
