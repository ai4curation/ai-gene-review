# App - Amyloid Precursor Protein Notes

## Overview

APP is a paradigm for **regulated intramembrane proteolysis (RIP)** - a type I transmembrane protein processed by multiple secretases to generate fragments with distinct biological activities. APP biology is central to Alzheimer's disease pathogenesis.

## Dual Complexity: Splicing + Proteolysis

APP has BOTH alternative splicing AND proteolytic processing, making it more complex than POMC:

### Alternative Splice Isoforms

| Isoform | UniProt | Length | KPI Domain | Tissue |
|---------|---------|--------|------------|--------|
| APP695 | P12023-4 | 695 AA | No | Neuronal (predominant in brain) |
| APP751 | P12023-2 | 751 AA | Yes | Peripheral, some neurons |
| APP770 | P12023-1 | 770 AA | Yes + OX-2 | Peripheral, microglia |
| APP-L | P12023-3 | 733 AA | Yes | Leukocytes |

The KPI (Kunitz Protease Inhibitor) domain is encoded by exon 7 - APP695 skips this exon.

**Functional significance**:
- APP695 is the predominant neuronal form - relevant for synaptic function
- KPI-containing isoforms (751/770) may have protease inhibitor functions
- The ratio of isoforms changes in AD and with aging

### Proteolytic Cleavage Products

Two competing pathways:

**Non-amyloidogenic pathway** (alpha-secretase, ADAM10/17):
```
APP → sAPPα + C83 (α-CTF)
C83 → p3 + AICD (via gamma-secretase)
```

**Amyloidogenic pathway** (beta-secretase, BACE1):
```
APP → sAPPβ + C99 (β-CTF)
C99 → Aβ40/Aβ42 + AICD (via gamma-secretase)
```

### Cleavage Products (from UniProt)

| Product | Residues | PRO ID | Function |
|---------|----------|--------|----------|
| N-APP | 18-286 | PRO_0000000088 | DR6 binding, axon pruning |
| sAPPα | 18-687 | PRO_0000000089 | Neuroprotective, neurotrophic |
| sAPPβ | 18-671 | PRO_0000000090 | Less neurotrophic than sAPPα |
| C99 (β-CTF) | 672-770 | PRO_0000000091 | Precursor to Aβ |
| C83 (α-CTF) | 688-770 | PRO_0000000092 | Non-amyloidogenic pathway |
| **Aβ42** | 672-713 | PRO_0000000093 | **Pathogenic - aggregates in AD** |
| Aβ40 | 672-711 | PRO_0000000094 | Major Aβ species |
| p3 | 688-713/711 | - | Non-amyloidogenic fragment |
| AICD | 714/712-770 | PRO_0000000095 | Nuclear signaling (controversial) |

### Key Functional Differences

1. **sAPPα vs sAPPβ**: sAPPα is neuroprotective and neurotrophic; sAPPβ has 10-100x less activity and may be pro-apoptotic via DR6 binding

2. **Aβ40 vs Aβ42**: Aβ42 is more aggregation-prone and toxic; Aβ42/Aβ40 ratio is critical for AD pathogenesis

3. **AICD**: Proposed transcription factor that translocates to nucleus with Fe65/Tip60 - regulates genes including EGFR, p53, KAI1, GSK3B (controversial, may be artifact)

4. **N-APP**: The N-terminal fragment binds DR6 and triggers axon degeneration - relevant for developmental pruning and possibly neurodegeneration

## GO Annotation Challenges

1. **Pathway-specific functions**: "Positive regulation of neuron death" applies to Aβ, but "neuroprotection" applies to sAPPα - both from same gene

2. **Isoform specificity**: KPI-containing isoforms have protease inhibitor activity that APP695 lacks

3. **Cleavage product specificity**: Most experimental work uses specific fragments, but annotations are at gene level

4. **Full-length APP functions**:
   - Cell adhesion
   - Copper/zinc binding
   - Heparin binding
   - Synapse formation
   - Axon guidance

## Key References

- PMID:3322280 - Original mouse APP cloning
- PMID:2493250 - Alternative splicing characterization
- PMID:8510506 - Tissue-specific isoform expression

## Questions for Curation

1. How to handle annotations that clearly apply only to Aβ vs sAPP vs full-length?
2. Should we use functional_isoforms for both splice variants AND cleavage products?
3. How to handle the controversial AICD transcription factor activity?

## Source-defect re-review (2026-11-10)

An independent re-review of this gene's wrong-gene / wrong-reference source defects changed the following; where earlier notes above say otherwise, this section supersedes them.

- GO:0042802 / PMID:23986251: defect retyped (evidence depth: FULL_TEXT). PMC full text (PMC3756761, read through a web fetch of the first 100k characters, not cached) shows immunoblots of SDS-stable Abeta dimers/trimers from 7PA2 cells, so the paper does bear on identical protein binding and the reference is correctly keyed. The ISO donor, however, is O35463, an unreviewed Chinese hamster APP fragment, while 7PA2 cells are CHO cells expressing human APP V717F. Retyped to WRONG_WITH_FROM (slot With/From, asserted O35463, candidate P05067 verified, CHECK, cause OTHER); the defect stays on the same annotation.
