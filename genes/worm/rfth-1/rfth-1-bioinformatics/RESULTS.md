# rfth-1 (Q23444) pairwise identity to characterized RFT1 orthologs

Script: `pairwise_identity.py` (Biopython global alignment, BLOSUM62, gap open -10, extend -0.5).
Run from the repository root with `uv run python genes/worm/rfth-1/rfth-1-bioinformatics/pairwise_identity.py`.

## Output (2026-10-28)

```
worm RFTH-1 Q23444 length 522
human RFT1 Q96AA3: length 541; identical 156/505 aligned positions = 30.9%; identity over worm length = 29.9%
yeast Rft1 P38206: length 574; identical 121/488 aligned positions = 24.8%; identity over worm length = 23.2%
```

## Interpretation

C. elegans RFTH-1 aligns end to end with human RFT1 at about 31% identity over aligned positions and
with yeast Rft1 at about 25%. Human RFT1 and yeast Rft1 are themselves only weakly similar yet are
functional orthologs (human RFT1 complements yeast rft1 deletion), so this level of identity, together with
the shared Pfam PF04506 / InterPro IPR007594 family membership and similar length, supports RFTH-1 being
the single worm member of the RFT1 family. The analysis does not test function; no C. elegans experimental
data exist for this gene.
