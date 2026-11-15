# Carnitine CI fixture relocation

The GitHub validation job for PR #6182 failed because the finite evidence fixture lived under `modules/`, where every YAML is correctly validated as a ModuleReview. The fixture now lives here with exactly the same bytes. No gene, family, module, source publication or prior receipt changed.

Run `uv run python analysis/module_audits/bacterial_l_carnitine_catabolism/round2-fixture-location/check_followup.py` for the current verification. It carries forward the round-one preservation, source-closure, capacity and proposed-activity checks, resolving only the recorded file move. Earlier checkers/generators and manifests are historical snapshots; their old fixture path remains recorded, and they should not be used to regenerate the obsolete location.

The previous full gene-corpus validation remains evidence for the unchanged curated content. The module validation command is rerun after this artifact-layout fix; no new full gene-corpus run is claimed.
