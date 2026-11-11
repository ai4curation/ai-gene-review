# CHAMP1 (chicken A0A8V0YM97) vs human CHAMP1 (Q96JM3)

Script: `compare_human.py` (Biopython global alignment, BLOSUM62, gap open -10 / extend -0.5).
Run from repo root:
`uv run python genes/CHICK/CHAMP1/CHAMP1-bioinformatics/compare_human.py genes/human/CHAMP1/CHAMP1-uniprot.txt genes/CHICK/CHAMP1/CHAMP1-uniprot.txt`

## Results (output of the script)

- Human 812 aa, chicken 948 aa; 462 identical aligned residues (56.9% of human length).
- Per-window identity (human coordinates): 1-100 0.78; 101-200 0.36; 201-300 0.53;
  301-400 0.46; 401-500 0.47; 501-600 0.45; 601-700 0.57; 701-800 0.92; 801-812 0.67.
- WK motif occurrences: human 13 (positions 290-515), chicken 6 (positions 404-485).
- FPE tripeptide occurrences: human 6, chicken 3. SPE occurrences: human 19, chicken 20.
- A canonical C2H2 pattern (C..C.{12}H...H) is found once in each (human 740, chicken 878),
  inside the most conserved C-terminal window.

## Interpretation

- The N-terminal region and the C-terminal zinc-finger region are well conserved
  (78% and 92% window identity), consistent with InterPro CHAMP1_N (IPR063396) and
  Znf-C2H2_CHAMP1_1 (IPR063349) family signatures in the chicken entry.
- The central low-complexity repeat region (WK/SPE/FPE motifs, disordered in MobiDB-lite)
  is diverged in sequence and copy number. The human WK motif that binds MAD2L2/REV7
  (W334/K335/P341, context SGPWKPAKP; PMID:28887307) has no exact counterpart among the
  six chicken WK motifs in this simple motif scan; whether chicken CHAMP1 binds REV7
  through one of its WK motifs is therefore not established by sequence alone.
- This analysis is a simple pairwise comparison; it does not test function.
