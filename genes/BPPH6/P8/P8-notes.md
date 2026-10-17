# P8 (CAPSD_BPPH6, P07579) — Curation Notes

## Overview
- **Organism:** *Pseudomonas* phage phi6 (`NCBITaxon:2928686`, *Cystovirus phi6*)
- **Gene / Protein:** `P8` / Major outer capsid protein P8 (`UniProtKB:P07579`, 149 AA)
- **Genomic Segment:** Encoded on the small (S) dsRNA segment.

## Biological Role in the Cystovirus Lifecycle
1. **T=13 Outer Nucleocapsid Shell (`GO:0039660`, `GO:0039621`, `GO:0039624`):**
   - Phage phi6 possesses a double-layered icosahedral nucleocapsid surrounded by a lipid-protein envelope.
   - Protein P8 forms 200 homotrimers (600 monomers total, plus vertices occupied by P4 hexamers) arranged in an interrupted $T=13$ icosahedral lattice (`GO:0039621`) that encases the $T=2$ inner polymerase core (`P1`/`P2`/`P4`/`P7`) to form the mature nucleocapsid (`GO:0039624`, `GO:0039660`) [file:BPPH6/P8/P8-uniprot.txt].
   - Assembly and stability of the P8 shell around the polymerase core depend on calcium ions (`GO:0005509` calcium ion binding); chelation of $\text{Ca}^{2+}$ strips the P8 shell from the nucleocapsid.
2. **Host Cytoplasmic Membrane Penetration (`GO:0046718`):**
   - After P3 attaches to the host type IV pilus and fusogenic envelope protein P6 mediates fusion of the viral envelope with the *Pseudomonas syringae* outer membrane, the nucleocapsid enters the periplasm.
   - Following peptidoglycan digestion by P5, the outer P8 shell directly interacts with the host cytoplasmic (inner) membrane and drives voltage-dependent, endocytic-like penetration of the inner polymerase core into the host cytoplasm (`GO:0046718`), shedding P8 in the process [file:BPPH6/P8/P8-uniprot.txt].

## Curation Decisions
- **Existing GOA Annotations:**
  - `GO:0019028` (`viral capsid`, IEA): `MODIFY` to `GO:0039621` (`T=13 icosahedral viral capsid`) and `GO:0039624` (`viral outer capsid`), which are already present and capture the exact architecture and layer of P8.
  - `GO:0039621` (`T=13 icosahedral viral capsid`, IEA): `ACCEPT`.
  - `GO:0039624` (`viral outer capsid`, IEA): `ACCEPT`.
- **New Annotations (`action: NEW`):**
  - `GO:0039660` (`structural constituent of virion`, `enables`, `IC` from `file:BPPH6/P8/P8-uniprot.txt`): Captures the core structural molecular function of P8 in forming the 600-copy $T=13$ outer nucleocapsid lattice.
  - `GO:0046718` (`symbiont entry into host cell`, `involved_in`, `IC` from `file:BPPH6/P8/P8-uniprot.txt`): Captures P8's active role in driving penetration of the viral core across the host plasma membrane into the cytoplasm.
