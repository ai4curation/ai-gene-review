# Curation Notes: *Variovorax paradoxus* TBEA6 `exbD5` (`A0A0H2M1F3`, `VPARA_25800`)

## 1. Gene & Protein Identity
- **Organism:** *Variovorax paradoxus* TBEA6 (`NCBITaxon:34073`)
- **UniProtKB Accession:** `A0A0H2M1F3` (`A0A0H2M1F3_VARPD`, unreviewed TrEMBL, 137 aa)
- **Gene Symbol / Locus Tag:** `exbD5` / `VPARA_25800`
- **Genomic Context:** First gene of the syntenic four-gene ferric-siderophore import operon `exbD5-exbB4-tonB-bfrD1` (`VPARA_25800`–`VPARA_25830`) on contig `JZWI01000012`.

## 2. Sequence & Structural Verification
- **Single-Pass Type II Inner-Membrane Topology (`UniProtKB:A0A0H2M1F3`):**
  - Cytoplasmic N-tail: residues 1–19 (`1-MAFGTQDEPDEVMNEINMT-19`)
  - `FT TRANSMEM 20..39`: `20-PLVDVMLVLLIIFIITVPVM-39` (`/note="Helical" /evidence="ECO:0000256|SAM:Phobius"`)
  - Invariant proton-binding aspartate residue: **`Asp23`** (`20-PLVDVMLVLLIIFIITVPVM-39`), corresponding to the essential catalytic proton-relay aspartate (*E. coli* ExbD Asp25) inside the central pore of the ExbB pentamer.
  - Periplasmic C-terminal domain: residues 40–137 (`Pfam:PF02472` `ExbD`, `InterPro:IPR003400`, `Gene3D:3.30.420.270`, `PANTHER:PTHR30558`).
  - **PANTHER Subfamily Call (`PTHR30558:SF7`):** Note that `UniProtKB:A0A0H2M1F3` lists `DR PANTHER; PTHR30558:SF7; TOL-PAL SYSTEM PROTEIN TOLR; 1.` alongside family `PTHR30558` (`EXBD MEMBRANE COMPONENT OF PMF-DRIVEN MACROMOLECULE IMPORT SYSTEM`). Because `VPARA_25800` is encoded at the 5' end of the canonical TonB-dependent ferric-siderophore uptake operon `exbD5-exbB4-tonB-bfrD1` (`VPARA_25800`–`VPARA_25830`) rather than a `tolQ-tolR-tolA-tolB-pal` cell-envelope locus, the `SF7` TolR subfamily assignment is an automated subfamily boundary artifact and is deliberately omitted in favor of family-level `PTHR30558`.
- **Mechanism in the TonB-ExbB-ExbD Motor:**
  - Two copies of ExbD reside inside the central lumen of the ExbB pentamer in the cytoplasmic membrane and extend their C-terminal domains into the periplasm [PMID:37219427 Energization of Outer Membrane Transport by the ExbB ExbD Molecular Motor., "ExbB forms a pentamer with a pore inside, in which an ExbD dimer resides. This complex harvests the energy of the pmf and transmits it to TonB."].
  - Together with ExbB4 (`VPARA_25810`) and TonB (`VPARA_25820`), ExbD5 transduces the proton-motive force to outer-membrane TonB-dependent ferric-siderophore receptors such as BfrD1 (`VPARA_25830`) [PMID:20420522 TonB-dependent transporters: regulation, structure, and function., "The transport process requires energy in the form of proton motive force and a complex of three inner membrane proteins, TonB-ExbB-ExbD, to transduce this energy to the outer membrane."].

## 3. Curation Decisions
- **Accepted:** `GO:0005886` (`plasma membrane`).
- **Modified:**
  - `GO:0022857` (`transmembrane transporter activity`) $\rightarrow$ `GO:0015078` (`proton transmembrane transporter activity`).
  - `GO:0055085` (`transmembrane transport`) $\rightarrow$ `GO:1902600` (`proton transmembrane transport`) and `GO:0015891` (`siderophore transport`).
- **Added (`NEW`, `IC`):**
  - `GO:0030288` (`outer membrane-bounded periplasmic space`)
  - `GO:0098797` (`plasma membrane protein complex`)
