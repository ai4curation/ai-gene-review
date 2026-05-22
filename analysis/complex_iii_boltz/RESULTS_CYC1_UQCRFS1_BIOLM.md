# Boltz Complex III CYC1:UQCRFS1 Domain Analysis

Prediction directory: `analysis/complex_iii_boltz/biolm_boltz2_cyc1_uqcrfs1_domains_api_out`
Model CIF: `analysis/complex_iii_boltz/biolm_boltz2_cyc1_uqcrfs1_domains_api_out/boltz2_biolm_results_0.cif`

## Hypothesis

CYC1 and UQCRFS1 should behave as active Complex III electron-transfer subunits if the CYC1 heme-binding region and UQCRFS1 Rieske Fe-S region form a reproducible, confident interface. This contrasts with structural core subunits such as UQCRC1/UQCRC2.

## Chains

| Chain | Segment |
|---|---|
| A | CYC1_85-281 |
| B | UQCRFS1_141-274 |

## Confidence

| Metric | Value |
|---|---:|
| confidence_score | 0.414 |
| ptm | 0.384 |
| iptm | 0.241 |
| protein_iptm | 0.241 |
| complex_plddt | 0.457 |
| complex_iplddt | 0.436 |
| complex_pde | 2.801 |
| complex_ipde | 9.048 |

## Interface Readout

| Readout | Value | Closest atoms |
|---|---:|---|
| CYC1 heme residues to UQCRFS1 Rieske residues, min CA distance | 6.20 A | A125:CA - B219:CA |
| CYC1:UQCRFS1 pair-chain ipTM | 0.241 | n/a |

## Interpretation

This run does not reach the provisional pair-chain ipTM > 0.5 threshold, so it should be treated as hypothesis-generating only.
