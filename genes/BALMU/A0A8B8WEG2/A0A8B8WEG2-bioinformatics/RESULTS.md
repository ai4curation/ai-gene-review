# A0A8B8WEG2 (blue whale CDK16, 421 aa): isoform comparison

Script: `compare_isoforms.py` (standard library; fetches sequences from UniProt REST).
Raw output: `compare_isoforms_output.txt`.

## Result

All four blue whale UniProt entries for CDK16 come from one gene (NCBI GeneID 118888515,
chromosome X) and differ only at their N termini (RefSeq XP_036695535-XP_036695538).

- A0A8B8WEG2 (421 aa, XP_036695538.1) aligns to human CDK16 isoform 1 (Q00536, 496 aa) from human residue 76 to the C terminus, with 419 of 421 residues identical. It begins at the internal methionine equivalent to human Met76, so it lacks human residues 1-75.
- A0A8B8WEF1 (496 aa, XP_036695536.1) is colinear with human isoform 1 over its full length (487/496 identical). This is the whale product equivalent to the human canonical isoform.
- A0A8C0DX89 (502 aa) carries a 6-residue N-terminal extension (MQSEVA...), equivalent to human isoform 3.
- A0A8B8WEA8 (482 aa) has an internal 14-residue difference around human residues 106-120.

Residues mapped onto A0A8B8WEG2:

| human CDK16 residue | role (literature) | A0A8B8WEG2 |
|---|---|---|
| Ser12 | BRSK2 phosphosite | absent |
| Ser95 | CDK5 phosphosite | S20 |
| 112-121 | conserved segment required for CCNY binding | present (from E37) |
| Ser119 | needed for CCNY binding | S44 |
| Ser153 | PKA site; phosphorylation blocks CCNY binding | S78 |
| Gly158 | needed for CCNY binding | G83 |
| Lys194 | catalytic lysine | K119 |
| Asp286 | catalytic proton acceptor | D211 |
| 461-473 | C-terminal segment needed for CCNY binding | present (from S386) |

## Interpretation

A0A8B8WEG2 is an N-terminally shorter alternative-start isoform, not a fragment. It keeps the
complete kinase domain, the catalytic residues and all the cyclin Y binding determinants mapped by
Mikolcevic et al. 2012, who reported that the first 105 residues of CDK16 are not needed for CCNY
binding. Its only loss among the mapped sites is the N-terminal Ser12 BRSK2 phosphosite.
