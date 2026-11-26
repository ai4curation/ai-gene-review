# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** 9FUNG
- **Taxon:** Actinomortierella ambigua (NCBITaxon:1343610)
- **Gene directory:** SUCLG2__A0A9P6TY68
- **Gene symbol:** SUCLG2
- **UniProt accession:** A0A9P6TY68

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-suclg2-nucleotide-gatekeeper
- **Source file:** genes/9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether the succinyl-CoA synthetase containing this Mortierellomycota beta subunit forms GTP or ATP may be decidable at residue level, but not at the position the gap currently rests on, and the companion run on the Blastocystis enzyme says why. Already recorded and not to be re-derived: that this protein groups by sequence with the SUCLG2-type (G-type) beta subunits whose assayed animal members form GTP, that it carries glutamine at the position contacting the guanine base in the pig GTP-specific enzyme, that the same glutamine occurs in the ATP-specific Blastocystis enzyme while the E. coli enzyme with proline there uses both nucleotides, that the genome also encodes an A-type beta subunit and a single alpha subunit as animals do, and that no succinyl-CoA synthetase of any Mortierellomycota species has been assayed. Carry forward and do not re-derive: the published Blastocystis work found that analysis of residues inside the nucleotide-binding site predicted GTP specificity while the enzyme is in fact ATP-specific, and attributed the discrimination to an electrostatic gatekeeper formed by two lysines whose side chains lie outside the binding cavity rather than to the residues in direct substrate contact. Single analysis only. The question this run should answer is whether the gatekeeper model, rather than the contact glutamine, can be applied here. Identify in the Blastocystis sequence the two lysine positions that were proposed to destabilise GTP, map those positions onto this protein and onto a panel of beta subunits whose nucleotide specificity has actually been measured, including the pig GTP-specific and ATP-specific enzymes, the E. coli dual-specificity enzyme and the Blastocystis enzyme, and state for each whether a basic residue occupies the gatekeeper positions. Report the mapping method and say plainly how confident the equivalences are, since this is an alignment across large evolutionary distance and a mis-set column would invent a result. Then state what the panel predicts for this protein, and whether the gatekeeper and contact-residue signals agree or conflict for it. Separately, check whether any structural model of this protein or a close ortholog is available and whether the electrostatic environment of the nucleotide site can be described at all, distinguishing what a predicted model can support from what it cannot. If the gatekeeper positions are not alignable with confidence, or if the panel does not separate the measured specificities cleanly, say so plainly and conclude that the specificity cannot be predicted from sequence; that is an acceptable and expected outcome, and it is more useful than a confident call. Do not propose a GO annotation that names GTP or ATP unless the analysis separates them, and do not treat descent from the G-type lineage as evidence of GTP formation, which is the inference the gap already identifies as unsupported.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether the succinyl-CoA synthetase containing this Mortierellomycota beta subunit forms
  GTP or ATP may be decidable at residue level, but not at the position the gap currently rests on, and
  the companion run on the Blastocystis enzyme says why. Already recorded and not to be re-derived: that
  this protein groups by sequence with the SUCLG2-type (G-type) beta subunits whose assayed animal members
  form GTP, that it carries glutamine at the position contacting the guanine base in the pig GTP-specific
  enzyme, that the same glutamine occurs in the ATP-specific Blastocystis enzyme while the E. coli enzyme
  with proline there uses both nucleotides, that the genome also encodes an A-type beta subunit and a
  single alpha subunit as animals do, and that no succinyl-CoA synthetase of any Mortierellomycota species
  has been assayed. Carry forward and do not re-derive: the published Blastocystis work found that analysis
  of residues inside the nucleotide-binding site predicted GTP specificity while the enzyme is in fact
  ATP-specific, and attributed the discrimination to an electrostatic gatekeeper formed by two lysines
  whose side chains lie outside the binding cavity rather than to the residues in direct substrate contact.
  Single analysis only. The question this run should answer is whether the gatekeeper model, rather than
  the contact glutamine, can be applied here. Identify in the Blastocystis sequence the two lysine positions
  that were proposed to destabilise GTP, map those positions onto this protein and onto a panel of beta
  subunits whose nucleotide specificity has actually been measured, including the pig GTP-specific and
  ATP-specific enzymes, the E. coli dual-specificity enzyme and the Blastocystis enzyme, and state for
  each whether a basic residue occupies the gatekeeper positions. Report the mapping method and say plainly
  how confident the equivalences are, since this is an alignment across large evolutionary distance and
  a mis-set column would invent a result. Then state what the panel predicts for this protein, and whether
  the gatekeeper and contact-residue signals agree or conflict for it. Separately, check whether any structural
  model of this protein or a close ortholog is available and whether the electrostatic environment of
  the nucleotide site can be described at all, distinguishing what a predicted model can support from
  what it cannot. If the gatekeeper positions are not alignable with confidence, or if the panel does
  not separate the measured specificities cleanly, say so plainly and conclude that the specificity cannot
  be predicted from sequence; that is an acceptable and expected outcome, and it is more useful than a
  confident call. Do not propose a GO annotation that names GTP or ATP unless the analysis separates them,
  and do not treat descent from the G-type lineage as evidence of GTP formation, which is the inference
  the gap already identifies as unsupported.'
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
**Generated:** 2026-11-26T15:42:40.498713

1. PMID:18452512
2. PMID:31282474
3. PMID:22751660
4. PMID:33174373
5. PMID:27478903
6. PMID:16481318