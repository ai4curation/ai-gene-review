# Gene Rz1 (A8CGF6 / SPAN2_BPP22) Research Notes

## Overview
- **Gene symbol**: `Rz1`
- **UniProt ID**: `A8CGF6` (`SPAN2_BPP22`)
- **Protein**: Probable spanin, outer lipoprotein subunit (o-spanin Rz1; 61 AA precursor, 6.6 kDa)
- **Organism**: *Salmonella* phage P22 (`NCBITaxon:10754`)
- **Genomic context**: Embedded within the +1 reading frame of the inner membrane spanin subunit gene `15` (`Rz`, `P13583`) in the P22 late lysis cassette [PMID:2763468, PMID:12562822, file:BPP22/Rz1/Rz1-uniprot.txt].

## Function & Architecture
- **Outer membrane lipoprotein spanin subunit (o-spanin)**: P22 Rz1 is synthesized as a 61-residue prolipoprotein with an N-terminal lipoprotein signal peptide (`SIGNAL 1..28`) that is cleaved by signal peptidase II to yield a mature 33-residue proline-rich periplasmic lipoprotein (`CHAIN 29..61`) lipid-anchored via `Cys29` (`LIPID 29`, `S-diacylglycerol cysteine` and `N-acyl-(S-diacylglycerol) cysteine`) to the inner leaflet of the *Salmonella* host outer membrane [file:BPP22/Rz1/Rz1-uniprot.txt].
- **Periplasmic spanin complex formation**: Rz1 interacts via its C-terminus with the C-terminus of the inner membrane spanin subunit gp15 (`P13583`), forming a trans-periplasmic spanin complex (`TCDB:1.M.1.1.4`) that bridges the host inner and outer membranes (`InterPro:IPR010346` `O-spanin`, `Pfam:PF06085` `Rz1`). Once endolysin gp19 degrades the peptidoglycan meshwork following holin gp13 pore formation, the gp15–Rz1 complex disrupts the host outer membrane via local membrane fusion to complete host cell lysis [file:BPP22/Rz1/Rz1-uniprot.txt].
- **Literature note**: `PMID:18621868` in the UniProt record is an environmental study on decay rates of bacteriophage P22 and *Staphylococcus aureus* on household surfaces and does not characterize the Rz1 protein.

## Existing GO Annotations Review
- `GO:0020002` (`host cell plasma membrane`, IEA via `GO_REF:0000044`, `UniProtKB-SubCell:SL-0376`): **ACCEPT**. Note that UniProt annotates `SL-0376` (`Host cell outer membrane`), which the UniProtKB-SubCell-to-GO mapping maps to `GO:0020002` (`host cell plasma membrane`, as GO lacks a separate "host cell Gram-negative outer membrane" term and `GO:0020002` is the standard host envelope membrane term used across phage o-spanins, while the mature Rz1–gp15 spanin complex bridges the host outer and inner membranes).
- `GO:0044659` (`viral release from host cell by cytolysis`, IEA via `GO_REF:0000002`, `InterPro:IPR010346`): **ACCEPT**. Core biological process of the o-spanin subunit.
- `GO:0031640` (`killing of cells of another organism`, IEA via `GO_REF:0000043`, `UniProtKB-KW:KW-0204`): **MODIFY** to `GO:0044659` (`viral release from host cell by cytolysis`), the specific descendant term already present on this gene.
