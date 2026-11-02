# SEC23A: donkey-human sequence comparison

Reproduce: `uv run python genes/EQUAS/SEC23A/SEC23A-bioinformatics/align.py genes/EQUAS/SEC23A/SEC23A-uniprot.txt genes/EQUAS/SEC23A/SEC23A-bioinformatics Q15436`

Method: Biopython PairwiseAligner, global mode, BLOSUM62, gap open -10, gap extend -0.5. The human sequence(s) (Q15436) are fetched from UniProt REST and saved as FASTA, together with the human canonical UniProt flat file (human-Q15436-uniprot.txt); the donkey sequence is parsed from the local UniProt flat file.

## Output

```
## donkey A0A9L0IQB9 length 739 vs human Q15436 length 765
aligned pairs 739; identical 734; identity over aligned pairs 99.32%
coverage of human 96.60%; coverage of donkey 100.00%
aligned blocks (donkey start-end : human start-end, 1-based):
  1-553 : 1-553
  554-739 : 580-765

```

## Interpretation

The donkey model A0A9L0IQB9 (739 aa) is 99.32% identical to human SEC23A over 739 aligned residues and covers 96.6% of the human sequence. It lacks a 26-residue segment corresponding to human 554-579 (CQKFGEYHKDDPSSFRFSETFSLYPQ), located between the helical domain and the C-terminal gelsolin-like repeat; the rest of the protein, including the gelsolin-like repeat (human 632-718), aligns without gaps. The four zinc-coordinating cysteines of the Sec23/Sec24 zinc finger (human Cys61, Cys66, Cys85, Cys88) are conserved at the same positions in donkey. Whether the 26-residue deletion is a real splice form or a gene-model artefact is not known.
