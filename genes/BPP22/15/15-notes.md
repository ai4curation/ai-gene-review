# Gene 15 (P13583 / SPAN1_BPP22) Research Notes

## Overview
- **Gene symbol**: `15` (synonym `Rz`)
- **UniProt ID**: `P13583` (`SPAN1_BPP22`)
- **Protein**: Spanin, inner membrane subunit (i-spanin gp15; 145 AA, 16.2 kDa)
- **Organism**: *Salmonella* phage P22 (`NCBITaxon:10754`)
- **Genomic context**: Located in the P22 late lysis cassette (`13`-`19`-`15`/`Rz1`), directly downstream of lysozyme gene `19` and containing the overlapping +1 reading frame for outer membrane lipoprotein subunit gene `Rz1` (`A8CGF6`).

## Function & Architecture
- **Inner membrane spanin subunit (i-spanin)**: P22 gp15 is the inner membrane subunit of the two-component spanin complex (`gp15`–`Rz1`) that bridges the periplasm and disrupts the *Salmonella* host outer membrane as the final step of bacteriophage-induced host cell lysis, following inner membrane permeabilization by holin gp13 and peptidoglycan degradation by endolysin gp19 [PMID:2763468, file:BPP22/15/15-uniprot.txt].
- **Cation-dependent lysis requirement and functional equivalence**: Casjens et al. (1989) identified gene `15` between genes `19` and `3`, constructed P22 gene `15` mutant alleles, and showed that gp15 is required for efficient host cell lysis in the presence of divalent cations (`Mg2+`), which stabilize the Gram-negative outer membrane lipopolysaccharide layer [PMID:2763468]. They also demonstrated sequence similarity to phage lambda `Rz` and phage T7 gene `18.5`, and showed that substituting T7 gene `18.5` for P22 gene `15` restores wild-type plating properties [PMID:2763468].
- **Topology & domain classifications**: Single-pass type II membrane protein anchored in the host cell inner membrane (`TRANSMEM 4..24`) with a short N-terminal cytoplasmic tail (`1..3`) and a coiled-coil periplasmic domain (`25..145`) that forms a disulfide-linked homodimer via Cys92 and Cys143 and binds the C-terminus of the outer membrane lipoprotein subunit Rz1 (`A8CGF6`) across the periplasm (`HAMAP:MF_04137`, `InterPro:IPR004929` `I-spanin`, `Pfam:PF03245` `Phage_lysis`, `TCDB:1.M.1.1.4`) [file:BPP22/15/15-uniprot.txt].

## Existing GO Annotations Review
- `GO:0020002` (`host cell plasma membrane`, IEA via `UniProtKB-SubCell:SL-0373`, `UniRule:UR001207013`): **ACCEPT**. Accurately captures localization of the i-spanin N-terminal transmembrane helix in the bacterial inner (plasma) membrane.
- `GO:0044659` (`viral release from host cell by cytolysis`, IEA via `InterPro:IPR004929`, `UniRule:UR001207013`): **ACCEPT**. Core biological process of the spanin complex.
- `GO:0031640` (`killing of cells of another organism`, IEA via `UniProtKB-KW:KW-0204`): **MODIFY** to `GO:0044659` (`viral release from host cell by cytolysis`), which is the specific descendant term already present on this gene.
