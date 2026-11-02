# BPMS2 A (Maturation protein / P03610) Notes

## Overview
- **Gene symbol**: `A`
- **UniProt ID**: `P03610` (`MAT_BPMS2`)
- **Organism**: Escherichia phage MS2 (`NCBITaxon:12022`)
- **Protein**: Maturation protein (MP, A protein), 393 amino acids.

## Biological Function & Architecture
- **Asymmetric capsid integration**: A single copy of the maturation protein (`A`) is incorporated into the MS2 virion, where it replaces one coat protein (`cp`) dimer at a 2-fold axis of the T=3 icosahedral lattice, breaking strict icosahedral symmetry ([PMID:23810697]; [file:BPMS2/A/A-uniprot.txt]).
- **Genomic RNA binding and circularization**: The N-terminal half of the maturation protein binds specific stem-loop packaging sequences near both the 5' and 3' ends of the single-stranded viral genomic RNA, circularizing the genome inside the virion and playing a central role in packaging-signal-mediated assembly and subsequent genome ejection ([PMID:26608810]; [file:BPMS2/A/A-uniprot.txt]).
- **Receptor attachment and genome delivery**: The maturation protein mediates phage adsorption to the side of the host *Escherichia coli* conjugative F-pilus (`GO:0039666`) and enters the host cell together with the genomic RNA during infection (`GO:0046718`) ([PMID:23810697]; [file:BPMS2/A/A-uniprot.txt]).

## Curation Decisions
- **ACCEPT**:
  - `GO:0003723` (`RNA binding`, IDA from PMID:26608810 and IEA from GO_REF:0000043): Directly demonstrated by X-ray footprinting and cross-linking/mass spectrometry of MS2 virion RNA-MP contacts.
  - `GO:0039666` (`virion attachment to host cell pilus`, IDA from PMID:23810697 and IEA from GO_REF:0000120): Directly visualized by cryo-electron tomography of MS2 bound to the F-pilus via its single-copy maturation protein.
  - `GO:0046718` (`symbiont entry into host cell`, IEA from GO_REF:0000043): The maturation protein is proteolytically cleaved and enters the host cell along with the genomic RNA during pilus retraction.
  - `GO:0099009` (`viral genome circularization`, IEA from GO_REF:0000043): Supported by binding of the single maturation protein to both 5'-proximal and 3'-proximal regions of the MS2 genomic ssRNA ([PMID:26608810]).
- **MODIFY**:
  - `GO:0019062` (`virion attachment to host cell`, IEA from GO_REF:0000043) -> `GO:0039666` (`virion attachment to host cell pilus`), which is already present on this gene and captures the specific F-pilus receptor attachment mechanism.
