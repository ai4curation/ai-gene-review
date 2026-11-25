# SLC27A5 (horse): comparison of gene models F6X2Q2 and A0A5F5PXH2 with human Q9Y2P5

Reproduce (from the repository root):
`uv run --script genes/HORSE/SLC27A5/SLC27A5-bioinformatics/compare_models.py`

Inputs: `../SLC27A5-uniprot.txt` (F6X2Q2, the benchmark accession, 671 aa, Ensembl
ENSECAT00000018051.4); `A0A5F5PXH2.fasta` and `horse-A0A5F5PXH2-uniprot.txt` (700 aa,
Ensembl ENSECAT00000070308.2; both transcripts belong to the same Ensembl gene
ENSECAG00000046881.1); `Q9Y2P5.fasta` (human SLC27A5, Swiss-Prot). All were fetched from
the UniProt REST API on 2026-10-21.

Method: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, gap extend -0.5,
free end gaps. Raw output is in `compare_models_output.txt`.

## Output

```
## F6X2Q2 (len 671) vs A0A5F5PXH2 (len 700)
aligned pairs 666; identical 615; identity 92.34%
aligned blocks (A start-end : B start-end, 1-based):
  1-599 : 1-599  (block identity 100.0%)
  600-605 : 604-609  (block identity 33.3%)
  606-630 : 618-642  (block identity 20.0%)
  636-671 : 643-678  (block identity 25.0%)

## F6X2Q2 (len 671) vs human Q9Y2P5 (len 690)
aligned pairs 656; identical 492; identity 75.00%
aligned blocks (A start-end : B start-end, 1-based):
  11-599 : 1-589  (block identity 80.8%)
  600-605 : 594-599  (block identity 33.3%)
  606-630 : 608-632  (block identity 24.0%)
  636-671 : 633-668  (block identity 22.2%)

## A0A5F5PXH2 (len 700) vs human Q9Y2P5 (len 690)
aligned pairs 690; identical 558; identity 80.87%
aligned blocks (A start-end : B start-end, 1-based):
  11-700 : 1-690  (block identity 80.9%)
```

## Interpretation

F6X2Q2 residues 1-599 are identical to the 700-aa horse model A0A5F5PXH2 and align to
human SLC27A5 residues 1-589 at 80.8% identity (horse has a 10-residue N-terminal
extension, MDISQGEAGA, also present in the donkey model). After residue 599 the two horse
models diverge completely: the F6X2Q2 C-terminal 72 residues align to the conserved
SLC27A5 C-terminus at only 20-33% identity in short gapped blocks, which is background
level. A0A5F5PXH2, in contrast, is 80.9% identical to human over the whole human length,
including the C-terminus.

Consequently F6X2Q2 lacks the C-terminal AMP-binding_C subdomain (Pfam PF13193), which
UniProt maps to residues 576-652 of A0A5F5PXH2 and which is absent from the F6X2Q2 domain
annotations (only PF00501, 130-453, is mapped). The N-terminal membrane-anchoring region
(human TM 31-51 and 56-76, horse 41-61 and 66-86; called a signal peptide 1-31 by SignalP
on both horse records) and the large N-terminal AMP-binding domain (PF00501, with the
PROSITE AMP_BINDING signature) are intact.

The most likely explanation is that F6X2Q2 is an alternative or erroneous gene model with
an aberrant 3' end (alternative last exon, intron read-through or frameshift) rather than a
conserved product; the 700-aa A0A5F5PXH2 model matches the human, and the donkey
(A0A9L0JNL2, 700 aa), full-length protein. This analysis cannot tell whether a
transcript encoding the F6X2Q2 C-terminus is expressed in horse.
