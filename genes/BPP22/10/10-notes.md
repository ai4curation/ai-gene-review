# Curation Notes: Salmonella phage P22 Tail hub protein gp10 (gene `10`, UniProt `P26749`)

## Identity & Domain Architecture
- **Gene symbol:** `10` (`HUB10_BPP22`)
- **UniProt ID:** `P26749` (472 AA, ~52.4 kDa monomer)
- **InterPro / Pfam Classification:**
  - `InterPro:IPR063099` (`P22_Gp10_C`, Phage P22 tail accessory factor Gp10 C-terminal)
  - `InterPro:IPR021098` (`Phage_P22_Gp10`, Bacteriophage P22, tail protein Gp10)
  - `Pfam:PF29665` (`P22_Gp10_C`)
  - `Pfam:PF11134` (`Phage_stabilise`)
- **PDB structures:** `8I1T`, `8I1V` (3.7 Å cryo-EM localized reconstruction of the complete P22 tail apparatus).

## Literature & Functional Synthesis
1. **Hexameric Tail Hub / Baseplate Hub (`PMID:16970964`, `PMID:19482036`, `PMID:26574546`, `PMID:37952769`):**
   - Following headful DNA packaging and attachment of 12 copies of the head-to-tail adapter gp4 to the portal ring, 6 copies of gp10 assemble onto the distal face of the dodecameric gp4 ring to form the hexameric tail hub (baseplate hub) (`PMID:26574546`, `PMID:37952769`).
   - High-resolution cryo-EM (`PMID:37952769`) shows that gp10 adopts a beta-propeller-like fold and serves as the central structural organizer of the distal tail machine:
     - Its top surface mediates the 12:6 symmetry match with the dodecameric gp4 ring.
     - Its central lumen binds the N-terminal 60 residues of the homotrimeric tail needle gp26 (`PMID:19482036`, `PMID:26574546`), which plugs the central channel to prevent premature DNA leakage.
     - Its six exterior lateral surfaces provide the binding sites for the N-terminal head-binding domains of the six homotrimeric tailspikes (gp9) (`PMID:37952769`).
2. **Role in Short-Tail Genome Ejection (`PMID:30886360`, `PMID:37952769`):**
   - Cryo-electron tomography of P22 infecting *Salmonella* minicells (`PMID:30886360`) demonstrates that after the gp26 tail needle penetrates the outer membrane and is released from the gp10 lumen, the internal head protein gp7* is ejected through the gp1-gp4-gp10 channel and assembles into a ~40 nm trans-envelope channel extending directly from the distal end of the gp10 baseplate to the host cell surface to guide dsDNA translocation into the cytoplasm.

## GO Annotation Decisions
- `GO:0098015` (virus tail, IDA `PMID:37952769`): `ACCEPT`.
- `GO:0005198` (structural molecule activity, IDA `PMID:37952769`): `NEW`.
- `GO:0019068` (virion assembly, IDA `PMID:26574546`): `NEW`.
- `GO:0099002` (symbiont genome ejection through host cell envelope, short tail mechanism, IDA `PMID:30886360`): `NEW`.
