# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** ADAMTSL1
- **Gene symbol:** ADAMTSL1
- **UniProt accession:** Q8N6G6

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-adamtsl1-domain-structure
- **Source file:** genes/human/ADAMTSL1/ADAMTSL1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human ADAMTSL1 (UniProt Q8N6G6), a secreted ADAMTS-like protein lacking the metalloprotease domain, contains structured domains (thrombospondin type-1 repeats, a cysteine-rich/spacer module, Ig-like and PLAC domains) whose closest structural homologs suggest a matrix-binding function. Single analysis only: run Foldseek with the AlphaFold model segments of ADAMTSL1 against PDB, report the domains with confident structural homologs and the functions of those homologs (e.g. fibrillin/LTBP or heparin binding of ADAMTS spacer/TSR modules), and state what molecular function, if any, the structure supports.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Human ADAMTSL1 (UniProt Q8N6G6), a secreted ADAMTS-like protein lacking the metalloprotease
  domain, contains structured domains (thrombospondin type-1 repeats, a cysteine-rich/spacer module, Ig-like
  and PLAC domains) whose closest structural homologs suggest a matrix-binding function. Single analysis
  only: run Foldseek with the AlphaFold model segments of ADAMTSL1 against PDB, report the domains with
  confident structural homologs and the functions of those homologs (e.g. fibrillin/LTBP or heparin binding
  of ADAMTS spacer/TSR modules), and state what molecular function, if any, the structure supports.'
focus_type: free_text
context: []
reference_id: []
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
**Generated:** 2026-11-23T11:41:24.899936

1. PMID:11805097
2. PMID:28514442
3. PMID:31439947
4. PMID:33544829
5. PMID:38284126
6. PMID:19671700
7. PMID:17395588
8. PMID:33961781
9. PMID:22242013
10. PMID:19940141
11. PMID:32141660
12. PMID:36924352
13. PMID:39190555
14. PMID:35115729
15. PMID:39880678
16. PMID:37081215
17. PMID:32196558
18. PMID:28209710
19. PMID:34946607
20. PMID:34517169
21. PMID:42173289
22. PMID:25957949
23. PMID:31463913
24. PMID:38324186
25. PMID:32855533
26. PMID:34790768
27. PMID:41534528
28. PMID:39769211
29. PMID:37061115
30. PMID:34499774
31. PMID:40401006
32. PMID:40869199
33. PMID:42413983
34. PMID:42175658
35. PMID:36339449