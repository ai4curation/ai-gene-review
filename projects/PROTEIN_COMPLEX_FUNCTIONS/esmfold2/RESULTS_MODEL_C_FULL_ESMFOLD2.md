# ESMFold2 Model C full Analysis (full-length, TM-containing)

Prediction directory: `model_c_full_out`
Model CIF: `model_c_full_out/esmfold2_model_0.cif`

## Chains

| Chain | Segment |
|---|---|
| A | MT-CO2_1-227 |
| B | SCO1_68-301 |
| C | SCO2_42-266 |

## Confidence

| Metric | Value |
|---|---:|
| confidence_score | 0.307 |
| ptm | 0.421 |
| iptm | 0.307 |
| complex_plddt | 0.689 |

## Pair-Chain ipTM

| Pair | Value |
|---|---:|
| All pairs | n/a — not returned by hosted ESMFold2 API |

## Attribution Readouts

| Readout | Min CA distance | Min SG-SG distance | Closest atoms |
|---|---:|---:|---|
| SCO1 CxxxC to COX2 CuA | 46.43 A | 49.79 A | B173:SG - A196:SG |
| SCO2 CxxxC to COX2 CuA | 38.14 A | 39.27 A | C137:SG - A196:SG |
| SCO2 CxxxC to SCO1 CxxxC | 31.80 A | 33.25 A | C133:SG - B173:SG |

## Interpretation

This run is below the ipTM > 0.5 threshold, so it should not be used as curation-grade structural evidence. Treat any short motif distances as hypotheses to retest with MSA-backed and multi-seed runs.

## Takeaway

Adding the membrane-anchor (TM) regions gives the **lowest-confidence run in the
whole series** (ipTM 0.307, vs 0.390 for the domain-only Model C and 0.583 for
the 2-chain Model A), and COX2 stays disengaged (SCO1 CxxxC -> CuA 49.8 A). This
reproduces the Boltz2 full-length result (ipTM 0.237): full-length, lipid-free
membrane-protein prediction degrades the interface. The SCO1:SCO2 sites are 33 A
apart here vs 18.8 A in the domain Model C — the arrangement is not reproducible
across runs, a hallmark of low-confidence docking rather than a real interface.
