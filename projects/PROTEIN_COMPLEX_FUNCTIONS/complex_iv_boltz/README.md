# Complex IV COX2 Copper-Maturation BioLM Boltz2 Pilot

This directory contains the retained hosted structure-prediction pilot for the human Complex IV
COX2 copper-maturation module. Local Boltz run outputs were deliberately omitted; the archived
artifacts here are hosted BioLM inputs, returned structures, confidence summaries, and analysis
notes.

## Attribution Question

`SCO1` and `SCO2` are copper-delivery and COX2 CuA maturation factors, not mature Complex IV
catalytic subunits. The structural question is whether a prediction can support a direct
MT-CO2/SCO1/SCO2 copper-transfer assembly, or whether the annotation decision should remain
literature-driven.

## Retained Targets

- Model C full/mature: `MT-CO2` residues 1-227, `SCO1` residues 68-301, `SCO2` residues 42-266,
  with four `CU` ligand pocket constraints.
- Model C domain-only: `MT-CO2` residues 88-227, `SCO1` residues 112-301, `SCO2` residues 79-266,
  with four `CU` ligand pocket constraints.
- Model A pairwise control: `MT-CO2` residues 88-227 and `SCO1` residues 112-301, with `CU`
  ligand pocket constraints.

The domain-only Model C BioLM result is the best retained Complex IV run and is used for the static
project viewer.

## Files

- `make_model_c_inputs.py`: builds the three-chain Model C inputs and pairwise Model A control.
- `make_biolm_payload.py`: converts Boltz YAML inputs into BioLM hosted Boltz2 payloads.
- `run_biolm_boltz2.py`: submits a prepared BioLM payload and writes the returned response,
  structure, and confidence summary.
- `analyze_model_c_output.py`: summarizes confidence, pair-chain ipTM, and CxxxC-to-CuA distance
  readouts.
- `make_viewer.py`: rebuilds the static project viewer in `projects/PROTEIN_COMPLEX_FUNCTIONS/`
  and the rendered GitHub Pages copy in `pages/projects/PROTEIN_COMPLEX_FUNCTIONS/`.
- `API_ACCESS.md`: notes on existing-structure APIs and the BioLM hosted prediction workflow.
- `RESULTS.md`: integrated summary of the retained hosted Complex IV runs.
- `RESULTS_MODEL_C_FULL_CU_BIOLM.md`: hosted BioLM full/mature Model C result.
- `RESULTS_MODEL_C_DOMAINS_CU_BIOLM.md`: hosted BioLM domain-only Model C result.
- `RESULTS_MODEL_A_COX2_SCO1_DOMAINS_CU_BIOLM.md`: hosted BioLM pairwise MT-CO2:SCO1 control.

## Interpretation Boundary

The retained BioLM predictions are useful for hypothesis generation and workflow development, but
they are not standalone GO evidence. The best run has better domain confidence and a moderate
SCO1:SCO2 pair-chain ipTM, but MT-CO2 interfaces remain low-confidence and the cysteine motifs are
not in a confident copper-transfer geometry.
