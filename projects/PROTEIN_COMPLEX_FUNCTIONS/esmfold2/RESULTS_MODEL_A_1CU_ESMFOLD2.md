# ESMFold2 Model A domains Analysis (single shared Cu, unconstrained)

Prediction directory: `cox2_sco1_model_a_1cu_out`
Model CIF: `cox2_sco1_model_a_1cu_out/esmfold2_model_0.cif`

Bridging-copper probe. The two domains plus a **single** `CU` ligand
(`--ligand U1:CU`), with **no** pocket conditioning, to ask where the model puts
one shared copper: at a bridging interface (sites converge) or committed to one
site (sites stay apart). The intended *forced* bridge (`--pocket`) could not be
run: `PocketConditioning` is feature-gated on `esmfold2-fast-2026-05` for this
key (server returns 401 for any pocket request; plain and ligand-only requests
succeed). This unconstrained run is the honest substitute.

## Chains

| Chain | Segment |
|---|---|
| A | MT-CO2_88-227 |
| B | SCO1_112-301 |

## Confidence

| Metric | Value |
|---|---:|
| confidence_score | 0.606 |
| ptm | 0.724 |
| iptm | 0.606 |
| complex_plddt | 0.770 |

## Pair-Chain ipTM

| Pair | Value |
|---|---:|
| All pairs | n/a — not returned by hosted ESMFold2 API |

## Copper Placement (verified from CIF, unforced)

| Cu | Nearest CYS SG | Distance | Site |
|---|---|---:|---|
| Cu-C | A109 (CuA) | 1.97 A | COX2 CuA |
| Cu-C | A113 (CuA) | 1.98 A | COX2 CuA |
| Cu-C | B62 (SCO1 CxxxC) | 53.5 A | (far — SCO1 left apo) |

The single copper went straight into the COX2 CuA acceptor site, coordinated by
**both** CuA cysteines at ~2.0 A, and sits 53.5 A from the SCO1 CxxxC, which is
left metal-free. The model does **not** place one shared copper at a bridging
SCO1–CuA interface; it commits it to the higher-affinity acceptor site.

## Attribution Readouts

| Readout | Min CA distance | Min SG-SG distance | Closest atoms |
|---|---:|---:|---|
| SCO1 CxxxC to COX2 CuA | 48.27 A | 51.72 A | B173:SG - A196:SG |

## Interpretation

Curation-grade structural support would require reproducible placement with ipTM > 0.5 and low interface PAE. Distances below the 12 A CA threshold are hypothesis-generating only when global/interface confidence is low.

## Takeaway

Across every metal configuration we can run, the conclusion is the same. SCO1
CxxxC stays **~51–52 A** from the COX2 CuA cysteines:

| Run | ipTM | SCO1 CxxxC -> CuA (SG-SG) | Copper |
|---|---:|---:|---|
| apo | 0.583 | 52.5 A | none |
| 3 Cu (holo) | 0.632 | 51.3 A | binuclear CuA + mononuclear SCO1 |
| 1 Cu (shared) | 0.606 | 51.7 A | single Cu -> CuA only; SCO1 apo |

Given a single copper to share, ESMFold2 seats it in CuA and leaves SCO1 empty —
no spontaneous bridging/transfer geometry. The intended *forced* bridge would be
a stronger test, but pocket conditioning is unavailable on this endpoint. What we
can run consistently shows the confident MT-CO2:SCO1 interface is not the
copper-transfer interface, and no metal configuration moves it toward one. The
"missing copper" explanation for the apo off-target docking is refuted.
