---
title: "Homology Propagation Statistics"
---
# Homology Propagation Statistics

Generated 2026-09-26 by `just propagation-stats` from the cached GOA
files under `genes/` (donor cache refreshed 2026-09-26).
Counts cover every gene with a cached GOA file; *reviewed* counts are rows
matched to an `existing_annotations` entry with a final review action.
These numbers are regenerated; do not copy them into project prose.
Browse the rows in the [propagation browser](../../app/propagation/index.html).

## All propagation methods

| Method | Rows | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| IBA · PAINT phylogenetic (IBA) | 11069 | 11057 | 8101 | 1753 | 327 | 461 | 198 | 217 | 9% |
| IEA · Ensembl Compara (IEA) | 8462 | 8462 | 2587 | 3995 | 1115 | 231 | 310 | 224 | 20% |
| ISS · Manual ortholog transfer | 5590 | 5590 | 2568 | 2400 | 331 | 129 | 90 | 72 | 10% |
| IEA · Combined IEA (orthology component) | 3638 | 3638 | 2700 | 615 | 135 | 139 | 23 | 26 | 8% |
| ISO · Alliance human→mouse ISO | 2114 | 2114 | 785 | 1011 | 180 | 44 | 79 | 15 | 14% |
| ISO · Alliance mouse↔rat ISO | 1165 | 1165 | 319 | 653 | 126 | 32 | 26 | 9 | 16% |
| ISO · RGD ISO from other mammals | 1137 | 1137 | 406 | 495 | 129 | 35 | 63 | 9 | 20% |
| IEA · TreeGrafter (IEA) | 969 | 969 | 435 | 202 | 102 | 67 | 105 | 58 | 28% |
| ISS · Paper-referenced ISS | 535 | 535 | 283 | 157 | 24 | 51 | 13 | 7 | 16% |
| ISO · Paper-referenced ISO | 154 | 154 | 82 | 49 | 14 | 2 | 6 | 1 | 14% |
| ISA · TFClass DbTF classification | 89 | 89 | 88 | 0 | 0 | 1 | 0 | 0 | 1% |
| ISO · Manual ortholog transfer | 50 | 50 | 37 | 8 | 1 | 1 | 2 | 1 | 8% |
| ISO · MGI curated orthology | 39 | 39 | 16 | 16 | 0 | 3 | 4 | 0 | 18% |
| ISS · Manual complex transfer | 14 | 14 | 13 | 1 | 0 | 0 | 0 | 0 | 0% |
| ISA · Paper-referenced ISA | 12 | 12 | 7 | 4 | 1 | 0 | 0 | 0 | 8% |
| ISO · Manual complex transfer | 8 | 8 | 7 | 0 | 0 | 1 | 0 | 0 | 12% |

## ISO: donor species → target species

| Donor → target | Rows | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Homo sapiens → Mus musculus | 2262 | 2262 | 853 | 1062 | 194 | 49 | 88 | 16 | 15% |
| Rattus norvegicus → Mus musculus | 1182 | 1182 | 324 | 665 | 126 | 32 | 26 | 9 | 16% |
| Homo sapiens → Rattus norvegicus | 643 | 643 | 241 | 297 | 77 | 15 | 9 | 4 | 16% |
| Mus musculus → Rattus norvegicus | 463 | 463 | 151 | 184 | 50 | 19 | 54 | 5 | 27% |
| Saccharomyces cerevisiae → Schizosaccharomyces pombe | 52 | 52 | 39 | 9 | 1 | 1 | 1 | 1 | 6% |
| Sus scrofa → Rattus norvegicus | 26 | 26 | 14 | 11 | 1 | 0 | 0 | 0 | 4% |
| Canis lupus familiaris → Rattus norvegicus | 10 | 10 | 7 | 1 | 1 | 1 | 0 | 0 | 20% |
| unresolved → Homo sapiens | 8 | 8 | 7 | 0 | 0 | 1 | 0 | 0 | 12% |
| Homo sapiens → Schizosaccharomyces pombe | 4 | 4 | 3 | 0 | 0 | 0 | 1 | 0 | 25% |
| Bos taurus → Mus musculus | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0% |
| Chinchilla lanigera → Rattus norvegicus | 2 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0% |
| Cricetulus griseus → Mus musculus | 2 | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 50% |
| Gallus gallus → Mus musculus | 2 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0% |
| Mus musculus → Schizosaccharomyces pombe | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0% |
| Pyrococcus furiosus → Schizosaccharomyces pombe | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0% |
| Aspergillus niger → Schizosaccharomyces pombe | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0% |
| Escherichia coli → Schizosaccharomyces pombe | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0% |
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
| EXPERIMENTAL | 4172 | 4172 | 1485 | 2010 | 405 | 101 | 144 | 27 | 16% |
| INFERRED_ONLY | 57 | 57 | 30 | 16 | 2 | 3 | 6 | 0 | 19% |
| ABSENT | 392 | 392 | 109 | 192 | 41 | 12 | 30 | 8 | 21% |
| NOT_CHECKED | 46 | 46 | 28 | 14 | 2 | 2 | 0 | 0 | 9% |

## ISO: donor symbol vs target symbol

A different donor symbol flags paralog or multi-locus sourcing (for example rat
Calm1/Calm2 as donors for mouse Calm3). It prompts a check; it is not a verdict.

| Symbol match | Rows | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SAME_SYMBOL | 4406 | 4406 | 1574 | 2137 | 424 | 109 | 130 | 32 | 15% |
| DIFFERENT_SYMBOL | 250 | 250 | 70 | 93 | 26 | 8 | 50 | 3 | 34% |
| UNRESOLVED | 11 | 11 | 8 | 2 | 0 | 1 | 0 | 0 | 9% |

## What does ISO add on top of IBA?

For each ISO row, the closest IBA annotation on the same target (GO is_a/part_of
closure). Rows in the first two buckets are already implied by PAINT; the last two
are what ISO contributes beyond IBA.

| IBA on target | biological_process | cellular_component | molecular_function | All ISO | Share |
|---|---:|---:|---:|---:|---:|
| IBA to the same term | 232 | 268 | 249 | 749 | 16% |
| IBA to a more specific term (already entails the ISO row) | 109 | 97 | 97 | 303 | 6% |
| IBA only to a more general term (ISO adds specificity) | 162 | 211 | 71 | 444 | 10% |
| No related IBA (ISO adds a new assertion) | 1903 | 613 | 655 | 3171 | 68% |

Review outcome by IBA coverage (reviewed ISO rows):

| IBA on target | Rows | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SAME | 749 | 749 | 591 | 131 | 10 | 8 | 8 | 1 | 3% |
| MORE_SPECIFIC | 303 | 303 | 154 | 85 | 21 | 41 | 2 | 0 | 21% |
| MORE_GENERAL | 444 | 444 | 177 | 229 | 24 | 10 | 4 | 0 | 9% |
| NONE | 3171 | 3171 | 730 | 1787 | 395 | 59 | 166 | 34 | 20% |

ISO rows not implied by IBA, split by the target's own experimental evidence:

| Experimental on target | Rows | Reviewed | ACCEPT | KEEP_AS_NON_CORE | MARK_AS_OVER_ANNOTATED | MODIFY | REMOVE | UNDECIDED | REMOVE/OVER/MODIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SAME | 506 | 506 | 248 | 223 | 18 | 13 | 3 | 1 | 7% |
| MORE_SPECIFIC | 126 | 126 | 39 | 52 | 14 | 11 | 10 | 0 | 28% |
| MORE_GENERAL | 783 | 783 | 219 | 461 | 64 | 12 | 22 | 5 | 13% |
| NONE | 2200 | 2200 | 401 | 1280 | 323 | 33 | 135 | 28 | 22% |

## Recorded propagation reviews

Structured `review.propagation_review` classifications (all methods).

| Root cause | Rows |
|---|---:|
| NO_FAILURE_CORE | 948 |
| NO_FAILURE_NON_CORE | 596 |
| PROPAGATION_BAD | 445 |
| TERM_SCOPING_PROBLEM | 419 |
| UNRESOLVED | 208 |
| SOURCE_WEAK_OR_INFERRED | 65 |
| SOURCE_BAD | 43 |
| SOURCE_STALE_OR_MISSING | 27 |
| EVIDENCE_CIRCULAR_OR_REDUNDANT | 23 |

| Failure mode | Rows |
|---|---:|
| GRANULARITY_MISMATCH | 345 |
| CONTEXT_OR_TISSUE_MISMATCH | 267 |
| ROLE_CONFLATION | 173 |
| FUNCTIONAL_DIVERGENCE | 170 |
| COMPARTMENT_OR_COMPLEX_MISMATCH | 140 |
| WRONG_ORTHOLOG_OR_PARALOG | 121 |
| SOURCE_EVIDENCE_WEAK | 92 |
| PSEUDO_OR_SUBACTIVITY_LOSS | 50 |
| LINEAGE_OR_TAXON_MISMATCH | 21 |
| CIRCULAR_PROPAGATION | 21 |
| SOURCE_MISCITATION | 18 |
| REGULATORY_SIGN_INVERSION | 13 |

## Donor coverage

21,811 of 23,007 donor-based rows have at least one donor checked.

