# AP3S1 bioinformatics

One analysis, two questions:

1. Does human AP3S1 (sigma3A) carry the residues that the dileucine-signal literature
   names for it, and does an independent alignment reproduce the sigma2 -> sigma3A
   correspondences that literature asserts?
2. Is sigma3A distinguishable from its paralog sigma3B (AP3S2) at that site?

```bash
uv run python sigma3_pocket.py
```

Fetches ten AP-complex sigma subunits live from UniProt (no cached or hardcoded
sequences), asserts every expected length so a re-released canonical sequence aborts the
run rather than silently shifting positions, and maps the structurally defined sigma2
dileucine pocket onto each by pairwise alignment. Writes `results.json` and exits non-zero
if the literature-named residues or the literature-stated homologies fail to reproduce.

sigma4 (AP4S1) is included as a verified negative control: same PANTHER family, but its
hemicomplex demonstrably does not bind these signals.

Findings are written up in `RESULTS.md`.
