# MTM-9 catalytic-loop check

Script: `catalytic_motif_check.py` (run with `uv run --with biopython python catalytic_motif_check.py`).
Raw output: `catalytic_motif_check.out`.

Method: the active myotubularin catalytic loop (H-C-x-x-G-x-x-R; HCSDGWDR in MTMR6) was
located by regex in human MTMR6 (Q9Y217, positive reference, active Cys336). Each query
was globally aligned to MTMR6 (BLOSUM62, gap open -10, extend -0.5) and the residue in the
active-Cys column and the following 8-residue loop window were read off.

## Results (verbatim from catalytic_motif_check.out)

- Worm MTM-6 (G5ED68), active control: residue at active-Cys column = C335; loop (H..R window) = HCSDGWDR; matches HCxxGxxR: True
- Human MTMR9 (Q96QG7), inactive control: residue at active-Cys column = G333; loop (H..R window) = HGTEGTDS; matches HCxxGxxR: False
- Worm MTM-9 (Q965W9): residue at active-Cys column = G346; loop (H..R window) = HGGDGLDS; matches HCxxGxxR: False

## Interpretation

MTM-9 has glycine in place of the nucleophilic cysteine (G346) and serine in place of
the catalytic-loop arginine, the same substitution pattern as inactive human MTMR9. The
positive control recovers C335 of worm MTM-6, the residue mutated to serine in the MTM-6
substrate-trapping construct of PMID:14565969. MTM-9 is therefore predicted to be
catalytically inactive, consistent with the UniProt CAUTION note. This is a sequence
prediction; no biochemical assay of MTM-9 has been reported.
