# cysNC curation notes

## First-pass synthesis

- Q88NA8 is the CysN-family GTPase subunit that partners with CysD for APS
  formation [UniProtKB:Q88NA8, "With CysD forms the ATP sulfurylase (ATPS) that
  catalyzes the adenylation of sulfate"].
- The conserved mechanism couples CysN GTP turnover to sulfate adenylation
  [PMID:16387658, "conserved switch motifs in the G domain of CysN allosterically
  mediate interactions between the nucleotide binding sites"].
- The imported `enables GO:0004781` relation is too strong for the regulatory
  GTPase subunit. CysNC contributes to the CysD-catalyzed ATP sulfurylase
  activity; its own catalytic activity is GTP hydrolysis.
- Q88NA8 contains an APS-kinase-like C-terminal domain, but the exact record
  does not assign an APS kinase reaction. The first pass therefore does not add
  a PAPS-producing pathway step.

## Open issue

Test whether the C-terminal domain is active or is a catalytically eroded fusion
remnant. This distinction determines whether KT2440 can generate PAPS through
CysNC even though its CysH is assigned as an APS reductase.
