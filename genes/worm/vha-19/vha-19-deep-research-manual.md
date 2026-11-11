# vha-19 (Q9TYW1, Y55H10A.1) - manual literature research

No deep-research provider was available for this review; this file records a manual
literature survey (PubMed search "vha-19 elegans", cached full text, and orthology
context from the human ATP6AP1 review).

## Identity and family

- vha-19 encodes a 451-aa type I membrane glycoprotein, the C. elegans member of the
  vacuolar ATPase subunit S1 (Ac45/ATP6AP1) family [file:worm/vha-19/vha-19-uniprot.txt
  "Belongs to the vacuolar ATPase subunit S1 family."]. InterPro IPR008388 (Ac45_acc_su)
  and Pfam PF20520 (Ac45-VOA1_TM); PANTHER PTHR12471:SF7.
- Predicted N-terminal signal peptide (1-16), a single C-terminal TM helix (408-428), a
  large lumenal domain with four predicted N-glycosylation sites, and a short cytoplasmic
  tail. Knight et al. also predicted a furin site at 159/160 [PMID:22768351 "the ProP 1.0
  server [13] predicts that there is an N-terminal signal cleavage site between amino acids
  16 and 17 in VHA-19 and that it is cleaved by furin between amino acids 159 and 160"].
- Sequence identity to mammalian Ac45 is low (<30% over 150 aa), which is why the gene
  was originally selected as "nematode-specific" [PMID:22768351 "it had less than 30%
  sequence identity over 150 amino acids to any mammalian proteins"]. Association with
  the worm V-ATPase has not been tested experimentally [PMID:22768351 "However, any
  association between VHA-19 and the C. elegans V-ATPase is yet to be shown
  experimentally."].

## Mammalian ortholog context (ATP6AP1/Ac45, Q15904)

- Ac45 is a V0-associated accessory subunit and assembly hub of the V-ATPase
  [PMID:33065002 "ATP6AP1 as a structural hub for Vo complex assembly"]; processed Ac45
  can replace yeast Voa1 [PMID:27231034 "Processed wild-type Ac45, but not its disease
  mutants, restored V-ATPase-dependent growth in Voa1 mutant yeast."]. Loss in humans
  causes a congenital disorder of glycosylation (ATP6AP1-CDG).

## C. elegans functional data

### Knight, Johnson & Behm 2012 (PMID:22768351, full text)

- vha-19(tm2205) deletion mutants are inviable; RNAi from L1 causes L3/L4 arrest
  [PMID:22768351 "C. elegans fed vha-19 dsRNA from the L1 stage arrested and died as
  larvae by the L3/L4 stage"].
- RNAi from L4: adults normal but embryos fail; germline-specific requirement shown with
  rrf-1, and fog-2 mating experiments show the requirement is maternal (oocyte) not
  sperm [PMID:22768351 "Thus, VHA-19 was required in the oocytes rather than the sperm"].
- Oocytes: fewer oocytes, endomitotic oocytes, failure of VIT-2::GFP uptake, and
  RME-2::GFP retained in perinuclear, Golgi-like aggregates instead of reaching the plasma
  membrane [PMID:22768351 "the majority of RME-2::GFP aggregated around the nucleus of
  vha-19(RNAi) oocytes and did not reach the plasma membrane"].
- Embryos: osmotically sensitive, swell to fill the eggshell, some permeable to dyes,
  signs of cytokinesis failure; authors attribute this to a defective eggshell via a
  possible trafficking/secretion (cortical granule) role [PMID:22768351 "vha-19(RNAi)
  embryos were osmotically sensitive in hypertonic and hypotonic media"].
- Expression: vha-19p::GFP in excretory cell, intestine, hypodermis, pharynx, vulval
  hypodermis of larvae and adults; germline expression not seen with the transgene but
  supported by other mRNA data.
- The authors note the phenotypes resemble, but are milder than, those of core V-ATPase
  subunit knockdowns [PMID:22768351 "these phenotypes were also observed when expression
  of known subunits of the V-ATPase were silenced [41], although the onset of the
  phenotypes was earlier and more severe when individual V-ATPase genes were silenced"].

### Kanaki et al. 2019 (PMID:30445613, abstract only)

- In an RNAi screen of germline-expressed N-glycosylated proteins, vha-19 RNAi phenocopied
  loss of the N-glycosylation initiating enzyme algn-7 (endomitotic oocytes, permeable
  eggs), and vha-19 is noted as the ortholog of a CDG gene [PMID:30445613 "They were
  ribo-1, stt-3, ptc-1, ptc-2, and vha-19."].

### Zawadzki et al. 2012 (PMID:22348596, not cached)

- Hc-vha-19 RNAi by feeding affected development/viability of Haemonchus contortus larvae;
  relevant only as a parasite drug-target context.

### Rao et al. 2011 (PMID:21070894, abstract only)

- C. elegans lipid raft proteome (44 proteins by geLC-MS/MS); source of the HDA membrane
  raft annotation.
