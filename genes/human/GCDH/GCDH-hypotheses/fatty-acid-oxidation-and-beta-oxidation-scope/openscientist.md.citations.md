# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** GCDH
- **Gene symbol:** GCDH
- **UniProt accession:** Q92947

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** fatty-acid-oxidation-and-beta-oxidation-scope
- **Source file:** genes/human/GCDH/GCDH-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human GCDH Q92947 participates in fatty acid oxidation GO:0019395 and specifically fatty acid beta-oxidation using acyl-CoA dehydrogenase GO:0033539. Adjudicate separately using exact process definitions, substrate chemistry, full primary studies and phylogenetic placement. Exact PTHR42807 target PTN002533783 descends from positive IBD PTN005130278; GO:0033539 IBD uses Q92947 itself, which is legitimate experimental grounding, not circularity. The target IDA cites PMID25416781: the accessible cache contains abstract/introduction/discussion but omits the assay methods/results. Obtain the full assays and determine which substrate was tested with GCDH versus MCAD. RHEA13389 oxidatively decarboxylates glutaryl-CoA to crotonyl-CoA, with ETF as electron acceptor. Current ChEBI57378 glutaryl-CoA(5-) has parent177898 omega-carboxy-(fatty acyl)-CoA(5-), so dicarboxylate chemistry alone is not exclusion from fatty-acid oxidation. GO0033539 specifically describes iterative beta-oxidation beginning with fatty-acid activation and ending in acetyl/propionyl-CoA; distinguish that from a related dehydrogenation and decarboxylation. PMID21974953 directly compared rat GCDH substrate specificity with short/medium-chain ACADs; recover its substrate table rather than infer no fatty acyl substrates from a lysine-pathway label. PMID37198486 shows GCDH-generated crotonyl-CoA in human cells, and PMID17176108 identifies product release as rate limiting. Fatty-acyl-CoA binding and biosynthesis are independently plausible and are not the disputed hypotheses here. Determine any demonstrated secondary fatty-acid oxidation capability versus only downstream metabolic convergence. Do not equate lack of one assay, low relative activity, or predominant amino-acid catabolism with absence of all other capacities.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Human GCDH Q92947 participates in fatty acid oxidation GO:0019395 and specifically fatty
  acid beta-oxidation using acyl-CoA dehydrogenase GO:0033539. Adjudicate separately using exact process
  definitions, substrate chemistry, full primary studies and phylogenetic placement. Exact PTHR42807 target
  PTN002533783 descends from positive IBD PTN005130278; GO:0033539 IBD uses Q92947 itself, which is legitimate
  experimental grounding, not circularity. The target IDA cites PMID25416781: the accessible cache contains
  abstract/introduction/discussion but omits the assay methods/results. Obtain the full assays and determine
  which substrate was tested with GCDH versus MCAD. RHEA13389 oxidatively decarboxylates glutaryl-CoA
  to crotonyl-CoA, with ETF as electron acceptor. Current ChEBI57378 glutaryl-CoA(5-) has parent177898
  omega-carboxy-(fatty acyl)-CoA(5-), so dicarboxylate chemistry alone is not exclusion from fatty-acid
  oxidation. GO0033539 specifically describes iterative beta-oxidation beginning with fatty-acid activation
  and ending in acetyl/propionyl-CoA; distinguish that from a related dehydrogenation and decarboxylation.
  PMID21974953 directly compared rat GCDH substrate specificity with short/medium-chain ACADs; recover
  its substrate table rather than infer no fatty acyl substrates from a lysine-pathway label. PMID37198486
  shows GCDH-generated crotonyl-CoA in human cells, and PMID17176108 identifies product release as rate
  limiting. Fatty-acyl-CoA binding and biosynthesis are independently plausible and are not the disputed
  hypotheses here. Determine any demonstrated secondary fatty-acid oxidation capability versus only downstream
  metabolic convergence. Do not equate lack of one assay, low relative activity, or predominant amino-acid
  catabolism with absence of all other capacities.'
focus_type: function_assignment
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
**Generated:** 2026-09-21T05:58:12.886838

1. PMID:25416781
2. PMID:15274622
3. PMID:37198486
4. PMID:17176108
5. PMID:21974953
6. PMID:11024031
7. PMID:3597357