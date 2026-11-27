# USP36: donkey-human sequence comparison

Reproduce: `uv run python genes/EQUAS/USP36/USP36-bioinformatics/align.py genes/EQUAS/USP36/USP36-uniprot.txt genes/EQUAS/USP36/USP36-bioinformatics Q9P275 --pos 131,415`

Method: Biopython PairwiseAligner, global mode, BLOSUM62, gap open -10, gap extend -0.5. The human sequence(s) (Q9P275) are fetched from UniProt REST and saved as FASTA, together with the human canonical UniProt flat file (human-Q9P275-uniprot.txt); the donkey sequence is parsed from the local UniProt flat file.

## Output

```
## donkey A0A9L0JCH5 length 1156 vs human Q9P275 length 1123
aligned pairs 1114; identical 870; identity over aligned pairs 78.10%
coverage of human 99.20%; coverage of donkey 96.37%
aligned blocks (donkey start-end : human start-end, 1-based):
  1-252 : 1-252
  286-470 : 253-437
  471-577 : 439-545
  580-861 : 546-827
  862-912 : 834-884
  913-926 : 886-899
  933-969 : 900-936
  971-1022 : 937-988
  1023-1156 : 990-1123
donkey C131 aligns to human C131
donkey H415 aligns to human H382

```

## Interpretation

The donkey model A0A9L0JCH5 (1156 aa) is 78.10% identical to human USP36 over 1114 aligned residues (99.2% of human covered). The main difference is a 33-residue insertion (donkey 253-285) inside the USP catalytic domain, between the Cys-box and His-box regions, plus small indels in the long C-terminal low-complexity region. The catalytic nucleophile (donkey Cys131 = human Cys131) and proton acceptor (donkey His415 = human His382) of the USP domain are conserved. The effect of the inserted segment on activity has not been tested.
