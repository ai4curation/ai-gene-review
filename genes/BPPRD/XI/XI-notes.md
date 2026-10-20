# Enterobacteria phage PRD1 Gene XI (Infectivity protein P11, UniProt: P27382) - Curation Notes

## Overview
- **Gene symbol**: `XI`
- **UniProt Accession**: `P27382` (`VP11_BPPRD`, Infectivity protein P11, 207 aa, 22.2 kDa)
- **Organism**: Enterobacteria phage PRD1 (`NCBITaxon:10658`)
- **Genomic / Structural Context**: Part of Cluster 2 (PRD1 DNA delivery / membrane tube apparatus). Protein P11 is the major viral membrane-associated infectivity protein of PRD1 and a core component of the phage DNA ejection machinery (`TCDB: 1.K.2.1.1`) [PMID:11741849, file:BPPRD/XI/XI-uniprot.txt].

## Literature & Functional Evidence
1. **UniProtKB P27382 (`file:BPPRD/XI/XI-uniprot.txt`)**:
   - **Function**: `"FUNCTION: Component of the phage ejection machinery. Pilot protein for the formation of the tube that conducts the genome into the target cell. Probably involved in penetration of the bacterial outer membrane and for making the peptidoglycan layer accessible to the viral transglycosylase. Essential for viral infectivity."`
   - **Subcellular Location**: `"SUBCELLULAR LOCATION: Virion membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}. Note=Part of the capsid inner membrane."`
   - **Sequence Features**: Single-pass transmembrane helix near the N-terminus (`TRANSMEM 13..28`) and an alpha-helical coiled-coil region (`COILED 64..95`). Classified in TCDB `1.K.2.1.1` (Bacteriophage PRD1 DNA delivery tube complex).
2. **Rydman & Bamford (2002) [PMID:11741849] — *The lytic enzyme of bacteriophage PRD1 is associated with the viral membrane***:
   - Identifies P11 as the `"major membrane-associated protein P11 of PRD1"` (used to normalize quantities of isolated PRD1-specific membrane vesicles in biochemical assays).
   - Shows that mutant phage particles lacking the major membrane-associated protein P11 exhibit decreased particle-associated muralytic activity in turbidimetric assays on chloroform-treated *E. coli* cells, consistent with P11's role in organizing the viral inner membrane and making the host peptidoglycan layer accessible to the virion muralytic machinery [PMID:11741849, file:BPPRD/XI/XI-uniprot.txt].

## Review of Existing GOA Annotations
- `GO:0039641` (`viral inner membrane`, `IEA` from `UniProtKB-KW:KW-1231`): **ACCEPT**. P11 is the major integral/membrane-associated protein of the PRD1 internal lipid membrane.
- `GO:0046718` (`symbiont entry into host cell`, `IEA` from `UniProtKB-KW:KW-1160`/`KW-1162`): **ACCEPT**. P11 is an essential pilot protein of the DNA ejection machinery that forms the tubular membrane conduit and penetrates the host outer membrane to deliver the viral genome.
- `GO:0055036` (`virion membrane`, `IDA` from `PMID:11741849` and `IEA` from `UniProtKB-SubCell:SL-0275`): **ACCEPT**. Both experimental (`PMID:11741849`) and curated subcellular location mappings confirm P11 localization in the PRD1 virion membrane.
- **Molecular Function**: P11 is a non-catalytic structural/pilot component of the membrane tail-tube ejection apparatus whose precise molecular function is not yet defined by a specific GO MF term (`GO:0003674` molecular_function unknown).
