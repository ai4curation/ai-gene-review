# Iron-Sulfur Cluster Biogenesis Project

## Overview

Iron-sulfur (Fe-S) clusters are ancient and essential cofactors required for numerous cellular processes including electron transfer, enzyme catalysis, and gene regulation. The mitochondrial ISC assembly machinery is the primary system in eukaryotes, with cytosolic Fe-S assembly dependent on mitochondrial function.

## Model Species

**Primary: Homo sapiens (human)**
- Already reviewed HSCB in this project
- Multiple rare diseases (Friedreich's ataxia, etc.)

## Core Pathway Architecture

### 1. Mitochondrial ISC Assembly
Core machinery for de novo cluster synthesis:
- **NFS1** - Cysteine desulfurase (sulfur donor)
- **ISCU** - Scaffold protein
- **FXN** - Frataxin (iron donor/regulator)
- **LYRM4** (ISD11) - NFS1 stabilizer
- **FDXR/FDX2** - Ferredoxin reductase/ferredoxin

### 2. Cluster Transfer (Chaperone System)
Transfer from scaffold to recipients:
- **HSPA9** - Mitochondrial Hsp70
- **HSCB** - J-domain co-chaperone (already reviewed!)
- **GLRX5** - Glutaredoxin 5

### 3. [4Fe-4S] Cluster Assembly
Late-acting ISC machinery:
- **ISCA1/ISCA2** - A-type carriers
- **IBA57** - [4Fe-4S] assembly factor
- **NFU1** - Alternative scaffold
- **BOLA3** - [4Fe-4S] maturation

### 4. Mitochondrial Export
- **ABCB7** - ABC transporter (exports unknown sulfur compound)

### 5. Cytosolic Iron-Sulfur Assembly (CIA)
Cytosolic/nuclear Fe-S protein maturation:
- **CIAO1** - CIA targeting complex
- **CIAO2A/2B** - CIA factors
- **CIAO3** (NARFL) - CIA component
- **MMS19** - Late-acting factor

## Candidate Genes (~20)

| Gene | UniProt | Function |
|------|---------|----------|
| NFS1 | Q9Y697 | Cysteine desulfurase |
| ISCU | Q9H1K1 | Scaffold |
| FXN | Q16595 | Frataxin |
| LYRM4 | Q9HD34 | NFS1 partner |
| HSPA9 | P38646 | Hsp70 chaperone |
| HSCB | Q8IWL3 | Co-chaperone (reviewed) |
| GLRX5 | Q86SX6 | Glutaredoxin |
| ISCA1 | Q9BUE6 | [4Fe-4S] assembly |
| ISCA2 | Q86U28 | [4Fe-4S] assembly |
| IBA57 | Q5T440 | [4Fe-4S] factor |
| NFU1 | Q9UMS0 | Alternative scaffold |
| BOLA3 | Q53S33 | [4Fe-4S] factor |
| ABCB7 | O75027 | Mitochondrial export |
| CIAO1 | O76071 | CIA complex |
| MMS19 | Q96T76 | CIA factor |

## Disease Relevance

- Friedreich's ataxia (FXN)
- Sideroblastic anemia (GLRX5, ABCB7)
- Multiple mitochondrial dysfunctions (NFU1, BOLA3, IBA57)
- HSCB-related disease (not yet characterized)

## Project Status

- [x] HSCB reviewed
- [ ] Remaining genes need setup
