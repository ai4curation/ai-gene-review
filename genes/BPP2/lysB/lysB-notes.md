# Bacteriophage P2 Gene lysB (Spanin, inner membrane subunit gpLysB; UniProt P51770)

## Overview
Gene **lysB** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes the 141-amino-acid inner-membrane spanin subunit (i-spanin; 16.0 kDa; `UniProt:P51770`, `InterPro:IPR008776` / `PF05850`) (`PMID:8051010`, `file:BPP2/lysB/lysB-uniprot.txt`). Anchored in the *Escherichia coli* inner (plasma) membrane by an N-terminal transmembrane helix (residues 9–29) with its C-terminal coiled-coil periplasmic domain extending across the periplasm, LysB complexes with the outer-membrane lipoprotein spanin subunit LysC (`UniProt:Q8LTD0`, encoded by an overlapping frame within `lysB`, analogous to phage lambda Rz/Rz1) to form the two-component spanin complex that disrupts the Gram-negative outer membrane after peptidoglycan degradation by endolysin gpK (`PMID:8051010`, `file:BPP2/lysB/lysB-uniprot.txt`). An amber mutation in `lysB` delays host cell lysis (`PMID:8051010`).

## Key Literature & Experimental Evidence
- **PMID:8051010** (*Functions involved in bacteriophage P2-induced host cell lysis and identification of a new tail gene.*):
  - `"The gene products of lysA and lysB, although nonessential, appear to play a role in the correct timing of lysis, since a lysA amber mutant caused slightly accelerated lysis and a lysB amber mutant slightly delayed lysis of nonpermissive strains."`
- **UniProtKB P51770 (`file:BPP2/lysB/lysB-uniprot.txt`)**:
  - `"Component of the spanin complex that disrupts the host outer membrane and participates in cell lysis during virus exit."`

## Curation Decisions
- **Molecular Function**:
  - No specific catalytic or molecular function term applies to the non-enzymatic inner-membrane spanin subunit; `core_functions` records its biological process (`GO:0044659`) and host plasma membrane location (`GO:0020002`).
- **Biological Process**:
  - `GO:0031640` (`killing of cells of another organism`, IEA): **MODIFY** to `GO:0044659` (`viral release from host cell by cytolysis`).
  - `GO:0044659` (`viral release from host cell by cytolysis`): **NEW** supported by `PMID:8051010` and `file:BPP2/lysB/lysB-uniprot.txt`.
- **Cellular Component**:
  - `GO:0020002` (`host cell plasma membrane`, IEA): **ACCEPT**
