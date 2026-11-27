# acr-18 sequence motif check

Script: `cys_motifs.py` (run as `python cys_motifs.py ../acr-18-uniprot.txt`),
reading the G5EG72 sequence from the cached UniProt record. Raw output in `out.txt`.

## Output

```
length	510
cysteines	6,80,155,169,219,220,355,473
cys_loop_pair	C155-C169	CNLNLQQFPFDQQIC
vicinal_cys	C219-C220	YQKIYDCCPHPFPD
```

## Interpretation

- Cys-loop disulfide pair C155-C169 with 13 intervening residues: the defining
  motif of the Cys-loop ligand-gated ion channel superfamily.
- Vicinal cysteine pair C219-C220 lies in the extracellular domain at the
  position of loop C of the agonist-binding site. In nicotinic acetylcholine
  receptors this vicinal disulfide marks alpha-type subunits, which provide the
  principal face of an agonist-binding site. ACR-18 is therefore an alpha-type
  subunit. This is a sequence-motif inference; it does not identify the agonist.
