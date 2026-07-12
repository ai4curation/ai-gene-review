---
name: module-curation
description: Curate, review, or repair ai-gene-review ModuleReview YAML documents under modules/, including pathway/module boundary setting, parts and variant modeling, annoton-level molecular functions, representative UniProt/PTN grounding, module deep-research provenance, validation, rendering, and project batch updates.
---

# Module Curation

Use this skill for `modules/*.yaml` work and for project pages that describe
module/pathway curation. The goal is a reusable, defensible biological module,
not a flat list of annotations or a species-specific note disguised as a module.

## Workflow

1. Read the local context before editing:
   - `modules/README.md`
   - the target `modules/<module>.yaml`
   - any adjacent `<module>-deep-research-*.md`
   - related `projects/**` batch page(s), if the task is pathway-batch work
   - relevant gene reviews and UniProt/GOA files for concrete members
2. Decide the module boundary before filling YAML:
   - What biological process, complex, reaction chain, or reusable motif is the
     module?
   - Which genes/proteins are core members, and which are activation context,
     substrate supply, regulation, upstream/downstream biology, or separate modules?
   - Is this a concrete species/pathway instance or an abstract reusable motif?
3. Model the structure:
   - Put module-level process/complex/context terms on `module.concepts` and
     `module.context`.
   - Put molecular functions on leaf `annotons[].function`, not on a
     biological-process module just because the member protein has that MF.
   - Use `parts` for required steps or roles, `variant_sets` for alternatives,
     and `connections` for ordered/causal links.
4. Ground claims with checkable provenance:
   - Use exact UniProt, GO, Rhea, ChEBI, PANTHER `PTHR`, and PAINT `PTN` ids.
   - Never guess PTNs or identifiers. Resolve PTNs from local PANTHER/PAINT data
     or GOA WITH/FROM evidence.
   - Use representative members to orient family-level claims without turning a
     reusable module into a species-specific member list.
5. Validate and render before committing:
   - `uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/<module>.yaml`
   - `uv run python -m ai_gene_review.validation.module_validator modules/<module>.yaml`
   - `just render-module modules/<module>.yaml`
   - render any touched project page with `uv run ai-gene-review render-projects ...`
   - run `git diff --check`

## Reference Files

Load only the reference needed for the decision at hand:

- `references/modeling.md` — module-vs-annoton placement, parts, variants,
  locations, exemplars, PTNs, and common anti-patterns.
- `references/research-and-grounding.md` — module deep research, species/pathway
  satisfiability checks, gene review integration, and provenance rules.
- `references/validation-and-pr.md` — validation, rendering, derived QC, cache
  noise, and PR checklist.

## Curation Rules

- Prefer a small, explicit decomposition over a one-part wrapper that adds no
  modeling value. If a module has one gene but two separable roles, model two
  parts or annotons.
- Avoid redundant parent/child context such as both cytoplasm and cytosol unless
  the distinction is intentional and explained.
- Do not use broad parent processes as the module core when a specific process
  or reaction step is available. Keep broad terms as prose/context if needed.
- Keep species-specific notes in evidence, notes, project pages, or concrete
  instantiations; reusable modules should stay species-neutral unless the scope
  is deliberately concrete.
- Treat deep research as retrieval support, not authority. Every structural
  claim must still be grounded in identifiers, gene reviews, GOA/UniProt, GO-CAM,
  literature, or explicit curator judgment.
