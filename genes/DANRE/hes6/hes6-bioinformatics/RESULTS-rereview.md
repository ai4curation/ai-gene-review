# hes6 (Q6P0J1) re-review: PTHR10985:SF11 membership and pairwise identity

Analysis date: 2026-10-21. Script: `compare_sf11_rereview.py` (PEP 723; run with
`uv run --script compare_sf11_rereview.py`). Raw output: `compare_sf11_rereview.out`.
Sequences are fetched live from UniProt REST.

## Subfamily placement (PANTHER 19.0 HMM classification files)

PANTHER 19.0 classifies Q6P0J1 (ZFIN:ZDB-GENE-030828-5) in PTHR10985:SF11,
"TRANSCRIPTION COFACTOR HES-6", together with human HES6 (Q96HZ4), mouse Hes6
(Q9JHE6), rat Hes6, Xenopus hes6.1, chicken and cow HES6, and a second zebrafish
gene, her13 (Q568A5, ZDB-GENE-050228-1). Out-group HES/HEY proteins (HES1,
BHLHE40) are in other PTHR10985 subfamilies.

## Pairwise global identity (BLOSUM62, gap -10/-0.5)

| pair | identity | similarity |
|---|---|---|
| Q6P0J1 hes6 vs Q568A5 her13 (zebrafish) | 0.611 | 0.764 |
| Q6P0J1 hes6 vs Q96HZ4 human HES6 | 0.582 | 0.731 |
| Q6P0J1 hes6 vs Q9JHE6 mouse Hes6 | 0.562 | 0.743 |
| Q568A5 her13 vs Q96HZ4 human HES6 | 0.584 | 0.727 |
| Q96HZ4 human vs Q9JHE6 mouse | 0.857 | 0.902 |
| Q6P0J1 hes6 vs Q14469 HES1 (out-group) | 0.364 | 0.560 |
| Q6P0J1 hes6 vs O14503 BHLHE40 (out-group) | 0.358 | 0.542 |

All four SF11 proteins end in the C-terminal WRPW tetrapeptide (the Groucho/TLE
corepressor-recruitment motif of HES proteins). Human HES1 carries WRPW two
residues before its C-terminus (...WRPWRN, checked separately); BHLHE40 lacks it.

## Interpretation

- Q6P0J1 is a full-length (226 aa) product with bHLH, Orange and WRPW, not a
  fragment or alternative model; length matches the 224-aa mammalian HES6.
- The two zebrafish SF11 genes are about equally distant from mammalian HES6
  (0.58 identity each), so pairwise identity alone does not show which of
  them (if either) retains each mammalian HES6 role; a gene-tree would be
  needed. Functions demonstrated for mammalian/Xenopus Hes6 (promotion of
  neurogenesis) therefore cannot be assigned to hes6 rather than her13 from
  these data.
- Identity to out-group HES1/BHLHE40 (~0.36) is much lower, consistent with the
  subfamily split.
