# Curation Notes: Salmonella phage P22 Tail needle protein gp26 (gene `26`, UniProt `P35837`)

## Identity & Domain Architecture
- **Gene symbol:** `26` (`NEEDL_BPP22`)
- **UniProt ID:** `P35837` (233 AA, ~24.7 kDa monomer; ~74 kDa homotrimer)
- **Structural / Database Cross-References:**
  - `Gene3D:1.20.5.340` (`Tail needle protein gp26, helical core domain`)
  - `Gene3D:6.10.140.940`
  - `SUPFAM:SSF57997` (`Tropomyosin`)
  - `TCDB:1.K.4.1.1`
- **PDB structures:** `2POH` (2.1 Å crystal structure at acidic pH), `3C9I`, `4ZKP` / `4ZKQ` / `4ZKR` (neutral and alkaline pH crystal structures), `8I1T` / `8I1V` (cryo-EM of P22 tail apparatus).

## Literature & Functional Synthesis
1. **Homotrimeric Coiled-Coil Tail Needle & Portal Plug (`PMID:18059287`, `PMID:19482036`, `PMID:26574546`, `PMID:37952769`):**
   - `gp26` forms an extraordinary 240-Å-long, ~25-Å-wide homotrimeric fiber ($T_m \approx 85\text{--}88^\circ\text{C}$, $C_m = 6.4\text{ M}$ GdnHCl) located at the distal tip of the central tail axis (`PMID:18059287`, `PMID:19482036`).
   - It comprises four linearly arranged domains (`PMID:18059287`, `PMID:19482036`, `PMID:26574546`):
     1. **N-terminal tip (NTT, residues 1-60):** Binds inside the central channel of the hexameric gp10 tail hub in an extended pre-ejection conformation to plug the portal-tail channel and trap the pressurized dsDNA genome inside the capsid; loss of gp26 produces particles that package DNA normally but leak it spontaneously ("DNA leakage phenotype"). Upon ejection, the NTT refolds into a compact trimer of hairpins (`PMID:26574546`).
     2. **Central alpha-helical coiled-coil core (residues 60-140):** Spans 11 tandem trimerization heptads stabilized by hydrophobic knobs-into-holes packing, inter-helical salt bridges, and buried calcium and chloride ions (`PMID:18059287`, `PMID:19482036`).
     3. **Triple beta-helix domain.**
     4. **C-terminal distal tip (CTT, inverted alpha-helical coiled-coil / lazo domain):** Exposes beta-hairpins with hydrophobic tips resembling class II viral fusion peptides (`PMID:18059287`, `PMID:20817910`).
2. **Outer Membrane Penetration & Triggering of Genome Ejection (`PMID:20817910`, `PMID:30886360`):**
   - During infection initiation (`PMID:20817910`, `PMID:30886360`), gp9 tailspike binding and hydrolysis of *Salmonella* O-antigen LPS brings the virion close to the cell surface and reorients it perpendicularly, driving the gp26 tail needle into the host outer membrane (`GO:0044694`).
   - Outer membrane interaction triggers release of the gp26 plug from the gp10 baseplate, opening the tail conduit so that the internal ejection proteins (`gp7*`, `gp20`, `gp16`) and the 43-kbp dsDNA genome are ejected across the host cell envelope (`GO:0099002`, `PMID:30886360`).

## GO Annotation Decisions
- `GO:0044694` (viral penetration into host cell via proteinaceous needle, IEA `GO_REF:0000120`): `ACCEPT` (directly supported by crystallography in `PMID:18059287` and cryo-ET in `PMID:30886360`).
- `GO:0046718` (symbiont entry into host cell, IEA `GO_REF:0000120`): `MODIFY` -> `GO:0044694` and `GO:0099002`.
- `GO:0098015` (virus tail, IDA `PMID:37952769` & IEA `GO_REF:0000120`): `ACCEPT`.
- `GO:0099002` (symbiont genome ejection through host cell envelope, short tail mechanism, IEA `GO_REF:0000120`): `ACCEPT` (supported by `PMID:20817910`, `PMID:26574546`, `PMID:30886360`).
- `GO:0005198` (structural molecule activity, IDA `PMID:18059287`): `NEW`.
- `GO:0019068` (virion assembly, IDA `PMID:26574546`): `NEW`.
