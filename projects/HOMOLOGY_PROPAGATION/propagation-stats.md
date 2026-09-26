---
title: "Homology Propagation Statistics"
---
# Homology Propagation Statistics

Generated 2026-09-26 by `just propagation-stats` from the cached GOA
files under `genes/` (donor cache refreshed 2026-09-26).
Counts cover every gene with a cached GOA file. The unit is one annotation
(gene, term, evidence, reference, negation): pipelines that emit one GOA line
per donor, or split one annotation across qualifiers, are merged
(35,045 GOA lines → 34,265 annotations).
*Reviewed* annotations are those matched to an `existing_annotations` entry
with a final review action.
These numbers are regenerated; do not copy them into project prose.
Browse the rows in the [propagation browser](../../app/propagation/index.html).

## All propagation methods

| Method | Annotations | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| IBA · PAINT phylogenetic (IBA) | 11069 | 11057 | 8101 | 1753 | 327 | 461 | 198 | 217 | 9% |
| IEA · Ensembl Compara (IEA) | 8462 | 8462 | 2587 | 3995 | 1115 | 231 | 310 | 224 | 20% |
| ISS · Manual ortholog transfer | 5260 | 5260 | 2368 | 2286 | 323 | 123 | 89 | 71 | 10% |
| IEA · Combined IEA (orthology component) | 3638 | 3638 | 2700 | 615 | 135 | 139 | 23 | 26 | 8% |
| ISO · Alliance human→mouse ISO | 2009 | 2009 | 723 | 972 | 177 | 44 | 78 | 15 | 15% |
| ISO · Alliance mouse↔rat ISO | 1072 | 1072 | 296 | 590 | 122 | 29 | 26 | 9 | 17% |
| IEA · TreeGrafter (IEA) | 969 | 969 | 435 | 202 | 102 | 67 | 105 | 58 | 28% |
| ISO · RGD ISO from other mammals | 906 | 906 | 268 | 423 | 119 | 27 | 60 | 9 | 23% |
| ISS · Paper-referenced ISS | 525 | 525 | 278 | 152 | 24 | 51 | 13 | 7 | 17% |
| ISO · Paper-referenced ISO | 149 | 149 | 81 | 47 | 12 | 2 | 6 | 1 | 13% |
| ISA · TFClass DbTF classification | 89 | 89 | 88 | 0 | 0 | 1 | 0 | 0 | 1% |
| ISO · Manual ortholog transfer | 49 | 49 | 36 | 8 | 1 | 1 | 2 | 1 | 8% |
| ISO · MGI curated orthology | 39 | 39 | 16 | 16 | 0 | 3 | 4 | 0 | 18% |
| ISS · Manual complex transfer | 13 | 13 | 12 | 1 | 0 | 0 | 0 | 0 | 0% |
| ISA · Paper-referenced ISA | 8 | 8 | 6 | 1 | 1 | 0 | 0 | 0 | 12% |
| ISO · Manual complex transfer | 8 | 8 | 7 | 0 | 0 | 1 | 0 | 0 | 12% |

## ISO: donor species → target species

| Donor → target | Annotations | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Homo sapiens → Mus musculus | 2153 | 2153 | 791 | 1021 | 189 | 49 | 87 | 16 | 15% |
| Rattus norvegicus → Mus musculus | 1090 | 1090 | 302 | 602 | 122 | 29 | 26 | 9 | 16% |
| Homo sapiens → Rattus norvegicus | 454 | 454 | 128 | 234 | 71 | 8 | 9 | 4 | 19% |
| Mus musculus → Rattus norvegicus | 300 | 300 | 52 | 139 | 41 | 12 | 51 | 5 | 35% |
| Homo sapiens + Mus musculus → Rattus norvegicus | 124 | 124 | 76 | 37 | 5 | 6 | 0 | 0 | 9% |
| Saccharomyces cerevisiae → Schizosaccharomyces pombe | 51 | 51 | 38 | 9 | 1 | 1 | 1 | 1 | 6% |
| Homo sapiens + Mus musculus + Sus scrofa → Rattus norvegicus | 9 | 9 | 6 | 3 | 0 | 0 | 0 | 0 | 0% |
| unresolved → Homo sapiens | 8 | 8 | 7 | 0 | 0 | 1 | 0 | 0 | 12% |
| Homo sapiens + Sus scrofa → Rattus norvegicus | 7 | 7 | 4 | 3 | 0 | 0 | 0 | 0 | 0% |
| Canis lupus familiaris + Homo sapiens + Mus musculus → Rattus norvegicus | 5 | 5 | 4 | 0 | 0 | 1 | 0 | 0 | 20% |
| Sus scrofa → Rattus norvegicus | 5 | 5 | 0 | 4 | 1 | 0 | 0 | 0 | 20% |
| Homo sapiens → Schizosaccharomyces pombe | 4 | 4 | 3 | 0 | 0 | 0 | 1 | 0 | 25% |
| Canis lupus familiaris + Homo sapiens + Sus scrofa → Rattus norvegicus | 3 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0% |
| Bos taurus → Mus musculus | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0% |
| Chinchilla lanigera → Rattus norvegicus | 2 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0% |
| Cricetulus griseus → Mus musculus | 2 | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 50% |
| Gallus gallus → Mus musculus | 2 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0% |
| Pyrococcus furiosus → Schizosaccharomyces pombe | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0% |
| Aspergillus niger → Schizosaccharomyces pombe | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0% |
| Canis lupus familiaris + Homo sapiens + Mus musculus + Sus scrofa → Rattus norvegicus | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0% |
| Canis lupus familiaris + Mus musculus → Rattus norvegicus | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 100% |
| Escherichia coli → Schizosaccharomyces pombe | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0% |
| Mus musculus + Sus scrofa → Rattus norvegicus | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0% |
| Mus musculus → Schizosaccharomyces pombe | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0% |
| Saccharomyces cerevisiae → Homo sapiens | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0% |
| Salmonella typhimurium → Escherichia coli | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0% |
| Xenopus laevis → Mus musculus | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0% |

## ISO: does the donor still carry the term?

Donor support is the donor's current evidence for the exact transferred term
(QuickGO). `INFERRED_ONLY` means the donor itself only has inferred support —
typically a transfer of a transfer. `ABSENT` means the donor was checked and no
longer carries the term.

| Donor support | Annotations | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EXPERIMENTAL | 3780 | 3780 | 1288 | 1845 | 387 | 93 | 140 | 27 | 16% |
| INFERRED_ONLY | 54 | 54 | 28 | 16 | 2 | 2 | 6 | 0 | 19% |
| ABSENT | 383 | 383 | 104 | 189 | 41 | 11 | 30 | 8 | 21% |
| NOT_CHECKED | 15 | 15 | 7 | 6 | 1 | 1 | 0 | 0 | 13% |

## ISO: donor symbol vs target symbol

A different donor symbol flags paralog or multi-locus sourcing (for example rat
Calm1/Calm2 as donors for mouse Calm3). `MIXED` means the annotation has both a
namesake donor and a differently named one. It prompts a check; it is not a verdict.

| Symbol match | Annotations | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SAME_SYMBOL | 4014 | 4014 | 1360 | 1992 | 405 | 98 | 127 | 32 | 16% |
| MIXED | 45 | 45 | 9 | 31 | 5 | 0 | 0 | 0 | 11% |
| DIFFERENT_SYMBOL | 162 | 162 | 50 | 31 | 21 | 8 | 49 | 3 | 48% |
| UNRESOLVED | 11 | 11 | 8 | 2 | 0 | 1 | 0 | 0 | 9% |

## What does ISO add on top of IBA?

For each ISO row, the closest IBA annotation on the same target (GO is_a/part_of
closure). Rows in the first two buckets are already implied by PAINT; the last two
are what ISO contributes beyond IBA.

| IBA on target | biological_process | cellular_component | molecular_function | All ISO | Share |
|---|---:|---:|---:|---:|---:|
| IBA to the same term | 190 | 197 | 199 | 586 | 14% |
| IBA to a more specific term (already entails the ISO row) | 95 | 81 | 88 | 264 | 6% |
| IBA only to a more general term (ISO adds specificity) | 144 | 174 | 64 | 382 | 9% |
| No related IBA (ISO adds a new assertion) | 1825 | 552 | 623 | 3000 | 71% |

Review outcome by IBA coverage (reviewed ISO rows):

| IBA on target | Annotations | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SAME | 586 | 586 | 460 | 100 | 10 | 7 | 8 | 1 | 4% |
| MORE_SPECIFIC | 264 | 264 | 136 | 73 | 20 | 33 | 2 | 0 | 21% |
| MORE_GENERAL | 382 | 382 | 153 | 193 | 23 | 9 | 4 | 0 | 9% |
| NONE | 3000 | 3000 | 678 | 1690 | 378 | 58 | 162 | 34 | 20% |

ISO rows not implied by IBA, split by the target's own experimental evidence:

| Experimental on target | Annotations | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SAME | 445 | 445 | 213 | 198 | 18 | 12 | 3 | 1 | 7% |
| MORE_SPECIFIC | 121 | 121 | 36 | 51 | 14 | 11 | 9 | 0 | 28% |
| MORE_GENERAL | 742 | 742 | 201 | 441 | 62 | 11 | 22 | 5 | 13% |
| NONE | 2074 | 2074 | 381 | 1193 | 307 | 33 | 132 | 28 | 23% |

## Recorded propagation reviews

Structured `review.propagation_review` classifications (all methods).

| Root cause | Annotations |
|---|---:|
| NO_FAILURE_CORE | 934 |
| NO_FAILURE_NON_CORE | 590 |
| PROPAGATION_BAD | 433 |
| TERM_SCOPING_PROBLEM | 407 |
| UNRESOLVED | 208 |
| SOURCE_WEAK_OR_INFERRED | 65 |
| SOURCE_BAD | 43 |
| SOURCE_STALE_OR_MISSING | 27 |
| EVIDENCE_CIRCULAR_OR_REDUNDANT | 23 |

| Failure mode | Annotations |
|---|---:|
| GRANULARITY_MISMATCH | 329 |
| CONTEXT_OR_TISSUE_MISMATCH | 257 |
| FUNCTIONAL_DIVERGENCE | 170 |
| ROLE_CONFLATION | 169 |
| COMPARTMENT_OR_COMPLEX_MISMATCH | 139 |
| WRONG_ORTHOLOG_OR_PARALOG | 118 |
| SOURCE_EVIDENCE_WEAK | 92 |
| PSEUDO_OR_SUBACTIVITY_LOSS | 50 |
| LINEAGE_OR_TAXON_MISMATCH | 21 |
| CIRCULAR_PROPAGATION | 21 |
| SOURCE_MISCITATION | 18 |
| REGULATORY_SIGN_INVERSION | 13 |

## Donor coverage

21,063 of 22,227 donor-based annotations have at least one donor checked.

