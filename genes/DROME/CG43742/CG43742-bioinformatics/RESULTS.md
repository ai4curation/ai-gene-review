# CG43742 (A0A0B4KFF2) subfamily placement and catalytic residues

Script: `subfamily_tree.py` (run with `uv run python subfamily_tree.py`); raw output in
`subfamily_tree_output.txt`, alignment in `sf147_plus_outgroups.aln.fasta`, tree in `sf147_nj.nwk`.

## PANTHER placement

The PANTHER 19.0 fruit-fly HMM classification assigns A0A0B4KFF2 to PTHR24260:SF147 (EG:BACR7A4.3 PROTEIN-RELATED), a subfamily of 27 D. melanogaster proteins that also contains snk (P05049) and CG10764/SP77 (A1ZAT2). The UniProt record's PANTHER cross-reference and the GOA IBA rows instead use PTHR24256 (TRYPTASE-RELATED) and its PAINT node PTN000667087. The PAINT seeds of that node (psh, MP1, spirit, SPE, grass, sphinx1/2, modSP, scaf) all fall in other PTHR24260 subfamilies (SF134-SF145) in PANTHER 19.0, not in SF147.

## Tree

A neighbour-joining tree (identity distance over a MAFFT alignment of the 27 SF147 proteins plus psh, modSP and SPE as outgroups) places CG43742 on a branch of long (480-525 aa) tandem-domain proteins: HDC06631 (A1ZA51), CG4827 (C0PDF1), CG10764 (A1ZAT2), CG42694 (A0A0B4JD89) and CG30187 (A0A0B4K875). snk falls alone on a separate deep branch near the root of the tree. CG43742 is about 30-40% identical to every SF147 member over aligned columns, so no one-to-one ortholog relationship to a characterized protein is implied. CG10764 (SP77) is the only experimentally studied protein on the tandem-domain branch and is, like SP251, classified in PMID:30367934 as a PD plus PLD protein.

## Catalytic residues

S1 domain 1 (residues 35-258) carries H73 in a TAAHC motif, D121 and S207 in a DSGGP motif: the His-Asp-Ser triad is complete. S1 domain 2 (residues 282-472) has no TAAHC-type histidine motif and no GDSGG-type serine motif, so it is a protease-like domain that cannot be catalytic.

Limitations: the NJ tree uses full-length identity distances without bootstrap support and is only a coarse placement check. No substrate preference or activity is inferred.
