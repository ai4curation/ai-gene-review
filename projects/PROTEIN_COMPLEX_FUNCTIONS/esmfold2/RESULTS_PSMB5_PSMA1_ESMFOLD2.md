# ESMFold2 Proteasome PSMB5:PSMA1 Attribution Analysis

Prediction directory: `psmb5_psma1_out`
Model CIF: `psmb5_psma1_out/esmfold2_model_0.cif`

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
| confidence_score | 0.362 |
| ptm | 0.616 |
| iptm | 0.362 |
| complex_plddt | 0.825 |

## Attribution Readouts

| Readout | Value | Notes |
|---|---:|---|
| PSMB5:PSMA1 pair-chain ipTM | n/a | structural-interface confidence |
| PSMB5:PSMA1 5 A residue contacts | 27 | co-complex/interface signal, not activity export |
| PSMB5 active-site T60 to nearest PSMA1 atom | 30.00 A | PSMB5 T60:CA - PSMA1 99:CA |

## Interpretation

The interface confidence is below the provisional pair-chain ipTM > 0.5 threshold, so this particular prediction should be treated as hypothesis-generating only. The annotation conclusion is still clear from UniProt features and proteasome biology: PSMB5 carries the protease active site; PSMA1 is structural.
