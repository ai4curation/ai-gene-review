# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** BACTN
- **Taxon:** Bacteroides thetaiotaomicron VPI-5482 (NCBITaxon:226186)
- **Gene directory:** BT_4612
- **Gene symbol:** BT_4612
- **UniProt accession:** Q89YW9

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kgap-bt4612-amine-supply
- **Source file:** genes/BACTN/BT_4612/BT_4612-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Whether the physiological amine substrate of BT_4612 can be constrained is the question, and two completed runs in this campaign have already mapped where the evidence for such a question does and does not come from. Carry forward and do not re-derive: from the Clostridium leptum decarboxylase run, that the only residue the structural literature names as a substrate-selection determinant in this superfamily is effectively invariant and cannot discriminate carboxyspermidine from carboxynorspermidine from carboxyaminopropylagmatine, and that no structure in the family holds a carboxypolyamine; from the Campylobacter jejuni dehydrogenase run, that the cofactor site is richly testable while no amine-contacting position is testable at all, and that a partner decarboxylase which accepts both candidate substrates in vitro transmits no constraint upstream. Nothing in this run should attempt to read the substrate off pocket residues. Already recorded for BT_4612 itself: PANTHER PTHR43796:SF2 membership, the NAD(P)-binding and C-terminal catalytic domains of the CASDH/CANSDH/CAPADH group, a provisional CASDH assignment in a pathway diagram, and that this subfamily also contains CAPADH enzymes. Single analysis only. Work the question the way the Clostridium case was eventually settled, through amine supply and the measured behaviour of the pathway in this organism. Establish from the Bacteroides thetaiotaomicron genome, naming accessions, which amines the cell can make: arginine decarboxylase, agmatinase or aminopropylagmatine ureohydrolase, ornithine decarboxylase, and the diaminobutyrate aminotransferase and decarboxylase pair that supplies 1,3-diaminopropane, and say which candidate substrates that supply permits and which it excludes. Then set that against what has been measured in this organism rather than inferred: state what the published deletion of the carboxyspermidine decarboxylase gene did to spermidine and to decarboxylase activity, whether any upstream dehydrogenase in this organism has been deleted or assayed, and whether BT_4612 is the only candidate dehydrogenase in the genome or one of several, naming the others. A second candidate would change the question, so establish the count before interpreting anything. State also whether the cofactor can be assigned as NAD or NADP from the sequence, and on what basis, keeping that claim separate from the substrate claim. Conclude with what can and cannot be asserted for this protein. If the substrate is constrained only by exclusion of amines the organism cannot synthesise, say exactly that and no more; if it is not constrained at all, say that. Do not infer the substrate from the pathway diagram or from the subfamily name, and do not recommend a specific-activity annotation that names a compound the analysis cannot reach.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Whether the physiological amine substrate of BT_4612 can be constrained is the question,
  and two completed runs in this campaign have already mapped where the evidence for such a question does
  and does not come from. Carry forward and do not re-derive: from the Clostridium leptum decarboxylase
  run, that the only residue the structural literature names as a substrate-selection determinant in this
  superfamily is effectively invariant and cannot discriminate carboxyspermidine from carboxynorspermidine
  from carboxyaminopropylagmatine, and that no structure in the family holds a carboxypolyamine; from
  the Campylobacter jejuni dehydrogenase run, that the cofactor site is richly testable while no amine-contacting
  position is testable at all, and that a partner decarboxylase which accepts both candidate substrates
  in vitro transmits no constraint upstream. Nothing in this run should attempt to read the substrate
  off pocket residues. Already recorded for BT_4612 itself: PANTHER PTHR43796:SF2 membership, the NAD(P)-binding
  and C-terminal catalytic domains of the CASDH/CANSDH/CAPADH group, a provisional CASDH assignment in
  a pathway diagram, and that this subfamily also contains CAPADH enzymes. Single analysis only. Work
  the question the way the Clostridium case was eventually settled, through amine supply and the measured
  behaviour of the pathway in this organism. Establish from the Bacteroides thetaiotaomicron genome, naming
  accessions, which amines the cell can make: arginine decarboxylase, agmatinase or aminopropylagmatine
  ureohydrolase, ornithine decarboxylase, and the diaminobutyrate aminotransferase and decarboxylase pair
  that supplies 1,3-diaminopropane, and say which candidate substrates that supply permits and which it
  excludes. Then set that against what has been measured in this organism rather than inferred: state
  what the published deletion of the carboxyspermidine decarboxylase gene did to spermidine and to decarboxylase
  activity, whether any upstream dehydrogenase in this organism has been deleted or assayed, and whether
  BT_4612 is the only candidate dehydrogenase in the genome or one of several, naming the others. A second
  candidate would change the question, so establish the count before interpreting anything. State also
  whether the cofactor can be assigned as NAD or NADP from the sequence, and on what basis, keeping that
  claim separate from the substrate claim. Conclude with what can and cannot be asserted for this protein.
  If the substrate is constrained only by exclusion of amines the organism cannot synthesise, say exactly
  that and no more; if it is not constrained at all, say that. Do not infer the substrate from the pathway
  diagram or from the subfamily name, and do not recommend a specific-activity annotation that names a
  compound the analysis cannot reach.'
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
**Generated:** 2026-11-26T16:24:54.239429

1. PMID:37437886
2. PMID:42754158
3. PMID:43093060
4. PMID:27118128
5. PMID:1955861
6. PMID:37878710
7. PMID:10801923
8. PMID:15983049
9. PMID:36362306
10. PMID:22025614
11. PMID:41298497