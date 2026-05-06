# SNIPE GO Issue: Supporting Bioinformatics Note

This note contains detailed architecture-analysis support for the InterPro2GO section of:

- `go-issue-antiviral-nucleic-acid-defense.md`

## Scope

Question addressed:

`IPR025280 + GIY-YIG nuclease + membrane targeting features`

for an architecture-aware mapping strategy.

## Data source

Analysis outputs are in:

- `genes/ECOLX/SNIPE/SNIPE-bioinformatics/results/IPR025280/`
- `genes/ECOLX/SNIPE/SNIPE-bioinformatics/RESULTS.md`

## Key observations

- `IPR025280` proteins are distributed across 17 architectures (n=1612 proteins total).
- Catalytic co-features are dominated by:
  - `PF13455` (73.76%)
  - `IPR018306/PF10544` (17.18%)
  - Combined catalytic coverage: 90.94%
- Membrane-targeting evidence:
  - N-terminal TM-like heuristic signal in 61.41% of proteins
  - Dominant architecture representatives show N-terminal TM/signal features
  - Rare but explicit membrane-associated accessory domains include `IPR039519` and `IPR007829`
  - `IPR018929` can be treated as lower-confidence, optional membrane-linked support

## Suggested architecture-aware combination

```
IPR025280
AND (PF13455 OR IPR018306/PF10544)
AND (
  N-terminal TM/signal-peptide feature
  OR IPR007829
  OR IPR039519
  OR [lower-confidence] IPR018929
)
```

## Intent

This supports a conservative recommendation: avoid mapping `IPR025280` alone to catalytic or membrane GO terms; require architecture-level evidence.
