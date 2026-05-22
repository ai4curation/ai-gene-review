# Boltz Proteasome PSMB5:PSMA1 Attribution Analysis

Prediction directory: `analysis/proteasome_boltz/biolm_boltz2_psmb5_psma1_api_out`
Model CIF: `analysis/proteasome_boltz/biolm_boltz2_psmb5_psma1_api_out/boltz2_biolm_results_0.cif`

## Hypothesis

PSMB5 is a catalytic beta subunit and should retain threonine-type endopeptidase activity attribution. PSMA1 is an alpha-ring structural subunit; even if it forms a confident structural interface with PSMB5, it should not inherit PSMB5 protease activity by complex membership.

## Chains

| Chain | Segment |
|---|---|
| A | PSMB5_60-263 |
| B | PSMA1_1-263 |

## Confidence

| Metric | Value |
|---|---:|
| confidence_score | 0.595 |
| ptm | 0.450 |
| iptm | 0.230 |
| protein_iptm | 0.230 |
| complex_plddt | 0.686 |
| complex_iplddt | 0.633 |
| complex_pde | 2.411 |
| complex_ipde | 12.173 |

## Attribution Readouts

| Readout | Value | Notes |
|---|---:|---|
| PSMB5:PSMA1 pair-chain ipTM | 0.230 | structural-interface confidence |
| PSMB5:PSMA1 5 A residue contacts | 79 | co-complex/interface signal, not activity export |
| PSMB5 active-site T60 to nearest PSMA1 atom | 9.68 A | PSMB5 T60:OG1 - PSMA1 120:OG1 |

## Interpretation

The interface confidence is below the provisional pair-chain ipTM > 0.5 threshold, so this particular prediction should be treated as hypothesis-generating only. The annotation conclusion is still clear from UniProt features and proteasome biology: PSMB5 carries the protease active site; PSMA1 is structural.
