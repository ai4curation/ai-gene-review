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

Design notes:

- Use `parts` for required or optional submodules.
- Use `variant_sets` for alternative implementations along an axis such as
  enzyme chemistry, taxon, cell type, compartment, route, or developmental
  context.
- Use leaf `annotons` for role assertions. The participant can be a concrete
  gene, a complex, a family, a domain, a homolog/ortholog selector, or an
  abstract `ANY_WITH_FUNCTION` / `ANY_WITH_DOMAIN` selector.
- Use `representative_members` on family descriptors when an abstract family or
  evolutionary role needs a concrete UniProt/PTN exemplar without becoming
  species-specific.
- Use `active_units` on complex descriptors when the complex has role-bearing
  components that should be visible to module reasoning.
- Use PANTHER `PTHR` or `PTHR:SF` identifiers for family/subfamily descriptors
  when grounding to the local `interpro/panther/` cache. Use PAINT `PTN`
  identifiers as evidence/provenance for a specific ancestral-node assertion, or
  as the descriptor grounding only when the selector is explicitly “descendants
  of this PAINT node”.
- Use descriptor holders for terms. A descriptor always has `preferred_term`,
  may have an ontology/database `term`, and may carry local nuance in
  `description`, `substrates`, `products`, `targets`, `cargo`, locations, and
  evidence.
- Use `connections` to join nodes or annotons by document-scoped IDs. These can
  be stated at any level, including above variant nodes.
