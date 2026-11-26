# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** BPPGK
- **Taxon:** Kayvirus kay (NCBITaxon:221915)
- **Gene directory:** lysK
- **Gene symbol:** lysK
- **UniProt accession:** Q6Y7T6

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-lysk-assay-discrepancy
- **Source file:** genes/BPPGK/lysK/lysK-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Why the CHAP-only truncation of LysK lyses cells in zymogram, plate-lysis and turbidity assays yet shows no activity in a minimal inhibitory concentration assay, while the CHAP-SH3b fusion works in all of them, may be explained by what those assays differ in rather than by potency alone. That LysK is a 495-residue modular hydrolase with a CHAP domain carrying a Cys54/His117/Glu134 triad and a structural calcium, a central amidase domain, and a C-terminal SH3b wall-binding domain needed for full activity, is already recorded, so do not re-derive the architecture. Single analysis only: state what each of those four assay formats actually requires of an enzyme, naming for each whether the substrate is purified sacculi or renatured protein in gel, whether the cells are growing or stationary, the medium composition and the incubation time, quoting the methods from the primary papers, since the explanation has to be a property the MIC assay demands and the others do not; assess whether the isolated CHAP domain is predicted to be less stable than the fusion, giving any measured melting temperature or aggregation datum and otherwise saying so, and state whether the SH3b domain is known to contribute stability as distinct from binding; state what is known about divalent-cation availability in the MIC medium, since the CHAP domain needs a structural calcium and a loosely bound zinc and a chelating or cation-poor medium would disable it selectively; and state whether growing staphylococci differ from stationary ones in wall teichoic acid or peptidoglycan O-acetylation in ways known to block endolysin access. State which explanation the evidence favours among potency, stability and accessibility, and say plainly if the published methods are not reported in enough detail to separate them.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Why the CHAP-only truncation of LysK lyses cells in zymogram, plate-lysis and turbidity assays
  yet shows no activity in a minimal inhibitory concentration assay, while the CHAP-SH3b fusion works
  in all of them, may be explained by what those assays differ in rather than by potency alone. That LysK
  is a 495-residue modular hydrolase with a CHAP domain carrying a Cys54/His117/Glu134 triad and a structural
  calcium, a central amidase domain, and a C-terminal SH3b wall-binding domain needed for full activity,
  is already recorded, so do not re-derive the architecture. Single analysis only: state what each of
  those four assay formats actually requires of an enzyme, naming for each whether the substrate is purified
  sacculi or renatured protein in gel, whether the cells are growing or stationary, the medium composition
  and the incubation time, quoting the methods from the primary papers, since the explanation has to be
  a property the MIC assay demands and the others do not; assess whether the isolated CHAP domain is predicted
  to be less stable than the fusion, giving any measured melting temperature or aggregation datum and
  otherwise saying so, and state whether the SH3b domain is known to contribute stability as distinct
  from binding; state what is known about divalent-cation availability in the MIC medium, since the CHAP
  domain needs a structural calcium and a loosely bound zinc and a chelating or cation-poor medium would
  disable it selectively; and state whether growing staphylococci differ from stationary ones in wall
  teichoic acid or peptidoglycan O-acetylation in ways known to block endolysin access. State which explanation
  the evidence favours among potency, stability and accessibility, and say plainly if the published methods
  are not reported in enough detail to separate them.'
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
**Generated:** 2026-11-26T11:52:43.650522

1. PMID:19047377
2. PMID:25790497
3. PMID:25064136
4. PMID:19493008
5. PMID:28852930
6. PMID:38203699
7. PMID:35075218
8. PMID:23413880
9. PMID:20144680
10. PMID:22286996
11. PMID:21468207
12. PMID:23431312