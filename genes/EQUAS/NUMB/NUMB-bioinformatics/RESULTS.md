# NUMB: donkey-human sequence comparison

Reproduce: `uv run python genes/EQUAS/NUMB/NUMB-bioinformatics/align.py genes/EQUAS/NUMB/NUMB-uniprot.txt genes/EQUAS/NUMB/NUMB-bioinformatics P49757 P49757-2 P49757-5`

Method: Biopython PairwiseAligner, global mode, BLOSUM62, gap open -10, gap extend -0.5. The human sequence(s) (P49757 P49757-2 P49757-5) are fetched from UniProt REST and saved as FASTA, together with the human canonical UniProt flat file (human-P49757-uniprot.txt); the donkey sequence is parsed from the local UniProt flat file.

## Output

```
## donkey A0A9L0IQ95 length 506 vs human P49757 length 651
aligned pairs 505; identical 490; identity over aligned pairs 97.03%
coverage of human 77.57%; coverage of donkey 99.80%
aligned blocks (donkey start-end : human start-end, 1-based):
  1-218 : 1-218
  219-243 : 317-341
  245-268 : 342-365
  269-506 : 414-651

## donkey A0A9L0IQ95 length 506 vs human P49757-2 length 603
aligned pairs 505; identical 490; identity over aligned pairs 97.03%
coverage of human 83.75%; coverage of donkey 99.80%
aligned blocks (donkey start-end : human start-end, 1-based):
  1-218 : 1-218
  219-243 : 317-341
  245-506 : 342-603

## donkey A0A9L0IQ95 length 506 vs human P49757-5 length 505
aligned pairs 505; identical 490; identity over aligned pairs 97.03%
coverage of human 100.00%; coverage of donkey 99.80%
aligned blocks (donkey start-end : human start-end, 1-based):
  1-243 : 1-243
  245-506 : 244-505

```

## Interpretation

The donkey model A0A9L0IQ95 (506 aa) is 97.03% identical to human NUMB over 505 aligned residues. Its exon structure matches human isoform 5 (P49757-5, 505 aa): it retains the 11-residue PTB-domain insert (human 68-78) and lacks both the segment corresponding to human 219-316 (VSP_047756) and the proline-rich-region insert corresponding to human 366-413 (VSP_004349). Against isoform 5 the alignment covers 100% of the human sequence with a single 1-residue gap. The PTB (PID) domain (donkey 37-173) is fully contained in the aligned block 1-243. These are properties of this predicted sequence, not observations of donkey NUMB protein; other donkey isoforms may exist that are not represented by this entry.
