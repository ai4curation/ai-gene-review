# benD (P07772, Acinetobacter baylyi ADP1) notes

## Provenance of this review

- Created as a cross-genus representative member of
  `modules/benzoate_upper_pathway.yaml`, so the module is grounded beyond
  Pseudomonas putida KT2440.
- Deep research: `just deep-research-falcon ACIAD benD` was attempted and failed with
  "Failed to authenticate" (provider credentials rejected), so there is no
  `-deep-research-*.md` file and none was written by hand. The review rests on
  the UniProt entry and the cached publications: PMID:2824437, PMID:1740120.
- Every quotation is verbatim from those cached sources; several are
  abstract-only, flagged with `full_text_unavailable` on the reference.

## This gene

- Partially purified from the heterologous host and shown to be a homodimer
  [PMID:2824437 "The dehydrogenase has been partially purified and is a dimer
  with two identical 31-kilodalton subunits."], which is why the review asserts
  the activity directly rather than inferring it from family membership.
- The reaction is decarboxylating: the cis-diol goes to catechol, CO2 and NADH.
  Worth keeping in mind when reading the module's boundary note, since CO2
  release is therefore not a feature that distinguishes this step from
  decarboxylating monooxygenases outside the module.
- Two PANTHER-derived problems in one entry: GO:0016616 is MODIFYed to the
  already-carried specific child GO:0047116, and GO:0030497 fatty acid
  elongation is REMOVEd. The latter comes from node PTN001211919, whose seeds
  are genuine FabG reductases but which sits at a Eubacteria node spanning 14
  subfamilies; that is adjudicated in
  `interpro/panther/PTHR42760/PTHR42760-review.yaml`.
