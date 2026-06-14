# ESMFold2 Model C domains Analysis

Prediction directory: `cox2_model_c_out`
Model CIF: `cox2_model_c_out/esmfold2_model_0.cif`

## Chains

| Chain | Segment |
|---|---|
| A | MT-CO2_88-227 |
| B | SCO1_112-301 |
| C | SCO2_79-266 |

## Confidence

| Metric | Value |
|---|---:|
| confidence_score | 0.390 |
| ptm | 0.532 |
| iptm | 0.390 |
| complex_plddt | 0.757 |

## Pair-Chain ipTM

| Pair | Value |
|---|---:|
| All pairs | n/a — not returned by hosted ESMFold2 API |

## Attribution Readouts

| Readout | Min CA distance | Min SG-SG distance | Closest atoms |
|---|---:|---:|---|
| SCO1 CxxxC to COX2 CuA | 46.57 A | 50.24 A | B173:SG - A196:SG |
| SCO2 CxxxC to COX2 CuA | 37.16 A | 39.80 A | C133:SG - A196:SG |
| SCO2 CxxxC to SCO1 CxxxC | 20.32 A | 18.79 A | C137:SG - B169:SG |

## Interpretation

This run is below the ipTM > 0.5 threshold, so it should not be used as curation-grade structural evidence. Treat any short motif distances as hypotheses to retest with MSA-backed and multi-seed runs.
