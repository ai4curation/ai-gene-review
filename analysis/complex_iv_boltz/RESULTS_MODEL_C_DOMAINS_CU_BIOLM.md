# Boltz Model C Analysis (domains)

Prediction directory: `analysis/complex_iv_boltz/biolm_boltz2_model_c_domains_cu_api_out`
Model CIF: `analysis/complex_iv_boltz/biolm_boltz2_model_c_domains_cu_api_out/boltz2_biolm_results_0.cif`

## Chains

| Chain | Segment |
|---|---|
| A | MT-CO2_88-227 |
| B | SCO1_112-301 |
| C | SCO2_79-266 |

## Confidence

| Metric | Value |
|---|---:|
| confidence_score | 0.642 |
| ptm | 0.563 |
| iptm | 0.389 |
| protein_iptm | 0.388 |
| complex_plddt | 0.705 |
| complex_iplddt | 0.608 |
| complex_pde | 1.742 |
| complex_ipde | 8.306 |

## Pair-Chain ipTM

| Pair | Value |
|---|---:|
| MT-CO2:SCO1 | 0.165 |
| MT-CO2:SCO2 | 0.196 |
| SCO1:SCO2 | 0.540 |

## Attribution Readouts

| Readout | Min CA distance | Min SG-SG distance | Closest atoms |
|---|---:|---:|---|
| SCO1 CxxxC to COX2 CuA | 38.00 A | 38.12 A | B173:SG - A196:SG |
| SCO2 CxxxC to COX2 CuA | 23.01 A | 23.11 A | C133:SG - A196:SG |
| SCO2 CxxxC to SCO1 CxxxC | 17.13 A | 12.96 A | C137:SG - B173:SG |

## Interpretation

This run is below the ipTM > 0.5 threshold, so it should not be used as curation-grade structural evidence. Treat any short motif distances as hypotheses to retest with MSA-backed and multi-seed runs.
