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

### Function compliance

Both an annoton's explicit `function` and its participant's `required_function`
are checked. Checks descend into complex `active_units` and use each unit's own
assertions; a complex's overall activity is not assigned to all of its subunits.

For concrete UniProt participants and family `representative_members`, the
checker joins to `genes/**/*-ai-review.yaml`. A matching
`core_functions[].molecular_function` establishes core coverage. Retained
annotations and curated replacement terms can support the activity while
revealing missing core coverage. An intentional `KEEP_AS_NON_CORE` is valid and
does not request promotion to core functions. Missing gene reviews, missing
support or core coverage, and functions without GO identifiers produce
**warnings**, not evidence that the activity is absent. A retained, applicable
`NOT` annotation contradicting the asserted activity produces an **error**.
Rejected evidence rows, contribution-only functions, and unresolved isoform or
annotation-extension context are reported for review without being treated as
unconditional biological negations.

Term comparisons use exact GO identifiers and **`is_a` relationships only**:
a reviewed specific activity supports its broader ancestors, while a broad
annotation cannot establish a more specific activity. Negation applies in the
opposite direction: exclusion of a broad activity excludes its descendants.
`part_of` and regulatory relationships do not establish molecular-function
support. If the ontology cannot be loaded, comparisons fall back to exact IDs.

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
