# Validation And PR Checklist

## Required Checks

Run these for any edited module YAML:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/<module>.yaml
uv run python -m ai_gene_review.validation.module_validator modules/<module>.yaml
just render-module modules/<module>.yaml
git diff --check
```

If project markdown changed, render the touched project page:

```bash
uv run ai-gene-review render-projects projects/<path>.md -o pages/projects
```

If concrete gene reviews were edited or are central to the module claim, run:

```bash
just validate <species> <gene>
```

## Derived QC

Rendered module pages include derived QC from `ai_gene_review.module_qc`:

- recommended-field compliance;
- module deep-research provider detection;
- leaf nodes lacking representative members;
- gene-review completeness for UniProt groundings;
- advisory reaction chaining for `PRECEDES` connections.

Treat leaf-grounding warnings as modeling signals. Add a concrete UniProt
representative only when it truly helps orient an abstract family role; do not
add every organism mentioned in evidence just to improve a count.

## Cache Noise

Validation may update ontology cache files such as `cache/go/terms.csv`. Do not
include these incidental timestamp/cache changes in a module-curation PR unless
the task explicitly requires cache refresh. Remove them from the diff before
staging.

## PR Scope

A clean module-curation PR usually includes:

- the edited `modules/<module>.yaml`;
- rendered `pages/modules/<module>.html`;
- any touched project markdown and rendered page;
- generated deep-research files only if they were produced by an approved
  provider command and are part of the requested work.

The PR body should state:

- what boundary/modeling decision changed;
- where terms were placed and why;
- which exemplars/PTNs/GO-CAMs/gene reviews ground the module;
- validation and render commands run;
- known warnings or follow-up issues.
