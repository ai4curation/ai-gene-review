# P1 (P11126) — Pseudomonas phage phi6

## Overview
- **Gene symbol**: P1
- **UniProt ID**: P11126 (`P1_BPPH6`)
- **Product**: Major inner protein P1 (769 AA, 84.9 kDa), encoded on dsRNA segment L.

## Literature & Functional Evidence
- **Inner capsid / procapsid shell framework**: P1 is the major structural subunit of the inner icosahedral capsid (polymerase complex / procapsid core), assembling as 60 asymmetric dimers (120 copies total) in a pseudo-T=2 (`T=1` of dimers) icosahedral lattice [PMID:16765897, "Asymmetric P1 dimers organize as an inner T = 1 shell, and P8 trimers organize as an outer T = 13 laevo shell. The organization of the P1 molecules in the unexpanded and expanded polymerase complex suggests that the expansion is accomplished by rigid body movements of the P1 monomers."].
- **Subunit structure and sequential RNA packaging**: Crystal structure and cryo-EM reconstruction show that P1 has a flattened trapezoidal alpha-helical fold and undergoes step-wise conformational expansion during sequential ssRNA packaging, exposing and closing segment-specific binding cavities [PMID:23891288, "ϕ6 assembles as a dodecahedral procapsid that undergoes major conformational changes as it matures into the spherical capsid. We determined the crystal structure of the capsid protein, P1, revealing a flattened trapezoid subunit with an α-helical fold."].
- **RNA binding and procapsid function**: UniProt curates that P1 forms the dodecahedral procapsid shell responsible for genomic replication and transcription and binds viral RNA during sequential packaging [file:BPPH6/P1/P1-uniprot.txt, "FUNCTION: P1 is the major inner capsid (core) protein of the polyhedral procapsid, which is responsible for genomic replication and transcription. Forms a dodecahedral shell from 60 asymmetric dimers. Binds to RNA and may be involved in genomic packaging."].

## Curation Decisions
- **ACCEPT**:
  - `GO:0003723` (`RNA binding`, IEA): Supported by positively charged s-segment binding cavities on the P1 procapsid surface (`PMID:23891288`).
  - `GO:0039616` (`T=2 icosahedral viral capsid`, IEA) and `GO:0039625` (`viral inner capsid`, IEA): Accurately describe the inner T=2 (60 asymmetric dimers) capsid shell formed by P1 (`PMID:16765897`, `PMID:23891288`).
  - `GO:0042802` (`identical protein binding`, IPI from `PMID:16765897` and `PMID:23891288`): P1 forms asymmetric homodimers that assemble into the 120-subunit inner capsid shell.
- **TOO_GENERAL**:
  - `GO:0019013` (`viral nucleocapsid`, IEA) and `GO:0019028` (`viral capsid`, IEA): True but less specific than `GO:0039625` (`viral inner capsid`) and `GO:0039616` (`T=2 icosahedral viral capsid`), which are already asserted on this gene.
