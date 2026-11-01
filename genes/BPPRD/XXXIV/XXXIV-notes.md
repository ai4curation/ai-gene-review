# Enterobacteria phage PRD1 Gene XXXIV (Protein P34, UniProt: P27390) - Curation Notes

## Overview
- **Gene symbol**: `XXXIV` (synonym `ORFO`)
- **UniProt Accession**: `P27390` (`VP34_BPPRD`, Protein P34, 68 aa, 6.8 kDa)
- **Organism**: Enterobacteria phage PRD1 (`NCBITaxon:10658`)
- **Genomic / Structural Context**: Part of Cluster 2 (PRD1 DNA delivery / membrane tube apparatus). Protein P34 is a small two-pass integral viral inner-membrane protein (`InterPro:IPR020085`, `Pfam:PF11087`) paralogous in its N-terminal domain to PRD1 DNA delivery protein P32 (`gene XXXII`) [file:BPPRD/XXXIV/XXXIV-uniprot.txt].

## Literature & Functional Evidence
1. **UniProtKB P27390 (`file:BPPRD/XXXIV/XXXIV-uniprot.txt`)**:
   - **Subcellular Location**: `"SUBCELLULAR LOCATION: Virion membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}. Note=Part of the capsid inner membrane."`
   - **Sequence & Domain Features**:
     - 68 amino acids containing two predicted transmembrane helices (`TRANSMEM 4..24` and `TRANSMEM 41..61`).
     - Member of `InterPro:IPR020085` (`DNA_delivery_prot_P32/34`) and `Pfam:PF11087` (`PRD1_DD`, residues 1–46), the conserved tectiviral P32/P34 DNA delivery membrane protein family.

## Review of Existing GOA Annotations
- `GO:0039641` (`viral inner membrane`, `IEA` from `GO_REF:0000120` via `InterPro:IPR020085` and `UniProtKB-KW:KW-1231`): **ACCEPT**. P34 is a two-pass integral membrane protein of the PRD1 capsid inner membrane.
- `GO:0055036` (`virion membrane`, `IEA` from `GO_REF:0000044` via `UniProtKB-SubCell:SL-0275`): **ACCEPT**. Accurately captures localization in the PRD1 virion membrane.
- **Core Function Summary**: P34 is an integral multi-pass protein of the PRD1 viral inner membrane (`GO:0039641`, `GO:0055036`) belonging to the P32/P34 DNA delivery protein family (`InterPro:IPR020085`, `Pfam:PF11087`); its exact molecular function and specific biological process role remain to be directly characterized (`GO:0003674` molecular_function unknown).
