# KDM4C: donkey-human sequence comparison

## Method

The donkey sequence (A0A9L0K3L6, from `../KDM4C-uniprot.txt`) was aligned globally to the
reviewed human ortholog (Q9H3R0, `human-KDM4C-Q9H3R0.fasta`, downloaded from the UniProt
REST API on 2026-10-14 together with the flat file `human-KDM4C-Q9H3R0-uniprot.txt`) using
Biopython PairwiseAligner (BLOSUM62, gap open -10, gap extend -0.5).

Reproduce from this folder:

```
uv run --with biopython python align_to_human.py ../KDM4C-uniprot.txt human-KDM4C-Q9H3R0.fasta 134 190 192 200 208 236 242 243 278 308 310
```

## Output (alignment_output.txt)

```
Donkey A0A9L0K3L6: 1052 aa; human Q9H3R0: 1056 aa
Paired residues: 1052; identical: 962; identity over paired: 91.44%
Coverage of human: 99.62%; coverage of donkey: 100.00%
Human ranges with no aligned donkey residue: 396..396, 474..474, 488..489
Donkey ranges with no aligned human residue: none
Human Y134 -> donkey Y134
Human H190 -> donkey H190
Human E192 -> donkey E192
Human N200 -> donkey N200
Human K208 -> donkey K208
Human C236 -> donkey C236
Human H242 -> donkey H242
Human K243 -> donkey K243
Human H278 -> donkey H278
Human C308 -> donkey C308
Human C310 -> donkey C310
```

## Interpretation

The donkey KDM4C protein matches human KDM4C at 91.44% identity over 1052 paired residues, covering 99.62% of the human sequence. All human 2-oxoglutarate-binding residues (Y134, N200, K208, K243), catalytic Fe-binding residues (H190, E192, H278) and Zn-binding residues (C236, H242, C308, C310) of the JmjC domain are conserved, so the donkey protein is predicted to retain the 2-oxoglutarate/Fe(II)-dependent histone demethylase activity of KDM4C.
