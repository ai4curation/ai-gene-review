# VPS29 (Q9UBQ0) Curation Notes

## Overview & Dual Complex Membership (Retromer & Retriever/Commander)
- **VPS29** (`Q9UBQ0`, ~20.5 kDa, 182 aa) is a compact subunit with a calcineurin-like **metallophosphoesterase (MPE) fold** that serves as an essential structural scaffold and regulatory hub in **two distinct endosomal cargo-recycling complexes**:
  1. **Retromer Cargo-Selective Complex (CSC)** (`VPS35:VPS29:VPS26A` or `VPS35:VPS29:VPS26B`), where the C-terminal alpha-solenoid of **VPS35** wraps around VPS29 ([PMID:11102511]; [PMID:17891154, "Here we report the crystal structure of a VPS29-VPS35 subcomplex showing how the metallophosphoesterase-fold subunit VPS29 (refs 14, 15) acts as a scaffold for the carboxy-terminal half of VPS35."]; [PMID:37172566]).
  2. **Retriever Complex** (`VPS26C:VPS35L:VPS29`), a heterotrimer composed of **VPS26C** (`DSCR3`), **VPS35L** (`C16orf62`), and **VPS29** that assembles with the 10-subunit **CCC complex** (`COMMD1–10`, `CCDC22`, `CCDC93`) and **DENND10** to form the 16-subunit **Commander supercomplex** (`GO:0160309`, `commander complex`) ([PMID:28892079, "We have called this complex 'retriever'; it is a heterotrimer composed of DSCR3, C16orf62 and VPS29, and bears striking similarity to retromer."]; [PMID:34943955]; [PMID:37172566, "Retriever, a VPS26C:VPS35L:VPS29 trimer, shares distant homology to Retromer, itself a trimer of VPS29, VPS35, and either VPS26A or VPS26B (paralogues with VPS26C)."]).

## Pseudoenzyme Status: Complete Lack of Phosphatase Activity
- Although VPS29 adopts a classic calcineurin-like metallophosphoesterase fold capable of coordinating divalent metal cations in vitro, **VPS29 is a catalytically inactive pseudoenzyme**:
  - In the `Q9UBQ0` sequence (`SQ`, residues 61–65 `GDFDE`, immediately adjacent to the divalent metal-coordinating `Asp62`), position 63 is a conserved phenylalanine (**Phe63**) rather than a catalytic histidine (`file:human/VPS29/VPS29-uniprot.txt`).
  - Furthermore, when VPS29 is assembled into the retromer CSC (or Retriever), the putative metal-binding cleft is sterically occluded by the C-terminal alpha-solenoid of **VPS35** (or **VPS35L**) ([PMID:17891154, "VPS35 forms a horseshoe-shaped, right-handed, alpha-helical solenoid, the concave face of which completely covers the metal-binding site of VPS29"]; [PMID:37172566]).
  - UniProt `Q9UBQ0` explicitly records in `CC -!- CAUTION` (lines 401–404, citing `RN [9]` and `RN [14]` Swarbrick et al., `"VPS29 is not an active metallo-phosphatase but is a rigid scaffold required for retromer interaction with accessory proteins."`): `"CAUTION: Was originally believed to be a metal-dependent phosphatase but shown to lack catalytic activity; can bind metals with very low affinity suggesting that metal binding is not required for its function."` (`file:human/VPS29/VPS29-uniprot.txt`).
  - Therefore, any `phosphoprotein phosphatase activity` (`GO:0004721`) or `hydrolase activity` (`GO:0016787`) annotations inferred from the MPE fold or early in vitro assays would be false; notably, human GOA has already removed those MF terms, leaving `GO:0140312` (`cargo adaptor activity`, `contributes_to` via IBA) and `GO:0005515` (`protein binding`).

## Core Biological Functions
1. **Structural Scaffold of Retromer CSC and Retriever**:
   - Stabilizes the C-terminal domain of **VPS35** in retromer ([PMID:17891154]) and the C-terminal domain of **VPS35L** in Retriever/Commander ([PMID:28892079]; [PMID:37172566]).
2. **Regulatory Hub for Endosomal Rab7 Cycling (`TBC1D5`) and Tubular Scission (`VARP`, `SNX1/2`)**:
   - Presents a conserved hydrophobic surface patch (centered on **Leu152**) opposite the VPS35-binding interface that directly recruits the Rab7 GTPase-activating protein **TBC1D5** ([PMID:20923837]; [PMID:24603492, "The RabGAP protein TBC1D5 controls cellular endomembrane trafficking processes and binds the retromer subunit VPS29 and the ubiquitin-like protein ATG8 (LC3)."]), the Rab21/VAMP7-interacting adaptor **VARP** (`ANKRD27`), and the bacterial effector **RidL** (from *Legionella pneumophila*).
   - By recruiting **TBC1D5**, VPS29 promotes GTP hydrolysis on **RAB7A** to drive timely retromer coat disassembly and coordinate endosomal tubule dynamics ([PMID:20923837]).
   - Inside the 16-subunit **Commander** complex, the C-terminal tail of **VPS35L** wraps across the Leu152 hydrophobic pocket of VPS29, sterically blocking TBC1D5 and VARP binding so that Retriever does not recruit retromer-specific accessory factors ([PMID:37172566]).
3. **Endosome-to-TGN Retrieval (`GO:0042147`) and Endocytic Recycling (`GO:0032456`)**:
   - Essential as part of retromer for endosome-to-TGN retrieval of **CI-MPR** (`IGF2R`), **sortilin** (`SORT1`), and **Wntless** (`WLS`) ([PMID:15078903]; [PMID:18193037]; [PMID:20923837]) and for SNX27-retromer endocytic recycling ([PMID:21602791]).
   - Essential as part of **Retriever** (coupled to **SNX17** and the **CCC complex**) for retromer-independent endosome-to-plasma membrane recycling of over 120 cell-surface cargoes carrying `NPxY/NxxY` motifs, including **alpha5-beta1 integrin** (`ITGA5`/`ITGB1`), **LRP1**, and **LDLR** ([PMID:28892079]; [PMID:34943955]; [PMID:37172566]).

## Key Curation & GO Annotation Decisions
- **Core MF (`ACCEPT` and `REMOVE`)**:
  - `GO:0140312` (`cargo adaptor activity`, `contributes_to`, IBA `GO_REF:0000033`): `ACCEPT` — VPS29 scaffolds the C-terminal alpha-solenoid of VPS35 (and VPS35L) and recruits TBC1D5/VARP to contribute to retromer and retriever cargo adaptor activity; represented under `contributes_to_molecular_function` in both `core_functions` entries (for `GO:0030906` `retromer, cargo-selective complex` and `GO:0160309` `commander complex`).
  - `GO:0005515` (`protein binding`): All 39 unique IPI entries in `existing_annotations` (corresponding to 40 raw `GO:0005515` IPI rows in `VPS29-goa.tsv`, where rows 19 and 68 are duplicate IntAct/`UniProtKB:Q9UBQ0` self-interaction rows) are `REMOVE` per standard GO protein-binding policy.
- **Core BP (`ACCEPT` and `MODIFY`)**:
  - `GO:0042147` (`retrograde transport, endosome to Golgi`, IBA, IEA, and NAS `PMID:26220253`): `ACCEPT`.
  - `GO:0032456` (`endocytic recycling`, IMP `PMID:28892079`, NAS `PMID:30072228`, NAS `PMID:34943955`): `ACCEPT`.
  - `NOT|involved_in GO:0010506` (`regulation of autophagy`, IMP `PMID:24603492`, `negated: true`): `ACCEPT` — `PMID:24603492` shows that TBC1D5 and the AP2 complex regulate the rerouting of ATG9-containing vesicular carriers toward sites of autophagosome formation via clathrin/AP2 and the active ULK1 complex, and the GO curator recorded a `NOT|involved_in` assertion for `VPS29`.
- **Core CC (`ACCEPT`, `MODIFY`, `NEW`, and `REMOVE`)**:
  - `GO:0030906` (`retromer, cargo-selective complex`, IDA `PMID:27385586`, IPI `PMID:11102511`, NAS `PMID:26220253`) and `GO:0030904` (`retromer complex`, IBA, IDA `PMID:11102511`, IDA `PMID:28892079`, IEA): `ACCEPT`.
  - `GO:0032991` (`protein-containing complex`, IDA `PMID:28892079` and IDA `PMID:37172566`): `MODIFY` to `GO:0160309` (`commander complex`).
  - `GO:0005768` (`endosome`), `GO:0005769` (`early endosome`), `GO:0010008` (`endosome membrane`), and `GO:0005829` (`cytosol`): `ACCEPT`.
  - `GO:0097422` (`tubular endosome`, IDA `PMID:15078903`): Proposed as `NEW` because `PMID:15078903` demonstrates that human VPS26, VPS29, and VPS35 colocalize on tubular early endosomal domains (already annotated on `VPS26A` and `VPS35` from the same paper).
  - `GO:0005737` (`cytoplasm`) and `GO:0016020` (`membrane`): `MODIFY` to `GO:0005829` (`cytosol`) and `GO:0010008` (`endosome membrane`).
  - `GO:0005770` (`late endosome`, IEA `GO_REF:0000044`): `KEEP_AS_NON_CORE` — retromer remains associated with maturing early-to-late endosomes during Rab7/TBC1D5 recruitment.
  - `GO:0005789` (`endoplasmic reticulum membrane`, NAS `PMID:34943955`): `REMOVE` with `source_defects` (`WRONG_TERM` -> `GO:0010008` `endosome membrane`) — spurious ComplexPortal NAS annotation from an endosomal Commander review article.
