# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** PSEPK
- **Taxon:** Pseudomonas putida KT2440 (NCBITaxon:160488)
- **Gene directory:** PP_1451
- **Gene symbol:** PP_1451
- **UniProt accession:** Q88MW7

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-pp1451-tether-hydrolase
- **Source file:** genes/PSEPK/PP_1451/PP_1451-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether PP_1451 is a competent tether hydrolase, and what it acts on, may be assessable from its catalytic site and its genomic context. That it is a small Sec-exported YafK/LdtF-family cysteine hydrolase predicted to act in the periplasm, and predicted to hydrolyse the amide bond linking OprI-like outer-membrane lipoproteins to peptidoglycan, are already recorded, so do not re-derive them. Single analysis only: identify the catalytic residues of a characterised LdtF or YafK-family hydrolase, naming the structure and quoting the assignment, and state what PP_1451 has at each, so a competent cysteine-histidine site is distinguished from a fold that merely belongs to the family; state whether the residues that in the characterised enzyme contact the peptidoglycan stem peptide and the lipoprotein lysine are retained, since those are what set substrate specificity rather than activity; test the second gap's proposal directly by searching the KT2440 genome for L,D-transpeptidases of both kinds, the lipoprotein-anchoring ErfK type and the 3-to-3 crosslinking YcbB type, reporting locus tags and the basis for each call, since the proposal that KT2440 lacks a dedicated crosslinking enzyme stands or falls on that inventory; and state whether the LdtF-type hydrolase and the anchoring transpeptidase co-occur across Pseudomonas and other gammaproteobacterial genomes, and whether any genome carries one without the other. State whether tether hydrolysis is the supported activity and whether KT2440 lacks a 3-to-3 crosslinking enzyme, and say plainly if the site cannot be distinguished from a related hydrolase activity on sequence alone.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether PP_1451 is a competent tether hydrolase, and what it acts on, may be assessable from
  its catalytic site and its genomic context. That it is a small Sec-exported YafK/LdtF-family cysteine
  hydrolase predicted to act in the periplasm, and predicted to hydrolyse the amide bond linking OprI-like
  outer-membrane lipoproteins to peptidoglycan, are already recorded, so do not re-derive them. Single
  analysis only: identify the catalytic residues of a characterised LdtF or YafK-family hydrolase, naming
  the structure and quoting the assignment, and state what PP_1451 has at each, so a competent cysteine-histidine
  site is distinguished from a fold that merely belongs to the family; state whether the residues that
  in the characterised enzyme contact the peptidoglycan stem peptide and the lipoprotein lysine are retained,
  since those are what set substrate specificity rather than activity; test the second gap''s proposal
  directly by searching the KT2440 genome for L,D-transpeptidases of both kinds, the lipoprotein-anchoring
  ErfK type and the 3-to-3 crosslinking YcbB type, reporting locus tags and the basis for each call, since
  the proposal that KT2440 lacks a dedicated crosslinking enzyme stands or falls on that inventory; and
  state whether the LdtF-type hydrolase and the anchoring transpeptidase co-occur across Pseudomonas and
  other gammaproteobacterial genomes, and whether any genome carries one without the other. State whether
  tether hydrolysis is the supported activity and whether KT2440 lacks a 3-to-3 crosslinking enzyme, and
  say plainly if the site cannot be distinguished from a related hydrolase activity on sequence alone.'
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
**Generated:** 2026-11-26T10:46:51.244359

1. PMID:37830798
2. PMID:37255442
3. PMID:33941679
4. PMID:33947763
5. PMID:42100858
6. PMID:2502533
7. PMID:23123904
8. PMID:36602318
9. PMID:9163432
10. PMID:23246592
11. PMID:15259268