# SE / SERRATE (At2g27100, Q9ZVD0) curation notes

## Deep research status

`just deep-research ARATH SE` failed on 2026-10-20. Falcon gave "Failed to
authenticate", perplexity is not configured, and openai returned
`invalid_api_key`. No deep-research file was written. These notes come from my
own reading of the cached publications and the UniProt record (`SE-uniprot.txt`).

## Identity

- UniProtKB Q9ZVD0 (SRRT_ARATH), gene SE, locus At2g27100, "Serrate RNA effector
  molecule". It belongs to the ARS2 family (PF04959; IPR039727 SE/Ars2; N- and
  C-terminal SE/Ars2 domains; a single C2H2 zinc finger).
- The folder is named `SE` to match the UniProt primary gene name (cf. `DRB1` for HYL1).
- Null alleles are embryo lethal; se-1, se-2 and se-3 are weak alleles (UniProt).

## Microprocessor scaffold in miRNA biogenesis (core)

- se is a general miRNA biogenesis mutant
  [PMID:16977334 "We show that SE is a general regulator of miRNA levels affecting the processing of primary miRNA to miRNA."]
  [PMID:16889646 "We further demonstrate that SE is localized in the nucleus and interacts physically with HYL1."]
- In vitro, SE and HYL1 increase the rate and accuracy of DCL1 cleavage
  [PMID:18632569 "We show that recombinant HYL1 and SE proteins accelerate the rate of DCL1-mediated cleavage of pre- and pri-miR167b substrates and promote accurate processing."].
  SE does not itself carry nuclease activity; DCL1 is the RNase III.
- DCL1, HYL1 and SE interact in nuclear dicing bodies (BiFC). SE is mostly in nuclear
  speckles and is only transiently in D-bodies
  [PMID:17442570 "SE predominantly localizes to nuclear speckles"].
- SE is the phase-separating scaffold of D-bodies
  [PMID:33288888 "SE forms droplets and drives DCL1, HYL1 and pri/pre-miRNAs into the droplets in vitro, and mutation of SE abrogates the formation of D-bodies in vivo, which indicates that D-bodies arise through SE-mediated phase separation."]
  (abstract only).
- It is a scaffold for regulators of the microprocessor:
  - CPL1 phosphatase recruitment to HYL1
    [PMID:23141542 "In the miRNA processing complex, SE functions as a scaffold to mediate CPL1 interaction with HYL1, which needs to be dephosphorylated for optimal activity."]
  - CHR2/BRM docks on SE to remodel pri-miRNAs and inhibit their processing (PMID:29769717).
  - SE recruits the NEXT complex (HEN2, RBM7, ZCCHC8A/B) to send pri-miRNAs to the
    nuclear exosome (PMID:32449937).
  - It also associates with splicing-related factors: HOS5/RCF3, RS40 and RS41 in speckles
    (PMID:26227967), SMA1 (PMID:29982637) and SEAP1 (PMID:34449907).

## Splicing and the cap-binding complex

- SE binds CBP20 and CBP80 (PMID:24137006). se, cbp20 and cbp80 mutants share
  intron-retention defects (PMID:18550839) and alternative-splicing changes
  (PMID:24137006). The relationship parallels CBC-ARS2 in animals. This is a
  real but secondary role.

## Developmental phenotypes (downstream)

- Leaf serration, phase change, phyllotaxy (PMID:10607301), meristem function and
  adaxial/abaxial patterning via miR165/166-PHB (PMID:16222298). These are
  consequences of defective miRNA biogenesis.

## Legacy annotations of SE as a transcription factor

- The original cloning paper speculated that SE might regulate transcription because
  of its zinc finger. It also noted that a single zinc finger is unlikely to bind DNA
  with high sequence specificity
  [PMID:11402159 "The putative zinc-finger and nuclear localization motifs suggest that the SE protein regulates transcription, possibly by altering chromatin structure."].
- GOA still carries "DNA binding" (ISS, PMID:11402159), "DNA-binding transcription
  factor activity" (ISS, PMID:11118137) and "regulation of DNA-templated
  transcription" (TAS, PMID:11402159). None of these has direct support.
  PMID:11118137 is a genome-wide transcription-factor census (Riechmann et al. 2000)
  that does not discuss SE individually. An ISS row with no with/from entity that
  cites a census paper looks like a legacy family-classification attachment, not a
  gene-specific inference. The two MF rows are REMOVE and the TAS BP row is
  MARK_AS_OVER_ANNOTATED.
- Nucleolus (HDA, PMID:15496452): I found no At2g27100/SERRATE mention in the cached
  full text, which probably lacks the supplementary protein list. I could not verify
  it, so the row is UNDECIDED.

## Molecular condensate scaffold (NEW row)

- Added a NEW `enables` row for molecular condensate scaffold activity (GO:0140693),
  IDA from PMID:33288888 (abstract only). SE itself forms the droplets and draws DCL1,
  HYL1 and pri/pre-miRNAs into them, so SE performs the activity. This is the MF
  behind the existing dicing-body and miRNA-processing annotations.
- The IBA nuclear body row (PTN000323018) is a refinement (MODIFY to nuclear dicing
  body and nuclear speck), not a propagation failure.
