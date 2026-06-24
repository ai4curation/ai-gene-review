# Citations for Research Query

**Query:** # AIGR TreeGrafter Function-Inference Stress Test

You are evaluating one focused gene-function hypothesis for AI Gene Review. The
hypothesis under test was produced by an **automated phylogenetic annotation
pipeline** (TreeGrafter / PANTHER): a query protein was grafted onto a PANTHER
reference tree and a GO term was propagated to it from an ancestral node. Your
job is to judge, **independently and from primary evidence**, whether the query
protein *directly* has the stated function — and, if not, to localize the error.

This is not a general gene overview. Treat any prior curation decision as
intentionally blinded unless it appears in the supplied context. Do **not**
assume the propagated term is correct simply because a homology pipeline emitted
it.

## Target Gene

- **Organism code:** NICAT
- **Taxon:** Nicotiana attenuata (NCBITaxon:49451)
- **Gene directory:** NaUGT1_candidate_UGT85A2_0
- **Gene symbol:** NaUGT1_candidate_UGT85A2_0
- **UniProt accession:** A0A2H4GSI3

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0080043
- **Source file:** genes/NICAT/NaUGT1_candidate_UGT85A2_0/NaUGT1_candidate_UGT85A2_0-ai-review.yaml
- **Source selector:** existing_annotations[3].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

NaUGT1_candidate_UGT85A2_0 has quercetin 3-O-glucosyltransferase activity (GO:0080043).

## Term and Decision Context

- Term: quercetin 3-O-glucosyltransferase activity (GO:0080043)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118

## Source Context YAML

```yaml
term:
  id: GO:0080043
  label: quercetin 3-O-glucosyltransferase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **NaUGT1_candidate_UGT85A2_0 directly has the stated function**. Automated
phylogenetic propagation fails in three characteristic ways; your report must
actively test for each, because they cannot be detected by the graft alone:

1. **Granularity / family-vs-subfamily.** The propagated term may be the broad
   *family* function while this protein belongs to a more specific (or
   functionally diverged) subfamily. Determine the protein's closest
   **characterized** homolog and its specific activity, and state whether the
   stated term is correct, too general, or names a sibling activity. (Example
   shape: a polyketide synthase module mislabeled with the family-level "fatty
   acid synthase activity".)
2. **Pseudo-enzyme / loss of activity.** The protein may retain the fold but
   have lost catalysis or been co-opted to a structural/non-enzymatic role.
   Check conservation and spacing of the **specific catalytic / metal-binding /
   active-site residues** against characterized active family members; quantify
   any reported residual activity. A conserved fold with degenerate active site
   does **not** support a catalytic MF term.
3. **Within-superfamily mis-placement.** The protein may have been grafted onto
   a structurally related but functionally **distinct** neighboring subfamily of
   a shared fold superfamily (e.g. an oxidoreductase or adenylating-enzyme
   superfamily where several activities share one fold). Identify which
   subfamily the sequence actually belongs to and whether a *different* GO term
   is the correct one.

Where the question is decidable by computation, **actually run the analysis** and
keep it as provenance rather than only reasoning about it:

- **Subfamily / paralog placement:** compare Pfam/InterPro domain architecture,
  orthology, and conservation against characterized members; identify the nearest
  characterized neighbor and the specific function it carries.
- **Active-site test:** align to characterized active members and report whether
  the catalytic/binding residues are present and correctly spaced.
- **Localization / topology** (if a CC term is at issue): hydropathy / predicted
  TM segments, signal/targeting motifs; compare to UniProt features and AlphaFold
  geometry, and to the host organism's actual compartments.

Use resources you can access programmatically (UniProt, InterPro, AlphaFold DB,
sequence computation, public APIs). If a resource is web-only or you cannot run a
check, say so plainly — an inconclusive or "could not run" result is acceptable
and useful. **Never fabricate a result.** Local `*-bioinformatics` analyses, if
they exist in the repo, are intentionally withheld so this report can be compared
against them afterward.

## Required Output

### Executive Judgment

Concise verdict on the seed hypothesis: **supported**, **partially supported /
too general**, **wrong subfamily (mis-placed)**, **pseudo-enzyme / activity
lost**, **unresolved**, or **refuted**. Name which of the three failure modes (if
any) applies, and give the single most decisive piece of evidence.

### Independent Family/Function Assignment

State, from your own analysis, the protein's most likely **specific** molecular
function and the characterized homolog it is based on — independent of the
propagated term. Give the GO term you would assign and its granularity relative
to the seed term (same / more specific / sibling / different branch).

### Evidence Matrix

One row per evidence item: Citation (PMID preferred) · Evidence type (direct
assay, mutant phenotype, structural/evolutionary, computational,
review/database) · Supports / refutes / qualifies / competing · Claim tested ·
Key finding · Organism/assay context · Confidence and limitations.

### Active-Site / Placement Analysis

Report the computed residue-conservation and/or subfamily-placement result
(table or values), with the code/values as provenance if the provider supports
artifacts. State explicitly whether catalytic residues are intact.

### GO Curation Implications

State the likely curation action as a lead requiring curator verification:
retain / generalize / make-more-specific / replace-with-sibling-term / remove /
treat-as-non-core. Avoid "protein binding" as a final recommendation.

### Conflicts, Knowledge Gaps, Discriminating Tests

Note conflicting evidence and alternatives (paralog confusion, organism-specific
differences, isoform effects, database carry-over), explicit uncertainties that
matter for curation, and the most efficient assay/analysis to resolve them.

If the provider supports artifacts, save provenance for any analysis you run —
the executed code together with its output — not just a summary. Do not
synthesize a figure implying an analysis you did not run.

**Provider:** falcon
**Generated:** 2026-06-24T05:03:20.333798

1. song2018attractivebuttoxic pages 4-7
2. zhang2025singlecelltranscriptomicsand pages 12-14
3. yamada2019aglucosyltransferasespecific pages 4-7
4. roy2016glycosylationisa pages 4-5
5. yin2010arabidopsisflavonoidglycosylation pages 9-13
6. selmar2010biosynthesisofcyanogenic pages 22-25
7. rehman2018comparativegenomicand pages 13-13
8. offen2006structureofa pages 6-7
9. offen2006structureofa pages 2-4
10. offen2006structureofa pages 4-6
11. louveau2019thesweetside pages 6-7
12. louveau2019thesweetside pages 7-9
13. louveau2019thesweetside pages 5-6
14. muller2024physiologicalandphytochemical pages 86-88
15. 3
16. https://doi.org/10.3389/fpls.2016.00735,
17. https://doi.org/10.5282/edoc.13146,
18. https://doi.org/10.1016/j.molp.2018.09.001,
19. https://doi.org/10.1186/s12915-025-02297-6,
20. https://doi.org/10.1038/s41598-018-19535-3,
21. https://doi.org/10.1080/09168451.2018.1524706,
22. https://doi.org/10.1002/9781444320503.ch3,
23. https://doi.org/10.3390/biology11030441,
24. https://doi.org/10.1038/sj.emboj.7600970,
25. https://doi.org/10.1101/cshperspect.a034744,