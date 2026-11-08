# Curatorial Notes for `pstC` (`A0A0H2MMT5`, `VPARA_10470`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0H2MMT5` (`A0A0H2MMT5_VARPD`)
- **Gene Symbol:** `pstC`
- **Locus Tag / EMBL CDS:** `VPARA_10470` / `KLN58035.1` on contig `JZWI01000005` (`RefSeq:WP_047783562.1`)
- **Protein Length:** 359 aa (37,449 Da); 6 transmembrane helices (`65..88`, `108..139`, `151..175`, `195..221`, `266..288`, `325..348`) and an ABC transmembrane type-1 domain (`PROSITE:PS50928` at `114..344`, `Pfam:PF00528` `BPD_transp_1`, `CDD:cd06261` `TM_PBP2`).
- **Specific Family & Active-Site Conservation:**
  - `InterPro:IPR011864` (`Phosphate_PstC`), `NCBIfam:TIGR02138` (`phosphate_pstC`), `PANTHER:PTHR30425:SF1` (`PHOSPHATE TRANSPORT SYSTEM PERMEASE PROTEIN PSTC`).
  - Conserves the essential transmembrane/coupling motif `281-LGRALGETM-289` containing `Arg282` and `Glu286` (corresponding to *E. coli* PstC `Arg237` and `Glu240`, whose substitution to Gln abolishes Pst phosphate transport in `PMID:2646285`).

## 2. Operon Context on Contig `JZWI01000005`
- Encoded immediately between `pstA` (`VPARA_10460`, `KLN58034.1`) and `pstS` (`VPARA_10480`, `KLN58036.1`) within the `phoR1-phoB1-phoU-pstB-pstA-pstC-pstS-ppx` (`VPARA_10420`–`VPARA_10490`) phosphate regulon gene cluster.

## 3. Literature & Comparative Evidence
- **[PMID:3881386]** (Surin et al. 1985 *J Bacteriol*): Complete sequence and gene-polypeptide relationships of the *E. coli* `phoS-pstC-pstA-pstB-phoU` operon.
- **[PMID:2646285]** (Cox, Webb & Rosenberg 1989 *J Bacteriol*): Site-directed mutagenesis of *E. coli* `pstC` (`Arg237Gln`, `Glu240Gln`) abolishes phosphate transport through the Pst system.
- **[PMID:24563032]** (Gardner et al. 2014 *J Bacteriol*): Establishes that PstC and PstA are integral inner-membrane proteins that form the pore of the PstSCAB high-affinity $\text{P}_i$ ABC importer.

## 4. Annotation Review Decisions
- Following `ECOLI/pstC` (`P0AGH8`):
  - `GO:0005315` (`phosphate transmembrane transporter activity`, IEA `GO_REF:0000002`, `enables`): **MARK_AS_OVER_ANNOTATED** — PstC is one of two heterodimeric transmembrane permease subunits (with PstA) of the PstSCAB holocomplex rather than an independent transporter; its `contributes_to` relationship to `GO:0005315` is captured in `core_functions.contributes_to_molecular_function`.
  - `GO:0005886` (`plasma membrane`, IEA `GO_REF:0000044`): **ACCEPT** — core location of this 6-TMH inner-membrane permease subunit.
  - `GO:0006817` (`phosphate ion transport`, IEA `GO_REF:0000002`): **MODIFY** -> `GO:0035435` (`phosphate ion transmembrane transport`).
  - `GO:0016020` (`membrane`, IEA `GO_REF:0000120`): **TOO_GENERAL** — entailed by `GO:0005886` (`plasma membrane`).
  - `GO:0043190` (`ATP-binding cassette (ABC) transporter complex`, IEA `GO_REF:0000104`): **MODIFY** -> `GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`).
  - `GO:0055085` (`transmembrane transport`, IEA `GO_REF:0000002`): **MODIFY** -> `GO:0035435` (`phosphate ion transmembrane transport`).
  - `GO:0035435` (`phosphate ion transmembrane transport`, IC from `file:VARPD/pstC/pstC-uniprot.txt`): **NEW**.
  - `GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`, IC from `file:VARPD/pstC/pstC-uniprot.txt`): **NEW**.
