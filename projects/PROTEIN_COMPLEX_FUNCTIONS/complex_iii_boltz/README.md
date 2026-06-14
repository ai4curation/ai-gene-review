# Complex III CYC1:UQCRFS1 Boltz Pilot

This directory contains a structure-prediction pilot for the Complex III active electron-transfer
interface between cytochrome c1 (`CYC1`) and the Rieske iron-sulfur protein (`UQCRFS1`).

## Hypothesis

`CYC1` and `UQCRFS1` are active contributors to Complex III electron-transfer activity, unlike
structural core subunits such as `UQCRC1` and `UQCRC2`. A useful prediction should place CYC1
heme-binding residues near UQCRFS1 Rieske [2Fe-2S] binding residues with a confident pair-chain
interface.

## Target

- `CYC1` residues 85-281: intermembrane-space cytochrome c1/heme domain.
- `UQCRFS1` residues 141-274: intermembrane-space Rieske head domain.

## Files

- `make_inputs.py`: rebuilds Boltz YAML and FASTA inputs from local UniProt records.
- `inputs/cyc1_uqcrfs1_ims_domains.yaml`: Boltz-style protein input.
- `inputs/cyc1_uqcrfs1_ims_domains_biolm.json`: BioLM hosted Boltz2 payload.
- `analyze_output.py`: summarizes confidence and CYC1 heme-to-UQCRFS1 Rieske motif distances.
- `RESULTS_CYC1_UQCRFS1_BIOLM.md`: hosted BioLM Boltz2 result summary.

## Interpretation Boundary

This is a proof-of-concept attribution test, not standalone GO evidence. Existing Complex III
experimental structures and curated literature remain primary evidence. Prediction output is useful
only if it provides a confident, reproducible interface signal that agrees with known electron
transfer chemistry.
