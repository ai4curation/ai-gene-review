# CADM1: donkey-human sequence comparison

## Method

The donkey sequence (A0A9L0IX39, from `../CADM1-uniprot.txt`) was aligned globally to the
reviewed human ortholog (Q9BY67, `human-CADM1-Q9BY67.fasta`, downloaded from the UniProt
REST API on 2026-10-14 together with the flat file `human-CADM1-Q9BY67-uniprot.txt`) using
Biopython PairwiseAligner (BLOSUM62, gap open -10, gap extend -0.5).

Reproduce from this folder:

```
uv run --with biopython python align_to_human.py ../CADM1-uniprot.txt human-CADM1-Q9BY67.fasta 
```

## Output (alignment_output.txt)

```
Donkey A0A9L0IX39: 390 aa; human Q9BY67: 442 aa
Paired residues: 387; identical: 373; identity over paired: 96.38%
Coverage of human: 87.56%; coverage of donkey: 99.23%
Human ranges with no aligned donkey residue: 332..359, 407..429, 439..442
Donkey ranges with no aligned human residue: 16..18
```

## Interpretation

The donkey CADM1 protein matches human CADM1 at 96.38% identity over 387 paired residues. Its extracellular region (three Ig-like domains), stalk and transmembrane segment are conserved. The donkey stalk lacks the segment corresponding to human 333..360, which is the region absent from the naturally spliced human isoform 5. The cytoplasmic tail differs: after the conserved juxtamembrane residues the donkey sequence ends with GLFSLTSSPRIK, whereas human CADM1 continues with a tail ending in the PDZ-binding residues EYFI. The donkey entry therefore lacks the human C-terminal region that binds protein 4.1 (EPB41L3) and PDZ proteins (MPP2, MPP3, PALS2); whether this is a natural alternative terminal exon or a gene-model artefact is not known.
