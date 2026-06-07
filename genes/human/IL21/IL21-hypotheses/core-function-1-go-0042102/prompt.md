# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** IL21
- **Gene symbol:** IL21

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-1-go-0042102
- **Source file:** genes/human/IL21/IL21-ai-review.yaml
- **Source selector:** existing_annotations[GO:0042102] (currently action: UNDECIDED; see issue #1418)

## Seed Hypothesis

Positive regulation of T cell proliferation (GO:0042102) is currently annotated
to IL21 with direct experimental evidence (IDA: PMID:17673207, PMID:15207081),
but its status as a **core** function is contested and has been set to UNDECIDED
pending review. IL21 is a secreted cytokine whose signature, well-established
functions are in the B-cell / T-follicular-helper axis (germinal center B cell
differentiation, Tfh differentiation, immunoglobulin production, B cell
proliferation). IL21 is a comparatively weak, context-dependent T-cell mitogen
and can be anti-proliferative in some settings.

Evaluate whether positive regulation of T cell proliferation represents a CORE
function of IL21 (one of the primary processes the cytokine evolved to drive)
versus a downstream, secondary, or context-dependent consequence of
IL21R/IL2RG -> JAK1/JAK3 -> STAT3 signaling that is better captured as non-core.
Crucially, distinguish a "real, documented effect" (not in question) from a
"core function". A secondary related question: should NK cell mediated
cytotoxicity (GO:0045954, currently IBA/IEA only) be treated the same way?

## Term and Decision Context

- Biological process under review: positive regulation of T cell proliferation (GO:0042102)
- Current action: UNDECIDED (was ACCEPT); two IDA annotations (PMID:17673207, PMID:15207081)
- Core molecular function (not in question): cytokine activity (GO:0005125), via IL21R/IL2RG -> JAK1/JAK3-STAT3
- Likely-core ("signature") IL21 processes: germinal center B cell differentiation (GO:0002314), T follicular helper cell differentiation (GO:0061470), positive regulation of immunoglobulin production (GO:0002639), positive regulation of B cell proliferation (GO:0030890)
- Related, also uncertain: positive regulation of natural killer cell mediated cytotoxicity (GO:0045954) (IBA/IEA only)
- Location: extracellular region (GO:0005576)
- Decision needed: core vs KEEP_AS_NON_CORE vs remove; and, for a dedicated cytokine, whether such downstream immune processes belong as core via `directly_involved_in` or should be modeled with a regulatory / acts-upstream relation while "core" is reserved for signature processes.

## Reference Context

- PMID:17673207
- PMID:15207081
- file:human/IL21/IL21-uniprot.txt

## Source Context YAML

```yaml
gene_symbol: IL21
id: Q9HBE4
existing_annotations:
  - term: {id: GO:0042102, label: positive regulation of T cell proliferation}
    evidence_type: IDA
    original_reference_id: PMID:17673207
    review:
      action: UNDECIDED
      reason: >-
        Real but borderline core vs non-core; IL21 is a weak, context-dependent
        T-cell mitogen relative to its B-cell/Tfh signature. Deferred to expert
        review (issue #1418).
  - term: {id: GO:0042102, label: positive regulation of T cell proliferation}
    evidence_type: IDA
    original_reference_id: PMID:15207081
    review: {action: UNDECIDED}
core_functions:
  - molecular_function: {id: GO:0005125, label: cytokine activity}
    directly_involved_in:
      - {id: GO:0002314, label: germinal center B cell differentiation}
      - {id: GO:0002639, label: positive regulation of immunoglobulin production}
      - {id: GO:0061470, label: T follicular helper cell differentiation}
      - {id: GO:0030890, label: positive regulation of B cell proliferation}
      # GO:0042102 (T cell proliferation) removed pending this hypothesis review
      - {id: GO:0045954, label: positive regulation of natural killer cell mediated cytotoxicity}
    locations:
      - {id: GO:0005576, label: extracellular region}
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

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews and database records as
orientation unless they contain directly relevant synthesized evidence that is
clearly labeled as review-level or database-level support.

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
