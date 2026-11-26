# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** BRUMA
- **Taxon:** Brugia malayi (NCBITaxon:6279)
- **Gene directory:** bma-ben-1
- **Gene symbol:** bma-ben-1
- **UniProt accession:** A0A1U7F2B2

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-bmaben1-isotype-target
- **Source file:** genes/BRUMA/bma-ben-1/bma-ben-1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Which Brugia malayi beta-tubulin isotype forms the benzimidazole-engaged target is unresolved, and the tractable approach is to ask which isotype the pharmacology and the genetics of related nematodes actually point to, rather than which one carries a suggestive name. Already recorded and not to be re-derived: that BMA-BEN-1 is an intact beta-tubulin at the WormBase-named bma-ben-1 locus with the conserved Tubulin/FtsZ GTPase and C-terminal beta-tubulin architecture, that deletion of C. elegans BEN-1 confers benzimidazole resistance, and that no B. malayi loss-of-function or allele-swap assay has tested whether this isotype is the flubendazole or oxfendazole response determinant. Single analysis only. Begin with the isotype inventory, because the question is comparative and cannot be answered on one protein. Enumerate the beta-tubulin genes of B. malayi, naming accessions and loci, and state for each its identity to C. elegans BEN-1 and to the other Brugia isotypes, so that it is clear whether bma-ben-1 is the closest relative of the gene whose loss confers resistance or whether another isotype is. Report an effect size or a clear identity ranking rather than an impression. Then take the residues that benzimidazole resistance is known to act through in nematodes, the positions implicated in field and laboratory resistance across parasitic nematode species, and state for each B. malayi isotype which residue occupies each position, confirming the positions in this protein against the local UniProt record. A susceptible isotype and a constitutively resistant one differ at these positions, so the inventory across isotypes is the single most informative thing a sequence analysis can supply here; say plainly if all isotypes are identical at every position, which would mean sequence cannot discriminate them. Then address expression and localisation, since a target must be present in the tissue the drug acts on: state what is known about which isotypes are expressed in B. malayi and in which life-cycle stages and tissues, naming the datasets, and say whether any isotype is restricted in a way that would exclude or favour it as the drug target. Consider also whether the genetics of related species helps: state whether the resistance-associated gene in other filarial or parasitic nematodes is the ortholog of this locus or of a different isotype, which is a comparative-genomics question with a definite answer. Finally say which isotype the evidence favours and with what strength, and if the available evidence cannot separate them, say so plainly and name the experiment that would, which is likely an allele swap or a stage-specific knockdown. An unresolved verdict is acceptable. Do not treat the gene name as evidence of orthology to C. elegans BEN-1, and do not propose a GO annotation naming a drug response for this protein.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Which Brugia malayi beta-tubulin isotype forms the benzimidazole-engaged target is unresolved,
  and the tractable approach is to ask which isotype the pharmacology and the genetics of related nematodes
  actually point to, rather than which one carries a suggestive name. Already recorded and not to be re-derived:
  that BMA-BEN-1 is an intact beta-tubulin at the WormBase-named bma-ben-1 locus with the conserved Tubulin/FtsZ
  GTPase and C-terminal beta-tubulin architecture, that deletion of C. elegans BEN-1 confers benzimidazole
  resistance, and that no B. malayi loss-of-function or allele-swap assay has tested whether this isotype
  is the flubendazole or oxfendazole response determinant. Single analysis only. Begin with the isotype
  inventory, because the question is comparative and cannot be answered on one protein. Enumerate the
  beta-tubulin genes of B. malayi, naming accessions and loci, and state for each its identity to C. elegans
  BEN-1 and to the other Brugia isotypes, so that it is clear whether bma-ben-1 is the closest relative
  of the gene whose loss confers resistance or whether another isotype is. Report an effect size or a
  clear identity ranking rather than an impression. Then take the residues that benzimidazole resistance
  is known to act through in nematodes, the positions implicated in field and laboratory resistance across
  parasitic nematode species, and state for each B. malayi isotype which residue occupies each position,
  confirming the positions in this protein against the local UniProt record. A susceptible isotype and
  a constitutively resistant one differ at these positions, so the inventory across isotypes is the single
  most informative thing a sequence analysis can supply here; say plainly if all isotypes are identical
  at every position, which would mean sequence cannot discriminate them. Then address expression and localisation,
  since a target must be present in the tissue the drug acts on: state what is known about which isotypes
  are expressed in B. malayi and in which life-cycle stages and tissues, naming the datasets, and say
  whether any isotype is restricted in a way that would exclude or favour it as the drug target. Consider
  also whether the genetics of related species helps: state whether the resistance-associated gene in
  other filarial or parasitic nematodes is the ortholog of this locus or of a different isotype, which
  is a comparative-genomics question with a definite answer. Finally say which isotype the evidence favours
  and with what strength, and if the available evidence cannot separate them, say so plainly and name
  the experiment that would, which is likely an allele swap or a stage-specific knockdown. An unresolved
  verdict is acceptable. Do not treat the gene name as evidence of orthology to C. elegans BEN-1, and
  do not propose a GO annotation naming a drug response for this protein.'
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
**Generated:** 2026-11-26T19:52:41.119138

1. PMID:16103581
2. PMID:9576511
3. PMID:16197589
4. PMID:22677339
5. PMID:2052017
6. PMID:22180794
7. PMID:31796568
8. PMID:27733308
9. PMID:2592410
10. PMID:42247472
11. PMID:35961997
12. PMID:42302569
13. PMID:38370666
14. PMID:27145083
15. PMID:42547829
16. PMID:35671324
17. PMID:42931220
18. PMID:39652258