# RASGEF1A: donkey-human sequence comparison

Script: `align_to_human.py` (Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5).
Command: `uv run python align_to_human.py ../RASGEF1A-uniprot.txt RASGEF1A-human-Q8N9B8-uniprot.txt 1 41 214 461`
Raw output: `alignment_output.txt`. Human record Q8N9B8 was downloaded from the UniProt REST API (`RASGEF1A-human-Q8N9B8-uniprot.txt`).

## Results

- The donkey sequence A0A9L0J8J4 (516 residues) aligns to human Q8N9B8 (481 residues) with 96.25% identity across 480 paired residues, covering 99.8% of the human sequence.
- Human Met1 aligns to donkey Met37: the donkey gene model carries a 36-residue N-terminal extension not present in human.
- The N-terminal Ras-GEF (REM) domain (human 41-170; donkey 76-205) and the catalytic Ras-GEF (CDC25) domain (human 214-461; donkey 249-496) are both complete; donkey 301-450 are 150/150 identical to human 266-415.

## Interpretation

The donkey protein is a full-length RASGEF1A ortholog with an intact catalytic Ras-GEF domain; the N-terminal extension is outside the annotated domains.
