# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** CANAL
- **Taxon:** Candida albicans SC5314 (NCBITaxon:237561)
- **Gene directory:** EAF3
- **Gene symbol:** EAF3
- **UniProt accession:** Q59K07

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-caeaf3-rpd31s-interface
- **Source file:** genes/CANAL/EAF3/EAF3-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether Candida albicans Eaf3 can associate with an Rco1/Rpd31-containing Rpd3S-type deacetylase complex may be decidable from the interface, independently of the purifications that failed to recover it. That CaEaf3 has an N-terminal Tudor-knot/chromo-like module and a C-terminal MRG interaction domain, that it belongs to the fungal Eaf3/Alp13 branch, that PAINT supports Rpd3S inheritance, and that the 2016 Candida study's Rpd3/Rpd31 purifications did not recover Eaf3 or Rco1, are already recorded, so do not re-derive them. Single analysis only: identify from the structural literature the residues of the S. cerevisiae Eaf3 MRG domain that contact Rco1, and the reciprocal Rco1 residues, naming the structures and quoting the statements that assign the interface; align CaEaf3 to ScEaf3 and the C. albicans Rco1 ortholog to ScRco1 and report, position by position, whether each interface residue is conserved, conservatively substituted or lost, so that a retained interface is distinguishable from a decayed one; state whether C. albicans encodes a single Rco1 ortholog and whether it keeps the PHD and Sin3-interaction regions that the complex requires, since a missing partner would explain the absence without any change on the Eaf3 side; and assess whether the reported failure to recover Eaf3 and Rco1 is informative, by stating what is known about the stoichiometry and salt-lability of the Rpd3S complex and whether the purification conditions used would be expected to retain it. State whether the association is predicted to occur, and say plainly if an interface analysis cannot distinguish a genuine absence from a purification artefact.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether Candida albicans Eaf3 can associate with an Rco1/Rpd31-containing Rpd3S-type deacetylase
  complex may be decidable from the interface, independently of the purifications that failed to recover
  it. That CaEaf3 has an N-terminal Tudor-knot/chromo-like module and a C-terminal MRG interaction domain,
  that it belongs to the fungal Eaf3/Alp13 branch, that PAINT supports Rpd3S inheritance, and that the
  2016 Candida study''s Rpd3/Rpd31 purifications did not recover Eaf3 or Rco1, are already recorded, so
  do not re-derive them. Single analysis only: identify from the structural literature the residues of
  the S. cerevisiae Eaf3 MRG domain that contact Rco1, and the reciprocal Rco1 residues, naming the structures
  and quoting the statements that assign the interface; align CaEaf3 to ScEaf3 and the C. albicans Rco1
  ortholog to ScRco1 and report, position by position, whether each interface residue is conserved, conservatively
  substituted or lost, so that a retained interface is distinguishable from a decayed one; state whether
  C. albicans encodes a single Rco1 ortholog and whether it keeps the PHD and Sin3-interaction regions
  that the complex requires, since a missing partner would explain the absence without any change on the
  Eaf3 side; and assess whether the reported failure to recover Eaf3 and Rco1 is informative, by stating
  what is known about the stoichiometry and salt-lability of the Rpd3S complex and whether the purification
  conditions used would be expected to retain it. State whether the association is predicted to occur,
  and say plainly if an interface analysis cannot distinguish a genuine absence from a purification artefact.'
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
**Generated:** 2026-11-26T04:12:29.243766

1. PMID:27935838
2. PMID:25578729
3. PMID:38065958
4. PMID:37468628
5. PMID:17510366
6. PMID:26747610
7. PMID:16286007
8. PMID:36190236
9. PMID:18490440
10. PMID:37798513
11. PMID:39779918
12. PMID:30594984
13. PMID:37577459
14. PMID:37666978
15. PMID:16286008
16. PMID:17179083
17. PMID:22728643
18. PMID:27868254
19. PMID:25601565
20. PMID:20730094