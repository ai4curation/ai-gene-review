# ADNP2 bioinformatics

One script, `analyze_adnp2_propagation.py`, which asks whether the NAP-peptide annotation defect
characterised on ADNP (PR #2331) propagated to its paralogue ADNP2, and which supplies the motif
measurements the review cites.

```bash
uv run python analyze_adnp2_propagation.py --self-test   # 6 break-tested guard directions
uv run python analyze_adnp2_propagation.py               # regenerates results.json and RESULTS.md
```

Everything is fetched live from UniProt, QuickGO and PubMed and re-derived at run time; the only
hardcoded values are the merged ADNP review's published PxVxL figures, which are asserted as a
precondition so this panel cannot be interpreted against them unless it reproduces them exactly.
A fresh run reproduces both committed artifacts byte-for-byte.

Read `RESULTS.md` for the findings.
