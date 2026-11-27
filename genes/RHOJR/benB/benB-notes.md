# benB (Q93HW4, Rhodococcus jostii RHA1) notes

## Provenance of this review

- Created as a cross-genus representative member of
  `modules/benzoate_upper_pathway.yaml`, so the module is grounded beyond
  Pseudomonas putida KT2440.
- Deep research: `just deep-research-falcon RHOJR benB` was attempted and failed with
  "Failed to authenticate" (provider credentials rejected), so there is no
  `-deep-research-*.md` file and none was written by hand. The review rests on
  the UniProt entry and the cached publications: PMID:11673430.
- Every quotation is verbatim from those cached sources; several are
  abstract-only, flagged with `full_text_unavailable` on the reference.

## This gene

- Unreviewed (TrEMBL) entry: the protein names and EC 1.14.12.10 come from the
  EMBL submissions (`ECO:0000313`), so they are not cited as evidence. Support
  for the activity rests on the NCBIfam BenB equivalog TIGR03232 plus the
  heterologous reconstitution of RHA1 benABCD.
- Same two corrections as the ADP1 paralog, for the same reasons: the GOA
  `enables` on GO:0018623 is reported upstream as WRONG_QUALIFIER (should be
  contributes_to for a non-catalytic subunit), and GO:0019380 3-phenylpropionate
  catabolic process is REMOVEd as TreeGrafter over-propagation from
  PTN002222817.
- GO:0043639 is NEW with IC: the operon was reconstituted as a whole, and BenB
  was not assayed separately.
