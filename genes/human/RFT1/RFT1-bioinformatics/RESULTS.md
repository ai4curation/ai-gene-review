# RFT1 side-chain orientation — resolving a conflict between two structural analyses

## Why

Two OpenScientist runs on the same AlphaFold model (AF-Q96AA3-F1) disagreed about E298:

- `RFT1-hypotheses/scramblase-vs-binding-cavity` classified it **"neither cavity nor portal;
  exposed membrane-interface"**, with side-chain exposure `+0.44` (opening outward) and radial
  distance 13.8 Å.
- `RFT1-hypotheses/family-constraint-cavity-vs-portal` listed it among the **most constrained
  central-cavity-lining** positions (KL 3.31).

Both derived the membrane normal themselves, by different methods, so the disagreement is about
the axis estimate rather than the coordinates. Since one of these calls had already been written
into the gene notes, it needed settling before either was relied on further.

## Method

`axis_orientation.py` — deliberately minimal. No cavity detection, no conservation, no docking.
The one question asked is whether a side chain points toward or away from the membrane-normal
axis, and how stable that answer is when the axis is perturbed.

- Membrane normal = principal eigenvector of `sum(v v^T)` over local helix direction vectors
  (Cα i→i+4 spans of 5–7 Å). The outer product is sign-invariant, so helices running in opposite
  directions through the membrane reinforce rather than cancel.
- Centre = centroid of all Cα. TM slab = `|z| <= 15 Å` along the normal (320 of 541 residues).
- Per residue: `dRad = r(side-chain centroid) − r(Cα)`, negative meaning the side chain turns
  toward the axis.
- Stability: the sign is recomputed under 24 perturbed axes (±10° and ±20° tilts × 12 azimuths).

```
uv run --no-project --with numpy python axis_orientation.py
```

## Result

Median `dRad` across the TM slab is **+0.31 Å** — most side chains point outward, as expected for
a transmembrane bundle. Against that background, every residue tested points inward:

| residue | pLDDT | z (Å) | r_Cα (Å) | dRad (Å) | call | axes agreeing |
|---|---|---|---|---|---|---|
| E64  | 94.4 | +5.3  | 16.2 | −2.57 | inward | 24/24 |
| R67  | 95.2 | +9.4  | 17.2 | −1.54 | inward | 24/24 |
| K152 | 91.6 | +6.4  | 16.4 | −3.37 | inward | 24/24 |
| Q186 | 98.2 | −11.0 | 16.8 | −1.66 | inward | 24/24 |
| N283 | 92.6 | −7.9  | 2.7  | −1.68 | inward | 18/24 |
| R290 | 87.2 | +1.4  | 6.0  | −2.63 | inward | 24/24 |
| E298 | 88.8 | +12.2 | 7.0  | −2.49 | inward | 24/24 |
| Y378 | 97.4 | −5.5  | 14.3 | −2.45 | inward | 24/24 |
| N435 | 93.0 | −5.2  | 14.1 | −2.34 | inward | 24/24 |

**E298 points inward, not outward**, at 7.0 Å from the axis — among the closest of the set, and
stable under every perturbation tried. The `family-constraint` run's classification is
corroborated; the `scramblase-vs-binding-cavity` run's "exposed, outward-facing" call for E298 is
**not reproducible** here and should not be relied on.

A secondary observation, not something either run stated: **R67 is inward-facing but peripheral**
(r_Cα 17.2 Å, against 7.0 Å for E298 and 2.7 Å for N283). That is consistent with R67 being absent
from the `family-constraint` run's top-constrained cavity list despite being an invariant arginine.
Inward-facing and cavity-lining are not the same thing, and the first run's r = 9.1 Å for R67 is
not reproduced either.

## Limitations

- One static AlphaFold model, apparently an occluded state. A different conformation could move
  these side chains.
- The membrane normal is estimated from helix geometry, not from an OPM/PPM membrane fit. The
  perturbation test bounds sensitivity to that choice but does not remove it.
- `dRad` measures orientation only. It does not establish that a residue lines a contiguous solvent
  cavity, and says nothing about substrate contact.
- Absolute radial distances depend on the centre and axis estimates, so they are comparable within
  this table but not directly against either run's numbers.

## Reproducing

The AlphaFold model is not committed; `axis_orientation.py` downloads
`AF-Q96AA3-F1-model_v6.cif` from the AlphaFold DB on first run.
