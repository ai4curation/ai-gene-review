# crt10 (O42996) orthology check against budding-yeast Crt10 (Q08226)

Script: `reciprocal_phmmer.sh` (HMMER phmmer; UniProt reference proteomes UP000002311
S. cerevisiae, 6067 sequences, and UP000002485 S. pombe, 5130 sequences). Raw output:
`reciprocal_phmmer_output.txt`. Run 2026-10-21.

## Question

PANTHER gives no family for budding-yeast Crt10 (Q08226, 957 aa), while it places
O42996 (482 aa) in PTHR19876:SF20 (COATOMER family; subfamily named PRE-MRNA-SPLICING
FACTOR PRP46-LIKE). PANTHER therefore cannot ground the PomBase Crt10 orthology call, and
there is no PAINT/IBA node shared by the two proteins. This analysis tests whether the
orthology is at least reciprocal at the sequence level.

## Results

- Pfam (InterPro API): Q08226 carries two strong PF08728 (CRT10) matches (126-390,
  E=2.8e-41; 396-948, E=2.4e-63). O42996 carries one weak PF08728 match (311-400,
  E=7.3e-4) and one PF00400 WD40 repeat (186-221). Each of the two yeast proteomes has
  exactly one UniProt protein with PF08728: Q08226 in S. cerevisiae and O42996 in S. pombe.
- Full-length O42996 against the S. cerevisiae proteome: the top hits are generic WD40
  proteins (NLE1, TUP1, COPA, GBLP, PWP2); Q08226 CRT10_YEAST ranks 20 of 29 hits (E=1.5e-4).
- The non-WD40 C-terminal region of O42996 (residues 260-482) against the S. cerevisiae
  proteome: the only hit is Q08226 CRT10_YEAST (E=4.6e-4).
- Q08226 against the S. pombe proteome: the only hit is O42996 (E=2.1e-4).
- The best local alignment pairs O42996 342-400 with Q08226 796-851, inside the
  C-terminal CRT10 domain of budding-yeast Crt10.

## Interpretation

O42996 and Q08226 are reciprocal sole matches through the Crt10-specific region, which
is consistent with the PomBase one-to-one ortholog assignment. The similarity is weak
and confined to about 60 residues, and O42996 is roughly half the length of budding-yeast
Crt10, so the relationship supports transfer of the conserved pathway role
(nonfunctional rRNA decay) only at the level PomBase asserted; it does not establish
that fission-yeast Crt10 binds the same cullin-RING ligase partners.
