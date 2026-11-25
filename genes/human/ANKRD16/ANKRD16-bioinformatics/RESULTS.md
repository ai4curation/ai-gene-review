# ANKRD16 serine-accepting lysine conservation

Script: `lysine_site_check.py` (run with `uv run --with biopython python lysine_site_check.py`).
It aligns mouse ANKRD16 (A2AS55) to human ANKRD16 (Q6P6B7) using global BLOSUM62 alignment,
then maps the three lysines that PMID:29769718 identified as serine acceptors in mouse.

Output:

```
mouse A2AS55 len=361  human Q6P6B7 len=361  identity/mouse_len=0.82
mouse K102 -> human K102
mouse K135 -> human K135
mouse K165 -> human K165
```

All three serine-accepting lysines are conserved at identical positions in human ANKRD16. The two proteins are the same length and 82% identical.
