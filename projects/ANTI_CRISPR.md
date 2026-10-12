---
title: "Anti-CRISPR Proteins Project"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [BPZF4]
genes: [AcrF8, ACA2]
manifest:
  slides:
    - href: ANTI_CRISPR/slides/ANTI_CRISPR-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/RLHL9r41LvokY2PpeEuBzu
      title: Project brief
---

# Anti-CRISPR Proteins Project

**Bottom line:** anti-CRISPR (Acr) proteins are small phage proteins that switch
off bacterial CRISPR-Cas immunity, and their GO annotations lag far behind a
detailed structural literature. We reviewed two complete genes from Pectobacterium
phage ZF40: the Type I-F inhibitor AcrF8 and the dual DNA/RNA-binding Aca2
repressor that controls the `acrIF8-aca2` operon. For AcrF8, the generic IEA
term `GO:0052170` (symbiont-mediated suppression of host innate immune response) was
modified to `GO:0098672` (symbiont-mediated suppression of host CRISPR-cas system), and
`GO:0043021` ribonucleoprotein complex binding was added as its core function
from the cryo-EM structure (PMID:32170016). We also proposed a new term,
"CRISPR RNA binding anti-CRISPR activity", because AcrF8 contacts the crRNA as
well as the Cas7f backbone and no current term captures that. The Aca2 review
refined generic DNA/RNA-binding annotations into a transcriptional and
translational repressor model, with low-priority cleanup tracked in
[ai4curation/ai-gene-review#778](https://github.com/ai4curation/ai-gene-review/issues/778).
The wider Acr families (AcrIF, AcrIE, AcrIIA) remain the next review target,
and GO term curation for drafted CRISPR/anti-CRISPR terms is tracked in
[ai4curation/ai-gene-review#3966](https://github.com/ai4curation/ai-gene-review/issues/3966).

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

### Completed ZF40 reviews

| Species | Gene | Role | Status |
|---------|------|------|--------|
| BPZF4 | <gene species="BPZF4" symbol="AcrF8">AcrF8</gene> | Type I-F inhibitor with dual protein/crRNA binding | COMPLETE |
| BPZF4 | <gene species="BPZF4" symbol="ACA2">ACA2</gene> | Aca2 DNA/RNA-binding repressor of the `acrIF8-aca2` operon | COMPLETE; follow-up [#778](https://github.com/ai4curation/ai-gene-review/issues/778) |

### Next review targets

- **AcrIF / AcrIE / AcrIIA families** — expand beyond the ZF40 type I-F worked example.
- **Aca regulators beyond Aca2** — compare whether DNA and RNA repression are conserved or Aca2-specific.
- **Drafted CRISPR/anti-CRISPR GO terms** — curate the new-term requests tracked in [#3966](https://github.com/ai4curation/ai-gene-review/issues/3966).

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
- [x] BPZF4/ACA2 - Aca2 dual DNA/RNA-binding repressor

## Pending
- [ ] Identify additional Acr proteins in UniProt/QuickGO
- [ ] Resolve Aca2 cleanup in [#778](https://github.com/ai4curation/ai-gene-review/issues/778)
- [ ] Propose and curate drafted CRISPR/anti-CRISPR GO terms in [#3966](https://github.com/ai4curation/ai-gene-review/issues/3966)

Last updated: 2026-10-04

## 2026-10-04

Rechecked the project against both complete BPZF4 gene reviews. AcrF8 remains the
flagship anti-CRISPR mechanism example, and ACA2 is now listed explicitly as the
paired Aca regulator review rather than left in the pending queue.

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
