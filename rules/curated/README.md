# Curated annotation rules

Rules written and owned by this project. Each `CR-nnnn.yaml` is a `CuratedRule`
(`src/ai_gene_review/schema/gene_review.yaml`). A rule couples the sequence-feature
logic of an annotation with the taxon or context logic that limits it, in one
auditable record, and names the external source it replaces.

| Rule | Assigns | Conditions | Replaces | Status |
|---|---|---|---|---|
| [CR-0001](CR-0001.yaml) | GO:0007034 vacuolar transport | IPR005024 AND Eukaryota | interpro2go IPR005024 | PROPOSED |
| [CR-0002](CR-0002.yaml) | GO:0061639 Cdv-dependent cytokinesis | IPR053654 OR IPR053492 | (new coverage) | PROPOSED |
| [CR-0003](CR-0003.yaml) | GO:0006511 ubiquitin-dependent protein catabolic process | IPR000426 AND ubiquitin relay module not absent | interpro2go IPR000426 | DRAFT |
| [CR-0004](CR-0004.yaml) | EC 1.2.1.75 name, RHEA:26446 | FunFam 3.40.50.720:FF:000411 AND MCR-type CDD AND Archaea | ARBA00067001, ARBA00052213 | PROPOSED |

## Semantics

- A rule fires when **any** condition set holds; a set holds when **all** its
  conditions hold. `negated: true` inverts a condition.
- Every set needs at least one non-negated sequence-feature condition (InterPro,
  Pfam, PANTHER, FunFam, CDD, NCBIfam). Taxon and module conditions only restrict.
- `MODULE_CONTEXT` conditions name a module in `modules/` and are
  **exclusion-only**: the condition fails only when the module is evaluated as
  unsatisfiable in the protein's organism or context, and holds when it is
  satisfiable or not evaluated. A missing component may be a detection gap, so
  absence of evidence never blocks an annotation. They cannot be negated.

## When to use which condition

Use the condition that actually separates right from wrong members:

- **Taxon** when a whole lineage lacks the prerequisite and the taxon is an exact
  proxy for it (CR-0001: only eukaryotes have a vacuole).
- **Module context** when the prerequisite is a set of components that a taxon
  only approximates (CR-0003: a ubiquitin conjugation system, which some archaea
  may have).
- **Sequence features** (CDD models, sites, subfamilies) when the problem is
  paralogy or a subfamily with a different function; a taxon cannot help when
  both paralogs sit in the same genome (CR-0004).

If a term is wrong for every member of an entry, no rule is needed: record the
removal in `projects/INTERPRO/interpro2go.sssom.yaml` or the ARBA rule review.

## Relation to other records

- `projects/INTERPRO/interpro2go.sssom.yaml` records what is wrong with a
  mapping; a row that cannot be fixed inside interpro2go names its replacement
  rule ("REPLACE WITH RULE CR-nnnn").
- `rules/arba/<ID>/<ID>-review.yaml` records what is wrong with a UniProt rule;
  the curated rule lists it under `replaces`.
- Modules provide the context layer. Rules whose components are detected by
  other rules must not depend, through a module, on themselves.

## Commands

```bash
just validate-curated-rules           # schema + semantic checks
just count-curated-rules              # UniProtKB match counts (network)
```

`count-curated-rules` turns each rule into a UniProt query (module conditions
cannot be queried and are left out, so the count is an upper bound). Record
the result in the rule's `validation_runs`.
