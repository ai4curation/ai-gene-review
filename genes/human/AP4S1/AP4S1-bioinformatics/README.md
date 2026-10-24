# AP4S1 bioinformatics

One analysis, supporting the AP4S1 gene review.

- `basic_patch.py` — is the large-subunit half of the dileucine-signal basic patch present
  in AP-4 epsilon (AP4E1)? Fetches eight human AP-subunit sequences live from UniProt,
  asserts every expected length, transfers the three published large-subunit anchor
  residues (gamma1 R15, alphaC R21, delta R26 from PMID:21097499) onto epsilon by pairwise
  alignment, and refuses to report the answer unless a 6/6 method control passes first.
  Also re-derives the sigma-side anchor (sigma2 R15) onto sigma1A, sigma3A and sigma4.
- `RESULTS.md` — the write-up, including the caveats that bound the conclusion.
- `RESULTS_raw.txt` — verbatim console output of the run that produced `RESULTS.md`.
- `results.json` — machine-readable results.

```bash
uv run python basic_patch.py
```

Exit codes: `0` both tests ran; `2` a fetched sequence was not the expected length, a
published anchor did not hold, or the method control failed (in which case Test 2 is
deliberately not reported).
