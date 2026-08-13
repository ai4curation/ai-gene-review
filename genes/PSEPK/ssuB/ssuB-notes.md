# ssuB curation notes

## Identity and ISS provenance

- Q88R93 is reviewed as the PP_0240 ATP-binding subunit of the KT2440 SsuABC
  importer [file:PSEPK/ssuB/ssuB-uniprot.txt, "Part of the ABC transporter
  complex SsuABC involved in"]. The record specifies an SsuB2-SsuC2-SsuA
  assembly [file:PSEPK/ssuB/ssuB-uniprot.txt, "The complex is composed of two
  ATP-binding proteins (SsuB)"].
- E. coli SsuB P0AAI1 is the explicit `supporting_entities` comparator on every
  ISS annotation. The conserved ABC transporter domain and ATP-binding feature
  support ATP binding/hydrolysis, while the syntenic `ssuEADCB` context supports
  alkanesulfonate specificity.
- GO:0005524 ATP binding is retained as a low-information `NEW` annotation but
  is not the core function. The informative biology is ATP hydrolysis coupled
  to contribution to GO:0042959, whose official QuickGO label includes the
  doubled word `transporter`.

## Research coverage

The completed OpenScientist report materialized at
`ssuB-deep-research-openscientist.md`. It correctly notes that direct
biochemical characterization of KT2440 SsuB itself has not been reported
[file:PSEPK/ssuB/ssuB-deep-research-openscientist.md, "Direct biochemical
characterization of the KT2440 SsuB protein itself has not been reported"].
Identifiers, motifs, complex composition, and central pathway claims were
independently checked against UniProt and cached primary literature.

## Residual uncertainty

Target-protein ATPase kinetics, stimulation by cognate SsuA/SsuC, and the exact
transported substrate range remain unmeasured.
