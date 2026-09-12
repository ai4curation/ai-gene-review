# DYNLT2B: horse–human sequence comparison

The horse sequence A0A9L0SWY1 (245 residues) aligns to human Q8WW35 (142 residues) with 91.41% identity across 128 paired residues. Paired coverage is 90.14% of the human sequence and 52.24% of the horse sequence.

Global alignment uses Biopython PairwiseAligner, BLOSUM62, gap open -10, gap extension -0.5. Inputs are the fetched UniProt flat files; sequence hashes and mapped human structural features are in `results.json`. Reproduce with `uv run python genes/HORSE/DYNLT2B/DYNLT2B-bioinformatics/compare_pair.py`.

This establishes sequence conservation between the selected pair; it does not independently establish one-to-one orthology or verify the sequence supplied to ProtNLM. Functional transfer must also consider the specific family, mapped residues and experimental human evidence.

## Mapped human structural features

- STRAND: human [4, 5, 6, 7, 8, 9, 10, 11] SIGVSFSV → horse [121, 122, 123, 124, 125, 126, 127, 128] SAGVSFSV.
- STRAND: human [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99] YKMVVQVVIGE → horse [206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216] YKMVVQVVIGE.
- STRAND: human [104, 105, 106, 107, 108, 109, 110, 111, 112, 113] GVFMASRCFW → horse [221, 222, 223, 224, 225, 226, 227, 228, 229, 230] GVFMAARCFW.
- STRAND: human [119, 120, 121, 122, 123, 124, 125, 126] NYTHDVFM → horse [236, 237, 238, 239, 240, 241, 242, 243] NYTHDVFM.
- STRAND: human [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140] DSLFCVVAAFGCF → horse [245, None, None, None, None, None, None, None, None, None, None, None, None] K------------.
