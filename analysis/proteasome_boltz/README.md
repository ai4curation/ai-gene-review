# Proteasome PSMB5:PSMA1 Boltz Pilot

This directory contains a non-OXPHOS structure-prediction pilot for protein-complex function
attribution in the human 20S proteasome core.

## Hypothesis

`PSMB5` is a catalytic beta subunit with the threonine nucleophile for chymotrypsin-like protease
activity. `PSMA1` is an alpha-ring structural subunit. A predicted interface between the two should
support proteasome architecture, not export protease molecular function to `PSMA1`.

## Target

- `PSMB5` residues 60-263: mature beta5 catalytic chain; UniProt active-site nucleophile Thr60.
- `PSMA1` residues 1-263: alpha-ring structural subunit.

## Files

- `make_inputs.py`: rebuilds Boltz YAML and FASTA inputs from local UniProt records.
- `inputs/psmb5_psma1_attribution_domains.yaml`: Boltz-style protein input.
- `inputs/psmb5_psma1_attribution_domains_biolm.json`: BioLM hosted Boltz2 payload.
- `analyze_output.py`: summarizes confidence, contacts, and active-site proximity readouts.
- `RESULTS_PSMB5_PSMA1_BIOLM.md`: hosted BioLM Boltz2 result summary.

## Interpretation Boundary

This pilot tests a key annotation principle: structural interface evidence is not the same as
molecular-function execution. Even a high-confidence PSMB5:PSMA1 interface would not justify
annotating `PSMA1` to threonine-type endopeptidase activity.
