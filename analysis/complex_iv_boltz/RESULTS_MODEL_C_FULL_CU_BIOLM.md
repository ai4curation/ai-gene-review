# Boltz Model C Analysis (full)

Prediction directory: `analysis/complex_iv_boltz/biolm_boltz2_model_c_full_cu_api_out`
Model CIF: `analysis/complex_iv_boltz/biolm_boltz2_model_c_full_cu_api_out/boltz2_biolm_results_0.cif`

## Chains

| Chain | Segment |
|---|---|
| A | MT-CO2_1-227 |
| B | SCO1_68-301 |
| C | SCO2_42-266 |

## Confidence

| Metric | Value |
|---|---:|
| confidence_score | 0.573 |
| ptm | 0.374 |
| iptm | 0.237 |
| protein_iptm | 0.237 |
| complex_plddt | 0.657 |
| complex_iplddt | 0.585 |
| complex_pde | 2.253 |
| complex_ipde | 11.656 |

## Pair-Chain ipTM

| Pair | Value |
|---|---:|
| MT-CO2:SCO1 | 0.269 |
| MT-CO2:SCO2 | 0.263 |
| SCO1:SCO2 | 0.226 |

## Attribution Readouts

| Readout | Min CA distance | Min SG-SG distance | Closest atoms |
|---|---:|---:|---|
| SCO1 CxxxC to COX2 CuA | 72.15 A | 73.84 A | B169:SG - A196:SG |
| SCO2 CxxxC to COX2 CuA | 71.77 A | 73.44 A | C133:SG - A196:SG |
| SCO2 CxxxC to SCO1 CxxxC | 28.99 A | 25.53 A | C133:SG - B169:SG |

## Interpretation

This run is below the ipTM > 0.5 threshold, so it should not be used as curation-grade structural evidence. Treat any short motif distances as hypotheses to retest with MSA-backed and multi-seed runs.
