# fruK curation notes

## Boundary and evidence

FruK (Q88PQ4; PP_0794) is the ATP-dependent 1-phosphofructokinase in the
fruBKA operon. The exact UniProt record assigns EC 2.7.1.56 and RHEA:14213 for
conversion of fructose 1-phosphate plus ATP to fructose 1,6-bisphosphate plus
ADP and proton. Primary KT2440 literature describes the same locus as
containing "a third gene needed for F1P phosphorylation, fruK" and identifies
FruK as 1-phosphofructokinase [PMID:27933319].

The generic phosphofructokinase annotation was marked over-annotated because it
can be confused with fructose 6-phosphate kinase activity; GO:0008662 is the
exact molecular function. ATP binding and predicted cytosolic localization were
retained as non-core properties.

The broad carbohydrate-catabolic annotation `GO:0016052` was modified to
`GO:0006001` because FruK is the fructose-specific `fruBKA` step needed for
fructose 1-phosphate phosphorylation
[PMID:27933319 "a third gene needed for F1P phosphorylation, fruK"].

## 2026-11-05 completion pass (Claude, AI-assisted)

- `GO:0008443 phosphofructokinase activity`, `GO:0016301 kinase activity` and
  `GO:0016773 phosphotransferase activity, alcohol group as acceptor` changed from
  MARK_AS_OVER_ANNOTATED to `TOO_GENERAL`: they are true is_a ancestors of the accepted
  `GO:0008662 1-phosphofructokinase activity`, not over-annotations. This matches the
  E. coli FruK (P0AEW9) review, where the same terms are now TOO_GENERAL.
- Added vetted support to every row: the UniRule-backed RHEA:14213 catalytic activity,
  the NCBIfam TIGR03168 1-PFK family model, the PfkB family similarity line, and the KT2440
  fruBKA literature [PMID:27933319 "fruK (1-phosphofructokinase)"]. No proposed_new_terms
  existed. Status set to COMPLETE.
