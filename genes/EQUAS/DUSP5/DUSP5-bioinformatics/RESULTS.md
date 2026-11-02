# DUSP5: donkey-human comparison

Donkey A0A8C4MED2 (384 aa) aligned globally to human Q16690 (384 aa): 94.79% identity over 384 paired residues; paired coverage 100.0% of human and 100.0% of donkey.

Donkey ranges (>=5 aa) without a human partner: none.
Human ranges (>=5 aa) without a donkey partner: none.

Method: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5. Regenerate with `uv run python genes/EQUAS/DUSP5/DUSP5-bioinformatics/compare.py`. Pairwise similarity does not by itself establish orthology or function.

## Human UniProt features mapped onto the donkey sequence

- DOMAIN Rhodanese: human [19, 141] AV -> donkey [19, 141] AV; 122 of 123 human residues in this span are identical in the aligned donkey sequence (123 paired; aligned donkey span length 123)
- DOMAIN Tyrosine-protein phosphatase: human [178, 319] GP -> donkey [178, 319] GP; 136 of 142 human residues in this span are identical in the aligned donkey sequence (142 paired; aligned donkey span length 142)
- MOTIF Nuclear localization signal: human [53, 74] RR -> donkey [53, 74] RR; 22 of 22 human residues in this span are identical in the aligned donkey sequence (22 paired; aligned donkey span length 22)
- ACT_SITE Phosphocysteine intermediate: human [263] C -> donkey [263] C; 1 of 1 human residues in this span are identical in the aligned donkey sequence (1 paired; aligned donkey span length 1)

## Human non-IEA GO annotations (human-Q16690-quickgo-annotations.tsv, QuickGO download)

- enables GO:0004721 [IBA GO_REF:0000033]
- enables GO:0004722 [EXP PMID:7961985]
- enables GO:0004725 [TAS PMID:7961985]
- enables GO:0005515 [IPI PMID:15713638]
- enables GO:0005515 [IPI PMID:36115835]
- enables GO:0008138 [IDA PMID:7961985]
- enables GO:0008138 [TAS Reactome:R-HSA-5675373]
- enables GO:0016791 [IDA PMID:24531476]
- involved_in GO:0000165 [TAS Reactome:R-HSA-5673001]
- involved_in GO:0001706 [IBA GO_REF:0000033]
- involved_in GO:0006470 [TAS PMID:7961985]
- involved_in GO:0007165 [IBA GO_REF:0000033]
- involved_in GO:0016311 [IDA PMID:24531476]
- involved_in GO:0035335 [IDA PMID:7961985]
- involved_in GO:0035970 [IDA PMID:7961985]
- involved_in GO:0043409 [IBA GO_REF:0000033]
- involved_in GO:0070371 [TAS Reactome:R-HSA-112409]
- is_active_in GO:0005634 [IBA GO_REF:0000033]
- is_active_in GO:0005737 [IBA GO_REF:0000033]
- located_in GO:0005654 [TAS Reactome:R-HSA-5675373]
