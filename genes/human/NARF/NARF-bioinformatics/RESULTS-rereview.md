# NARF J3KS48 vs canonical Q9UHQ1: independent re-review mapping (2026-10-21)

Script: `compare_sequences_rereview.py` (PEP 723; `uv run --script compare_sequences_rereview.py`).
It fetches both sequences from the UniProt REST API and Pfam coordinates from the InterPro API
at run time, and writes `results-rereview.json`. It does not read any frozen prediction input.

Global alignment (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5).

J3KS48 is 217 residues; canonical NARF Q9UHQ1 isoform 1 is 456 residues. 216 J3KS48 residues are identical to aligned Q9UHQ1 residues.

| Q9UHQ1 interval | J3KS48 interval | Identical |
|---|---|---|
| 1-128 | 1-128 | 128 |
| 174-258 | 129-213 | 85 |
| 383-385 | 214-216 | 2 |
| 456 | 217 | 1 |

J3KS48 lacks Q9UHQ1 129-173 (an internal 45-residue segment) and essentially all of 259-455. The last four residues (214-217) are a short alternative tail, not a retained block.

Pfam domains of Q9UHQ1 and what J3KS48 retains:

- PF02906 (Iron only hydrogenase large subunit, C-terminal domain), Q9UHQ1 93-381: 121 of 289 residues retained.
- PF02256 (Iron hydrogenase small subunit), Q9UHQ1 393-444: 0 of 52 residues retained.

Cysteines: Q9UHQ1 has 15 Cys (3, 6, 11, 53, 56, 59, 86, 99, 122, 172, 192, 228, 252, 374, 378). J3KS48 retains 12. It loses Cys172 and the C-terminal Cys374/Cys378 pair inside PF02906, and all of PF02256.

Interpretation (limits stated): J3KS48 keeps the N-terminal cysteine-rich region and roughly the first 40% of the hydrogenase-like large-subunit domain. It lacks the C-terminal portion of that domain, including a CxxxC pair, and the whole small-subunit-like domain. A protein this truncated is unlikely to adopt the complete hydrogenase-like fold. This analysis does not show where the NARF nuclear-localization determinants or the prelamin-A-binding surface lie, because neither has been mapped experimentally. Sequence coverage alone does not establish that J3KS48 folds, is stably expressed, localizes, or binds anything.
