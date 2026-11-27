# CADM1 (donkey canonical product A0A9L0IJE9): comparison with human and mouse CADM1

## Method

The donkey sequence (A0A9L0IJE9, from `../CADM1__A0A9L0IJE9-uniprot.txt`) was aligned globally
to reviewed human CADM1 (Q9BY67) and mouse Cadm1 (Q8R5M8). The FASTA and flat files were
downloaded from the UniProt REST API on 2026-10-21 and are saved in this folder. The alignment
uses Biopython PairwiseAligner (BLOSUM62, gap open -10, gap extend -0.5). Region boundaries are
read from the human flat file at run time. Reproduce from this folder:

```
uv run --script compare_canonical_to_orthologs.py
```

## Output (alignment_output.txt)

```
Donkey A0A9L0IJE9: 473 aa; C-terminal 4 residues: EYFI
Human Q9BY67: 442 aa; C-terminal 4 residues: EYFI
Mouse Q8R5M8: 456 aa; C-terminal 4 residues: EYFI
vs human Q9BY67: paired 441, identical 436, identity over paired 98.87%
vs mouse Q8R5M8: paired 455, identical 451, identity over paired 99.12%
Per-region identity, human Q9BY67 coordinates:
  SIGNAL 1..44: 44/44 aligned, 42 identical
  TOPO_DOM Extracellular 45..374: 329/330 aligned, 326 identical
  TRANSMEM Helical 375..395: 21/21 aligned, 21 identical
  TOPO_DOM Cytoplasmic 396..442: 47/47 aligned, 47 identical
  DOMAIN Ig-like V-type 45..139: 95/95 aligned, 95 identical
  DOMAIN Ig-like C2-type 1 144..238: 95/95 aligned, 93 identical
  DOMAIN Ig-like C2-type 2 243..329: 87/87 aligned, 87 identical
Human cytoplasmic tail : GRYFARHKGTYFTHEAKGADDAADADTAIINAEGGQNNSEEKKEYFI
Donkey aligned residues: GRYFARHKGTYFTHEAKGADDAADADTAIINAEGGQNNSEEKKEYFI
```

## Interpretation

The donkey canonical CADM1 product is 98.87% identical to human CADM1 and 99.12% identical to mouse Cadm1 over the aligned residues.
The V-type Ig domain, which carries the homophilic and CRTAM-binding interface, is identical to human over all 95 residues.
The transmembrane helix and the whole 47-residue cytoplasmic tail are also identical to human, including the protein 4.1-binding juxtamembrane region and the C-terminal EYFI PDZ-binding motif.
The donkey product is longer than human canonical isoform 1 (473 vs 442 aa); since every human residue except one is paired, the 32 unpaired donkey residues are an insertion relative to the human canonical isoform. This script does not locate the insertion; CADM1 has alternatively spliced stalk exons, which is a plausible but untested explanation.
All three proteins are classified in PANTHER subfamily PTHR45889:SF2 (CELL ADHESION MOLECULE 1), so donkey A0A9L0IJE9 is the 1:1 ortholog of the experimentally characterised human and mouse proteins.
No donkey-specific experimental data were found, so every functional statement for this protein is an inference from these orthologs.
