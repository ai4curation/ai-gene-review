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

- **Organism code:** PSEPK
- **Taxon:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440) (NCBITaxon:160488)
- **Gene directory:** ahpC
- **Gene symbol:** ahpC
- **UniProt accession:** Q88K52

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008379
- **Source file:** genes/PSEPK/ahpC/ahpC-ai-review.yaml
- **Source selector:** existing_annotations[5].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

ahpC has thioredoxin peroxidase activity (GO:0008379).

## Term and Decision Context

- Term: thioredoxin peroxidase activity (GO:0008379)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- PMID:12483614
- file:PSEPK/ahpC/ahpC-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0008379
  label: thioredoxin peroxidase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **ahpC directly has the stated function**. Automated
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
**Generated:** 2026-06-24T05:08:40.429747

1. hishinuma2008oxyrisinvolved pages 1-2
2. bojanovic2017globaltranscriptionalresponses pages 10-11
3. wong2017ahpcofthe pages 11-12
4. parsonage2010broadspecificityahpclike pages 2-3
5. fukumori2001molecularcloningand pages 4-6
6. zhang2019molecularmechanismsof pages 4-5
7. fukumori2001molecularcloningand pages 1-3
8. kim2014oxidativestressresponse pages 5-6
9. yang2025insectperoxiredoxinsa pages 2-4
10. rhee2016overviewonperoxiredoxin pages 1-2
11. ellis1997rolesforthe pages 4-5
12. ellis1997rolesforthe pages 1-2
13. fukumori2001molecularcloningand pages 6-8
14. ellis1997rolesforthe pages 8-8
15. poole2000ahpfandother pages 3-4
16. poole2000ahpfandother pages 4-5
17. poole2000ahpfandother pages 1-2
18. poole2000ahpfandother pages 2-3
19. zhang2019molecularmechanismsof pages 5-7
20. broden2016insightsintothe pages 12-16
21. 5
22. https://doi.org/10.2323/jgam.47.269,
23. https://doi.org/10.1007/s00253-014-5883-4,
24. https://doi.org/10.3390/insects16070678,
25. https://doi.org/10.14348/molcells.2016.2368,
26. https://doi.org/10.1128/aem.03236-16,
27. https://doi.org/10.1111/j.1574-6968.2008.01374.x,
28. https://doi.org/10.1021/bi9713658,
29. https://doi.org/10.1046/j.1432-1327.2000.01704.x,
30. https://doi.org/10.1038/s41598-017-05354-5,
31. https://doi.org/10.1073/pnas.0910057107,
32. https://doi.org/10.3389/fmicb.2019.01483,
33. https://doi.org/10.1089/ars.2011.4404,
34. https://doi.org/10.1128/jb.00679-15,