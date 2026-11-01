# Enterobacteria phage PRD1 Gene XVIII (Protein P18, UniProt: P27389) - Curation Notes

## Overview
- **Gene symbol**: `XVIII`
- **UniProt Accession**: `P27389` (`VP18_BPPRD`, Protein P18, 90 aa, 9.8 kDa)
- **Organism**: Enterobacteria phage PRD1 (`NCBITaxon:10658`)
- **Genomic / Structural Context**: Part of Cluster 2 (PRD1 DNA delivery / membrane tube apparatus). Protein P18 is an integral multi-pass viral inner-membrane protein with three transmembrane helices that is essential for the vesicle-to-tube membrane transformation and DNA injection into the host cytosol (`TCDB: 1.K.2.1.1`) [file:BPPRD/XVIII/XVIII-uniprot.txt].

## Literature & Functional Evidence
1. **UniProtKB P27389 (`file:BPPRD/XVIII/XVIII-uniprot.txt`)**:
   - **Function**: `"FUNCTION: Component of the phage injection machinery. Required for DNA injection in the membrane transformation event. Involved in the formation of the membrane tail tube to connect the virus interior with the host cytosol. Essential for viral infectivity."`
   - **Subcellular Location**: `"SUBCELLULAR LOCATION: Virion membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}. Note=Part of the capsid inner membrane."`
   - **Sequence & Topological Features**:
     - 90 amino acids containing three predicted transmembrane helices (`TRANSMEM 1..21`, `TRANSMEM 37..57`, `TRANSMEM 60..80`), making it a highly hydrophobic multi-pass integral protein of the PRD1 internal membrane.
     - Classified in TCDB `1.K.2.1.1` (Bacteriophage PRD1 DNA delivery tube complex). Mutants lacking P18 assemble DNA-filled virions but fail to transform the spherical internal membrane vesicle into the tubular tail-like conduit required for DNA delivery into the host cytoplasm [file:BPPRD/XVIII/XVIII-uniprot.txt].

## Review of Existing GOA Annotations
- `GO:0039641` (`viral inner membrane`, `IEA` from `UniProtKB-KW:KW-1231`): **ACCEPT**. P18 is a three-pass integral membrane protein of the PRD1 capsid inner membrane.
- `GO:0046718` (`symbiont entry into host cell`, `IEA` from `UniProtKB-KW:KW-1160`/`KW-1162`): **ACCEPT**. P18 is an essential component of the phage DNA injection machinery required for forming the membrane tail tube that delivers the viral genome into the host cell.
- `GO:0055036` (`virion membrane`, `IEA` from `UniProtKB-SubCell:SL-0275`): **ACCEPT**. Accurately captures localization in the PRD1 virion membrane.
- **Molecular Function**: P18 acts as a non-catalytic multi-pass membrane-remodeling component of the phage DNA delivery apparatus (`GO:0003674` molecular_function unknown).
