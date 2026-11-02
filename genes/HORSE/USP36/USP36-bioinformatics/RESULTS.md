# USP36: horse (F6W2H6) vs human (Q9P275) sequence comparison

Reproduce (from the repository root):

- `uv run python genes/HORSE/USP36/USP36-bioinformatics/align.py genes/HORSE/USP36/USP36-uniprot.txt genes/HORSE/USP36/USP36-bioinformatics Q9P275 --pos 131,382` (output: `alignment_output.txt`; fetches `Q9P275.fasta` and `human-Q9P275-uniprot.txt` from UniProt REST)
- `uv run --script domain_identity.py ../USP36-uniprot.txt Q9P275.fasta <start> <end>` run from this folder for each window (output: `domain_identity_output.txt`)

Method: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5.
`align.py` is a copy of `genes/EQUAS/USP36/USP36-bioinformatics/align.py` with "donkey" relabelled "query".

## Output

```
## query F6W2H6 length 1123 vs human Q9P275 length 1123
aligned pairs 1114; identical 867; identity over aligned pairs 77.83%
coverage of human 99.20%; coverage of query 99.20%
query C131 aligns to human C131
query H382 aligns to human H382
```

```
human 1-437: aligned pairs 437, identical 412, identity 94.28%
human 122-423: aligned pairs 302, identical 290, identity 96.03%
human 438-1123: aligned pairs 677, identical 455, identity 67.21%
human 990-1123: aligned pairs 134, identical 109, identity 81.34%
```

## Interpretation

Horse F6W2H6 is a full-length USP36 product: it is the same length as human USP36 (1123 aa) and
aligns over 99.2% of both sequences, with only small indels confined to the long disordered
C-terminal region. The USP catalytic domain (human 122-423) is 96.0% identical, and the catalytic
nucleophile Cys131 and proton acceptor His382 are conserved at the same positions. The
disordered middle region (human 438-1123) is less conserved (67.2%), while the C-terminal block
(human 990-1123), which includes the basic stretches reported to direct nucleolar localization
in human USP36, is 81.3% identical. Nothing in the comparison suggests a fragment, isoform or
defective gene model. Both genes are classified in PANTHER subfamily PTHR24006:SF653
(UBIQUITIN CARBOXYL-TERMINAL HYDROLASE 36) by their UniProt records.
