# PIKFYVE re-review: donkey A0A9L0JQ61 versus the donkey canonical product (2026-10-21)

Reproduce from this folder with:

    uv run --script compare_to_donkey_canonical_rereview.py ../PIKFYVE-uniprot.txt donkey-A0A8C4L106-canonical.fasta

`donkey-A0A8C4L106-canonical.fasta` was downloaded from the UniProt REST API on 2026-10-21. Raw output is in `compare_to_donkey_canonical_rereview.out`.

## Gene model

All seven donkey PIKFYVE UniProt entries map to the same Ensembl gene, ENSEASG00005003072 (Ensembl REST lookup, 2026-10-21). The Ensembl canonical transcript of that gene is ENSEAST00005004444, whose product is A0A8C4L106 (2108 residues). A0A9L0JQ61 is the product of a non-canonical transcript, ENSEAST00005054447 (460 residues). Both are placed in PANTHER PTHR46715:SF1 by UniProt, the same subfamily as human Q9Y2I7 and mouse Q9Z1T6 PIKFYVE. Yeast Fab1 (P34756) is placed in a different PANTHER family, PTHR45748:SF7.

## Alignment

The short entry aligns to the donkey canonical product with 99.57% identity among 460 paired residues (458 identical), covering 100.00% of the short entry and 21.82% of the canonical product. Canonical segments without a short-entry partner are 117-213 (the region replaced by the NSLQHPQEN junction, covering most of the FYVE finger), and 567-2108 (the C-terminal region, including the chaperonin-like and PIPK catalytic domains); a further 8-residue segment at 556-563 is the alignment of the GRR tail.

## Interpretation

A0A9L0JQ61 is an alternative splice product of the donkey PIKFYVE gene, matching human isoform 3, and not a separate gene. The catalytic domain is encoded only by the canonical and other full-length transcripts, so the gene's lipid-kinase function belongs to those products.
