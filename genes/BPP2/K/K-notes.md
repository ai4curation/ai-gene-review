# Bacteriophage P2 Gene K (Endolysin gpK; UniProt P51771)

## Overview
Gene **K** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes the 165-amino-acid endolysin gpK (18.5 kDa; `UniProt:P51771`, `EC:4.2.2.n1`, `InterPro:IPR034691`) (`PMID:8051010`, `file:BPP2/K/K-uniprot.txt`). gpK shares strong sequence homology with the phage lambda R endolysin (a soluble lytic transglycosylase that cleaves the $\beta$-1,4-glycosidic bond between N-acetylmuramic acid and N-acetylglucosamine with concomitant formation of a 1,6-anhydro-N-acetylmuramic acid ring) (`PMID:8051010`, `file:BPP2/K/K-uniprot.txt`). During the late lytic cycle, gpK accumulates in the host cell cytoplasm until the class I holin Y (`gpY`) forms membrane lesions in the inner membrane, allowing gpK to access the periplasm and degrade the peptidoglycan cell wall for host cell lysis (`PMID:8051010`, `PMID:23335412`).

## Key Literature & Experimental Evidence
- **PMID:8051010** (*Functions involved in bacteriophage P2-induced host cell lysis and identification of a new tail gene.*):
  - Mapped P2 lysis-defective amber and temperature-sensitive mutations (`ts60`, `am12`, `am76`, `am218`) to `orf21` (`gene K`): `"All of the existing lysis mutants--ts60, am12, am76, and am218--were located in orf21, which must therefore correspond to gene K. The K gene product has extensive amino acid sequence similarity to the product of gene R of bacteriophage lambda, and its exhibits endolysin function."`

## Curation Decisions
- **Molecular Function**:
  - `GO:0003796` (`lysozyme activity`, IEA) and `GO:0016829` (`lyase activity`, IEA): **ACCEPT** (lambda R / P2 K family endolysins act as peptidoglycan lytic transglycosylases, EC 4.2.2.n1).
  - `GO:0003824` (`catalytic activity`, IEA): **MODIFY** to `GO:0003796` (`lysozyme activity`) and `GO:0016829` (`lyase activity`).
- **Biological Process**:
  - `GO:0009253` (`peptidoglycan catabolic process`, IEA): **ACCEPT**
  - `GO:0044659` (`viral release from host cell by cytolysis`, IEA): **ACCEPT**
  - `GO:0031640` (`killing of cells of another organism`, IEA): **MODIFY** to `GO:0044659` (`viral release from host cell by cytolysis`).
  - `GO:0042742` (`defense response to bacterium`, IEA): **REMOVE** (false-positive mapping from `KW-0081` Bacteriolytic enzyme; phage endolysin K lyses the host bacterium to release progeny phage, not as an antibacterial immune defense response).
- **Cellular Component**:
  - `GO:0030430` (`host cell cytoplasm`, IEA): **ACCEPT** (accumulates in the host cytoplasm prior to holin Y pore formation).
