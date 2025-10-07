# LexA (SCO5803) Research Notes - Streptomyces coelicolor

## Gene Overview
- **UniProt ID**: O69979
- **Gene Symbol**: lexA
- **Locus**: SCO5803
- **Protein Name**: LexA repressor
- **EC Number**: 3.4.21.88 (serine-type endopeptidase activity)

## Core Functions

### Primary Function: SOS Response Regulation
LexA serves as the master repressor of the bacterial SOS response system in Streptomyces coelicolor. The SOS response is a crucial DNA damage response mechanism that helps bacteria survive genotoxic stress.

**Key Mechanism**:
1. **Normal conditions**: LexA homodimer binds to SOS boxes (16 bp palindromic sequences) in promoter regions of SOS genes, repressing their transcription
2. **DNA damage**: Single-stranded DNA activates RecA, which stimulates LexA autocatalytic cleavage
3. **Derepression**: Cleaved LexA cannot bind DNA, leading to expression of DNA repair genes
4. **Recovery**: After DNA repair, LexA levels recover and re-repress SOS genes

### Autopeptidase Activity
LexA possesses intrinsic serine-type endopeptidase activity (EC 3.4.21.88) that enables autocatalytic cleavage. This self-cleavage occurs specifically at an Ala-Gly bond within the protein, triggered by RecA interaction during DNA damage conditions.

## Structural Features
- **Size**: 234 amino acids
- **Domains**:
  - N-terminal DNA-binding domain (residues ~52-72 contain HTH motif)
  - C-terminal regulatory/catalytic domain with autopeptidase activity
- **Active Sites**:
  - Ser158 and Lys195 are critical for autocatalytic cleavage activity
  - Cleavage occurs at Ala123-Gly124 bond
- **Quaternary Structure**: Functions as homodimer

## Regulon and Target Genes
Based on studies in related Streptomyces species and S. coelicolor, the LexA regulon includes:
- **recA**: RecA recombinase (key SOS response activator)
- **lexA**: Self-regulation (negative autoregulation)
- **uvrA**: DNA excision repair protein
- **dnaE2**: Error-prone DNA polymerase
- **dinP**: DNA damage-inducible protein
- **recX**: RecA inhibitor

## Conservation Across Streptomyces
LexA shows high conservation across Streptomyces species:
- 94.8% identity with S. venezuelae
- 96.3% identity with S. griseus
- 94.2% identity with S. avermitilis
- Complete conservation of HTH DNA-binding domain

## Additional Regulatory Roles
Beyond DNA repair, LexA in Streptomyces has been implicated in:
- **Development**: Required for normal sporulation and morphological development
- **Secondary metabolism**: May influence antibiotic production
- **Chromosome supercoiling response**: Expression responds to topological stress

## Cellular Localization
LexA localizes to the nucleoid as part of protein-DNA complexes, where it binds to SOS box sequences in target gene promoters.

## Biological Significance
The LexA-mediated SOS response is essential for:
1. **DNA damage tolerance**: Enables survival under genotoxic stress
2. **Genomic stability**: Coordinates DNA repair pathways
3. **Stress adaptation**: Part of broader stress response networks
4. **Development**: Links DNA integrity to cellular differentiation

## References
- UniProt entry O69979
- PMID:35862789 (S. venezuelae LexA regulon study)
- Web search findings on Streptomyces LexA function and conservation