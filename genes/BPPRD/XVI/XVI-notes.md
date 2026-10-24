# Enterobacteria phage PRD1 Gene XVI (Protein P16, UniProt: P27392) - Curation Notes

## Overview
- **Gene symbol**: `XVI`
- **UniProt Accession**: `P27392` (`VP16_BPPRD`, Protein P16, 117 aa, 12.6 kDa)
- **Organism**: Enterobacteria phage PRD1 (`NCBITaxon:10658`)
- **Genomic / Structural Context**: Part of Cluster 2 (PRD1 vertex-membrane linker / DNA delivery apparatus). Protein P16 is an integral single-pass viral inner-membrane protein resolved in the atomic structure of the whole PRD1 virion (`PDB:1W8X`) that anchors the fivefold icosahedral vertex complex to the underlying internal lipid membrane [file:BPPRD/XVI/XVI-uniprot.txt].

## Literature & Functional Evidence
1. **UniProtKB P27392 (`file:BPPRD/XVI/XVI-uniprot.txt`)**:
   - **Function**: `"FUNCTION: Protein of the infection vertex complex, which increases the vertex stability. Anchors the vertex structure to the viral membrane. Essential for viral infectivity."`
   - **Subcellular Location**: `"SUBCELLULAR LOCATION: Virion membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}. Note=Part of the capsid inner membrane."`
   - **Structural & Domain Features**:
     - Contains an N-terminal transmembrane helix (`TRANSMEM 7..24`) and belongs to `Pfam:PF09301` (`DUF1970`).
     - Resolved by X-ray crystallography in the intact PRD1 virion at 4.09 Å (`PDB:1W8X`, chains M–Q, residues 34–93) and annotated in DisProt (`DP01012`), where its partially disordered/flexible periplasmic-equivalent linker region bridges the fivefold vertex (penton P31 and peripentonal major capsid protein P3 trimers) to the viral inner membrane, stabilizing the vertex and coupling vertex opening to the membrane transformation event required for infectivity [file:BPPRD/XVI/XVI-uniprot.txt].

## Review of Existing GOA Annotations
- `GO:0039641` (`viral inner membrane`, `IEA` from `UniProtKB-KW:KW-1231`): **ACCEPT**. P16 is an integral single-pass transmembrane protein (`TRANSMEM 7..24`) of the PRD1 internal membrane.
- `GO:0055036` (`virion membrane`, `IEA` from `UniProtKB-SubCell:SL-0275`): **ACCEPT**. Accurately captures localization in the virion membrane (`PDB:1W8X`, `file:BPPRD/XVI/XVI-uniprot.txt`).
- **Core Function Summary**: P16 acts as a vertex-stabilizing membrane anchor (`GO:0039641`, `GO:0055036`) that tethers the icosahedral vertex structure (`GO:0019028` viral capsid) to the internal lipid bilayer and is essential for viral infectivity (`GO:0046718` symbiont entry into host cell / vertex complex stabilization).
