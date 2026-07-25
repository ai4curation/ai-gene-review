# PP_0094 (Q88RN5) curation notes

## Functional assignment provenance

The original UniProt/GenBank submission (EMBL AAN65728.1, 2002 KT2440 whole-genome
auto-annotation) names PP_0094 a 5'-nucleotidase (EC 3.1.3.5). This is a
lower-resolution legacy call.

Domain, orthology, and OpenScientist deep-research evidence favor
2-phosphoglycolate phosphatase (EC 3.1.3.18) as the most likely primary activity:

- KEGG orthology K01091 (phosphoglycolate phosphatase), pathway ppu00630.
- PANTHER family PTHR43434 (PHOSPHOGLYCOLATE PHOSPHATASE).
- InterPro PGP-like C2 cap domain IPR023198.
- Closest characterized homolog is *E. coli* Gph (P32662), top pairwise match
  among characterized HAD enzymes.

The enzyme is therefore curated conservatively as a predicted cytosolic
phosphoglycolate/small-phosphometabolite cleanup enzyme. PP_0094 has never been
experimentally assayed (UniProt protein-existence level 4, "Predicted"), so the
phosphoglycolate phosphatase MF (GO:0008967) is entered as a NEW/ISS prediction
rather than an established function; direct substrate assays are still needed to
distinguish EC 3.1.3.18 from EC 3.1.3.5.

## GO:0046487 glyoxylate metabolic process — dropped

An earlier draft added a NEW `involved_in GO:0046487 glyoxylate metabolic process`
annotation, inferred from the predicted phosphoglycolate-to-glycolate reaction and
KEGG ppu00630 context. This was dropped on reviewer feedback: it is a prediction
stacked on a prediction (the phosphoglycolate phosphatase MF is itself only
predicted, NEW/ISS), and the glycolate/glyoxylate module explicitly frames
PP_0094/PP_0416/PP_1907 as housekeeping phosphoglycolate salvage rather than the
physiological ppu00630 glycolate-entry route in KT2440. The process link was also
removed from `core_functions[].directly_involved_in` for internal consistency.
