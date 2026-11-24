# Pcf11 isoform comparison (re-review, 2026-10-20)

Script: `compare_isoforms_rereview.py` (fetches UniProt JSON live). Output: `compare_isoforms_rereview.out.tsv`.

| Accession | Length | Shared N-terminal prefix with C0P8M6 | Identical to C0P8M6 | UniProt CID (PS51391) |
|---|---|---|---|---|
| C0P8M6 | 86 | 86 | yes | 11-86 |
| E1JH69 | 86 | 86 | yes | 11-86 |
| Q8IGR2 | 573 | 62 | no | 11-146 |
| A1Z9W4 | 1953 | 62 | no | 11-146 |

Conclusion: C0P8M6 (cDNA clone MIP05908p) is identical in sequence to E1JH69, the FlyBase-derived 86-residue "isoform C" entry. It shares only residues 1-62 with the 573-residue and 1953-residue Pcf11 products, after which its last 24 residues (63-86) are unique. In the longer products the CID spans residues 11-146, so C0P8M6 retains residues 11-62 of the CID (about 38% of it) plus an unrelated C-terminal tail. The CID boundary reported for C0P8M6 (11-86) is a profile match that runs into the unique tail; it is not a complete domain. C0P8M6 has none of the regions C-terminal to the CID that the longer products carry.
