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

- **Organism code:** ECOLX
- **Taxon:** Escherichia coli (NCBITaxon:562)
- **Gene directory:** mcr-1
- **Gene symbol:** mcr-1
- **UniProt accession:** A0A0R6L508

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0016776
- **Source file:** genes/ECOLX/mcr-1/mcr-1-ai-review.yaml
- **Source selector:** existing_annotations[5].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

mcr-1 has phosphotransferase activity, phosphate group as acceptor (GO:0016776).

## Term and Decision Context

- Term: phosphotransferase activity, phosphate group as acceptor (GO:0016776)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- PMID:29079699

## Source Context YAML

```yaml
term:
  id: GO:0016776
  label: phosphotransferase activity, phosphate group as acceptor
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **mcr-1 directly has the stated function**. Automated
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
**Generated:** 2026-06-24T04:44:29.552187

1. anandan2017structureofa pages 1-2
2. schumann2024themultifacetedroles pages 4-6
3. anderson2020theescherichiacoli pages 16-18
4. sun2021deepmutationalscanning pages 5-7
5. thai2023phosphoethanolaminetransferasesas pages 16-18
6. sun2021deepmutationalscanning pages 10-11
7. zinkle2025mechanisticbasisof pages 3-4
8. zinkle2025mechanisticbasisof pages 7-8
9. zinkle2025mechanisticbasisof pages 1-2
10. sun2021deepmutationalscanning pages 3-5
11. anandan2020structureandfunction pages 14-17
12. samantha2020lipidaphosphoethanolamine pages 8-12
13. samantha2020lipidaphosphoethanolamine pages 5-8
14. sun2021deepmutationalscanning pages 11-13
15. thai2023phosphoethanolaminetransferasesas pages 14-16
16. thai2023phosphoethanolaminetransferasesas pages 12-14
17. thai2023phosphoethanolaminetransferasesas pages 7-9
18. 5
19. https://doi.org/10.1038/s41467-025-65515-3,
20. https://doi.org/10.1128/mbio.02776-21,
21. https://doi.org/10.1111/nyas.14244,
22. https://doi.org/10.1016/j.jmb.2020.04.022,
23. https://doi.org/10.1073/pnas.1612927114,
24. https://doi.org/10.3390/antibiotics12091382,
25. https://doi.org/10.1128/mmbr.00193-23,
26. https://doi.org/10.1074/jbc.ra119.011668,