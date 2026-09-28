# AKAP12 bioinformatics — results

## The PKC-binding motifs coincide with two of the three CaM-binding motifs

`akap12_motifs.py` searched human Q02952 (1782 aa) with the PKC-binding consensus
published for rodent SSeCKS (`PMID:21903576`), without assuming the rodent
coordinates transfer. Two matches, and both fall inside a UniProt-annotated AKAP
CaM-binding (WSK) motif:

| PKC consensus match | UniProt CaM motif | WSK core |
|---|---|---|
| 605-633 | 607-627 | `WASFK` (610-614) |
| 754-782 | 756-776 | `WESFK` (759-763) |
| *(no match)* | 801-821 | `WVSIK` (804-808) |

So the human protein has **three** WSK motifs, of which **two** also match the
PKC-binding consensus, and the third (801-821) does not.

This is a structural rationale for an observation the review records as
rodent-only: PKC phosphorylation antagonises calmodulin binding
(`PMID:11820772`). If the PKC-binding determinant physically overlaps the
CaM-binding motif, the two ligands compete for the same segment, and
phosphorylation within it would be expected to disfavour CaM. The overlap is a
sequence fact about the human protein; the antagonism itself has still only been
measured in rodent, and the review hedges it accordingly.

**Caveats.** These are regex matches to a published consensus, not binding
measurements — they establish that the motif is present and where, not that it is
used. The UniProt motif annotations are PROSITE-ProRule (`PRU01241`) inferences,
not experimental. Nothing here demonstrates human PKC binding or human CaM
binding.

## Open discrepancy: three human motifs vs four rodent sites

`PMID:11820772` reports **four** 1-5-10 CaM-binding sites in rodent SSeCKS;
human UniProt annotates **three** WSK motifs, and this search finds three WSK
cores. Whether the fourth rodent site is genuinely absent from human or merely
unannotated is unresolved, and is recorded as a `knowledge_gaps` entry on the
calmodulin `core_functions` entry rather than silently reconciled.

## Document integrity

`akap12_audit.py` passes: 42 entries (38 matching GOA rows 1:1, plus 4 `NEW`),
actions ACCEPT 11 / KEEP_AS_NON_CORE 17 / MODIFY 3 / MARK_AS_OVER_ANNOTATED 7 /
NEW 4; 53 `reference_id` occurrences parse to 53; 13 `propagation_review` blocks
checked; the retracted `PMID:27683220` retains `is_invalid: true` and is cited by
no `supported_by`.

`akap12_audit_selftest.py` passes: eight mutations each trip their named guard with the
expected message, and two controls leave the audit silent, so a guard that fires on
everything would be caught too. Mutants are audited in a tempfile — the curated review file
is never written, which the script asserts at the end.
