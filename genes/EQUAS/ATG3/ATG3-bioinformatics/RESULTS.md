# ATG3: donkey-human sequence comparison

Reproduce from this folder with:

    uv run compare_to_human.py human-Q9NT62-uniprot.txt ../ATG3-uniprot.txt alignment.json 264 4 5 104 105 108

`human-Q9NT62-uniprot.txt` was downloaded from the UniProt REST API (Q9NT62, reviewed human ATG3) on 2026-10-14. The full alignment, counts and residue checks are in `alignment.json`.

## Result

The donkey sequence A0A9L0IHI0 (342 residues) aligns to human Q9NT62 (314 residues) with 98.41% identity among 314 paired residues. Paired coverage is 100.0% of the human sequence and 91.81% of the donkey sequence.

The donkey model contains a 28-residue insertion (VVADITKPCWTDFFLPPLLGVNFPPNNP) between human residues 222 and 223; this segment is not one of the human isoform variants listed in the human record. Every human residue has a donkey partner.

Residue checks (human position -> donkey residue): the catalytic Cys-264 (glycyl thioester intermediate) aligns to donkey Cys-292; N-terminal curvature-sensing-motif residues Val-4 and Ile-5 and LIR-motif residues Asp-104, Gly-105 and Val-108 are identical at the same positions.

## Limitations

The insertion lies in the catalytic core region downstream of the flexible region and may come from an extra exon or a gene-model error; other donkey ATG3 entries (for example a 314-residue model) lack it. Whether the inserted protein is active is not measured. Pairwise similarity does not by itself establish orthology.
