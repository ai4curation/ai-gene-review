# Gene Review Notes: Enterobacteria phage phiX174 gene E (P03639)

## Overview
- **Gene symbol**: `E`
- **UniProt ID**: `P03639` (`LYS_BPPHS`)
- **Organism**: Enterobacteria phage phiX174 isolate Sanger (`NCBITaxon:1217068`)
- **Product**: Lysis protein E (gpE, 91 aa, 10.6 kDa; single-pass type I membrane protein encoded completely within an alternative reading frame inside gene D)
- **Phage lifecycle module**: `phage_lysis_single_gene.yaml` (Single-gene lysis via MraY inhibition / "protein antibiotic" YES complex)

## Biological Function & Mechanism
1. **Archetypal Single-Gene Lysis ("Protein Antibiotic")**:
   - Unlike double-stranded DNA tailed phages that use a multi-gene holin-endolysin-spanin system to degrade existing peptidoglycan, phiX174 encodes a single 91-aa integral membrane protein E (in a +1 overlapping reading frame within gene D) that triggers host bacteriolysis by blocking de novo cell wall peptidoglycan biosynthesis (`PMID:10760296`, `PMID:11078734`, `PMID:37440661`).
2. **Formation of the Transmembrane YES Complex & Inhibition of Host MraY**:
   - Lysis protein E inserts into the E. coli inner (plasma) membrane via its conserved N-terminal transmembrane helix (residues 9-29, containing the essential `Pro-21` hinge; `PMID:22742425`, `file:BPPHS/E/E-uniprot.txt`).
   - As shown by the 3.5-Angstrom cryo-EM structure (`PMID:37440661`), two copies of protein E bridge a homodimer of host phospho-N-acetylmuramoyl-pentapeptide-transferase (`MraY`, `UniProtKB:P0A6W3`) and two copies of the host peptidyl-prolyl cis-trans isomerase chaperone `SlyD` (`UniProtKB:P0A9K9`) to form the heterohexameric transmembrane `YES` (`MraY2-E2-SlyD2`) complex (`PMID:37440661`, `file:BPPHS/E/E-uniprot.txt`).
   - Within the YES complex, the transmembrane helix of gpE physically obstructs the active site of MraY, preventing synthesis of lipid I (undecaprenyl-pyrophosphoryl-MurNAc-pentapeptide) and causing osmotic cytolysis of dividing host cells (`PMID:11078734`, `PMID:37440661`).

## GO Annotation Review Summary
- **Accepted core terms**:
  - `GO:0004857` (`enzyme inhibitor activity`, IEA from `InterPro:IPR007605`)
  - `GO:0020002` (`host cell plasma membrane`, IEA from `UniProtKB-SubCell:SL-0375`)
  - `GO:0039635` (`symbiont-mediated suppression of host peptidoglycan biosynthetic process`, IDA `PMID:11078734` and IGI `PMID:10760296`)
  - `GO:0039640` (`viral release via suppression of host peptidoglycan biosynthetic process`, IDA `PMID:11078734` and IDA `PMID:37440661`)
- **Broad ancestor terms marked `TOO_GENERAL`**:
  - `GO:0031640` (`killing of cells of another organism`, IEA) and `GO:0044659` (`viral release from host cell by cytolysis`, IDA `PMID:10760296` and IMP `PMID:22742425`): both are direct ancestor terms of `GO:0039640` (`viral release via suppression of host peptidoglycan biosynthetic process`), which is already present and accepted on this record.
