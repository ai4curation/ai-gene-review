# At5g08650 (cpLEPA, Q9FNM5) sequence comparison

Script: `compare_lepa.py` (run with `uv run python compare_lepa.py`; raw output in
`compare_lepa_output.txt`). Sequences and PANTHER subfamily assignments were fetched
live from UniProt REST. Identity is from a global Needleman-Wunsch alignment
(BLOSUM62, gap open -10, extend -0.5) of full-length precursors, so the
51-residue chloroplast transit peptide of Q9FNM5 lowers the values somewhat.

## Subfamily placement

| Accession | Protein | PANTHER subfamily | Global identity to Q9FNM5 |
|---|---|---|---|
| P60785 | E. coli LepA (EF4) | PTHR43512:SF4 | 53.8% |
| Q9FLE4 | Arabidopsis GUF1 (mitochondrial) | PTHR43512:SF7 | 49.8% |
| Q8N442 | human GUF1 (mitochondrial) | PTHR43512:SF7 | 49.0% |
| P46943 | yeast GUF1 (mitochondrial) | PTHR43512:SF7 | 44.2% |

Q9FNM5 is in PTHR43512:SF4 together with E. coli LepA, separate from the
mitochondrial GUF1 subfamily SF7. The function-bearing PAINT node for ribosome
binding and positive regulation of translation (PTN002460656, seeded by yeast
GUF1 and E. coli LepA) lies above both subfamilies; the mitochondrion and
mitochondrial-ribosome-binding terms are placed on the eukaryotic mitochondrial
node PTN000563148 (see `interpro/panther/PTHR43512/PTHR43512-paint.tsv`), which
does not include Q9FNM5.

## Conserved G-domain motifs in Q9FNM5

- G1 (P-loop): `AHIDHGKS` at residue 93 (matches UniProt GTP-binding site 93..100)
- G3: `DTPGH` at residue 158 (UniProt GTP-binding site 158..162)
- G4: `NKID` at residue 212 (UniProt GTP-binding site 212..215)

The translational-GTPase nucleotide-binding motifs are intact, consistent with a
catalytically competent GTPase. No GTPase assay has been reported for the
Arabidopsis protein; this is a sequence-based inference.
