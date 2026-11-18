# PR 6122 round 5 annotation-reviewer consultation

Baseline: `f348f66391120fda4f8520fd648db8f2e36a06f0`. Reviewed the latest CHANGES_REQUESTED review submitted 2026-11-07T00:03:01Z, using the repository annotation-reviewer and PR-review guidance. This follow-up changes access metadata and prose only.

## Resolved findings

- **7:** Removed the stale `full_text_unavailable: true` entry for PMID:32631860 from PSEPK/PP_0312, PSEPK/PP_0313, CHRI1/etfA and CHRI1/etfB. The immutable publication cache declares full text available and contains the Results, Discussion and Methods used by these reviews. Their existing access notes already report reading that full text.
- **8:** Corrected the PSEPK/dgcA FMN-binding reason. DgcA retains MARK_AS_OVER_ANNOTATED because its cofactor inference is based on an ortholog; DdhC retains REMOVE because its active recombinant protein was directly characterized. The old claim that the two reviews had the same verdict was false.
- **c:** Removed schema syntax and core-encoding commentary from all twelve folate-coupled sarcosine oxidase proposed-term justifications. Their reaction definitions, supporting evidence, assembled-complex rationale and species-specific evidence limits are unchanged.
- **e:** Reworded the DdhC reason to describe the missing FMN-linking cysteine as a *possible explanation*, preserving the authors' uncertainty. The review suggestion underdescribed the source: the cached Discussion explicitly says that this cysteine is absent and that this may explain the missing FMN. The measured noncovalent FAD and lack of detected covalent flavin remain the analytical evidence; the cysteine argument is a hypothesis, not a proven causal mechanism.

## Preserved boundaries and remaining work

All original annotation payloads/order, actions, historical NEW rows, core functions, supporting quotations and protected raw/provider/publication sources are unchanged. No new biological annotation or proposed term was added.

Nonblocking **a** (PSEPK SoxA NAD+ binding), **b** (ontology treatment of an unreleased imine intermediate), and **f** (ARTGO Dmg FAD annotation and RHEA mapping label) remain unchanged. The consultation does not manufacture annotation rows to satisfy optional suggestions. Shared-tracker wording **d** belongs to the root agent and was not edited here. Final full validation, commit, publication and renewed external review belong to the root agent.

Exact changed-file manifest, frozen hashes, focused validation results and preservation checks are recorded in `round5-consultation.json`, with terminal logs under `.cache/module-audit-logs/dimethylglycine-20261107/round5/`. This consultation did not run full-repository validation or commit/push changes.
