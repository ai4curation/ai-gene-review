# PDIA4 re-review: locus context and N-terminal segment identity

## Genomic context (Ensembl REST)

- Donkey PDIA4 gene ENSEASG00005009014: chr1:1023772-1078943 strand 1 (55172 bp)
- Donkey protein-coding genes overlapping chr1:963772-1138943:
  - ENSEASG00005009014 PDIA4 1023772-1078943 strand 1
  - ENSEASG00005035571 ZNF425 1004371-1014880 strand 1
  - ENSEASG00005009006 ZNF398 945677-976966 strand -1
- Human genes (GRCh38):
  - PDIA4 ENSG00000155660 chr7:149003046-149028667 strand -1 (25622 bp)
  - ZNF786 ENSG00000197362 chr7:149069491-149090784 strand -1 (21294 bp)
  - ZNF425 ENSG00000204947 chr7:149102784-149126348 strand -1 (23565 bp)

## Segment alignments (local, BLOSUM62, gap -10/-0.5)

- A0A8C4LTV9 length 1197; N-terminal segment 1-580, C-terminal segment 581-1197
- N-terminal segment vs human PDIA4 (P13667, 645 aa): 29.0% identity over 283 paired residues; donkey 5-365, human 233-558
- C-terminal segment vs human PDIA4 (P13667, 645 aa): 90.1% identity over 615 paired residues; donkey 583-1197, human 31-645
- N-terminal segment vs human ZNF786 (Q8N393, 782 aa): 64.2% identity over 565 paired residues; donkey 1-580, human 1-649
- C-terminal segment vs human ZNF786 (Q8N393, 782 aa): 29.8% identity over 178 paired residues; donkey 780-986, human 5-231
- N-terminal segment vs human ZNF425 (Q6IV72, 752 aa): 45.2% identity over 544 paired residues; donkey 1-580, human 1-722
- C-terminal segment vs human ZNF425 (Q6IV72, 752 aa): 24.0% identity over 129 paired residues; donkey 758-945, human 500-661

Pairwise identity does not by itself establish orthology; the locus order is the positional (synteny) evidence.
