# RBM41: donkey-human comparison

Donkey A0A9L0IK51 (432 aa) aligned globally to human Q96IZ5 (413 aa): 95.83% identity over 408 paired residues; paired coverage 98.79% of human and 94.44% of donkey.

Donkey ranges (>=5 aa) without a human partner: [[175, 198]].
Human ranges (>=5 aa) without a donkey partner: [[409, 413]].

Method: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5. Regenerate with `uv run python genes/EQUAS/RBM41/RBM41-bioinformatics/compare.py`. Pairwise similarity does not by itself establish orthology or function.

## Human UniProt features mapped onto the donkey sequence

- DOMAIN RRM: human [309, 387] KN -> donkey [333, 411] KN; 78 of 79 human residues in this span are identical in the aligned donkey sequence (79 paired; aligned donkey span length 79)

## Human non-IEA GO annotations (human-Q96IZ5-quickgo-annotations.tsv, QuickGO download)

- enables GO:0005515 [IPI PMID:16189514]
- enables GO:0005515 [IPI PMID:21516116]
- enables GO:0005515 [IPI PMID:25416956]
- enables GO:0005515 [IPI PMID:32296183]
- enables GO:0005515 [IPI PMID:32353859]
- enables GO:0005515 [IPI PMID:33060197]
- enables GO:0005515 [IPI PMID:36217030]
- enables GO:0030626 [IBA GO_REF:0000033]
- enables GO:0097157 [IBA GO_REF:0000033]
- involved_in GO:0000398 [IBA GO_REF:0000033]
- part_of GO:0005689 [IBA GO_REF:0000033]
