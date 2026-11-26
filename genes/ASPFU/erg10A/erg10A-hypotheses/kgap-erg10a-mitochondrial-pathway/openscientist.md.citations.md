# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** ASPFU
- **Taxon:** Aspergillus fumigatus Af293 (NCBITaxon:330879)
- **Gene directory:** erg10A
- **Gene symbol:** erg10A
- **UniProt accession:** Q4WLA8

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-erg10a-mitochondrial-pathway
- **Source file:** genes/ASPFU/erg10A/erg10A-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Which mitochondrial pathway consumes or produces the acetoacetyl-CoA that AfErg10A's thiolase activity handles is the question, and the useful move is to ask what the organism's own metabolic inventory permits rather than to assume the mammalian ketone-body answer. Already recorded and not to be re-derived: that purified AfErg10A catalyses both the synthetic and the degradative acetoacetyl-CoA thiolase reactions reversibly, that a functional C-terminal GFP fusion colocalises with mitochondrial dye in hyphae, that the gene is essential, that it sits in the PTHR18919:SF156 ACAT1-like branch, and that UniProt's curated FUNCTION comment states Erg10A has no overlapping function with the cytosolic Erg10B and appears not to be involved in ergosterol biosynthesis. Single analysis only. Begin with the inventory, because it decides which candidate pathways are even available. For Aspergillus fumigatus, establish from the genome, naming accessions, whether the organism encodes the enzymes of mitochondrial ketone-body formation and utilisation, namely HMG-CoA synthase of the mitochondrial type and HMG-CoA lyase on the synthetic side and succinyl-CoA:3-oxoacid CoA-transferase and beta-hydroxybutyrate dehydrogenase on the utilisation side, and say which of those are present and which absent. The absence of a CoA-transferase in particular would make ketone-body utilisation impossible and would remove the obvious mammalian analogy, so state it plainly either way. Then take the alternatives in turn and say what the inventory and the literature permit for each: terminal beta-oxidation of fatty acids, in which the thiolase performs the last degradative step, noting whether beta-oxidation in this organism is peroxisomal, mitochondrial or both and which enzymes are localised where; isoleucine and other branched-chain amino acid catabolism, which produces 2-methylacetoacetyl-CoA rather than acetoacetyl-CoA, so state whether this enzyme's measured substrate preference distinguishes the two; leucine catabolism, which converges on HMG-CoA; and the biosynthetic direction supplying acetoacetyl-CoA for a mitochondrial polyketide, siderophore or secondary metabolite route, naming any such route the organism has. Essentiality is a constraint worth using: say which of the candidate pathways would plausibly be essential in this organism under laboratory conditions, since a dispensable catabolic route does not explain an essential gene, and note explicitly if the essentiality is better explained by a function other than the thiolase reaction, for example a role in complex assembly or an unrelated moonlighting activity. Conclude with which pathway the evidence favours and with what strength. If the inventory does not single out one pathway, say so plainly and name the measurement that would settle it; an unresolved verdict is acceptable. Do not assume the mammalian ACAT1 role transfers on the strength of the branch assignment, and do not propose a GO process annotation for a pathway whose enzymes this organism lacks.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Which mitochondrial pathway consumes or produces the acetoacetyl-CoA that AfErg10A''s thiolase
  activity handles is the question, and the useful move is to ask what the organism''s own metabolic inventory
  permits rather than to assume the mammalian ketone-body answer. Already recorded and not to be re-derived:
  that purified AfErg10A catalyses both the synthetic and the degradative acetoacetyl-CoA thiolase reactions
  reversibly, that a functional C-terminal GFP fusion colocalises with mitochondrial dye in hyphae, that
  the gene is essential, that it sits in the PTHR18919:SF156 ACAT1-like branch, and that UniProt''s curated
  FUNCTION comment states Erg10A has no overlapping function with the cytosolic Erg10B and appears not
  to be involved in ergosterol biosynthesis. Single analysis only. Begin with the inventory, because it
  decides which candidate pathways are even available. For Aspergillus fumigatus, establish from the genome,
  naming accessions, whether the organism encodes the enzymes of mitochondrial ketone-body formation and
  utilisation, namely HMG-CoA synthase of the mitochondrial type and HMG-CoA lyase on the synthetic side
  and succinyl-CoA:3-oxoacid CoA-transferase and beta-hydroxybutyrate dehydrogenase on the utilisation
  side, and say which of those are present and which absent. The absence of a CoA-transferase in particular
  would make ketone-body utilisation impossible and would remove the obvious mammalian analogy, so state
  it plainly either way. Then take the alternatives in turn and say what the inventory and the literature
  permit for each: terminal beta-oxidation of fatty acids, in which the thiolase performs the last degradative
  step, noting whether beta-oxidation in this organism is peroxisomal, mitochondrial or both and which
  enzymes are localised where; isoleucine and other branched-chain amino acid catabolism, which produces
  2-methylacetoacetyl-CoA rather than acetoacetyl-CoA, so state whether this enzyme''s measured substrate
  preference distinguishes the two; leucine catabolism, which converges on HMG-CoA; and the biosynthetic
  direction supplying acetoacetyl-CoA for a mitochondrial polyketide, siderophore or secondary metabolite
  route, naming any such route the organism has. Essentiality is a constraint worth using: say which of
  the candidate pathways would plausibly be essential in this organism under laboratory conditions, since
  a dispensable catabolic route does not explain an essential gene, and note explicitly if the essentiality
  is better explained by a function other than the thiolase reaction, for example a role in complex assembly
  or an unrelated moonlighting activity. Conclude with which pathway the evidence favours and with what
  strength. If the inventory does not single out one pathway, say so plainly and name the measurement
  that would settle it; an unresolved verdict is acceptable. Do not assume the mammalian ACAT1 role transfers
  on the strength of the branch assignment, and do not propose a GO process annotation for a pathway whose
  enzymes this organism lacks.'
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
**Generated:** 2026-11-26T15:08:06.662366

1. PMID:18245820
2. PMID:18331473
3. PMID:32005728
4. PMID:17371050
5. PMID:15554960
6. PMID:16008561
7. PMID:22106303
8. PMID:24649827