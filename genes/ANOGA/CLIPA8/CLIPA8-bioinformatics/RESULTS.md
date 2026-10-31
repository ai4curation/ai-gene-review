# CLIPA8 (A0A1S4H5S2) catalytic-triad check

Script: `catalytic_triad_check.py` (reads `../CLIPA8-uniprot.txt`; standard library only;
run with `python3 catalytic_triad_check.py`).

## Output (2026-10-21)

```
length 363
His57 region (TAAH[CI]): [(160, 'TAAHI')]
Asp102 region (ND[IV]AL): [(211, 'NDIAL')]
Ser195 canonical (GDSGGP): no match
Ser195 region, permissive (C.GD.G, canonical C.GDSGGP): [(307, 'CDGDGG')]
  residue at catalytic-Ser position 311: G
```

## Interpretation

- The chymotrypsin-numbering His57 (His163 in CLIPA8, motif TAAHI) and Asp102 (Asp212,
  motif NDIAL) motifs are retained.
- The canonical Ser195 motif GDSGGP is absent. The corresponding segment is CDGDGGSG
  (residues 307-314), in which the residue at the catalytic-serine position (311) is Gly.
  This agrees with the curated UniProt caution that the catalytic Ser is replaced by Gly.
- With no nucleophilic serine, CLIPA8 cannot perform serine-protease catalysis. It is a
  clip-domain serine protease homolog (cSPH, CLIPA subfamily), not a protease.

This is a motif scan, not an alignment; it checks only the three triad positions.
