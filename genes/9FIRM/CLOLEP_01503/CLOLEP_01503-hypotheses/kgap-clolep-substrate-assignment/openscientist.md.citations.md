# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** 9FIRM
- **Taxon:** [Clostridium] leptum DSM 753 (NCBITaxon:428125)
- **Gene directory:** CLOLEP_01503
- **Gene symbol:** CLOLEP_01503
- **UniProt accession:** A7VSG2

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-clolep-substrate-assignment
- **Source file:** genes/9FIRM/CLOLEP_01503/CLOLEP_01503-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether the native substrate of CLOLEP_01503 can be assigned from determinants is the prior question to its substrate distribution, and a companion analysis in this project found the answer is no for the partner enzyme of this pathway. That the protein is a PLP-dependent carboxypolyamine decarboxylase best assigned as carboxyaminopropylagmatine decarboxylase from heterologous reconstruction with CLOLEP_01502, that it has a 1.41 Angstrom structure with a PLP Schiff base at Lys43 and a homodimeric assembly, and that structural resemblance and the historical carboxyspermidine and carboxynorspermidine names do not establish native preference, are already recorded, so do not re-derive them. A companion run on the Vibrio cholerae synthase VC_1624 found that the only specificity assignment in that enzyme class is for agmatine, that no structure in the family has a diamine bound, and that the enzymes with measured kinetics are invariant at every pocket position, so no predictive rule could be fitted; treat the decarboxylase side as similarly suspect and say so if it fails the same way. Single analysis only: state which residues the structural literature assigns to substrate selection in any carboxypolyamine decarboxylase whose preference has been measured, naming the structures and quoting the assignments, and report what CLOLEP_01503 has at each; state whether any structure of this enzyme class has a carboxypolyamine substrate or product bound, as opposed to PLP alone, since a cofactor-only structure cannot define a substrate pocket; report whether the genome of this organism encodes the enzymes that would supply each candidate substrate, with locus tags, since substrate availability is what the reconstruction actually tested; and state whether the adjacent CLOLEP_01502 constrains the answer by its own assignment. State which substrate the evidence supports, and say plainly if the determinants are unknown and the question needs a comparative kinetic panel on the isolated enzyme.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether the native substrate of CLOLEP_01503 can be assigned from determinants is the prior
  question to its substrate distribution, and a companion analysis in this project found the answer is
  no for the partner enzyme of this pathway. That the protein is a PLP-dependent carboxypolyamine decarboxylase
  best assigned as carboxyaminopropylagmatine decarboxylase from heterologous reconstruction with CLOLEP_01502,
  that it has a 1.41 Angstrom structure with a PLP Schiff base at Lys43 and a homodimeric assembly, and
  that structural resemblance and the historical carboxyspermidine and carboxynorspermidine names do not
  establish native preference, are already recorded, so do not re-derive them. A companion run on the
  Vibrio cholerae synthase VC_1624 found that the only specificity assignment in that enzyme class is
  for agmatine, that no structure in the family has a diamine bound, and that the enzymes with measured
  kinetics are invariant at every pocket position, so no predictive rule could be fitted; treat the decarboxylase
  side as similarly suspect and say so if it fails the same way. Single analysis only: state which residues
  the structural literature assigns to substrate selection in any carboxypolyamine decarboxylase whose
  preference has been measured, naming the structures and quoting the assignments, and report what CLOLEP_01503
  has at each; state whether any structure of this enzyme class has a carboxypolyamine substrate or product
  bound, as opposed to PLP alone, since a cofactor-only structure cannot define a substrate pocket; report
  whether the genome of this organism encodes the enzymes that would supply each candidate substrate,
  with locus tags, since substrate availability is what the reconstruction actually tested; and state
  whether the adjacent CLOLEP_01502 constrains the answer by its own assignment. State which substrate
  the evidence supports, and say plainly if the determinants are unknown and the question needs a comparative
  kinetic panel on the isolated enzyme.'
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
**Generated:** 2026-11-26T11:52:43.604809

1. PMID:20534592
2. PMID:22025614
3. PMID:42754158
4. PMID:39887002
5. PMID:19196710
6. PMID:27118128
7. PMID:15983049
8. PMID:40074085
9. PMID:27402627
10. PMID:17626020