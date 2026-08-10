# purD curation notes

- UniProt identifies Q88DK2 as Phosphoribosylamine--glycine ligase [file:PSEPK/purD/purD-uniprot.txt "RecName: Full=Phosphoribosylamine--glycine ligase"].
- Replace generic catalytic activity with `GO:0004637`. ATP and metal binding are valid
  supporting molecular functions, retained as non-core.
- Mark purine nucleobase biosynthetic process as over-annotated because this route
  produces the nucleotide IMP rather than a free purine nucleobase; GO:0009113 is not
  a broad parent of `GO:0006189`.
