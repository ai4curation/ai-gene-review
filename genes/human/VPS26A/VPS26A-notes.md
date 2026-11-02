# VPS26A (O75436) Curation Notes

## Overview & Complex Architecture
- **VPS26A** (`O75436`, ~38 kDa, 327 aa) is the arrestin-fold cargo-recognition and membrane-docking subunit of the mammalian **retromer cargo-selective complex (CSC)** (`VPS35:VPS29:VPS26A`) ([PMID:11102511]; [PMID:16732284, "The structure of human Vps26A at 2.1-A resolution reveals two curved beta-sandwich domains connected by a polar core and a flexible linker. Vps26 has an unpredicted structural relationship to arrestins. The Vps35-binding site on Vps26 maps to a mobile loop spanning residues 235-246, near the tip of the C-terminal domain."]; [PMID:17891154]).
- **Paralog Specialization (`VPS26A` vs `VPS26B` vs `VPS26C`)**:
  - Vertebrates express two mutually exclusive retromer CSC paralogs, **VPS26A** and **VPS26B** (`Q4G0F5`), which compete for the same N-terminal `PRLYL` binding site on **VPS35** to form distinct `VPS35:VPS29:VPS26A` and `VPS35:VPS29:VPS26B` retromer complexes ([PMID:37172566, "Retriever, a VPS26C:VPS35L:VPS29 trimer, shares distant homology to Retromer, itself a trimer of VPS29, VPS35, and either VPS26A or VPS26B (paralogues with VPS26C)."]).
  - A third distant arrestin-fold paralog, **VPS26C** (`DSCR3`), does **not** bind VPS35 and instead pairs with **VPS35L** (`C16orf62`) and **VPS29** to form the **Retriever complex** ([PMID:28892079]).

## Core Biological Functions
1. **Structural Assembly of the Retromer Cargo-Selective Complex & Membrane Docking**:
   - VPS26A binds the N-terminal tip of the VPS35 alpha-solenoid via its C-terminal arrestin-like subdomain (mobile loop residues 235–246) ([PMID:16732284]).
   - On endosomal membranes, VPS26A interacts with the N-terminal extension and PX domain of **SNX3** to form the SNX3-retromer coat, positioning a conserved hydrophobic pocket at the interface of VPS26A and SNX3 to recognize canonical `Øx[L/M/V]` sorting signals ([PMID:27889239, "Here, we present an X-ray crystallographic analysis of a four-component complex comprising the VPS26 and VPS35 subunits of retromer, the sorting nexin SNX3, and a recycling signal from the divalent cation transporter DMT1-II. This analysis identifies a binding site for canonical recycling signals at the interface between VPS26 and SNX3."]; [PMID:21725319]).
2. **Direct Cargo & Adaptor Recognition (`GO:0140312` / `GO:0042147` / `GO:0032456`)**:
   - **Direct cargo tail binding**: VPS26A and SNX3 directly recognize cytoplasmic `Øx[L/M]` sorting signals on cargoes such as **DMT1-II** (`SLC11A2`), **CI-MPR** (`IGF2R`), **sortilin** (`SORT1`), and **Wntless** (`WLS`) ([PMID:27889239]; [PMID:15078903]; [PMID:18193037]).
   - **SNX27 adaptor binding**: VPS26A directly binds an exposed beta-hairpin loop in the PDZ domain of the endosomal sorting nexin **SNX27**, increasing SNX27 affinity for PDZ-binding motifs by an order of magnitude and coupling PDZ-motif cargoes (such as beta-2 adrenergic receptor `ADRB2`, glucose transporter `GLUT1`/`SLC2A1`, and metal/ion transporters) to the retromer CSC for endosome-to-plasma membrane recycling ([PMID:23563491, "Furthermore, we establish that direct interaction of the SNX27 PDZ domain with the retromer subunit VPS26 is necessary and sufficient to prevent lysosomal entry of SNX27 cargo."]; [PMID:25136126, "Crystal structures and NMR experiments reveal that an exposed β-hairpin in the SNX27 PDZ domain engages a groove in the arrestin-like structure of the vacuolar protein sorting 26A (VPS26A) retromer subunit."]; [PMID:21602791]).
3. **Endosome-to-TGN Retrieval**:
   - Required as an essential subunit of the retromer CSC for endosome-to-TGN retrieval of **CI-MPR** (`IGF2R`), **sortilin** (`SORT1`), and **Wntless** (`WLS`) ([PMID:15078903]; [PMID:18193037]; [PMID:22431521]).

## Key Curation & GO Annotation Decisions
- **Core MF (`NEW`)**:
  - `GO:0140312` (`cargo adaptor activity`, `contributes_to`): Proposed as `NEW` (`IDA` from `PMID:27889239`, supported by `PMID:27889239`, `PMID:23563491`, and `PMID:25136126`) because X-ray crystal structures demonstrate that VPS26A directly forms the canonical `Øx[L/M]` cargo-recognition pocket with SNX3 and binds the SNX27 PDZ domain; the other two retromer CSC subunits (`VPS35` and `VPS29`) already carry `GO:0140312` in GOA.
  - `GO:0005515` (`protein binding`): All 31 unique IPI entries in `existing_annotations` (corresponding to 32 raw `GO:0005515` IPI rows in `VPS26A-goa.tsv`, where rows 11 and 71 are duplicate IntAct/`UniProtKB:Q9UBQ0` rows) are `REMOVE` per standard GO protein-binding policy.
- **Core BP (`ACCEPT` and `MODIFY`)**:
  - `GO:0042147` (`retrograde transport, endosome to Golgi`): `ACCEPT` across IBA, IMP (`PMID:15078903`), and NAS (`PMID:11102511`, `PMID:26220253`) rows.
  - `GO:0032456` (`endocytic recycling`): `ACCEPT` across IMP (`PMID:21602791`) and NAS (`PMID:30072228`) rows, supported by direct SNX27-VPS26A structural and proteomic studies (`PMID:23563491`, `PMID:25136126`).
  - `GO:0006886` (`intracellular protein transport`, IBA and IEA): `MODIFY` to `GO:0042147` (`retrograde transport, endosome to Golgi`) and `GO:0032456` (`endocytic recycling`).
- **Core CC (`ACCEPT` and `MODIFY`)**:
  - `GO:0030906` (`retromer, cargo-selective complex`) and `GO:0030904` (`retromer complex`): `ACCEPT`.
  - `GO:0005768` (`endosome`), `GO:0005769` (`early endosome`), `GO:0010008` (`endosome membrane`), `GO:0097422` (`tubular endosome`), and `GO:0005829` (`cytosol`): `ACCEPT`.
  - `GO:0005737` (`cytoplasm`): `MODIFY` to `GO:0005829` (`cytosol`) and `GO:0010008` (`endosome membrane`).
  - `GO:0031982` (`vesicle`, IDA `PMID:20682791`): `MODIFY` to `GO:0005769` (`early endosome`) and `GO:0097422` (`tubular endosome`).
  - `GO:0005764` (`lysosome`, IDA `GO_REF:0000052`): `MODIFY` (lateral refinement of HPA endolysosomal puncta) to `GO:0005768` (`endosome`).
- **Non-Core / Indirect BP (`KEEP_AS_NON_CORE`)**:
  - `GO:0016241` (`regulation of macroautophagy`, IEA and TAS `PMID:26172538`): `KEEP_AS_NON_CORE` — in Vps26/Vps35-deficient cells, autophagosome formation and autophagy initiation are intact (consistent with the curated `NOT|involved_in GO:0010506` annotation on `VPS29`), whereas late-stage autophagic cargo degradation is impaired indirectly due to defective CI-MPR-mediated lysosomal hydrolase delivery.
