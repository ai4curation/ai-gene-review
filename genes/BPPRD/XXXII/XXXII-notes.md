# Enterobacteria phage PRD1 Gene XXXII (Protein P32, UniProt: Q3T4M7) - Curation Notes

## Overview
- **Gene symbol**: `XXXII`
- **UniProt Accession**: `Q3T4M7` (`VP32_BPPRD`, Protein P32, 54 aa, 5.4 kDa)
- **Organism**: Enterobacteria phage PRD1 (`NCBITaxon:10658`)
- **Genomic / Structural Context**: Part of Cluster 2 (PRD1 DNA delivery / membrane tube apparatus). Protein P32 is a small single-pass viral inner-membrane protein (`InterPro:IPR020085`, `Pfam:PF11087`) that shares sequence similarity with PRD1 protein P34 (`gene XXXIV`) and is a component of the phage DNA injection machinery (`TCDB: 1.K.2.1.1`) [file:BPPRD/XXXII/XXXII-uniprot.txt].

## Literature & Functional Evidence
1. **UniProtKB Q3T4M7 (`file:BPPRD/XXXII/XXXII-uniprot.txt`)**:
   - **Function**: `"FUNCTION: Component of the phage injection machinery. Required for DNA injection in the membrane transformation event. Involved in the formation of the membrane tail tube to connect the virus interior with the host cytosol. Essential for viral infectivity."`
   - **Subcellular Location**: `"SUBCELLULAR LOCATION: Virion membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}. Note=Part of the capsid inner membrane."`
   - **Miscellaneous**: `"MISCELLANEOUS: PRD1 virions are composed of a tail-less icosahedral capsid of diameter 63 nm, an inner protein-lipid membrane, and a dsDNA genome which is located inside the lipid vesicle. The DNA is packaged into a preformed procapsid. The internal membrane plays an active role in DNA delivery to the host cell by forming a tubular structure used for injecting the DNA into the host cytoplasm."`
   - **Sequence & Domain Features**:
     - 54 amino acids with an N-terminal transmembrane helix (`TRANSMEM 4..24`).
     - Member of `InterPro:IPR020085` (`DNA_delivery_prot_P32/34`) and `Pfam:PF11087` (`PRD1_DD`), the conserved tectiviral P32/P34 DNA delivery membrane protein family (`TCDB: 1.K.2.1.1`).

## Review of Existing GOA Annotations
- `GO:0039641` (`viral inner membrane`, `IEA` from `GO_REF:0000120` via `InterPro:IPR020085` and `UniProtKB-KW:KW-1231`): **ACCEPT**. P32 is a single-pass integral transmembrane protein of the PRD1 capsid inner membrane.
- `GO:0046718` (`symbiont entry into host cell`, `IEA` from `GO_REF:0000043` via `UniProtKB-KW:KW-1160`/`KW-1162`): **ACCEPT**. P32 is a core component of the PRD1 DNA injection machinery required for forming the membrane tail tube that delivers the viral genome into the host cell.
- `GO:0055036` (`virion membrane`, `IEA` from `GO_REF:0000044` via `UniProtKB-SubCell:SL-0275`): **ACCEPT**. Accurately captures localization in the PRD1 virion membrane.
- **Molecular Function**: P32 is a small non-catalytic transmembrane component of the phage DNA delivery apparatus (`GO:0003674` molecular_function unknown).
