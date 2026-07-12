# Module Modeling

## Choose The Right Level

- `ModuleReview` describes a recursively decomposable biological module:
  pathway, complex, organelle lifecycle, developmental program, molecular
  function program, reaction chain, or abstract motif.
- `ModuleNode` owns the module or submodule identity: `concepts`, `context`,
  `parts`, `variant_sets`, `connections`, and `gocam_associations`.
- `ModuleAnnoton` owns leaf role assertions: participant, molecular function,
  processes, locations, and role description.

For a `BIOLOGICAL_PROCESS` module, place molecular function terms under the leaf
annoton that performs the activity. Do not put an enzyme/adapter/binding MF in
`module.concepts` just because the module has one protein member. Use
module-level MF concepts only when the node itself is intentionally a
`MOLECULAR_FUNCTION` module or motif.

## Concepts And Context

- Use `module.concepts` for ontology/database terms that describe the module
  node as a whole.
- Use `module.context` for shared taxon, cell type, compartment, condition, or
  developmental scope.
- Use leaf `annotons[].locations` when the location applies to a specific
  activity rather than the whole module.
- Avoid redundant parent/child context (`cytoplasm` plus `cytosol`,
  `membrane` plus `plasma membrane`) unless both are needed for a reason recorded
  in `description` or `notes`.

## Parts, Variants, And Connections

- Use `parts` for required steps, roles, subcomplexes, or submodules.
- Use `variant_sets` for alternative implementations along an explicit axis such
  as taxon, compartment, enzyme family, substrate route, developmental context,
  or cell type.
- Use `connections` for relationships between document-scoped ids. For reaction
  chains, add `chaining_status` and `chaining_note` when the advisory CoA
  continuity check needs curator adjudication.
- Avoid a one-part wrapper unless the parent carries meaningful context or is an
  intentional concrete instantiation of a reusable template. If one protein has
  multiple mechanistic roles, model multiple parts or multiple leaf annotons.

## Participants

- Use `selector_type: GENE` or `GENE_PRODUCT` for a concrete species member.
- Use `FAMILY`, `DOMAIN`, `HOMOLOG_OF`, `ORTHOLOG_OF`, `ANY_WITH_FUNCTION`, or
  `ANY_WITH_DOMAIN` for reusable roles.
- Use `active_units` inside complex descriptors when a complex has role-bearing
  subunits that must remain visible to reasoning.
- Keep activation enzymes, cofactor biosynthesis, transport, regulation, and
  upstream/downstream biology outside the module core unless they are required
  parts of the pathway definition.

## Representative Members And PTNs

- Use `representative_members` on family descriptors for concrete UniProt
  exemplars that orient the reader and satisfy leaf grounding QC.
- Representative members are examples, not an exhaustive species list and not a
  claim that the module is limited to those proteins.
- Use `ancestral_nodes` for the stronger PAINT claim that a function arose at or
  was present in a PANTHER ancestral node and is inherited by descendants unless
  diverged.
- Ground ancestral nodes with exact `PANTHER:PTN...` ids from local canonical
  IBD data under `interpro/panther/<PTHR>/<PTHR>-paint.tsv` or from GOA
  WITH/FROM evidence with `GO_REF:0000033`. Never guess PTN ids.

## Common Anti-Patterns

- Module-level MF term on a process module when the MF belongs to a step.
- Broad process term as module core when a specific process/reaction term exists.
- Parent and child locations both asserted without explanation.
- Species-specific wording in a reusable module label or description.
- Inflating representative members to every species mentioned in evidence.
- Treating generated deep-research prose as a source of identifiers without
  checking UniProt, GOA, PANTHER, Rhea, ChEBI, GO-CAM, or publications.
