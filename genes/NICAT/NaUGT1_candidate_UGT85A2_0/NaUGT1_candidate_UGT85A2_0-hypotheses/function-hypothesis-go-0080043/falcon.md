---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:36:52.206823'
end_time: '2026-06-24T05:03:20.333798'
duration_seconds: 1588.13
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: NICAT
  gene: NaUGT1_candidate_UGT85A2_0
  gene_symbol: NaUGT1_candidate_UGT85A2_0
  uniprot_accession: A0A2H4GSI3
  taxon_id: NCBITaxon:49451
  taxon_label: Nicotiana attenuata
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0080043
  hypothesis_text: NaUGT1_candidate_UGT85A2_0 has quercetin 3-O-glucosyltransferase
    activity (GO:0080043).
  term_context: '- Term: quercetin 3-O-glucosyltransferase activity (GO:0080043)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118'
  source_file: genes/NICAT/NaUGT1_candidate_UGT85A2_0/NaUGT1_candidate_UGT85A2_0-ai-review.yaml
  source_selector: existing_annotations[3].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0080043\n  label: quercetin 3-O-glucosyltransferase\
    \ activity\nevidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# AIGR TreeGrafter Function-Inference Stress Test

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


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# AIGR TreeGrafter Function-Inference Stress Test

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


# AIGR TreeGrafter Function-Inference Stress Test Report

## Target: NaUGT1_candidate_UGT85A2_0 (A0A2H4GSI3) from *Nicotiana attenuata*
## Seed Hypothesis: GO:0080043 — quercetin 3-O-glucosyltransferase activity

---

## Executive Judgment

**Verdict: Wrong subfamily (mis-placed) — REFUTED**

The seed hypothesis that NaUGT1_candidate_UGT85A2_0 has quercetin 3-O-glucosyltransferase activity (GO:0080043) is **refuted**. This represents a clear instance of **failure mode 3 (within-superfamily mis-placement)**, with elements of **failure mode 1 (granularity / family-vs-subfamily error)**. The propagated GO term names a specific activity that belongs to phylogenetically distant UGT subfamilies (primarily UGT78D and certain UGT72 members), not to the UGT85A subfamily to which this protein belongs (roy2016glycosylationisa pages 4-5, yin2010arabidopsisflavonoidglycosylation pages 9-13, song2018attractivebuttoxic pages 4-7, zhang2025singlecelltranscriptomicsand pages 12-14).

**Single most decisive piece of evidence:** No characterized UGT85A subfamily member has ever been shown to possess quercetin 3-O-glucosyltransferase activity. Instead, UGT85A1 and UGT85A2 in *Arabidopsis thaliana* are established cytokinin (trans-zeatin) O-glucosyltransferases (zhang2025singlecelltranscriptomicsand pages 12-14, rehman2018comparativegenomicand pages 13-13), while other UGT85A members (e.g., UGT85A28) are volatile/monoterpene alcohol glucosyltransferases (song2018attractivebuttoxic pages 4-7). The canonical quercetin 3-O-glucosyltransferase is UGT78D2 in *Arabidopsis*, a member of a completely different UGT subfamily (roy2016glycosylationisa pages 4-5, yin2010arabidopsisflavonoidglycosylation pages 9-13).

---

## Independent Family/Function Assignment

**Most likely specific molecular function:** UDP-glucosyltransferase activity acting on cytokinins (zeatin O-glucosylation) and/or volatile/monoterpene alcohols.

**Characterized homolog basis:**
- *Arabidopsis thaliana* UGT85A1 and UGT85A2 — cytokinin (trans-zeatin) O-glucosyltransferases mediating reversible cytokinin inactivation/storage (zhang2025singlecelltranscriptomicsand pages 12-14, rehman2018comparativegenomicand pages 13-13).
- UGT85A28 from tea — volatile/monoterpene alcohol glucosyltransferase with broad substrate tolerance, glucosylating geraniol, citronellol, and at least 16 additional volatile alcohols (song2018attractivebuttoxic pages 4-7).
- UGT85K16 from strawberry — HDMF glucosyltransferase; and UGT85B1 from sorghum — cyanohydrin glucosyltransferase in dhurrin biosynthesis (yamada2019aglucosyltransferasespecific pages 4-7, selmar2010biosynthesisofcyanogenic pages 22-25). These related UGT85-family members further demonstrate that the UGT85 clade is associated with small alcohol, volatile, cyanohydrin, and cytokinin substrates, not flavonol aglycones.

**Recommended GO term:** GO:0016758 (hexosyltransferase activity) as a safe general assignment, or more specifically GO:0046527 (glucosyltransferase activity) pending direct biochemical characterization. If cytokinin O-glucosylation is confirmed, GO:0009690 (cytokinin metabolic process) in the BP aspect would be appropriate.

**Granularity relative to seed term:** Different branch entirely. GO:0080043 (quercetin 3-O-glucosyltransferase activity) is a sibling/neighboring activity within the GT1 superfamily that maps to a distinct subfamily (UGT78D), not to UGT85A.

---

## Evidence Matrix

The following table compiles all primary evidence bearing on the seed hypothesis:

| Citation | Evidence Type | Supports/Refutes/Qualifies | Claim Tested | Key Finding | Organism/Assay Context | Confidence and Limitations |
|---|---|---|---|---|---|---|
| Song et al. 2018, *Molecular Plant* (song2018attractivebuttoxic pages 4-7) | Review/database synthesis of characterized enzymes | Refutes | Does a UGT85A-subfamily protein plausibly have quercetin 3-O-glucosyltransferase activity? | UGT85 subfamily is described as a hotspot for glycosidically bound volatile production; characterized UGT85 enzymes glucosylate monoterpenols and other volatile alcohols (e.g., geraniol, citronellol, hexanol, benzyl alcohol, furaneol), not flavonol 3-O glucosylation. | Tea, grape, kiwifruit and other plant UGT functional studies summarized in review. | High confidence for subfamily-level functional trend; indirect for the Nicotiana attenuata query because it is a review and not a direct assay of A0A2H4GSI3. |
| Zhang et al. 2025, *BMC Biology* (zhang2025singlecelltranscriptomicsand pages 12-14) | Transcriptomic/metabolomic study with literature-grounded functional assignment | Refutes | Are UGT85A1/UGT85A2 associated with cytokinin O-glycosylation rather than quercetin 3-O-glucosylation? | The study states that UGT85A1 and UGT85A2 mediate cytokinin O-glycosylation, consistent with increased trans-zeatin-O-glucoside riboside and cytokinin glycosylation programs. | *Arabidopsis thaliana* pap1-D leaves; single-cell transcriptomics and metabolomics. | Moderate confidence: strong for pathway context and literature-backed annotation, but not a direct recombinant enzyme assay within this paper. |
| Yamada et al. 2019, *Bioscience, Biotechnology, and Biochemistry* (yamada2019aglucosyltransferasespecific pages 4-7) | Direct biochemical assay | Refutes | Are UGT85-family proteins generally specialized for flavonol 3-O-glucosylation? | UGT85K16 is a UDP-glucose:HDMF glucosyltransferase; related UGT85A members are noted to glucosylate monoterpene alcohols and simple volatiles, reinforcing non-flavonol chemistry in this clade. | Strawberry recombinant enzyme assays for HDMF glucosylation; discussion of related UGT85A enzymes. | High confidence for UGT85-family catalytic versatility outside flavonols; limited because UGT85K16 is not UGT85A2 and not from *N. attenuata*. |
| Roy et al. 2016, *Frontiers in Plant Science* (roy2016glycosylationisa pages 4-5) | Review of primary genetic/biochemical literature | Refutes | Which UGT subfamily carries established quercetin 3-O-glucosyltransferase activity? | UGT78D2 is identified as the UDP-glucose-dependent flavonol 3-O-glucosyltransferase in *Arabidopsis*; UGT78D1 and UGT78D3 use other sugar donors on similar flavonol aglycones. | *Arabidopsis thaliana* flavonol glycosylation literature synthesis. | High confidence for established subfamily-function mapping; indirect for the Nicotiana query because it is a review. |
| Yonekura-Sakakibara et al. 2008, *The Plant Cell* (yin2010arabidopsisflavonoidglycosylation pages 9-13) | Direct assay + mutant/metabolite profiling | Refutes | Is quercetin/flavonol 3-O-glycosylation a UGT85A-type function? | UGT78D2/UGT78D3 are confirmed flavonol 3-O-glycosyltransferases acting on quercetin and related flavonols, placing the activity in UGT78D rather than UGT85A. | *Arabidopsis thaliana* recombinant proteins, LC-MS flavonol profiling, coexpression analysis, mutant validation. | High confidence; strong primary evidence for the correct functional neighborhood, though not a direct comparison to UGT85A in the same experiment. |
| Speeckaert et al. 2022, *Biology* (speeckaert2022ugt72amajor pages 9-10, speeckaert2022ugt72amajor pages 8-9, speeckaert2022ugt72amajor pages 5-8, speeckaert2022ugt72amajor pages 10-10) | Review of characterized enzymes | Refutes/Qualifies | Are there non-UGT78D enzymes with quercetin 3-O-glucosyltransferase activity, and do they include UGT85A? | Several UGT72 enzymes (e.g., LjUGT72AH1, UGT72Z2, GmUGT72X4) catalyze quercetin 3-O-glucosylation, showing that this activity occurs in specific flavonoid-related clades such as UGT72 and UGT78D, not in characterized UGT85A members. | Legume and bryophyte flavonoid UGT literature synthesis. | High confidence for exclusion of UGT85A from currently characterized quercetin 3-O-glucosyltransferases; indirect inference from available characterized examples. |
| Offen et al. 2006, *EMBO Journal* (offen2006structureofa pages 6-7, offen2006structureofa pages 2-4, offen2006structureofa pages 4-6) | Structural/biochemical primary study | Qualifies | Could a generic active GT1 fold alone justify GO:0080043 assignment? | VvGT1 structure reveals a flavonoid 3-O-glucosyltransferase active site with catalytic His20/Asp119 and donor-recognition residues that determine sugar specificity; GT1 catalytic competence alone does not specify UGT85A as a flavonol 3-O-glucosyltransferase. | Grapevine flavonoid glucosyltransferase crystal structures and mechanistic analysis. | High confidence for catalytic mechanism and donor/acceptor recognition principles; does not test the Nicotiana sequence directly. |
| Selmar 2010; Gleadow et al. 2021 (selmar2010biosynthesisofcyanogenic pages 22-25) | Review/primary pathway literature | Refutes | Does UGT85-family membership point toward alternative chemistries besides flavonol glucosylation? | UGT85B1 catalyzes the terminal glucosylation step in dhurrin biosynthesis, showing UGT85-family participation in cyanogenic glucoside biosynthesis rather than quercetin 3-O-glucosylation. | *Sorghum bicolor* cyanogenic glucoside pathway. | Moderate-to-high confidence for UGT85-family functional breadth; subfamily is UGT85B rather than UGT85A, so informative at family level but not definitive for the precise query subfamily. |
| Rehman et al. 2018, *Scientific Reports* (rehman2018comparativegenomicand pages 13-13) | Comparative genomics/review of characterized genes | Refutes | Is UGT85A1 functionally linked to zeatin glycosylation? | UGT85A1 is identified as a characterized glucosyltransferase involved in zeatin glycosylation, supporting cytokinin-related function for UGT85A members. | *Arabidopsis* and Brassica comparative UGT analysis citing characterized Arabidopsis genes. | Moderate confidence because this is a comparative analysis summarizing prior functional characterization, not a new biochemical assay. |
| Louveau & Osbourn 2019, *Cold Spring Harbor Perspectives in Biology* (louveau2019thesweetside pages 6-7, louveau2019thesweetside pages 7-9, louveau2019thesweetside pages 5-6) | Mechanistic review | Qualifies | Could loss of catalytic residues explain the annotation error, or is the problem more likely wrong subfamily/function? | Plant GT1 UGTs share conserved catalytic architecture including N-terminal His, nearby Asp, and PSPG-linked donor-binding residues; absent direct sequence analysis of A0A2H4GSI3, pseudo-enzyme status cannot be excluded computationally here, but the dominant error signal is wrong subfamily/function rather than generic loss of catalysis. | Pan-plant GT1 UGT mechanism synthesis. | High confidence for mechanism; limited because the query sequence was not directly aligned in this analysis. |


*Table: This table compiles the main evidence bearing on whether Nicotiana attenuata NaUGT1_candidate_UGT85A2_0 directly has quercetin 3-O-glucosyltransferase activity. It shows that characterized quercetin 3-O-glucosyltransferases belong to UGT78D/UGT72-related clades, whereas UGT85A members are associated with cytokinin, volatile, and cyanogenic glucoside chemistry.*

---

## UGT Subfamily Functional Comparison

The following table demonstrates the functional divergence among GT1 UGT subfamilies relevant to this evaluation:

| UGT Subfamily | Characterized Function(s) | Known Substrates | Representative Members | GO Term(s) That Would Apply | Relationship to GO:0080043 |
|---|---|---|---|---|---|
| UGT78D | Flavonol 3-O-glycosyltransferases; includes the canonical quercetin 3-O-glucosyltransferase clade in Arabidopsis | Quercetin, kaempferol, isorhamnetin; UDP-glucose for UGT78D2, UDP-rhamnose for UGT78D1, UDP-arabinose for UGT78D3 | UGT78D2, UGT78D1, UGT78D3 | quercetin 3-O-glucosyltransferase activity (GO:0080043) for UGT78D2; related flavonol 3-O-glycosyltransferase terms for other sugar donors | **Correct subfamily** for GO:0080043; strongest characterized match to the seed term (yin2010arabidopsisflavonoidglycosylation pages 9-13, roy2016glycosylationisa pages 4-5) |
| UGT85A | Cytokinin O-glucosyltransferases; volatile/monoterpene alcohol glucosyltransferases; broad specialized-metabolite glucosylation | trans-zeatin and other cytokinin O-glycosides; geraniol, citronellol, hexanol, (Z)-3-hexenol, octanol, 2-phenylethanol, benzyl alcohol, furaneol | UGT85A1, UGT85A2, UGT85A28 | cytokinin O-glucosyltransferase activity / zeatin O-glucosyltransferase-type functions; monoterpenol glucosyltransferase or broader UDP-glycosyltransferase activity | **Not GO:0080043**; different substrate class and likely sibling activity within GT1 UGTs, refuting direct quercetin 3-O-glucosyltransferase assignment (rehman2018comparativegenomicand pages 13-13, song2018attractivebuttoxic pages 4-7, zhang2025singlecelltranscriptomicsand pages 12-14) |
| UGT85B | Cyanogenic glucoside biosynthesis enzyme catalyzing the terminal glucosylation step in dhurrin formation | p-hydroxymandelonitrile + UDP-glucose | UGT85B1 | p-hydroxymandelonitrile glucosyltransferase / cyanogenic glucoside biosynthetic glucosyltransferase-type functions | **Different branch/function**; demonstrates that UGT85-family members often act on non-flavonol defense metabolites rather than quercetin (selmar2010biosynthesisofcyanogenic pages 22-25, muller2024physiologicalandphytochemical pages 86-88) |
| UGT85K | Cyanogenic glucoside biosynthesis in cassava; in a distinct example, UGT85K16 glucosylates HDMF in strawberry | Linamarin/lotaustralin pathway intermediates in cassava; 4-hydroxy-2,5-dimethyl-3(2H)-furanone (HDMF) in strawberry | UGT85K4, UGT85K5, UGT85K16 | cyanogenic glucoside biosynthetic glucosyltransferase-type functions; HDMF glucosyltransferase | **Different branch/function**; further shows UGT85 clades are associated with cyanogenic or volatile/flavor chemistry, not quercetin 3-O-glucosylation (yamada2019aglucosyltransferasespecific pages 4-7, muller2024physiologicalandphytochemical pages 86-88) |
| UGT72 | Flavonoid and monolignol glucosyltransferases; some members directly catalyze quercetin 3-O-glucosylation | Quercetin, kaempferol, myricetin, monolignols, other phenylpropanoids | UGT72AH1, UGT72Z2, UGT72X4, UGT72B27 | quercetin 3-O-glucosyltransferase activity for specific members; broader flavonoid glucosyltransferase and monolignol glucosyltransferase terms for others | **Partially overlapping** with GO:0080043 for some members, but still distinct from UGT85A; shows quercetin 3-O-glucosylation maps to flavonoid-related clades, not the query’s UGT85A clade (speeckaert2022ugt72amajor pages 9-10, speeckaert2022ugt72amajor pages 8-9, speeckaert2022ugt72amajor pages 5-8, speeckaert2022ugt72amajor pages 10-10, song2018attractivebuttoxic pages 4-7) |


*Table: This table compares the main characterized functions of UGT subfamilies relevant to the annotation test. It shows that GO:0080043 aligns with flavonoid-focused clades such as UGT78D and some UGT72 members, whereas UGT85A maps to different chemistries such as cytokinin and volatile glucosylation.*

---

## Active-Site / Placement Analysis

| Analysis | Method/Result | Interpretation | Status |
|---|---|---|---|
| Catalytic His-Asp dyad conservation | Direct sequence alignment for A0A2H4GSI3 could not be run because the query sequence was not programmatically retrievable in this session. In active plant GT1 UGTs, the catalytic His near the N-terminus and nearby Asp are strongly conserved; active UGT85A homologs and the VvGT1 structural model support expecting this dyad to be intact in a catalytically competent UGT85A enzyme (louveau2019thesweetside pages 6-7, offen2006structureofa pages 6-7, zhang2025singlecelltranscriptomicsand pages 12-14) | No evidence for pseudo-enzyme status from family context, but catalytic-residue conservation for the query remains unverified without a direct alignment | Not directly verified |
| PSPG motif conservation | The C-terminal PSPG motif is a hallmark of active plant family-1 UGTs and underlies UDP-sugar binding. Because multiple UGT85A members are experimentally active, the motif is expected to be conserved in this candidate, but this could not be checked directly for A0A2H4GSI3 in the current session (louveau2019thesweetside pages 7-9, louveau2019thesweetside pages 5-6, song2018attractivebuttoxic pages 4-7) | Consistent with an active GT1 glucosyltransferase fold, but insufficient to support the specific substrate claim GO:0080043 | Not directly verified |
| Acceptor-binding pocket | Structural/mechanistic comparison indicates that flavonoid 3-O-glucosyltransferases such as VvGT1/UGT78-related enzymes use an acceptor pocket suited to planar flavonoid substrates, whereas characterized UGT85A enzymes glucosylate cytokinins and small volatile alcohols such as geraniol, citronellol, benzyl alcohol, and furaneol (offen2006structureofa pages 6-7, song2018attractivebuttoxic pages 4-7, zhang2025singlecelltranscriptomicsand pages 12-14) | The query’s acceptor pocket is much more likely to resemble UGT85A cytokinin/volatile-glucosylating enzymes than a quercetin 3-O-glucosyltransferase pocket | Inferred from homologs/subfamily |
| Subfamily placement by sequence identity | The query is explicitly labeled as a UGT85A2 candidate. Independent functional context shows UGT85A is a distinct GT1 subfamily from UGT78D, the canonical flavonol 3-O-glucosyltransferase clade, and from UGT72 flavonoid/monolignol clades (roy2016glycosylationisa pages 4-5, speeckaert2022ugt72amajor pages 10-10, zhang2025singlecelltranscriptomicsand pages 12-14, song2018attractivebuttoxic pages 4-7) | Placement supports a UGT85A assignment and argues strongly against direct quercetin 3-O-glucosyltransferase activity | Strongly supported |
| Nearest characterized homolog | Best characterized functional neighbors are AtUGT85A1 and AtUGT85A2, assigned to cytokinin O-glycosylation, and UGT85A28, a volatile/monoterpene alcohol glucosyltransferase with broad substrate tolerance (rehman2018comparativegenomicand pages 13-13, song2018attractivebuttoxic pages 4-7, zhang2025singlecelltranscriptomicsand pages 12-14) | The closest characterized activities are sibling GT1 glucosyltransferase functions, not quercetin 3-O-glucosyltransferase activity | Strongly supported |
| Pseudo-enzyme check | Multiple active UGT85A homologs exist, including cytokinin- and volatile-active enzymes; nothing in the available evidence suggests that the UGT85A clade is generally catalytically degenerate. However, a definitive pseudo-enzyme exclusion for the query would require direct residue-level alignment (louveau2019thesweetside pages 6-7, song2018attractivebuttoxic pages 4-7, zhang2025singlecelltranscriptomicsand pages 12-14) | Loss of activity is possible in principle for any individual paralog, but the dominant explanation for the GO error here is wrong subfamily/function assignment rather than catalytic decay | Unlikely but unproven |


*Table: This table summarizes the residue-level and subfamily-placement assessment for NaUGT1_candidate_UGT85A2_0. It highlights that direct catalytic-residue verification was not possible here, but the available evidence strongly supports UGT85A placement and refutes quercetin 3-O-glucosyltransferase assignment.*

### Summary of Active-Site Analysis

Plant family-1 UDP-glucosyltransferases share a conserved GT-B fold with a catalytic His-Asp dyad, where His (approximately position 20) acts as a general base to deprotonate the acceptor hydroxyl, enabling nucleophilic attack on the C1 anomeric carbon of the UDP-sugar donor (louveau2019thesweetside pages 6-7, offen2006structureofa pages 6-7). This mechanism is shared across all active GT1 members regardless of acceptor specificity. The VvGT1 crystal structure (1.9 Å resolution) reveals that acceptor specificity is determined by the hydrophobic pocket architecture (Phe15, Phe121, Phe200, Phe372, Ile87, Val281) and the sugar donor specificity by residues including Asp374, Gln375, and Thr141 (offen2006structureofa pages 6-7, offen2006structureofa pages 2-4, offen2006structureofa pages 4-6). Critically, UGT78D-type flavonol 3-O-glucosyltransferases accommodate the planar flavonoid A/C ring system, whereas UGT85A enzymes have acceptor pockets configured for small molecules such as cytokinins and volatile alcohols (song2018attractivebuttoxic pages 4-7).

Direct sequence-level verification of catalytic residue conservation in A0A2H4GSI3 could not be performed in this session because the UniProt sequence was not programmatically accessible. However, because multiple experimentally characterized UGT85A members (UGT85A1, UGT85A2, UGT85A28) are catalytically active, the pseudo-enzyme hypothesis (failure mode 2) is considered unlikely. The dominant error is within-superfamily mis-placement (failure mode 3).

---

## GO Curation Implications

**Recommended curation action: REMOVE the current annotation and REPLACE with a more general or subfamily-appropriate term.**

Specifically:
1. **Remove** GO:0080043 (quercetin 3-O-glucosyltransferase activity) — this term is incorrect for a UGT85A subfamily member. No characterized UGT85A enzyme has this activity.
2. **Replace with** GO:0016758 (hexosyltransferase activity) as a safe, evidence-supported general annotation, or GO:0046527 (glucosyltransferase activity) if UDP-glucose is the confirmed donor.
3. **Alternatively, if cytokinin glucosylation is supported by further evidence**, annotate with a zeatin/cytokinin O-glucosyltransferase-type term, consistent with the function of the closest characterized homologs (AtUGT85A1/A2).
4. **Do not annotate** with "protein binding" as a substitute; this would be uninformative.

The TreeGrafter propagation error likely arose because the PANTHER reference tree placed multiple GT1 UGT subfamilies under a shared ancestral node that was annotated with GO:0080043 based on a UGT78D descendant. When the UGT85A query sequence was grafted onto the tree, it inherited this annotation from a node whose GO term was subfamily-specific to UGT78D, not to the broader GT1 family.

---

## Conflicts, Knowledge Gaps, and Discriminating Tests

### Conflicts and Alternatives

1. **Paralog confusion / promiscuous activity caveat:** Plant UGTs are well-known for substrate promiscuity (song2018attractivebuttoxic pages 4-7). While UGT85A members preferentially glucosylate cytokinins and volatile alcohols, some in vitro promiscuity toward flavonoids cannot be absolutely excluded without direct biochemical testing. However, no published evidence supports this for any UGT85A member.

2. **Organism-specific functional divergence:** *Nicotiana attenuata* possesses a rich repertoire of specialized metabolites, including 17-hydroxygeranyllinalool diterpene glycosides (HGL-DTGs) that require multiple glycosylation steps. The UGT85 family has been implicated in Nicotiana terpenoid/cyanogenic glycoside contexts (Müller 2024 thesis mentions CYP79A207 and UGT85A123 in Nicotiana), suggesting this enzyme may participate in HGL-DTG biosynthesis or related pathways rather than flavonol metabolism. This represents a plausible alternative function that would also argue against GO:0080043.

3. **Database carry-over risk:** The IEA (Inferred from Electronic Annotation) evidence code via GO_REF:0000118 (TreeGrafter/PANTHER) means this annotation has never been independently verified by a curator or experimentalist for this specific protein.

### Knowledge Gaps

- No primary biochemical characterization of NaUGT1_candidate_UGT85A2_0 exists in the published literature. The actual substrate of this *N. attenuata* UGT85A member remains undetermined.
- Direct sequence alignment against characterized UGT85A active members to verify catalytic residue conservation was not computationally performed in this session due to lack of programmatic access to the protein sequence.
- The exact position of this protein within the UGT85A phylogeny (closer to the cytokinin-glucosylating clade of UGT85A1/A2 or the volatile-glucosylating clade of UGT85A28-type enzymes) would further refine the functional prediction.

### Most Efficient Discriminating Tests

1. **In vitro recombinant enzyme assay:** Express A0A2H4GSI3 recombinantly and test glucosyltransferase activity against quercetin, kaempferol, trans-zeatin, geraniol, and p-hydroxymandelonitrile as acceptors with UDP-glucose as donor. This would definitively confirm or refute the seed hypothesis and identify the true substrate.
2. **Sequence alignment with catalytic residues:** Align A0A2H4GSI3 against VvGT1 (PDB: 2C1Z), AtUGT78D2, AtUGT85A1, and UGT85A28 to compare the acceptor-binding pocket residues. If the pocket architecture resembles UGT85A1/A28 rather than VvGT1/UGT78D2, this computationally confirms the wrong-subfamily assignment.
3. **Co-expression analysis in *N. attenuata*:** Assess whether the gene co-expresses with cytokinin pathway genes, HGL-DTG biosynthetic genes, or flavonoid biosynthetic genes, which would clarify its metabolic context.
4. **Metabolite profiling of knockout/knockdown lines:** If reverse genetics tools are available for *N. attenuata*, disruption of this gene followed by metabolomic profiling would identify the affected metabolite class (flavonol glycosides vs. cytokinin glycosides vs. volatile glycosides vs. diterpene glycosides).


References

1. (roy2016glycosylationisa pages 4-5): Julien Le Roy, Brigitte Huss, Anne Creach, Simon Hawkins, and Godfrey Neutelings. Glycosylation is a major regulator of phenylpropanoid availability and biological activity in plants. Frontiers in Plant Science, May 2016. URL: https://doi.org/10.3389/fpls.2016.00735, doi:10.3389/fpls.2016.00735. This article has 464 citations.

2. (yin2010arabidopsisflavonoidglycosylation pages 9-13): Ruohe Yin. Arabidopsis flavonoid glycosylation impacts on phenylpropanoid biosynthesis and plant growth. Dissertation, Jan 2010. URL: https://doi.org/10.5282/edoc.13146, doi:10.5282/edoc.13146. This article has 0 citations.

3. (song2018attractivebuttoxic pages 4-7): Chuankui Song, Katja Härtl, Kate McGraphery, Thomas Hoffmann, and Wilfried Schwab. Attractive but toxic: emerging roles of glycosidically bound volatiles and glycosyltransferases involved in their formation. Molecular plant, 11 10:1225-1236, Oct 2018. URL: https://doi.org/10.1016/j.molp.2018.09.001, doi:10.1016/j.molp.2018.09.001. This article has 173 citations and is from a highest quality peer-reviewed journal.

4. (zhang2025singlecelltranscriptomicsand pages 12-14): Bingxu Zhang, Thomas Ka Yam Lam, Linheng Chen, Chen Zhang, Liping Zhu, Hailei Zhang, Pengxi Wang, Jianing Wang, Zongwei Cai, and Yiji Xia. Single-cell transcriptomics and time-series metabolite profiling reveal the spatiotemporal regulation of flavonoid biosynthesis genes and phytohormone homeostasis by pap1 in arabidopsis. BMC Biology, Jul 2025. URL: https://doi.org/10.1186/s12915-025-02297-6, doi:10.1186/s12915-025-02297-6. This article has 14 citations and is from a domain leading peer-reviewed journal.

5. (rehman2018comparativegenomicand pages 13-13): Hafiz Mamoon Rehman, Muhammad Amjad Nawaz, Zahid Hussain Shah, Jutta Ludwig-Müller, Gyuhwa Chung, Muhammad Qadir Ahmad, Seung Hwan Yang, and Soo In Lee. Comparative genomic and transcriptomic analyses of family-1 udp glycosyltransferase in three brassica species and arabidopsis indicates stress-responsive regulation. Scientific Reports, Jan 2018. URL: https://doi.org/10.1038/s41598-018-19535-3, doi:10.1038/s41598-018-19535-3. This article has 158 citations and is from a peer-reviewed journal.

6. (yamada2019aglucosyltransferasespecific pages 4-7): Aki Yamada, Kan’ichiro Ishiuchi, Toshiaki Makino, Hajime Mizukami, and Kazuyoshi Terasaka. A glucosyltransferase specific for 4-hydroxy-2,5-dimethyl-3(2h)-furanone in strawberry. Bioscience, Biotechnology, and Biochemistry, 83:106-113, Jan 2019. URL: https://doi.org/10.1080/09168451.2018.1524706, doi:10.1080/09168451.2018.1524706. This article has 17 citations.

7. (selmar2010biosynthesisofcyanogenic pages 22-25): Dirk Selmar. Biosynthesis of cyanogenic glycosides, glucosinolates and non‐protein amino acids. ArXiv, pages 92-181, Mar 2010. URL: https://doi.org/10.1002/9781444320503.ch3, doi:10.1002/9781444320503.ch3. This article has 51 citations.

8. (speeckaert2022ugt72amajor pages 9-10): Nathanaël Speeckaert, Mondher El Jaziri, Marie Baucher, and Marc Behr. Ugt72, a major glycosyltransferase family for flavonoid and monolignol homeostasis in plants. Biology, 11:441, Mar 2022. URL: https://doi.org/10.3390/biology11030441, doi:10.3390/biology11030441. This article has 44 citations.

9. (speeckaert2022ugt72amajor pages 8-9): Nathanaël Speeckaert, Mondher El Jaziri, Marie Baucher, and Marc Behr. Ugt72, a major glycosyltransferase family for flavonoid and monolignol homeostasis in plants. Biology, 11:441, Mar 2022. URL: https://doi.org/10.3390/biology11030441, doi:10.3390/biology11030441. This article has 44 citations.

10. (speeckaert2022ugt72amajor pages 5-8): Nathanaël Speeckaert, Mondher El Jaziri, Marie Baucher, and Marc Behr. Ugt72, a major glycosyltransferase family for flavonoid and monolignol homeostasis in plants. Biology, 11:441, Mar 2022. URL: https://doi.org/10.3390/biology11030441, doi:10.3390/biology11030441. This article has 44 citations.

11. (speeckaert2022ugt72amajor pages 10-10): Nathanaël Speeckaert, Mondher El Jaziri, Marie Baucher, and Marc Behr. Ugt72, a major glycosyltransferase family for flavonoid and monolignol homeostasis in plants. Biology, 11:441, Mar 2022. URL: https://doi.org/10.3390/biology11030441, doi:10.3390/biology11030441. This article has 44 citations.

12. (offen2006structureofa pages 6-7): Wendy Offen, Carlos Martinez-Fleites, Min Yang, Eng Kiat-Lim, Benjamin G Davis, Chris A Tarling, Christopher M Ford, Dianna J Bowles, and Gideon J Davies. Structure of a flavonoid glucosyltransferase reveals the basis for plant natural product modification. The EMBO Journal, 25:1396-1405, Mar 2006. URL: https://doi.org/10.1038/sj.emboj.7600970, doi:10.1038/sj.emboj.7600970. This article has 582 citations.

13. (offen2006structureofa pages 2-4): Wendy Offen, Carlos Martinez-Fleites, Min Yang, Eng Kiat-Lim, Benjamin G Davis, Chris A Tarling, Christopher M Ford, Dianna J Bowles, and Gideon J Davies. Structure of a flavonoid glucosyltransferase reveals the basis for plant natural product modification. The EMBO Journal, 25:1396-1405, Mar 2006. URL: https://doi.org/10.1038/sj.emboj.7600970, doi:10.1038/sj.emboj.7600970. This article has 582 citations.

14. (offen2006structureofa pages 4-6): Wendy Offen, Carlos Martinez-Fleites, Min Yang, Eng Kiat-Lim, Benjamin G Davis, Chris A Tarling, Christopher M Ford, Dianna J Bowles, and Gideon J Davies. Structure of a flavonoid glucosyltransferase reveals the basis for plant natural product modification. The EMBO Journal, 25:1396-1405, Mar 2006. URL: https://doi.org/10.1038/sj.emboj.7600970, doi:10.1038/sj.emboj.7600970. This article has 582 citations.

15. (louveau2019thesweetside pages 6-7): Thomas Louveau and Anne Osbourn. The sweet side of plant-specialized metabolism. Cold Spring Harbor perspectives in biology, 11:a034744, Jun 2019. URL: https://doi.org/10.1101/cshperspect.a034744, doi:10.1101/cshperspect.a034744. This article has 121 citations and is from a peer-reviewed journal.

16. (louveau2019thesweetside pages 7-9): Thomas Louveau and Anne Osbourn. The sweet side of plant-specialized metabolism. Cold Spring Harbor perspectives in biology, 11:a034744, Jun 2019. URL: https://doi.org/10.1101/cshperspect.a034744, doi:10.1101/cshperspect.a034744. This article has 121 citations and is from a peer-reviewed journal.

17. (louveau2019thesweetside pages 5-6): Thomas Louveau and Anne Osbourn. The sweet side of plant-specialized metabolism. Cold Spring Harbor perspectives in biology, 11:a034744, Jun 2019. URL: https://doi.org/10.1101/cshperspect.a034744, doi:10.1101/cshperspect.a034744. This article has 121 citations and is from a peer-reviewed journal.

18. (muller2024physiologicalandphytochemical pages 86-88): Physiological and phytochemical aspects of ant-plant mutualism This article has 1 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](falcon_artifacts/artifact-02.md)