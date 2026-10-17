# POLD2: donkey-human sequence comparison

Reproduce from this folder with:

    uv run compare_to_human.py human-P49005-uniprot.txt ../POLD2-uniprot.txt alignment.json

`human-P49005-uniprot.txt` was downloaded from the UniProt REST API (P49005, reviewed human POLD2) on 2026-10-14. The full alignment and counts are in `alignment.json`.

## Result

The donkey sequence A0A9L0IND0 (487 residues) aligns to human P49005 (469 residues) with 95.52% identity among 469 paired residues. Paired coverage is 100.0% of the human sequence and 96.3% of the donkey sequence.

The only length difference is an 18-residue N-terminal extension in the donkey model (MGWSIARGYCCLDTSSTA) preceding the human initiator methionine; no human region lacks a donkey partner. The DNA polymerase delta OB-fold domain and the DNA polymerase alpha/delta/epsilon subunit B (calcineurin-like phosphoesterase-fold) domain annotated on the donkey record are therefore complete.

## Limitations

Pairwise similarity supports homology but does not by itself establish orthology, correctness of the donkey gene model (the N-terminal extension may reflect an upstream start codon choice), or conservation of every interaction.
