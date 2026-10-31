# Enterobacteria phage PRD1 Gene XV (Endolysin P15, UniProt: P13559) - Curation Notes

## Overview
- **Gene symbol**: `XV`
- **UniProt Accession**: `P13559` (`ENLYS_BPPRD`, Endolysin P15, 149 aa, 17.3 kDa, EC `3.2.1.17`)
- **Organism**: Enterobacteria phage PRD1 (`NCBITaxon:10658`)
- **Genomic / Structural Context**: Part of Cluster 2 (PRD1 host lysis and virion-associated muralytic enzymes). Endolysin P15 is a soluble 1,4-beta-N-acetylmuramidase (`Pfam:PF11860`, `InterPro:IPR024408`, `InterPro:IPR016284`, `PIRSF:PIRSF001069`) that functions both as the canonical phage endolysin—degrading host peptidoglycan after cytoplasmic membrane permeabilization by holin P35 (`gene XXXV`) to lyse the host cell and release progeny virions—and as a peripheral structural component of the PRD1 virion inner membrane (anchored via small integral membrane proteins P20 and P22) [PMID:7925454, PMID:11741849, PMID:16030234, file:BPPRD/XV/XV-uniprot.txt].

## Literature & Functional Evidence
1. **Caldentey, Hänninen & Bamford (1994) [PMID:7925454] — *Gene XV of bacteriophage PRD1 encodes a lytic enzyme with muramidase activity***:
   - Cloned PRD1 gene `XV` into an expression plasmid and purified protein P15 to near homogeneity.
   - Showed that purified P15 displays strong lytic activity against chloroform-treated Gram-negative cells (pH optimum 7.0–8.0) and analyzed cell wall digests to prove that P15 is a glycosidase that hydrolyzes the beta-(1->4) linkage between N-acetylmuramic acid (MurNAc) and N-acetylglucosamine (GlcNAc), thus exhibiting beta-N-acetylmuramidase (lysozyme, `EC:3.2.1.17`) activity [PMID:7925454].
2. **Rydman & Bamford (2000) [PMID:10931330] — *Bacteriophage PRD1 DNA entry uses a viral membrane-associated transglycosylase activity***:
   - Used zymograms of wild-type and mutant PRD1 particles to distinguish the two virion-associated muralytic activities: transglycosylase P7 (`gene VII`) and the faster-migrating ~17.3 kDa muramidase P15 (`gene XV`) [PMID:10931330, PMID:11741849].
3. **Rydman & Bamford (2002) [PMID:11741849] — *The lytic enzyme of bacteriophage PRD1 is associated with the viral membrane***:
   - Demonstrated that soluble beta-1,4-N-acetylmuramidase P15 is also a structural component of the PRD1 virion associated with the internal viral membrane (`GO:0055036`).
   - Showed that small integral membrane proteins P20 and P22 modulate the incorporation of P15 into the virion (P15 is absent in P20-deficient `sus30` particles and reduced in P22-deficient `sus42` particles) [PMID:11741849].
   - Showed that in zymograms P15 degrades peptidoglycan from both Gram-negative (*E. coli*) and Gram-positive (*Micrococcus lysodeikticus*) bacteria.
   - Showed that amber mutations in gene `XV` (`sus174`, `sus232`, `sus240`) have a polar effect reducing receptor-binding protein P2 (translated from the same mRNA), and when P2 is complemented in *trans* (`P2+ P15-`), adsorption is wild-type and initiation of DNA replication is not delayed in `P2R P15-` particles, indicating P7 is the primary entry muralytic enzyme while P15's primary essential role is host cell lysis [PMID:11741849].
4. **Ziedaite et al. (2005) [PMID:16030234] — *The Holin protein of bacteriophage PRD1 forms a pore for small-molecule and endolysin translocation***:
   - Demonstrated using both PRD1 nonsense mutants (`sus232` in gene `XV` and `sus715` in holin gene `XXXV`) and co-expressed plasmid constructs (`pMG118` encoding P15 and `pGZ9` encoding holin P35) that PRD1 utilizes a canonical two-component holin-endolysin lysis system (`GO:0044659`).
   - Expression of P15 alone does not cause K+ leakage, membrane depolarization, or cell lysis; co-expression with holin P35 allows P15 translocation across the cytoplasmic membrane to digest peptidoglycan and lyse the host cell [PMID:16030234].

## Review of Existing GOA Annotations
- `GO:0003796` (`lysozyme activity`, `EXP` from `PMID:11741849`, `IDA` from `PMID:10931330`, `IDA` from `PMID:7925454`, `IEA` from `EC:3.2.1.17`) & `GO:0033922` (`peptidoglycan beta-N-acetylmuramidase activity`, `IDA` from `PMID:7925454`): **ACCEPT**. Directly supported by biochemical characterization of purified P15 and zymogram/turbidimetric assays (`PMID:7925454`, `PMID:10931330`, `PMID:11741849`).
- `GO:0003824` (`catalytic activity`, `IEA` from `UniProtKB-KW:KW-0081`), `GO:0016787` (`hydrolase activity`, `IEA` from `UniProtKB-KW:KW-0378`), and `GO:0016798` (`hydrolase activity, acting on glycosyl bonds`, `IEA` from `UniProtKB-KW:KW-0326`): **TOO_GENERAL**. All three are broad ancestor MF terms subsumed by `GO:0003796` and `GO:0033922`.
- `GO:0044659` (`viral release from host cell by cytolysis`, `IDA` from `PMID:16030234` and `IEA` from `InterPro:IPR016284`) & `GO:0044277` (`cell wall disassembly`, `IDA` from `PMID:7925454`): **ACCEPT**. Core biological processes of endolysin P15.
- `GO:0031640` (`killing of cells of another organism`, `IEA` from `UniProtKB-KW:KW-0081`/`KW-0204`): **TOO_GENERAL**. Subsumed by the more specific child term `GO:0044659` (`viral release from host cell by cytolysis`).
- `GO:0042742` (`defense response to bacterium`, `IEA` from `UniProtKB-KW:KW-0081`): **REMOVE**. False automated keyword mapping from `KW-0081` (Bacteriolytic enzyme); P15 is a bacteriophage endolysin that lyses the bacterial host for progeny release, not a host antibacterial defense protein.
- `GO:0055036` (`virion membrane`, `IDA` from `PMID:11741849` and `IEA` from `UniProtKB-SubCell:SL-0275`): **ACCEPT**. Experimentally demonstrated peripheral association of P15 with the PRD1 internal virion membrane via P20 and P22 (`PMID:11741849`).
