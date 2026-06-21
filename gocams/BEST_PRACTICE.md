# Reading & reviewing GO-CAM activities

The full rubric for reading and reviewing GO-CAM activities (annotons) lives in
the **`gocam-curation` skill**, which uses progressive disclosure so the detail
is only pulled into context when needed:

- Entry point: `.claude/skills/gocam-curation/SKILL.md`
- Detailed rules: `.claude/skills/gocam-curation/references/`
  - `molecular-function.md` — MF specificity, binding≠function, adaptor/sequestering/catalytic
  - `has-input.md` — `has input` semantics per activity type
  - `causal-relations.md` — direct/indirect causal, directionality, mechanism vs phenotype
  - `complexes.md` — complex subunit representation
  - `qc-and-consistency.md` — verdict scale, QC-flag glossary, consistency categories, checklist

The skill's controlled vocabularies map onto the schema enums
(`GoCamClaimVerdictEnum`, `GoCamQcFlagEnum`, `GoCamConsistencyEnum`) so a
`GoCamReview` (`gocams/<id>/<id>-review.yaml`) is machine-checkable.

## Quick checklist

- [ ] MF is the most specific correct term (not generic, not bare binding).
- [ ] `has input` names the substrate/target-gene/effector/cargo — not a ligand or raw DNA.
- [ ] Causal edges are direct/indirect as the mechanism warrants, pointing subject→object.
- [ ] `occurs_in` and `part_of` present where known.
- [ ] Every activity/edge has an ECO code + reference; claims have verbatim support.
- [ ] Complex activities attributed to the right subunit(s).
- [ ] `verdict`, any `qc_flags`, and `consistency` recorded for every activity.

Adapted from the GO Consortium GO-CAM guidelines and the
[`geneontology/gocam-agent`](https://github.com/geneontology/gocam-agent)
`gocam-best-practice` / `validate-claims` skills.
