# FBXL20: donkey-human sequence comparison

Reproduce: `uv run python genes/EQUAS/FBXL20/FBXL20-bioinformatics/align.py genes/EQUAS/FBXL20/FBXL20-uniprot.txt Q96IG2 genes/EQUAS/FBXL20/FBXL20-bioinformatics`

Method: Biopython PairwiseAligner, global mode, BLOSUM62, gap open -10, gap extend -0.5. The human canonical sequence (Q96IG2) is fetched from UniProt REST and saved as Q96IG2.fasta; the donkey sequence is parsed from the local UniProt flat file.

## Output

```
donkey A0A9L0IQA3 length 448; human Q96IG2 length 436
aligned pairs 436; identical 424; identity over aligned pairs 97.25%
coverage of human 100.00%; coverage of donkey 97.32%
aligned blocks (donkey start-end : human start-end, 1-based):
  1-5 : 1-5
  18-448 : 6-436
donkey C-terminus: QRFCRCCIIL human C-terminus: QRFCRCCIIL
```

## Interpretation

The donkey model A0A9L0IQA3 (448 aa) covers the full length of human FBXL20 (Q96IG2, 436 aa) at 97.25% identity, with a 12-residue insertion near the N-terminus (donkey 6-17) upstream of the F-box (donkey F-box 34-80, human 22-68). The C-terminal sequence QRFCRCCIIL, which ends in the CAAX-type prenylation motif of human FBXL20, is identical in donkey.
