# SLC27A5: donkey-human sequence comparison

Reproduce: `uv run python genes/EQUAS/SLC27A5/SLC27A5-bioinformatics/align.py genes/EQUAS/SLC27A5/SLC27A5-uniprot.txt genes/EQUAS/SLC27A5/SLC27A5-bioinformatics Q9Y2P5`

Method: Biopython PairwiseAligner, global mode, BLOSUM62, gap open -10, gap extend -0.5. The human sequence(s) (Q9Y2P5) are fetched from UniProt REST and saved as FASTA, together with the human canonical UniProt flat file (human-Q9Y2P5-uniprot.txt); the donkey sequence is parsed from the local UniProt flat file.

## Output

```
## donkey A0A9L0JNL2 length 700 vs human Q9Y2P5 length 690
aligned pairs 690; identical 561; identity over aligned pairs 81.30%
coverage of human 100.00%; coverage of donkey 98.57%
aligned blocks (donkey start-end : human start-end, 1-based):
  11-700 : 1-690

```

## Interpretation

The donkey model A0A9L0JNL2 (700 aa) is 81.30% identical to human SLC27A5 over 690 aligned residues, covering the full human sequence; donkey has a 10-residue N-terminal extension (MDISQGEAGA) before the residue aligned to human Met1. The N-terminal membrane-anchoring region (human TM 31-51/56-76) and the AMP-binding (ANL superfamily) catalytic domain are covered by the single ungapped aligned block, and the donkey record carries the PROSITE AMP_BINDING signature (PS00455).
