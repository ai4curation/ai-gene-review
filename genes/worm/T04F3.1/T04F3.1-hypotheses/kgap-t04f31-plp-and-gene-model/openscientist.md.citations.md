# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** worm
- **Taxon:** Caenorhabditis elegans (NCBITaxon:6239)
- **Gene directory:** T04F3.1
- **Gene symbol:** T04F3.1
- **UniProt accession:** G5EE32

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-t04f31-plp-and-gene-model
- **Source file:** genes/worm/T04F3.1/T04F3.1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether the C-terminal aminotransferase-like domain of C. elegans T04F3.1 can bind PLP, and whether the entry is one giant polypeptide or a mis-joined gene model, are both addressable from sequence and genome data. That the protein is 3,460 residues with a fold-type I domain at 3107-3444 in PANTHER PTHR43795:SF39, that it retains Lys3294, Asp3255 and Arg3427 while lacking the class-I PLP-attachment consensus, and that it diverges at Glu3105, Val3108 and Met3322 where human ACCS has Tyr132, Trp135 and Arg351, are already recorded, so do not re-derive any of it. Single analysis only: state which residues in a characterised fold-type I aminotransferase actually contact PLP, naming the structure and quoting the assignment, and report what T04F3.1 has at each, so that the absence of the consensus signature is separated from the loss of the contacts themselves, since a retained Schiff-base lysine in a pocket that has lost its phosphate-binding residues is a different claim from a competent site; assess whether the pocket is still enclosed in a predicted structure and whether the disordered N-terminus is predicted to occlude it. On the gene-model question, report whether the C. elegans genome places the disordered repeat region and the aminotransferase domain in one transcript supported end to end by reads or cDNAs, whether any neighbouring gene lies within the locus, and whether orthologs in other nematodes carry the same architecture or only the aminotransferase domain, which is the test that distinguishes a real giant protein from a fusion artefact. State whether PLP binding is predicted and whether the gene model is sound, and say plainly if either cannot be settled from available data.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether the C-terminal aminotransferase-like domain of C. elegans T04F3.1 can bind PLP, and
  whether the entry is one giant polypeptide or a mis-joined gene model, are both addressable from sequence
  and genome data. That the protein is 3,460 residues with a fold-type I domain at 3107-3444 in PANTHER
  PTHR43795:SF39, that it retains Lys3294, Asp3255 and Arg3427 while lacking the class-I PLP-attachment
  consensus, and that it diverges at Glu3105, Val3108 and Met3322 where human ACCS has Tyr132, Trp135
  and Arg351, are already recorded, so do not re-derive any of it. Single analysis only: state which residues
  in a characterised fold-type I aminotransferase actually contact PLP, naming the structure and quoting
  the assignment, and report what T04F3.1 has at each, so that the absence of the consensus signature
  is separated from the loss of the contacts themselves, since a retained Schiff-base lysine in a pocket
  that has lost its phosphate-binding residues is a different claim from a competent site; assess whether
  the pocket is still enclosed in a predicted structure and whether the disordered N-terminus is predicted
  to occlude it. On the gene-model question, report whether the C. elegans genome places the disordered
  repeat region and the aminotransferase domain in one transcript supported end to end by reads or cDNAs,
  whether any neighbouring gene lies within the locus, and whether orthologs in other nematodes carry
  the same architecture or only the aminotransferase domain, which is the test that distinguishes a real
  giant protein from a fusion artefact. State whether PLP binding is predicted and whether the gene model
  is sound, and say plainly if either cannot be settled from available data.'
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
**Generated:** 2026-11-26T05:35:22.020385

1. PMID:3167000
2. PMID:2564274
3. PMID:40290371
4. PMID:40082985
5. PMID:36965545
6. PMID:36168305
7. PMID:33846315
8. PMID:32019926
9. PMID:33589689
10. PMID:32365693
11. PMID:31348817
12. PMID:31043480