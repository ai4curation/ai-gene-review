# Plant-Encoded Sense & Response Biosensors

Notes from SEED SFA (Secure Ecosystem Engineering and Design) at ORNL.

## Key Publication

- Yang et al., 2025. BioDesign Research. doi:10.1016/j.bidere.2025.100007
- "Utilizing plant synthetic biology to accelerate plant-microbe interactions research"

## Overview

Goal: Create plant-encoded biosensors that detect microbial presence and trigger programmable responses.

Two-part system:
1. **Upstream (Sense):** Detect microbial ligands via receptor proteins
2. **Downstream (Response):** Signal transduction leading to gene expression changes

## Receptor Classes (Sensing)

### Pattern Recognition Receptors (PRRs)
- Recognize P/MAMPs (pathogen/microbe-associated molecular patterns)
- Located on plasma membrane

### Receptor-Like Kinases (RLKs)
- Transmembrane proteins with extracellular ligand-binding and intracellular kinase domains
- Subtypes by extracellular domain:
  - **LRR** - Leucine-rich repeat
  - **LysM** - Lysin motif (chitin/peptidoglycan binding)
  - **Lec** - Lectin domain
  - **EGF** - EGF-like domain
  - **Mal** - Malectin domain
  - **SD** - S-domain

## Chitin Perception Pathway (Fungal Detection)

Image from: Mittendorf et al. 2024. New Phytologist. doi:10.1111/nph.20074

**Key insight:** Chitin perception is one of the earliest molecular events in plant response to both beneficial and pathogenic fungal colonization. A specific biosensor for chitin detection has NOT yet been developed - this is an engineering target for SEED.

### Receptor Complex
Upon chitin binding, **CERK1** and **LYK5** form a heterodimer.

| Receptor | Type | Function | Notes |
|----------|------|----------|-------|
| **CERK1** | LysM-RLK | Chitin receptor, kinase-active | Central signaling component |
| **LYK5** | LysM-RLK | High-affinity chitin binding | Kinase-inactive, co-receptor |
| **LYK4** | LysM-RLK | Chitin co-receptor | Redundant with LYK5 |

### Signaling Cascade

```
Chitin binding
     ↓
CERK1-LYK5 heterodimerization
     ↓
Phosphorylation + Ubiquitination
     ↓
  ┌──────────────────┬────────────────────┐
  ↓                  ↓                    ↓
Endocytosis      BIK1 activation    PBL27 activation
of LYK5/LYK4          ↓                    ↓
  ↓              NADPH oxidase       MAPK cascade
Vacuolar              ↓                    ↓
degradation     ROS burst        Transcriptional
                (O₂ → ROS)        reprogramming
```

### Key Signaling Components
| Gene | Function | Notes |
|------|----------|-------|
| **BIK1** | RLCK | Activates NADPH oxidase (RBOHD) |
| **PBL27** | RLCK | Activates MAPK cascade |
| **RBOHD** | NADPH oxidase | Produces ROS burst |
| **MPK3/MPK6** | MAPKs | Defense gene activation |

### Receptor Turnover
- LYK5 (and LYK4) undergo ubiquitination after activation
- Endocytosis removes receptors from membrane
- Vacuolar degradation attenuates signaling
- Important for signal dynamics and preventing over-activation

### Receptor-Like Proteins (RLPs)
- Similar to RLKs but lack intracellular kinase domain
- Require co-receptors for signaling

## Signaling Pathway Components

### Cytoplasmic Kinases
- **RLCKs** - Receptor-like cytoplasmic kinases
- **CDPKs** - Calcium-dependent protein kinases
- **MAPKs** - Mitogen-activated protein kinases

### ROS Production
- **NADPH oxidase** - Generates reactive oxygen species (ROS) burst
- ROS serves as both antimicrobial and signaling molecule

### Intracellular Receptors (NLRs)
- **TNL** - TIR-NBS-LRR proteins
- **CNL** - CC-NBS-LRR proteins
- **hNLRs** - Helper NLRs
- Recognize intracellular effectors from pathogens
- **EDS1-PAD4** complex - downstream of TNLs

## Transcriptional Outputs

### Immunity Pathways
- **PTI** - Pattern-Triggered Immunity responsive genes
- **ETI** - Effector-Triggered Immunity responsive genes
- **Hypersensitive response** - Programmed cell death at infection site

### Phytohormone Signaling
- **Salicylic acid (SA)** pathway
  - NPR1 - key regulator
  - TGA3 transcription factors
  - **PR genes** - Pathogenesis-related proteins
  - **SAR** - Systemic Acquired Resistance

### Mobile Signals
- N-HPA (N-hydroxypipecolic acid)
- MeSA (Methyl salicylate)
- Azelaic acid

## Key Genes/Proteins to Curate

### Receptors
| Gene | Type | Ligand | Notes |
|------|------|--------|-------|
| FLS2 | LRR-RLK | flagellin (flg22) | Bacterial detection |
| EFR | LRR-RLK | EF-Tu (elf18) | Bacterial detection |
| CERK1 | LysM-RLK | chitin | Fungal detection |
| LYK5 | LysM-RLK | chitin | Co-receptor with CERK1 |
| PEPR1/2 | LRR-RLK | AtPep peptides | Damage signals |
| BAK1 | LRR-RLK | multiple | Co-receptor |
| PtLecRLK1 | Lec-RLK | fungal signals | Populus - symbiosis |

### Signaling
| Gene | Function | Notes |
|------|----------|-------|
| BIK1 | RLCK | Central hub downstream of PRRs |
| MPK3/6 | MAPK | Defense gene activation |
| WRKY33 | TF | Defense transcription factor |
| NPR1 | SA receptor/coactivator | Master regulator of SAR |
| EDS1 | Lipase-like | TNL signaling |
| PAD4 | Lipase-like | TNL signaling |

### NLRs
| Gene | Type | Effector recognized | Notes |
|------|------|---------------------|-------|
| RPS2 | CNL | AvrRpt2 | Arabidopsis |
| RPM1 | CNL | AvrRpm1/AvrB | Arabidopsis |
| RPS4 | TNL | AvrRps4 | Arabidopsis |

## SEED Model Systems

### Populus (poplar trees)
- Target for bioenergy
- Model for perennial woody plants
- PtLecRLK1 - receptor for Laccaria bicolor symbiosis

### Bacillus velezensis EB14
- Plant growth-promoting bacteria (PGPB)
- Biocontrol agent against Sphaerulina musiva
- Produces antimicrobials: iturin A, subtulene A, fengycin

### Laccaria bicolor
- Ectomycorrhizal fungus
- Beneficial symbiont of Populus
- Small secreted proteins (effectors) regulate colonization

## Biosensor Engineering Strategies

1. **Reporter fusions** - Link defense promoters to fluorescent/luminescent reporters
2. **Synthetic receptors** - Engineer receptor specificity for novel ligands
3. **Orthogonal signaling** - Rewire outputs to custom responses
4. **Tunable systems** - Anti-CRISPR for controllable gene editing
5. **Split-intein biosensors** - Detect protein-protein interactions via reconstitution

## Split-Intein Based Biosensor System

From: Boone et al., 2025. Plant Biotechnology Journal. doi:10.1111/pbi.70523

### Principle
Detects protein dimerization events using split-intein mediated protein reconstitution.

### Components

| Component | Function |
|-----------|----------|
| **N-terminal GFP half** | Reporter fragment 1 |
| **C-terminal GFP half** | Reporter fragment 2 |
| **Split inteins** | Mediate protein splicing when brought together |
| **FKBP12** | Dimerization domain 1 (binds rapamycin) |
| **FRB domain** | Dimerization domain 2 (binds rapamycin) |
| **Rapamycin** | Small molecule inducer of dimerization |

### Mechanism
1. Two fusion proteins expressed:
   - FKBP12 - Intein(N) - GFP(N)
   - FRB - Intein(C) - GFP(C)
2. In absence of rapamycin: proteins separate, no GFP signal
3. Rapamycin addition: FKBP12-FRB dimerize
4. Intein halves brought into proximity → protein splicing
5. Functional GFP reconstituted → fluorescence output

### Key Proteins
| Protein | Source | UniProt | Notes |
|---------|--------|---------|-------|
| FKBP12 | Human | P62942 | FK506/rapamycin binding protein |
| FRB | Human mTOR | P42345 (residues 2015-2114) | FKBP-rapamycin binding domain |
| Split inteins | Various (Npu DnaE, Cfa, etc.) | - | Fast-splicing preferred |

### Applications
- Detect any protein-protein interaction by swapping FKBP12/FRB for proteins of interest
- Monitor receptor dimerization in plant cells
- Validate microbial effector-host protein interactions
- Chemical-inducible gene expression systems

## Chitin Biosensor (Engineered)

From: Boone et al., 2025. Plant Biotechnology Journal. doi:10.1111/pbi.70523

### Design
Applies the split-intein GFP system to detect chitin-induced CERK1-LYK5 heterodimerization.

### Fusion Constructs

| Construct | Components |
|-----------|------------|
| **LYK5 fusion** | LYK5 - Intein(N) - GFP(N-terminal half) |
| **CERK1 fusion** | CERK1^Y428F - Intein(C) - GFP(C-terminal half) |

**Note:** CERK1^Y428F is a kinase-dead mutant - prevents downstream signaling, isolates the dimerization readout.

### Mechanism

```
         LYK5                    CERK1^Y428F
           │                          │
     ┌─────┴─────┐              ┌─────┴─────┐
     │  Intein-N │              │  Intein-C │
     │  GFP-N    │              │  GFP-C    │
     └───────────┘              └───────────┘
           │                          │
           └──────── Chitin ──────────┘
                       ↓
              Heterodimerization
                       ↓
           Intein halves associate
                       ↓
         Protein trans-splicing
                       ↓
            Reconstituted GFP
                       ↓
              FLUORESCENCE
```

### Significance
- First specific biosensor for chitin detection in plants
- Enables real-time monitoring of fungal colonization
- Could distinguish beneficial (mycorrhizal) vs pathogenic fungi by timing/location
- Platform for engineering plant responses to fungal signals

## Plant RNA Vision - RNA Biosensor

From: Liu et al. (2025). Plant Biotechnology Journal. doi:10.1111/pbi.14612
**2025 R&D 100 Finalist**

DOE article: https://www.energy.gov/science/ber/articles/novel-biosensors-offer-vivo-rna-imaging-plants

### Principle
Detects specific RNA transcripts using ribozyme-mediated transcript splicing to reconstitute sfGFP.

### Genetic Design

Two expression cassettes:
```
Cassette 1: [35S]──[sfGFP Fragment 1]──[Ribozyme Fragment 1]──[Guide RNA 1]
Cassette 2: [35S]──[HSP]──[sfGFP Fragment 2]──[Ribozyme Fragment 2]──[Guide RNA 2]
```

### Components

| Component | Function |
|-----------|----------|
| **sfGFP Fragment 1** | N-terminal half of superfolder GFP |
| **sfGFP Fragment 2** | C-terminal half of superfolder GFP |
| **Ribozyme Fragment 1** | Split ribozyme (catalytic RNA) |
| **Ribozyme Fragment 2** | Split ribozyme complement |
| **Guide RNA 1** | Directs to target transcript (5' region) |
| **Guide RNA 2** | Directs to target transcript (3' region) |
| **35S** | Constitutive promoter (CaMV) |
| **HSP** | Heat shock promoter element |

### Mechanism

```
     sfGFP-1 ─ Ribozyme-1 ─ gRNA-1
                    │
                    ↓ (gRNA-1 binds target)
              ┌─────────────────┐
              │ Transcript Target│
              └─────────────────┘
                    ↑ (gRNA-2 binds target)
                    │
     sfGFP-2 ─ Ribozyme-2 ─ gRNA-2

                    ↓
        Guide RNAs bring ribozyme
        halves to same transcript
                    ↓
        Ribozyme assembly & activation
                    ↓
        Trans-splicing of sfGFP fragments
                    ↓
           Spliced sfGFP mRNA
                    ↓
            Translation → GFP
                    ↓
             FLUORESCENCE
```

### Key Features
- **RNA-level detection** - senses transcripts, not proteins
- **Programmable** - guide RNAs can be designed for any target transcript
- **Live imaging** - real-time visualization in living plant cells
- **Non-destructive** - monitor gene expression without killing tissue

### Applications
- Track pathogen-induced transcripts during infection
- Monitor plant defense gene activation
- Visualize hormone signaling responses
- Study RNA localization and dynamics in vivo

## RNA Biosensor Applications Across DOE/DARPA

The SEED RNA biosensor system is being extended to multiple projects:

### 1. DARPA Ag x BTO - Viral Detection in Crops

**Goal:** Early detection of viral infections in U.S. domestic agricultural crops

| Component | Description |
|-----------|-------------|
| Input | Viral RNA + capsid protein |
| Sensor | Genetically encoded biosensor in crop plants |
| Output | Fluorescence detectable by drone w/ hyperspectral camera |

- Remote sensing at field scale
- Early warning before visible symptoms
- Biosecurity application

### 2. DOE Center for Bioenergy Innovation (CBI) - Cell-Type Specificity

**Goal:** Tool for studying cell-type specific gene expression in plants

Design:
- Ribozyme halves + GFP^UV coding sequence
- Homology regions target specific cell-type transcripts
- 1) Complementation of homology arms to target RNA
- 2) Ribozyme splicing & translation → GFP^UV output

Enables single-cell resolution imaging of gene expression in tissues.

### 3. Plant-Microbe Interface (PMI) SFA - Drought Stress Response

**Goal:** Non-destructive measures of plant gene expression responsive to drought stress

Design:
- Agrobacterium-mediated plant transformation
- RNA biosensor construct: [UTR]─[biosensor]─[GFP^UV]
- In-vivo imaging under UV light

**Timing advantage of RNA biosensors:**

```
Time after stress onset (hours)
0     100    200    300    400    500    600    700
│      │      │      │      │      │      │      │
├──────┼──────┴──────┴──────┴──────┴──────┴──────┤ Stress sensed
│      ├────┤                                      Early signal transduction
│      ├──────────┤                                Gene expression changes ← RNA BIOSENSOR DETECTS HERE
│             ├──────────────┤                     Protein translation
│                  ├────────────────┤              Protein modification (PTMs)
│                       ├──────────────────────────┤ Phenotype (stomatal closure, leaf curl)
```

RNA biosensors detect stress ~100-200 hours earlier than visible phenotypes (stomatal closure, cuticle changes, new organs).

## Related Publications

- doi:10.1016/j.bidere.2025.100007 - Yang et al. 2025 - Plant synthetic biology for plant-microbe interactions
- doi:10.1111/pbi.70523 - Boone et al. 2025 - Split-intein biosensor for protein dimerization
- doi:10.1111/nph.20074 - Mittendorf et al. 2024 - Chitin perception pathway (New Phytologist)
- doi:10.1111/pbi.14612 - Liu et al. 2025 - Plant RNA Vision biosensor (R&D 100 Finalist)
- doi:10.1093/hr/uhae232 - Populus-Laccaria effectors
- doi:10.1093/hr/uhad087 - CRISPR/Cas9 gene activation in Populus
- doi:10.1016/j.copbio.2020.10.007 - Plant Biosystems Design Research Roadmap 1.0
- doi:10.1093/plphys/kiad076 - Anti-CRISPR for tunable editing
- doi:10.34133/2022/9863496 - Genetically Encoded Plant-Based Biosensors (GEPBs)

## TODO

- [ ] Map genes to UniProt/TAIR IDs
- [ ] Add GO annotations for pathway components
- [ ] Cross-reference with Arabidopsis defense pathway annotations
- [ ] Identify orthologs in Populus trichocarpa
