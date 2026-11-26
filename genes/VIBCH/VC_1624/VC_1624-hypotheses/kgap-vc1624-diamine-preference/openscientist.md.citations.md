# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** VIBCH
- **Taxon:** Vibrio cholerae O1 biovar El Tor str. N16961 (NCBITaxon:243277)
- **Gene directory:** VC_1624
- **Gene symbol:** VC_1624
- **UniProt accession:** Q9KRL3

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-vc1624-diamine-preference
- **Source file:** genes/VIBCH/VC_1624/VC_1624-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether the diamine preference of V. cholerae VC1624 can be predicted at all is the prior question to its quantitative substrate preference, and a companion analysis in this project suggests it cannot. That VC1624 is an NADPH-dependent carboxynorspermidine synthase that condenses L-aspartate 4-semialdehyde with either 1,3-diaminopropane or putrescine, that purified enzyme makes carboxynorspermidine, that the 2023 kinetics concern B. fragilis and C. leptum rather than this enzyme, and that the C6709 genetic data establish both outputs without isolating preference from substrate supply, are already recorded, so do not re-derive them. A companion run on the Pseudomonas putida homolog PP_2928 found that active-site pocket analysis could not discriminate diamine preference and that a genome-absence argument failed a positive control, so treat both approaches as suspect and say so if they fail again. Single analysis only: state which residues the structural literature assigns to diamine selection in any carboxynorspermidine dehydrogenase whose preference has been measured, naming the structures and quoting the assignments, and report what VC1624 and the measured B. fragilis and C. leptum enzymes have at each, so that a predictive pattern is visible as a pattern or absent; state whether the enzymes with measured kinetics differ from VC1624 at those positions in a direction consistent with their measured preferences, which is the only test that would license transfer; report whether V. cholerae encodes a 1,3-diaminopropane biosynthetic route and a putrescine route, with locus tags, since relative substrate supply is the confound the gap names; and state whether the adjacent NspC decarboxylase constrains the answer. State whether a preference can be predicted, and say plainly if the determinants are unknown and the question needs steady-state kinetics on this enzyme.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether the diamine preference of V. cholerae VC1624 can be predicted at all is the prior
  question to its quantitative substrate preference, and a companion analysis in this project suggests
  it cannot. That VC1624 is an NADPH-dependent carboxynorspermidine synthase that condenses L-aspartate
  4-semialdehyde with either 1,3-diaminopropane or putrescine, that purified enzyme makes carboxynorspermidine,
  that the 2023 kinetics concern B. fragilis and C. leptum rather than this enzyme, and that the C6709
  genetic data establish both outputs without isolating preference from substrate supply, are already
  recorded, so do not re-derive them. A companion run on the Pseudomonas putida homolog PP_2928 found
  that active-site pocket analysis could not discriminate diamine preference and that a genome-absence
  argument failed a positive control, so treat both approaches as suspect and say so if they fail again.
  Single analysis only: state which residues the structural literature assigns to diamine selection in
  any carboxynorspermidine dehydrogenase whose preference has been measured, naming the structures and
  quoting the assignments, and report what VC1624 and the measured B. fragilis and C. leptum enzymes have
  at each, so that a predictive pattern is visible as a pattern or absent; state whether the enzymes with
  measured kinetics differ from VC1624 at those positions in a direction consistent with their measured
  preferences, which is the only test that would license transfer; report whether V. cholerae encodes
  a 1,3-diaminopropane biosynthetic route and a putrescine route, with locus tags, since relative substrate
  supply is the confound the gap names; and state whether the adjacent NspC decarboxylase constrains the
  answer. State whether a preference can be predicted, and say plainly if the determinants are unknown
  and the question needs steady-state kinetics on this enzyme.'
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
**Generated:** 2026-11-26T11:00:34.653723

1. PMID:43093060
2. PMID:1955861
3. PMID:19196710
4. PMID:42754158
5. PMID:37437886
6. PMID:22239666
7. PMID:36283333