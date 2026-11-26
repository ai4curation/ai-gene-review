# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** BACSU
- **Taxon:** Bacillus subtilis subsp. subtilis str. 168 (NCBITaxon:224308)
- **Gene directory:** cheB
- **Gene symbol:** cheB
- **UniProt accession:** Q05522

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-cheb-deamidation-sites
- **Source file:** genes/BACSU/cheB/cheB-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether the native receptor deamidation sites of Bacillus subtilis CheB can be identified, and what the physiological contribution of that activity is, is the question, and the tractable part of it is a sequence comparison against the sites where deamidation has actually been demonstrated in another organism. Already recorded and not to be re-derived: that CheB is a receiver-regulated receptor methylesterase of B. subtilis chemotaxis, that it removes methyl esters from chemoreceptor glutamates and participates in sensory adaptation particularly at high attractant concentrations, that CheA can phosphorylate its receiver domain, that a receptor deamidase activity is inferred from the conserved enzyme family rather than demonstrated here, and that McpB Gln371 is discussed as a candidate substrate in the cited work rather than shown to be one. Single analysis only. Begin with the demonstrated cases elsewhere, because they define what a real site looks like: state in which organism and on which receptors CheB-dependent deamidation has been directly shown, name the glutamine positions, say what evidence established them, and say whether the deamidated glutamine occupies a position that is a methyl-accepting glutamate in other receptors of the same family, since that equivalence is the heart of the inference. Then map those positions onto the B. subtilis receptors. Align the methylation-helix regions of McpB and the other B. subtilis chemoreceptors against the receptors with demonstrated sites, report whether a glutamine occupies the equivalent position in each, name the positions in each B. subtilis protein, and state how confident the column assignments are, since the methylation helices are repetitive and a mis-set column would invent a site. Say specifically whether McpB Gln371 falls at a position equivalent to a demonstrated deamidation site or not, which is the one check that would promote or demote the existing candidate. Then address contribution. State whether the B. subtilis receptors are made with glutamines at methylation positions that must be deamidated before methylation can occur, as in the demonstrated cases, or whether they are made with glutamates and so would need no deamidation at all; this is the difference between an essential maturation step and a dispensable one, and it is answerable from the sequences. Say what is known about whether a CheB catalytic mutant separates the two activities in this organism. Conclude with whether the native sites can be named and whether the contribution can be ranked against demethylation. If the alignment does not place a glutamine at an equivalent position, say plainly that the inferred activity may have no substrate in this organism, which would be a more interesting result than confirming it. Do not propose a GO annotation for deamidation unless a site can be named.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether the native receptor deamidation sites of Bacillus subtilis CheB can be identified,
  and what the physiological contribution of that activity is, is the question, and the tractable part
  of it is a sequence comparison against the sites where deamidation has actually been demonstrated in
  another organism. Already recorded and not to be re-derived: that CheB is a receiver-regulated receptor
  methylesterase of B. subtilis chemotaxis, that it removes methyl esters from chemoreceptor glutamates
  and participates in sensory adaptation particularly at high attractant concentrations, that CheA can
  phosphorylate its receiver domain, that a receptor deamidase activity is inferred from the conserved
  enzyme family rather than demonstrated here, and that McpB Gln371 is discussed as a candidate substrate
  in the cited work rather than shown to be one. Single analysis only. Begin with the demonstrated cases
  elsewhere, because they define what a real site looks like: state in which organism and on which receptors
  CheB-dependent deamidation has been directly shown, name the glutamine positions, say what evidence
  established them, and say whether the deamidated glutamine occupies a position that is a methyl-accepting
  glutamate in other receptors of the same family, since that equivalence is the heart of the inference.
  Then map those positions onto the B. subtilis receptors. Align the methylation-helix regions of McpB
  and the other B. subtilis chemoreceptors against the receptors with demonstrated sites, report whether
  a glutamine occupies the equivalent position in each, name the positions in each B. subtilis protein,
  and state how confident the column assignments are, since the methylation helices are repetitive and
  a mis-set column would invent a site. Say specifically whether McpB Gln371 falls at a position equivalent
  to a demonstrated deamidation site or not, which is the one check that would promote or demote the existing
  candidate. Then address contribution. State whether the B. subtilis receptors are made with glutamines
  at methylation positions that must be deamidated before methylation can occur, as in the demonstrated
  cases, or whether they are made with glutamates and so would need no deamidation at all; this is the
  difference between an essential maturation step and a dispensable one, and it is answerable from the
  sequences. Say what is known about whether a CheB catalytic mutant separates the two activities in this
  organism. Conclude with whether the native sites can be named and whether the contribution can be ranked
  against demethylation. If the alignment does not place a glutamine at an equivalent position, say plainly
  that the inferred activity may have no substrate in this organism, which would be a more interesting
  result than confirming it. Do not propose a GO annotation for deamidation unless a site can be named.'
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
**Generated:** 2026-11-26T18:34:40.201619

1. PMID:12011078
2. PMID:22931217
3. PMID:6304723
4. PMID:6300110
5. PMID:10485883
6. PMID:20864474
7. PMID:10825179
8. PMID:7608974
9. PMID:14731274