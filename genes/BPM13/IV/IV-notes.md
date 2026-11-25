# Enterobacteria phage M13 — Gene IV (G4P / pIV)

## Overview
- **UniProt Accession:** P03665 (`G4P_BPM13`)
- **Gene Symbol:** `IV`
- **Protein Product:** Virion export protein G4P (pIV), synthesized as a 426 aa precursor with a 21 aa N-terminal signal peptide cleaved to yield the 405 aa mature outer-membrane secretin subunit (`file:BPM13/IV/IV-uniprot.txt`).

## Biological Role in the M13 Lifecycle
- **Outer-Membrane Secretin Channel:** Mature pIV is a member of the bacterial type II/III secretion system secretin superfamily (`IPR001775`, `PF00263`). Fifteen pIV subunits assemble in the *Escherichia coli* outer membrane into a gated, barrel-like β-barrel secretin channel (~13.5 nm outer diameter, 22–24 nm length, ~6–9 nm central pore closed by a central gate) (`file:BPM13/IV/IV-uniprot.txt`, [PMID:35746635]).
- **Envelope-Spanning Extrusion Conduit:** The periplasmic N-terminal region of the pIV multimer interacts with the periplasmic C-terminal domains of the inner-membrane pI/pXI (G1P/G11P) ATPase assembly complex [PMID:35746635]. During filamentous phage assembly, the nascent virion pushes open the pIV periplasmic gate and traverses the outer membrane through the pIV lumen without lysing the host cell (`GO:0099045` viral extrusion).
- **Note on Existing Annotations:**
  - `GO:0020002` (host cell plasma membrane) in GOA arises from a conservative SubCell mapping (`SL-0376` Host cell outer membrane -> `GO:0020002` in older mapping tables or ISS transfer), whereas pIV is localized to the **host cell outer membrane** (`GO:0039662`). Therefore `GO:0020002` should be `MODIFY` -> `GO:0039662` (host cell outer membrane).
  - `GO:0009306` (protein secretion) comes from InterPro2GO mapping of the secretin domain (`IPR004846`); in phage M13, pIV mediates extrusion of the intact nucleoprotein virion (`GO:0099045` viral extrusion) rather than canonical bacterial protein secretion, so `GO:0009306` should be `MODIFY` -> `GO:0099045`.

## Key GO Annotations
- **Cellular Component:** `GO:0039662` (host cell outer membrane).
- **Biological Process:** `GO:0099045` (viral extrusion).
