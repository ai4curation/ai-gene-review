# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** BLAHN
- **Taxon:** Blastocystis sp. ATCC 50177/Nand II (NCBITaxon:478820)
- **Gene directory:** SCSb
- **Gene symbol:** SCSb
- **UniProt accession:** B3FHP0

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-scsb-gtp-exclusion-site
- **Source file:** genes/BLAHN/SCSb/SCSb-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether GTP is excluded from this ATP-specific succinyl-CoA synthetase at the entrance of the nucleotide site, inside it, or both, is the question, and a companion run in this campaign has already established something about these residues that sharpens it. Already recorded and not to be re-derived: that there is no detectable activity with GTP in two studies, that Gln20 hydrogen-bonds adenine in structures of the isolated nucleotide-binding domain, that exchanging Lys46 and Lys114 for acidic residues gives an enzyme preferring GTP in kinetic assays, that the double mutant crystallised only with ADP, and that no structure of the alpha/beta enzyme and none with a guanine nucleotide exists. Carry forward and do not re-derive: a run on the Mortierellomycota SUCLG2-type beta subunit mapped Lys46 and Lys114 across the family with two independent methods agreeing at all 48 site-protein combinations, confirmed that their side chains lie 6.98 and 5.21 Angstrom from bound ADP against 1.77 Angstrom for Gln20, and then found that basic character at either position fails to separate the measured GTP users from the measured ATP users across a seven-protein panel, with the Thermus enzyme preferring GDP and GTP while carrying a basic arginine at the first position and the ATP-specific mammalian subunits carrying aspartate there. Hold the distinction that result forces: a substitution that changes preference in this protein shows those residues are sufficient to perturb selection in this structural context, and does not show they are the family-wide determinant. This run should ask what mechanism is consistent with both facts. Single analysis only. Address exclusion at the entrance against exclusion inside the site as competing hypotheses with observable consequences. State what the available structures of the nucleotide-binding domain show about the path a nucleotide must take to reach the site, whether the two lysines line that path, and whether their replacement by acidic residues would be expected to change affinity, selectivity or both, distinguishing an electrostatic steering effect at the mouth from a change in the bound-state hydrogen-bonding network. Say what the kinetic signature of each mechanism would be, in terms of the Michaelis constant against the turnover number for the two nucleotides, and then say what the published kinetics of the wild type and the double mutant actually show on that axis, quoting the values if they are retrievable and saying plainly if they are not. Examine whether Gln20 can discriminate adenine from guanine at all on hydrogen-bonding grounds, given that the same glutamine occurs in GTP-specific animal enzymes, and state what else in the pocket differs between this enzyme and a GTP-specific one. Finally state whether the two mechanisms can be separated by any published observation, and if they cannot, name the single experiment that would separate them; an unresolved verdict is acceptable and expected here. Do not treat the double-mutant result as establishing a general determinant of nucleotide specificity, and do not propose a GO annotation on the strength of this analysis.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether GTP is excluded from this ATP-specific succinyl-CoA synthetase at the entrance of
  the nucleotide site, inside it, or both, is the question, and a companion run in this campaign has already
  established something about these residues that sharpens it. Already recorded and not to be re-derived:
  that there is no detectable activity with GTP in two studies, that Gln20 hydrogen-bonds adenine in structures
  of the isolated nucleotide-binding domain, that exchanging Lys46 and Lys114 for acidic residues gives
  an enzyme preferring GTP in kinetic assays, that the double mutant crystallised only with ADP, and that
  no structure of the alpha/beta enzyme and none with a guanine nucleotide exists. Carry forward and do
  not re-derive: a run on the Mortierellomycota SUCLG2-type beta subunit mapped Lys46 and Lys114 across
  the family with two independent methods agreeing at all 48 site-protein combinations, confirmed that
  their side chains lie 6.98 and 5.21 Angstrom from bound ADP against 1.77 Angstrom for Gln20, and then
  found that basic character at either position fails to separate the measured GTP users from the measured
  ATP users across a seven-protein panel, with the Thermus enzyme preferring GDP and GTP while carrying
  a basic arginine at the first position and the ATP-specific mammalian subunits carrying aspartate there.
  Hold the distinction that result forces: a substitution that changes preference in this protein shows
  those residues are sufficient to perturb selection in this structural context, and does not show they
  are the family-wide determinant. This run should ask what mechanism is consistent with both facts. Single
  analysis only. Address exclusion at the entrance against exclusion inside the site as competing hypotheses
  with observable consequences. State what the available structures of the nucleotide-binding domain show
  about the path a nucleotide must take to reach the site, whether the two lysines line that path, and
  whether their replacement by acidic residues would be expected to change affinity, selectivity or both,
  distinguishing an electrostatic steering effect at the mouth from a change in the bound-state hydrogen-bonding
  network. Say what the kinetic signature of each mechanism would be, in terms of the Michaelis constant
  against the turnover number for the two nucleotides, and then say what the published kinetics of the
  wild type and the double mutant actually show on that axis, quoting the values if they are retrievable
  and saying plainly if they are not. Examine whether Gln20 can discriminate adenine from guanine at all
  on hydrogen-bonding grounds, given that the same glutamine occurs in GTP-specific animal enzymes, and
  state what else in the pocket differs between this enzyme and a GTP-specific one. Finally state whether
  the two mechanisms can be separated by any published observation, and if they cannot, name the single
  experiment that would separate them; an unresolved verdict is acceptable and expected here. Do not treat
  the double-mutant result as establishing a general determinant of nucleotide specificity, and do not
  propose a GO annotation on the strength of this analysis.'
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
**Generated:** 2026-11-26T17:04:04.929587

1. PMID:27478903
2. PMID:31282474
3. PMID:18452512