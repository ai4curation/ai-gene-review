# purC curation notes

- UniProt identifies Q88NG9 as Phosphoribosylaminoimidazole-succinocarboxamide synthase [file:PSEPK/purC/purC-uniprot.txt "RecName: Full=Phosphoribosylaminoimidazole-succinocarboxamide synthase"].
- Remove the cobalamin-process annotation because it conflicts with the exact PurC
  assignment and has no target-specific support. Replace the broad purine nucleotide
  process with `GO:0006189`.
- Open question: Should the cobalamin-process InterPro mapping be narrowed so it is not transferred to canonical PurC proteins?
