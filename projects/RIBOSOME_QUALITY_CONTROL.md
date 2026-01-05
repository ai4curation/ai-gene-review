# Ribosome Quality Control (RQC) Project

## Overview

Ribosome Quality Control (RQC) is a surveillance pathway that detects and resolves stalled or colliding ribosomes during translation. This prevents accumulation of aberrant proteins and maintains proteostasis. The field has seen major advances 2020+ with structural and mechanistic discoveries.

## Model Species

**Primary: Homo sapiens (human)**
- Best characterized in human/mammalian systems
- Links to neurodegenerative disease (ALS, etc.)

## Core Pathway Architecture

### 1. Collision Sensors
Detect ribosome collisions:
- **ZNF598** - Ubiquitinates collided ribosomes (RPS10, RPS20)
- **EDF1** - Collision sensor, recruits GIGYF2
- **GIGYF2** - Recruits 4EHP to repress translation

### 2. Ribosome Splitting
Disassemble stalled ribosomes:
- **PELO** - Dom34 homolog, promotes subunit splitting
- **HBS1L** - GTPase, works with PELO
- **ABCE1** - ATPase that physically separates subunits

### 3. RQC Complex
Handles 60S-nascent chain complexes:
- **NEMF** - Recruits LTN1, stabilizes nascent chain
- **LTN1** - E3 ubiquitin ligase (Listerin)
- **TCF25** - RQC complex component
- **ANKZF1** - Vms1 homolog, releases stalled peptides

### 4. mRNA Decay
Targets problematic mRNAs:
- **No-go decay pathway genes**

### 5. Downstream Quality Control
- **VCP/p97** - Extracts ubiquitinated substrates
- **Proteasome** - Degrades aberrant proteins

## Candidate Genes (~15)

| Gene | UniProt | Function |
|------|---------|----------|
| ZNF598 | Q86UK7 | Collision sensor, E3 ligase |
| EDF1 | O60869 | Collision sensor |
| GIGYF2 | Q6Y7W6 | Translation repressor |
| PELO | Q9BRX2 | Ribosome rescue |
| HBS1L | Q9Y450 | GTPase for splitting |
| ABCE1 | P61221 | Ribosome splitting ATPase |
| NEMF | O00762 | RQC complex |
| LTN1 | O94822 | E3 ubiquitin ligase |
| TCF25 | Q9BQ70 | RQC complex |
| ANKZF1 | Q9H8Y5 | Peptide release |
| ASCC3 | Q8N3C0 | Helicase, collision resolution |
| ASCC2 | Q9H1I8 | ASCC complex |
| VCP | P55072 | AAA+ ATPase |

## Key Recent Discoveries (2020+)

- EDF1 as collision sensor (2020)
- ASCC complex structure and function
- Structural basis of ribosome splitting
- Links to neurodegeneration

## Disease Relevance

- ALS/neurodegeneration (C9orf72 repeat expansions cause ribosome stalling)
- NEMF mutations cause neurological disease
- Proteostasis disorders

## Project Status

- [ ] Stub - needs gene folder setup
