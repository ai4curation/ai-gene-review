# GEMIN7: donkey-human sequence comparison

Reproduce: `uv run python genes/EQUAS/GEMIN7/GEMIN7-bioinformatics/align.py genes/EQUAS/GEMIN7/GEMIN7-uniprot.txt genes/EQUAS/GEMIN7/GEMIN7-bioinformatics Q9H840`

Method: Biopython PairwiseAligner, global mode, BLOSUM62, gap open -10, gap extend -0.5. The human sequence(s) (Q9H840) are fetched from UniProt REST and saved as FASTA, together with the human canonical UniProt flat file (human-Q9H840-uniprot.txt); the donkey sequence is parsed from the local UniProt flat file.

## Output

```
## donkey A0A9L0ICL9 length 206 vs human Q9H840 length 131
aligned pairs 131; identical 115; identity over aligned pairs 87.79%
coverage of human 100.00%; coverage of donkey 63.59%
aligned blocks (donkey start-end : human start-end, 1-based):
  76-206 : 1-131

```

## Interpretation

The donkey model A0A9L0ICL9 (206 aa) contains a 75-residue N-terminal extension with no counterpart in human GEMIN7; donkey residues 76-206 align without gaps to the complete human protein (1-131) at 87.79% identity. The Sm-like domain (donkey 140-206; human Sm domain 65-131) lies within the aligned block. The extension may reflect an upstream start in the gene model and is a property of this predicted sequence, not an observation of donkey GEMIN7 protein.
