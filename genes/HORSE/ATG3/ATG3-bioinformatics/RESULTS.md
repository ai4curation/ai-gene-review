# ATG3: horse A0A3Q2L0A4 vs human Q9NT62

Reproduce from this folder with:

    uv run --script compare_horse_human.py human-Q9NT62-uniprot.txt ../ATG3-uniprot.txt horse-other-ATG3-entries.fasta alignment.json 4 5 104 105 108 166 169 264

Inputs were downloaded from the UniProt REST API on 2026-10-21: `human-Q9NT62-uniprot.txt` (reviewed human ATG3) and `horse-other-ATG3-entries.fasta` (the four other horse ATG3 UniProt entries: A0A3Q2HYB0, F6T6K3, A0A3Q2H2Q9, L7MRX2). Full output is in `alignment.json`.

## Result

Horse A0A3Q2L0A4 (342 residues) aligns to human Q9NT62 (314 residues) with 98.41% identity among 314 paired residues (309 identical). Coverage is 100% of the human sequence and 91.81% of the horse sequence.

The horse model has one 28-residue insertion (VVADITKPCWTDFFLPPLLGVNFPPNNP, horse 223-250) between human residues 222 and 223. In the human structure this point lies between the beta strand at residues 212-220 and the short helix at 229-232 of the catalytic core. Every human residue has a horse partner, and the horse model ends with the canonical human C-terminal 25 residues.

Residue checks (human position -> horse residue): the catalytic Cys-264 (glycyl thioester intermediate) aligns to horse Cys-292; N-terminal curvature-sensing-motif residues Val-4 and Ile-5, LIR-motif residues Asp-104, Gly-105 and Val-108, and the caspase LETD motif residues Leu-166 and Asp-169 are identical at the same positions.

None of the other four horse ATG3 entries contains the 28-residue insertion. L7MRX2, a fragment with transcript-level evidence (PE 2), and F6T6K3 (Ensembl model with a different N-terminus) carry the canonical C-terminus without the insertion. No horse UniProt entry matches the 314-residue human architecture end to end.

## Interpretation and limitations

The benchmark accession is an alternative gene model (RefSeq XP_005602052.1, Ensembl ENSECAT00000058152) of horse ATG3 carrying an extra internal segment. The same 28-residue segment is present in the donkey model A0A9L0IHI0 (see genes/EQUAS/ATG3), so it is probably an equid alternative exon or a shared annotation-pipeline exon call, not a sequencing error. Whether it is expressed as protein, and whether a protein with an insertion in the catalytic core is active, is not measured. All residues known to be required for E2 activity are conserved. Pairwise similarity alone does not establish orthology; the orthology call rests on PANTHER PTHR12866:SF2 membership shared with human, mouse and yeast ATG3.
