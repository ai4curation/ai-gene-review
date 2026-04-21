# VCP/p97 (P55072) Bioinformatics Analysis Results

## Checklist

- [x] None of the scripts use hardcoded inputs or outputs (all take CLI arguments)
- [x] Scripts tested on another input (NSF/P46459, a related type II AAA+ ATPase)
- [x] Analyses completed as expected
- [x] Direct results of the scripts are in `results/` directory
- [?] Conservation analysis uses pairwise alignment rather than full MSA (MUSCLE/MAFFT not available); this approximation may underestimate conservation in gapped regions
- [?] Arabidopsis CDC48A (682 aa) and Gallus VCP (573 aa) sequences from UniProt appear truncated, which may skew conservation estimates downward
- [x] Summary includes detailed provenance and justification

## Overview

VCP (Valosin-Containing Protein, also known as p97 or CDC48 in yeast) is a type II AAA+
ATPase (EC 3.6.4.6) that forms a homohexameric ring and functions as a ubiquitin-selective
segregase. It extracts ubiquitinated proteins from membranes, chromatin, and protein
complexes for proteasomal degradation or other downstream processing. This analysis
examines its domain architecture, functional motifs, evolutionary conservation, disease
mutation distribution, and cofactor binding interfaces.

## 1. Domain Architecture and Functional Motifs

**Script**: `analyze_domains.py`
**Results**: `results/VCP_motifs.tsv`, `results/VCP_domains.tsv`, `results/VCP_key_residues.tsv`

### Identified Domains

| Domain | Start | End | Size (aa) | Evidence |
|--------|-------|-----|-----------|----------|
| N-domain | 1 | 195 | 195 | Inferred from Walker A position in D1 |
| D1-ATPase | 205 | 488 | 284 | Walker A at 245-252 |
| D2-ATPase | 488 | 788 | 301 | Walker A at 518-525 |
| C-tail | 789 | 806 | 18 | Region after D2 ATPase domain |

These boundaries are consistent with the known structure (PDB: 5FTK, 5B6C, etc.) and UniProt
annotations. The N-domain boundary at ~195 matches the known N-D1 linker region (aa 187-209).

### Walker A/B Motifs

| Motif | Domain | Positions | Sequence | Notes |
|-------|--------|-----------|----------|-------|
| Walker A (P-loop) | D1 | 245-252 | GPPGTGKT | ATP binding; UniProt annotates binding at 247-253 |
| Walker A (P-loop) | D2 | 518-525 | GPPGCGKT | ATP binding; UniProt annotates binding at 521-526 |
| Walker B | D1 | 300-305 | IIFIDE | Contains catalytic D304/E305 |
| Walker B | D2 | 573-578 | VLFFDE | Contains catalytic D577/E578 |

### Key Catalytic Residues

| Residue | Domain | Role | Functional Importance |
|---------|--------|------|----------------------|
| K251 | D1 | Walker A lysine | Essential for ATP binding. K251Q mutation impairs ERAD (UniProt MUTAGEN) |
| K524 | D2 | Walker A lysine | Essential for ATP binding. K524A impairs RNF19A activity (UniProt MUTAGEN) |
| E305 | D1 | Walker B glutamate | Catalytic base. E305Q + E578Q double mutant traps ATP-bound state |
| E578 | D2 | Walker B glutamate | Main catalytic base for ATP hydrolysis. E578Q increases CAV1/UBXN6 binding, impairs autophagy |

The D2 domain is the primary catalytic ATPase. E578Q is the well-characterized "substrate trap"
mutation that locks VCP in an ATP-bound, high-affinity state for substrates.

## 2. Conservation Across CDC48/p97 Family

**Scripts**: `fetch_orthologs.py`, `analyze_conservation.py`
**Results**: `results/VCP_pairwise_identity.tsv`, `results/VCP_conservation.tsv`, `results/VCP_motif_conservation.tsv`

### Pairwise Identity to Human VCP

| Ortholog | Species | Identity |
|----------|---------|----------|
| Q01853 (Vcp) | Mus musculus | 100.0% |
| Q7ZU99 (vcp) | Danio rerio | 96.8% |
| Q7KN62 (TER94) | Drosophila melanogaster | 84.4% |
| P54811 (cdc-48.1) | Caenorhabditis elegans | 80.2% |
| Q9P3A7 (cdc48) | Schizosaccharomyces pombe | 73.5% |
| P25694 (CDC48) | Saccharomyces cerevisiae | 72.0% |
| Q5ZL72 (VCP) | Gallus gallus | 46.2% (partial sequence, 573 aa) |
| Q9SZJ3 (CDC48A) | Arabidopsis thaliana | 44.4% (partial sequence, 682 aa) |

VCP is extraordinarily conserved across eukaryotes. The 72% identity to S. cerevisiae CDC48
over ~800 aa (spanning >1 billion years of divergence) is among the highest conservation
levels observed for any eukaryotic protein, reflecting its essential and fundamental cellular
role.

**Caveat**: The pairwise identity was computed using Biopython's global PairwiseAligner
(scoring: match=2, mismatch=-1, gap_open=-3, gap_extend=-0.5). The Gallus and Arabidopsis
sequences appear truncated in UniProt, leading to artificially lower identity values.

### Conservation at Functional Motifs

| Motif | Domain | Sequence | Mean Conservation | Fully Conserved (>90%) |
|-------|--------|----------|-------------------|------------------------|
| Walker A | D1 | GPPGTGKT | 0.893 | No |
| Walker A | D2 | GPPGCGKT | 0.812 | No |
| Walker B | D1 | IIFIDE | 0.905 | No |
| Walker B | D2 | VLFFDE | 0.897 | No |

All Walker A/B motifs show high conservation (81-90%), consistent with their essential
catalytic roles. The slightly lower D2 Walker A conservation (0.812) may reflect the
inclusion of partial sequences that do not extend fully into the D2 domain.

### Overall Conservation Profile

- Mean conservation across all 806 positions: 0.778
- Positions with >90% conservation: 193/806 (24.0%)
- Positions with 100% conservation (identical in all orthologs): 193/806 (24.0%)

## 3. Disease Mutation Clustering

**Script**: `analyze_disease_mutations.py`
**Results**: `results/VCP_mutations.tsv`, `results/VCP_mutation_summary.tsv`

### Mutation Distribution by Domain

| Domain | Size (aa) | Disease Mutations | Density (per 100 aa) |
|--------|-----------|-------------------|---------------------|
| N-domain | 195 | 13 | 6.67 |
| N-D1 linker | ~10 | 1 | ~10 |
| D1-ATPase | 284 | 4 | 1.41 |
| D2-ATPase | 301 | 1 | 0.33 |
| C-tail | 18 | 0 | 0.00 |

**Key finding**: Disease mutations are heavily concentrated in the N-domain (68% of all
mutations, density 6.67 per 100 aa) and the N-D1 interface region. This is consistent
with the well-established observation that IBMPFD/MSP1 mutations cluster at the interface
between the N-domain and D1 ATPase ring, disrupting the conformational communication
between these domains.

### Hotspot Residues

- **R155**: The most frequently mutated position, with 5 different amino acid substitutions
  (C, H, L, P, S) all causing IBMPFD1. R155 is conserved at 85.7% across orthologs.
  R155H shows increased ATPase activity and impaired autophagy.

- **R159**: Mutated to G (FTDALS6) or H (IBMPFD1). Conserved at 87.5%.

- **R191**: Mutated to Q in IBMPFD1/FTDALS6. Fully conserved (100%) across all orthologs
  examined, indicating strong functional constraint. Mutations at this position abolish
  K315 methylation by ASPSCR1.

### Disease Associations

- **IBMPFD1** (Inclusion Body Myopathy with Paget Disease and Frontotemporal Dementia):
  16 of 19 variants. Predominantly N-domain and N-D1 interface.
- **FTDALS6** (Frontotemporal Dementia and/or ALS): 3 variants spanning N-domain (R159G,
  R191Q) and D2 (D592N).
- **CMT2Y** (Charcot-Marie-Tooth Type 2Y): 2 variants in N-domain (G97E, E185K).

### Conservation at Disease Sites

Mean conservation at disease mutation positions: 0.747 (compared to genome-wide mean of 0.778).
The disease sites are somewhat less conserved than average, which is surprising but may reflect
that the N-domain, where most mutations cluster, has both conserved structural residues and
more variable surface residues involved in cofactor binding specificity.

Notably, the most pathogenic mutations (R155, R159, R191) affect positions with above-average
conservation (0.857, 0.875, and 1.000 respectively), consistent with disruption of conserved
structural contacts.

## 4. Cofactor Binding Interfaces

**Script**: `analyze_cofactor_interfaces.py`
**Results**: `results/VCP_cofactor_interfaces.tsv`, `results/VCP_interface_summary.tsv`

### Interface Mapping from Mutagenesis Data

| Domain | Cofactors Identified | Mutagenesis Sites |
|--------|---------------------|-------------------|
| N-domain | DERL1, NPLOC4 | 7 |
| D1-ATPase | RHBDD1, VCPKMT | 9 |
| D2-ATPase | CAV1, RHBDD1, RNF19A, SOD1, UBXN6, ZFAND1 | 2 |

### N-domain Cofactor Interfaces

**NPLOC4 (Npl4) binding**: Residues 52-55 (FRGD motif) and Y110 are critical. FRGD->ARGA
combined with Y110A abolishes NPLOC4 interaction. The UFD1-NPLOC4 heterodimer is the
primary cofactor complex that recruits VCP to ubiquitinated ERAD substrates.

**DERL1 (Derlin-1) binding**: Multiple N-domain residues contribute: R113-H115, F131,
L140, H183. These map to a surface patch on the N-domain that contacts the ER membrane
retrotranslocation channel. D179 does not affect DERL1 binding, providing a negative
control.

### D1 Domain Interfaces

**VCPKMT (VCP lysine methyltransferase)**: K315 is the methylation site. K315L/Q/R
abolishes methylation, while neighboring residues (K312, R313, E314, T316, H317, G318)
are dispensable. IBMPFD mutations R95G, R159H, and R191Q (in the N-domain) abolish
K315 methylation enhancement by ASPSCR1, connecting disease pathology to post-translational
modification.

### D2 Domain and C-tail Interfaces

**E578Q (Walker B mutant)**: This substrate-trap mutation increases interaction with CAV1,
UBXN6, and ZFAND1 while impairing autophagy. This demonstrates that the ATP hydrolysis
cycle in D2 is directly coupled to cofactor release.

**PIM motif (aa 802-806)**: The C-terminal PIM motif mediates binding to PUL domain-
containing cofactors (PLAA/UBXN6). The C-terminal region (797-806) is the documented
UBXN6 interaction site.

### Disease Mutations and Cofactor Interfaces

The overlap between IBMPFD mutation sites and cofactor binding interfaces is notable:
- R95G (N-domain): Decreased interaction with CAV1 and UBXN6
- R155H (N-domain): Decreased interaction with CAV1 and UBXN6
- A232E (N-D1 interface): Decreased interaction with CAV1 and UBXN6
- R159H, R191Q (N-domain): Abolish ASPSCR1-mediated K315 methylation enhancement

This pattern supports the model that IBMPFD mutations disrupt the N-domain conformational
cycle, which in turn affects cofactor recruitment and release kinetics.

## Methods and Provenance

### Tools and Versions
- Python 3.x with Biopython for sequence parsing and pairwise alignment
- Regex-based motif scanning for Walker A (GxxxxGK[TS]) and Walker B ([VILMF]{4}DE) motifs
- UniProt REST API for ortholog sequence retrieval
- UniProt flat file parsing for variant and mutagenesis annotations

### Data Sources
- Human VCP sequence: UniProt P55072 (entry version 248, 2026-01-28)
- Ortholog sequences: UniProt REST API (Q01853, P25694, Q9P3A7, Q7KN62, P54811, Q9SZJ3, Q5ZL72, Q7ZU99)
- Disease variants and mutagenesis data: UniProt P55072 flat file FT annotations

### Limitations
1. Conservation analysis uses pairwise alignment rather than full MSA. A proper MUSCLE or MAFFT
   alignment would provide more accurate column-wise conservation scores, especially in
   regions with insertions/deletions.
2. Two ortholog sequences (Gallus gallus and Arabidopsis thaliana) appear truncated in UniProt,
   which reduces the effective number of orthologs for conservation calculations at C-terminal
   positions.
3. The disease mutation analysis is limited to variants annotated in UniProt. ClinVar and HGMD
   may contain additional pathogenic variants not included here.
4. Cofactor interface mapping is based solely on mutagenesis data in the UniProt flat file.
   Structural analysis of co-crystal structures (e.g., PDB 5B6C for VCP-NPLOC4) would provide
   more comprehensive interface residue identification.

### Reproducibility
All scripts accept command-line arguments and can be rerun via:
```bash
just run-vcp
```
Individual steps can also be run independently -- see the `justfile` for recipes.
Scripts were validated on human NSF (P46459), another type II AAA+ ATPase, confirming
that the Walker A/B detection and domain assignment logic generalizes correctly.
