# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** DROME
- **Taxon:** Drosophila melanogaster (NCBITaxon:7227)
- **Gene directory:** ttv
- **Gene symbol:** ttv
- **UniProt accession:** D5SHU8

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** fly41-short-isoform-glycosyltransferase
- **Source file:** genes/DROME/ttv/ttv-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The Drosophila melanogaster protein D5SHU8 has glycosyltransferase activity.

## Term and Decision Context

- Term: glycosyltransferase activity (GO:0016757)
- # Focused fly function hypothesis

Hypothesis: The Drosophila melanogaster protein D5SHU8 has glycosyltransferase activity.

Target: Drosophila melanogaster (NCBITaxon:7227), UniProt D5SHU8. Gene label: ttv. Verify identity and isoform independently; the gene label is not evidence for the hypothesis.

## Original prediction

F:glycosyltransferase activity

## Decisive question

Assess glycosyltransferase activity of the supplied exact sequence. Resolve its annotated transcript/isoform and compare it with structurally and biochemically characterized EXT-family proteins and relevant Drosophila partners. Determine which catalytic domain and substrate-binding architecture are present, whether the protein can fold into a functional catalytic unit, and whether partner interactions or targeting are required for intrinsic catalysis versus an in-vivo glycan-biosynthesis role. Neither short length nor a conserved catalytic residue alone settles the question. Distinguish experimentally demonstrated isolated-domain activity from structural plausibility.

## Identity and sequence

- Target record: https://www.uniprot.org/uniprotkb/D5SHU8/entry
- FlyBase identifier(s) from the cohort identity mapping: FBgn0265974.
- Frozen current UniProt sequence: 299 residues; SHA-256 `76d919802eaf321c50ecd217e0e45d5f74f2ec9e6fb7a3806aa74f3433760493`.
- The sequence was frozen for the fly cohort on 2026-09-08. It is not established as the original prediction-time input. Analyze this sequence explicitly and document any alternate accession, version or isoform you analyze.

```fasta
>D5SHU8 Drosophila melanogaster ttv
MPFLLNSMGAEPRHNYTAVIYVQIGAALGPNAALYKLVRTITKSQFVERILVLWAADRPL
PLKKRWPPTSHIPLHVISLGGSTRSQGAGPTSQTTEGRPSISQRFLPYDEIQTDAVLSLD
EDAILNTDELDFAYTVWRDFPERIVGYPARAHFWDDSKNAWGYTSKWTNYYSIVLTGAAF
YHRYYNYLYTNWLSLLLLKTVQQSSNCEDILMNLLVSHVTRKPPIKVTQRKGYKDRETGR
SPWNDPDHFIQRQSCLNTFAAVFGYMPLIRSNLRMDPMLYRDPVSNLRKKYRQIELVGS
```

Primary literature lead to inspect (not a preassigned conclusion): https://pubmed.ncbi.nlm.nih.gov/36593275/

## Evidence and deliverable

Use primary literature and public sequence, structural and genomic resources. This is a focused mechanistic investigation, not a general gene overview. Seek supporting, contrary and competing explanations; an unresolved result is acceptable. Distinguish direct fly experiments, justified transfers and results on a different isoform. Do not equate missing target experiments with evidence of absence.

Do not consult the ai-gene-review repository's current reviews, generated research summaries or local bioinformatics analyses; these are held out for comparison. Agreement with ARBA or repeated prediction text does not validate the biology. Save executed methods/code, actual analysis outputs, sequence identifiers and primary-source URLs/DOIs/PMIDs. Report decisive evidence and limitations, not just a verdict. Do not fabricate computations or use docking/structural resemblance alone as experimental validation.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The Drosophila melanogaster protein D5SHU8 has glycosyltransferase activity.
focus_type: function_assignment
term_id: GO:0016757
term_label: glycosyltransferase activity
context:
- |
  # Focused fly function hypothesis

  Hypothesis: The Drosophila melanogaster protein D5SHU8 has glycosyltransferase activity.

  Target: Drosophila melanogaster (NCBITaxon:7227), UniProt D5SHU8. Gene label: ttv. Verify identity and isoform independently; the gene label is not evidence for the hypothesis.

  ## Original prediction

  F:glycosyltransferase activity

  ## Decisive question

  Assess glycosyltransferase activity of the supplied exact sequence. Resolve its annotated transcript/isoform and compare it with structurally and biochemically characterized EXT-family proteins and relevant Drosophila partners. Determine which catalytic domain and substrate-binding architecture are present, whether the protein can fold into a functional catalytic unit, and whether partner interactions or targeting are required for intrinsic catalysis versus an in-vivo glycan-biosynthesis role. Neither short length nor a conserved catalytic residue alone settles the question. Distinguish experimentally demonstrated isolated-domain activity from structural plausibility.

  ## Identity and sequence

  - Target record: https://www.uniprot.org/uniprotkb/D5SHU8/entry
  - FlyBase identifier(s) from the cohort identity mapping: FBgn0265974.
  - Frozen current UniProt sequence: 299 residues; SHA-256 `76d919802eaf321c50ecd217e0e45d5f74f2ec9e6fb7a3806aa74f3433760493`.
  - The sequence was frozen for the fly cohort on 2026-09-08. It is not established as the original prediction-time input. Analyze this sequence explicitly and document any alternate accession, version or isoform you analyze.

  ```fasta
  >D5SHU8 Drosophila melanogaster ttv
  MPFLLNSMGAEPRHNYTAVIYVQIGAALGPNAALYKLVRTITKSQFVERILVLWAADRPL
  PLKKRWPPTSHIPLHVISLGGSTRSQGAGPTSQTTEGRPSISQRFLPYDEIQTDAVLSLD
  EDAILNTDELDFAYTVWRDFPERIVGYPARAHFWDDSKNAWGYTSKWTNYYSIVLTGAAF
  YHRYYNYLYTNWLSLLLLKTVQQSSNCEDILMNLLVSHVTRKPPIKVTQRKGYKDRETGR
  SPWNDPDHFIQRQSCLNTFAAVFGYMPLIRSNLRMDPMLYRDPVSNLRKKYRQIELVGS
  ```

  Primary literature lead to inspect (not a preassigned conclusion): https://pubmed.ncbi.nlm.nih.gov/36593275/

  ## Evidence and deliverable

  Use primary literature and public sequence, structural and genomic resources. This is a focused mechanistic investigation, not a general gene overview. Seek supporting, contrary and competing explanations; an unresolved result is acceptable. Distinguish direct fly experiments, justified transfers and results on a different isoform. Do not equate missing target experiments with evidence of absence.

  Do not consult the ai-gene-review repository's current reviews, generated research summaries or local bioinformatics analyses; these are held out for comparison. Agreement with ARBA or repeated prediction text does not validate the biology. Save executed methods/code, actual analysis outputs, sequence identifiers and primary-source URLs/DOIs/PMIDs. Report decisive evidence and limitations, not just a verdict. Do not fabricate computations or use docking/structural resemblance alone as experimental validation.
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
**Generated:** 2026-09-08T22:25:08.741024

1. PMID:16303756
2. PMID:17610078
3. PMID:36593275
4. PMID:14645127
5. PMID:14998928