# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** ENDOG
- **Gene symbol:** ENDOG
- **UniProt accession:** Q14249

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** submitochondrial-localization-ims-vs-matrix
- **Source file:** genes/human/ENDOG/ENDOG-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human ENDOG's targeting and sequence features place it with mitochondrial matrix proteins rather than with intermembrane space proteins.

## Term and Decision Context

- Run ONE analysis, not a survey. Classify the sub-mitochondrial localization of human ENDOG (Q14249) from its sequence, and validate the method on reference proteins whose sub-compartment is already settled. Report a call for ENDOG with a confidence, plus the method's accuracy on the reference sets. Do not spend iterations on anything else.
- Suggested reference sets, extend or substitute if you have better ones. Matrix: TFAM (Q00059), POLG (P54098), POLRMT (O00411), SSBP1 (Q04837), LONP1 (P36776), SOD2 (P04179), HSPD1 (P10809), CS (O75390). Intermembrane space: CYCS (P99999), DIABLO (Q9NR28), CHCHD4 (Q8N4Q1), HTRA2 (O43464), COX17 (Q14061), CHCHD2 (Q9Y6H1), TIMM13 (Q9Y5L4), SMAC. Controls: human EXOG (Q9Y2C4), the paralog that does mtDNA base-excision repair in the matrix; worm CPS-6 (Q95NM6), reported to relocate from intermembrane space to matrix; yeast NUC1 (P08466).
- Features worth computing, if the tools are reachable: presequence and cleavage-site prediction (TargetP, MitoFates, or similar), any bipartite or hydrophobic sorting signal, mature-protein net charge and pI, length, and cysteine spacing including the twin CX9C motif that marks MIA40/CHCHD4 substrates of the intermembrane space. A dedicated sub-mitochondrial predictor such as DeepMito or SubMitoPred is fine to use. Say which tool produced each number.
- Do NOT answer by quoting a database annotation. MitoCarta3.0 (PMID:33174596) carries a sub-mitochondrial assignment and you may report what it says as one line of evidence, but the deliverable is a computed feature comparison against the reference sets. If the only thing you can obtain is the database annotation, say so plainly and report that instead of dressing it up as an analysis.
- Why this matters, for context only, do not re-derive. Fractionation places mammalian EndoG in the intermembrane space and not the matrix (PMID:12444964). In human cells it colocalizes with the matrix nucleoid marker TFAM (PMID:36394256), and its cleavage of mtDNA and, in mouse, of mitochondrial transcripts (PMID:39752519) needs matrix access. The worm ortholog relocates between the two compartments (PMID:27338704). A result that supports either compartment, or that concludes the sequence cannot discriminate, is equally useful.

## Reference Context

- PMID:12444964
- PMID:36394256
- PMID:39752519
- PMID:27338704
- PMID:33174596

## Source Context YAML

```yaml
hypothesis: Human ENDOG's targeting and sequence features place it with mitochondrial matrix proteins
  rather than with intermembrane space proteins.
focus_type: free_text
context:
- Run ONE analysis, not a survey. Classify the sub-mitochondrial localization of human ENDOG (Q14249)
  from its sequence, and validate the method on reference proteins whose sub-compartment is already settled.
  Report a call for ENDOG with a confidence, plus the method's accuracy on the reference sets. Do not
  spend iterations on anything else.
- 'Suggested reference sets, extend or substitute if you have better ones. Matrix: TFAM (Q00059), POLG
  (P54098), POLRMT (O00411), SSBP1 (Q04837), LONP1 (P36776), SOD2 (P04179), HSPD1 (P10809), CS (O75390).
  Intermembrane space: CYCS (P99999), DIABLO (Q9NR28), CHCHD4 (Q8N4Q1), HTRA2 (O43464), COX17 (Q14061),
  CHCHD2 (Q9Y6H1), TIMM13 (Q9Y5L4), SMAC. Controls: human EXOG (Q9Y2C4), the paralog that does mtDNA base-excision
  repair in the matrix; worm CPS-6 (Q95NM6), reported to relocate from intermembrane space to matrix;
  yeast NUC1 (P08466).'
- 'Features worth computing, if the tools are reachable: presequence and cleavage-site prediction (TargetP,
  MitoFates, or similar), any bipartite or hydrophobic sorting signal, mature-protein net charge and pI,
  length, and cysteine spacing including the twin CX9C motif that marks MIA40/CHCHD4 substrates of the
  intermembrane space. A dedicated sub-mitochondrial predictor such as DeepMito or SubMitoPred is fine
  to use. Say which tool produced each number.'
- Do NOT answer by quoting a database annotation. MitoCarta3.0 (PMID:33174596) carries a sub-mitochondrial
  assignment and you may report what it says as one line of evidence, but the deliverable is a computed
  feature comparison against the reference sets. If the only thing you can obtain is the database annotation,
  say so plainly and report that instead of dressing it up as an analysis.
- Why this matters, for context only, do not re-derive. Fractionation places mammalian EndoG in the intermembrane
  space and not the matrix (PMID:12444964). In human cells it colocalizes with the matrix nucleoid marker
  TFAM (PMID:36394256), and its cleavage of mtDNA and, in mouse, of mitochondrial transcripts (PMID:39752519)
  needs matrix access. The worm ortholog relocates between the two compartments (PMID:27338704). A result
  that supports either compartment, or that concludes the sequence cannot discriminate, is equally useful.
reference_id:
- PMID:12444964
- PMID:36394256
- PMID:39752519
- PMID:27338704
- PMID:33174596
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
**Generated:** 2026-10-27T04:53:53.268159

1. PMID:12444964
2. PMID:36394256
3. PMID:39752519
4. PMID:27338704
5. PMID:33174596