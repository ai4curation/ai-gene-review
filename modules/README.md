# Module KB

Module documents describe reusable biological modules: pathways, organelle
lifecycles, complexes, molecular-function programs, developmental programs, or
other recursively decomposable biological sketches.

Validate a module document with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/gluconeogenesis.yaml
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

The module index (`pages/modules/index.html`) surfaces the headline figures
(reviewed-gene count, leaf-grounding gaps, module deep-research presence) as
sortable columns.

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
