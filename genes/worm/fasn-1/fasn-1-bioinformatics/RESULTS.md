# fasn-1 (P91871) catalytic-residue conservation vs human FASN (P49327)

Script: `catalytic_residues.py` (global BLOSUM62 alignment, Biopython PairwiseAligner;
inputs are the cached UniProt flat files `genes/worm/fasn-1/fasn-1-uniprot.txt` and
`genes/human/FASN/FASN-uniprot.txt`). Raw output: `catalytic_residues_output.tsv`.

Run: `uv run python genes/worm/fasn-1/fasn-1-bioinformatics/catalytic_residues.py`

## Result

- Global alignment: 2446 aligned residue pairs, 1103 identical (45.1% of aligned pairs);
  worm FASN-1 is 2613 aa, human FASN 2511 aa.
- Every catalytic residue annotated on human FASN (UniProt ACT_SITE) and the ACP
  phosphopantetheine-attachment serine (MOD_RES) aligns to an identical residue in FASN-1:

| Human FASN residue | Role | FASN-1 residue |
|---|---|---|
| Cys161 | beta-ketoacyl synthase (KS) | Cys197 |
| His293 | KS | His329 |
| His331 | KS | His367 |
| Ser581 | malonyl/acetyl transferase (MAT) | Ser621 |
| His878 | dehydratase (DH) proton acceptor | His926 |
| Asp1031 | DH proton donor | Asp1078 |
| Ser2156 | ACP O-(pantetheine 4'-phosphoryl)serine | Ser2248 |
| Ser2308 | thioesterase (TE) | Ser2415 |
| His2481 | TE | His2591 |

The worm positions Cys197, His926, Asp1078 and Ser2248 match the positions independently
annotated on P91871 by PROSITE ProRules (KS active site, DH proton acceptor/donor, and
pantetheine-phosphoserine), which is a cross-check that the alignment is in register.

## Interpretation

FASN-1 retains the full catalytic toolkit of an animal type I fatty acid synthase:
KS, MAT, DH, ACP and TE catalytic residues are all conserved. The ketoreductase (KR)
and enoylreductase (ER) domains are present by domain signatures (Pfam PF08659 KR,
SMART SM00829 PKS_ER, InterPro IPR020843 ER), but human FASN carries no ACT_SITE
features for KR/ER, so their catalytic residues were not tested here. Nothing in this
analysis suggests loss of any partial activity.
