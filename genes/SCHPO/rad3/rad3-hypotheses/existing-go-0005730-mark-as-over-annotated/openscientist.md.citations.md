# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812)
- **Gene directory:** rad3
- **Gene symbol:** rad3
- **UniProt accession:** Q02099

## Focus

- **Focus type:** existing_go_annotation_decision
- **Hypothesis slug:** existing-go-0005730-mark-as-over-annotated
- **Source file:** genes/SCHPO/rad3/rad3-ai-review.yaml
- **Source selector:** existing_annotations[36]

## Seed Hypothesis

The existing rad3 GO annotation to nucleolus (GO:0005730) should receive review action MARK_AS_OVER_ANNOTATED. Current rationale: A single localization observation; not a core functional site and not the principal compartment for Rad3 checkpoint activity.

## Term and Decision Context

- Term: nucleolus (GO:0005730)
- Evidence type: IDA
- Original reference: PMID:18180284
- Current review action: MARK_AS_OVER_ANNOTATED
- Review summary: Nucleolar localization is weakly supported and likely a minor or context-specific pool. Rad3's well-established sites of action are chromatin, stalled forks and telomeres, not the nucleolus.
- Review reason: A single localization observation; not a core functional site and not the principal compartment for Rad3 checkpoint activity.

## Reference Context

- PMID:18180284
- PMID:17531813

## Source Context YAML

```yaml
term:
  id: GO:0005730
  label: nucleolus
evidence_type: IDA
original_reference_id: PMID:18180284
qualifier: is_active_in
review:
  summary: Nucleolar localization is weakly supported and likely a minor or context-specific pool. Rad3's
    well-established sites of action are chromatin, stalled forks and telomeres, not the nucleolus.
  action: MARK_AS_OVER_ANNOTATED
  reason: A single localization observation; not a core functional site and not the principal compartment
    for Rad3 checkpoint activity.
  supported_by:
  - reference_id: PMID:17531813
    supporting_text: Cdc18 persists in a chromatin-bound complex including the checkpoint kinases Rad3
      and Rad26.
    reference_section_type: ABSTRACT
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
prompt so the report can be compared against them after the run. Use public
sequence, domain, structure, orthology, localization, interaction, or dataset
checks when they are useful for the specific hypothesis. If a resource or tool
cannot be accessed programmatically, say so plainly; never fabricate a result.
Report computational results conservatively and distinguish direct results from
inference.

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

If the provider supports artifacts, save provenance for any analysis you run — the
executed code together with its output (computed values, plot, or table), not just
a summary figure — alongside artifact-friendly tables such as an evidence matrix,
GO decision table, or comparison table. Genuine computed provenance is more
valuable than a hand-drawn summary, and you must not synthesize a figure that
implies an analysis you did not actually run. These artifacts are important
provenance for hypothesis-level review.

**Provider:** openscientist
**Generated:** 2026-09-01T08:43:58.051686

1. PMID:18180284
2. PMID:16823372
3. PMID:10559981
4. PMID:17531813
5. PMID:21945095
6. PMID:12196391
7. PMID:20140190
8. PMID:8843195
9. PMID:25916852
10. PMID:27391441
11. PMID:18385517
12. PMID:22918952