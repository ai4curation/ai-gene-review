# GPC3: donkey-human sequence comparison

## Method

The donkey sequence (A0A9L0J2B1, from `../GPC3-uniprot.txt`) was aligned globally to the
reviewed human ortholog (P51654, `human-GPC3-P51654.fasta`, downloaded from the UniProt
REST API on 2026-10-14 together with the flat file `human-GPC3-P51654-uniprot.txt`) using
Biopython PairwiseAligner (BLOSUM62, gap open -10, gap extend -0.5).

Reproduce from this folder:

```
uv run --with biopython python align_to_human.py ../GPC3-uniprot.txt human-GPC3-P51654.fasta 358 359 495 509 554
```

## Output (alignment_output.txt)

```
Donkey A0A9L0J2B1: 565 aa; human P51654: 580 aa
Paired residues: 555; identical: 514; identity over paired: 92.61%
Coverage of human: 95.69%; coverage of donkey: 98.23%
Human ranges with no aligned donkey residue: 21..39, 49..54
Donkey ranges with no aligned human residue: 3..11, 17..17
Human R358 -> donkey R343
Human S359 -> donkey S344
Human S495 -> donkey S480
Human S509 -> donkey S494
Human N554 -> donkey N539
```

## Interpretation

The donkey GPC3 protein matches human GPC3 at 92.61% identity over 555 paired residues; the unaligned human segments are in the signal peptide/N-terminal region (human 21..39, 49..54). The furin-like cleavage site (human R358/S359), the two heparan sulfate attachment serines (human S495, S509) and the GPI-anchor asparagine (human N554) are all conserved in the donkey sequence.
