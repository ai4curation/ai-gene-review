# BPQBE cp (Capsid protein / P03615) Notes

## Overview
- **Gene symbol**: `cp`
- **UniProt ID**: `P03615` (`CAPSD_BPQBE`)
- **Organism**: Qubevirus durum / Escherichia virus Qbeta (`NCBITaxon:39803`)
- **Protein**: Major capsid protein (coat protein, CP), 133 amino acids (mature chain 2-133).

## Biological Function & Architecture
- **T=3 icosahedral capsid and internalized dimer**: Forms homodimers stabilized by inter-subunit disulfide bonds and assembles into a T=3 quasi-icosahedral capsid (`GO:0039617`) around the 4,217-nt ssRNA genome ([PMID:19913556]; [PMID:27671640]). Asymmetric cryo-EM reconstructions revealed that in addition to the coat protein dimers forming the outer T=3 shell (together with 1 copy of `A2` and 3-10 readthrough copies of `A1`), one extra `cp` dimer is sequestered inside the virion where it binds a 5-way RNA junction hairpin and the buried alpha-region of `A2` ([PMID:27671640]; [PMID:29078304]; [file:BPQBE/cp/cp-uniprot.txt]).
- **Operator RNA binding and translational repression**: A `cp` homodimer binds via its large beta-sheet surface (`GO:0003723`) to the Qbeta translational operator stem-loop (an 8-bp stem with a 3-nt loop encompassing the `rep` start codon), acting as a translational repressor (`GO:0030371`) of viral replicase synthesis late in infection and discriminating against non-cognate phage operators ([PMID:8943226]; [PMID:16531233]).

## Curation Decisions
- **ACCEPT**:
  - `GO:0003723` (`RNA binding`, IDA from PMID:16531233, IEA from GO_REF:0000043, and IMP from PMID:8943226): Supported by mutational mapping of the beta-sheet RNA-binding site ([PMID:8943226]), structural analysis of operator discrimination ([PMID:16531233]), and cryo-EM visualization of 59 operator-like RNA hairpins contacting CP dimers in situ ([PMID:27671640]).
  - `GO:0030371` (`translation repressor activity`, IMP from PMID:8943226): Supported by in vivo translational repression assays of the replicase operator in [PMID:8943226] and [PMID:16531233].
  - `GO:0039617` (`T=3 icosahedral viral capsid`, IDA from PMID:19913556, IDA from PMID:27671640, and IEA from GO_REF:0000043): Directly demonstrated by X-ray and high-resolution cryo-EM structures of the Qbeta virion.
- **MODIFY**:
  - `GO:0005198` (`structural molecule activity`, IEA from GO_REF:0000002) -> `GO:0039660` (`structural constituent of virion`).
  - `GO:0019028` (`viral capsid`, IEA from GO_REF:0000120) -> `GO:0039617` (`T=3 icosahedral viral capsid`), already present on this gene.
