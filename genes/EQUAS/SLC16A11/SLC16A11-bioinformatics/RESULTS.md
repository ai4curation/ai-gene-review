# SLC16A11: donkey-human sequence comparison

Script: `align_to_human.py` (Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5; with per-50-residue identity windows).
Command: `uv run python align_to_human.py ../SLC16A11-uniprot.txt SLC16A11-human-Q8NCK7-uniprot.txt`
Raw output: `alignment_output.txt`. Human record Q8NCK7 was downloaded from the UniProt REST API (`SLC16A11-human-Q8NCK7-uniprot.txt`).

## Results

- The donkey sequence A0A9L0JV53 (439 residues) aligns to human Q8NCK7 (447 residues) with 80.60% identity across 397 paired residues, but identity is not uniform.
- Donkey residues 1-100 are essentially unrelated to human: only 21 of 62 forced-aligned pairs are identical (donkey 1-50: 16/48; donkey 51-100: 5/14), and the donkey N-terminus (EPARPGSGEK...) does not begin with methionine.
- Donkey residues 101-439 align to human 113-447 at high identity (e.g. donkey 201-250: 48/50 identical to human 209-258).
- The human N-terminal region containing predicted transmembrane helices 1-3 (human 12-32, 54-74, 82-102) therefore has no homologous counterpart in the donkey model; donkey Phobius predicts helices only from residue 131 onward.

## Interpretation

A0A9L0JV53 is an N-terminally truncated/misassembled gene model of donkey SLC16A11: the C-terminal ~340 residues are clearly orthologous (MCT11-specific), but the first three of the twelve MFS transmembrane helices are missing. Transport activity of this exact polypeptide is therefore doubtful, although the donkey gene itself is expected to encode a full-length transporter.
