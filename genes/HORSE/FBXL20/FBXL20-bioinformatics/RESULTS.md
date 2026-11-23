# FBXL20 (horse, A0A9L0TR23): comparison with human FBXL20 (Q96IG2)

Script: `compare_horse_human.py` (run with `uv run --script`, reads the cached UniProt flat files).

## Output (2026-10-21)

```
A0A9L0TR23: length 436; F-box ['22..68']; C-terminal 10 residues QRFCRCCIIL
Q96IG2: length 436; F-box ['22..68']; C-terminal 10 residues QRFCRCCIIL
equal length 436; identical positions 436; identity 100.00%
differences (pos, horse, human): []
```

## Interpretation

- Horse A0A9L0TR23 is a full-length FBXL20 product: 436 residues, the same length as the
  reviewed human canonical isoform Q96IG2-1, and identical to it at every position.
- The F-box (22-68) and the C-terminal CAAX-type prenylation motif region are intact.
- Both proteins are classified in PANTHER subfamily PTHR13318:SF47 (F-BOX_LRR-REPEAT PROTEIN 20)
  by UniProt, as is mouse SCRAPPER/Fbxl20 (Q9CZV8), so functions demonstrated for human and
  mouse FBXL20 can be transferred within the subfamily.
- This is not a fragment, isoform or alternative gene model.
