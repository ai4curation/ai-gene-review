# Module KB

Module documents describe reusable biological modules: pathways, organelle
lifecycles, complexes, molecular-function programs, developmental programs, or
other recursively decomposable biological sketches.

Validate all module documents, including schema and biological compliance checks:

```bash
just validate-modules
```

For one module, run both the schema validator and the module validator:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/gluconeogenesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/gluconeogenesis.yaml
```

The module validator label-checks every ontology `term` block and every
`evidence[].source_id` that cites a GO term with a `title`, at any depth, against
the configured ontology. An evidence entry therefore cannot keep citing a retired
id under its pre-obsoletion name after the `term` blocks have been refreshed.
A `term` block whose ontology label carries GO's `obsolete ` prefix is an error
whatever label the module wrote, so neither a reviewed alias in
`conf/oak_config.yaml` (those bridge only a lagging snapshot) nor pasting the
`obsolete ...` label in verbatim can keep a module grounded on a retired term.
An evidence entry may quote a retired label verbatim to document the retirement;
a stale pre-obsoletion title there is still reported as an obsoletion.

Run module-focused deep research with:

```bash
just module-deep-research-perplexity peroxisome-lifecycle
just module-deep-research-openai modules/gluconeogenesis.yaml
```

Render module pages (to `pages/modules/`) with:

```bash
uv run ai-gene-review render-modules --all
uv run ai-gene-review render-modules modules/bbsome.yaml
```

Each rendered module page carries a **Derived QC** panel (computed by
`ai_gene_review.module_qc`) with:

- **Recommended-field compliance** — `linkml-data-qc` analysis of the
  `ModuleReview` document, listing any recommended slots populated below 100%.
- **Module deep research** — whether a `<module>-deep-research-*.md` report
  exists alongside the module YAML, and from which provider(s).
- **Leaf nodes lacking representative members** — terminal nodes (no `parts`,
  no `variant_sets`) whose participants do not ground to a concrete protein
  (a `gene_product`/`gene`/`active_unit` with a `UniProtKB` term, or a `family`
  with `representative_members` / PTN exemplars). These are the abstract leaves
  that still need a concrete UniProt/PTN exemplar.
- **Gene-review completeness** — for every `UniProtKB` grounding in the module,
  joined against `genes/**/*-ai-review.yaml`: whether the gene has a review,
  whether that review is complete (no PENDING/UNDECIDED annotations), and
  whether it has its own deep research.
- **Function consistency and core coverage** — compares each asserted GO
  molecular function with the participant's gene review and, separately,
  applicable family reviews. Lists core support, retained noncore support,
  conflicts, and missing coverage per annoton/participant/function. The module
  validator reports the same warnings and errors; see the details below.
- **Reaction chaining (advisory)** — for every `PRECEDES` connection, each
  reaction's GO molecular-function term is resolved to RHEA (via the GO→RHEA
  mapping in the local OAK databases) and the upstream reaction's CoA-bearing
  products are compared with the downstream reaction's substrates. An
  unacknowledged break (no shared CoA intermediate) is a **warning, never an
  error** — this check is deliberately soft. A curator acknowledges a break (or
  overrides the matcher, which cannot see ChEBI class subsumption such as
  *acetoacetyl-CoA* ⊑ *3-oxoacyl-CoA*) with `chaining_status` +
  `chaining_note` on the connection:

  ```yaml
  connections:
    - source: acad_step
      target: ech_step
      connection_type: PRECEDES
      chaining_status: MAPPING_GAP   # VERIFIED | KNOWLEDGE_GAP | MAPPING_GAP | NOT_APPLICABLE | UNVERIFIED
      chaining_note: >-
        Chemistry is correct; GO:0004300 maps to RHEA:20724 (the (3E) variant)
        rather than the canonical (2E) crotonase RHEA:16105.
  ```

  Any explicit `chaining_status` suppresses the warning; the enum value and note
  record *why*. Leave it unset to let the check report. (Only CoA-carrier
  continuity is checked, so steps connected by non-CoA intermediates are
  reported as "not checked" rather than warned.)

The module index (`pages/modules/index.html`) surfaces the headline figures
(reviewed-gene count, leaf-grounding gaps, module deep-research presence) as
sortable columns.

Translate a module's `connections` graph into a Boolean network (BoolNet `.bnet`;
SBML-qual via biodivine-aeon) and calibrate its signed wiring against external
Boolean models and SIGNOR (see `projects/BOOLEAN_MODELS.md`, `models/boolean/`):

```bash
uv run ai-gene-review module-to-bnet modules/erk_cascade.yaml
```

### Function compliance

Both an annoton's explicit `function` and its participant's `required_function`
are checked. Checks descend into complex `active_units` and use each unit's own
assertions; a complex's overall activity is not assigned to all of its subunits.

For concrete UniProt participants and family `representative_members`, the
checker joins to `genes/**/*-ai-review.yaml`. A matching
`core_functions[].molecular_function` establishes core coverage. Retained
annotations and curated replacement terms can support the activity while
revealing missing core coverage. An intentional `KEEP_AS_NON_CORE` is valid and
does not request promotion to core functions. Missing support or core coverage
and functions without GO identifiers produce **warnings**, not evidence that the
activity is absent. Missing gene/family reviews and participant/family identifiers
are informational coverage notices: they remain in the QC panel and status counts
but do not flood the validator warning log. A retained, applicable
`NOT` annotation contradicting a concrete participant activity produces an **error**.
For a family representative, it produces an advisory warning to review the exemplar
or family scope; it does not negate the whole family.
Rejected evidence rows, contribution-only functions, and unresolved isoform or
annotation-extension context are reported for review without being treated as
unconditional biological negations.

Term comparisons use exact GO identifiers and **`is_a` relationships only**:
a reviewed specific activity supports its broader ancestors, while a broad
annotation cannot establish a more specific activity. Negation applies in the
opposite direction: exclusion of a broad activity excludes its descendants.
`part_of` and regulatory relationships do not establish molecular-function
support. If the ontology cannot be loaded or queried, its failure is cached for the run
and comparisons fall back to exact IDs. Each affected module reports one
`ONTOLOGY_UNAVAILABLE` warning; its coverage warnings explicitly identify the
incomplete subsumption check. Functionless annotons assert nothing to compare
and are skipped on both the gene and family paths.

Family representative checks establish support for the named proteins, not
conservation throughout a family. Separate checks read structured reviews in
`interpro/panther/` and `interpro/pfam/`. PANTHER assessments must cover the
asserted family or subfamily; `SUBFAMILY_ONLY` and `RESIDUE_DETERMINED` restrictions
remain visible instead of being generalized to every member. An explicitly
excluded family/subfamily claim is an error. For Pfam, support requires an
`ACCEPTED` molecular-function annotation with the `enables` relation;
`PROPOSED`, `contributes_to`, rejected mappings, and missing reviews leave gaps
or restrictions. Existing family-ID, membership, and PAINT-node validation
remains separate.

These checks compare structured assertions with current reviews. They do not
prove the meaning of free text, substrate refinements, reaction chemistry, or
biological context. A supported GO term can still accompany a more specific
claim that needs manual review.

Design notes:

- Use `parts` for required or optional submodules.
- Use `variant_sets` for alternative implementations along an axis such as
  enzyme chemistry, taxon, cell type, compartment, route, or developmental
  context.
- Use leaf `annotons` for role assertions. The participant can be a concrete
  gene, a complex, a family, a domain, a homolog/ortholog selector, or an
  abstract `ANY_WITH_FUNCTION` / `ANY_WITH_DOMAIN` selector.
- Use `representative_members` on family descriptors when an abstract family or
  evolutionary role needs a concrete extant exemplar (grounded with a
  `UniProtKB:` id) without becoming species-specific. These are only orienting
  examples, not a claim about where the function evolved.
- Use `ancestral_nodes` on family descriptors to make the stronger, clade-level
  claim that the annoton's function is inferred to have arisen at (or been
  present in) a PANTHER/PAINT ancestral node, and is therefore retained in
  extant descendants barring divergence, neofunctionalization, or loss of key
  residues. Ground each with a `PANTHER:PTN...` id taken from the canonical IBD
  data in `interpro/panther/<PTHR>/<PTHR>-paint.tsv` (columns: `family`, `node`,
  `go_id`, `aspect`, `evidence`, `negated`, `seeds`, `taxon`, `date`) — resolve
  the node by matching a representative member's accession in the `seeds` column,
  and record `GO_REF:0000033` as the IBD evidence. Never guess PTN ids. Note that
  a node's `family` is the PANTHER family it actually belongs to, which may differ
  from the descriptor's primary `PTHR` term (paralogous subfunctions are split
  across families); a family may therefore carry more than one node.
- Use `active_units` on complex descriptors when the complex has role-bearing
  components that should be visible to module reasoning.
- Use PANTHER `PTHR` or `PTHR:SF` identifiers for family/subfamily descriptors
  when grounding to the local `interpro/panther/` cache. PAINT `PTN`
  identifiers name a specific ancestral node; list them under `ancestral_nodes`
  (see above) for the evolutionary-inference claim, use them as
  evidence/provenance for a specific ancestral-node assertion, or use one as the
  descriptor grounding when the selector is explicitly “descendants of this
  PAINT node”.
- Use descriptor holders for terms. A descriptor always has `preferred_term`,
  may have an ontology/database `term`, and may carry local nuance in
  `description`, `substrates`, `products`, `targets`, `cargo`, locations, and
  evidence.
- Use `connections` to join nodes or annotons by document-scoped IDs. These can
  be stated at any level, including above variant nodes.
- Use `gocam_associations` (on a `ModuleNode` or a `ModuleAnnoton`) to ground an
  abstract/non-grounded module element in one or more **production GO-CAM**
  models. Each `GoCamAssociation` carries a required `model` (e.g.
  `gomodel:568b0f9600000284`) and an optional `activity` pinning a specific
  annoton within that model. The referenced models are cached under
  `gocams/<model_id>/<model_id>-src.yaml` (see `gocams/README.md`); the
  `gocams/index.tsv` gene→activity index is the join key. Example:

  ```yaml
  annotons:
    - id: a1
      label: TIR-1 signaling adaptor
      participant:
        selector_type: GENE
        gene:
          preferred_term: tir-1
      gocam_associations:
        - model: gomodel:568b0f9600000284
          activity: gomodel:568b0f9600000284/57ec3a7e00000079
          title: "Antibacterial innate immune response in the intestine via MAPK cascade (C. elegans)"
  ```

### Composing modules by reference (`module_ref`)

An umbrella module (for example an organelle lifecycle) composes existing modules
instead of copying their annotons. A node with `module_ref` stands in for another
module, written like a conformance template: `<stem>` for the whole module, or
`<stem>#<node_id>` for one node in it. The stem names a module file in the same
directory as the referencing module; the engine, the validator and the renderer
all resolve it that way.

```yaml
parts:
  - order: 5
    role: turnover
    node:
      id: mitochondrial_turnover
      label: Mitophagy
      module_ref: mitophagy
  - order: 4
    optional: true          # not every lineage has it; does not gate the umbrella
    node:
      id: respiration
      label: Oxidative phosphorylation
      module_ref: mitochondrial_complex_iv
```

`module_ref` means inclusion, which is different from `conforms_to` (an instance
of a motif):

- **Satisfiability.** `module_logic` compiles the referenced module in place, so
  the umbrella node is satisfied exactly when the referenced module or node is.
  `unsatisfied_steps` reports gaps at the umbrella step; `gap_report` follows
  the reference down to the failing step inside it. Atoms reached through a reference are
  namespaced `<stem>#<annoton_id>`, so a step reached twice is one atom.
  Mark the enclosing part `optional` when a lineage may lack the referenced
  module. Inlining multiplies route counts, so for umbrella modules use
  `is_satisfied`, `unsatisfied_steps` and `core_atoms`, which do not enumerate
  routes; `enumerate_routes` raises past `max_routes`. When two steps reference
  the same module, each copy's variant sets are enumerated independently, so
  routes can mix branches of one referenced variant set and are then not
  guaranteed minimal.
- **Validation (blocking).** The reference must resolve, references must not
  form a cycle, and the referencing node must not carry its own `annotons`,
  `parts` or `variant_sets`; label, description, concepts, context and
  evidence are allowed. Problems inside a referenced module are reported when
  that module itself is validated, not when the umbrella is.
- **Rendering.** The node links to the referenced module page or node anchor,
  it is not counted as an ungrounded leaf, and reference problems appear in the
  page's QC panel.

The Boolean-network translator (`module-to-bnet`) does not follow references yet,
and warns when a document uses them.

### Variant kinds and layered gap reports (`variant_kind`)

A rule makes two kinds of claim. A process step requires a molecular function,
which is close to binary. That function is carried out by one of several
families, domains or complexes, which is open-world. A variant set belongs to
one of the two layers, recorded in the optional `variant_kind`:

- `REALIZER`: the variants are alternative carriers of one required activity
  (families, isozymes, paralogs, lineage-specific proteins).
- `ROUTE`: the variants are alternative ways of achieving the step, with
  different activities (for example SCOT-dependent versus ligase-dependent
  acetoacetate activation in `ketone_body_oxidation`).

```yaml
variant_sets:
  - id: acetoacetate_activation_route
    axis: CoA-transfer chemistry   # free text, unchanged
    variant_kind: ROUTE
    selection: EXACTLY_ONE
```

When `variant_kind` is omitted, `module_logic` infers `REALIZER` if every
variant carries the same single molecular function, and otherwise leaves the
set unclassified. Declare it where the inference cannot tell, chiefly for
routes. `gap_report(circuit, holds)` returns each gap at its innermost failing
element, with its path from the top-level step, its layer and the absent atoms:

| layer | what failed | reading |
|---|---|---|
| `REALIZER` | an atom, or a realizer variant set | the activity is required but no known carrier was found |
| `ROUTE` | a route variant set | none of the modelled routes is present |
| `UNCLASSIFIED` | a variant set with no declared or inferable kind | either reading |

`abduce` attaches only the hypotheses that fit the layers of the gaps, and its
`gap_candidates` list only the atoms that do not hold. Compiled atoms also
carry the participant's family and domain ids (`family_ids`, `domain_ids`),
for oracles that scan a proteome with family models. The design is explained
in `projects/ORGANELLE_LIFECYCLES/two-layer-model.md`.
