# P3 (P11129) — Pseudomonas phage phi6

## Overview
- **Gene symbol**: P3
- **UniProt ID**: P11129 (`P3_BPPH6`)
- **Product**: Spike protein P3 (648 AA, 69.2 kDa), encoded on dsRNA segment M.

## Literature & Functional Evidence
- **Host receptor recognition (type IV pilus attachment)**: P3 forms the surface-exposed receptor-binding spikes of the enveloped phi6 virion, anchored to the viral membrane via integral membrane fusion protein P6, and attaches specifically to the host type IV pilus to initiate infection [file:BPPH6/P3/P3-uniprot.txt, "FUNCTION: P3 protein is necessary for adsorption onto host cells. Attaches to a type IV pilus of the host."]; [file:BPPH6/P3/P3-uniprot.txt, "SUBCELLULAR LOCATION: Virion membrane; Peripheral membrane protein. Note=The spike protein P3 protrudes from the membrane, where it is anchored by the integral membrane protein P6."].

## Curation Decisions
- **ACCEPT**:
  - `GO:0039666` (`virion attachment to host cell pilus`, IEA): Specifically captures P3's role in binding the Pseudomonas type IV pilus during adsorption.
  - `GO:0019031` (`viral envelope`, IEA) and `GO:0055036` (`virion membrane`, IEA): P3 is a peripheral virion membrane spike protein anchored via P6 on the viral envelope.
- **TOO_GENERAL**:
  - `GO:0019062` (`virion attachment to host cell`, IEA) and `GO:0046718` (`symbiont entry into host cell`, IEA): Subsumed by the more specific process `GO:0039666` (`virion attachment to host cell pilus`).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, IC from `file:BPPH6/P3/P3-uniprot.txt`): P3 is a major structural spike protein of the enveloped virion surface.
