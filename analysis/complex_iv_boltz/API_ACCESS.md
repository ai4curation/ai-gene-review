# API Access Notes

This note separates API access for existing structures from API access for new complex-structure
predictions.

## Existing Structures

Use existing structure APIs before running prediction:

- RCSB PDB Data API and file endpoints are the right first stop for experimental structures and
  model coordinates already deposited in PDB.
- AlphaFold DB API is useful for precomputed monomer models by UniProt accession. This is not a
  complex-prediction API.

These are low-risk for curation support because they retrieve citable, versioned records. They do
not solve the problem of predicting a complex that has no public structure.

## New Predictions

### Hosted BioLM Boltz2 API

The retained project workflow uses BioLM's hosted Boltz2 endpoint:

```text
POST https://biolm.ai/api/v3/boltz2/predict/
```

Files:

- `make_biolm_payload.py`: converts a Boltz YAML input into BioLM's `items`/`molecules` payload.
- `run_biolm_boltz2.py`: submits the payload with `Authorization: Token ...` and writes the raw
  response plus returned structure and confidence files.

Example:

```bash
python3 analysis/complex_iv_boltz/make_biolm_payload.py \
  --input analysis/complex_iv_boltz/inputs/cox2_sco1_sco2_model_c_domains_cu_pocket.yaml \
  --output analysis/complex_iv_boltz/inputs/cox2_sco1_sco2_model_c_domains_cu_pocket_biolm.json

BIOLM_API_KEY=... \
  python3 analysis/complex_iv_boltz/run_biolm_boltz2.py \
  --payload analysis/complex_iv_boltz/inputs/cox2_sco1_sco2_model_c_domains_cu_pocket_biolm.json \
  --output-dir analysis/complex_iv_boltz/biolm_boltz2_model_c_domains_cu_api_out
```

### Local Boltz CLI

Upstream Boltz can be run from the command line with `boltz predict`. This remains useful for
reproducibility, privacy, and batch work, but local run outputs are not part of the retained PR
artifact set for this project.

## Practical Recommendation

For this project, use this order:

1. Query RCSB and AlphaFold DB for existing structures.
2. Use a hosted prediction API when we want a quick no-infrastructure complex prediction.
3. Run local Boltz when reproducibility, privacy, or repeated batch work matters more than setup
   cost.
4. Treat hosted prediction APIs as optional convenience tools after checking terms, provenance,
   model version, retention policy, and whether outputs can be archived with confidence metrics.

No predicted-complex output should be used as GO evidence by itself. The API output is only useful
for triage: identifying plausible interfaces, checking whether a proposed active-member assignment
is structurally plausible, and selecting cases for manual review.

## Sources Checked

- Boltz upstream repository: <https://github.com/jwohlwend/boltz>
- BioLM Boltz2 hosted API: <https://biolm.ai/models/boltz2/>
- RCSB PDB Data API: <https://data.rcsb.org/>
- AlphaFold DB API docs: <https://alphafold.ebi.ac.uk/api-docs>
