# Expression-grounded pathway satisfiability: human gluconeogenesis

**Result: the textbook set of gluconeogenic tissues — and the metabolic gate that
defines it — is *derived*, not looked up, purely from pathway logic + tissue
expression.**

This is a first, self-contained demonstration of *context-resolved pathway
satisfiability* in a eukaryote. In microbes (GapMind) the question is "does the
**genome** encode each step?". In a metazoan every cell has the whole genome, so
the discriminating variable is **expression**: "is each isozyme **expressed** in
this tissue?". This prototype evaluates the human gluconeogenesis module against
GTEx v8 tissue expression and resolves which route is active where.

## What it does

1. **`module_logic.py`** compiles a `ModuleReview` YAML into a monotone boolean
   circuit — `parts`/`annotons` → AND, `variant_sets` → OR — then enumerates the
   *routes* (one choice per variant set) and the *AND-core* (atoms required by
   every route = gate candidates). Pure logic, no data dependency, doctested.
2. **`gtex_oracle.py`** fetches GTEx v8 median TPM per tissue for each isozyme
   (resolving symbol → versioned GENCODE id; alias-aware, e.g. `G6PC1`→`G6PC` for
   GENCODE v26) and caches a gene × tissue matrix (`cache/gtex_medians.tsv`).
3. **`resolve_context.py`** marks each atom expressed/absent per tissue
   (median TPM ≥ threshold), evaluates the circuit, and reports satisfiable
   tissues + the missing gate atom for the rest.

## The result (threshold: median TPM ≥ 1)

```
Routes through the module: 4
Gate (atoms required by every route): ['PC', 'G6PC1', 'SLC37A4']

SATISFIABLE in exactly: Liver, Kidney_Cortex, Small_Intestine_Terminal_Ileum
  (each realises 2 routes: PCK1 or PCK2 × FBP1; never the muscle isozyme FBP2)

NON-gluconeogenic tissues (Muscle, Brain, Heart, Blood, Adipose, Lung, …):
  all fail at the SAME gate atom -> G6PC1

Validation vs textbook gluconeogenic tissues:
  recovered = expected = {Liver, Kidney_Cortex, Small_Intestine}   (no false +, no misses)
```

So the engine independently recovers that **gluconeogenesis is liver / kidney-cortex
/ intestine**, that the **terminal G6PC1·SLC37A4 ER system is the gate** (which is
*why* muscle and brain cannot release free glucose), and that the realised route
uses **FBP1, not the muscle FBP2** isozyme.

### It resists the paralog trap

`G6PC3` ("G6Pase-β") is expressed in essentially every tissue (10–40 TPM). A naive
"is *some* glucose-6-phosphatase paralog expressed?" rule would wrongly call most
tissues gluconeogenic. Because the module grounds the gluconeogenic terminal step
specifically to **G6PC1** (with `G6PC2`/`G6PC3` recorded as a *paralog trap* in the
module notes), the engine correctly excludes them. This is the eukaryotic form of
the "permissibility ≠ presence" / paralog-overannotation caution.

### The gate is graded (and that matches physiology)

| threshold (median TPM) | satisfiable tissues |
|---|---|
| ≥ 1  | Liver, Kidney_Cortex, Small_Intestine |
| ≥ 5  | Liver, Kidney_Cortex |
| ≥ 10 | Liver |

G6PC1 is 169 TPM in liver, 5.6 in kidney cortex, 2.8 in intestine — so the order in
which tissues drop out as the bar rises recapitulates their known quantitative
contribution to gluconeogenesis (liver dominant, kidney secondary, intestine minor).

## Honest scope / epistemics

- **Expression is used asymmetrically:** absence excludes a route (no enzyme → no
  flux, the strong signal); presence only *permits* (it does not prove flux — protein
  level, allostery, and hormonal state still gate real activity). The satisfiable set
  is therefore an *upper bound* on capacity, not an assertion of active flux.
- **The reversible glycolytic trunk** is treated as constitutively satisfiable
  (broadly expressed housekeeping enzymes), so it is never the gate; the
  tissue-restricting logic lives entirely in the bypass reactions, as in biology.
- Bulk-tissue GTEx mixes cell types; the natural next step is single-cell / spatial
  data to derive **periportal zonation** of hepatic gluconeogenesis on the same engine.

## Why this is novel and useful

- KEGG/Reactome pathway-completeness is genome-level — every human cell "has"
  gluconeogenesis. This instead resolves **which route is wired up in which context**
  as a logic problem, and flags the **gate** that explains tissue restriction.
- The gate/abduction framing generalises: where a pathway is *independently known*
  active in a context but a required atom is unexpressed, that is a flagged gap — a
  missed isozyme, a non-canonical route, or a regulation-only explanation.

## Reproduce

```bash
cd modules/experimental/gluconeogenesis-context
uv run python -m doctest module_logic.py -v          # logic doctests
uv run python gtex_oracle.py                          # refresh cache from GTEx v8
uv run python module_logic.py ../../gluconeogenesis_human.yaml   # routes + gate
uv run python resolve_context.py                      # per-tissue resolution + validation
uv run python resolve_context.py --threshold 5        # graded gate
```

## Next steps

1. Single-cell / spatial oracle → derive hepatic gluconeogenesis **zonation**
   (full route satisfiable only in periportal hepatocytes).
2. Add the substrate-entry OR-branches (lactate / alanine / glycerol) as their own
   variant set so the engine also resolves *which precursor* a tissue can use.
3. Promote `module_logic.py` into `src/ai_gene_review/` with pytest coverage; it is
   the reusable core for satisfiability over any module (microbial or eukaryotic).
4. Wire the "known-active + unexpressed required atom = gap" abduction path and emit
   gaps as reviewable predictions.
