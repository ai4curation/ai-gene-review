# CAST review notes

## Literature synthesis

Human CAST / calpastatin is the specific endogenous inhibitor of calcium-activated
calpain cysteine proteases. UniProt summarizes the core function as "Specific
inhibition of calpain", and domain evidence explains the repeated architecture:
each flexible inhibitory domain can block a calcium-bound calpain active-site
cleft.

PAINT places both `GO:0010859` calcium-dependent cysteine-type endopeptidase
inhibitor activity and `GO:0005737` cytoplasm on `PTHR10077` node
`PTN002560636`, with human CAST as a seed for both rows and rat Cast as an
additional seed for the activity row. The human deletion study
[PMID:2407243] expressed fragments from human calpastatin cDNA and localized
the essential inhibitory sequence within domain 1, while Reactome summarizes
the same direct mechanism as CAST binding to calcium-bound calpain complexes.

Several GOA rows are contextual. The organelle-fractionation paper
[PMID:14559243] reports stimulated association of calpain-network proteins,
including calpastatin, with ER/Golgi fractions. The rat Cav1.2 study
[PMID:24462690] shows a calcium-dependent binding assay for the CAST domain L
against channel-tail peptides, but this xeno interactor row remains a bare
`GO:0005515` protein-binding annotation. The E-cadherin [PMID:25468996] and
mRNA-interactome [PMID:22658674] papers are discovery proteomics screens and
do not establish cadherin binding or RNA binding as evolved calpastatin
functions.

## Source checks

- The `PMID:27626661` presynaptic active-zone row is a symbol collision. That
  paper's CAST is an active-zone cytomatrix protein in the ELKS/ERC family, not
  calpastatin.
- The BHF-UCL `PMID:15044459` beta-cell apoptosis row is unresolved from the
  abstract-only cache: the abstract names calpain-10 as the protease but does
  not expose whether calpastatin was assayed in the full text.
- The HPA ER, cytosol and plasma-membrane rows are direct immunofluorescence
  annotations. They are compatible with a soluble calpain inhibitor that can
  associate peripherally with organelle and membrane compartments, but they do
  not change the core cytoplasmic calpain-inhibitor call.
