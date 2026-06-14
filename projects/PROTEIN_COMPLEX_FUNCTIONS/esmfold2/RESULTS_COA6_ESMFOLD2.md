# ESMFold2 Model C + COA6 (4-chain) Analysis

Prediction directory: `coa6_out`

Chain D = COA6 (55-98, Cx9C domain) is present in the prediction but has no motif
defined in the analyzer, so the readouts below cover only A/B/C (COX2/SCO1/SCO2).
Model CIF: `coa6_out/esmfold2_model_0.cif`

## Chains

| Chain | Segment |
|---|---|
| A | MT-CO2_88-227 |
| B | SCO1_112-301 |
| C | SCO2_79-266 |

## Confidence

| Metric | Value |
|---|---:|
| confidence_score | 0.377 |
| ptm | 0.518 |
| iptm | 0.377 |
| complex_plddt | 0.747 |

## Pair-Chain ipTM

| Pair | Value |
|---|---:|
| All pairs | n/a — not returned by hosted ESMFold2 API |

## Attribution Readouts

| Readout | Min CA distance | Min SG-SG distance | Closest atoms |
|---|---:|---:|---|
| SCO1 CxxxC to COX2 CuA | 47.63 A | 50.95 A | B173:SG - A196:SG |
| SCO2 CxxxC to COX2 CuA | 31.59 A | 29.17 A | C137:SG - A200:SG |
| SCO2 CxxxC to SCO1 CxxxC | 71.38 A | 71.91 A | C137:SG - B173:SG |

## Interpretation

This run is below the ipTM > 0.5 threshold, so it should not be used as curation-grade structural evidence. Treat any short motif distances as hypotheses to retest with MSA-backed and multi-seed runs.

## Takeaway

Adding the COA6 Cx9C domain (4 chains) leaves COX2 disengaged (SCO1 CxxxC -> CuA
51.0 A) and rearranges the chaperones: the SCO1 and SCO2 sites are now 71.9 A
apart, versus 18.8 A in the 3-chain Model C. The model finds no stable,
reproducible assembly — the inter-chaperone geometry swings wildly between runs
(18.8 -> 33 -> 72 A across domain / full / COA6), confirming low-confidence
docking. SCO2 came closest to CuA of any run (29.2 A) but still far outside the
12 A transfer heuristic.
