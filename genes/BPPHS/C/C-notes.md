# Gene Review Notes: Enterobacteria phage phiX174 gene C (P69172)

## Overview
- **Gene symbol**: `C`
- **UniProt ID**: `P69172` (`C_BPPHS`)
- **Organism**: Enterobacteria phage phiX174 isolate Sanger (`NCBITaxon:1217068`)
- **Product**: DNA packaging protein C (gpC, 86 aa, 10.1 kDa)
- **Phage lifecycle module**: `phage_dna_replication.yaml` and `phage_packaging_headful_cos.yaml` (Switch from Stage II dsDNA replication to Stage III packaging-coupled rolling-circle ssDNA synthesis)

## Biological Function & Mechanism
- During the transition from middle (Stage II semiconservative RF->RF) to late (Stage III RF->ssDNA) infection, protein C binds the replicative complex consisting of replicative form II (RFII) DNA, viral initiator protein A (gpA), and host E. coli Rep helicase (`file:BPPHS/C/C-uniprot.txt`).
- Binding of gpC inhibits further initiation of Stage II dsDNA synthesis (by outcompeting host SSB/polymerase progression in the absence of procapsids) and renders the gpA-Rep-RFII pre-initiation complex competent to dock onto the 108S empty procapsid (`file:BPPHS/C/C-uniprot.txt`).
- Once the 50S packaging complex forms, rolling-circle synthesis by host DNA polymerase III is directly coupled to translocation of the displaced viral (+) ssDNA strand and DNA-binding protein J into the procapsid (`file:BPPHS/C/C-uniprot.txt`).

## GO Annotation Review Summary
- **Accepted core term**:
  - `GO:0019073` (`viral DNA genome packaging`, IEA from `InterPro:IPR016407`): accurately captures the central role of gpC in coupling rolling-circle viral ssDNA synthesis to procapsid packaging.
