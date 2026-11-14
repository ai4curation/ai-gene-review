# Curation Notes: *Variovorax paradoxus* TBEA6 `exbB4` (`A0A0H2MHH3`, `VPARA_25810`)

## 1. Gene & Protein Identity
- **Organism:** *Variovorax paradoxus* TBEA6 (`NCBITaxon:34073`)
- **UniProtKB Accession:** `A0A0H2MHH3` (`A0A0H2MHH3_VARPD`, unreviewed TrEMBL, 238 aa)
- **Gene Symbol / Locus Tag:** `exbB4` / `VPARA_25810`
- **Genomic Context:** Encoded in the syntenic four-gene ferric-siderophore import cluster `exbD5-exbB4-tonB-bfrD1` (`VPARA_25800`–`VPARA_25830`) on contig `JZWI01000012`:
  - `VPARA_25800` (`exbD5`, `A0A0H2M1F3`, 137 aa)
  - `VPARA_25810` (`exbB4`, `A0A0H2MHH3`, 238 aa)
  - `VPARA_25820` (`tonB`, `A0A0H2M2E3`, 232 aa)
  - `VPARA_25830` (`bfrD1`, `A0A0H2M677`, 739 aa)

## 2. Domain Architecture & Structural Biology
- **Three-Transmembrane Stator Topology (`UniProtKB:A0A0H2MHH3`):**
  - `FT TRANSMEM 20..41` (TM1: `20-AVAVLLVGMSLASWIVIIIKAL-41`)
  - Cytoplasmic alpha-helical bundle (residues 42–126)
  - `FT TRANSMEM 127..150` (TM2: `127-LAILASVGSTAPFIGLFGTVWGIY-150`, containing conserved polar residues `Ser132`, `Ser135`, `Thr136`, and `Thr145`)
  - `FT TRANSMEM 174..195` (TM3: `174-ALIMTALGLAVAIPAVLGYNAL-195`, containing conserved `Thr178` and `Pro187`)
  - `FT DOMAIN 100..201` (`Pfam:PF01618` `MotA_ExbB`, `InterPro:IPR002898`, `PANTHER:PTHR30625:SF14` `BIOPOLYMER TRANSPORT PROTEIN EXBB`).
- **Role in the $\text{ExbB}_5\text{ExbD}_2\text{TonB}$ Molecular Motor:**
  - Structural and biochemical studies establish that ExbB forms a pentameric inner-membrane pore enclosing a dimer of ExbD transmembrane helices [PMID:37219427 Energization of Outer Membrane Transport by the ExbB ExbD Molecular Motor., "ExbB forms a pentamer with a pore inside, in which an ExbD dimer resides. This complex harvests the energy of the pmf and transmits it to TonB."].
  - Together with TonB (`VPARA_25820`), the inner-membrane TonB-ExbB-ExbD complex harvests the cytoplasmic-membrane proton-motive force and transduces mechanical energy across the periplasm to outer-membrane TonB-dependent siderophore receptors such as BfrD1 (`VPARA_25830`) [PMID:20420522 TonB-dependent transporters: regulation, structure, and function., "The transport process requires energy in the form of proton motive force and a complex of three inner membrane proteins, TonB-ExbB-ExbD, to transduce this energy to the outer membrane."].

## 3. Curation Decisions
- **Accepted:** `GO:0005886` (`plasma membrane`).
- **Too General:** `GO:0016020` (`membrane`) — subsumed by `GO:0005886` (`plasma membrane`).
- **Removed:** `GO:0017038` (`protein import`, IEA via `PANTHER:PTN004746216`) — over-propagated from opportunistic bacteriophage/colicin protein toxin entry in enteric bacteria; physiologically `exbB4` energizes siderophore-iron uptake.
- **Added (`NEW`, `IC`):**
  - `GO:0015078` (`proton transmembrane transporter activity`)
  - `GO:1902600` (`proton transmembrane transport`)
  - `GO:0015891` (`siderophore transport`)
  - `GO:0098797` (`plasma membrane protein complex`)
