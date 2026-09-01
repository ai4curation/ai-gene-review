---
title: "PSEPK bacterial non-homologous end joining"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [ku, ligD]
autolink_gene_symbols: false
---

# PSEPK bacterial non-homologous end joining

This batch repairs the `ppu03450` pathway curation around the reusable
`modules/bacterial_nonhomologous_end_joining.yaml` module. The KEGG bucket has
two primary KT2440 genes, `ku`/PP_3255 and `ligD`/PP_3260, which satisfy the
canonical Ku-LigD bacterial NHEJ core.

## Boundary

The module contains three substantive mechanistic stages:

1. Ku-mediated recognition, protection, and alignment of double-strand-break
   ends.
2. Conditional LigD end remodeling through distinct polymerase and
   polynucleotide 3-prime-phosphatase activities.
3. ATP-dependent phosphodiester sealing by the LigD ligase domain.

The second stage is conditional rather than universally required: compatible
Ku-bound ends can proceed directly to ligation. Homologous recombination,
single-strand annealing, eukaryotic NHEJ factors, and ungrounded backup-ligase
routes are outside this module.

## Status

- [x] Repair the species-neutral module with at least two substantive parts and
  molecular functions only on leaf annotons.
- [x] Verify PTHR41251:SF1 and PTHR42705:SF2 labels and membership.
- [x] Verify PAINT nodes PTN002222140 and PTN001627042 against local IBD exports.
- [x] Apply the annotation-reviewer workflow to every GOA row for `ku` and
  `ligD`; no PENDING or UNDECIDED actions remain.
- [x] Complete OpenScientist pathway/taxon and gene research with the full
  7,200-second provider allowance.
- [x] Validate the module schema and semantics and both gene reviews.
- [x] Render all touched pages and prepare one review PR.

## Focused Genes

| Gene | Locus | UniProt | Curation | OpenScientist | Module role |
|---|---|---|---|---|---|
| `ku` | PP_3255 | Q88HU8 | CURATED | COMPLETE (1,418.41 s) | Double-stranded-DNA-end recognition and LigD recruitment |
| `ligD` | PP_3260 | Q88HU3 | CURATED | COMPLETE (905.35 s) | Conditional end processing and ATP-dependent ligation |

## Evidence Interpretation

PMID:25942369 and PMID:36475478 provide direct KT2440 genetic evidence that
loss or perturbation of `ku` or `ligD` changes mutation outcomes after
carbon starvation or programmed double-strand breaks, and implicates the LigD
PE and POL domains. The cached records do not directly assay catalytic
chemistry, so molecular-function assignments remain grounded in family
biochemistry, target domain architecture, and PAINT:

- Q88HU8 is a PTHR41251:SF1 Ku protein. PAINT node PTN002222140 carries
  GO:0003690 from experimentally characterized mycobacterial and Pseudomonas
  aeruginosa Ku seeds.
- Q88HU3 is a PTHR42705:SF2 LigD protein with the phosphoesterase, polymerase,
  and ligase domain architecture. PAINT node PTN001627042 carries GO:0003887,
  GO:0003910, and GO:0006303 from characterized LigD seeds.
- Pseudomonas aeruginosa biochemical studies provide close-family evidence for
  Ku-dependent end protection, LigD polymerase gap filling, 3-prime-phosphatase
  activity, and end sealing (PMID:15897197; PMID:20018881).

The prior broad `DNA recombination` annotation on `ligD` is modified to
GO:0006303 because bacterial NHEJ is a DNA-repair route rather than a child of
generic recombination. The old generic exonuclease implication is not promoted;
the conserved LigD phosphoesterase domain supports the more precise
polynucleotide 3-prime-phosphatase activity.

## Satisfiability Result

The module + pathway + taxon OpenScientist report completed in 1,569.3 seconds
and found every modeled role covered. No additional core gene is required.
[The full species-aware research report](../deep-research/PSEPK__bacterial_nonhomologous_end_joining__ppu03450-deep-research-openscientist.md)
records the boundary and coverage analysis.
`ku` and `ligD` occur in the same chromosomal region but are separated by four
unrelated genes, so this curation does not assert a shared operon or
co-regulation. The KT2440 gene named `ligC` (PP_2602) is an aromatic-catabolism
dehydrogenase, not an NHEJ backup ligase; it is excluded. Mycobacterial
LigC/PrimC backup routes are likewise not projected into KT2440.
