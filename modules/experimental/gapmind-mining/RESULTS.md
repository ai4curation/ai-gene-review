# GapMind → module mining: feasibility spike

**Verdict: mining microbial amino-acid biosynthesis pathways into `modules/` is
highly feasible.** GapMind's `.steps` pathway definitions map almost 1:1 onto the
`ModuleReview` schema, and ModelSEED grounds 91% of the enzyme steps to
ModelSEED/KEGG/MetaCyc reaction ids — automatically, with no identifier guessing.

This directory is a **spike**, not a production importer. It exists to answer the
question *"can we mine ModelSEED / GapMind / IMG for microbial pathways?"* before
committing to a full build.

## What was done

1. **Cached the data** (`fetch_data.sh`, `cache/`):
   - all 18 GapMind amino-acid `.steps` pathway definitions (PaperBLAST, Price/Arkin, LBL) — committed (~160 KB)
   - the ModelSEED `reactions.tsv` biochemistry table (CC-BY) — gitignored (~37 MB)
2. **Wrote a prototype converter** (`gapmind_to_module.py`) that parses a `.steps`
   file and emits a `status: DRAFT` `ModuleReview` YAML, grounding EC numbers
   against ModelSEED.
3. **Generated two proof-of-concept drafts** and validated both against the schema:
   - `his-from-gapmind.yaml` — histidine, a clean **linear** 11-step pathway
   - `ile-from-gapmind.yaml` — isoleucine, which exercises **branching** (three
     alternative routes to 2-oxobutanoate) and **cross-file imports** (`val.steps`)

```
$ linkml-validate -s .../gene_review.yaml -C ModuleReview his-from-gapmind.yaml  →  No issues found
$ linkml-validate -s .../gene_review.yaml -C ModuleReview ile-from-gapmind.yaml  →  No issues found
```

## Source assessment — can we mine?

| Source | Verdict | Why |
|---|---|---|
| **GapMind** | ✅ Primary mine | Open, on GitHub, microbial. `.steps` = named steps grounded to EC/Pfam/TIGRFam + curated proteins, plus AND/OR rules. LBL-authored. |
| **ModelSEED** | ✅ Grounding layer | CC-BY, on GitHub. `reactions.tsv` gives EC→reaction with KEGG/MetaCyc/BiGG xrefs and substrates/products. 91% EC coverage here. |
| **IMG** | ❌ Not mineable | IMG Terms/Pathways are behind JGI auth and effectively frozen. KEGG modules are the practical conceptual replacement, but KEGG bulk access is license-restricted — use by hand, not in bulk. |

## Schema mapping (the key result)

| GapMind construct | → module schema |
|---|---|
| step (`hisG  ATP phosphoribosyltransferase  EC:2.4.2.17`) | `ModuleAnnoton` in a `REACTION` `ModuleNode` |
| EC-bearing step | `ANY_WITH_FUNCTION` selector; EC carried as `EvidenceItem` |
| HMM-only step (`hmm:TIGR00735` + `curated:` exemplars) | `FAMILY` selector, `term` = `NCBIfam:`/`Pfam:` id, `representative_members` from exemplars |
| `all: prs hisG hisI …` | ordered `parts` (the pathway backbone) |
| OR-rule (same name, multiple lines — e.g. `oxobutanoate:` ×3) | `ModuleVariantSet`, `selection: EXACTLY_ONE`, `axis: route` |
| single-definition rule | nested `METABOLIC_PATHWAY` node with ordered `parts` |
| `import val.steps:ilvI …` | step definitions resolved from the sibling file, provenance-tagged |
| EC number | grounded to `ModelSEED:rxnNNNNN` + `KEGG:` + `MetaCyc:` via `reactions.tsv` |

## Yield across the full GapMind aa set

```
pathways = 18
steps    = 204   (EC-grounded = 123, HMM-only = 27, rest = name/exemplar only)
OR-rules → variant_sets = 18
distinct ECs = 129, of which 118 (91%) ground to a ModelSEED reaction
```

## What the importer deliberately does NOT do (honesty notes)

- **It never guesses GO molecular-function term ids.** EC/Pfam/KEGG/MetaCyc ids are
  carried verbatim as provenance; the GO MF assignment is left for human/deep-research
  review (per repo policy "never guess identifiers"). The output is a `DRAFT` stub.
- GapMind `ignore:`/`ignore_other:` (negative exemplars) and `term:` (name synonyms)
  tokens are dropped from the structured output.
- Substrate/product *descriptors* are not auto-filled; ModelSEED's human-readable
  reaction definition is attached as evidence instead of inventing structured chemistry.

## Reproduce

```bash
cd modules/experimental/gapmind-mining
./fetch_data.sh                                   # re-fetch caches (ModelSEED is gitignored)
uv run python -m doctest gapmind_to_module.py -v  # parser doctests
uv run python gapmind_to_module.py cache/gapmind/aa/his.steps --name Histidine  -o his-from-gapmind.yaml
uv run python gapmind_to_module.py cache/gapmind/aa/ile.steps --name Isoleucine -o ile-from-gapmind.yaml
uv run linkml-validate -s ../../../src/ai_gene_review/schema/gene_review.yaml -C ModuleReview his-from-gapmind.yaml
```

## Recommended next steps (if we proceed past the spike)

1. Promote the converter into `src/ai_gene_review/` with pytest coverage and a `just`
   recipe (`module-ingest-gapmind`); fix the README's references to non-existent
   `module-deep-research-*` recipes while there.
2. Add a curation pass: assign GO MF terms (OLS MCP), write biological `description`
   prose, and run module deep-research — turning a `DRAFT` into a real `modules/*.yaml`.
3. Batch-convert the 18 aa pathways, then extend to GapMind's `carbon` catabolism set.
4. Treat ModelSEED `compound_ids`/`stoichiometry` as a source for structured
   `substrates`/`products` descriptors (ChEBI-grounded) in a second grounding pass.
