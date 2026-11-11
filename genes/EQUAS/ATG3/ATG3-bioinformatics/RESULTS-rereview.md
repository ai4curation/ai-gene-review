# ATG3 (donkey A0A9L0IHI0): gene-model comparison, 2026-10-21 re-review

Reproduce from this folder with:

    uv run --script compare_isoforms_rereview.py atg3_models_rereview.fasta

`atg3_models_rereview.fasta` holds the UniProt FASTA records of the six donkey ATG3 entries, the horse 342-residue model A0A3Q2L0A4 and reviewed human Q9NT62 (downloaded 2026-10-21). The script output is saved in `isoforms_rereview_output.txt`. `donkey-A0A9L0J149-uniprot.txt` is the UniProt flat file of the 314-residue donkey entry.

## Result

Removing the 28-residue segment VVADITKPCWTDFFLPPLLGVNFPPNNP from A0A9L0IHI0 gives exactly A0A9L0J149, the 314-residue donkey ATG3 entry: the two entries are products of one gene that differ only by this segment. A0A9L0J149 is the same length as human ATG3 and is 309/314 = 98.41% identical to it without gaps.

Both entries map to the same gene: A0A9L0IHI0 is Ensembl ENSEAST00005048432.1 / RefSeq XP_014694150.1 and A0A9L0J149 is Ensembl ENSEAST00005037718.1 / RefSeq XP_014694151.1, both on gene ENSEASG00005011413.2 (NCBI GeneID 106829515). The benchmark accession A0A9L0IHI0 is therefore an alternative splice product (the longer RefSeq transcript variant) of donkey ATG3, and the 314-residue A0A9L0J149 is the product that matches the canonical human ATG3 protein.

The horse model A0A3Q2L0A4 (342 residues) carries the identical segment, so the extra exon is predicted in both equid genomes. None of the other donkey ATG3 entries and not human Q9NT62 contain it.

Residue checks: the catalytic Cys-264 of human ATG3 is Cys-264 in A0A9L0J149 and Cys-292 in A0A9L0IHI0; the ATG12-acceptor Lys-243 is Lys-243 in A0A9L0J149 and Lys-271 in A0A9L0IHI0. The insertion lies after residue 222, upstream of both.

## Limitations

The analysis shows that the insertion is a gene-model (splice) difference, not whether the long transcript is expressed or whether its protein is active. The insertion sits 21 residues upstream of the ATG12-acceptor lysine and 42 upstream of the catalytic cysteine, inside the catalytic core, so an effect on activity cannot be ruled out from sequence alone.
