# Horse GEMIN5 (F6WDM0) versus human GEMIN5 (Q8TEQ6)

Script: `compare_to_human.py` (run with `uv run --no-project --with biopython python compare_to_human.py`).
Raw output: `results.txt`. Sequences come from the UniProt flat files in the repo
(`genes/HORSE/GEMIN5__F6WDM0/GEMIN5__F6WDM0-uniprot.txt`, `genes/human/GEMIN5/GEMIN5-uniprot.txt`).
Method: global pairwise alignment (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5).

## Evolutionary relationship

Both proteins are assigned to PANTHER subfamily PTHR46362:SF1 (GEM-ASSOCIATED PROTEIN 5) in their
UniProt records, and both receive IBA annotations from the same PAINT node, PTN005299808. Ensembl
Compara treats them as orthologs (the GO_REF:0000107 rows on F6WDM0 cite human ENSP00000285873).
F6WDM0 is the product of horse transcript ENSECAT00000022126 (protein ENSECAP00000018265) of gene ENSECAG00000020479.

## Global comparison

- human Q8TEQ6: 1508 aa; horse F6WDM0: 1517 aa
- 1507 aligned positions, 1338 identical: 88.8% identity over aligned positions (88.7% over the human length)
- Indels: a 9-residue horse insertion after human position 618 (horse 619-627, inside the second WD40
  propeller region; human `...KTVIE|SSPESPV...`, horse `...KTVIEMTSSPCLVESNPESPV...`), one single-residue
  insertion near horse 1317 and one single-residue deletion at human 1330 (both in the C-terminal RBS region).
- F6WDM0 is full length. It lacks none of the segments of the human protein: the tandem WD40 module,
  the 723-798 linker, the TPR-like dimerization region and the C-terminal RBS region are all present.

## Experimentally characterised residues

All human residues with structural or mutational evidence for RNA or cap contacts are identical at the
aligned horse positions (and fall at the same numbers, since the first indel is downstream of them):

- snRNA Sm-site contacts mutated in PMID:27881601: N13, W14, Y15, R33, R335, M357, R359, F381, Y383, M403, W422, Y474 -- all identical.
- m7G cap contacts in the m7GTP-soaked structure (PMID:27881601): Y474, L580, N582 -- all identical.
- Cap-binding residues identified by mutation (PMID:19750007): W286, F338 -- all identical.

## Interpretation and limits

The RNA-recognition surface of the WD40 module is fully conserved, which supports transfer of the
human snRNA- and cap-binding activities to the horse ortholog. The 9-residue insertion lies away from
all mapped contact residues; its structural effect is not determined by this analysis. No horse protein
has been tested experimentally; conservation is consistent with, but does not demonstrate, activity.
