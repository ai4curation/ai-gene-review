# SRP68 (Q9UHB9) review notes

## Identity / overview
SRP68 is the 68 kDa subunit of the signal recognition particle (SRP), a cytosolic ribonucleoprotein
(7SL RNA + 6 proteins: SRP9, SRP14, SRP19, SRP54, SRP68, SRP72). SRP68 and SRP72 form the
heterodimeric "S-domain" component that binds the large/S-domain of 7SL RNA and remodels the RNA
into the conformation required for SRP function and for SRP receptor docking.

- UniProt FUNCTION: "Component of the signal recognition particle (SRP) complex, a ribonucleoprotein
  complex that mediates the cotranslational targeting of secretory and membrane proteins to the
  endoplasmic reticulum (ER)" [file:human/SRP68/SRP68-uniprot.txt].
- SUBUNIT: "Heterodimer with SRP72"; "Within the SRP complex, interacts (via C-terminus) with SRP72
  (via N-terminus)" [file:human/SRP68/SRP68-uniprot.txt].
- DOMAIN: "The N-terminus is required for RNA-binding." Region 52-252 = RNA-binding; region 588-610 =
  required for interaction with SRP72 [file:human/SRP68/SRP68-uniprot.txt].

## Key functional evidence
- RNA remodeling / 7SL (7S) RNA binding: PMID:24700861 "SRP RNA remodeling by SRP68 explains its role
  in protein translocation" (crystal structure of SRP68-RBD with SRP19 + 7SL RNA). IMP for 7S RNA
  binding from PMID:27899666.
- SRP68-SRP72 heterodimer and ribosome interaction: PMID:27899666, PMID:28369529 (X-ray structures).
- Cryo-EM of SRP-RNC-SR: PMID:34020957 "Receptor compaction and GTPase rearrangement drive SRP-mediated
  cotranslational protein translocation into the ER" (FUNCTION evidence; not in local cache).
- Nucleolar pool: PMID:10618370 "Signal recognition particle components in the nucleolus" — SRP proteins
  including SRP68 traffic through the nucleolus during SRP assembly. UniProt records nucleolus + cytoplasm.
- ER association: PMID:28369529 (SUBCELLULAR LOCATION: Endoplasmic reticulum). MUTAGEN F590L "Diminished
  localization to endoplasmic reticulum" reflects SRP72-dependent ER targeting.

## Annotation review decisions
- Core MF: SRP/7SL (7S) RNA binding (GO:0008312) + signal recognition particle binding (GO:0005047).
  Core CC: signal recognition particle, ER targeting (GO:0005786) / SRP (GO:0048500).
  Core BP: SRP-dependent cotranslational protein targeting to membrane (GO:0006614) and the
  signal-sequence-recognition child (GO:0006617).
- GO:0030942 "endoplasmic reticulum signal sequence receptor activity" (IEA/InterPro): the SRP receptor
  (signal-sequence-receptor) activity is a property of the SRP receptor (SRPR/SRPRB), not of SRP68 itself,
  which is a 7SL-RNA-binding scaffold subunit. The InterPro mapping over-extends. MARK_AS_OVER_ANNOTATED.
  (Some sources also use SSR for the TRAP complex; not SRP68.)
- GO:0009410 "response to xenobiotic stimulus" (IDA, PMID:18089836): SRP68/SRP72 were pulled out as
  binding targets of the anticancer drug TAS-103 on drug-immobilized affinity beads; this is an
  affinity-capture observation, peripheral to SRP68's core SRP function. KEEP_AS_NON_CORE.
- GO:0005730 nucleolus: real (PMID:10618370) but reflects SRP assembly trafficking, not the core ER
  targeting site of action. KEEP_AS_NON_CORE.
- protein binding (GO:0005515) IPI rows: many are SRP72 (O76094) or SRP19 (P09132) captures — i.e. the
  informative interactions are already captured by GO:0005047/GO:0019904; CFTR (P13569) captures are from
  CFTR-interactome screens. Bare protein binding kept as KEEP_AS_NON_CORE per guidelines.
- GO:0043022 ribosome binding (contributes_to, IMP PMID:27899666): SRP68/72 contribute to SRP-ribosome
  interaction; supported. KEEP as supporting (not the single core MF but valid).

## Disease
Biallelic SRP68 variants -> severe congenital neutropenia (SCN10) [PMID:32273475]. Not a GO BP per se.
</content>
