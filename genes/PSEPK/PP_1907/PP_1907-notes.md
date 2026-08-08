# PP_1907 (Q88LM3) curation notes

## Functional assignment provenance

Automated orthology and family resources converge on 2-phosphoglycolate
phosphatase (Gph; EC 3.1.3.18) for PP_1907:

- KEGG ortholog K01091 (phosphoglycolate phosphatase), pathway ppu00630.
- PANTHER family PTHR43434 (PHOSPHOGLYCOLATE PHOSPHATASE).
- UniProt/TreeGrafter GO:0008967 phosphoglycolate phosphatase activity.
- All six catalytic residues align one-to-one with characterized *E. coli* Gph
  (P32662), despite only ~29% overall identity.

The GO:0008967 molecular function (GOA/TreeGrafter) is therefore accepted as
well-supported. The assignment is nonetheless inferential (bioinformatic /
structural / evolutionary); PP_1907 itself has never been biochemically
characterized.

## Paralog context and salvage framing

PP_1907 is one of three K01091-annotated HAD-IA paralogs in *P. putida* KT2440
(PP_0094, PP_0416, PP_1907). PP_0416 (43% identical to *E. coli* Gph, explicitly
named "Phosphoglycolate phosphatase") is the stronger candidate for the principal
KT2440 2-phosphoglycolate phosphatase; PP_1907 may act redundantly on
2-phosphoglycolate and/or related small phosphometabolites.

Per the glycolate/glyoxylate assimilation module, PP_0094/PP_0416/PP_1907 are
housekeeping phosphoglycolate-salvage candidates, NOT the physiological ppu00630
glycolate-entry route for KT2440 (which lacks the CBB/photorespiratory context
that makes 2-phosphoglycolate a major glycolate source; GlcDEF supplies the
physiological glycolate). The NEW `involved_in GO:0046487 glyoxylate metabolic
process` annotation was retained (the phosphoglycolate phosphatase MF is
well-supported here, unlike PP_0094 where it is only predicted), but its
`review.reason` was rewritten to make this contextual-salvage / non-physiological-
route caveat explicit and consistent with the module framing.
