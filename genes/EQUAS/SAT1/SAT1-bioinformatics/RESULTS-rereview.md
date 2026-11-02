# SAT1 (donkey A0A9L0KCT9): paralog comparison for the 2026-10-21 re-review

Script: `compare_paralogs_rereview.py` (PEP 723; `uv run --script compare_paralogs_rereview.py`).
Sequences fetched from UniProt REST. Global Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5.
Raw output: `paralog_output_rereview.txt`.

## Results

- donkey_SAT1 vs human_SAT1 (P21673, 171 aa): 166/171 identical paired residues = 97.1%
- donkey_SAT1 vs human_SAT2 (Q96F10, 170 aa): 77/170 identical paired residues = 45.3%
- Human SAT1 catalytic residues (Glu92 general base, Tyr140 general acid) map to donkey Glu92 and Tyr140.

## Interpretation

The donkey protein is a full-length SAT1 ortholog (same length as human SAT1, no gaps), far closer to
SAT1 than to the SAT2 paralog (thialysine N-epsilon-acetyltransferase, PANTHER SF51). This agrees with its
UniProt PANTHER assignment to PTHR10545:SF36 (DIAMINE ACETYLTRANSFERASE 1), the subfamily of human SAT1.
