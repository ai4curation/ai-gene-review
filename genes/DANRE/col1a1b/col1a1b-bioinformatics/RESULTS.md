# col1a1b C-propeptide cysteine check

Script: `cpropeptide_cys.py` (run from the repository root with `uv run python`).
Input: the cached UniProt records `genes/DANRE/col1a1a/col1a1a-uniprot.txt` (Q6U1J5)
and `genes/DANRE/col1a1b/col1a1b-uniprot.txt` (Q6PEI9). The script takes the
PROSITE "Fibrillar collagen NC1" domain of each protein (the C-propeptide) and
aligns the two domains globally (BLOSUM62, gap open -10, extend -0.5).

Output (2026-09-28):

```
col1a1a length 1447, NC1 starts at 1212; col1a1b length 1449, NC1 starts at 1214
Cys count in NC1: col1a1a 8 col1a1b 7
Cys not conserved: col1a1a C1265 <-> col1a1b S1267
```

Interpretation: all C-propeptide cysteines of alpha1(I) are conserved in
alpha3(I) except one, which is a serine in col1a1b. This agrees with the published
observation that proalpha3(I) lacks one of the four inter-chain cysteines of the
C-propeptide (Cys63 of the proalpha1(I) C-propeptide; PMID:26876635), and with
the Cys/Ser discriminator between alpha1(I) and alpha3(I) chains across fishes
(PMID:34430038). The numbering differs between sources because the C-propeptide
boundary used in the papers is not the PROSITE domain start. This check only
confirms the residue difference in the two zebrafish sequences; it says nothing
about its effect on trimer assembly.
