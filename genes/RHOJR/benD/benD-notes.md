# benD (Q93HW2, Rhodococcus jostii RHA1) notes

## Provenance of this review

- Created as a cross-genus representative member of
  `modules/benzoate_upper_pathway.yaml`, so the module is grounded beyond
  Pseudomonas putida KT2440.
- Deep research: `just deep-research-falcon RHOJR benD` was attempted and failed with
  "Failed to authenticate" (provider credentials rejected), so there is no
  `-deep-research-*.md` file and none was written by hand. The review rests on
  the UniProt entry and the cached publications: PMID:11673430.
- Every quotation is verbatim from those cached sources; several are
  abstract-only, flagged with `full_text_unavailable` on the reference.

## This gene

- Unreviewed entry; the EC number and product names come from EMBL submissions,
  so support rests on the NCBIfam BenD equivalog NF040811 plus the reconstitution
  of benzoate-to-catechol conversion via the cis-diol by RHA1 benABCD. benD is
  the only dehydrogenase in that gene set.
- Carries the same two PANTHER-derived problems as the ADP1 paralog: GO:0016616
  MODIFYed to GO:0047116, and GO:0030497 fatty acid elongation REMOVEd
  (node PTN001211919, judged TOO_DEEP in the PTHR42760 family review).
- Open question recorded: RHA1 BenABC transforms 3-chlorobenzoate, so whether
  BenD also accepts the corresponding 3-chloro cis-diol is untested.
