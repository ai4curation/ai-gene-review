# Bacteriophage lambda gene R (Endolysin / Lambda lysozyme; UniProt P03706)

## Overview
Gene `R` of *Escherichia phage lambda* (`NCBITaxon:2681611`) encodes the 158-amino-acid (~17.5 kDa) endolysin ("lambda lysozyme", EC `4.2.2.n2`), the muralytic enzyme of the late lysis cassette (`S-R-Rz-Rz1`) [PMID:4889461, PMID:6448076, PMID:9514719]. During the late lytic cycle, `R` lacks a signal peptide and accumulates harmlessly in the host cell cytoplasm until the holin S-105 triggers to form >300 nm lesions in the inner membrane, allowing `R` to escape into the periplasm and degrade the peptidoglycan (murein) sacculus [PMID:28637001].

## Catalytic Mechanism and Structure
1. **Non-Hydrolytic Peptidoglycan Lytic Transglycosylase Activity**: Although historically named "lambda lysozyme" when first purified as a 17.9 kDa basic bacteriolytic enzyme [PMID:4889461], biochemical product analysis by Taylor, Das, and van Heijenoort (`PMID:6448076`) demonstrated that `R` is **not** a hydrolytic muramidase (EC 3.2.1.17) or endopeptidase. Instead, `R` is a peptidoglycan lytic transglycosylase (`GO:0008933`) that cleaves the beta-1,4-glycosidic bond between N-acetylmuramic acid (MurNAc) and N-acetylglucosamine (GlcNAc) with concomitant intramolecular transglycosylation to form 1,6-anhydro-N-acetylmuramic acid ends without consuming a water molecule [PMID:6448076, PMID:9514719, PMID:10556513].
2. **Crystal Structure and Conformational Flexibility**: The 2.3 Å X-ray crystal structure (`PDB:1AM7`, `PDB:1D9U`, `PMID:9514719`) showed that lambda endolysin folds into two domains connected by a long alpha-helix, with the single catalytic acid residue **Glu-19** positioned at the base of a deep interdomain cleft. Chemical modification (diethylpyrocarbonate carbethoxylation) and site-directed mutagenesis of conserved histidines (`PMID:10556513`) revealed that `R` undergoes a large conformational transition between open and closed states during substrate binding and catalysis, with Asp-27 and Arg-33 stabilizing the closed conformation.

## GO Annotation Review Summary
- **Accepted Core Terms**:
  - `GO:0008933` (`peptidoglycan lytic transglycosylase activity`, IDA `PMID:9514719`, IMP `PMID:10556513`): Exact catalytic activity of `R`.
  - `GO:0009253` (`peptidoglycan catabolic process`, IEA `GO_REF:0000120`): Core biological process of murein degradation.
  - `GO:0044659` (`viral release from host cell by cytolysis`, IDA `PMID:28637001`, IDA `PMID:6448076`, IEA `GO_REF:0000120`): Core viral exit process enabled by `R`-mediated peptidoglycan degradation.
  - `GO:0030430` (`host cell cytoplasm`, IEA `GO_REF:0000044`): Where `R` is synthesized and accumulates prior to holin-mediated inner membrane permeabilization (`PMID:28637001`).
- **Modified Terms**:
  - `GO:0003796` (`lysozyme activity`, IDA `PMID:4889461`, IEA `GO_REF:0000120`): Replaced (`MODIFY`) with `GO:0008933` (`peptidoglycan lytic transglycosylase activity`), because `R` acts via a non-hydrolytic intramolecular transglycosylation mechanism (lyase EC `4.2.2.n2`) rather than hydrolytic muramidase (`GO:0003796`, EC 3.2.1.17) cleavage (`PMID:6448076`, `PMID:9514719`, `PMID:10556513`).
  - `GO:0008932` (`lytic endotransglycosylase activity`, EXP `PMID:10556513`, EXP `PMID:6448076`): Replaced (`MODIFY`) with the canonical GO term `GO:0008933` (`peptidoglycan lytic transglycosylase activity`) already experimentally annotated to `R`.
  - `GO:0003824` (`catalytic activity`, IEA `GO_REF:0000043`) and `GO:0016829` (`lyase activity`, IEA `GO_REF:0000120`): Too general; replaced (`MODIFY`) with `GO:0008933` (`peptidoglycan lytic transglycosylase activity`).
  - `GO:0031640` (`killing of cells of another organism`, IEA `GO_REF:0000043`): Too general; replaced (`MODIFY`) with `GO:0044659` (`viral release from host cell by cytolysis`).
- **Removed Terms**:
  - `GO:0042742` (`defense response to bacterium`, IEA `GO_REF:0000043` from `UniProtKB-KW:KW-0081` Bacteriolytic enzyme): False automatic keyword mapping; `R` is a bacteriophage lytic endolysin mediating virion release, not a host antibacterial defense protein.
