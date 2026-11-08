# Curatorial Notes for `pstA` (`A0A0H2M6I3`, `VPARA_10460`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0H2M6I3` (`A0A0H2M6I3_VARPD`)
- **Gene Symbol:** `pstA`
- **Locus Tag / EMBL CDS:** `VPARA_10460` / `KLN58034.1` on contig `JZWI01000005` (`RefSeq:WP_080966475.1`)
- **Protein Length:** 294 aa (31,555 Da); 6 transmembrane helices (`30..51`, `79..102`, `123..144`, `150..169`, `205..223`, `267..289`) and an ABC transmembrane type-1 domain (`PROSITE:PS50928` at `83..286`, `Pfam:PF00528` `BPD_transp_1`, `CDD:cd06261` `TM_PBP2`).
- **Specific Family & Active-Site Conservation:**
  - `InterPro:IPR005672` (`Phosphate_PstA`), `NCBIfam:TIGR00974` (`3a0107s02c`), `NCBIfam:NF008430` (`pstA`), `PANTHER:PTHR42922:SF1` (`PHOSPHATE TRANSPORT SYSTEM PERMEASE PROTEIN PSTA`).
  - Conserves `Arg221` and `Glu225` within `220-ARIAGETA-227` (corresponding to *E. coli* PstA `Arg220`, whose mutation `Arg220Gln` abolishes phosphate transport through PstSCAB in `PMID:2896188`).

## 2. Operon Context on Contig `JZWI01000005`
- Encoded between `pstB` (`VPARA_10450`, `KLN58033.1`) and `pstC` (`VPARA_10470`, `KLN58035.1`) within the `phoR1-phoB1-phoU-pstB-pstA-pstC-pstS-ppx` (`VPARA_10420`–`VPARA_10490`) phosphate regulon gene cluster.

## 3. Literature & Comparative Evidence
- **[PMID:2896188]** (Cox et al. 1988 *J Bacteriol*): Site-directed mutagenesis demonstrates that `Arg220` of *E. coli* PstA is essential for orthophosphate translocation through the Pst system.
- **[PMID:3881386]** (Surin et al. 1985 *J Bacteriol*): Complete sequence of the `phoS-pstC-pstA-pstB-phoU` operon.
- **[PMID:24563032]** (Gardner et al. 2014 *J Bacteriol*): Subunit architecture of PstSCAB and coupling to PhoU and PhoR.

## 4. Annotation Review Decisions
- Following `ECOLI/pstA` (`P0AGH5`) and `ECOLI/pstC` (`P0AGH8`):
  - `GO:0005315` (`phosphate transmembrane transporter activity`, IEA `GO_REF:0000002`, `enables`): **MARK_AS_OVER_ANNOTATED** — PstA is one of two heterodimeric transmembrane permease subunits (with PstC) of the PstSCAB complex; its `contributes_to` relationship to `GO:0005315` is captured in `core_functions.contributes_to_molecular_function`.
  - `GO:0005886` (`plasma membrane`, IEA `GO_REF:0000120`): **ACCEPT** — core location of this 6-pass inner-membrane permease subunit.
  - `GO:0016020` (`membrane`, IEA `GO_REF:0000120`): **TOO_GENERAL** — entailed by `GO:0005886`.
  - `GO:0035435` (`phosphate ion transmembrane transport`, IEA `GO_REF:0000002`): **ACCEPT** — core biological process.
  - `GO:0043190` (`ATP-binding cassette (ABC) transporter complex`, IEA `GO_REF:0000104`): **MODIFY** -> `GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`).
  - `GO:0055085` (`transmembrane transport`, IEA `GO_REF:0000002`): **TOO_GENERAL** — entailed by `GO:0035435`.
  - `GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`, IC from `file:VARPD/pstA/pstA-uniprot.txt`): **NEW**.
