# GPAT2: donkey-human sequence comparison

Reproduce from this folder with:

    uv run compare_to_human.py human-Q6NUI2-uniprot.txt ../GPAT2-uniprot.txt alignment.json 205 206 209 210

`human-Q6NUI2-uniprot.txt` was downloaded from the UniProt REST API (Q6NUI2, reviewed human GPAT2) on 2026-10-14. The full alignment, counts and residue checks are in `alignment.json`.

## Result

The donkey sequence A0A9L0ILJ0 (718 residues) aligns to human Q6NUI2 (795 residues) with 80.25% identity among 714 paired residues. Paired coverage is 89.81% of the human sequence and 99.44% of the donkey sequence.

Identity is high across the N-terminal acyltransferase region; the HXXXXD catalytic motif (human 205-210) is conserved in donkey as H205, K206, L209, D210 at the same positions. From about donkey residue 632 onward the donkey sequence no longer matches human (human segments 651-702, 746-764 and 779-786 have no donkey partner, and the aligned residues in this tail are mostly non-identical), so the donkey C-terminal ~85 residues differ from the human C-terminus.

## Limitations

The divergent C-terminus may reflect an alternative last exon or a gene-model error; other donkey GPAT2 entries (for example an 800-residue model) exist. Conservation of the catalytic motif does not demonstrate enzymatic activity, and the C-terminal difference may affect membrane topology or partner binding. Pairwise similarity does not by itself establish orthology.
