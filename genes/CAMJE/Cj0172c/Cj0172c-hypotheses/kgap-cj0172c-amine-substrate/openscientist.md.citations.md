# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** CAMJE
- **Taxon:** Campylobacter jejuni subsp. jejuni NCTC 11168 = ATCC 700819 (NCBITaxon:192222)
- **Gene directory:** Cj0172c
- **Gene symbol:** Cj0172c
- **UniProt accession:** Q0PBW7

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-cj0172c-amine-substrate
- **Source file:** genes/CAMJE/Cj0172c/Cj0172c-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether Cj0172c is the carboxypolyamine dehydrogenase that supplies the Campylobacter jejuni spermidine route, and which amine it condenses with aspartate semialdehyde, is sharpened rather than settled by the one perturbation on record, and the shape of that result is the place to start. Already recorded and not to be re-derived: that Cj0172c is a predicted NADPH-dependent carboxypolyamine dehydrogenase of NCTC 11168, that family evidence supports reductive condensation of an amine with aspartate semialdehyde, that the imported saccharopine dehydrogenase name is not validated, and that deleting the corresponding candidate C8J_0166 in strain 81116 increased rather than abolished spermidine accumulation. Carry forward from the completed run on the Clostridium leptum decarboxylase CLOLEP_01503 and do not re-derive it: that the only residue the structural literature names as a substrate-selection determinant in the carboxypolyamine decarboxylases is wild type across the family and cannot discriminate carboxyspermidine from carboxynorspermidine from carboxyaminopropylagmatine, that no structure in that family holds a carboxypolyamine, and that in Clostridium the assignment ultimately rested on amine supply plus the measured preference of the partner enzyme rather than on any pocket feature. Single analysis only. Begin with the deletion result, because an increase is more informative than a loss: state what else C8J_0166 loss changed, whether the strain still made spermidine and by what route it could have, whether the gene lies in an operon whose polarity the deletion could have altered, whether 81116 and NCTC 11168 carry the same complement of polyamine genes, and what hypotheses an increase is compatible with, including the possibility that the gene is not in the spermidine route at all or that its loss relieves consumption of a shared precursor. Then establish the amine supply in NCTC 11168 as was done for Clostridium: name the accessions for arginine decarboxylase, agmatinase or aminopropylagmatine ureohydrolase, ornithine decarboxylase and the diaminobutyrate route, and say which amines the cell can actually make, since an amine the organism cannot supply is not a candidate substrate however well it fits. State what the partner decarboxylase in this genome is, whether it has been assayed, and what is known about the native product of the C. jejuni enzyme, bearing in mind the published finding that the carboxynorspermidine decarboxylase orthologue of this organism makes spermidine rather than norspermidine in vivo. Finally say whether the aspartate-semialdehyde-dependent condensation can be assigned to Q0PBW7 at all on the evidence available, and with what substrate; if the cofactor and reaction class can be constrained while the substrate cannot, report that split explicitly, as the Clostridium analysis did. Do not infer the substrate from the family name or from the operon, and do not recommend replacing the existing UNDECIDED action unless the evidence supports a specific activity for this protein.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether Cj0172c is the carboxypolyamine dehydrogenase that supplies the Campylobacter jejuni
  spermidine route, and which amine it condenses with aspartate semialdehyde, is sharpened rather than
  settled by the one perturbation on record, and the shape of that result is the place to start. Already
  recorded and not to be re-derived: that Cj0172c is a predicted NADPH-dependent carboxypolyamine dehydrogenase
  of NCTC 11168, that family evidence supports reductive condensation of an amine with aspartate semialdehyde,
  that the imported saccharopine dehydrogenase name is not validated, and that deleting the corresponding
  candidate C8J_0166 in strain 81116 increased rather than abolished spermidine accumulation. Carry forward
  from the completed run on the Clostridium leptum decarboxylase CLOLEP_01503 and do not re-derive it:
  that the only residue the structural literature names as a substrate-selection determinant in the carboxypolyamine
  decarboxylases is wild type across the family and cannot discriminate carboxyspermidine from carboxynorspermidine
  from carboxyaminopropylagmatine, that no structure in that family holds a carboxypolyamine, and that
  in Clostridium the assignment ultimately rested on amine supply plus the measured preference of the
  partner enzyme rather than on any pocket feature. Single analysis only. Begin with the deletion result,
  because an increase is more informative than a loss: state what else C8J_0166 loss changed, whether
  the strain still made spermidine and by what route it could have, whether the gene lies in an operon
  whose polarity the deletion could have altered, whether 81116 and NCTC 11168 carry the same complement
  of polyamine genes, and what hypotheses an increase is compatible with, including the possibility that
  the gene is not in the spermidine route at all or that its loss relieves consumption of a shared precursor.
  Then establish the amine supply in NCTC 11168 as was done for Clostridium: name the accessions for arginine
  decarboxylase, agmatinase or aminopropylagmatine ureohydrolase, ornithine decarboxylase and the diaminobutyrate
  route, and say which amines the cell can actually make, since an amine the organism cannot supply is
  not a candidate substrate however well it fits. State what the partner decarboxylase in this genome
  is, whether it has been assayed, and what is known about the native product of the C. jejuni enzyme,
  bearing in mind the published finding that the carboxynorspermidine decarboxylase orthologue of this
  organism makes spermidine rather than norspermidine in vivo. Finally say whether the aspartate-semialdehyde-dependent
  condensation can be assigned to Q0PBW7 at all on the evidence available, and with what substrate; if
  the cofactor and reaction class can be constrained while the substrate cannot, report that split explicitly,
  as the Clostridium analysis did. Do not infer the substrate from the family name or from the operon,
  and do not recommend replacing the existing UNDECIDED action unless the evidence supports a specific
  activity for this protein.'
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
**Generated:** 2026-11-26T14:31:25.542616

1. PMID:22025614
2. PMID:29190068
3. PMID:19196710
4. PMID:36283333
5. PMID:20534592