# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** PANAN
- **Taxon:** Pantoea ananatis (NCBITaxon:553)
- **Gene directory:** crtY
- **Gene symbol:** crtY
- **UniProt accession:** P21687

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-crty-membrane-docking
- **Source file:** genes/PANAN/crtY/crtY-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

How CrtY (P21687) docks onto a membrane to reach its hydrophobic substrate may be predictable from sequence and model. That the inner-membrane location is experimentally supported, that there is no signal peptide or transmembrane span so an integral multipass topology is excluded, and that Glu199 is a catalytic residue, is already established, so do not re-derive it. Single analysis only: from the AlphaFold model, compute the surface distribution of hydrophobic and basic residues and identify every candidate monotopic membrane-binding element, including amphipathic helices with their hydrophobic moments, exposed hydrophobic patches with their areas, and basic patches that could read anionic phospholipid headgroups, giving residue ranges for each; state the spatial relationship between the strongest candidate element and both the predicted FAD site and Glu199, and whether the geometry would place the substrate-entry channel at the membrane surface; compare these features with structurally characterised monotopic membrane enzymes that act on lipophilic substrates, and with a soluble FAD enzyme of the same fold family as a negative control; and report conservation of the candidate element across bacterial lycopene cyclases and in the fused plant and fungal enzymes. State which element most likely mediates peripheral membrane docking and which mutation would test it, and say plainly if the model cannot distinguish a genuine membrane-binding element from an ordinary hydrophobic surface.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'How CrtY (P21687) docks onto a membrane to reach its hydrophobic substrate may be predictable
  from sequence and model. That the inner-membrane location is experimentally supported, that there is
  no signal peptide or transmembrane span so an integral multipass topology is excluded, and that Glu199
  is a catalytic residue, is already established, so do not re-derive it. Single analysis only: from the
  AlphaFold model, compute the surface distribution of hydrophobic and basic residues and identify every
  candidate monotopic membrane-binding element, including amphipathic helices with their hydrophobic moments,
  exposed hydrophobic patches with their areas, and basic patches that could read anionic phospholipid
  headgroups, giving residue ranges for each; state the spatial relationship between the strongest candidate
  element and both the predicted FAD site and Glu199, and whether the geometry would place the substrate-entry
  channel at the membrane surface; compare these features with structurally characterised monotopic membrane
  enzymes that act on lipophilic substrates, and with a soluble FAD enzyme of the same fold family as
  a negative control; and report conservation of the candidate element across bacterial lycopene cyclases
  and in the fused plant and fungal enzymes. State which element most likely mediates peripheral membrane
  docking and which mutation would test it, and say plainly if the model cannot distinguish a genuine
  membrane-binding element from an ordinary hydrophobic surface.'
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
**Generated:** 2026-11-25T15:39:02.342161

1. PMID:15113001
2. PMID:42315832
3. PMID:29222193
4. PMID:30626872
5. PMID:42943443
6. PMID:42825966
7. PMID:41092119
8. PMID:20178989
9. PMID:9931258
10. PMID:18247576
11. PMID:41980065
12. PMID:9295270
13. PMID:42051075
14. PMID:41102519
15. PMID:41131924
16. PMID:12031670
17. PMID:42121163
18. PMID:42201412