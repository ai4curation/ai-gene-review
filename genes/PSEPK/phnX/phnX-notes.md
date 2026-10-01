# phnX curation notes

- Q88KT1 is a reviewed PhnX-family phosphonoacetaldehyde hydrolase with EC
  3.11.1.1 and RHEA:18905. The assigned reaction is phosphonoacetaldehyde plus
  water to acetaldehyde plus phosphate [UniProtKB:Q88KT1,
  "Reaction=phosphonoacetaldehyde + H2O = acetaldehyde + phosphate + H(+);"]
- The specific family evidence is concordant across HAMAP MF_01375, InterPro
  IPR006323, NCBIfam TIGR01422, and PANTHER PTHR43434:SF19
  [UniProtKB:Q88KT1, "DR   InterPro; IPR006323; Phosphonoacetald_hydro."].
- The TreeGrafter phosphoglycolate-phosphatase and DNA-repair annotations are
  inconsistent with the exact PhnX subfamily and reaction and are removed.
- Direct 2-aminoethylphosphonate:pyruvate aminotransferase and phosphonatase
  activities were measured in *P. putida* NG2 and were induced by substrate
  independently of phosphate status [PMID:9841125,
  "phosphonoacetaldehyde hydrolase (phosphonatase) activities which were inducible"].
  No direct biochemical assay of Q88KT1 from KT2440 was found, so its assignment
  remains a strong family- and pathway-context inference rather than
  strain-specific experimental evidence.

## 2026-07-19 first-pass evidence

Q88KT1 is assigned to the substrate-specific PhnX family and to
phosphonoacetaldehyde hydrolysis by the UniProt record
[file:PSEPK/phnX/phnX-uniprot.txt "Belongs to the HAD-like hydrolase
superfamily. PhnX family."].

The species-aware pathway report independently identifies PP_2208/Q88KT1 as
the single-copy PhnX step in the adjacent phnWX route and notes that the
assignment is grounded by the PhnX-specific signature rather than only the
broad HAD fold
[file:projects/P_PUTIDA/deep-research/PSEPK__phosphonoacetaldehyde_degradation__ppu00440-deep-research-openscientist.md
"Substrate-specific signature: **IPR006323 (PhnX family)** — a
phosphonatase-specific TIGRFAM, not merely the broad HAD fold."].

No direct biochemical characterization of KT2440 Q88KT1 was identified; the
report explicitly treats the assignment as homology-based and transfers
species-level support from other P. putida strains
[file:projects/P_PUTIDA/deep-research/PSEPK__phosphonoacetaldehyde_degradation__ppu00440-deep-research-openscientist.md
"Direct biochemical evidence for KT2440 itself does not exist in the
literature"].

## 2026-08-12 primary-literature follow-up

P. putida NG2 contains inducible 2-aminoethylphosphonate:pyruvate
aminotransferase and phosphonoacetaldehyde hydrolase activities, directly
supporting the two-reaction pathway at species level while not assaying KT2440
[PMID:9841125 "source contained 2-aminoethylphosphonic acid: pyruvate aminotransferase and phosphonoacetaldehyde hydrolase (phosphonatase) activities"].

P. putida BIRD-1 genetics identifies PhnWX as its AEP
transaminase-phosphonatase system and shows that the route is regulated by AepR
and global nutrient-response regulators [PMID:35229442 "Mutation of a LysR-type
regulator, termed AepR, upstream of the 2AEP transaminase-phosphonatase system
(PhnWX), confirmed this dual regulatory mechanism."].

The Bacillus cereus family exemplar provides direct structural evidence for
magnesium-dependent phosphonoacetaldehyde hydrolysis and the HAD-family
mechanism [PMID:10956028 "Phosphonoacetaldehyde hydrolase (phosphonatase)
catalyzes the hydrolysis of phosphonoacetaldehyde to acetaldehyde and phosphate
using Mg(II) as cofactor."].
