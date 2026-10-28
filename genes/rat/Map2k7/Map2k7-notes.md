# Map2k7 (rat) review notes

- Entry: Q4KSH7 (Swiss-Prot), RGD:1560043, GeneID 363855; GOA file keyed to Q4KSH7 (72 rows, 70 seeded).
- Literature synthesis in `Map2k7-deep-research-manual.md` (manual; no deep-research provider used).
- Only PMID:12514131 and PMID:20550965 have full text among the rat papers; the rest are abstract-only, so their
  experimental rows were not downgraded beyond refinement.

## Key decisions
- Core MF: JUN kinase kinase activity (GO:0008545). Generic kinase/MAPKK/Ser/Tyr kinase rows MODIFY to it
  (PMID:20550965 assayed endogenous MKK7 on GST-JNK + GST-c-Jun, i.e. a JNKK assay).
- GO:0004707 MAP kinase activity (ISO from mouse) is the wrong tier: MKK7 is the MAP2K, it phosphorylates MAPKs.
  The mouse source is a UniProt IDA on Q8CE90 citing PMID:9405446 - recorded as a source defect.
- positive regulation of JNK cascade rows: MKK7 is a component of the cascade, MODIFY laterally to JNK cascade.
- JNK cascade (GO:0007254) is NOT an is_a descendant of stress-activated MAPK cascade (GO:0051403) in the current GO
  (checked with OAK), so GO:0051403 rows are accepted as an additional core process, not refined.
- Mouse ISO rows for response to wounding / regulation of motor neuron apoptotic process come from PMID:25100604
  (axotomy-induced motoneuron death; MKK7 loss makes some motoneurons resistant) - refined to response to axon injury
  and positive regulation of motor neuron apoptotic process.

## 2026-10-28: positive regulation of JNK cascade rows (PR #5679 review)

The five GO:0046330 rows (three IDA, IEA, ISO) were first MODIFYed laterally to GO:0007254 JNK cascade. The rat Map3k5 review in the same batch keeps the identical rows as non-core, because GO conventionally gives the cascade kinases the positive-regulation term as well as the cascade term. For consistency the Map2k7 rows are now KEEP_AS_NON_CORE too, and JNK cascade stays the core process.
