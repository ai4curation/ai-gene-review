# Complex IV COX2 Copper-Maturation Hosted BioLM Boltz2 Results

Date: 2026-05-20

## Target

The retained Complex IV pilot tests whether structure prediction supports a direct
MT-CO2/SCO1/SCO2 copper-transfer assembly. Three hosted BioLM Boltz2 runs were archived:

| Run | Chains | Purpose |
|---|---|---|
| Full/mature Model C | MT-CO2 1-227; SCO1 68-301; SCO2 42-266 | Test the complete mature-domain hypothesis with copper pocket constraints |
| Domain-only Model C | MT-CO2 88-227; SCO1 112-301; SCO2 79-266 | Reduce low-confidence transmembrane and targeting regions; retained as the best viewer model |
| Pairwise Model A | MT-CO2 88-227; SCO1 112-301 | Test the expected terminal donor pair without SCO2 |

All three payloads requested `recycling_steps=3`, `sampling_steps=200`, and
`diffusion_samples=5`.

## Confidence Summary

| Run | confidence_score | ipTM | Key pair-chain ipTM | Motif-distance readout |
|---|---:|---:|---|---|
| Full/mature Model C | 0.573 | 0.237 | MT-CO2:SCO1 0.269; MT-CO2:SCO2 0.263; SCO1:SCO2 0.226 | SCO1/SCO2 CxxxC motifs remain about 72 A from COX2 CuA cysteines |
| Domain-only Model C | 0.642 | 0.389 | SCO1:SCO2 0.540; MT-CO2:SCO1 0.165; MT-CO2:SCO2 0.196 | SCO1/SCO2 interface is plausible, but neither SCO motif is in transfer range of COX2 CuA |
| Pairwise Model A | 0.582 | 0.158 | MT-CO2:SCO1 0.151 | Closest SCO1 CxxxC to COX2 CuA: 13.97 A CA and 13.75 A SG-SG |

Detailed result files:

- `RESULTS_MODEL_C_FULL_CU_BIOLM.md`
- `RESULTS_MODEL_C_DOMAINS_CU_BIOLM.md`
- `RESULTS_MODEL_A_COX2_SCO1_DOMAINS_CU_BIOLM.md`

## Interpretation for GO Curation

The best retained run is the domain-only Model C BioLM result. It has higher confidence than the
other Complex IV predictions and gives a moderate SCO1:SCO2 pair-chain ipTM, but it does not produce
a confident MT-CO2 interface. The pairwise MT-CO2:SCO1 control also fails the interface-confidence
threshold.

These outputs should therefore be treated as hypothesis-generating only. They do not justify
annotating `SCO1` or `SCO2` as mature cytochrome c oxidase catalytic subunits or as direct
executors of cytochrome c oxidase activity. The current review position remains literature-driven:
`SCO1` and `SCO2` are copper-delivery and Complex IV assembly/maturation factors, while mature
Complex IV catalytic activity should be attributed to the relevant active complex members.
