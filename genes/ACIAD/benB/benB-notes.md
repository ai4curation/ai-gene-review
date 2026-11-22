# benB (P07770, Acinetobacter baylyi ADP1) notes

## Provenance of this review

- Created as a cross-genus representative member of
  `modules/benzoate_upper_pathway.yaml`, so the module is grounded beyond
  Pseudomonas putida KT2440.
- Deep research: `just deep-research-falcon ACIAD benB` was attempted and failed with
  "Failed to authenticate" (provider credentials rejected), so there is no
  `-deep-research-*.md` file and none was written by hand. The review rests on
  the UniProt entry and the cached publications: PMID:1885518, PMID:2824437, PMID:12949084.
- Every quotation is verbatim from those cached sources; several are
  abstract-only, flagged with `full_text_unavailable` on the reference.

## This gene

- BenB carries no redox centre; the Rieske cluster and the mononuclear iron are
  both in BenA. Its contribution is structural, shown by hybrid oxygenases
  [PMID:12949084 "However, they also demonstrate that the β subunit contributes
  significantly to the enzyme's function."], so the core function is recorded as
  `contributes_to_molecular_function` rather than as an independent activity.
- The GOA row states `enables` for GO:0018623 because the EC-mapping pipeline
  gives the holoenzyme's EC number to every subunit. That is recorded faithfully
  and reported upstream in `review.source_defects` (WRONG_QUALIFIER, enables ->
  contributes_to) rather than silently corrected here.
- GO:0043639 is NEW with IC, not IDA: neither cached paper assayed BenB on its
  own, the evidence being whole-operon reconstitution. This matches the PSEPK
  benB review.
- GO:0019380 3-phenylpropionate catabolic process is REMOVEd as TreeGrafter
  over-propagation; the adjudication of the node behind it (PTN002222817, judged
  TOO_DEEP) lives in `interpro/panther/PTHR41534/PTHR41534-review.yaml`.
