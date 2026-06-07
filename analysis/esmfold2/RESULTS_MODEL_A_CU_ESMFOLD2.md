# ESMFold2 Model A domains Analysis (metal-aware, +3 Cu)

Prediction directory: `cox2_sco1_model_a_cu_out`
Model CIF: `cox2_sco1_model_a_cu_out/esmfold2_model_0.cif`

Metal-aware companion to `RESULTS_MODEL_A_ESMFOLD2.md` (apo). Same two domains,
plus three `CU` ligands (`--ligand U1:CU U2:CU U3:CU`) with **no** pocket
conditioning — the all-atom model placed the coppers itself (verified below).

## Chains

| Chain | Segment |
|---|---|
| A | MT-CO2_88-227 |
| B | SCO1_112-301 |

## Confidence

| Metric | Value |
|---|---:|
| confidence_score | 0.632 |
| ptm | 0.743 |
| iptm | 0.632 |
| complex_plddt | 0.808 |

## Pair-Chain ipTM

| Pair | Value |
|---|---:|
| All pairs | n/a — not returned by hosted ESMFold2 API |

## Copper Placement (verified from CIF, unforced)

The all-atom model seated all three coppers in their correct cognate sites with
no pocket conditioning, at near-bonding Cu-S distances and the right stoichiometry:

| Cu | Nearest CYS SG | Distance | Site |
|---|---|---:|---|
| Cu-C | A113 (CuA) | 2.33 A | COX2 CuA |
| Cu-E | A113 (CuA) | 2.36 A | COX2 CuA |
| Cu-D | B62 (CxxxC) | 2.35 A | SCO1 metallochaperone |

- **Cu-C–Cu-E = 2.67 A** → a binuclear CuA pair correctly reconstructed in COX2
  (real CuA is a mixed-valence dicopper centre ~2.5 A apart).
- The SCO1 site took a single copper (correct mononuclear CxxxC stoichiometry).
- The two metal sites sit **~53 A apart** (Cu(CuA)–Cu(SCO1)).

So the metal-aware premise holds: this is a genuine holo prediction, not an
apo-with-decorations artifact.

## Attribution Readouts

| Readout | Min CA distance | Min SG-SG distance | Closest atoms |
|---|---:|---:|---|
| SCO1 CxxxC to COX2 CuA | 47.79 A | 51.26 A | B173:SG - A196:SG |

## Interpretation

Curation-grade structural support would require reproducible placement with ipTM > 0.5 and low interface PAE. Distances below the 12 A CA threshold are hypothesis-generating only when global/interface confidence is low.

## Takeaway

Loading copper **raised** interface confidence (ipTM 0.583 apo -> 0.632 holo;
pTM 0.710 -> 0.743; pLDDT 0.790 -> 0.808) yet left the transfer geometry
essentially unchanged: the SCO1 CxxxC motif stays **~51 A** (SG-SG) from the COX2
CuA cysteines, versus ~52 A apo. The coppers seated correctly in both sites
(binuclear CuA + mononuclear SCO1), so the off-target docking is **not** an
artifact of missing metals — ESMFold2 simply, and confidently, predicts a
MT-CO2:SCO1 contact that is not the copper-transfer interface, holo or apo. This
strengthens the apo conclusion: high interface confidence here does not support a
direct, transfer-ready SCO1->COX2 docking.

Caveat: three independent `CU` ligands pre-seat the two sites in their *resting*
holo states, so this run tests whether the resting holo-domains dock adjacently
(they do not), not whether a single bridging-copper transition state can form.
A bridging-copper or covalent-tether setup would be the next, more targeted probe.
