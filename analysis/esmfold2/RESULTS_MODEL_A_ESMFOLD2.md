# ESMFold2 Model A domains Analysis

Prediction directory: `cox2_sco1_model_a_out`
Model CIF: `cox2_sco1_model_a_out/esmfold2_model_0.cif`

## Chains

| Chain | Segment |
|---|---|
| A | MT-CO2_88-227 |
| B | SCO1_112-301 |

## Confidence

| Metric | Value |
|---|---:|
| confidence_score | 0.583 |
| ptm | 0.710 |
| iptm | 0.583 |
| complex_plddt | 0.790 |

## Pair-Chain ipTM

| Pair | Value |
|---|---:|
| All pairs | n/a — not returned by hosted ESMFold2 API |

## Attribution Readouts

| Readout | Min CA distance | Min SG-SG distance | Closest atoms |
|---|---:|---:|---|
| SCO1 CxxxC to COX2 CuA | 49.02 A | 52.51 A | B173:SG - A196:SG |

## Interpretation

Curation-grade structural support would require reproducible placement with ipTM > 0.5 and low interface PAE. Distances below the 12 A CA threshold are hypothesis-generating only when global/interface confidence is low.

## Takeaway

This is the first run in the pilot to clear the `ipTM > 0.5` bar (ipTM 0.583 vs the
hosted Boltz2 Model A control's 0.158), and ESMFold2 docks the two domains with a
substantial interface (48 residue-residue contacts at 5 A). However, the confident
interface is **not copper-transfer-competent**: the SCO1 CxxxC motif (B169/B173) sits
~49 A (CA) / ~52 A (SG-SG) from the COX2 CuA cysteines (A196/A200), far outside the
12 A transfer heuristic. So a higher-confidence interface does not move the functional
conclusion — neither backend supports a stable, transfer-ready SCO1->COX2 docking, and
this case illustrates that interface confidence and motif geometry must be read together.
Metals are modeled apo (no Cu/heme/Fe-S); a metal-aware follow-up remains the next step.
