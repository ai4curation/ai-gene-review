# sox9a / sox9b / human SOX9 region identity

Script: `region_identity.py` (run from repo root with
`uv run python genes/DANRE/sox9a/sox9a-bioinformatics/region_identity.py`).
Input: cached UniProt flat files for Q9DFH2 (sox9a), Q9DFH1 (sox9b) and P48436
(human SOX9). Global alignment, BLOSUM62, gap open -10 / extend -0.5 (same
settings as `projects/DANRE_DUPLICATION/scripts/compare_pair.py`). Region
boundaries are taken from the first sequence's UniProt HMG-box feature.

Output (2026-09-27):

```
sox9a: length 462, HMG box (107, 175), C-terminal 10 aa QPVYTQLSRP
sox9b: length 407, HMG box (91, 159), C-terminal 10 aa QPVYTQLSRP
SOX9: length 509, HMG box (105, 173), C-terminal 10 aa QPVYTQLTRP
```

| Pair | Whole protein | N-term (before HMG) | HMG box | C-term (after HMG) |
|---|---|---|---|---|
| sox9a vs sox9b | 61.3% (478 cols) | 62.6% (107 cols) | 98.6% (69 cols) | 52.3% (302 cols) |
| sox9a vs SOX9 | 70.2% (521 cols) | 81.3% (107 cols) | 98.6% (69 cols) | 61.2% (345 cols) |
| sox9b vs SOX9 | 56.8% (521 cols) | 61.9% (105 cols) | 98.6% (69 cols) | 47.0% (347 cols) |

## Interpretation

- The HMG-box DNA-binding domain is almost identical in both zebrafish copies
  and in human SOX9 (98.6% identity over 69 columns), so sequence-specific DNA
  binding is expected to be conserved in both copies. This agrees with the
  in vitro binding of both proteins to HMG consensus sites reported by
  Chiang et al. 2001 (PMID:11180959).
- Divergence is concentrated outside the HMG box, mostly C-terminal (the
  region containing the transactivation domains in mammalian SOX9). Sox9b is
  55 aa shorter than Sox9a and is more diverged from human SOX9 than Sox9a is
  (56.8% vs 70.2% overall). Both copies keep the same extreme C-terminus
  (QPVYTQLSRP; human QPVYTQLTRP).
- Region identity alone does not show whether transactivation strength
  differs between the copies. Chiang et al. 2001 identified a potential
  activation domain in the middle of both proteins; no quantitative
  comparison of the two copies' transactivation was found in the cached
  literature.
- Caveat: the region split uses a simple column-assignment rule for gaps; the
  whole-protein value reproduces compare_pair.py (61.3%).
