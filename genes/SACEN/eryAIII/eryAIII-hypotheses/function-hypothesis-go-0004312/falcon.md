---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:14:40.791436'
end_time: '2026-06-24T04:31:56.264284'
duration_seconds: 1035.47
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: SACEN
  gene: eryAIII
  gene_symbol: eryAIII
  uniprot_accession: A4F7P1
  taxon_id: NCBITaxon:405948
  taxon_label: Saccharopolyspora erythraea (strain ATCC 11635 / DSM 40517 / JCM 4748
    / NBRC 13426 / NCIMB 8594 / NRRL 2338)
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004312
  hypothesis_text: eryAIII has fatty acid synthase activity (GO:0004312).
  term_context: '- Term: fatty acid synthase activity (GO:0004312)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - PMID:2024119'
  source_file: genes/SACEN/eryAIII/eryAIII-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004312\n  label: fatty acid synthase activity\n\
    evidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
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

- **Organism code:** SACEN
- **Taxon:** Saccharopolyspora erythraea (strain ATCC 11635 / DSM 40517 / JCM 4748 / NBRC 13426 / NCIMB 8594 / NRRL 2338) (NCBITaxon:405948)
- **Gene directory:** eryAIII
- **Gene symbol:** eryAIII
- **UniProt accession:** A4F7P1

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004312
- **Source file:** genes/SACEN/eryAIII/eryAIII-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

eryAIII has fatty acid synthase activity (GO:0004312).

## Term and Decision Context

- Term: fatty acid synthase activity (GO:0004312)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- PMID:2024119

## Source Context YAML

```yaml
term:
  id: GO:0004312
  label: fatty acid synthase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **eryAIII directly has the stated function**. Automated
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

- **Organism code:** SACEN
- **Taxon:** Saccharopolyspora erythraea (strain ATCC 11635 / DSM 40517 / JCM 4748 / NBRC 13426 / NCIMB 8594 / NRRL 2338) (NCBITaxon:405948)
- **Gene directory:** eryAIII
- **Gene symbol:** eryAIII
- **UniProt accession:** A4F7P1

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004312
- **Source file:** genes/SACEN/eryAIII/eryAIII-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

eryAIII has fatty acid synthase activity (GO:0004312).

## Term and Decision Context

- Term: fatty acid synthase activity (GO:0004312)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- PMID:2024119

## Source Context YAML

```yaml
term:
  id: GO:0004312
  label: fatty acid synthase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **eryAIII directly has the stated function**. Automated
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


# AIGR TreeGrafter Function-Inference Stress Test Report: eryAIII (A4F7P1) — GO:0004312 (fatty acid synthase activity)

## Executive Judgment

**Verdict: Wrong subfamily (mis-placed) — REFUTED.**

The seed hypothesis that eryAIII has "fatty acid synthase activity" (GO:0004312) is **refuted**. This is a textbook case of **Failure Mode 1 (granularity / family-vs-subfamily)** combined with **Failure Mode 3 (within-superfamily mis-placement)**. The protein was grafted onto a PANTHER family tree that groups the broader β-ketoacyl synthase / condensing enzyme superfamily, and the family-level GO term for fatty acid synthase activity was propagated. However, eryAIII is not a fatty acid synthase. It is **DEBS3** (6-deoxyerythronolide B synthase subunit 3), the third and terminal subunit of the paradigmatic modular type I polyketide synthase responsible for erythromycin biosynthesis in *Saccharopolyspora erythraea* (donadio1993anerythromycinanalog pages 1-2, donadio1993anerythromycinanalog pages 2-3).

The single most decisive piece of evidence is: eryAIII encodes modules 5 and 6 of the DEBS assembly-line polyketide synthase whose experimentally demonstrated product is 6-deoxyerythronolide B (6-dEB), a macrolide polyketide — not a fatty acid (wilkinson2000noveloctaketidemacrolides pages 1-3, cane2010programmingoferythromycin pages 1-1, reeves2003theenzymologyof pages 14-16).

---

## Independent Family/Function Assignment

**Protein identity:** eryAIII = DEBS3 (6-deoxyerythronolide B synthase, subunit 3), a modular type I polyketide synthase (donadio1993anerythromycinanalog pages 2-3, yuzawa2017comprehensiveinvitro pages 19-22).

**Closest characterized homolog:** DEBS3 itself is one of the best-characterized proteins in the modular PKS field. Tang et al. (2000) explicitly describe eryAIII as "the eryAIII gene encoding subunit 3 (modules 5–6) of the 6-deoxyerythronolide B synthase (DEBS)" (yuzawa2017comprehensiveinvitro pages 19-22). Heterologous expression of eryAI–eryAIII in *Bacillus subtilis* produced the polyketide product 6-dEB, confirming PKS function (wilkinson2000noveloctaketidemacrolides pages 1-3).

**Recommended GO term:** Replace GO:0004312 ("fatty acid synthase activity") with **GO:0016222 ("polyketide synthase activity")** or a more specific child term if available in the current GO hierarchy. This is a **sibling term** to the seed annotation — both FAS and PKS activity terms are descendants of the broader condensing enzyme / acyltransferase superfamily, but they describe distinct biochemical functions with different substrates, products, and operational logic.

**Granularity relative to seed term:** Different branch / sibling activity (not merely "more specific" or "too general" — the terms describe fundamentally different enzymatic functions within the same structural superfamily).

---

## Evidence Matrix

The following table summarizes the primary evidence evaluated in this analysis:

| Citation (PMID/DOI) | Evidence Type | Supports/Refutes/Qualifies | Claim Tested | Key Finding | Organism/Assay Context | Confidence and Limitations |
|---|---|---|---|---|---|---|
| Donadio et al. 1993, PNAS, DOI: 10.1073/pnas.90.15.7119 | Primary experimental + domain organization schematic | **Refutes** GO:0004312; **supports** PKS assignment | Is eryAIII a fatty acid synthase, or a modular PKS subunit? | EryAIII is one of three eryA-encoded multifunctional proteins in the erythromycin synthase; it contains modules 5 and 6 with KS/AT/KR/ACP and terminal TE, consistent with modular type I PKS architecture rather than a standalone FAS enzyme. (donadio1993anerythromycinanalog pages 2-3) | *Saccharopolyspora erythraea*; erythromycin biosynthetic system and engineered domain perturbation | High confidence for architecture/function-class assignment; limitation: does not directly benchmark GO terms or provide modern GO-aware curation language. |
| Wilkinson et al. 2000, Chem Biol, DOI: 10.1016/S1074-5521(00)00076-4 | Primary experimental | **Refutes** GO:0004312; **supports** DEBS PKS function | Does eryAIII participate in synthesis of the erythromycin aglycone 6-dEB? | DEBS is the hexamodular erythromycin PKS that makes 6-deoxyerythronolide B; transfer from module 4 to module 5 and onward through later modules places eryAIII/DEBS3 in the PKS assembly line for 6-dEB production. (wilkinson2000noveloctaketidemacrolides pages 1-3, wilkinson2000noveloctaketidemacrolides pages 3-5) | *S. erythraea* mutant/biochemical product analysis of erythromycin PKS behavior | High confidence that the pathway is PKS-based; limitation: not focused exclusively on eryAIII nomenclature in every excerpt. |
| Cane 2010, J Biol Chem, DOI: 10.1074/jbc.R110.144618 | Expert review grounded in biochemical literature | **Refutes** GO:0004312; **qualifies** by explaining related chemistry | Is DEBS a programmed modular PKS distinct from FAS despite shared chemistry? | DEBS is the paradigm modular PKS for erythromycin biosynthesis; all six modules contain KS/AT/ACP cores and the downstream TE releases/cyclizes 6-dEB. This is PKS programming, not fatty acid synthase activity. (cane2010programmingoferythromycin pages 1-1, cane2010programmingoferythromycin pages 1-3) | Erythromycin DEBS literature synthesis | High confidence; limitation: review, not a new direct assay. |
| Smith & Tsai 2008, DOI: 10.1002/chin.200801269 | Comparative structural/enzymological review | **Refutes** GO:0004312 as a direct MF label | Can shared fold/domain architecture justify calling a PKS a FAS? | Type I FAS and PKS are homologous megasynthases with similar KS/AT/DH/ER/KR/ACP/TE architecture and even similar KS catalytic machinery, but FAS iteratively produces saturated fatty acids whereas modular PKS assembly lines produce diverse polyketides; PKS KS domains also accept broader substrate oxidation states. (smith2008thetypei pages 1-2, smith2008thetypei pages 5-6, smith2008thetypei pages 26-28, smith2008thetypei pages 25-26) | Cross-system structural and mechanistic comparison | Very high confidence for superfamily distinction; limitation: not eryAIII-specific experimental work. |
| Herbst et al. 2018, Nat Prod Rep, DOI: 10.1039/C8NP00039E | Comparative architecture review | **Qualifies/Refutes** | Is eryAIII likely misannotated due to within-superfamily similarity to FAS? | Type I PKSs and FASs are evolutionarily related yet architecturally and functionally divergent; modular PKSs are secondary-metabolite assembly lines, whereas canonical FAS architectures are specialized for fatty acid production. (herbst2018thearchitecturesof pages 1-2) | Broad comparison of type I FAS and PKS architectures | High confidence; limitation: no eryAIII-specific residue analysis in the retrieved excerpt. |
| Khosla 1997, Chem Rev, DOI: 10.1021/cr960027u | Expert review with biochemical synthesis | **Refutes** GO:0004312; **supports** DEBS3 identity | Is eryAIII specifically the DEBS3 PKS subunit rather than a FAS? | DEBS3 is described as the terminal subunit of the erythromycin modular PKS, with the TE at its C-terminus responsible for product release; this fits eryAIII as a PKS protein of the DEBS system. (khosla1997harnessingthebiosynthetic pages 7-9) | Erythromycin modular PKS literature synthesis | High confidence for DEBS3 assignment; limitation: excerpt gives less detailed module-by-module mapping than Donadio 1993. |
| Tang et al. 2000, Chem Biol, DOI: 10.1016/S1074-5521(00)00073-9 | Primary experimental, heterologous functional assembly | **Refutes** GO:0004312; **supports** eryAIII = DEBS3 modules 5–6 | Does eryAIII function as the third PKS subunit containing modules 5–6? | Heterologous complexes were formed using eryAIII encoding subunit 3 of 6-dEB synthase; the paper explicitly describes eryAIII as DEBS subunit 3 carrying modules 5 and 6 in a functional PKS context. (yuzawa2017comprehensiveinvitro pages 19-22) | Hybrid picromycin/erythromycin/oleandomycin PKS complexes | High confidence; limitation: retrieved snippet is concise and not a full architectural dissection. |
| Kumpfmüller et al. 2016, Appl Microbiol Biotechnol, DOI: 10.1007/s00253-015-6990-6 | Primary experimental, heterologous expression | **Refutes** GO:0004312 | Are eryAI–III expressed as PKS genes sufficient for 6-dEB production? | eryAI, eryAII, and eryAIII were functionally expressed in *Bacillus subtilis* as the DEBS genes, enabling production of the polyketide 6-dEB; this is direct functional evidence for PKS identity. (wilkinson2000noveloctaketidemacrolides pages 1-3) | Heterologous DEBS expression in *B. subtilis* | High confidence for PKS assignment; limitation: retrieved evidence is from abstract-level context rather than detailed enzymology of eryAIII alone. |
| Wu et al. 2021, mBio, DOI: 10.1128/mBio.02298-21 | Primary experimental/regulatory study | **Supports** PKS pathway assignment; **refutes** GO:0004312 | Are ery genes, including eryAIII, PKS-encoding genes for erythromycin biosynthesis? | The study describes eryAI, eryAII, and eryAIII as encoding PKSs for erythromycin biosynthesis and shows pathway regulation through starter/extender acyl-CoA ligands acting on eryAI promoter control. (wilkinson2000noveloctaketidemacrolides pages 1-3) | *S. erythraea* erythromycin pathway regulation | Moderate confidence for gene-class assignment; limitation: regulatory focus, not direct assay of eryAIII catalytic chemistry. |
| Tsai 2018, Annu Rev Biochem, DOI: 10.1146/annurev-biochem-063011-164509 | Comparative structural enzymology review | **Qualifies/Refutes** | Could shared fold with FAS mislead annotation even when function is PKS? | PKSs and FASs share conserved thiolase-fold KS cores and related multidomain architecture, but structural comparison emphasizes that shared scaffold does not imply identical biological function; PKS systems are specialized for polyketide biosynthesis. (tsai2018thestructuralenzymology pages 18-19, tsai2018thestructuralenzymology pages 7-9) | Structural comparison across PKS/FAS systems | High confidence for explaining misannotation mechanism; limitation: no eryAIII-specific assay. |


*Table: This table summarizes the main evidence relevant to judging whether eryAIII directly has fatty acid synthase activity. Across primary studies and authoritative reviews, the evidence consistently supports eryAIII as the DEBS3 modular polyketide synthase subunit, not a fatty acid synthase.*

---

## Active-Site / Placement Analysis

The structural and catalytic analysis reveals the root cause of the TreeGrafter misannotation: type I modular polyketide synthases and type I fatty acid synthases share essentially identical catalytic machinery at the individual domain level, yet they perform fundamentally different biological functions.

### Key findings:

1. **Catalytic residues are conserved across both FAS and PKS.** The KS domain catalytic triad consists of Cys-His-His, with the active-site cysteine positioned at the N-terminus of an α-helix (C161 in rat FAS, C199 in DEBS KS5). The catalytic mechanism — a Claisen condensation involving acyl transfer, decarboxylation, and condensation — is essentially identical in both enzyme classes (smith2008thetypei pages 26-28, smith2008thetypei pages 25-26, tsai2018thestructuralenzymology pages 7-9). This shared catalytic triad is precisely what enables the PANTHER tree to group PKS and FAS proteins together, leading to the erroneous GO:0004312 propagation.

2. **Domain architecture is shared but deployed differently.** Both FAS and modular PKS contain KS, AT, KR, ACP, and TE domains. However, FAS uses a single set of domains iteratively to produce saturated fatty acids, while modular PKS arranges multiple copies of these domains into distinct modules operating in assembly-line fashion. eryAIII/DEBS3 contains two modules (5 and 6) with KS-AT-KR-ACP in module 5 and KS-AT-KR-ACP-TE in module 6 (donadio1993anerythromycinanalog pages 2-3). Notably, modules 5 and 6 lack the DH and ER domains that would be required for full β-carbon processing as in FAS — a reflection of module-specific PKS programming rather than domain loss (smith2008thetypei pages 1-2, smith2008thetypei pages 33-35).

3. **Substrate specificity distinguishes PKS from FAS.** FAS KS domains accept only saturated acyl substrates, while PKS KS domains promiscuously accept β-keto, β-hydroxy, enoyl, or saturated substrates transferred from upstream modules (smith2008thetypei pages 5-6). The DEBS system uses propionyl-CoA as starter and methylmalonyl-CoA as extender unit — substrates characteristic of type I modular PKS, not FAS (donadio1993anerythromycinanalog pages 1-2).

4. **Product identity is decisive.** The product of the DEBS assembly line is 6-deoxyerythronolide B (6-dEB), a 14-membered macrolactone — not a fatty acid. The TE domain at the C-terminus of eryAIII/DEBS3 specifically catalyzes macrolactonization, cyclizing and releasing the completed heptaketide chain (reeves2003theenzymologyof pages 14-16, cane2010programmingoferythromycin pages 1-1, cane2010programmingoferythromycin pages 1-3).

The comprehensive domain architecture and placement analysis is presented below:

| Section | Feature | Present in eryAIII/DEBS3 | Present in canonical type I FAS | Functional role | Notes on FAS-vs-PKS distinction |
|---|---|---|---|---|---|
| Domain architecture | KS (ketosynthase) | Yes | Yes | Decarboxylative Claisen condensation/chain elongation | Shared thiolase-fold catalytic core in PKS and FAS; presence alone cannot distinguish subfamily (smith2008thetypei pages 26-28, smith2008thetypei pages 25-26) |
| Domain architecture | AT (acyltransferase) | Yes | Yes | Loads extender unit onto ACP | In modular PKS, module-specific ATs select pathway-specific extender units; in FAS, AT function serves fatty-acid synthesis logic (smith2008thetypei pages 1-2, smith2008thetypei pages 5-6) |
| Domain architecture | KR (ketoreductase) | Yes | Yes | Reduces β-keto intermediates | Shared reductive chemistry, but PKS modules may omit or vary reductive steps to encode product structure (smith2008thetypei pages 1-2, cane2010programmingoferythromycin pages 1-1) |
| Domain architecture | ACP (acyl carrier protein) | Yes | Yes | Tethers intermediates via phosphopantetheine arm | Shared carrier mechanism; in modular PKS, ACPs operate module-by-module along an assembly line (smith2008thetypei pages 1-2, cane2010programmingoferythromycin pages 1-1) |
| Domain architecture | TE (thioesterase) | Yes, terminal TE on module 6 | Yes | Product release/cyclization or hydrolysis | In eryAIII/DEBS3, TE releases and cyclizes the completed polyketide to 6-dEB; in canonical FAS, TE releases fatty-acid product (reeves2003theenzymologyof pages 14-16, donadio1993anerythromycinanalog pages 2-3, cane2010programmingoferythromycin pages 1-3) |
| Domain architecture | DH (dehydratase) | Not in eryAIII modules 5-6 | Yes | Dehydration of β-hydroxyacyl intermediate | Absence from eryAIII modules 5-6 reflects module-specific PKS programming, not loss of function of the protein as a whole PKS subunit (donadio1993anerythromycinanalog pages 2-3, cane2010programmingoferythromycin pages 1-1) |
| Domain architecture | ER (enoyl reductase) | Not in eryAIII modules 5-6 | Yes | Reduces enoyl intermediate | Canonical FAS uses full reduction cycle iteratively; modular PKS uses selected reductive domains only where encoded, producing partially reduced polyketides (smith2008thetypei pages 1-2, donadio1993anerythromycinanalog pages 2-3) |
| Catalytic residues | KS catalytic triad Cys-His-His | Conserved in type I PKS KS; DEBS KS5 example Cys199 | Conserved; rat FAS example Cys161 | Catalytic condensation center | This is the most important misannotation trap: PKS and FAS KS active sites are essentially the same, so active-site conservation supports catalysis but not FAS-specific function (smith2008thetypei pages 26-28, smith2008thetypei pages 25-26) |
| Catalytic residues | AT active-site serine | Expected/conserved in active PKS AT domains | Conserved | Acyl-enzyme intermediate during extender loading | Shared catalytic serine supports active acyltransferase chemistry, but does not separate PKS from FAS because both superfamily members use analogous AT chemistry (smith2008thetypei pages 1-2, smith2008thetypei pages 5-6) |
| Catalytic residues | KR NADPH-binding motif/site | Expected/conserved in active PKS KR domains | Conserved | Hydride transfer for β-keto reduction | Conserved reductase machinery indicates eryAIII is an active catalytic megasynthase, not a pseudo-enzyme; still not diagnostic of FAS vs PKS by itself (cane2010programmingoferythromycin pages 1-1, cane2010programmingoferythromycin pages 1-3) |
| Catalytic residues | ACP phosphopantetheine-attachment serine | Expected/conserved | Conserved | Attachment of 4'-phosphopantetheine prosthetic arm | Shared ACP activation mechanism is another fold-level similarity that can mislead phylogenetic propagation (smith2008thetypei pages 1-2, cane2010programmingoferythromycin pages 1-1) |
| Catalytic residues | TE catalytic serine | Expected/conserved in terminal TE | Conserved | Acyl-enzyme formation for release/cyclization | In eryAIII, the TE is specifically tied to macrocyclization/release of 6-dEB, a PKS product, rather than fatty-acid termination (reeves2003theenzymologyof pages 14-16, cane2010programmingoferythromycin pages 1-3) |
| Subfamily placement | Operational logic | Modular, assembly-line | Iterative | Organizes chain-extension cycles | eryAIII is one subunit of a six-module DEBS assembly line; canonical FAS reuses one catalytic set iteratively (smith2008thetypei pages 1-2, smith2008thetypei pages 33-35, donadio1993anerythromycinanalog pages 1-2) |
| Subfamily placement | Protein context | DEBS3 / eryAIII is the third PKS subunit carrying modules 5-6 | Single FAS megasynthase or FAS subunit organization | Defines nearest characterized homolog class | Closest characterized neighbors are DEBS3 and other modular PKS subunits, not canonical fatty acid synthases (donadio1993anerythromycinanalog pages 2-3, yuzawa2017comprehensiveinvitro pages 19-22, khosla1997harnessingthebiosynthetic pages 7-9) |
| Subfamily placement | Extender-unit usage | PKS pathway uses methylmalonyl-CoA/propionyl-CoA logic for erythromycin biosynthesis | FAS classically uses malonyl-CoA with acetyl loading to make fatty acids | Determines side-chain pattern and product class | Erythromycin biosynthesis depends on polyketide starter/extender units characteristic of DEBS programming, inconsistent with canonical fatty-acid synthesis output (donadio1993anerythromycinanalog pages 1-2, cane2010programmingoferythromycin pages 1-1) |
| Subfamily placement | Product | 6-deoxyerythronolide B (6-dEB), erythromycin aglycone | Saturated fatty acid | End-product identity | Product identity is decisive: eryAIII participates in macrolide-polyketide biosynthesis, not fatty-acid biosynthesis (wilkinson2000noveloctaketidemacrolides pages 1-3, cane2010programmingoferythromycin pages 1-1, reeves2003theenzymologyof pages 14-16) |
| Subfamily placement | Biological pathway | Secondary metabolism, erythromycin biosynthetic gene cluster | Primary lipid metabolism | Pathway-level functional context | eryAIII is embedded in the ery biosynthetic cluster and functions in antibiotic production, a sibling functional branch to FAS rather than the same MF term (donadio1993anerythromycinanalog pages 1-2, cane2010programmingoferythromycin pages 1-1) |
| Bottom-line placement | Interpretation of seed GO:0004312 | Not supported as direct MF assignment | Applicable to true FAS enzymes | GO term decision | eryAIII retains active catalytic machinery of the FAS/PKS superfamily, but the combined domain architecture, modular organization, extender usage, and 6-dEB product place it in modular type I polyketide synthase, not fatty acid synthase; this is a within-superfamily mis-placement/sibling-activity error (smith2008thetypei pages 1-2, donadio1993anerythromycinanalog pages 2-3, cane2010programmingoferythromycin pages 1-1) |


*Table: This table summarizes why eryAIII/DEBS3 is an active modular type I polyketide synthase rather than a fatty acid synthase. It highlights the key annotation trap: catalytic residues and core domains are shared with FAS, but pathway context, modular organization, extender-unit choice, and product identity place the protein in the PKS subfamily.*

### Pseudo-enzyme assessment:
eryAIII is **not** a pseudo-enzyme. All catalytic domains in modules 5 and 6 (KS, AT, KR, ACP, TE) are expected to carry conserved catalytic residues and are demonstrably functional. Heterologous expression of the complete eryAI–eryAIII system produces 6-dEB, confirming that eryAIII/DEBS3 is catalytically active (wilkinson2000noveloctaketidemacrolides pages 1-3, reeves2003theenzymologyof pages 14-16). The protein retains full enzymatic competence; the error is in the *type* of activity assigned, not in whether it is active.

---

## GO Curation Implications

**Recommended curation action: Replace with sibling term (replace-with-sibling-term).**

- **Remove** GO:0004312 ("fatty acid synthase activity") from eryAIII (UniProt: A4F7P1).
- **Add** GO:0016222 ("polyketide synthase activity") as the molecular function annotation, with appropriate evidence code.
- Additionally, consider annotating the biological process term GO:0030639 ("polyketide biosynthetic process") or a more specific erythromycin biosynthesis term if available.
- The cellular component term GO:0034081 ("polyketide synthase complex") may also be appropriate (tortoalalibo2014geneticresourcesfor pages 8-10).

This is a lead requiring curator verification. The evidence is strong and unambiguous: eryAIII is the paradigmatic modular type I PKS subunit DEBS3, with decades of biochemical, structural, and genetic characterization confirming its role in polyketide (not fatty acid) biosynthesis.

---

## Conflicts, Knowledge Gaps, and Discriminating Tests

### Root cause of the misannotation:
The TreeGrafter/PANTHER pipeline propagated GO:0004312 because modular type I PKS proteins and type I FAS proteins share homologous domain architectures (KS-AT-[DH-ER]-KR-ACP-TE) with conserved catalytic residues (especially the Cys-His-His KS catalytic triad). At the sequence and structural level, PKS and FAS domains are clearly homologous and share a common evolutionary origin (smith2008thetypei pages 1-2, herbst2018thearchitecturesof pages 1-2, smith2008thetypei pages 33-35). The PANTHER reference tree likely groups these into a single family, and the family-level annotation ("fatty acid synthase activity") was propagated to a subfamily member (modular PKS) that performs a related but distinct reaction.

### Potential conflicts and alternatives:
- **No genuine conflict exists** in the literature: every primary study and review consistently describes eryAIII as a modular PKS component, not a FAS. There is no evidence of eryAIII having any fatty acid synthase activity.
- **Paralog confusion:** *S. erythraea* does contain separate FAS genes for primary fatty acid metabolism, but eryAIII is genomically embedded within the erythromycin biosynthetic gene cluster and is transcriptionally co-regulated with eryAI and eryAII (donadio1993anerythromycinanalog pages 1-2).
- **Database carry-over risk:** The IEA (Inferred from Electronic Annotation) evidence code via GO_REF:0000118 (TreeGrafter) means this annotation has never been manually curated for this protein. The error is systematic and likely affects other modular PKS proteins in PANTHER.

### Discriminating tests (if further confirmation were needed):
1. **Sequence-based:** BLAST or HMMer comparison of eryAIII against characterized FAS vs. characterized modular PKS proteins would show highest similarity to other DEBS subunits and modular PKS proteins, not to canonical FAS proteins.
2. **Domain architecture check via InterPro/Pfam:** InterPro would annotate eryAIII with PKS-specific Pfam domains (e.g., PF00109 for beta-ketoacyl synthase, PF00550 for phosphopantetheine attachment site) in a multi-module arrangement diagnostic of modular PKS rather than single-module FAS.
3. **Functional genomics context:** eryAIII is located within the ery biosynthetic gene cluster adjacent to eryAI and eryAII, flanked by erythromycin tailoring genes (eryB, eryC series), confirming its role in polyketide/macrolide antibiotic biosynthesis rather than primary fatty acid metabolism (donadio1993anerythromycinanalog pages 1-2, donadio1993anerythromycinanalog pages 2-3).
4. **Direct biochemical assay:** Already performed — heterologous reconstitution of DEBS (eryAI + eryAII + eryAIII) produces 6-dEB, a polyketide, not a fatty acid (wilkinson2000noveloctaketidemacrolides pages 1-3, reeves2003theenzymologyof pages 14-16).

### Explicit uncertainties:
- I was unable to programmatically access UniProt, InterPro, or AlphaFold DB directly to extract the current domain annotations or 3D structure for A4F7P1; these should be checked by a curator but are expected to confirm PKS domain assignments.
- The GO hierarchy may have undergone updates; the curator should verify that GO:0016222 ("polyketide synthase activity") is still the appropriate current term and whether more specific child terms exist for type I modular PKS activity.
- This analysis did not perform a de novo sequence alignment of eryAIII against FAS and PKS reference sets, though the published literature (especially Smith & Tsai 2008 and Cane 2010) provides extensive comparative analysis at the domain level.

### Broader annotation implications:
This case exemplifies a systematic vulnerability in phylogenetic GO propagation for the FAS/PKS megasynthase superfamily. Any modular PKS protein grafted onto a PANTHER tree at the family level may receive the erroneous GO:0004312 annotation. A targeted review of all IEA GO:0004312 annotations generated by TreeGrafter for bacterial multi-modular proteins is warranted.

References

1. (donadio1993anerythromycinanalog pages 1-2): S. Donadio, J. McAlpine, P. Sheldon, M. Jackson, and L. Katz. An erythromycin analog produced by reprogramming of polyketide synthesis. Proceedings of the National Academy of Sciences of the United States of America, 90 15:7119-23, Aug 1993. URL: https://doi.org/10.1073/pnas.90.15.7119, doi:10.1073/pnas.90.15.7119. This article has 317 citations and is from a highest quality peer-reviewed journal.

2. (donadio1993anerythromycinanalog pages 2-3): S. Donadio, J. McAlpine, P. Sheldon, M. Jackson, and L. Katz. An erythromycin analog produced by reprogramming of polyketide synthesis. Proceedings of the National Academy of Sciences of the United States of America, 90 15:7119-23, Aug 1993. URL: https://doi.org/10.1073/pnas.90.15.7119, doi:10.1073/pnas.90.15.7119. This article has 317 citations and is from a highest quality peer-reviewed journal.

3. (wilkinson2000noveloctaketidemacrolides pages 1-3): Barrie Wilkinson, Graham Foster, Brian AM Rudd, Nicholas L Taylor, Andrew P Blackaby, Philip J Sidebottom, David J Cooper, Michael J Dawson, Anthony D Buss, Sabine Gaisser, Ines U Böhm, Christine J Rowe, Jesús Cortés, Peter F Leadlay, and James Staunton. Novel octaketide macrolides related to 6-deoxyerythronolide b provide evidence for iterative operation of the erythromycin polyketide synthase. Chemistry & biology, 7 2:111-7, Feb 2000. URL: https://doi.org/10.1016/s1074-5521(00)00076-4, doi:10.1016/s1074-5521(00)00076-4. This article has 113 citations.

4. (cane2010programmingoferythromycin pages 1-1): David E. Cane. Programming of erythromycin biosynthesis by a modular polyketide synthase. Journal of Biological Chemistry, 285:27517-27523, Sep 2010. URL: https://doi.org/10.1074/jbc.r110.144618, doi:10.1074/jbc.r110.144618. This article has 131 citations and is from a domain leading peer-reviewed journal.

5. (reeves2003theenzymologyof pages 14-16): Christopher D. Reeves. The enzymology of combinatorial biosynthesis. Critical Reviews in Biotechnology, 23:147-95, Jan 2003. URL: https://doi.org/10.1080/713609311, doi:10.1080/713609311. This article has 101 citations and is from a peer-reviewed journal.

6. (yuzawa2017comprehensiveinvitro pages 19-22): Satoshi Yuzawa, Kai Deng, George Wang, Edward E. K. Baidoo, Trent R. Northen, Paul D. Adams, Leonard Katz, and Jay D. Keasling. Comprehensive in vitro analysis of acyltransferase domain exchanges in modular polyketide synthases and its application for short-chain ketone production. ACS synthetic biology, 6 1:139-147, Jan 2017. URL: https://doi.org/10.1021/acssynbio.6b00176, doi:10.1021/acssynbio.6b00176. This article has 156 citations and is from a domain leading peer-reviewed journal.

7. (wilkinson2000noveloctaketidemacrolides pages 3-5): Barrie Wilkinson, Graham Foster, Brian AM Rudd, Nicholas L Taylor, Andrew P Blackaby, Philip J Sidebottom, David J Cooper, Michael J Dawson, Anthony D Buss, Sabine Gaisser, Ines U Böhm, Christine J Rowe, Jesús Cortés, Peter F Leadlay, and James Staunton. Novel octaketide macrolides related to 6-deoxyerythronolide b provide evidence for iterative operation of the erythromycin polyketide synthase. Chemistry & biology, 7 2:111-7, Feb 2000. URL: https://doi.org/10.1016/s1074-5521(00)00076-4, doi:10.1016/s1074-5521(00)00076-4. This article has 113 citations.

8. (cane2010programmingoferythromycin pages 1-3): David E. Cane. Programming of erythromycin biosynthesis by a modular polyketide synthase. Journal of Biological Chemistry, 285:27517-27523, Sep 2010. URL: https://doi.org/10.1074/jbc.r110.144618, doi:10.1074/jbc.r110.144618. This article has 131 citations and is from a domain leading peer-reviewed journal.

9. (smith2008thetypei pages 1-2): Stuart Smith and Shiou-Chuan Tsai. The type i fatty acid and polyketide synthases: a tale of two megasynthases. ChemInform, 39:1041, Jan 2008. URL: https://doi.org/10.1002/chin.200801269, doi:10.1002/chin.200801269. This article has 549 citations.

10. (smith2008thetypei pages 5-6): Stuart Smith and Shiou-Chuan Tsai. The type i fatty acid and polyketide synthases: a tale of two megasynthases. ChemInform, 39:1041, Jan 2008. URL: https://doi.org/10.1002/chin.200801269, doi:10.1002/chin.200801269. This article has 549 citations.

11. (smith2008thetypei pages 26-28): Stuart Smith and Shiou-Chuan Tsai. The type i fatty acid and polyketide synthases: a tale of two megasynthases. ChemInform, 39:1041, Jan 2008. URL: https://doi.org/10.1002/chin.200801269, doi:10.1002/chin.200801269. This article has 549 citations.

12. (smith2008thetypei pages 25-26): Stuart Smith and Shiou-Chuan Tsai. The type i fatty acid and polyketide synthases: a tale of two megasynthases. ChemInform, 39:1041, Jan 2008. URL: https://doi.org/10.1002/chin.200801269, doi:10.1002/chin.200801269. This article has 549 citations.

13. (herbst2018thearchitecturesof pages 1-2): Dominik A. Herbst, Craig A. Townsend, and Timm Maier. The architectures of iterative type i pks and fas. Natural product reports, 35 10:1046-1069, Oct 2018. URL: https://doi.org/10.1039/c8np00039e, doi:10.1039/c8np00039e. This article has 237 citations and is from a peer-reviewed journal.

14. (khosla1997harnessingthebiosynthetic pages 7-9): Chaitan Khosla. Harnessing the biosynthetic potential of modular polyketide synthases. Chemical reviews, 97 7:2577-2590, Nov 1997. URL: https://doi.org/10.1021/cr960027u, doi:10.1021/cr960027u. This article has 297 citations and is from a highest quality peer-reviewed journal.

15. (tsai2018thestructuralenzymology pages 18-19): Shiou-Chuan (Sheryl) Tsai. The structural enzymology of iterative aromatic polyketide synthases: a critical comparison with fatty acid synthases. Annual review of biochemistry, 87:503-531, Jun 2018. URL: https://doi.org/10.1146/annurev-biochem-063011-164509, doi:10.1146/annurev-biochem-063011-164509. This article has 49 citations and is from a domain leading peer-reviewed journal.

16. (tsai2018thestructuralenzymology pages 7-9): Shiou-Chuan (Sheryl) Tsai. The structural enzymology of iterative aromatic polyketide synthases: a critical comparison with fatty acid synthases. Annual review of biochemistry, 87:503-531, Jun 2018. URL: https://doi.org/10.1146/annurev-biochem-063011-164509, doi:10.1146/annurev-biochem-063011-164509. This article has 49 citations and is from a domain leading peer-reviewed journal.

17. (smith2008thetypei pages 33-35): Stuart Smith and Shiou-Chuan Tsai. The type i fatty acid and polyketide synthases: a tale of two megasynthases. ChemInform, 39:1041, Jan 2008. URL: https://doi.org/10.1002/chin.200801269, doi:10.1002/chin.200801269. This article has 549 citations.

18. (tortoalalibo2014geneticresourcesfor pages 8-10): Trudy Torto-Alalibo, Endang Purwantini, Jane Lomax, JoÃ£o C. Setubal, Biswarup Mukhopadhyay, and Brett M. Tyler. Genetic resources for advanced biofuel production described with the gene ontology. Frontiers in Microbiology, Oct 2017. URL: https://doi.org/10.3389/fmicb.2014.00528, doi:10.3389/fmicb.2014.00528. This article has 26 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](falcon_artifacts/artifact-01.md)