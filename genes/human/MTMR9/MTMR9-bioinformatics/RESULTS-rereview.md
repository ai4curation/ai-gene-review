# MTMR9 catalytic-motif check (re-review, 2026-10-20)

Script: `catalytic_motif_rereview.py` (fetches UniProt sequences; raw output in `catalytic_motif_rereview.out`).

| Protein | Length | Loop start | CX5R loop | Cys | Arg |
|---|---|---|---|---|---|
| MTMR9 (Q96QG7) | 549 | 332 | HGTEGTDST | absent | absent |
| mouse Mtmr9 (Q9Z2D0) | 545 | 332 | HGTEGTDST | absent | absent |
| MTMR6 (Q9Y217) | 621 | 335 | HCSDGWDRT | present | present |
| MTMR7 (Q9Y216) | 660 | 337 | HCSDGWDRT | present | present |
| MTMR8 (Q96EF0) | 704 | 337 | HCSDGWDRT | present | present |

Conclusion: MTMR9 lacks both the catalytic cysteine and the catalytic arginine of the
myotubularin HCX5R phosphatase loop (G333 and S339 replace C and R), and the substitution is
conserved in the mouse ortholog in the same PANTHER subfamily (PTHR10807:SF56). Its three
dimerization partners retain the intact active-site loop. This agrees with the PAINT IRD
(NOT) for GO:0004438/GO:0106018 at node PTN000086907.

Q96QG7 is the canonical 549-aa reviewed product; isoform 2 (Q96QG7-2) lacks residues 1-85
(most of the PH-GRAM domain, 4-99) but keeps the phosphatase-like domain and coiled coil.
