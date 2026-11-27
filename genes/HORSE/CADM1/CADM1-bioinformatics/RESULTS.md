# CADM1: horse-human sequence comparison

## Method

The horse sequence (A0A5F5PGJ5, from `../CADM1-uniprot.txt`) was aligned globally to the
reviewed human ortholog (Q9BY67, `human-CADM1-Q9BY67.fasta`; flat file
`human-CADM1-Q9BY67-uniprot.txt`, both downloaded from the UniProt REST API on 2026-10-21)
using Biopython PairwiseAligner (BLOSUM62, gap open -10, gap extend -0.5). The script is a
copy of the donkey CADM1 script with species labels changed.

Reproduce from this folder:

```
uv run --with biopython python align_to_human.py ../CADM1-uniprot.txt human-CADM1-Q9BY67.fasta 332 361 442
```

## Output (alignment_output.txt)

```
Horse A0A5F5PGJ5: 417 aa; human Q9BY67: 442 aa
Paired residues: 414; identical: 410; identity over paired: 99.03%
Coverage of human: 93.67%; coverage of horse: 99.28%
Human ranges with no aligned horse residue: 332..359
Horse ranges with no aligned human residue: 16..18
Human D332 -> not aligned in horse
Human S361 -> horse S336
Human I442 -> horse I417
```

## Interpretation

The horse CADM1 protein matches human CADM1 at 99.03% identity over 414 paired residues. The only
differences in length are three extra alanines in the horse signal-peptide poly-Ala tract (horse
16..18) and a 28-residue gap in the extracellular stalk at human 332..359. That gap is the
Thr-rich segment that UniProt records as missing from human isoform 5 (VAR_SEQ 333..360; the
one-residue offset is an alignment ambiguity because aspartate flanks both ends of the segment).
The horse entry therefore corresponds to the human isoform 5 splice form (exons 7/8/11, called SP4
in PMID:22438059), not to the displayed human isoform 1 (SP1, exons 7/8/9/11). It is a complete
product, not a fragment: the signal peptide, all three Ig-like domains, the transmembrane segment
and the entire cytoplasmic tail are present, and the tail ends with the same PDZ-binding residues
(EYFI, horse I417 = human I442) used by human and rodent CADM1 to bind protein 4.1 and PDZ proteins.
