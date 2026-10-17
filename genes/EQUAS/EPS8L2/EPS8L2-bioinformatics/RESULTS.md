# EPS8L2: donkey-human sequence comparison

## Method

The donkey sequence (A0A9L0KBR4, from `../EPS8L2-uniprot.txt`) was aligned globally to the
reviewed human ortholog (Q9H6S3, `human-EPS8L2-Q9H6S3.fasta`, downloaded from the UniProt
REST API on 2026-10-14 together with the flat file `human-EPS8L2-Q9H6S3-uniprot.txt`) using
Biopython PairwiseAligner (BLOSUM62, gap open -10, gap extend -0.5).

Reproduce from this folder:

```
uv run --with biopython python align_to_human.py ../EPS8L2-uniprot.txt human-EPS8L2-Q9H6S3.fasta 
```

## Output (alignment_output.txt)

```
Donkey A0A9L0KBR4: 681 aa; human Q9H6S3: 715 aa
Paired residues: 679; identical: 572; identity over paired: 84.24%
Coverage of human: 94.97%; coverage of donkey: 99.71%
Human ranges with no aligned donkey residue: 4..27, 38..47, 546..547
Donkey ranges with no aligned human residue: 207..207, 677..677
```

## Interpretation

The donkey EPS8L2 protein is a near full-length ortholog of human EPS8L2 (84.24% identity over 679 paired residues, covering the human sequence end to end). The unaligned human segments lie in the N-terminal region before the PTB domain (human 4..27 and 38..47); the PTB, SH3 and C-terminal actin-binding effector regions are present in the donkey sequence.
