# FOXJ3: donkey-human sequence comparison

Reproduce from this folder with:

    uv run compare_to_human.py human-Q9UPW0-uniprot.txt ../FOXJ3-uniprot.txt alignment.json

`human-Q9UPW0-uniprot.txt` was downloaded from the UniProt REST API (Q9UPW0, reviewed human FOXJ3) on 2026-10-14. The full alignment and counts are in `alignment.json`.

## Result

The donkey sequence A0A9L0JKH1 (580 residues) aligns to human Q9UPW0 (622 residues) with 98.1% identity among 579 paired residues. Paired coverage is 93.09% of the human sequence and 99.83% of the donkey sequence.

The only human segment without a donkey partner is residues 211-253, an internal stretch C-terminal to the fork-head domain inside the region that both records annotate as disordered. The fork-head DNA-binding domain (donkey 78-173) aligns without gaps, and the N-terminal 210 residues are identical except for one substitution.

## Limitations

The missing internal segment probably reflects alternative splicing or the gene model; the donkey gene also has other FOXJ3 entries (for example a 623-residue model). Pairwise similarity does not establish that the missing disordered segment is functionally dispensable.
