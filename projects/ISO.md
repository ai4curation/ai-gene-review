# Inferred from Sequence Orthology (ISO) Evidence Code Review

## Overview

ISO (Inferred from Sequence Orthology, ECO:0000266) is one of the most widely used
evidence codes in GO annotation, particularly for transferring annotations from
well-characterized model organisms to less-studied species. This project examines
ISO annotations in detail to assess their quality, identify systematic issues, and
develop review guidelines.

## Background

### What ISO means
ISO annotations are created when a GO term is transferred from one gene to its
ortholog in another species based on orthology relationships. The logic:
- Gene A in species 1 has experimentally validated annotation X
- Gene B in species 2 is an ortholog of Gene A
- Therefore Gene B receives annotation X with ISO evidence

### Scale and impact
- ISO is among the top evidence codes by volume in GOA
- Mouse, rat, and other model organism genes receive many ISO annotations
  transferred from human experimental data (and vice versa)
- Quality depends on: orthology call accuracy, functional conservation across
  species, and whether the specific GO term (not just broad function) is conserved

### Known concerns
1. **Over-transfer**: Broad functional conservation doesn't guarantee that specific
   GO terms transfer correctly. Paralogs may have diverged in substrate specificity,
   subcellular localization, or regulatory context.
2. **Circular evidence**: If species A annotates from species B (ISO) and species B
   annotates from species A (ISO), neither has primary experimental backing.
3. **Granularity mismatch**: A specific MF term validated in human may not apply at
   the same specificity in mouse if the gene has subtly different biochemistry.
4. **Orthology method sensitivity**: Different orthology resources (PANTHER, OMA,
   InParanoid, EggNOG) may disagree on orthology calls, especially for multi-copy
   gene families.

## Review Strategy

For each gene reviewed under this project:
1. Identify all ISO annotations
2. Trace each to its source (which ortholog, which species, what experimental evidence
   does the source have?)
3. Assess whether the specific GO term (not just the broad function) is likely
   conserved in the target species
4. Flag annotations where:
   - The source gene is a paralog, not a true ortholog
   - The GO term is too specific for confident cross-species transfer
   - The experimental evidence in the source species is itself weak
   - There's contradictory experimental evidence in the target species

## Initial Gene Targets

| Gene | Species | Why interesting |
|------|---------|-----------------|
| Calm3 | mouse | Calmodulin family — highly conserved but subtle paralog differences between Calm1/2/3 |
| | | |

## Notes

### Calmodulin family context
Calm1, Calm2, and Calm3 encode identical protein sequences in many mammals but differ
in UTR regulation, tissue expression patterns, and potentially in interaction partners.
ISO annotations that transfer from human CALM1/2/3 to mouse Calm1/2/3 should be
scrutinized for whether paralog-specific annotations are being inappropriately
transferred across the family.

## Action Items

- [ ] Review mouse Calm3 ISO annotations as initial test case
- [ ] Develop ISO-specific review criteria for the review skill
- [ ] Assess scale: how many ISO annotations exist for mouse genes in GOA?
- [ ] Compare orthology sources used for ISO transfers (PANTHER vs OMA)
- [ ] Identify systematic patterns in problematic ISO transfers
