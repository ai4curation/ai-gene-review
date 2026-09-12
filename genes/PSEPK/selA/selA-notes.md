# selA review notes

- Q88QJ8 is a reviewed SelA-family L-seryl-tRNA(Sec) selenium transferase (EC
  2.9.1.1). [file:PSEPK/selA/selA-uniprot.txt
  "RecName: Full=L-seryl-tRNA(Sec) selenium transferase"]
  [file:interpro/panther/PTHR32328/PTHR32328-entries.csv
  "Q88QJ8,L-seryl-tRNA(Sec) selenium transferase"]
- The reaction consumes Ser-tRNA(Sec) and selenophosphate and produces
  Sec-tRNA(Sec); UniProt also assigns PLP as cofactor.
  [file:PSEPK/selA/selA-uniprot.txt
  "Reaction=L-seryl-tRNA(Sec) + selenophosphate"]
- Review boundary: SelA completes charged Sec-tRNA biosynthesis. The generic
  selenocysteine-incorporation annotation was narrowed to GO:0001717 because
  ribosomal delivery and UGA/SECIS decoding are SelB functions, not SelA
  functions.

## OpenScientist reconciliation

Source: `file:PSEPK/selA/selA-deep-research-openscientist.md`.

- The report independently supports the PLP-dependent conversion of
  Ser-tRNA(Sec) to Sec-tRNA(Sec), the bacterial substrate distinction from
  SepSecS, and the cytoplasmic pathway placement.
- The Q88QJ8-specific sequence, neighborhood, and structure analyses are
  computational corroboration, not direct organism-specific experiments.
- The report found no biochemical or structural study of Q88QJ8 itself. This
  limitation is retained as a core-function knowledge gap.
