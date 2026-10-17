# PIKFYVE: donkey A0A9L0JQ61 versus human PIKFYVE isoforms

Reproduce from this folder with:

    uv run compare_to_human.py human-Q9Y2I7-uniprot.txt ../PIKFYVE-uniprot.txt alignment.json 164 167 180 183 188 191 210 213
    uv run compare_to_human.py human-Q9Y2I7-3.fasta ../PIKFYVE-uniprot.txt alignment-isoform3.json

`human-Q9Y2I7-uniprot.txt` (reviewed human PIKFYVE, canonical isoform 1, 2098 residues) and `human-Q9Y2I7-3.fasta` (human isoform 3) were downloaded from the UniProt REST API on 2026-10-14. Full alignments and counts are in the two JSON files.

## Result 1: against canonical human PIKFYVE

The donkey sequence A0A9L0JQ61 (460 residues) aligns to human Q9Y2I7 (2098 residues) with 94.35% identity among 460 paired residues. Paired coverage is 21.93% of the human sequence and 100.0% of the donkey sequence.

Human segments without a donkey partner are 107-202 (with two isolated paired residues) and 546-2098. The donkey protein therefore lacks most of the FYVE-type zinc finger (human 158-218): of the eight zinc-binding cysteines, Cys-164, Cys-167, Cys-180, Cys-183, Cys-188 and Cys-191 have no donkey counterpart and only Cys-210 and Cys-213 are retained (donkey Cys-122 and Cys-125). It also lacks the chaperonin-like domain (human 616-868) and the entire PIPK catalytic domain (human 1758-2084). The DEP domain (human 365-440; donkey 277-352) is retained.

## Result 2: against human isoform 3

The donkey sequence aligns to human isoform Q9Y2I7-3 (462 residues) with 96.08% identity among 459 paired residues, covering 99.35% of the human isoform and 99.78% of the donkey sequence, with no human segment lacking a donkey partner. Human isoform 3 replaces residues 109-203 with NSLQHPQEN and ends after a short GRR tail at residue 548 (UniProt VAR_SEQ VSP_040109, VSP_040110, VSP_040111); the donkey sequence contains the same junction (...RRPSAVLENSLQHPQENTGDLR...) and the same C-terminal ...PADQKGRR.

## Interpretation and limitations

A0A9L0JQ61 is the donkey counterpart of the short human PIKFYVE splice isoform 3, not of the full-length kinase. Full-length donkey PIKFYVE products exist as separate UniProt entries (for example A0A8C4L106, 2108 residues). The short isoform has no lipid-kinase domain and no complete PtdIns3P-binding FYVE finger, so the catalytic and endomembrane-targeting properties of full-length PIKFYVE cannot be transferred to it. Its own function, if any, is not characterized in the human record, which cites only cDNA sequencing for isoforms 2-4.
