# PDIA4: donkey-human comparison

Donkey A0A8C4LTV9 (1197 aa) aligned globally to human P13667 (645 aa): 88.37% identity over 645 paired residues; paired coverage 100.0% of human and 53.88% of donkey.

Donkey ranges (>=5 aa) without a human partner: [[2, 139], [142, 312], [319, 425], [428, 478], [484, 537], [542, 572]].
Human ranges (>=5 aa) without a donkey partner: none.

Method: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5. Regenerate with `uv run python genes/EQUAS/PDIA4/PDIA4-bioinformatics/compare.py`. Pairwise similarity does not by itself establish orthology or function.

## Human UniProt features mapped onto the donkey sequence

- SIGNAL : human [1, 20] MA -> donkey [1, 541] MS; 14 of 20 human residues in this span are identical in the aligned donkey sequence (20 paired; aligned donkey span length 541)
- DOMAIN Thioredoxin 1: human [21, 169] VQ -> donkey [573, 721] LQ; 121 of 149 human residues in this span are identical in the aligned donkey sequence (149 paired; aligned donkey span length 149)
- DOMAIN Thioredoxin 2: human [158, 301] EK -> donkey [710, 853] EK; 135 of 144 human residues in this span are identical in the aligned donkey sequence (144 paired; aligned donkey span length 144)
- DOMAIN Thioredoxin 3: human [505, 636] FT -> donkey [1057, 1188] FR; 120 of 132 human residues in this span are identical in the aligned donkey sequence (132 paired; aligned donkey span length 132)
- MOTIF CXXC: human [91, 94] CC -> donkey [643, 646] CC; 4 of 4 human residues in this span are identical in the aligned donkey sequence (4 paired; aligned donkey span length 4)
- MOTIF CXXC: human [555, 558] CC -> donkey [1107, 1110] CC; 4 of 4 human residues in this span are identical in the aligned donkey sequence (4 paired; aligned donkey span length 4)
- MOTIF Prevents secretion from ER: human [642, 645] KL -> donkey [1194, 1197] RL; 3 of 4 human residues in this span are identical in the aligned donkey sequence (4 paired; aligned donkey span length 4)
- DISULFID Redox-active: human [91, 94] CC -> donkey [643, 646] CC; 4 of 4 human residues in this span are identical in the aligned donkey sequence (4 paired; aligned donkey span length 4)
- DISULFID Redox-active: human [206, 209] CC -> donkey [758, 761] CC; 4 of 4 human residues in this span are identical in the aligned donkey sequence (4 paired; aligned donkey span length 4)
- DISULFID Redox-active: human [555, 558] CC -> donkey [1107, 1110] CC; 4 of 4 human residues in this span are identical in the aligned donkey sequence (4 paired; aligned donkey span length 4)

## Human non-IEA GO annotations (human-P13667-quickgo-annotations.tsv, QuickGO download)

- enables GO:0003723 [HDA PMID:22658674]
- enables GO:0003756 [ISS GO_REF:0000024]
- enables GO:0003756 [IBA GO_REF:0000033]
- enables GO:0005515 [IPI PMID:16287128]
- enables GO:0005515 [IPI PMID:22190034]
- enables GO:0005515 [IPI PMID:22665516]
- enables GO:0005515 [IPI PMID:23956175]
- enables GO:0005515 [IPI PMID:28514442]
- enables GO:0005515 [IPI PMID:30021884]
- enables GO:0005515 [IPI PMID:32296183]
- enables GO:0005515 [IPI PMID:33961781]
- enables GO:0015035 [IDA PMID:16677074]
- involved_in GO:0006457 [ISS GO_REF:0000024]
- involved_in GO:0006457 [IBA GO_REF:0000033]
- involved_in GO:0009306 [TAS PMID:2295602]
- involved_in GO:0034976 [IBA GO_REF:0000033]
- is_active_in GO:0005783 [IBA GO_REF:0000033]
- is_active_in GO:0009986 [IBA GO_REF:0000033]
- located_in GO:0005576 [IDA PMID:19995400]
- located_in GO:0005783 [IDA GO_REF:0000052]
- located_in GO:0005788 [EXP PMID:12643545]
- located_in GO:0005788 [TAS PMID:2295602]
- located_in GO:0009986 [IDA PMID:19995400]
- located_in GO:0042470 [EXP PMID:17081065]
