---
title: "Homology Propagation Statistics"
---
# Homology Propagation Statistics

Generated 2026-09-26 by `just propagation-stats` from the cached GOA
files under `genes/` (donor cache refreshed 2026-09-26).
Counts cover every gene with a cached GOA file. The unit is one annotation
(gene, term, qualifier, evidence, reference): pipelines that emit one GOA line
per donor are merged (35,045 GOA lines → 34,439 annotations).
*Reviewed* annotations are those matched to an `existing_annotations` entry
with a final review action.
These numbers are regenerated; do not copy them into project prose.
Browse the rows in the [propagation browser](../../app/propagation/index.html).

## All propagation methods

| Method | Rows | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| IBA · PAINT phylogenetic (IBA) | 11069 | 11057 | 8101 | 1753 | 327 | 461 | 198 | 217 | 9% |
| IEA · Ensembl Compara (IEA) | 8462 | 8462 | 2587 | 3995 | 1115 | 231 | 310 | 224 | 20% |
| ISS · Manual ortholog transfer | 5278 | 5278 | 2377 | 2293 | 324 | 124 | 89 | 71 | 10% |
| IEA · Combined IEA (orthology component) | 3638 | 3638 | 2700 | 615 | 135 | 139 | 23 | 26 | 8% |
| ISO · Alliance human→mouse ISO | 2103 | 2103 | 776 | 1009 | 180 | 44 | 79 | 15 | 14% |
| ISO · Alliance mouse↔rat ISO | 1074 | 1074 | 297 | 590 | 122 | 30 | 26 | 9 | 17% |
| IEA · TreeGrafter (IEA) | 969 | 969 | 435 | 202 | 102 | 67 | 105 | 58 | 28% |
| ISO · RGD ISO from other mammals | 966 | 966 | 303 | 441 | 122 | 28 | 63 | 9 | 22% |
| ISS · Paper-referenced ISS | 525 | 525 | 278 | 152 | 24 | 51 | 13 | 7 | 17% |
| ISO · Paper-referenced ISO | 149 | 149 | 81 | 47 | 12 | 2 | 6 | 1 | 13% |
| ISA · TFClass DbTF classification | 89 | 89 | 88 | 0 | 0 | 1 | 0 | 0 | 1% |
| ISO · Manual ortholog transfer | 49 | 49 | 36 | 8 | 1 | 1 | 2 | 1 | 8% |
| ISO · MGI curated orthology | 39 | 39 | 16 | 16 | 0 | 3 | 4 | 0 | 18% |
| ISS · Manual complex transfer | 13 | 13 | 12 | 1 | 0 | 0 | 0 | 0 | 0% |
| ISA · Paper-referenced ISA | 8 | 8 | 6 | 1 | 1 | 0 | 0 | 0 | 12% |
| ISO · Manual complex transfer | 8 | 8 | 7 | 0 | 0 | 1 | 0 | 0 | 12% |

## ISO: donor species → target species

| Donor → target | Rows | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Homo sapiens → Mus musculus | 2247 | 2247 | 844 | 1058 | 192 | 49 | 88 | 16 | 15% |
| Rattus norvegicus → Mus musculus | 1092 | 1092 | 303 | 602 | 122 | 30 | 26 | 9 | 16% |
| Homo sapiens → Rattus norvegicus | 496 | 496 | 152 | 248 | 74 | 9 | 9 | 4 | 19% |
| Mus musculus → Rattus norvegicus | 336 | 336 | 73 | 147 | 44 | 13 | 54 | 5 | 33% |
| Homo sapiens + Mus musculus → Rattus norvegicus | 106 | 106 | 66 | 33 | 2 | 5 | 0 | 0 | 7% |
| Saccharomyces cerevisiae → Schizosaccharomyces pombe | 51 | 51 | 38 | 9 | 1 | 1 | 1 | 1 | 6% |
| Homo sapiens + Mus musculus + Sus scrofa → Rattus norvegicus | 8 | 8 | 5 | 3 | 0 | 0 | 0 | 0 | 0% |
| Homo sapiens + Sus scrofa → Rattus norvegicus | 8 | 8 | 5 | 3 | 0 | 0 | 0 | 0 | 0% |
| unresolved → Homo sapiens | 8 | 8 | 7 | 0 | 0 | 1 | 0 | 0 | 12% |
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
| Canis lupus familiaris + Mus musculus + Sus scrofa → Rattus norvegicus | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0% |
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

| Donor support | Rows | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EXPERIMENTAL | 3931 | 3931 | 1373 | 1899 | 393 | 95 | 144 | 27 | 16% |
| INFERRED_ONLY | 55 | 55 | 29 | 16 | 2 | 2 | 6 | 0 | 18% |
| ABSENT | 387 | 387 | 107 | 190 | 41 | 11 | 30 | 8 | 21% |
| NOT_CHECKED | 15 | 15 | 7 | 6 | 1 | 1 | 0 | 0 | 13% |

## ISO: donor symbol vs target symbol

A different donor symbol flags paralog or multi-locus sourcing (for example rat
Calm1/Calm2 as donors for mouse Calm3). `MIXED` means the annotation has both a
namesake donor and a differently named one. It prompts a check; it is not a verdict.

| Symbol match | Rows | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SAME_SYMBOL | 4168 | 4168 | 1449 | 2046 | 411 | 100 | 130 | 32 | 15% |
| MIXED | 45 | 45 | 9 | 31 | 5 | 0 | 0 | 0 | 11% |
| DIFFERENT_SYMBOL | 164 | 164 | 50 | 32 | 21 | 8 | 50 | 3 | 48% |
| UNRESOLVED | 11 | 11 | 8 | 2 | 0 | 1 | 0 | 0 | 9% |

## What does ISO add on top of IBA?

For each ISO row, the closest IBA annotation on the same target (GO is_a/part_of
closure). Rows in the first two buckets are already implied by PAINT; the last two
are what ISO contributes beyond IBA.

| IBA on target | biological_process | cellular_component | molecular_function | All ISO | Share |
|---|---:|---:|---:|---:|---:|
| IBA to the same term | 210 | 222 | 200 | 632 | 14% |
| IBA to a more specific term (already entails the ISO row) | 104 | 86 | 89 | 279 | 6% |
| IBA only to a more general term (ISO adds specificity) | 157 | 181 | 66 | 404 | 9% |
| No related IBA (ISO adds a new assertion) | 1874 | 576 | 623 | 3073 | 70% |

Review outcome by IBA coverage (reviewed ISO rows):

| IBA on target | Rows | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SAME | 632 | 632 | 503 | 103 | 10 | 7 | 8 | 1 | 4% |
| MORE_SPECIFIC | 279 | 279 | 147 | 76 | 20 | 34 | 2 | 0 | 20% |
| MORE_GENERAL | 404 | 404 | 166 | 201 | 23 | 10 | 4 | 0 | 9% |
| NONE | 3073 | 3073 | 700 | 1731 | 384 | 58 | 166 | 34 | 20% |

ISO rows not implied by IBA, split by the target's own experimental evidence:

| Experimental on target | Rows | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SAME | 472 | 472 | 232 | 206 | 18 | 12 | 3 | 1 | 7% |
| MORE_SPECIFIC | 125 | 125 | 38 | 52 | 14 | 11 | 10 | 0 | 28% |
| MORE_GENERAL | 759 | 759 | 207 | 450 | 63 | 12 | 22 | 5 | 13% |
| NONE | 2121 | 2121 | 389 | 1224 | 312 | 33 | 135 | 28 | 23% |

## Recorded propagation reviews

Structured `review.propagation_review` classifications (all methods).

| Root cause | Rows |
|---|---:|
| NO_FAILURE_CORE | 935 |
| NO_FAILURE_NON_CORE | 591 |
| PROPAGATION_BAD | 440 |
| TERM_SCOPING_PROBLEM | 408 |
| UNRESOLVED | 208 |
| SOURCE_WEAK_OR_INFERRED | 65 |
| SOURCE_BAD | 43 |
| SOURCE_STALE_OR_MISSING | 27 |
| EVIDENCE_CIRCULAR_OR_REDUNDANT | 23 |

| Failure mode | Rows |
|---|---:|
| GRANULARITY_MISMATCH | 333 |
| CONTEXT_OR_TISSUE_MISMATCH | 263 |
| FUNCTIONAL_DIVERGENCE | 170 |
| ROLE_CONFLATION | 170 |
| COMPARTMENT_OR_COMPLEX_MISMATCH | 139 |
| WRONG_ORTHOLOG_OR_PARALOG | 118 |
| SOURCE_EVIDENCE_WEAK | 92 |
| PSEUDO_OR_SUBACTIVITY_LOSS | 50 |
| LINEAGE_OR_TAXON_MISMATCH | 21 |
| CIRCULAR_PROPAGATION | 21 |
| SOURCE_MISCITATION | 18 |
| REGULATORY_SIGN_INVERSION | 13 |

## Donor coverage

21,237 of 22,401 donor-based rows have at least one donor checked.

