# Curation Notes: Salmonella phage P22 Head-to-tail adapter gp4 (gene `4`, UniProt `P26746`)

## Identity & Domain Architecture
- **Gene symbol:** `4` (`EXLYS_BPP22`)
- **UniProt ID:** `P26746` (166 AA, ~18.0 kDa monomer)
- **InterPro / Pfam / Structural Classification:**
  - `InterPro:IPR038258` (`Gp4_sf`, Phage P22 tail accessory factor gp4 superfamily)
  - `InterPro:IPR020362` (`Tail_accessory_Gp4`, Bacteriophage P22, tail accessory factor Gp4)
  - `Pfam:PF11650` (`P22_Tail-4`)
  - `Gene3D:1.10.3230.20` (`Portal vertex protein GP4`)
- **PDB structures:** `1VT0` (isolated gp1-gp4 complex), `3LJ4` / `3LJ5` (crystal structure of dodecameric portal gp1 bound to dodecameric gp4), `8I1T` / `8I1V` (cryo-EM structure of the complete P22 tail apparatus).

## Literature & Functional Synthesis
1. **Dodecameric Head-to-Tail Structural Adapter (`PMID:16970964`, `PMID:21499245`, `PMID:37952769`):**
   - Monomeric gp4 in solution has very low thermal stability ($T_m = 34^\circ\text{C}$) and is prone to aggregation (`PMID:16970964`).
   - Upon termination of headful DNA packaging and dissociation of the terminase complex (`PMID:28134243`), gp4 binds to the bottom of the dodecameric portal ring (gp1) in two non-equivalent hexameric steps (via a $\text{gp1}_{12}:\text{gp4}_6$ intermediate) to assemble into a stable dodecameric ring (~75 Å tall) forming a hollow bi-dodecameric $\text{gp1}_{12}:\text{gp4}_{12}$ complex (`PMID:16970964`, `PMID:21499245`).
   - Rather than plugging the DNA channel itself, gp4 acts as the structural head-to-tail adapter that recruits the hexameric tail hub (gp10) and six homotrimeric tailspikes (gp9), stabilizing the packaged DNA genome and forming part of the axial genome-delivery conduit (`PMID:16970964`, `PMID:21499245`, `PMID:37952769`).
2. **Reported Virion-Associated Peptidoglycan Hydrolase Activity (`PMID:14763988`):**
   - Moak & Molineux (2004, `PMID:14763988`) reported muralytic (peptidoglycan hydrolase) activity at the molecular mass of gp4 in zymogram assays of SDS-disrupted P22 virions ("P22gp4 is part of the neck of the particle and is essential for infectivity").
   - Subsequent atomic structures (`PMID:21499245`, `PMID:37952769`) and cryo-ET of P22 infection initiation (`PMID:30886360`) show that gp4 folds as a compact four-helix bundle with an extended C-terminal tail that remains stably bound to the portal vertex outside the host outer membrane during genome ejection. Following GO curation guidelines, the experimental annotation from `PMID:14763988` (`GO:0098932`) and its concordant IEA (`GO:0016787`, `GO:0098932`) are retained as `KEEP_AS_NON_CORE`, while the structural head-to-tail adapter role in virion assembly (`GO:0019068`) and short-tail genome ejection (`GO:0099002`) is captured as the core function.

## GO Annotation Decisions
- `GO:0098015` (virus tail, IDA `PMID:16970964` & IDA `PMID:37952769`): `ACCEPT`.
- `GO:0099002` (symbiont genome ejection through host cell envelope, short tail mechanism, IDA `PMID:21499245` & IEA `GO_REF:0000043`): `ACCEPT`.
- `GO:0098932` (symbiont entry into host cell via disruption of host cell wall peptidoglycan, IDA `PMID:14763988` & IEA `GO_REF:0000043`): `KEEP_AS_NON_CORE`.
- `GO:0016787` (hydrolase activity, IEA `GO_REF:0000043`): `KEEP_AS_NON_CORE` (zymogram assay in `PMID:14763988` detected muralytic hydrolysis without defining the specific bond cleaved).
- `GO:0046718` (symbiont entry into host cell, IEA `GO_REF:0000043`): `MODIFY` -> `GO:0099002` and `GO:0098932`.
- `GO:0098994` (symbiont entry into host cell via disruption of host cell envelope, IEA `GO_REF:0000043`): `MODIFY` -> `GO:0099002` and `GO:0098932`.
- `GO:0005198` (structural molecule activity, IDA `PMID:21499245`): `NEW`.
- `GO:0019068` (virion assembly, IDA `PMID:16970964`): `NEW`.
