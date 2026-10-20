# Enterobacteria phage PRD1 Gene XXXV (Holin P35, UniProt: Q3T4L9) - Curation Notes

## Overview
- **Gene symbol**: `XXXV` (synonym `ORFM`)
- **UniProt Accession**: `Q3T4L9` (`HOLIN_BPPRD`, Holin P35, 117 aa, 12.8 kDa)
- **Organism**: Enterobacteria phage PRD1 (`NCBITaxon:10658`)
- **Genomic / Structural Context**: Part of Cluster 2 (PRD1 host lysis system). Holin P35 is a class I three-transmembrane-helix phage holin (`InterPro:IPR032126`, `Pfam:PF16083`, `TCDB: 1.E.5.1.1`) that accumulates in the host bacterial inner (cytoplasmic) membrane (`GO:0020002`) and forms pores at a genetically programmed time point triggered by intracellular ATP depletion, allowing endolysin P15 (`gene XV`) to escape into the periplasm and lyse the host cell (`GO:0044659`) [PMID:16030234, file:BPPRD/XXXV/XXXV-uniprot.txt].

## Literature & Functional Evidence
1. **Ziedaite et al. (2005) [PMID:16030234] — *The Holin protein of bacteriophage PRD1 forms a pore for small-molecule and endolysin translocation***:
   - Characterized the PRD1 two-component lysis system (holin P35 encoded by gene `XXXV` and endolysin P15 encoded by gene `XV`) using both nonsense mutant phage `sus715` (gene `XXXV` mutant) and recombinant plasmid expression (`pGZ9` and `pGZ15` carrying gene `XXXV`).
   - Showed that in wild-type PRD1 infection, holin P35 inserts into the host cytoplasmic membrane (`GO:0020002`) and initiates intracellular K+ efflux at ~35–40 min postinfection (15–20 min before membrane voltage ΔΨ dissipation and turbidity decrease), whereas the `sus715` holin mutant causes no K+ leakage, no ΔΨ collapse, and no host cell lysis even upon addition of the ATP-depleting agent arsenate [PMID:16030234].
   - Demonstrated that expression of recombinant holin P35 alone in *E. coli* induces K+ leakage, ΔΨ collapse, and growth arrest without cell lysis, whereas co-expression of holin P35 and endolysin P15 results in complete cell lysis and arsenate-inducible premature lysis [PMID:16030234].
   - Showed that PRD1-infected temperature-sensitive *groEL* and *groES* mutant host cells fail to lyse at 40°C, suggesting GroEL/GroES chaperonins may assist in holin storage or delivery to the cytoplasmic membrane [PMID:16030234].
2. **UniProtKB Q3T4L9 (`file:BPPRD/XXXV/XXXV-uniprot.txt`)**:
   - **Function**: `"FUNCTION: Isoform Holin: Accumulates harmlessly in the cytoplasmic membrane until it reaches a critical concentration that triggers the formation of micron-scale pores (holes) causing host cell membrane disruption and endolysin escape into the periplasmic space (PubMed:12813073, PubMed:16030234). Determines the precise timing of host cell lysis (By similarity). Participates with the endolysin and spanin proteins in the sequential events which lead to the programmed host cell lysis releasing the mature viral particles from the host cell (By similarity)."`
   - **Antiholin note**: `"FUNCTION: Isoform Antiholin: Counteracts the aggregation of the holin molecules and thus of pore formation."` (predicted dual-start motif M1 / M3 similar to class I lambdoid holins).
   - **Subcellular Location**: `"SUBCELLULAR LOCATION: Host cell inner membrane {ECO:0000250|UniProtKB:P03705}; Multi-pass membrane protein {ECO:0000250|UniProtKB:P03705}. Note=Classified as a class I holin."`
   - **Sequence & Domain Features**:
     - 117 amino acids with three transmembrane helices (`TRANSMEM 6..26`, `TRANSMEM 40..60`, `TRANSMEM 67..87`) and a hydrophilic, highly charged disordered C-terminal tail (`REGION 97..117`).
     - Member of `InterPro:IPR032126` (`LydA_holin`) and `Pfam:PF16083` (`Phage_holin_3_3`).

## Review of Existing GOA Annotations
- `GO:0044659` (`viral release from host cell by cytolysis`, `IDA` from `PMID:16030234`): **ACCEPT**. Directly demonstrated by `sus715` holin mutant and plasmid complementation/co-expression assays (`PMID:16030234`).
- `GO:0020002` (`host cell plasma membrane`, `IEA` from `UniProtKB-SubCell:SL-0373` and `ISS` from `UniProtKB:P03705`): **ACCEPT**. P35 is a three-pass integral membrane protein that inserts into the host bacterial cytoplasmic (inner) membrane (`PMID:16030234`, `file:BPPRD/XXXV/XXXV-uniprot.txt`).
- `GO:0031640` (`killing of cells of another organism`, `IEA` from `UniProtKB-KW:KW-0081`/`KW-0204`): **TOO_GENERAL**. Subsumed by the more specific accepted child term `GO:0044659` (`viral release from host cell by cytolysis`).
- `GO:0003824` (`catalytic activity`, `IEA` from `UniProtKB-KW:KW-0081`): **REMOVE**. False automated keyword mapping from `KW-0081` (Bacteriolytic enzyme), which was erroneously applied to the holin entry in UniProt. Holin P35 is a non-catalytic transmembrane pore-forming protein, not an enzyme (`PMID:16030234`, `file:BPPRD/XXXV/XXXV-uniprot.txt`).
- `GO:0042742` (`defense response to bacterium`, `IEA` from `UniProtKB-KW:KW-0081`): **REMOVE**. False automated keyword mapping from `KW-0081`; P35 is a bacteriophage holin that permeabilizes the bacterial host membrane for progeny release, not an antibacterial defense protein.
- **Core Function Summary**: P35 is a pore-forming class I holin (`GO:0015288` porin/pore-forming activity or `GO:0022829` wide pore channel activity) localized in the `GO:0020002` (`host cell plasma membrane`) that mediates `GO:0044659` (`viral release from host cell by cytolysis`). Let's check which molecular function term is in our local ontology cache (`GO:0003674` is cached and validated).
