---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:14:39.530780'
end_time: '2026-06-24T04:36:19.348609'
duration_seconds: 1299.82
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: fcs
  gene_symbol: fcs
  uniprot_accession: Q88HK0
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440)
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0031956
  hypothesis_text: fcs has medium-chain fatty acid-CoA ligase activity (GO:0031956).
  term_context: '- Term: medium-chain fatty acid-CoA ligase activity (GO:0031956)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118'
  source_file: genes/PSEPK/fcs/fcs-ai-review.yaml
  source_selector: existing_annotations[2].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0031956\n  label: medium-chain fatty acid-CoA\
    \ ligase activity\nevidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
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

- **Organism code:** PSEPK
- **Taxon:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440) (NCBITaxon:160488)
- **Gene directory:** fcs
- **Gene symbol:** fcs
- **UniProt accession:** Q88HK0

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0031956
- **Source file:** genes/PSEPK/fcs/fcs-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

fcs has medium-chain fatty acid-CoA ligase activity (GO:0031956).

## Term and Decision Context

- Term: medium-chain fatty acid-CoA ligase activity (GO:0031956)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118

## Source Context YAML

```yaml
term:
  id: GO:0031956
  label: medium-chain fatty acid-CoA ligase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **fcs directly has the stated function**. Automated
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

- **Organism code:** PSEPK
- **Taxon:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440) (NCBITaxon:160488)
- **Gene directory:** fcs
- **Gene symbol:** fcs
- **UniProt accession:** Q88HK0

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0031956
- **Source file:** genes/PSEPK/fcs/fcs-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

fcs has medium-chain fatty acid-CoA ligase activity (GO:0031956).

## Term and Decision Context

- Term: medium-chain fatty acid-CoA ligase activity (GO:0031956)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118

## Source Context YAML

```yaml
term:
  id: GO:0031956
  label: medium-chain fatty acid-CoA ligase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **fcs directly has the stated function**. Automated
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


# AIGR TreeGrafter Function-Inference Stress Test Report: fcs (Q88HK0, *Pseudomonas putida* KT2440)

## Executive Judgment

**Verdict: Refuted — Wrong subfamily (mis-placed); Failure mode 3.**

The propagated GO term GO:0031956 (medium-chain fatty acid-CoA ligase activity) is **incorrect** for fcs (Q88HK0) from *Pseudomonas putida* KT2440. This represents a clear case of **within-superfamily mis-placement** (failure mode 3): the TreeGrafter/PANTHER pipeline grafted fcs onto a PANTHER node representing medium-chain acyl-CoA synthetases (ACSM subfamily) within the ANL (acyl-CoA synthetase / NRPS adenylation / luciferase) superfamily, when fcs actually belongs to the 4-coumarate:CoA ligase (4CL) / hydroxycinnamate-CoA synthetase subfamily — a functionally distinct, sibling branch of the same adenylate-forming enzyme superfamily.

**Most decisive evidence:** An fcs deletion mutant in *P. putida* F1 cannot grow on ferulic acid, caffeic acid, or *p*-coumaric acid as sole carbon sources, and growth is restored by complementation with fcs in trans (hughes2017pseudomonasputidaf1 pages 3-4). This directly demonstrates that fcs is essential for hydroxycinnamic acid (aromatic) catabolism, not medium-chain fatty acid metabolism. The characterized closest homolog CouL from *Rhodococcus jostii* RHA1 thioesterifies ferulate, *p*-coumarate, caffeate, and dihydroferulate but shows no activity with non-aromatic substrates such as vanillate, benzoate, or aliphatic acids (otani2014characterizationofp pages 7-8, otani2014characterizationofp pages 8-9).

---

## Independent Family/Function Assignment

**Protein:** fcs (Q88HK0, PP_3356), *Pseudomonas putida* KT2440

**Most likely specific molecular function:** Feruloyl-CoA synthetase / *p*-hydroxycinnamoyl-CoA synthetase activity. The enzyme catalyzes the ATP-dependent CoA ligation of hydroxycinnamic acids (ferulic acid, caffeic acid, *p*-coumaric acid) as the first committed step in the CoA-dependent, non-β-oxidative phenylpropenoid degradation pathway leading to vanillin and vanillate production (jimenez2002genomicanalysisof pages 9-10, ruhl2025productionofvanillin pages 1-3, zhou2020developmentofa pages 6-7).

**Reaction catalyzed:** Ferulic acid + CoA + ATP → Feruloyl-CoA + AMP + PPi

**Recommended GO term:** GO:0016207 (4-coumarate-CoA ligase activity) is the most appropriate existing GO molecular function term. This term describes the ATP-dependent CoA ligation of hydroxycinnamic acid substrates, which is precisely the reaction catalyzed by fcs. If a more specific child term for feruloyl-CoA synthetase activity exists or is created, that would be even more precise.

**Characterized homolog basis:** CouL from *Rhodococcus jostii* RHA1, which has been biochemically characterized with purified enzyme kinetics showing *k*cat/*K*m of ~370 mM⁻¹ s⁻¹ for *p*-coumarate, with activity on ferulate, caffeate, and dihydroferulate, but no detectable activity on sinapate, vanillate, or benzoate (otani2014characterizationofp pages 7-8, otani2014characterizationofp pages 8-9, otani2014characterizationofp pages 1-2).

**Granularity relative to seed term:** The correct term (GO:0016207 or a child thereof) is a **sibling** of GO:0031956 within the broader CoA ligase / acid-thiol ligase activity hierarchy — both are acyl-CoA synthetase activities but act on entirely different substrate classes (aromatic hydroxycinnamic acids vs. aliphatic medium-chain fatty acids). This is not a granularity issue (too general or too specific) but rather a mis-placement onto the wrong neighboring subfamily.

---

## Evidence Matrix

The following table summarizes all evidence items evaluated, showing that every independent line of evidence refutes the assignment of GO:0031956 to fcs.

| Citation (PMID/DOI) | Evidence Type | Supports/Refutes/Qualifies | Claim Tested | Key Finding | Organism/Assay Context | Confidence/Limitations |
|---|---|---|---|---|---|---|
| Hughes et al. 2017, doi:10.1099/mic.0.000533 | Mutant phenotype / complementation | Refutes | Does **fcs** encode a medium-chain fatty acid-CoA ligase? | **fcs** deletion abolished growth on ferulic acid, caffeic acid, and *p*-coumaric acid; complementation restored growth, showing **fcs** is required for hydroxycinnamate catabolism rather than medium-chain fatty acid utilization (hughes2017pseudomonasputidaf1 pages 3-4) | *Pseudomonas putida* F1; deletion mutant growth on aromatic sole carbon sources | High for pathway role; indirect for exact reaction product because assay is genetic, not purified-enzyme biochemistry |
| Jiménez et al. 2002, doi:10.1046/j.1462-2920.2002.00370.x | Genomic/pathway analysis | Refutes | Is **fcs** positioned in a fatty-acid activation pathway? | Identified **fcs** in the KT2440 phenylpropenoid/ferulic acid catabolic gene cluster with **ech**, **vdh**, **aat**, **acd**; pathway context indicates activation of ferulic acid to feruloyl-CoA in aromatic metabolism, not fatty-acid metabolism (jimenez2002genomicanalysisof pages 9-10) | *P. putida* KT2440 genome context and aromatic catabolic reconstruction | High for pathway placement; not a direct substrate assay |
| Otani et al. 2014, doi:10.1128/JB.02247-14 | Direct biochemical assay of characterized homolog | Refutes | Does the closest characterized subfamily behave like fatty acid-CoA ligases or hydroxycinnamate-CoA ligases? | CouL, an **fcs** homolog, thioesterified *p*-coumarate, ferulate, caffeate, and dihydroferulate, but not sinapate, vanillate, or benzoate; kinetics showed preference for *p*-hydroxycinnamates, not aliphatic fatty acids (otani2014characterizationofp pages 7-8, otani2014characterizationofp pages 8-9, otani2014characterizationofp pages 1-2) | *Rhodococcus jostii* RHA1 purified enzyme kinetics | High for homolog subfamily specificity; inference to Q88HK0 is by homology, not same-protein assay |
| Li & Nair 2015, doi:10.1016/j.str.2015.08.012 | Structural / enzymology | Refutes | Is the substrate pocket consistent with aromatic hydroxycinnamates or medium-chain fatty acids? | 4CL2 structures with coumaroyl-, caffeoyl-, and feruloyl-AMP showed an aromatic-binding cavity with residues such as Tyr239, Met306, Gly308, Val341, and Met344; pocket architecture is optimized for hydroxycinnamate rings rather than aliphatic acyl chains (li2015structuralbasisfor pages 7-8, li2015structuralbasisfor pages 4-5, li2015structuralbasisfor pages 6-7, li2015structuralbasisfor pages 5-6) | Plant 4-coumarate:CoA ligase crystal structures and mutagenesis | High for mechanistic distinction of subfamilies; non-bacterial homolog |
| Khurana et al. 2010, doi:10.1186/1471-2105-11-57 | Computational subfamily classification / SDR analysis | Refutes | Could an ANL-superfamily protein be misassigned from aromatic CoA ligase to fatty acid-CoA ligase? | Active-site residue profiles (15 SDRs) distinguish 4CL enzymes from medium-/long-chain fatty acid-CoA ligases with high sensitivity/specificity; demonstrates that ANL-family members can be separated by substrate-determining residues and that aromatic-CoA ligases are a distinct subfamily (khurana2010genomescaleprediction pages 6-8, khurana2010genomescaleprediction pages 4-6, khurana2010genomescaleprediction pages 3-4, khurana2010genomescaleprediction pages 10-13, khurana2010genomescaleprediction pages 14-16) | Multi-genome computational analysis of ANL superfamily | Moderate-high; computational rather than direct assay on Q88HK0 |
| Priyadarshan & Sankaranarayanan 2018, doi:10.1007/s41745-018-0084-2 | Review/structural superfamily analysis | Qualifies / Refutes | Are aromatic CoA ligases and fatty acyl ligases mechanistically neighboring but distinct ANL subfamilies? | ANL enzymes share catalytic logic but aromatic-ligase pockets are broader and shaped for aryl substrates, whereas fatty-acyl ligases use tunnel-like pockets and chain-length rulers; supports a likely within-superfamily misplacement rather than loss of activity (priyadarshan2018fattyacylampligases pages 7-9, priyadarshan2018fattyacylampligases pages 2-4) | Cross-family structural/mechanistic synthesis | Moderate; authoritative synthesis but not primary assay of Q88HK0 |
| Ruhl et al. 2025, doi:10.1111/1751-7915.70152 | Metabolic engineering / pathway validation | Refutes | Is Fcs part of ferulic-acid-to-vanillin metabolism? | Fcs is one of the enzymes responsible for conversion of ferulic acid toward vanillin in engineered KT2440, reinforcing assignment to hydroxycinnamate activation rather than fatty acid activation (ruhl2025productionofvanillin pages 1-3) | Engineered *P. putida* KT2440 for vanillin production | Moderate; pathway engineering evidence, not purified enzyme specificity panel |
| Zhou et al. 2020, doi:10.1038/s42003-020-0824-5 | Metabolic engineering / CRISPR pathway reconstruction | Refutes | Does **fcs** function in the ferulic acid catabolic module? | CRISPR-based engineering treated **fcs**, **ech**, and **vdh** as the core ferulic acid catabolic module converting ferulic acid through vanillin/vanillate metabolism; incompatible with a medium-chain fatty acid-specific annotation (zhou2020developmentofa pages 6-7) | Engineered *P. putida* KT2440 ferulic acid bioconversion | Moderate; pathway-level rather than direct enzyme-substrate assay |
| D'Arrigo et al. 2019, doi:10.1111/1758-2229.12704 | Transcriptomics / systems biology | Refutes | Is **fcs** responsive to ferulic acid assimilation conditions? | **fcs** (PP_3356) was strongly induced during growth on ferulic acid as sole carbon source, alongside **ech** and **vdh**, consistent with aromatic catabolism rather than generic medium-chain fatty acid activation (darrigo2019analysisofpseudomonas pages 14-16) | *P. putida* KT2440 RNA-seq and metabolic modeling under ferulic acid growth | Moderate; expression evidence is correlative, not direct biochemical proof |


*Table: This table summarizes independent evidence evaluating whether P. putida fcs (Q88HK0) has medium-chain fatty acid-CoA ligase activity. The evidence consistently points instead to hydroxycinnamate/feruloyl-CoA synthetase function and a within-superfamily misannotation.*

---

## Active-Site / Placement Analysis

The following analysis compares the structural, catalytic, and SDR-profile features of fcs with characterized 4CL-type (aromatic CoA ligase) and ACSM-type (medium-chain fatty acid CoA ligase) enzymes within the ANL superfamily.

| Analysis aspect | P. putida fcs (Q88HK0) / aromatic CoA ligase interpretation | Characterized 4CL / hydroxycinnamate-CoA ligases | Medium-chain fatty acid-CoA ligases (ACSM/MCS) | Implication for GO:0031956 |
|---|---|---|---|---|
| Superfamily membership | fcs belongs to the ANL (acyl-CoA synthetase/NRPS adenylation/luciferase) superfamily and therefore is expected to share the canonical AMP-forming fold and domain alternation chemistry with other acyl-CoA synthetases (li2015structuralbasisfor pages 4-5, priyadarshan2018fattyacylampligases pages 2-4) | 4CL enzymes are established ANL-family adenylating enzymes using the same two-step adenylation/thioesterification mechanism (li2015structuralbasisfor pages 1-3, li2015structuralbasisfor pages 4-5) | Medium-chain FA-CoA ligases are also ANL-family members with the same broad fold and chemistry (khurana2010genomescaleprediction pages 6-8, khurana2010genomescaleprediction pages 10-13) | Shared superfamily does **not** justify direct transfer of the ACSM-specific MF term |
| Conserved catalytic core | Expected to retain the ANL catalytic core; no evidence of pseudization or catalytic loss, and pathway genetics show activity in vivo (li2015structuralbasisfor pages 4-5, priyadarshan2018fattyacylampligases pages 2-4, hughes2017pseudomonasputidaf1 pages 3-4) | Conserved A1-A10 motifs, P-loop, catalytic His, catalytic Thr, and invariant A10 Lys are essential for adenylation in 4CL enzymes (li2015structuralbasisfor pages 4-5, li2015structuralbasisfor pages 5-6) | ACSM enzymes also retain the same superfamily-level catalytic motifs for adenylation/thioesterification (khurana2010genomescaleprediction pages 6-8, priyadarshan2018fattyacylampligases pages 2-4) | Catalytic motif conservation supports “active ANL enzyme,” but not “medium-chain fatty acid substrate” |
| Invariant Lys / catalytic motifs | By ANL-family placement, fcs is expected to carry the invariant A10 Lys and associated catalytic motifs required for adenylate formation; functional complementation indicates these motifs are intact enough for catalysis in vivo (li2015structuralbasisfor pages 4-5, priyadarshan2018fattyacylampligases pages 2-4, hughes2017pseudomonasputidaf1 pages 3-4) | Nt4CL2 uses invariant Lys526 (A10), His237, Thr336, and P-loop residues for catalysis; mutation abolishes or severely reduces activity (li2015structuralbasisfor pages 4-5, li2015structuralbasisfor pages 5-6) | ACSM/MCS enzymes use the same catalytic logic but with different substrate-recognition determinants around the pocket (khurana2010genomescaleprediction pages 6-8, khurana2010genomescaleprediction pages 10-13) | Failure mode is **not** pseudo-enzyme/lost activity |
| Aromatic substrate-recognition features | fcs function and physiology fit an aromatic hydroxycinnamate-binding pocket rather than an aliphatic chain tunnel: growth depends on fcs specifically on ferulate, caffeate, and p-coumarate (hughes2017pseudomonasputidaf1 pages 3-4) | 4CL pockets include residues enabling aromatic binding and π-stacking, e.g. Tyr239 equivalent, with cavity features formed by residues such as Met306, Gly308, Val341, Met344; optimized for flat hydroxycinnamic acids (li2015structuralbasisfor pages 7-8, li2015structuralbasisfor pages 6-7) | ACSM/MCS enzymes instead use hydrophobic aliphatic-chain tunnels rather than aromatic planar-substrate cavities (priyadarshan2018fattyacylampligases pages 7-9, khurana2010genomescaleprediction pages 10-13) | Strongly inconsistent with medium-chain fatty acid-CoA ligase activity |
| Pocket geometry | Best explained by a broader aromatic-acid pocket in the 4CL-like branch of ANL enzymes (priyadarshan2018fattyacylampligases pages 7-9, li2015structuralbasisfor pages 7-8) | Broader cavity accommodates coumarate/caffeate/ferulate-class substrates; aromatic face and steric gate shape hydroxycinnamate selectivity (li2015structuralbasisfor pages 7-8, li2015structuralbasisfor pages 8-10) | Narrower hydrophobic tunnel acts as a chain-length selector or “molecular ruler” for aliphatic medium-chain substrates (priyadarshan2018fattyacylampligases pages 7-9, khurana2010genomescaleprediction pages 10-13) | Indicates wrong neighboring subfamily assignment rather than coarse family-level correctness |
| SDR position 210 | fcs should not be interpreted with the ACSM-specific medium-chain chain-length signature at this position (khurana2010genomescaleprediction pages 10-13) | Not the defining medium-chain signature in 4CL enzymes; aromatic-ligase classification depends on a different SDR pattern (khurana2010genomescaleprediction pages 4-6, khurana2010genomescaleprediction pages 8-10) | Position 210 is informative for fatty-acyl chain length, with His associated with medium-chain and Asn with long-chain CoA ligases (khurana2010genomescaleprediction pages 10-13) | Presence of ANL-family homology alone cannot override subfamily-specific SDR logic |
| SDR position 234 | fcs is more consistent with the aromatic-ligase SDR regime that includes conserved His at this position in 4CL-like enzymes (khurana2010genomescaleprediction pages 6-8) | Conserved His234 is characteristic in 4CL/LCS/MCS comparisons and contributes to attraction/positioning of larger carboxylic acid substrates in deep pockets (khurana2010genomescaleprediction pages 6-8) | ACSM subfamily is distinguished by a different overall 15-residue profile, not by simple transfer from 4CL-like profiles (khurana2010genomescaleprediction pages 4-6, khurana2010genomescaleprediction pages 14-16) | Supports need for subfamily-specific annotation |
| SDR position 324 | fcs should be interpreted in the context of aromatic-substrate accommodation rather than the small-substrate/chain-length logic used for aliphatic ACSs (khurana2010genomescaleprediction pages 6-8, khurana2010genomescaleprediction pages 8-10) | In ANL comparisons, pocket-opening effects around this position help define capacity for larger aromatic substrates (khurana2010genomescaleprediction pages 6-8, li2015structuralbasisfor pages 7-8) | Trp at equivalent position constricts pocket in small-substrate enzymes, while Gly can permit larger substrates; this illustrates how a few SDRs shift specificity across ANL neighbors (khurana2010genomescaleprediction pages 6-8) | Demonstrates how TreeGrafter can misplace proteins within a shared fold superfamily |
| SDR position 301 | fcs should follow the aromatic-CoA ligase active-site profile rather than ACSM-specific chain-binding constraints (khurana2010genomescaleprediction pages 13-14, khurana2010genomescaleprediction pages 14-16) | 4CL-like enzymes show subfamily-specific residue usage across the 15-SDR profile that predicts aromatic-acid activation (khurana2010genomescaleprediction pages 4-6, khurana2010genomescaleprediction pages 14-16) | Larger or different residues at position 301 contribute to acyl-chain pocket properties in fatty-acid ligases (khurana2010genomescaleprediction pages 13-14, khurana2010genomescaleprediction pages 10-13) | Another indicator that correct annotation requires SDR-level classification |
| Closest characterized functional neighborhood | fcs clusters functionally with hydroxycinnamate-activating enzymes such as CouL/fcs homologs, not ACSM enzymes (otani2014characterizationofp pages 7-8, otani2014characterizationofp pages 1-2) | CouL and related 4CL/fcs-type enzymes activate p-coumarate, ferulate, caffeate, and dihydroferulate; they do not behave as fatty-acid ligases (otani2014characterizationofp pages 7-8, otani2014characterizationofp pages 8-9, otani2014characterizationofp pages 1-2) | ACSM enzymes specialize in aliphatic medium-chain fatty acids and are classified separately by SDR/pocket architecture (khurana2010genomescaleprediction pages 6-8, khurana2010genomescaleprediction pages 10-13) | Nearest characterized subfamily carries a sibling activity, not the propagated one |
| Genomic/pathway context | In KT2440, fcs is embedded in the ferulic acid/phenylpropenoid catabolic module with ech and vdh, exactly where a hydroxycinnamoyl-CoA ligase is expected (jimenez2002genomicanalysisof pages 9-10, zhou2020developmentofa pages 6-7, darrigo2019analysisofpseudomonas pages 14-16) | 4CL/fcs-type enzymes function in hydroxycinnamate conversion to CoA esters in aromatic metabolism (jimenez2002genomicanalysisof pages 9-10, ruhl2025productionofvanillin pages 1-3) | ACSM genes are associated with fatty-acid activation/metabolism, not ferulate-to-vanillin pathways (ruhl2025productionofvanillin pages 1-3, zhou2020developmentofa pages 6-7) | Strong refutation of GO:0031956 by orthogonal pathway evidence |
| Experimental activity status | Catalytically active in vivo: deleting fcs abolishes growth on ferulate, caffeate, and p-coumarate; complementation restores growth (hughes2017pseudomonasputidaf1 pages 3-4) | Active hydroxycinnamoyl-CoA ligases show direct or inferred conversion of hydroxycinnamates to CoA esters (otani2014characterizationofp pages 7-8, otani2014characterizationofp pages 8-9) | No evidence that fcs supports utilization of medium-chain fatty acids (hughes2017pseudomonasputidaf1 pages 3-4) | Activity is intact, but the substrate class is wrong |
| Placement verdict | **fcs belongs to the 4CL / hydroxycinnamate-CoA ligase branch of the ANL superfamily** based on pathway context, mutant phenotype, characterized homologs, and aromatic-pocket structural logic (hughes2017pseudomonasputidaf1 pages 3-4, jimenez2002genomicanalysisof pages 9-10, otani2014characterizationofp pages 7-8, li2015structuralbasisfor pages 7-8) | Correct functional neighborhood: aromatic hydroxycinnamate CoA ligases / feruloyl-CoA synthetases (otani2014characterizationofp pages 7-8, li2015structuralbasisfor pages 7-8) | Incorrect neighboring branch: medium-chain fatty acid-CoA ligases (khurana2010genomescaleprediction pages 6-8, khurana2010genomescaleprediction pages 10-13) | **Refutes GO:0031956; this is a within-superfamily mis-placement** |
| Curation consequence | Assign aromatic hydroxycinnamate CoA-ligase function, e.g. 4-coumarate-CoA ligase / feruloyl-CoA synthetase-type activity, rather than medium-chain fatty acid-CoA ligase (hughes2017pseudomonasputidaf1 pages 3-4, jimenez2002genomicanalysisof pages 9-10, otani2014characterizationofp pages 7-8) | More specific and biologically coherent with known hydroxycinnamate catabolism (jimenez2002genomicanalysisof pages 9-10, otani2014characterizationofp pages 7-8) | GO:0031956 should not be retained for fcs (hughes2017pseudomonasputidaf1 pages 3-4) | Replace with sibling-term in aromatic CoA-ligase branch |


*Table: This table compares P. putida fcs with aromatic 4CL-type ligases and medium-chain fatty acid-CoA ligases across catalytic motifs, substrate-pocket architecture, SDRs, and pathway evidence. It is useful for localizing the TreeGrafter error as a within-superfamily misplacement rather than loss of activity.*

### Summary of Active-Site Analysis

**Catalytic residues:** The ANL superfamily conserves ten signature motifs (A1–A10) across all members, including the invariant A10 lysine (Lys526 in Nt4CL2) required for adenylation, the P-loop for pyrophosphate coordination, His237 (A4 motif) essential for catalysis, and Thr336 (A5 motif) (li2015structuralbasisfor pages 4-5, li2015structuralbasisfor pages 5-6). These catalytic residues are shared between 4CL-type and ACSM-type enzymes as superfamily-level features. The fcs enzyme is catalytically active as demonstrated by genetic complementation (hughes2017pseudomonasputidaf1 pages 3-4). **This rules out failure mode 2 (pseudo-enzyme / loss of activity).**

**Substrate-binding pocket architecture:** The critical distinction between the two subfamilies lies in the substrate-binding pocket. 4CL-type enzymes have broader cavities optimized for flat, planar hydroxycinnamic acid substrates, with residues enabling π-stacking interactions (e.g., Tyr239 equivalent) and specific gate residues controlling ring-substitution tolerance (e.g., Val341 in Nt4CL2) (li2015structuralbasisfor pages 7-8, li2015structuralbasisfor pages 6-7). In contrast, ACSM/medium-chain fatty acid-CoA ligases use hydrophobic tunnel-like pockets that act as "molecular rulers" to select for aliphatic chain length, with bulkier residues along helices α7/α8 and strands β10/β12 that restrict tunnel dimensions (priyadarshan2018fattyacylampligases pages 7-9, khurana2010genomescaleprediction pages 10-13).

**SDR-based classification:** The Khurana et al. (2010) computational framework using 15 substrate-specificity-determining residues (SDRs) can distinguish 4CL, ACSM, ACSL (long-chain), AcCS (acetyl), and other subfamilies with sensitivity of 0.91–1.0 and specificity of 0.96–1.0 (khurana2010genomescaleprediction pages 6-8, khurana2010genomescaleprediction pages 4-6, khurana2010genomescaleprediction pages 3-4). Key discriminating positions include: position 210 (His in medium-chain vs. Asn in long-chain), position 234 (conserved His in 4CL-type), position 324 (Trp in small-substrate enzymes vs. Gly for larger substrates), and position 301 (khurana2010genomescaleprediction pages 6-8, khurana2010genomescaleprediction pages 10-13). These SDR profiles clearly separate the 4CL aromatic-CoA ligase subfamily from the ACSM fatty acid-CoA ligase subfamily.

**Limitation:** I was unable to programmatically perform a direct residue-by-residue alignment of Q88HK0 against characterized 4CL and ACSM sequences because the tools available do not include sequence retrieval and alignment capabilities. However, the genomic context, characterized homolog data, and substrate specificity evidence are individually and collectively decisive.

---

## GO Curation Implications

**Recommended curation action: Replace with sibling term.**

- **Remove:** GO:0031956 (medium-chain fatty acid-CoA ligase activity) — this is a clear mis-annotation resulting from within-superfamily mis-placement by the TreeGrafter pipeline.
- **Replace with:** GO:0016207 (4-coumarate-CoA ligase activity) — this correctly captures the ATP-dependent CoA ligation of hydroxycinnamic acid substrates (ferulic acid, *p*-coumaric acid, caffeic acid) that fcs catalyzes (hughes2017pseudomonasputidaf1 pages 3-4, jimenez2002genomicanalysisof pages 9-10, otani2014characterizationofp pages 7-8).
- **Evidence code:** The replacement annotation could be supported by IDA (inferred from direct assay) based on the genetic complementation and growth phenotype data in *P. putida* F1 (hughes2017pseudomonasputidaf1 pages 3-4), combined with ISS (inferred from sequence/structural similarity) to CouL from *Rhodococcus jostii* RHA1, which has been directly characterized biochemically (otani2014characterizationofp pages 7-8, otani2014characterizationofp pages 8-9).
- **Biological process terms** such as GO:0019439 (aromatic compound catabolic process) and GO:0009058 (biosynthetic process) related to vanillin biosynthesis from ferulic acid should also be considered for annotation (jimenez2002genomicanalysisof pages 9-10, ruhl2025productionofvanillin pages 1-3, zhou2020developmentofa pages 6-7).

---

## Conflicts, Knowledge Gaps, and Discriminating Tests

### Source of the Error
The mis-annotation is a textbook example of the ANL superfamily confounding phylogenetic propagation pipelines. Both 4CL-type hydroxycinnamate-CoA ligases and ACSM-type medium-chain fatty acid-CoA ligases share the AMP-forming/AMP-binding domain (Pfam PF00501), the same two-step adenylation/thioesterification catalytic mechanism, and similar overall folds (priyadarshan2018fattyacylampligases pages 2-4, khurana2010genomescaleprediction pages 4-6). However, their substrate-binding pockets have diverged to accommodate fundamentally different substrate classes (aromatic vs. aliphatic), and their biological roles are unrelated (aromatic catabolism vs. lipid metabolism) (priyadarshan2018fattyacylampligases pages 7-9, li2015structuralbasisfor pages 7-8). TreeGrafter apparently grafted fcs onto the wrong branch of the PANTHER reference tree at the superfamily level rather than the subfamily level.

### Key Uncertainties
1. **Direct in vitro kinetics on purified fcs (Q88HK0):** While the genetic evidence is strong and the characterized homolog CouL provides kinetic data, published purified-enzyme kinetics for the exact Q88HK0 protein were not identified in this search. A 2022 paper by dos Santos et al. (doi:10.1016/j.pep.2022.106109) and a 2025 Methods in Enzymology chapter by Sodré & Squina (doi:10.1016/bs.mie.2025.01.046) describe recombinant feruloyl-CoA synthetase characterization but were unobtainable.
2. **SDR alignment not computed:** I could not programmatically extract the 15 SDR positions from Q88HK0 and compare them to the 4CL vs. ACSM reference profiles from Khurana et al. (2010). This would be the most direct computational proof of subfamily placement.

### Discriminating Tests to Resolve
1. **Most efficient resolution:** Extract SDR positions from Q88HK0 by aligning to the 1AMU structural template and compare the 15-residue profile against the 4CL, ACSM, and ACSL subfamily PSSMs from Khurana et al. (2010) (khurana2010genomescaleprediction pages 4-6, khurana2010genomescaleprediction pages 14-16). This would computationally confirm subfamily placement in minutes.
2. **Direct enzymatic assay:** Purify recombinant Q88HK0 and test CoA ligation activity with: (a) hydroxycinnamic acid substrates (ferulic, *p*-coumaric, caffeic acid), and (b) medium-chain fatty acids (hexanoic, octanoic, decanoic acid). Activity with the former and not the latter would definitively refute GO:0031956.
3. **Negative control:** Test whether an fcs deletion mutant shows any defect in medium-chain fatty acid utilization. Based on the available evidence, no such defect is expected.

### No Conflicting Evidence
No evidence was found supporting the assignment of GO:0031956 to fcs. All nine independent lines of evidence (genetic, transcriptomic, pathway, structural, computational, metabolic engineering) consistently point to hydroxycinnamate-CoA synthetase activity. There is no paralog confusion concern because fcs (PP_3356) is the sole gene in the *P. putida* KT2440 genome encoding the ferulic acid catabolic pathway's CoA-activating step, and it resides in a well-characterized gene cluster with ech and vdh (jimenez2002genomicanalysisof pages 9-10, darrigo2019analysisofpseudomonas pages 14-16).


References

1. (hughes2017pseudomonasputidaf1 pages 3-4): Jonathan G. Hughes, Xiangsheng Zhang, Juanito V. Parales, Jayna L. Ditty, and Rebecca E. Parales. Pseudomonas putida f1 uses energy taxis to sense hydroxycinnamic acids. Oct 2017. URL: https://doi.org/10.1099/mic.0.000533, doi:10.1099/mic.0.000533. This article has 13 citations and is from a peer-reviewed journal.

2. (otani2014characterizationofp pages 7-8): Hiroshi Otani, Young-Eun Lee, Israël Casabon, and Lindsay D. Eltis. Characterization of <i>p</i> -hydroxycinnamate catabolism in a soil actinobacterium. Journal of Bacteriology, 196:4293-4303, Dec 2014. URL: https://doi.org/10.1128/jb.02247-14, doi:10.1128/jb.02247-14. This article has 74 citations and is from a peer-reviewed journal.

3. (otani2014characterizationofp pages 8-9): Hiroshi Otani, Young-Eun Lee, Israël Casabon, and Lindsay D. Eltis. Characterization of <i>p</i> -hydroxycinnamate catabolism in a soil actinobacterium. Journal of Bacteriology, 196:4293-4303, Dec 2014. URL: https://doi.org/10.1128/jb.02247-14, doi:10.1128/jb.02247-14. This article has 74 citations and is from a peer-reviewed journal.

4. (jimenez2002genomicanalysisof pages 9-10): José Ignacio Jiménez, Baltasar Miñambres, José Luis García, and Eduardo Díaz. Genomic analysis of the aromatic catabolic pathways from pseudomonas putida kt2440. Environmental microbiology, 4 12:824-41, Dec 2002. URL: https://doi.org/10.1046/j.1462-2920.2002.00370.x, doi:10.1046/j.1462-2920.2002.00370.x. This article has 704 citations and is from a domain leading peer-reviewed journal.

5. (ruhl2025productionofvanillin pages 1-3): Ilona A. Ruhl, Sean P. Woodworth, Stefan J. Haugen, Hannah M. Alt, Gregg T. Beckham, and Christopher W. Johnson. Production of vanillin from ferulic acid by pseudomonas putida kt2440 using metabolic engineering and in situ product recovery. Microbial Biotechnology, May 2025. URL: https://doi.org/10.1111/1751-7915.70152, doi:10.1111/1751-7915.70152. This article has 13 citations and is from a peer-reviewed journal.

6. (zhou2020developmentofa pages 6-7): Yueyue Zhou, Lu Lin, Heng Wang, Zhichao Zhang, Jizhong Zhou, and Nianzhi Jiao. Development of a crispr/cas9n-based tool for metabolic engineering of pseudomonas putida for ferulic acid-to-polyhydroxyalkanoate bioconversion. Communications Biology, Mar 2020. URL: https://doi.org/10.1038/s42003-020-0824-5, doi:10.1038/s42003-020-0824-5. This article has 102 citations and is from a peer-reviewed journal.

7. (otani2014characterizationofp pages 1-2): Hiroshi Otani, Young-Eun Lee, Israël Casabon, and Lindsay D. Eltis. Characterization of <i>p</i> -hydroxycinnamate catabolism in a soil actinobacterium. Journal of Bacteriology, 196:4293-4303, Dec 2014. URL: https://doi.org/10.1128/jb.02247-14, doi:10.1128/jb.02247-14. This article has 74 citations and is from a peer-reviewed journal.

8. (li2015structuralbasisfor pages 7-8): Zhi Li and Satish K. Nair. Structural basis for specificity and flexibility in a plant 4-coumarate:coa ligase. Structure, 23:2032-2042, Nov 2015. URL: https://doi.org/10.1016/j.str.2015.08.012, doi:10.1016/j.str.2015.08.012. This article has 93 citations and is from a domain leading peer-reviewed journal.

9. (li2015structuralbasisfor pages 4-5): Zhi Li and Satish K. Nair. Structural basis for specificity and flexibility in a plant 4-coumarate:coa ligase. Structure, 23:2032-2042, Nov 2015. URL: https://doi.org/10.1016/j.str.2015.08.012, doi:10.1016/j.str.2015.08.012. This article has 93 citations and is from a domain leading peer-reviewed journal.

10. (li2015structuralbasisfor pages 6-7): Zhi Li and Satish K. Nair. Structural basis for specificity and flexibility in a plant 4-coumarate:coa ligase. Structure, 23:2032-2042, Nov 2015. URL: https://doi.org/10.1016/j.str.2015.08.012, doi:10.1016/j.str.2015.08.012. This article has 93 citations and is from a domain leading peer-reviewed journal.

11. (li2015structuralbasisfor pages 5-6): Zhi Li and Satish K. Nair. Structural basis for specificity and flexibility in a plant 4-coumarate:coa ligase. Structure, 23:2032-2042, Nov 2015. URL: https://doi.org/10.1016/j.str.2015.08.012, doi:10.1016/j.str.2015.08.012. This article has 93 citations and is from a domain leading peer-reviewed journal.

12. (khurana2010genomescaleprediction pages 6-8): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

13. (khurana2010genomescaleprediction pages 4-6): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

14. (khurana2010genomescaleprediction pages 3-4): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

15. (khurana2010genomescaleprediction pages 10-13): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

16. (khurana2010genomescaleprediction pages 14-16): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

17. (priyadarshan2018fattyacylampligases pages 7-9): Kinatukara Priyadarshan and Rajan Sankaranarayanan. Fatty acyl-amp ligases as mechanistic variants of anl superfamily and molecular determinants dictating substrate specificities. Journal of the Indian Institute of Science, 98:261-272, Jul 2018. URL: https://doi.org/10.1007/s41745-018-0084-2, doi:10.1007/s41745-018-0084-2. This article has 13 citations.

18. (priyadarshan2018fattyacylampligases pages 2-4): Kinatukara Priyadarshan and Rajan Sankaranarayanan. Fatty acyl-amp ligases as mechanistic variants of anl superfamily and molecular determinants dictating substrate specificities. Journal of the Indian Institute of Science, 98:261-272, Jul 2018. URL: https://doi.org/10.1007/s41745-018-0084-2, doi:10.1007/s41745-018-0084-2. This article has 13 citations.

19. (darrigo2019analysisofpseudomonas pages 14-16): Isotta D'Arrigo, João G. R. Cardoso, Maja Rennig, Nikolaus Sonnenschein, Markus J. Herrgård, and Katherine S. Long. Analysis of pseudomonas putida growth on non‐trivial carbon sources using transcriptomics and genome‐scale modelling. Environmental Microbiology Reports, 11:87–97, Nov 2019. URL: https://doi.org/10.1111/1758-2229.12704, doi:10.1111/1758-2229.12704. This article has 38 citations and is from a peer-reviewed journal.

20. (li2015structuralbasisfor pages 1-3): Zhi Li and Satish K. Nair. Structural basis for specificity and flexibility in a plant 4-coumarate:coa ligase. Structure, 23:2032-2042, Nov 2015. URL: https://doi.org/10.1016/j.str.2015.08.012, doi:10.1016/j.str.2015.08.012. This article has 93 citations and is from a domain leading peer-reviewed journal.

21. (li2015structuralbasisfor pages 8-10): Zhi Li and Satish K. Nair. Structural basis for specificity and flexibility in a plant 4-coumarate:coa ligase. Structure, 23:2032-2042, Nov 2015. URL: https://doi.org/10.1016/j.str.2015.08.012, doi:10.1016/j.str.2015.08.012. This article has 93 citations and is from a domain leading peer-reviewed journal.

22. (khurana2010genomescaleprediction pages 8-10): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

23. (khurana2010genomescaleprediction pages 13-14): Pankaj Khurana, Rajesh S Gokhale, and Debasisa Mohanty. Genome scale prediction of substrate specificity for acyl adenylate superfamily of enzymes based on active site residue profiles. BMC Bioinformatics, 11:57-57, Jan 2010. URL: https://doi.org/10.1186/1471-2105-11-57, doi:10.1186/1471-2105-11-57. This article has 45 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](falcon_artifacts/artifact-01.md)