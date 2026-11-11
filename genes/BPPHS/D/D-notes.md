# Gene Review Notes: Enterobacteria phage phiX174 gene D (P69486)

## Overview
- **Gene symbol**: `D`
- **UniProt ID**: `P69486` (`SCAFD_BPPHS`)
- **Organism**: Enterobacteria phage phiX174 isolate Sanger (`NCBITaxon:1217068`)
- **Product**: External scaffolding protein D (gpD, 152 aa, 16.9 kDa; initiator Met removed)
- **Phage lifecycle module**: `phage_capsid_assembly.yaml` (External procapsid scaffolding and provirion-to-virion maturation)

## Biological Function & Mechanism
1. **External Scaffolding of the 108S Procapsid**:
   - External scaffolding protein D forms asymmetric dimers and tetramers (D1-D4 per icosahedral asymmetric unit; 240 copies total per particle) that bind twelve `12S` pentameric pre-assembly complexes (each containing five copies of F, five copies of G, five copies of internal scaffold B, and one copy of pilot protein H) to organize them into the T=1 icosahedral `108S` procapsid in the host cytoplasm (`file:BPPHS/D/D-uniprot.txt`, `PMID:9305849`).
   - Within the 108S procapsid, the external D lattice holds the F coat pentamers in an expanded conformation with 30-Angstrom pores at the 3-fold axes, through which viral ssDNA and protein J enter while internal scaffold B exits (`PMID:9305849`, `PMID:11991963`).
2. **Provirion Stabilization and Release During Maturation**:
   - After ssDNA and protein J are packaged and gpB is extruded, the particle forms the `132S` provirion intermediate, which still retains the 240-copy external D shell (`PMID:9305849`, `file:BPPHS/D/D-uniprot.txt`).
   - Dissociation of external scaffolding protein D triggers an 8.5-Angstrom radial collapse of the F coat proteins around the packaged genome, closing the 3-fold pores to yield the mature `114S` infectious virion (`PMID:11991963`, `file:BPPHS/D/D-uniprot.txt`).

## GO Annotation Review Summary
- **Accepted core terms**:
  - `GO:0046797` (`viral procapsid maturation`, IEA from `InterPro:IPR004196`, `InterPro:IPR036632`)
  - `GO:0030430` (`host cell cytoplasm`, IEA from `UniProtKB-SubCell:SL-0381`)
