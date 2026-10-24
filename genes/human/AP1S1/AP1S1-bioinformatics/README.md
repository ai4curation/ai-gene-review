# AP1S1 bioinformatics

One analysis: does human AP1S1 (sigma1A) retain the dileucine-signal binding site, and is
residue conservation at that site sufficient evidence that a sigma subunit binds these
signals?

```bash
uv run python dileucine_site.py
```

Fetches nine AP-complex sigma subunits live from UniProt (no cached or hardcoded
sequences), asserts each expected length so a re-released canonical sequence aborts the
run rather than silently shifting positions, and maps the structurally defined sigma2
dileucine pocket onto each by pairwise alignment. Writes `results.json` and exits non-zero
if the literature-named residues or the literature-stated homologies fail to reproduce.

Findings are written up in `RESULTS.md`. The short version: the site is retained in
sigma1A and every named residue checks out, but the verified non-binder sigma4 retains the
same residues, so conservation alone does not establish the activity.
