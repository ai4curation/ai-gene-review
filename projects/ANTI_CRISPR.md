# Anti-CRISPR Proteins Project

## Overview

This project tracks the annotation review of anti-CRISPR (Acr) proteins - phage-encoded inhibitors of bacterial CRISPR-Cas immune systems. These proteins represent a fascinating example of evolutionary arms race between bacteria and their viral predators, and present unique challenges for GO annotation:

1. **Novel molecular mechanisms** - Acr proteins often have unique mechanisms not well-captured by existing GO terms
2. **Dual-targeting strategies** - Some Acrs interact with both protein and RNA components
3. **Regulatory complexity** - Expression is tightly regulated via Aca (anti-CRISPR associated) repressors
4. **Sparse annotations** - Many Acr proteins have only generic IEA annotations

These proteins are excellent targets for AI-assisted curation because their mechanisms are well-studied structurally but annotations lag behind.

**Source**: Presented at Gene Ontology Consortium Meeting, October 2025, Cambridge UK. See [ai4curation/ai-gene-review](https://github.com/ai4curation/ai-gene-review).

## Key Concepts

### Anti-CRISPR Mechanisms
- **Type I-F inhibitors** (AcrIF family) - Target Csy surveillance complex
- **Type I-E inhibitors** (AcrIE family) - Target Cascade complex
- **Type II inhibitors** (AcrIIA/IIC) - Target Cas9/Cas12
- **Type III inhibitors** - Target Csm/Cmr complexes

### Inhibition Strategies
- Blocking DNA recognition
- Preventing R-loop formation
- Mimicking DNA substrates
- Direct crRNA binding (unique mechanism)
- Enzymatic inactivation

## Featured Examples

### AcrF8 (Pectobacterium phage ZF40)

**Organism**: BPZF4 (bacteriophage)
**UniProt**: H9C181
**Status**: COMPLETE

**Key Findings**:
- 92-amino acid protein that inhibits Type I-F CRISPR-Cas system
- Unique dual-targeting mechanism: binds BOTH Cas7f protein backbone AND crRNA scaffold
- Contacts nucleotides U[+21], U[+22], G[+23] of crRNA at <4Å distance
- Blocks R-loop formation and prevents target DNA recognition
- Cryo-EM structure at 3.42Å resolution (PMID:32170016)

**Annotation Issues Identified**:
- `GO:0052170` (symbiont-mediated suppression of host innate immune response) - Too general
  - **Action**: MODIFY → `GO:0098672` (symbiont-mediated suppression of host CRISPR-cas system)
- Missing core function annotation for ribonucleoprotein complex binding

**Proposed New GO Term**:
- **Name**: CRISPR RNA binding anti-CRISPR activity
- **Justification**: Current terms don't distinguish between Acrs that only bind Cas proteins vs. those that directly contact crRNA. AcrF8 represents a unique class with dual protein-RNA binding.

## Genes for Review

### Priority 1: Structurally Characterized Acrs
| Species | Gene | CRISPR Type | Status |
|---------|------|-------------|--------|
| BPZF4 | AcrF8 | Type I-F | COMPLETE |

### Priority 2: Other Acr Families
(To be identified - AcrIF, AcrIE, AcrIIA families)

### Priority 3: Aca Regulators
(Anti-CRISPR associated proteins that regulate Acr expression)

## Key Mechanisms to Annotate

1. **Surveillance complex binding** - `GO:0043021` ribonucleoprotein complex binding
2. **CRISPR-Cas suppression** - `GO:0098672` symbiont-mediated suppression of host CRISPR-cas system
3. **DNA mimic function** - Where Acrs structurally mimic DNA
4. **crRNA binding** - Direct RNA contacts (needs new term?)

## Key References

- Bondy-Denomy J et al. (2013) Nature - Anti-CRISPR discovery
- Pawluk A et al. (2016) Cell - AcrIF mechanisms
- Wang J et al. (2020) Nat Commun - AcrF8/F9/F6 cryo-EM structures (PMID:32170016)
- Stanley SY et al. (2019) Cell - Aca repressor mechanisms (PMID:31474367)

## Related Projects

- Phage-host interactions
- Bacterial immune systems

---

# STATUS

## Completed Reviews
- [x] BPZF4/AcrF8 - Type I-F inhibitor with dual protein-RNA binding

## Pending
- [ ] Identify additional Acr proteins in UniProt/QuickGO
- [ ] Review Aca regulator annotations
- [ ] Propose new GO terms for crRNA-binding mechanisms

Last updated: 2026-01-22

# NOTES

## 2026-01-22

**Project Creation**

Created project to track anti-CRISPR protein annotations.

**AcrF8 Highlights**:
- Unique dual-targeting: binds both Cas7f protein AND crRNA directly
- Cryo-EM structure shows <4Å contacts with crRNA nucleotides
- Expression regulated by Aca2 repressor in negative feedback loop
- Proposed new GO term for crRNA-binding anti-CRISPR mechanism

The AcrF8 example demonstrates:
1. Need for more specific GO terms for CRISPR-Cas inhibition mechanisms
2. Value of structural biology in informing function annotations
3. Importance of distinguishing protein-only vs. protein+RNA binding mechanisms
