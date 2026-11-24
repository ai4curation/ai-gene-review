# P6 (P11128) — Pseudomonas phage phi6

## Overview
- **Gene symbol**: P6
- **UniProt ID**: P11128 (`FUS_BPPH6`)
- **Product**: Fusion protein P6 (168 AA, 17.2 kDa), encoded on dsRNA segment M.

## Literature & Functional Evidence
- **Integral virion membrane protein mediating viral-host outer membrane fusion and anchoring P3**:
  - P6 is a multi-pass integral membrane protein of the phi6 viral envelope that anchors the peripheral receptor-binding spike protein P3 and mediates fusion between the phage lipid envelope and the Gram-negative host outer membrane during viral entry [file:BPPH6/P6/P6-uniprot.txt, "FUNCTION: Mediates the fusion with the host outer membrane during virus entry into the host cell."]; [file:BPPH6/P6/P6-uniprot.txt, "SUBUNIT: Interacts with P3."]; [file:BPPH6/P6/P6-uniprot.txt, "SUBCELLULAR LOCATION: Virion membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."].

## Curation Decisions
- **ACCEPT**:
  - `GO:0098997` (`fusion of virus membrane with host outer membrane`, IEA): Specifically captures P6's role in fusing the phi6 lipid envelope with the Gram-negative host outer membrane.
  - `GO:0019031` (`viral envelope`, IEA) and `GO:0055036` (`virion membrane`, IEA): P6 is an integral multi-pass membrane protein of the phi6 virion membrane/envelope.
- **TOO_GENERAL**:
  - `GO:0039663` (`membrane fusion involved in viral entry into host cell`, IEA) and `GO:0046718` (`symbiont entry into host cell`, IEA): Subsumed by the more specific descendant term `GO:0098997` (`fusion of virus membrane with host outer membrane`).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, IC from `file:BPPH6/P6/P6-uniprot.txt`): P6 is a major integral membrane structural component of the enveloped virion that anchors the P3 spike.
