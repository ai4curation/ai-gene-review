---
title: "BioReason-Pro Comparison Project"
maturity: IN_PROGRESS
tags: [PIPELINE, FLAGSHIP]
species: [human, mouse, rat, worm, yeast, SCHPO, DROME, ARATH, ECOLI, BACSU, PSEPK, DANRE]
sidecars:
  genes: BIOREASON_COMPARISON/genes.csv
  argo139_species_counts: BIOREASON_COMPARISON/argo139-species-counts.csv
  argo139_curation_context_counts: BIOREASON_COMPARISON/argo139-curation-context-counts.csv
  benchmark_cohorts: BIOREASON_COMPARISON/benchmark-cohorts.csv
  benchmark_genes: BIOREASON_COMPARISON/benchmark-genes.csv
  benchmark_quality: BIOREASON_COMPARISON/benchmark-quality.csv
  benchmark_policy: BIOREASON_COMPARISON/benchmark-policy.yaml
  benchmark_metrics: BIOREASON_COMPARISON/benchmark-metrics.json
  second_review_ratings: BIOREASON_COMPARISON/second-review-ratings.csv
  second_review_agreement: BIOREASON_COMPARISON/second-review-agreement.json
---
# BioReason-Pro Comparison Project

Systematic evaluation of BioReason-Pro functional summaries and reasoning traces (Fallahpour et al. 2026, [doi:10.64898/2026.03.19.712954](https://doi.org/10.64898/2026.03.19.712954)) against agent-adjudicated local AIGR gene reviews.

**Bottom line:** across the ARGO139 collected cohort, BioReason-Pro's functional summaries mostly restate what InterPro domain labels already say. The model-performance denominator excludes the wrong-input `csr-1` case (n=138) and separately flags seven sequence-truncated cases. It adds real value mainly for proteins with distinctive multi-domain architectures, and fails systematically on localization, pseudoenzymes, paralogs, and organism-specific biology.

📄 **[Read the manuscript (PDF)](BIOREASON_COMPARISON/article/manuscript.pdf)** &nbsp;·&nbsp; 🖥 **[View the slide deck](BIOREASON_COMPARISON/article/slides.html)** &nbsp;·&nbsp; 📝 [Abstract](BIOREASON_COMPARISON/article/abstract.md)

**Explore the evaluations interactively:**
- [BioReason-Pro SFT evaluation](BIOREASON_COMPARISON/sft-eval.html) — ARGO95 primary cohort: 95 genes, 955 predictions; the browser also includes supplemental source cohorts
- [GO-GPT leaf evaluation](BIOREASON_COMPARISON/gogpt-eval.html) — ARGO139 collected cohort; unresolved terms are explicitly pending
- [GO-GPT leaf adjudication (OpenScientist)](BIOREASON_COMPARISON/gogpt-leaf-adjudication.md) — expert overlay: 7 specific-MF calls blind-tested; **0/7 novel-correct** — GO-GPT mirrors GOA
- [DeepECTF evaluation (ESR-ECOLI-DET-Mini)](BIOREASON_COMPARISON/deepectf-eval.html) — 7 E. coli genes

<details>
<summary>Data, benchmarks, and reproducibility</summary>

- **Benchmarks.** [`genes.csv`](BIOREASON_COMPARISON/genes.csv) is **ARGO139** (Annotation Review GO), the fixed 139-gene collected cohort used for RL narrative review. **ARGO95** is the 95-gene subset with HuggingFace `wanglab/protein_catalogue` SFT GO-term predictions, used for the primary SFT term review. The [benchmark policy](BIOREASON_COMPARISON/benchmark-policy.yaml) freezes the audit baseline and scoring rules. Composition and provenance are recorded in [species counts](BIOREASON_COMPARISON/argo139-species-counts.csv), [curation-context counts](BIOREASON_COMPARISON/argo139-curation-context-counts.csv), [cohorts](BIOREASON_COMPARISON/benchmark-cohorts.csv), [per-gene sources](BIOREASON_COMPARISON/benchmark-genes.csv), [input/reference quality and checksums](BIOREASON_COMPARISON/benchmark-quality.csv), the authoritative generated [metrics](BIOREASON_COMPARISON/benchmark-metrics.json), and the [benchmark supplement](BIOREASON_COMPARISON/article/supplemental-benchmark-details.md).
- **ESR-ECOLI-DET-Mini** ([recap experiment](BIOREASON_COMPARISON/recapitulation-experiment/claude-expt-1/)): a 7-gene quick-check recap of the de Crécy-Lagard expert review of DeepECTransformer predictions. Dataset [`10.5281/zenodo.20751016`](https://doi.org/10.5281/zenodo.20751016). `ESR-ECOLI-DET-7` is a count-explicit alias.
- **Reproducible stats notebooks** ([`notebooks/`](BIOREASON_COMPARISON/notebooks/)) recompute the summary statistics below directly from the committed per-gene files, with no hard-coded numbers.

</details>

## Methods

We downloaded the reports for selected genes from https://app.bioreason.net/ (there is no API yet so this cannot be done in bulk). We assigned an AI agent to compare them with existing pipelines (for example, InterPro2GO) and with the agent-adjudicated local AIGR reference. These local references have mixed review maturity and are not independently expert-signed ground truth.

## Notes on browsing results

Each individual gene review page, e.g. aprE, SlyD contains BOTH the bioreason results AND the detailed review of the bioreason results. You will need to search in the page for "bioreason" or scroll down to the sections:

- Deep Research Bioreason RL (we treat the bioreason outputs as a kind of preliminary research)
- Bioreason RL review


## Key findings (139 RL reviews)

1. **BioReason largely recapitulates InterPro labels in narrative form.** For most genes, the functional summary does not provide biological insight beyond what InterPro domain annotations already capture. Genuine value-add is modest and concentrated in proteins with distinctive, well-annotated domain architectures such as TOR1 (FRB domain enables pathway-level inference), PTEN, NOTCH1, and EGFR. For standard domain families like Src-family kinases, Fyn and Src receive essentially identical generic descriptions.

2. **Systematic localization errors.** BioReason defaults to "cytosolic" or "cytoplasmic" when no transmembrane domains are detected, failing for periplasmic proteins (Skp, CpxP, Spy), vacuolar proteins (cps1), mitochondrial matrix proteins (alo1, HSP60, CAT2), and ER membrane proteins (IRE1, ETR1). Proteins where InterPro domain names explicitly mention the compartment (KAR2, PDI1) are handled correctly.

3. **Pseudo-enzymes are a blind spot.** BioReason assumes catalytic activity from conserved but degenerate domains and cannot reliably identify inactive family members. Epe1 (pseudo-demethylase), cts2 (pseudo-chitinase missing catalytic glutamate), and pmp20 (a 1-Cys peroxiredoxin-family protein with an intact peroxidatic cysteine but directly assayed as peroxidase-inactive and functioning as a chaperone) are all incorrectly assigned ancestral enzymatic activity.

4. **Paralogs get identical generic descriptions.** Closely related paralogs such as Fyn/Src (mouse), sigF/sigG/sigK (B. subtilis sporulation sigma factors), and Hspa5/Hspa8 (rat Hsp70 family) receive interchangeable summaries with no gene-specific biology.

5. **Organism-specific biology is consistently absent.** Dauer formation and insulin/IGF-1 signaling in C. elegans (daf-16, daf-2), UPRmt master regulation (atfs-1), sporulation compartment specificity in B. subtilis (sigF forespore, sigK mother cell), prion propagation in yeast (HSP104), and cytoophidium biology (ura7) are all missed.

6. **Selected-case organism means differ.** Mouse has the highest descriptive correctness mean (4.7), followed by BACSU (4.5), rat (4.4), ARATH and human (4.3), while the selected S. pombe cases score lowest (3.2). These differences are confounded by deliberate case selection: S. pombe is enriched for obscure proteins and pseudoenzymes, whereas several other groups contain more canonical proteins. InterPro informativeness and training distribution are hypotheses, not measured explanations.

- **Overall correctness: 4.0/5** | **Overall completeness: 2.9/5** (n=138 performance set)
- Only 1 gene scored 5/5 on both axes (Uggt1)

## Background

**Architecture:**
- **GO-GPT**: autoregressive transformer (ESM2 embeddings + organism -> GO terms). Upstream predictor.
- **BioReason-Pro**: Qwen3-based multimodal reasoning LLM. Takes GO-GPT predictions + InterPro + PPI + organism context -> chain-of-thought reasoning trace + functional summary. Two variants: **SFT** (richer mechanistic depth) and **RL** (fewer hallucinations).

The GO term list in web exports is raw GO-GPT output (input to reasoning). BioReason-Pro produces its own GO terms after the reasoning step, but the current web app does not separately expose these.

**Web app:** [app.bioreason.net](https://app.bioreason.net) | **Code:** [bowang-lab/BioReason-Pro](https://github.com/bowang-lab/BioReason-Pro) | **Models:** [HuggingFace wanglab collection](https://huggingface.co/collections/wanglab/bioreason-pro)

## Data

Per gene, the following files are available (example: [ECOLI/SlyD](https://github.com/ai4curation/ai-gene-review/tree/main/genes/ECOLI/SlyD)):

| File | Description |
|------|-------------|
| `{GENE}-bioreason-rl-predictions.md` | Raw BioReason-Pro RL web export (reasoning trace, functional summary, InterPro, GO-GPT terms) |
| `{GENE}-bioreason-rl-review.md` | Evaluation of the Functional Summary (correctness/completeness scores + InterPro domain-label comparison and, where present, InterPro2GO comparison) |
| `{GENE}-gogpt-leaf-predictions.yaml` | GO-GPT leaf terms as PredictionReview YAML |
| `{GENE}-sft-predictions.yaml` | BioReason-Pro SFT GO terms as PredictionReview YAML |
| `{GENE}-ai-review.yaml` | Agent-adjudicated local AIGR reference; completion status is recorded in `benchmark-quality.csv` |

## Evaluation rubric

### Correctness (1-5)
- 5: All material claims are supported; no substantive factual error
- 4: Core function is correct with one limited secondary error or overstatement
- 3: Core function is correct, but one or more substantive claims are wrong
- 2: Some relevant biology is present, but errors materially distort the function
- 1: Fundamental mischaracterization or predominantly unsupported account

### Completeness (1-5)
- 5: Covers established core functions, locations, complexes, and pathway context
- 4: Covers the core function and most major context, with a limited omission
- 3: Gets the basics but misses significant established biology
- 2: Captures only one important facet or remains substantially incomplete
- 1: Superficial, one-dimensional, or misses the core function

Correctness is scored only on claims the model makes; missing biology lowers completeness, not correctness. Each review also assesses whether the narrative adds information beyond InterPro domain/family labels. Only 92/139 genes have an actual `GO_REF:0000002` annotation in the committed GOA snapshot, so this qualitative domain-label comparison is not described as a universal InterPro2GO control.

## Benchmark integrity audit

ARGO139 names the **collected cohort** (139 exports), not an unconditional model-performance denominator. The current policy excludes `worm/csr-1` from model scoring because the export was generated from nhr-47/Q17370 rather than CSR-1. Seven otherwise retained exports are exact 2,000-residue prefixes of longer UniProt sequences (`Dscam1`, `BRCA2`, `HTT`, `LRRK2`, human and mouse `NOTCH1`, and `TOR1`) and are stratified as `TRUNCATED_AT_MODEL_LIMIT`.

The local AIGR references are also not represented as independently expert-signed ground truth: 64 are `COMPLETE`, 48 `DRAFT`, 23 `IN_PROGRESS`, and 4 `INITIALIZED` at the frozen audit baseline. `benchmark-quality.csv` records this status plus export/accession, sequence lengths, GOA dates, raw-export checksums, and separate counts/checksums for the InterPro and upstream GO-GPT sections. All 139 exports contain the GO-GPT section; three lack an InterPro section (`Shu1`, `atg16`, and `pgl-1`). Publication-facing analyses must disclose the reference-status and input-quality strata.

The rescored axes remain associated (Pearson 0.688; Spearman 0.617), so they should not be interpreted as statistically independent merely because the rubric defines different concepts. A [blinded second rater](BIOREASON_COMPARISON/second-review-protocol.md) scored a deterministic 20-gene subset balanced across first-rater correctness strata. Correctness agreement was 80% exact and 100% within one point (quadratic-weighted kappa 0.950); completeness agreement was 55% exact and 95% within one point (kappa 0.744). Raw ratings and [generated agreement metrics](BIOREASON_COMPARISON/second-review-agreement.json) are committed.

ARGO95 contains 955 HF-catalogue terms: 678 `CNN` (71.0%; 631 exact frozen-GOA matches and 47 supported as non-novel by other established local evidence), 118 `NPI`, 5 `PLI`, 29 `REP`, 44 `LSP`, 24 `COR`, and 57 `UNC`. A frozen-ontology [ID/label adjudication](BIOREASON_COMPARISON/argo95-ontology-pair-adjudication.tsv) reviewed 82 mismatched or unresolved raw pairs that were nonnegative either at the audit baseline or after manual biological reclassification, and changed 65 calls after separating ontology status from the biological rubric and assessing the canonical GO concept rather than an intended but incompatible label. Raw model pairs remain unchanged and are explicitly flagged in their review rationales.

The ontology authority for this audit is the official archived 2026-03-25 `go-basic.obo`, pinned by SHA-256 in `benchmark-policy.yaml` and checked at load time with both obsolete and active sentinel terms. That release, and the current GO API, explicitly mark terms such as `GO:0005615` extracellular space and `GO:0005844` polysome obsolete. Committed GOA snapshots can lag those obsoletions, and the mixed-date legacy `cache/ontologies/go.tsv` flag is not used for benchmark adjudication.

The [external-authority verification](BIOREASON_COMPARISON/verify_ontology_authority.py) independently downloads the official archive and queries both QuickGO and OLS. On 2026-07-12, the remote archive matched the pinned SHA-256, and both services returned all five disputed sentinels as obsolete; OLS additionally states that `GO:0005615` duplicates `GO:0005576`. Ontology status is reported separately from the seven biological assessment categories: obsoletion alone does not turn a correct non-novel prediction into `LSP`. `LSP` remains reserved for a supplied ID whose canonical concept is more generic than the supported annotation. This distinction restores status-only cases such as `DROME/LysB` and `BACSU/aprE` `GO:0005615` to `CNN` while retaining the obsolete-ID warning.

The ARGO139 GO-GPT files were rebuilt from raw web exports with ontology-aware leaf pruning. The cleaned set contains 5,923 terms: 1,900 exact positive AIGR matches (`CNN`), 129 exact rejected/over-annotated matches (`NPI`), and 3,894 unresolved terms (`UNC`). Because unresolved entries still require manual assessment, 138/139 documents are `DRAFT`; only the fully resolved `BACSU/ftsZ` document is `COMPLETE`. This is a transparent pending review, not a completed GO-GPT performance result.

## Results (138-gene performance set; 139 collected exports)

### Score distribution

| Score | Correctness | Completeness |
|-------|-------------|--------------|
| 5 | 70 (51%) | 1 (1%) |
| 4 | 25 (18%) | 40 (29%) |
| 3 | 22 (16%) | 51 (37%) |
| 2 | 14 (10%) | 39 (28%) |
| 1 | 7 (5%) | 7 (5%) |

### By organism

| Organism | n | Correctness | Completeness |
|----------|---|-------------|--------------|
| mouse | 11 | 4.7 | 3.6 |
| BACSU | 13 | 4.5 | 2.9 |
| rat | 12 | 4.4 | 3.5 |
| ARATH | 3 | 4.3 | 3.3 |
| human | 19 | 4.3 | 3.3 |
| worm | 14 | 4.1 | 2.4 |
| yeast | 11 | 4.1 | 2.6 |
| DROME | 8 | 4.0 | 2.8 |
| PSEPK | 8 | 3.6 | 3.0 |
| ECOLI | 13 | 3.6 | 3.1 |
| SCHPO | 23 | 3.2 | 2.3 |

### Top performers (correctness 5/5)

| Gene | Organism | Completeness | Why it works |
|------|----------|--------------|--------------|
| Uggt1 | rat | 5 | ER quality control enzyme with highly informative domain names |
| TP53 | human | 4 | Distinctive TAD-DBD-tetramerization architecture |
| PTEN | human | 4 | Dual-specificity phosphatase domains are unambiguous |
| EGFR | human | 4 | Canonical RTK architecture well-represented in InterPro |
| NOTCH1 | human | 4 | Proteolytic cascade well-encoded in domain layout |
| MYC | human | 4 | bHLH-LZ domains directly predict E-box binding |
| Akt1 | mouse | 4 | PH + AGC kinase architecture is diagnostic |
| Calm1 | mouse | 4 | EF-hand domains immediately predict calcium sensing |
| Pten | mouse | 4 | Same as human PTEN |
| Trp53 | mouse | 4 | Same as human TP53 |
| ftsZ | BACSU | 4 | Tubulin-like GTPase domain is highly specific |
| spo0A | BACSU | 4 | Response regulator + DNA-binding domains clearly predict phosphorelay TF |
| GroEL | ECOLI | 4 | Chaperonin domains are unambiguous |
| lgg-1 | worm | 4 | Atg8/ubiquitin-like fold directly predicts autophagy adaptor |
| bst1 | SCHPO | 3 | GPI inositol-deacylase function nailed from specific family annotation |

### Critical failures (correctness 1/5)

| Gene | Organism | Completeness | Failure mode |
|------|----------|--------------|--------------|
| atg16 | SCHPO | 1 | No InterPro domains available; confabulated carbohydrate metabolism |
| Epe1 | SCHPO | 1 | Degenerate JmjC pseudoenzyme described as an active histone demethylase |
| pmp20 | SCHPO | 2 | Neo-functionalized peroxiredoxin -> chaperone; model assumes ancestral function |
| pol5 | SCHPO | 1 | Predicted cytokinesis scaffold; actual function is rDNA transcription |
| Shu1 | SCHPO | 1 | Predicted HECT ubiquitin ligase; actually a GPI-anchored heme receptor |
| tam10 | SCHPO | 1 | Unsupported essential-growth scaffold narrative invents molecular and pathway roles for a protein of unknown function |
| pgl-1 | worm | 1 | Described as nuclear TF scaffold; actually cytoplasmic P granule component |

## Failure mode taxonomy

The prose failure modes below are encoded as controlled `error_type` values on the
discordant (NPI/PLI/REP) predictions in the per-gene `*-predictions.yaml` files, using the
same shared `PredictionErrorTypeEnum` as the [ProtNLM evaluation](PROTNLM_EVALUATION.md) so
the two projects are directly comparable. Four values were added for patterns Table 1 of de
Crécy-Lagard et al. does not name: `PSEUDOENZYME_OVERANNOTATION` (mode 1), `LOCALIZATION_DEFAULT`
(mode 2), `TAXON_CONSTRAINT_VIOLATION` (mode 7, cross-kingdom), and `WRONG_INPUT_SEQUENCE`
(mode 9). Paralog indistinguishability (mode 3) maps to the existing `PARALOG_OVERANNOTATION`
and neofunctionalization/moonlighting (mode 5) to `MULTIPLE_FUNCTIONS`. These tags are applied
where a *predicted GO term* embodies the failure; modes that are narrative-only (e.g. the model
calling a periplasmic protein "cytoplasmic" in prose while GO-GPT still predicts the periplasm
term) leave no discordant term to tag and are recorded only in the RL narrative reviews.

### 1. Pseudo-enzyme blind spot

BioReason assumes catalytic activity from conserved domains without checking whether catalytic residues are intact. This is a systematic failure for proteins that retain an ancestral fold but have lost enzymatic activity.

**Examples:**
- **Epe1** (SCHPO, 1/5): BioReason claims *"JmjC catalytic center dictates a lysine demethylase mechanism"* but Epe1 has degenerate active site residues (HVD instead of HXD, Tyr307 instead of catalytic His). No detectable demethylase activity in mass spec assays. Functions as anti-silencing factor through HP1/Swi6 binding.
- **cts2** (SCHPO, 2/5): Called an active chitinase, but the protein lacks the essential catalytic glutamate and is likely catalytically dead.
- **pmp20** (SCHPO, 1/5): Predicted as an active peroxidase, but this 1-Cys family member was directly assayed as peroxidase-inactive and functions as a molecular chaperone; absence of a resolving cysteine is not itself the mechanistic defect.

Notably, the BioReason paper highlights CFAP61 as a correctly identified pseudoenzyme, but this success does not generalize to our test set.

**Independent adjudication (OpenScientist).** Three predictions we had scored `UNC`
(genuinely on the fence) were re-tested as blinded gene-function hypotheses by an
independent OpenScientist agent (structure + comparative genomics; the suspected answer
was withheld from the prompt). Two were pseudoenzyme over-annotations, resolving the
`UNC` calls to `NPI` (full reports live under each gene's `*-hypotheses/` directory):
- **MJ1511** (METJA) predicted as a thiol-disulfide oxidoreductase (GO:0016671):
  **refuted** — no CxxC redox motif, no proton-relay histidines, and its two cysteines sit
  ~36.5 Å apart in the AlphaFold model.
- **cts2** (SCHPO) predicted to drive fungal cell-wall disassembly (GO:0031506):
  **refuted** — GH18 catalytic glutamate replaced by asparagine (E166N); the *S. japonicus*
  ortholog retains the intact motif.
- **DCAF12L2** (human) predicted to target proteasomal degradation via CRL4 (GO:0043161):
  **partially supported, kept as a lead** — the WD40 substrate-binding arm is intact but the
  DDB1-binding interface is degenerate and DDB1 is absent from all 43 experimental interactors,
  so the CRL4-assembly step is unconfirmed.

**Dispute confirmation (OpenScientist).** Separately, 12 SFT predictions we had *disputed*
(`NPI`/`PLI`) were re-tested the same blinded way to check our own rejections. Most incorrect-call
verdicts were upheld, with three important corrections. **pmp20**'s peroxiredoxin `NPI` stands but the rationale
was corrected (it is a 1-Cys peroxiredoxin with an intact peroxidatic site — not a "lost resolving
cysteine" — that is nonetheless directly assayed as inactive: GOA `NOT|enables` glutathione
peroxidase), and **SPAC8E11.10**'s NADP⁺-alcohol-dehydrogenase call was softened `NPI → LSP` (a
defensible broad activity class, less precise than its sorbose-reductase function). The
**DnaJ protein-disulfide reductase activity** call was corrected from `NPI` to `CNN`: the activity
has direct assay support
and the current AIGR keeps it as non-core. The remaining confirmed incorrect calls recapitulate the
same failure modes — pseudoenzyme/paralog over-annotation (LysB lysozyme≠chitinase; DnaK is not a
redox enzyme; alo1, mlcD, rdgBbeta wrong
paralog/substrate; comK/fliY misread domain labels), and wrong-input-sequence (**csr-1**, which
also surfaced a real accession bug: Q21992 is deleted and maps to larp-1). Full reports live under
each gene's `*-hypotheses/` directory.

### 2. Localization defaults to cytoplasm

When InterPro annotations lack transmembrane or signal peptide information, BioReason systematically defaults to cytoplasmic localization. This fails for:

- **Periplasmic proteins**: Skp, CpxP, Spy (all E. coli) are called cytoplasmic despite having signal peptides.
- **ER membrane proteins**: ETR1 (Arabidopsis ethylene receptor) called "soluble cytoplasmic signal transducer" — actually an ER membrane integral protein with 3 TM helices. IRE1 (yeast) similarly mislocalised.
- **Mitochondrial proteins**: alo1 (SCHPO), HSP60 (yeast), CAT2 (yeast) all called cytosolic.
- **Vacuolar proteins**: cps1 (SCHPO) called cytoplasmic.
- **Secreted proteins**: fibrolase (AGKCO) claimed as "membrane-tethered neural/endocrine" — actually a secreted venom fibrinolytic enzyme.

Proteins succeed when InterPro domain names explicitly contain the compartment (KAR2/BiP -> ER, PDI1 -> ER).

### 3. Paralog indistinguishability

Closely related family members receive essentially identical descriptions:

- **Fyn vs Src** (mouse): Both get a generic Src-family kinase description. No mention of Fyn-specific T-cell signaling, tau phosphorylation, or myelination. No mention of Src-specific osteoclast biology.
- **sigF vs sigG vs sigK** (BACSU): All three sporulation sigma factors treated as generic sigma factors. The curated reviews show sigF is forespore-specific with partner-switching (SpoIIAB), sigG is late-forespore with Gin anti-sigma regulation, sigK requires processing from pro-sigK and excision of the skin element.
- **Hspa5 vs Hspa8** (rat): Both described as generic Hsp70 chaperones. Hspa5 (BiP) is ER-specific with UPR regulation. Hspa8 (Hsc70) has distinctive constitutive functions in clathrin uncoating and chaperone-mediated autophagy.

### 4. Organism-specific biology absent

BioReason's domain-to-function reasoning cannot capture biology that is specific to a lineage or organism:

- **C. elegans**: daf-16 described as generic forkhead TF (misses IIS pathway, longevity, dauer biology). daf-2 described as generic RTK (misses insulin/IGF-1 receptor identity and aging). atfs-1 described as generic bZIP TF (misses UPRmt master regulator role). hlh-30 described as generic bHLH (misses TFEB ortholog identity and autophagy/lysosome biology).
- **B. subtilis**: Sporulation compartment specificity is never captured. aprE's role in quorum sensing/Phr peptide processing is missed. comK described via protein binding instead of competence regulation.
- **S. cerevisiae**: HSP104 misses prion propagation and thermotolerance. RAS2 fundamentally wrong (vesicle trafficking instead of cAMP/PKA signaling). TOR1 is the exception where FRB domain enables pathway identification.
- **S. pombe**: ura7 misses cytoophidium biology. pol5 completely wrong (cytokinesis scaffold instead of rDNA transcription).

### 5. Neo-functionalization and moonlighting

When a protein has acquired a function different from its ancestral domain prediction, BioReason defaults to the ancestral/family-typical function:

- **pmp20** (SCHPO): Peroxiredoxin fold -> predicted peroxidase; actual chaperone
- **Nmnat** (DROME): NAD+ biosynthesis enzyme fold -> misses moonlighting chaperone/neuroprotection function
- **LysB** (DROME): Lysozyme fold -> framed as immune defense; actually a digestive enzyme
- **GAPDH** (human): Correctly identifies glycolytic enzyme but misses all moonlighting functions
- **Casp3** (rat): Core protease/apoptosis correct but misses differentiation roles in neurons, keratinocytes, erythrocytes

### 6. Narrative-GO prediction disconnect

In multiple cases, the GO term predictions from the upstream ESM model are more accurate than BioReason's narrative functional summary. The two outputs appear to be generated somewhat independently:

- **RidA** (ECOLI): Narrative describes the correct chemistry ("accelerating hydrolysis of reactive intermediates") but calls it "non-enzymatic" and assigns protein binding (GO:0005515) instead of deaminase activity (GO:0019239).
- **atg2** (SCHPO): GO terms include correct autophagy terms but the narrative describes only scaffolding, missing the primary lipid transfer function.
- **BenR** (PSEPK): GO term predictions are reasonable but the narrative describes a CO/formate regulator instead of a benzoate pathway activator.

### 7. Cross-kingdom fold bias

Training data skewed toward well-studied organisms can bias predictions:

- **aprE** (BACSU): BioReason predicts human hemostasis/blood coagulation processes for a B. subtilis subtilisin, reflecting mammalian-dominated training data.
- **PGRPLB** (ANOGA): Called a "fruit fly" protein when it is actually from the mosquito Anopheles gambiae.
- **NFE2L2** (human): bZIP domain analysis erroneously emphasizes erythroid function (from the NF-E2 family name) over the protein's primary role in antioxidant response.

### 8. Generated UniProt-style summary fabrication

The export section titled `UniProt Summary` is generated by BioReason's instruction to summarize in UniProt format; it is not text imported from UniProt. Only 3/139 RL strings are exact substrings of the cached UniProt record. Incorrect text in this section is therefore a model-output error, not an upstream UniProt error. Clear examples include steroid-sulfate transport for `Slc5a1`, a protist/cytochrome-b6 context for human `CYCS`, and "probable glutamine amidotransferase" for `PARK7`.

### 9. Wrong input data

- **csr-1** (worm, 1/5): BioReason received the nhr-47 sequence instead of the CSR-1 Argonaute. All predictions are for the wrong protein.

## Comparison with InterPro domain/family labels and InterPro2GO

A central question is whether BioReason provides value beyond the InterPro domain/family information supplied to it. Our reviews assessed domain-label recapitulation for each gene and an actual InterPro2GO (`GO_REF:0000002`) baseline where present (92/139 genes).

**In most cases, BioReason is a narrative restatement of its InterPro inputs.** The functional summary translates domain and family labels into prose without adding new biological insight. Where an actual InterPro2GO mapping is present and wrong, or where the family label encourages an invalid extrapolation, BioReason typically recapitulates and sometimes amplifies the error.

**BioReason adds value in specific cases:**
- Proteins with distinctive multi-domain architectures where the combination is diagnostic (TOR1, NOTCH1, PTEN, EGFR, spo0A)
- Proteins where family-level InterPro names are highly informative (Uggt1, bst1, KAR2)

**BioReason inherits domain-label and mapping errors:**
- KEAP1: InterPro2GO assigns BTB-Kelch to actin binding; BioReason amplifies this into "actin remodeling" instead of the correct NRF2 regulation
- Ctnnb1: Armadillo repeat -> cell adhesion dominates; transcriptional co-activator role (Wnt/TCF-LEF) underweighted
- SecB: Chaperone family -> "protein folding" assigned, but SecB is an anti-folding holdase

## Paper case study proteins

Full reasoning traces in supplementary C.6-C.15:

| Protein | UniProt | Paper section | Key finding |
|---------|---------|---------------|-------------|
| eEFSec | P57772 | Fig. 5, S2.6 | De novo predicted SBP2 as binding partner, validated by cryo-EM |
| CFAP61 | Q8NHU2 | Fig. 6, S2.7 | Correctly identified pseudoenzyme scaffold despite catalytic domains |
| EvoAcr1 | synthetic | S2.8 | No homology/domains. Predictions varied by organism label. SFT fabricated InterPro. |
| EvoAcr2 | synthetic | S2.8 | RL predicted phage-encoded host modulator -- biologically coherent |

### CFAP61 vs Epe1: same class, opposite results

Both are pseudoenzymes with catalytic domain signatures. BioReason **correctly** identifies CFAP61 as non-enzymatic (paper's featured result) but **fails** on Epe1, confidently calling it an active demethylase. This suggests pseudoenzyme detection is not systematic but case-dependent.

## SFT vs RL comparison

### Paper findings (27 evaluators, 162 proteins)
- **SFT**: 8.0/10, preferred for mechanistic depth
- **RL**: 7.4/10, preferred for factual reliability
- SFT fabricated InterPro entries for novel proteins; RL never did

### Our pilot (5 genes)
- Texts clearly different; SFT ~10% longer
- SFT more specific but sometimes wrong; RL safer but shallower
- Both fail on pseudoenzymes (Epe1)

The primary structured SFT term cohort is ARGO95 (95 HF-catalogue genes, 955 terms); mixed-source SFT views are supplemental.

## Paper evaluation sets

- **Test set**: 8,630 proteins ([HuggingFace](https://huggingface.co/datasets/wanglab/bioreason-pro-test-data)), temporal holdout post-2022
- **Human eval**: 192 proteins, 162 by external biologists. Protein list not published.
- **Overlap with AIGR**: 7 of 1,211 genes. Low by design -- their test set is newly annotated, ours is deeply characterized.
- 99 additional genes from their test set are being reviewed to expand overlap.

## HuggingFace protein_catalogue analysis

The HF dataset [`wanglab/protein_catalogue`](https://huggingface.co/datasets/wanglab/protein_catalogue) contains 223,214 proteins across 8,439 organisms (Apache-2.0). All entries are **SFT model only** (the `model` column is uniformly `SFT`). There is no RL equivalent.

Local copy: `data/bioreason-hf/*.parquet` (3 shards, ~626MB total). Queryable with duckdb:

```sql
SELECT * FROM 'data/bioreason-hf/*.parquet' WHERE protein_id = 'P0A9K9'
```

### What the pipeline actually produces

| Component | Model | Output |
|-----------|-------|--------|
| GO-GPT (`wanglab/gogpt`) | Autoregressive transformer (ESM2 + organism) | GO term hierarchy (F_max 0.65-0.70) |
| BioReason-Pro SFT (`wanglab/bioreason-pro-sft`, 4B) | Qwen3 fine-tuned on GPT-5-generated reasoning traces (124K examples) | `<think>` trace + functional summary. *"More hypothesis, more hallucinations"* |
| BioReason-Pro RL (`wanglab/bioreason-pro-rl`, 4B) | Same base + GRPO (9.2K examples) | Same format. *"More accurate, less mechanistically deep"*. Never fabricated InterPro |

### GO term provenance: what comes from where

The web app shows "GO GPT" and "GO Leaf" panels regardless of SFT/RL selection. Those panels are **GO-GPT predictions** supplied to the reasoning model. The HuggingFace `protein_catalogue` is a different artifact: its structured GO section is documented as BioReason-Pro SFT model output. ARGO95 therefore evaluates the HF SFT output, while the web-export GO panels are reviewed separately as upstream GO-GPT output.

The HF catalogue's structured GO section (at the end of the `generation` column) substantially overlaps the GO-GPT input, but provenance follows the official catalogue description: it is model-generated SFT output, not an imported GO-GPT panel. Approximately 97% of entries have this structured section; approximately 3% are truncated.

**RL model GO predictions are not accessible anywhere.** The web app shows GO-GPT (input), the HF catalogue is SFT only, and the RL reasoning trace does not emit its own GO terms.

**How accurate are GO-GPT's specific leaf calls?** Because every downstream GO term originates here, we
blind-tested 7 of GO-GPT's most informative specific-MF predictions (one per gene, across
kinase/protease/transferase/lipid-transfer/adaptor/chaperone functions in 5 organisms) with an
independent OpenScientist agent — an **expert-adjudication overlay** on the deterministic ARGO139
benchmark, not a rewrite of it. **0/7 were novel-correct.** GO-GPT *mirrors GOA*: its 4 correct calls
all re-derive an annotation GOA already has (2 `CNN` exactly; 2 `LSP` as a coarse parent of an existing
curated child), and its 3 wrong calls (`NPI`) either reproduce an *anomalous* existing GOA annotation
(Akt1 inverted kinase-inhibitor; Prkaa2 a lone rat adaptor IDA that is really the β subunit's function)
or, in the single case that ventures beyond GOA (gaa1), commit a **subunit-level misattribution**
(assigning Gpi8's catalytic cysteine-protease chemistry to the non-catalytic gaa1). Where the benchmark's
deterministic action-matching already resolves a term, the overlay agrees; for the terms it leaves
`UNC`, the overlay supplies an expert verdict — details in the
[GO-GPT leaf adjudication](BIOREASON_COMPARISON/gogpt-leaf-adjudication.md).

| Source | GO-GPT (input) | BioReason SFT GO | BioReason RL GO |
|--------|----------------|------------------|-----------------|
| Web app panels | "GO GPT" + "GO Leaf" | Not shown separately | Not shown separately |
| HF `protein_catalogue` | In `<think>` block | Structured section at end | **Not available** |
| Scraped `-rl.md` files | Full hierarchy in GO Terms section | N/A | **Not emitted** |

### SlyD (P0A9K9) cross-source comparison

We compared GO terms for SlyD across three sources to understand the relationship between them:

**Legacy website SFT scrape** (deleted unsuffixed raw export; 9 terms -- leaf-pruned):
GO:0003755 (PPIase activity), GO:0016859, GO:0140096, GO:0016853, GO:0003824, GO:0006457, GO:0005737, GO:0005829, GO:0005622

**Website RL scrape** (`SlyD-bioreason-rl-predictions.md`, 58 terms -- full GO-GPT with all ancestors):
Includes the above plus metal binding (GO:0008270, GO:0005507, GO:0016151, GO:0050897), unfolded protein binding (GO:0051082), heat response (GO:0009408), refolding (GO:0042026), stabilization (GO:0050821), and all ancestor terms up to root.

**HF SFT catalogue** (structured section, 13 terms):
GO:0051082, GO:0003755, GO:0008270, GO:0005507, GO:0016151, GO:0050897 (MF);
GO:0009408, GO:0022417, GO:0042026, GO:0044008, GO:0050821, GO:0000413 (BP);
GO:0005829 (CC)

**Key finding**: 12 of 13 HF SFT terms are contained in the RL website GO-GPT output. The one HF-only term (GO:0044008, modulation by symbiont of host adenylate cyclase pathway) is a more specific descendant also present in the RL hierarchy. The website RL dump includes the full GO hierarchy (all ancestors up to root), while the HF SFT keeps leaf-ish terms. The website SFT scrape was pruned to very generic parent terms.

This shows strong cross-source dependence, but does not establish that all three artifacts are identical predictions. The HF catalogue remains the most useful bulk source because it retains informative leaf-like terms without the web panel's ancestor noise.

### Coverage gaps

Notable proteins NOT in the 223K catalogue: TP53 (P04637), EGFR (P00533), NOTCH1 (P46531), MTOR (P42345). Several well-known proteins that are present have truncated generations (cut off mid-sentence, never reaching the GO section): MYC (P01106), BCL2 (P10415), PTEN (P60484), CTNNB1 (P35222).

## SFT Catalogue Evaluation (45 proteins, 15 clades)

Full details: [research/bioreason-sft-evaluation.md](/research/bioreason-sft-evaluation.md)

We evaluated 45 proteins from the HF SFT catalogue across 15 clades (DANRE, DICDI, METJA, MYCTU, PSEAE, ANOGA, ARATH, DROME, ECOLI, SCHPO, human, mouse, rat, worm, yeast), 3 proteins per clade, mixing well-characterized and poorly-characterized proteins.

**Overall: Correctness 3.0/5, Completeness 2.7/5**

### Score distribution

| Score | Correctness | Completeness |
|-------|:-----------:|:------------:|
| 5 | 0 (0%) | 0 (0%) |
| 4 | 15 (33%) | 5 (11%) |
| 3 | 18 (40%) | 25 (56%) |
| 2 | 7 (16%) | 12 (27%) |
| 1 | 5 (11%) | 3 (7%) |

These results are consistent with the RL evaluation (138-gene performance set): **overall correctness 4.0/5, completeness 2.9/5** (RL scores higher on correctness, consistent with the paper's claim that RL has fewer hallucinations).

### Top failure modes (SFT catalogue)

1. **Fabricated UniProt summaries (7/45 = 16%)**. BioReason generates fake "UniProt Summary" text for uncharacterized proteins. All 7 cases are on proteins where UniProt says "Uncharacterized protein." This is systematic and dangerous — it misrepresents an authoritative database.

2. **Paralog/family conflation (8/45 = 18%)**. Biology from well-characterized family members is applied to divergent paralogs: mlcD (calmodulin→myosin I LC), rdgBbeta (vibrator→Class II PITP), Ndufb1/NDUFAB1 confusion, Ifi204/AIM2 conflation, Hmgcs2/HMGCS1 mixing.

3. **Organism-specific biology usually absent**. Most reviews found no organism-specific insight beyond domain architecture. Mosquito eye pigmentation, Mtb drug targets, yeast cell wall biology, worm body size regulation, and plant cold stress were missed; `fen1` is a counterexample where the review credits a zebrafish retinal-phenotype link.

4. **Inverse quality vs characterization**. Proteins with 0-3 GOA annotations (where BioReason could add most value) consistently score 0-1/5. Well-characterized proteins (where BioReason scores 4/5) already have extensive annotations making the narrative redundant.

5. **Hallucinated GO IDs**. BioReason cites specific GO IDs that map to completely different terms (e.g. GO:0047554 cited as caffeoyl-CoA O-methyltransferase, actually 2-pyrone-4,6-dicarboxylate lactonase).

6. **Directional errors**. Several errors get the mechanism exactly backwards: CRH1 donor-acceptor direction, Sstr5 ligand preference, gcl substrate clearance direction, CHL1 cell death promotion vs limitation.

### Comparison: SFT catalogue vs RL web scrapes

| Metric | SFT catalogue (45) | RL performance set (138) |
|--------|:------------------:|:--------------------:|
| Mean correctness | 3.0 | 4.0 |
| Mean completeness | 2.7 | 2.9 |
| Generated UniProt-style summary exact in cached record | not measured | 3/139 collected exports |
| 5/5 correctness | 0% | 51% |
| 1/5 | 11% | 5% |

The SFT model scores lower than RL, consistent with the paper's finding that SFT has "more hallucinations." Generated UniProt-style prose is a concern in both modes: only 3/139 RL strings are exact substrings of the cached UniProt record, and several contain clear factual conflicts. The RL model's claim to "never fabricate InterPro entries" does not extend to UniProt-style summaries.

### Key conclusion

BioReason SFT is a **domain-interpretation narrative engine**, not a biological knowledge system. It adds modest value (~30% of proteins) when domain architectures are diagnostic, but introduces systematic fabrication and false specificity for the remaining ~70%. The proteins where BioReason could add the most value (uncharacterized, minimal annotations) are precisely where it performs worst.
