---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:47:50.870327'
end_time: '2026-06-24T05:08:40.429747'
duration_seconds: 1249.56
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: ahpC
  gene_symbol: ahpC
  uniprot_accession: Q88K52
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440)
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0008379
  hypothesis_text: ahpC has thioredoxin peroxidase activity (GO:0008379).
  term_context: '- Term: thioredoxin peroxidase activity (GO:0008379)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - PMID:12483614

    - file:PSEPK/ahpC/ahpC-deep-research-falcon.md'
  source_file: genes/PSEPK/ahpC/ahpC-ai-review.yaml
  source_selector: existing_annotations[5].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0008379\n  label: thioredoxin peroxidase activity\n\
    evidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
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


# Function-Inference Stress Test Report: *P. putida* ahpC (Q88K52) — GO:0008379 (thioredoxin peroxidase activity)

---

## Executive Judgment

**Verdict: Partially supported / too general — sibling-term error (Failure Mode 1: granularity / family-vs-subfamily)**

The seed hypothesis that *P. putida* AhpC (Q88K52) has **thioredoxin peroxidase activity (GO:0008379)** is **partially supported but names the wrong electron donor**. The protein is unambiguously an active peroxiredoxin of the Prx1/AhpC (typical 2-Cys) subfamily with fully conserved catalytic residues. However, GO:0008379 explicitly specifies thioredoxin as the electron donor, whereas in *P. putida* the physiological reductant is AhpF, a dedicated NADH:peroxiredoxin oxidoreductase co-transcribed with AhpC in an operon (fukumori2001molecularcloningand pages 4-6, fukumori2001molecularcloningand pages 1-3, kim2014oxidativestressresponse pages 5-6). The peroxiredoxin field explicitly renamed the family from "thioredoxin peroxidase" to "peroxiredoxin" precisely because not all members use thioredoxin (yang2025insectperoxiredoxinsa pages 2-4, rhee2016overviewonperoxiredoxin pages 1-2). This represents a **granularity/sibling-term error** characteristic of TreeGrafter Failure Mode 1: the family-level PANTHER node likely carries a GO term appropriate for the thioredoxin-dependent subfamily members (e.g., mycobacterial AhpC or *T. pallidum* AhpC), but incorrectly propagated it to an AhpF-dependent classical AhpC.

**Most decisive evidence:** *P. putida* ahpC and ahpF are co-transcribed in an operon (PP_2439/PP_2440), both are co-induced >70-fold under H₂O₂ stress under OxyR regulation, and AhpF is described as the dedicated peroxiredoxin reductase in this organism (bojanovic2017globaltranscriptionalresponses pages 10-11, fukumori2001molecularcloningand pages 4-6, hishinuma2008oxyrisinvolved pages 1-2). This AhpC–AhpF partnership is the hallmark of the classical alkyl hydroperoxide reductase system, not a thioredoxin-dependent peroxidase system.

---

## Independent Family/Function Assignment

**Most likely specific molecular function:** Peroxiredoxin activity (GO:0051920), specifically alkyl hydroperoxide reductase activity operating in the AhpC–AhpF two-component system.

**Characterized homolog basis:** *Salmonella typhimurium* AhpC (P0A251), 69% sequence identity, with biochemically established catalytic mechanism (Ellis & Poole, 1997) (ellis1997rolesforthe pages 4-5, ellis1997rolesforthe pages 1-2). The *P. putida* AhpC has been directly cloned and shown to confer organic hydroperoxide resistance upon overexpression (fukumori2001molecularcloningand pages 4-6, fukumori2001molecularcloningand pages 6-8).

**Recommended GO term:** GO:0051920 (peroxiredoxin activity) — this is a **parent/more general** term relative to the seed term GO:0008379 and does not incorrectly specify the electron donor.

**Granularity relative to seed term:** The recommended term is **more general** (parent term). The seed term GO:0008379 is a sibling that specifies the wrong electron donor for this classical AhpCF system.

---

## Evidence Matrix

The following table compiles the evidence assessed for this analysis:

| Citation | Evidence Type | Supports/Refutes/Qualifies | Claim Tested | Key Finding | Organism/Assay Context | Confidence & Limitations |
|---|---|---|---|---|---|---|
| Fukumori & Kishii 2001 (fukumori2001molecularcloningand pages 4-6, fukumori2001molecularcloningand pages 6-8, fukumori2001molecularcloningand pages 1-3) | Direct molecular/genetic characterization | Qualifies | Does P. putida AhpC directly function as a peroxiredoxin, and what reductant system is it paired with? | P. putida ahpC and ahpF are co-transcribed in an operon; AhpC is a 186 aa/24 kDa AhpC-family peroxiredoxin with conserved catalytic cysteines at positions 47 and 166; AhpC overexpression increases resistance to organic hydroperoxide (BHP); AhpF regenerates oxidized AhpC. | P. putida KT2442/KT2440 cloning, transcription mapping, heterologous expression in E. coli, peroxide-resistance assays. | High for AhpC/AhpF partnership and peroxide-defense role in P. putida; limitation: no purified-enzyme kinetic assay directly testing thioredoxin vs AhpF as reductant in P. putida. |
| Hishinuma et al. 2008 (hishinuma2008oxyrisinvolved pages 1-2) | Regulatory/proteomic study | Qualifies | Is AhpC part of the classical OxyR-controlled peroxide defense system in P. putida, and how does this relate to thioredoxin? | OxyR regulates AhpC, AhpF, KatA, KatB, and also affects TrxB; AhpF is explicitly described as the peroxiredoxin reductase increased with AhpC. This supports an AhpC-AhpF antioxidant module distinct from generic thioredoxin dependence. | P. putida KT2442 proteome and transcriptional analysis under oxidative stress. | High for regulatory linkage; limitation: indirect for catalytic electron donor specificity. |
| Bojanovic et al. 2017 (bojanovic2017globaltranscriptionalresponses pages 10-11) | Transcriptomics | Qualifies | Are ahpC and ahpF co-induced under peroxide stress in P. putida? | Under H2O2 stress, ahpC (PP_2439) and ahpF (PP_2440) are both strongly induced, with ahpF showing very large early induction, consistent with a coupled AhpCF peroxide-defense system. | P. putida KT2440 RNA-seq / transcriptional profiling under H2O2 stress. | High for stress-responsive co-expression; limitation: transcript data do not by themselves prove enzymatic donor usage. |
| Ellis & Poole 1997 (ellis1997rolesforthe pages 4-5, ellis1997rolesforthe pages 1-2, ellis1997rolesforthe pages 8-8) | Direct biochemical mutagenesis | Supports | Are the catalytic residues required for active AhpC peroxiredase function conserved in the query protein? | In S. typhimurium AhpC, Cys46 is the essential peroxidatic cysteine and Cys165 the resolving cysteine; mutagenesis established both as central to catalysis. P. putida AhpC conserves the corresponding residues as Cys47/Cys166. | Purified S. typhimurium AhpC mutants; peroxide-reduction biochemistry. | High for catalytic mechanism and residue assignment; limitation: assay is in homolog, not the P. putida protein itself. |
| Poole et al. 2000 (poole2000ahpfandother pages 3-4, poole2000ahpfandother pages 4-5, poole2000ahpfandother pages 1-2, poole2000ahpfandother pages 2-3) | Biochemical/mechanistic review and assay synthesis | Refutes | Is classical AhpC best described as a thioredoxin peroxidase? | Classical bacterial AhpC is reduced by AhpF, a dedicated NADH:peroxiredoxin oxidoreductase whose N-terminal thioredoxin-like redox center directly reduces AhpC. This argues that AhpC in AhpCF systems is not best annotated with a term that explicitly names thioredoxin as donor. | Bacterial AhpF/AhpC systems, especially Salmonella and related species. | High for classical AhpCF systems; limitation: not P. putida-specific, though P. putida has the same ahpCF organization. |
| Wong et al. 2017 (wong2017ahpcofthe pages 11-12) | Direct biochemical/structural characterization | Competing | Can some AhpC proteins truly have thioredoxin peroxidase activity? | Mycobacterial AhpC uses thioredoxin-C as a reducing partner; catalytic cysteines are typical of AhpC-family proteins, but reductant usage differs from classical AhpF-dependent systems. | Mycobacterium bovis/BCG structural and partner-interaction studies. | High for this lineage; limitation: demonstrates subfamily plasticity rather than P. putida function. |
| Parsonage et al. 2010 (parsonage2010broadspecificityahpclike pages 2-3) | Direct biochemical characterization | Competing | Can AhpC-like proteins be thioredoxin-dependent when AhpF is absent? | T. pallidum AhpC-like peroxiredoxin uses thioredoxin as electron donor in an organism lacking the usual AhpF partner. This validates GO:0008379 for some AhpC-like proteins but also shows donor usage is context-dependent. | T. pallidum purified antioxidant system biochemistry. | High for thioredoxin-dependent AhpC-like enzymes; limitation: exceptional genomic context, unlike P. putida which encodes ahpF. |
| Zhang et al. 2019 (zhang2019molecularmechanismsof pages 4-5, zhang2019molecularmechanismsof pages 5-7) | Direct biochemical characterization | Competing/Qualifies | Can AhpC use multiple reductants, and is thioredoxin always primary? | B. thailandensis AhpC can be reduced by both AhpD and thioredoxin, but AhpD shows higher catalytic efficiency. This demonstrates that thioredoxin compatibility does not mean thioredoxin is the physiologically preferred reductant. | Purified B. thailandensis AhpC with kinetic comparison of AhpD vs TrxC. | High; limitation: species-specific, but highly informative for interpreting donor-specific GO terms. |
| Gretes et al. 2012 (gretes2012peroxiredoxinsinparasites. pages 2-4, gretes2012peroxiredoxinsinparasites. pages 1-2) | Evolutionary/structural classification | Supports | Is the query correctly placed within the AhpC/Prx1 typical 2-Cys peroxiredoxin family? | AhpC belongs to the Prx1/AhpC subfamily of typical 2-Cys peroxiredoxins. This supports the general peroxiredoxin assignment and argues against misplacement into another peroxiredoxin subfamily. | Cross-species Prx classification/review. | High for family placement; limitation: does not specify donor usage for the P. putida enzyme. |
| Rhee 2016; Yang et al. 2025 (yang2025insectperoxiredoxinsa pages 2-4, rhee2016overviewonperoxiredoxin pages 1-2) | Authoritative review/nomenclature history | Refutes/Qualifies | Does the label “thioredoxin peroxidase” generally fit all peroxiredoxins/AhpCs? | “Thioredoxin peroxidase/TPx” was an early name, but the family was renamed “peroxiredoxin” because not all members use thioredoxin as electron donor. This directly cautions against assigning thioredoxin-specific MF terms solely from family membership. | Broad peroxiredoxin nomenclature and mechanistic reviews. | Moderate-high; limitation: not experimental on P. putida, but directly relevant to GO term granularity. |


*Table: This table summarizes the key experimental, mechanistic, and evolutionary evidence used to assess whether Pseudomonas putida AhpC (Q88K52) directly has GO:0008379 thioredoxin peroxidase activity. It is useful for separating the supported peroxiredoxin function from the likely incorrect donor-specific assignment to thioredoxin rather than AhpF.*

---

## Active-Site / Placement Analysis

The active-site conservation and subfamily placement analysis is summarized below:

| Residue Position in *P. putida* AhpC | Equivalent Position in *S. typhimurium* AhpC (P0A251) | Equivalent Position in *B. thailandensis* AhpC | Equivalent Position in *M. bovis* AhpC | Role/Function | Conservation Status | Note |
|---|---|---|---|---|---|---|
| Cys47 | Cys46 | Cys57 | Cys61 | Peroxidatic cysteine (CP); attacks peroxide substrate to form sulfenic acid intermediate | CONSERVED | Essential catalytic cysteine of typical 2-Cys AhpC/Prx1 enzymes; directly matches experimentally defined CP residues in characterized homologs (ellis1997rolesforthe pages 4-5, ellis1997rolesforthe pages 1-2, wong2017ahpcofthe pages 11-12, zhang2019molecularmechanismsof pages 5-7, fukumori2001molecularcloningand pages 4-6) |
| Cys166 | Cys165 | Cys171 plus nearby Cys173 in *B. thailandensis* | Cys174 | Resolving cysteine (CR); condenses with oxidized CP to form catalytic disulfide | CONSERVED | Matches experimentally defined resolving cysteine position of active AhpC homologs; *B. thailandensis* has an extra resolving-region cysteine but retains the same AhpC catalytic logic (ellis1997rolesforthe pages 4-5, wong2017ahpcofthe pages 11-12, zhang2019molecularmechanismsof pages 5-7, fukumori2001molecularcloningand pages 4-6) |
| Thr/Pro motif around Cys47 | Thr/Pro motif around Cys46 | Thr/Pro motif around Cys57 | Thr/Pro motif around Cys61 | Canonical active-site environment of Prx1/AhpC typical 2-Cys peroxiredoxins; supports CP reactivity and family placement | CONSERVED | Preserved catalytic-region architecture supports placement in the Prx1/AhpC typical 2-Cys subfamily (gretes2012peroxiredoxinsinparasites. pages 2-4, parsonage2010broadspecificityahpclike pages 2-3, fukumori2001molecularcloningand pages 4-6) |
| Overall sequence relationship | 69 percent identity to *S. typhimurium* AhpC | Conserved AhpC-family architecture | Conserved AhpC-family architecture | Nearest characterized-function placement | CONSERVED FAMILY CORE | High identity to classical AhpC, plus conserved catalytic cysteines, supports assignment to active AhpC/peroxiredoxin rather than another Prx subfamily; P. putida AhpC also shows 65 percent identity to *P. aeruginosa* and 65 percent similarity to *A. xylanus* AhpC homologs (fukumori2001molecularcloningand pages 4-6) |
| Subfamily placement | AhpC / Prx1 | AhpC / Prx1 | AhpC / Prx1 | Typical 2-Cys peroxiredoxin subfamily assignment | CONSERVED | No evidence for mis-placement into Prx5, Prx6, Tpx, or other neighboring peroxiredoxin subfamilies (gretes2012peroxiredoxinsinparasites. pages 2-4, parsonage2010broadspecificityahpclike pages 2-3, gretes2012peroxiredoxinsinparasites. pages 1-2) |
| Genomic and electron-donor context | ahpC-ahpF operon in classical AhpCF arrangement | AhpC reduced by AhpF in classical system | AhpC can use AhpD and TrxC in that species | AhpC can interact with thioredoxin-C in that species | Functional context and donor specificity | QUALIFIED | In *P. putida*, ahpC is co-transcribed with ahpF and AhpF is the dedicated reductant; this argues against the donor-specific GO term thioredoxin peroxidase activity even though the enzyme is clearly an active peroxiredoxin (poole2000ahpfandother pages 3-4, kim2014oxidativestressresponse pages 5-6, zhang2019molecularmechanismsof pages 4-5, fukumori2001molecularcloningand pages 4-6, fukumori2001molecularcloningand pages 6-8, hishinuma2008oxyrisinvolved pages 1-2) |
| Conclusion | Active-site architecture intact | Active-site architecture intact | Active-site architecture intact | Final placement and catalytic competence | SUPPORTED FOR CATALYSIS | Active site fully intact, catalysis predicted, no pseudo-enzyme features. Q88K52 is an active Prx1/AhpC typical 2-Cys peroxiredoxin. The annotation issue is electron-donor specificity of GO:0008379, not active-site integrity or wrong superfamily placement (ellis1997rolesforthe pages 4-5, gretes2012peroxiredoxinsinparasites. pages 2-4, fukumori2001molecularcloningand pages 4-6, rhee2016overviewonperoxiredoxin pages 1-2) |


*Table: This table summarizes catalytic-residue conservation and subfamily placement for Pseudomonas putida AhpC relative to characterized homologs. It shows that Q88K52 is a bona fide active typical 2-Cys peroxiredoxin, with the main curation issue being donor-specific GO term specificity rather than catalytic loss.*

### Summary of active-site findings

*P. putida* AhpC (Q88K52) is a 186-amino-acid protein with two conserved catalytic cysteines: Cys47 (peroxidatic cysteine, CP) and Cys166 (resolving cysteine, CR) (fukumori2001molecularcloningand pages 4-6). These correspond precisely to the experimentally characterized Cys46/Cys165 in *S. typhimurium* AhpC, where mutagenesis demonstrated that C46S eliminates peroxidatic activity and C165S retains activity but alters the catalytic cycle kinetics (ellis1997rolesforthe pages 4-5, ellis1997rolesforthe pages 1-2, ellis1997rolesforthe pages 8-8). The protein shares 69% overall identity with *S. typhimurium* AhpC and 65% with *P. aeruginosa* AhpC (fukumori2001molecularcloningand pages 4-6).

**Pseudo-enzyme test result: NEGATIVE.** Both catalytic cysteines are intact with proper spacing. The protein has been functionally validated — overexpression in *E. coli* confers resistance to organic hydroperoxide (tert-butyl hydroperoxide) (fukumori2001molecularcloningand pages 4-6, fukumori2001molecularcloningand pages 6-8).

**Subfamily placement test result: CORRECT.** The protein is unambiguously a Prx1/AhpC typical 2-Cys peroxiredoxin based on sequence identity, catalytic residue conservation, and genomic organization (gretes2012peroxiredoxinsinparasites. pages 2-4, parsonage2010broadspecificityahpclike pages 2-3, gretes2012peroxiredoxinsinparasites. pages 1-2). No evidence of mis-placement into Prx5, Prx6, Tpx, or other Prx subfamilies.

---

## GO Curation Implications

**Recommended curation action: REPLACE-WITH-SIBLING-TERM (or generalize)**

The term GO:0008379 (thioredoxin peroxidase activity) should be replaced with **GO:0051920 (peroxiredoxin activity)** for this protein. The rationale:

1. **GO:0008379 specifies thioredoxin as the electron donor.** The GO definition of thioredoxin peroxidase activity describes the reaction: thioredoxin + ROOH → thioredoxin disulfide + ROH + H₂O. This is biochemically accurate for some AhpC-family members (e.g., mycobacterial AhpC with TrxC, *T. pallidum* AhpC with TpTrx, *H. pylori* AhpC) (wong2017ahpcofthe pages 11-12, parsonage2010broadspecificityahpclike pages 2-3, broden2016insightsintothe pages 12-16).

2. **P. putida AhpC uses AhpF, not thioredoxin.** In this organism, ahpC and ahpF form a co-transcribed operon. AhpF is a dedicated NADH:peroxiredoxin oxidoreductase — a flavoprotein homologous to thioredoxin reductase but structurally and functionally distinct from thioredoxin itself (poole2000ahpfandother pages 3-4, poole2000ahpfandother pages 4-5, poole2000ahpfandother pages 1-2, kim2014oxidativestressresponse pages 5-6, fukumori2001molecularcloningand pages 1-3). The AhpF N-terminal domain contains a thioredoxin-like fold that directly reduces AhpC, but AhpF is not thioredoxin (poole2000ahpfandother pages 3-4, poole2000ahpfandother pages 4-5).

3. **The peroxiredoxin field explicitly addressed this naming issue.** The enzyme family was renamed from "thioredoxin peroxidase" to "peroxiredoxin" because not all members use thioredoxin as their electron donor (yang2025insectperoxiredoxinsa pages 2-4, rhee2016overviewonperoxiredoxin pages 1-2).

4. **GO:0051920 (peroxiredoxin activity)** is the appropriate broader term that captures the thiol-dependent peroxidase activity without incorrectly specifying the electron donor.

5. A potential caveat: it is conceivable that *P. putida* AhpC could also accept thioredoxin as a backup electron donor, as demonstrated for *B. thailandensis* AhpC which can use both AhpD and TrxC (zhang2019molecularmechanismsof pages 4-5). However, AhpD/AhpF are preferred in those cases, and no experimental evidence supports thioredoxin as the primary or even a significant donor for *P. putida* AhpC in the presence of AhpF.

---

## Conflicts, Knowledge Gaps, and Discriminating Tests

### Conflicts and alternative interpretations

1. **AhpF contains thioredoxin-like domains**, which may have led to the conflation. PANTHER/TreeGrafter may group AhpF-dependent and thioredoxin-dependent peroxiredoxins together at a shared ancestral node, and the GO:0008379 annotation at that node would be appropriate only for the thioredoxin-dependent branch (poole2000ahpfandother pages 3-4, poole2000ahpfandother pages 4-5).

2. **Some AhpC proteins genuinely use thioredoxin.** *Mycobacterium* AhpC uses TrxC (wong2017ahpcofthe pages 11-12), *T. pallidum* AhpC uses thioredoxin because it lacks AhpF (parsonage2010broadspecificityahpclike pages 2-3), and *B. thailandensis* AhpC can use both TrxC and AhpD (zhang2019molecularmechanismsof pages 4-5). This means the PANTHER family annotation GO:0008379 is correct for a subset of family members — the error is in indiscriminate propagation to all family members including classical AhpCF-system proteins.

3. **Possible secondary thioredoxin compatibility.** It is unknown whether *P. putida* AhpC can accept electrons from thioredoxin at all. The organism does express TrxB under OxyR control (hishinuma2008oxyrisinvolved pages 1-2), and cross-reactivity cannot be excluded. However, the genomic architecture strongly favors AhpF as the physiological partner.

### Knowledge gaps

- **No purified-enzyme kinetic assay** has been performed with *P. putida* AhpC testing thioredoxin vs. AhpF as reductant. The functional data are from overexpression/resistance assays and transcriptomics, not direct kinetic characterization of donor specificity.
- **No AlphaFold/structural analysis** was computationally executed in this review (web-only resource, not programmatically accessible for alignment). The analysis relies on sequence-level catalytic residue mapping.

### Discriminating tests to resolve

1. **Most efficient resolution:** Purified *P. putida* AhpC + purified AhpF vs. purified thioredoxin/TrxB in an NADH-consumption peroxidase assay. Compare kcat/Km for each reducing system. This would definitively establish whether GO:0008379 or GO:0051920 is the correct annotation.
2. **Genetic test:** Construct an ahpF deletion mutant in *P. putida* and assess whether AhpC-dependent peroxide resistance is lost or maintained (the latter would suggest alternative reductants can substitute).
3. **Computational test:** Submit Q88K52 to the PREX (PeroxiRedoxin classification indEX) server to confirm Prx1/AhpC subfamily assignment and check for donor-specificity predictors.

---

## Summary

*P. putida* AhpC (Q88K52) is an active, catalytically competent typical 2-Cys peroxiredoxin of the Prx1/AhpC subfamily with fully conserved active-site cysteines (Cys47/Cys166). The protein functions as the peroxidase component of the classical AhpC–AhpF alkyl hydroperoxide reductase system, using AhpF as its dedicated NADH-dependent reductant rather than thioredoxin. The propagated GO term GO:0008379 (thioredoxin peroxidase activity) correctly identifies the protein as a peroxiredoxin but incorrectly specifies the electron donor, representing a characteristic TreeGrafter granularity error (Failure Mode 1). The recommended corrective action is to replace GO:0008379 with GO:0051920 (peroxiredoxin activity), pending curator verification and ideally an in vitro donor-specificity assay.

References

1. (fukumori2001molecularcloningand pages 4-6): Fumiyasu Fukumori and Mitsuru Kishii. Molecular cloning and transcriptional analysis of the alkyl hydroperoxide reductase genes from pseudomonas putida kt2442. The Journal of general and applied microbiology, 47 5:269-277, Oct 2001. URL: https://doi.org/10.2323/jgam.47.269, doi:10.2323/jgam.47.269. This article has 21 citations.

2. (fukumori2001molecularcloningand pages 1-3): Fumiyasu Fukumori and Mitsuru Kishii. Molecular cloning and transcriptional analysis of the alkyl hydroperoxide reductase genes from pseudomonas putida kt2442. The Journal of general and applied microbiology, 47 5:269-277, Oct 2001. URL: https://doi.org/10.2323/jgam.47.269, doi:10.2323/jgam.47.269. This article has 21 citations.

3. (kim2014oxidativestressresponse pages 5-6): Jisun Kim and Woojun Park. Oxidative stress response in pseudomonas putida. Applied Microbiology and Biotechnology, 98:6933-6946, Jun 2014. URL: https://doi.org/10.1007/s00253-014-5883-4, doi:10.1007/s00253-014-5883-4. This article has 145 citations and is from a domain leading peer-reviewed journal.

4. (yang2025insectperoxiredoxinsa pages 2-4): Li Yang, Shaohua Lu, Yujie Lu, Mingshun Chen, and Sufen Cui. Insect peroxiredoxins: a comprehensive review of their classification, distribution, structural features, expression profiles and physiological functions. Insects, 16:678, Jun 2025. URL: https://doi.org/10.3390/insects16070678, doi:10.3390/insects16070678. This article has 3 citations.

5. (rhee2016overviewonperoxiredoxin pages 1-2): Sue Goo Rhee. Overview on peroxiredoxin. Molecules and Cells, 39:1-5, Jan 2016. URL: https://doi.org/10.14348/molcells.2016.2368, doi:10.14348/molcells.2016.2368. This article has 512 citations and is from a peer-reviewed journal.

6. (bojanovic2017globaltranscriptionalresponses pages 10-11): Klara Bojanovič, Isotta D'Arrigo, and Katherine S. Long. Global transcriptional responses to osmotic, oxidative, and imipenem stress conditions in pseudomonas putida. Applied and Environmental Microbiology, Apr 2017. URL: https://doi.org/10.1128/aem.03236-16, doi:10.1128/aem.03236-16. This article has 84 citations and is from a peer-reviewed journal.

7. (hishinuma2008oxyrisinvolved pages 1-2): Sota Hishinuma, Iwao Ohtsu, Makoto Fujimura, and Fumiyasu Fukumori. Oxyr is involved in the expression of thioredoxin reductase trxb in pseudomonas putida. FEMS microbiology letters, 289 2:138-45, Dec 2008. URL: https://doi.org/10.1111/j.1574-6968.2008.01374.x, doi:10.1111/j.1574-6968.2008.01374.x. This article has 24 citations and is from a peer-reviewed journal.

8. (ellis1997rolesforthe pages 4-5): Holly R. Ellis and Leslie B. Poole. Roles for the two cysteine residues of ahpc in catalysis of peroxide reduction by alkyl hydroperoxide reductase from salmonella typhimurium. Biochemistry, 36 43:13349-56, Oct 1997. URL: https://doi.org/10.1021/bi9713658, doi:10.1021/bi9713658. This article has 277 citations and is from a peer-reviewed journal.

9. (ellis1997rolesforthe pages 1-2): Holly R. Ellis and Leslie B. Poole. Roles for the two cysteine residues of ahpc in catalysis of peroxide reduction by alkyl hydroperoxide reductase from salmonella typhimurium. Biochemistry, 36 43:13349-56, Oct 1997. URL: https://doi.org/10.1021/bi9713658, doi:10.1021/bi9713658. This article has 277 citations and is from a peer-reviewed journal.

10. (fukumori2001molecularcloningand pages 6-8): Fumiyasu Fukumori and Mitsuru Kishii. Molecular cloning and transcriptional analysis of the alkyl hydroperoxide reductase genes from pseudomonas putida kt2442. The Journal of general and applied microbiology, 47 5:269-277, Oct 2001. URL: https://doi.org/10.2323/jgam.47.269, doi:10.2323/jgam.47.269. This article has 21 citations.

11. (ellis1997rolesforthe pages 8-8): Holly R. Ellis and Leslie B. Poole. Roles for the two cysteine residues of ahpc in catalysis of peroxide reduction by alkyl hydroperoxide reductase from salmonella typhimurium. Biochemistry, 36 43:13349-56, Oct 1997. URL: https://doi.org/10.1021/bi9713658, doi:10.1021/bi9713658. This article has 277 citations and is from a peer-reviewed journal.

12. (poole2000ahpfandother pages 3-4): Leslie B. Poole, C. Michael Reynolds, Zachary A. Wood, P. Andrew Karplus, Holly R. Ellis, and Marco Li Calzi. Ahpf and other nadh:peroxiredoxin oxidoreductases, homologues of low mr thioredoxin reductase. European journal of biochemistry, 267 20:6126-33, Oct 2000. URL: https://doi.org/10.1046/j.1432-1327.2000.01704.x, doi:10.1046/j.1432-1327.2000.01704.x. This article has 179 citations.

13. (poole2000ahpfandother pages 4-5): Leslie B. Poole, C. Michael Reynolds, Zachary A. Wood, P. Andrew Karplus, Holly R. Ellis, and Marco Li Calzi. Ahpf and other nadh:peroxiredoxin oxidoreductases, homologues of low mr thioredoxin reductase. European journal of biochemistry, 267 20:6126-33, Oct 2000. URL: https://doi.org/10.1046/j.1432-1327.2000.01704.x, doi:10.1046/j.1432-1327.2000.01704.x. This article has 179 citations.

14. (poole2000ahpfandother pages 1-2): Leslie B. Poole, C. Michael Reynolds, Zachary A. Wood, P. Andrew Karplus, Holly R. Ellis, and Marco Li Calzi. Ahpf and other nadh:peroxiredoxin oxidoreductases, homologues of low mr thioredoxin reductase. European journal of biochemistry, 267 20:6126-33, Oct 2000. URL: https://doi.org/10.1046/j.1432-1327.2000.01704.x, doi:10.1046/j.1432-1327.2000.01704.x. This article has 179 citations.

15. (poole2000ahpfandother pages 2-3): Leslie B. Poole, C. Michael Reynolds, Zachary A. Wood, P. Andrew Karplus, Holly R. Ellis, and Marco Li Calzi. Ahpf and other nadh:peroxiredoxin oxidoreductases, homologues of low mr thioredoxin reductase. European journal of biochemistry, 267 20:6126-33, Oct 2000. URL: https://doi.org/10.1046/j.1432-1327.2000.01704.x, doi:10.1046/j.1432-1327.2000.01704.x. This article has 179 citations.

16. (wong2017ahpcofthe pages 11-12): Chui Fann Wong, Joon Shin, Malathy Sony Subramanian Manimekalai, Wuan Geok Saw, Zhan Yin, Shashi Bhushan, Arvind Kumar, Priya Ragunathan, and Gerhard Grüber. Ahpc of the mycobacterial antioxidant defense system and its interaction with its reducing partner thioredoxin-c. Scientific Reports, Jul 2017. URL: https://doi.org/10.1038/s41598-017-05354-5, doi:10.1038/s41598-017-05354-5. This article has 39 citations and is from a peer-reviewed journal.

17. (parsonage2010broadspecificityahpclike pages 2-3): Derek Parsonage, Daniel C. Desrosiers, Karsten R. O. Hazlett, Yongcheng Sun, Kimberly J. Nelson, David L. Cox, Justin D. Radolf, and Leslie B. Poole. Broad specificity ahpc-like peroxiredoxin and its thioredoxin reductant in the sparse antioxidant defense system of treponema pallidum. Proceedings of the National Academy of Sciences, 107:6240-6245, Mar 2010. URL: https://doi.org/10.1073/pnas.0910057107, doi:10.1073/pnas.0910057107. This article has 44 citations and is from a highest quality peer-reviewed journal.

18. (zhang2019molecularmechanismsof pages 4-5): Bing Zhang, Huawei Gu, Yantao Yang, Haonan Bai, Chao Zhao, Meiru Si, Tao Su, and Xihui Shen. Molecular mechanisms of ahpc in resistance to oxidative stress in burkholderia thailandensis. Frontiers in Microbiology, Jul 2019. URL: https://doi.org/10.3389/fmicb.2019.01483, doi:10.3389/fmicb.2019.01483. This article has 52 citations and is from a peer-reviewed journal.

19. (zhang2019molecularmechanismsof pages 5-7): Bing Zhang, Huawei Gu, Yantao Yang, Haonan Bai, Chao Zhao, Meiru Si, Tao Su, and Xihui Shen. Molecular mechanisms of ahpc in resistance to oxidative stress in burkholderia thailandensis. Frontiers in Microbiology, Jul 2019. URL: https://doi.org/10.3389/fmicb.2019.01483, doi:10.3389/fmicb.2019.01483. This article has 52 citations and is from a peer-reviewed journal.

20. (gretes2012peroxiredoxinsinparasites. pages 2-4): Michael C. Gretes, Leslie B. Poole, and P. Andrew Karplus. Peroxiredoxins in parasites. Antioxidants & redox signaling, 17 4:608-33, Aug 2012. URL: https://doi.org/10.1089/ars.2011.4404, doi:10.1089/ars.2011.4404. This article has 119 citations and is from a domain leading peer-reviewed journal.

21. (gretes2012peroxiredoxinsinparasites. pages 1-2): Michael C. Gretes, Leslie B. Poole, and P. Andrew Karplus. Peroxiredoxins in parasites. Antioxidants & redox signaling, 17 4:608-33, Aug 2012. URL: https://doi.org/10.1089/ars.2011.4404, doi:10.1089/ars.2011.4404. This article has 119 citations and is from a domain leading peer-reviewed journal.

22. (broden2016insightsintothe pages 12-16): Nicole J. Broden, Sarah Flury, Alyssa N. King, Braden W. Schroeder, Gabrielle Dierker Coe, and Melinda J. Faulkner. Insights into the function of a second, nonclassical ahp peroxidase, ahpa, in oxidative stress resistance in bacillus subtilis. Journal of Bacteriology, 198:1044-1057, Apr 2016. URL: https://doi.org/10.1128/jb.00679-15, doi:10.1128/jb.00679-15. This article has 17 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](falcon_artifacts/artifact-01.md)