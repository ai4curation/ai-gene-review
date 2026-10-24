# NUMB (donkey A0A9L0IHZ0): ortholog comparison

Reproduce (from the repository root):
`uv run --script genes/EQUAS/NUMB__A0A9L0IHZ0/NUMB__A0A9L0IHZ0-bioinformatics/compare_orthologs.py`
Raw output: `compare_orthologs_output.txt`. Human and mouse UniProt flat files are saved alongside
(`human-P49757-uniprot.txt`, `mouse-Q9QZS3-uniprot.txt`).

Method: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, gap extend -0.5. Motif positions
are simple pattern matches. PANTHER assignments are read from the local
`interpro/panther/PTHR47368/PTHR47368-entries.csv` table and the donkey UniProt DR PANTHER line.

## Key output

```
## donkey A0A9L0IHZ0 length 652; PID domain (37, 173)
## vs human P49757 length 651: aligned pairs 650; identical 630; identity 96.92%
human T102 (T) maps to donkey 102 (T)
## vs mouse Q9QZS3 length 653: aligned pairs 652; identical 614; identity 94.17%
P49757 Homo sapiens NUMB -> PTHR47368:SF5 PROTEIN NUMB HOMOLOG
Q9QZS3 Mus musculus Numb -> PTHR47368:SF5 PROTEIN NUMB HOMOLOG
Q9Y6R0 Homo sapiens NUMBL -> PTHR47368:SF4 NUMB-LIKE PROTEIN
P16554 Drosophila melanogaster numb -> PTHR47368:SF2 PID DOMAIN-CONTAINING PROTEIN
A0A9L0IHZ0 (UniProt DR PANTHER) -> ['PTHR47368', 'PTHR47368:SF5']
```

## Interpretation

Donkey A0A9L0IHZ0 is classified in PANTHER subfamily PTHR47368:SF5 (PROTEIN NUMB HOMOLOG), the same
subfamily as human NUMB P49757 and mouse Numb Q9QZS3, and separate from the NUMBL subfamily (SF4)
and from Drosophila numb (SF2). The 652-residue donkey protein aligns end to end with human canonical
NUMB (96.92% identity over 650 aligned residues, only single-residue gaps), so its exon content matches
human isoform 1 (p72): it carries the PTB-domain insert and the proline-rich-region insert.
The threonine at human position 102 (the AAK1 phosphorylation site) is conserved at donkey position 102,
and the C-terminal DPF (donkey 343, 615) and NPF (donkey 638) motifs sit at the same positions as in
human NUMB (343, 614; 637). This establishes one-to-one orthology within the NUMB subfamily, which
supports transfer of the experimentally established human and mouse NUMB functions; it does not
itself demonstrate any activity of the donkey protein. No experimental data on donkey NUMB exist.
