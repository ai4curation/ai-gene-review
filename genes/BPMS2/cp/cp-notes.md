# BPMS2 cp (Capsid protein / P03612) Notes

## Overview
- **Gene symbol**: `cp`
- **UniProt ID**: `P03612` (`CAPSD_BPMS2`)
- **Organism**: Escherichia phage MS2 (`NCBITaxon:12022`)
- **Protein**: Capsid protein (coat protein, CP), 130 amino acids (mature chain 2-130 after initiator methionine removal).

## Biological Function & Architecture
- **Capsid assembly**: Self-assembles into homodimers (`GO:0042802`) that adopt either symmetric (C/C) or asymmetric (A/B) conformations to form a T=3 quasi-icosahedral viral capsid (`GO:0039617`) containing 89 coat protein dimers (178 subunits) and 1 copy of the maturation protein `A` ([PMID:8254664]; [PMID:23810697]; [file:BPMS2/cp/cp-uniprot.txt]).
- **Genomic RNA packaging and allosteric conformer switching**: Binds the 19-nucleotide translational operator (TR) stem-loop and multiple dispersed packaging signals along the MS2 ssRNA genome (`GO:0003723`). Binding of stem-loops allosterically switches coat protein dimers from the symmetric C/C conformer to the asymmetric A/B conformer, driving two-stage genome condensation and efficient T=3 shell assembly ([PMID:7523953]; [PMID:23019360]).
- **Translational repression of replicase**: High-affinity binding of a coat protein dimer to the 19-nt TR hairpin encompassing the `rep` initiation codon represses translation of the viral RNA-directed RNA polymerase late in infection (`GO:1904972`) ([PMID:4903176]; [PMID:7523953]).

## Curation Decisions
- **ACCEPT**:
  - `GO:0003723` (`RNA binding`, IDA from PMID:7523953 and IEA from GO_REF:0000043): Directly demonstrated by crystal structure of the MS2 coat protein dimer bound to the 19-nt TR RNA operator hairpin.
  - `GO:0039617` (`T=3 icosahedral viral capsid`, IDA from PMID:8254664 and IEA from GO_REF:0000043): Directly supported by the 2.8 Å crystal structure of the MS2 T=3 capsid.
  - `GO:0042802` (`identical protein binding`, IPI from PMID:23019360 and PMID:23810697): Coat protein subunits form stable homodimers (A/B and C/C) and higher-order inter-dimer contacts required for capsid assembly.
  - `GO:1904972` (`negative regulation of viral translation`, IDA from PMID:4903176): Classic in vitro and in vivo demonstration that MS2 coat protein represses translation of the viral replicase cistron by binding the operator stem-loop covering its ribosome-binding site.
- **MODIFY**:
  - `GO:0005198` (`structural molecule activity`, IEA from GO_REF:0000002) -> `GO:0039660` (`structural constituent of virion`).
  - `GO:0019028` (`viral capsid`, IEA from GO_REF:0000120) -> `GO:0039617` (`T=3 icosahedral viral capsid`), already present on this gene.
