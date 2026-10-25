# SNAP23: donkey-human sequence comparison

## Method

The donkey sequence (A0A8C4M285, from `../SNAP23-uniprot.txt`) was aligned globally to the
reviewed human ortholog (O00161, `human-SNAP23-O00161.fasta`, downloaded from the UniProt
REST API on 2026-10-14 together with the flat file `human-SNAP23-O00161-uniprot.txt`) using
Biopython PairwiseAligner (BLOSUM62, gap open -10, gap extend -0.5).

Reproduce from this folder:

```
uv run --with biopython python align_to_human.py ../SNAP23-uniprot.txt human-SNAP23-O00161.fasta 79 80 83 85 87 112 150 200
```

## Output (alignment_output.txt)

```
Donkey A0A8C4M285: 97 aa; human O00161: 211 aa
Paired residues: 97; identical: 88; identity over paired: 90.72%
Coverage of human: 45.97%; coverage of donkey: 100.00%
Human ranges with no aligned donkey residue: 90..170, 174..201, 207..211
Donkey ranges with no aligned human residue: none
Human C79 -> donkey C79
Human C80 -> donkey C80
Human C83 -> donkey C83
Human C85 -> donkey C85
Human C87 -> donkey C87
Human C112 -> not aligned in donkey
Human D150 -> not aligned in donkey
Human I200 -> not aligned in donkey
```

## Interpretation

The donkey entry A0A8C4M285 is a 97-residue product. Donkey residues 1..89 correspond to human SNAP23 residues 1..89: they contain the N-terminal t-SNARE coiled-coil motif (Qb) and the cysteine-rich palmitoylation linker, and all five linker cysteines (human C79, C80, C83, C85, C87) are conserved. The donkey sequence then ends with the 8-residue tail FNIRSRAQ, which has no counterpart in human SNAP23 (the few aligned residues in that tail are gap-placement artefacts of the global alignment). The product lacks the human region 90..211, which includes the C-terminal t-SNARE coiled-coil motif (Qc, human 146..208). The donkey entry therefore represents a truncated SNAP23 gene product with only one of the two SNARE motifs that SNAP23 contributes to a SNARE four-helix bundle. Full-length SNAP23-family entries also exist for donkey in UniProt (for example A0A8C4M333, 211 aa), queried from the UniProt REST API on 2026-10-14.
