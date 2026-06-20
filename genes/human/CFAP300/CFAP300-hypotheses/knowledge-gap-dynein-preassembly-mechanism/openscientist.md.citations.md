# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** CFAP300
- **Gene symbol:** CFAP300

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** knowledge-gap-dynein-preassembly-mechanism
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

CFAP300's unresolved biochemical role in axonemal dynein-arm preassembly is best explained by a dynein-complex scaffold/adaptor or chaperone activity rather than a generic protein-binding annotation.

## Term and Decision Context

- Derived from projects/FUNCTION_KNOWLEDGE_GAPS.md: CFAP300 is required for cytoplasmic preassembly and IFT-dependent delivery of both outer and inner axonemal dynein arms, but its biochemical activity and clients remain unknown.

## Reference Context

- PMID:29727692
- PMID:29727693

## Source Context YAML

```yaml
hypothesis: CFAP300's unresolved biochemical role in axonemal dynein-arm preassembly is best explained
  by a dynein-complex scaffold/adaptor or chaperone activity rather than a generic protein-binding annotation.
focus_type: free_text
context:
- 'Derived from projects/FUNCTION_KNOWLEDGE_GAPS.md: CFAP300 is required for cytoplasmic preassembly and
  IFT-dependent delivery of both outer and inner axonemal dynein arms, but its biochemical activity and
  clients remain unknown.'
reference_id:
- PMID:29727692
- PMID:29727693
```

## Research Objective

Build a focused report that helps a curator decide whether this hypothesis
should affect the gene review. Address the focus type directly:

1. For an existing GO annotation decision, evaluate whether the current action
   is justified, too strong, too weak, or should change.
2. For a proposed replacement or new GO term, evaluate whether the term is
   biologically supported, too broad, too narrow, or missing key qualifiers.
3. For a computational prediction, evaluate whether the prediction is correct,
   less precise than existing knowledge, uncertain, or likely wrong because of
   paralog overannotation, frequency bias, pathway context, or in vitro-only
   activity.
4. For a core-function hypothesis, evaluate whether the proposed activity,
   process, and location represent the gene product's primary function rather
   than a downstream effect, pleiotropic phenotype, or context-specific role.
5. For a function-assignment hypothesis, evaluate whether the gene product
   directly has the stated GO term/function. Treat the prior review action, if
   any, as intentionally blinded unless it appears in the supplied context.

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews and database records as
orientation unless they contain directly relevant synthesized evidence that is
clearly labeled as review-level or database-level support.

Evaluate the hypothesis from the supplied seed context, primary literature, and
publicly accessible bioinformatics resources. Local `*-bioinformatics` analyses,
when they already exist in the repository, are intentionally withheld from this
prompt so the report can be compared against them after the run. Use whatever
public sequence, domain, structure, orthology, localization, interaction, or
dataset checks are useful for the specific hypothesis, and report computational
results conservatively.

## Required Output

### Executive Judgment

Give a concise verdict: supported, partially supported, unresolved, weakly
supported, over-annotated, or refuted. Explain the reasoning and the most
important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (direct assay, mutant phenotype, localization, interaction,
  structural/evolutionary, computational, review/database)
- Supports / refutes / qualifies / competing
- Claim tested
- Key finding
- Organism, tissue, cell type, or assay context
- Confidence and limitations

### GO Curation Implications

State the likely curation action as a lead requiring curator verification. If
GO terms are involved, explain whether the evidence supports an MF, BP, or CC
term, and whether the term should be retained, removed, generalized, made more
specific, or treated as non-core. Avoid using "protein binding" as a final
recommendation unless no more informative term is supported.

### Mechanistic Scope

Describe the immediate molecular or cellular function being tested. Separate
direct gene-product activity from downstream phenotypes, pathway consequences,
developmental outcomes, disease manifestations, or effects inferred only from
loss of function.

### Conflicts and Alternatives

Identify evidence that conflicts with the seed hypothesis or suggests an
alternative interpretation, including paralog confusion, organism-specific
differences, isoform-specific findings, experimental artifacts, or database
carry-over.

### Knowledge Gaps

List explicit uncertainties that matter for curation. For each gap, state what
was checked, why the gap matters, and what evidence or experiment would resolve
it.

### Discriminating Tests

Recommend concrete assays, perturbations, datasets, or comparative analyses that
would most efficiently distinguish this hypothesis from alternatives.

### Curation Leads

Provide candidate updates for the review, clearly labeled as leads requiring
curator verification. Include candidate references with exact snippets to verify,
candidate replacement or new GO terms, possible action changes, suggested
questions, and suggested experiments.

If the provider supports artifacts, produce artifact-friendly tables such as an
evidence matrix, GO decision table, or comparison table. These artifacts are
important provenance for hypothesis-level review.

**Provider:** openscientist
**Generated:** 2026-06-19T16:22:49.311206

1. PMID:29727693
2. PMID:29727692
3. PMID:28514442
4. PMID:35178554
5. PMID:18852297
6. PMID:37712517
7. PMID:30561330
8. PMID:33263282
9. PMID:42067934
10. PMID:30428028
11. PMID:31817850
12. PMID:28176794
13. PMID:38498551
14. PMID:39880089
15. PMID:29113992