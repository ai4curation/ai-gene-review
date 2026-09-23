# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** HSPA14
- **Gene symbol:** HSPA14
- **UniProt accession:** Q0VDF9

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** atp-hydrolysis-refolding-and-secondary-compartments
- **Source file:** genes/human/HSPA14/HSPA14-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human HSPA14/Hsp70L1 Q0VDF9 has intrinsic ATP hydrolysis activity, participates in refolding of previously denatured proteins, and functions in the nucleus or at plasma membrane under appropriate conditions. Adjudicate each claim separately from its established ATP-binding mRAC cofactor role with DNAJC2/MPP11. Read full PMID21245388: purified E.coli-produced mRAC gives 0.01 ATP/min, above mRAC-LKA and MPP11 but near background; authors explicitly say intrinsic Hsp70L1 hydrolysis cannot be conclusively answered. L1-K68A/E172A hydrolysis-site mutants still complement yeast, whereas ATP-binding-deficient LKA fails. mRAC stimulates separate Hsp70/HSPA1, not a demonstrated DNAJC2 stimulation of HSPA14 itself. Determine whether later purified kinetics or structures resolve the near-background signal. Read PMID21231916 full primary Figures4/5 and exact HSPA14 assays (available ResearchGate accepted manuscript has garbled font extraction) to assess substrate-specific refolding versus aggregation prevention. A negative luciferase assay cannot disprove every client or cofactor context. PMID16002468 establishes human mRAC, not exclusion of other roles. Actual PTHR19375 v19 target leafPTN002500131 descends from ATPase/refolding IBDPTN000452648 and nuclear IBDPTN002500132; the yeast SSZ1 loss nodePTN001065099 is not on this target path. Original plasma-membrane IBA citesPTN002500132, but the current path lacks that term; explain version differences separately from biology. HDA membrane PMID19946888 is a lead; distinguish generic membrane fraction from plasma-membrane activity. DNAJC2 chromatin roles alone do not locate HSPA14. Recombinant HSP70L1 extracellular dendritic/TLR4 stimulation is not evidence of endogenous secretion or membrane residence. Do not infer exclusivity from predominant cytosol, absence of signal peptide, absent target experiment, or single donor.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Human HSPA14/Hsp70L1 Q0VDF9 has intrinsic ATP hydrolysis activity, participates in refolding
  of previously denatured proteins, and functions in the nucleus or at plasma membrane under appropriate
  conditions. Adjudicate each claim separately from its established ATP-binding mRAC cofactor role with
  DNAJC2/MPP11. Read full PMID21245388: purified E.coli-produced mRAC gives 0.01 ATP/min, above mRAC-LKA
  and MPP11 but near background; authors explicitly say intrinsic Hsp70L1 hydrolysis cannot be conclusively
  answered. L1-K68A/E172A hydrolysis-site mutants still complement yeast, whereas ATP-binding-deficient
  LKA fails. mRAC stimulates separate Hsp70/HSPA1, not a demonstrated DNAJC2 stimulation of HSPA14 itself.
  Determine whether later purified kinetics or structures resolve the near-background signal. Read PMID21231916
  full primary Figures4/5 and exact HSPA14 assays (available ResearchGate accepted manuscript has garbled
  font extraction) to assess substrate-specific refolding versus aggregation prevention. A negative luciferase
  assay cannot disprove every client or cofactor context. PMID16002468 establishes human mRAC, not exclusion
  of other roles. Actual PTHR19375 v19 target leafPTN002500131 descends from ATPase/refolding IBDPTN000452648
  and nuclear IBDPTN002500132; the yeast SSZ1 loss nodePTN001065099 is not on this target path. Original
  plasma-membrane IBA citesPTN002500132, but the current path lacks that term; explain version differences
  separately from biology. HDA membrane PMID19946888 is a lead; distinguish generic membrane fraction
  from plasma-membrane activity. DNAJC2 chromatin roles alone do not locate HSPA14. Recombinant HSP70L1
  extracellular dendritic/TLR4 stimulation is not evidence of endogenous secretion or membrane residence.
  Do not infer exclusivity from predominant cytosol, absence of signal peptide, absent target experiment,
  or single donor.'
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
**Generated:** 2026-09-21T04:14:54.806448

1. PMID:21245388
2. PMID:21231916
3. PMID:16002468
4. PMID:30635648
5. PMID:23202586
6. PMID:28067917
7. PMID:17901048
8. PMID:32198371
9. PMID:19946888
10. PMID:14592822
11. PMID:21730052