---
species: [human, mouse, rat, worm, yeast, SCHPO, DROME, ARATH, ECOLI, BACSU, PSEPK, DANRE]
sidecars:
  genes: BIOREASON_COMPARISON/genes.csv
---
# BioReason-Pro Comparison Project

Systematic evaluation of BioReason-Pro functional summaries and reasoning traces (Fallahpour et al. 2026, [doi:10.64898/2026.03.19.712954](https://doi.org/10.64898/2026.03.19.712954)) against expert-curated AIGR gene reviews.

**Paper drafts** based on this project live in [`BIOREASON_COMPARISON/article/`](BIOREASON_COMPARISON/article/): see [`manuscript.md`](BIOREASON_COMPARISON/article/manuscript.md) for the full manuscript draft (intended for ISMB 2026 Function-COSI), plus [`abstract.md`](BIOREASON_COMPARISON/article/abstract.md) (long-form) and [`short-abstract.md`](BIOREASON_COMPARISON/article/short-abstract.md) (250 words).

## Methods

We downloaded the reports for selected genes from https://app.bioreason.net/ (there is no API yet so this cannot be done in bulk). We assigned an AI agent to review this, and compare them with both existing pipelines (e.g. interpro2go), and also with the complete AI gene review.

## Notes on browsing results

Each individual gene review page, e.g. aprE, SlyD contains BOTH the bioreason results AND the detailed review of the bioreason results. You will need to search in the page for "bioreason" or scroll down to the sections:

- Deep Research Bioreason RL (we treat the bioreason outputs as a kind of preliminary research)
- Bioreason RL review


## Key findings (139 RL reviews)

1. **BioReason largely recapitulates interpro2go in narrative form.** For most genes, the functional summary does not provide biological insight beyond what InterPro domain annotations already capture. Genuine value-add is modest and concentrated in proteins with distinctive, well-annotated domain architectures such as TOR1 (FRB domain enables pathway-level inference), PTEN, NOTCH1, and EGFR. For standard domain families like Src-family kinases, Fyn and Src receive essentially identical generic descriptions.

2. **Systematic localization errors.** BioReason defaults to "cytosolic" or "cytoplasmic" when no transmembrane domains are detected, failing for periplasmic proteins (Skp, CpxP, Spy), vacuolar proteins (cps1), mitochondrial matrix proteins (alo1, HSP60, CAT2), and ER membrane proteins (IRE1, ETR1). Proteins where InterPro domain names explicitly mention the compartment (KAR2, PDI1) are handled correctly.

3. **Pseudo-enzymes are a blind spot.** BioReason assumes catalytic activity from conserved but degenerate domains and cannot detect loss of catalytic residues. Epe1 (pseudo-demethylase), cts2 (pseudo-chitinase missing catalytic glutamate), and pmp20 (peroxiredoxin that has lost resolving cysteine and functions as a chaperone) are all incorrectly assigned the ancestral enzymatic activity.

4. **Paralogs get identical generic descriptions.** Closely related paralogs such as Fyn/Src (mouse), sigF/sigG/sigK (B. subtilis sporulation sigma factors), and Hspa5/Hspa8 (rat Hsp70 family) receive interchangeable summaries with no gene-specific biology.

5. **Organism-specific biology is consistently absent.** Dauer formation and insulin/IGF-1 signaling in C. elegans (daf-16, daf-2), UPRmt master regulation (atfs-1), sporulation compartment specificity in B. subtilis (sigF forespore, sigK mother cell), prion propagation in yeast (HSP104), and cytoophidium biology (ura7) are all missed.

6. **Mammalian genes score highest** (mouse 4.7, rat 4.4, human 4.2 correctness) while S. pombe scores lowest (2.8). This likely reflects richer InterPro annotations and more informative family-level names for well-studied mammalian proteins.

- **Overall correctness: 3.7/5** | **Overall completeness: 2.9/5**
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
| `{GENE}-deep-research-bioreason-rl.md` | Raw BioReason-Pro RL web export (reasoning trace, functional summary, InterPro, GO-GPT terms) |
| `{GENE}-bioreason-rl-review.md` | Evaluation of reasoning trace vs curated review (correctness/completeness scores + interpro2go comparison) |
| `{GENE}-gogpt-leaf-predictions.yaml` | GO-GPT leaf terms as PredictionReview YAML |
| `{GENE}-ai-review.yaml` | Expert-curated AIGR review (ground truth for comparison) |

## Evaluation rubric

### Correctness (1-5)
- 5: All claims supported by evidence
- 3: Core function right, some wrong claims
- 1: Fundamental mischaracterization

### Completeness (1-5)
- 5: Covers core functions, complexes, pathway context
- 3: Gets the basics, misses significant biology
- 1: Superficial or one-dimensional

Each review includes a comparison with interpro2go (GO_REF:0000002) annotations to assess whether BioReason adds value beyond automated domain-based annotation.

## Results (139 genes)

### Score distribution

| Score | Correctness | Completeness |
|-------|-------------|--------------|
| 5 | 38 (27%) | 1 (1%) |
| 4 | 48 (35%) | 40 (29%) |
| 3 | 32 (23%) | 51 (37%) |
| 2 | 15 (11%) | 40 (29%) |
| 1 | 6 (4%) | 7 (5%) |

### By organism

| Organism | n | Correctness | Completeness |
|----------|---|-------------|--------------|
| mouse | 11 | 4.7 | 3.6 |
| rat | 12 | 4.4 | 3.6 |
| human | 19 | 4.2 | 3.4 |
| ARATH | 3 | 4.0 | 3.3 |
| yeast | 11 | 3.9 | 2.6 |
| BACSU | 13 | 3.8 | 2.9 |
| DROME | 8 | 3.8 | 2.8 |
| worm | 15 | 3.5 | 2.3 |
| PSEPK | 8 | 3.4 | 3.0 |
| ECOLI | 13 | 3.2 | 3.0 |
| SCHPO | 23 | 2.8 | 2.3 |

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
| TOR1 | yeast | 4 | FRB domain enables pathway-level inference |
| ftsZ | BACSU | 4 | Tubulin-like GTPase domain is highly specific |
| spo0A | BACSU | 4 | Response regulator + DNA-binding domains clearly predict phosphorelay TF |
| GroEL | ECOLI | 4 | Chaperonin domains are unambiguous |
| lgg-1 | worm | 4 | Atg8/ubiquitin-like fold directly predicts autophagy adaptor |
| bst1 | SCHPO | 3 | GPI inositol-deacylase function nailed from specific family annotation |

### Critical failures (correctness 1/5)

| Gene | Organism | Completeness | Failure mode |
|------|----------|--------------|--------------|
| atg16 | SCHPO | 1 | No InterPro domains available; confabulated carbohydrate metabolism |
| pmp20 | SCHPO | 2 | Neo-functionalized peroxiredoxin -> chaperone; model assumes ancestral function |
| pol5 | SCHPO | 1 | Predicted cytokinesis scaffold; actual function is rDNA transcription |
| Shu1 | SCHPO | 1 | Predicted HECT ubiquitin ligase; actually a GPI-anchored heme receptor |
| csr-1 | worm | 1 | Wrong input sequence (nhr-47 instead of CSR-1 Argonaute) |
| pgl-1 | worm | 1 | Described as nuclear TF scaffold; actually cytoplasmic P granule component |

## Failure mode taxonomy

### 1. Pseudo-enzyme blind spot

BioReason assumes catalytic activity from conserved domains without checking whether catalytic residues are intact. This is a systematic failure for proteins that retain an ancestral fold but have lost enzymatic activity.

**Examples:**
- **Epe1** (SCHPO, 2/5): BioReason claims *"JmjC catalytic center dictates a lysine demethylase mechanism"* but Epe1 has degenerate active site residues (HVD instead of HXD, Tyr307 instead of catalytic His). No detectable demethylase activity in mass spec assays. Functions as anti-silencing factor through HP1/Swi6 binding.
- **cts2** (SCHPO, 2/5): Called an active chitinase, but the protein lacks the essential catalytic glutamate and is likely catalytically dead.
- **pmp20** (SCHPO, 1/5): Predicted as a peroxidase, but has lost its resolving cysteine and functions as a molecular chaperone.

Notably, the BioReason paper highlights CFAP61 as a correctly identified pseudoenzyme, but this success does not generalize to our test set.

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

### 8. Wrong input data

- **csr-1** (worm, 1/5): BioReason received the nhr-47 sequence instead of the CSR-1 Argonaute. All predictions are for the wrong protein.

## Comparison with interpro2go

A central question is whether BioReason provides value beyond the automated interpro2go pipeline (GO_REF:0000002). Our reviews assessed this for each gene.

**In most cases, BioReason is a narrative restatement of interpro2go.** The functional summary translates domain annotations into prose without adding new biological insight. Where interpro2go makes errors (e.g., assigning generic "protein binding" to CnoX, importing eukaryotic flagellar terms for B. subtilis divIVA), BioReason typically recapitulates and sometimes amplifies these errors.

**BioReason adds value in specific cases:**
- Proteins with distinctive multi-domain architectures where the combination is diagnostic (TOR1, NOTCH1, PTEN, EGFR, spo0A)
- Proteins where family-level InterPro names are highly informative (Uggt1, bst1, KAR2)

**BioReason inherits interpro2go errors:**
- KEAP1: interpro2go assigns BTB-Kelch to actin binding; BioReason amplifies this into "actin remodeling" instead of the correct NRF2 regulation
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
- SFT collection: 135/139 complete

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

The web app shows "GO GPT" and "GO Leaf" panels regardless of SFT/RL selection. These are always **GO-GPT predictions** (the upstream model), not BioReason-Pro output. BioReason-Pro is fundamentally a narrative reasoning model -- it takes GO-GPT's GO terms as input and produces a reasoning trace + functional summary. It does not independently predict GO terms.

The HF catalogue's structured GO section (at the end of the `generation` column) appears to be reformulated from the GO-GPT input, not independent predictions. ~97% of entries have this structured section; ~3% are truncated.

**RL model GO predictions are not accessible anywhere.** The web app shows GO-GPT (input), the HF catalogue is SFT only, and the RL reasoning trace does not emit its own GO terms.

| Source | GO-GPT (input) | BioReason SFT GO | BioReason RL GO |
|--------|----------------|------------------|-----------------|
| Web app panels | "GO GPT" + "GO Leaf" | Not shown separately | Not shown separately |
| HF `protein_catalogue` | In `<think>` block | Structured section at end | **Not available** |
| Scraped `-rl.md` files | Full hierarchy in GO Terms section | N/A | **Not emitted** |

### SlyD (P0A9K9) cross-source comparison

We compared GO terms for SlyD across three sources to understand the relationship between them:

**Website SFT scrape** (`SlyD-deep-research-bioreason.md`, 9 terms -- leaf-pruned):
GO:0003755 (PPIase activity), GO:0016859, GO:0140096, GO:0016853, GO:0003824, GO:0006457, GO:0005737, GO:0005829, GO:0005622

**Website RL scrape** (`SlyD-deep-research-bioreason-rl.md`, 58 terms -- full GO-GPT with all ancestors):
Includes the above plus metal binding (GO:0008270, GO:0005507, GO:0016151, GO:0050897), unfolded protein binding (GO:0051082), heat response (GO:0009408), refolding (GO:0042026), stabilization (GO:0050821), and all ancestor terms up to root.

**HF SFT catalogue** (structured section, 13 terms):
GO:0051082, GO:0003755, GO:0008270, GO:0005507, GO:0016151, GO:0050897 (MF);
GO:0009408, GO:0022417, GO:0042026, GO:0044008, GO:0050821, GO:0000413 (BP);
GO:0005829 (CC)

**Key finding**: 12 of 13 HF SFT terms are contained in the RL website GO-GPT output. The one HF-only term (GO:0044008, modulation by symbiont of host adenylate cyclase pathway) is a more specific descendant also present in the RL hierarchy. The website RL dump includes the full GO hierarchy (all ancestors up to root), while the HF SFT keeps leaf-ish terms. The website SFT scrape was pruned to very generic parent terms.

This confirms all three sources derive from the same GO-GPT predictions, just pruned/presented differently. The HF catalogue is the most useful bulk source since it retains informative leaf terms without ancestor noise.

### Coverage gaps

Notable proteins NOT in the 223K catalogue: TP53 (P04637), EGFR (P00533), NOTCH1 (P46531), MTOR (P42345). Several well-known proteins that are present have truncated generations (cut off mid-sentence, never reaching the GO section): MYC (P01106), BCL2 (P10415), PTEN (P60484), CTNNB1 (P35222).

## SFT Catalogue Evaluation (45 proteins, 15 clades)

Full details: [research/bioreason-sft-evaluation.md](/research/bioreason-sft-evaluation.md)

We evaluated 45 proteins from the HF SFT catalogue across 15 clades (DANRE, DICDI, METJA, MYCTU, PSEAE, ANOGA, ARATH, DROME, ECOLI, SCHPO, human, mouse, rat, worm, yeast), 3 proteins per clade, mixing well-characterized and poorly-characterized proteins.

**Overall: Correctness 2.9/5, Completeness 2.7/5**

### Score distribution

| Score | Correctness | Completeness |
|-------|:-----------:|:------------:|
| 5 | 0 (0%) | 0 (0%) |
| 4 | 12 (27%) | 1 (2%) |
| 3 | 20 (44%) | 28 (62%) |
| 2 | 7 (16%) | 10 (22%) |
| 1 | 4 (9%) | 4 (9%) |
| 0 | 1 (2%) | 1 (2%) |

These results are consistent with the RL evaluation (139 genes): **overall correctness 3.7/5, completeness 2.9/5** (RL scores slightly higher, as expected from the paper's claim that RL has fewer hallucinations).

### Top failure modes (SFT catalogue)

1. **Fabricated UniProt summaries (7/45 = 16%)**. BioReason generates fake "UniProt Summary" text for uncharacterized proteins. All 7 cases are on proteins where UniProt says "Uncharacterized protein." This is systematic and dangerous — it misrepresents an authoritative database.

2. **Paralog/family conflation (8/45 = 18%)**. Biology from well-characterized family members is applied to divergent paralogs: mlcD (calmodulin→myosin I LC), rdgBbeta (vibrator→Class II PITP), Ndufb1/NDUFAB1 confusion, Ifi204/AIM2 conflation, Hmgcs2/HMGCS1 mixing.

3. **Organism-specific biology absent (systematic)**. Not once in 45 proteins did BioReason provide organism-specific insight beyond domain architecture. Mosquito eye pigmentation, Mtb drug targets, yeast cell wall biology, worm body size regulation, plant cold stress — all missed.

4. **Inverse quality vs characterization**. Proteins with 0-3 GOA annotations (where BioReason could add most value) consistently score 0-1/5. Well-characterized proteins (where BioReason scores 4/5) already have extensive annotations making the narrative redundant.

5. **Hallucinated GO IDs**. BioReason cites specific GO IDs that map to completely different terms (e.g. GO:0047554 cited as caffeoyl-CoA O-methyltransferase, actually 2-pyrone-4,6-dicarboxylate lactonase).

6. **Directional errors**. Several errors get the mechanism exactly backwards: CRH1 donor-acceptor direction, Sstr5 ligand preference, gcl substrate clearance direction, CHL1 cell death promotion vs limitation.

### Comparison: SFT catalogue vs RL web scrapes (139 genes)

| Metric | SFT catalogue (45) | RL web scrapes (139) |
|--------|:------------------:|:--------------------:|
| Mean correctness | 2.9 | 3.7 |
| Mean completeness | 2.7 | 2.9 |
| Fabricated UniProt summaries | 16% | not assessed |
| 5/5 correctness | 0% | 27% |
| 1/5 or worse | 11% | 4% |

The SFT model scores lower than RL, consistent with the paper's finding that SFT has "more hallucinations." The fabricated UniProt summary rate (16%) is particularly concerning and was not systematically assessed in the RL evaluation. The RL model's claim to "never fabricate InterPro entries" (from the paper) does not extend to UniProt summaries in SFT.

### Key conclusion

BioReason SFT is a **domain-interpretation narrative engine**, not a biological knowledge system. It adds modest value (~30% of proteins) when domain architectures are diagnostic, but introduces systematic fabrication and false specificity for the remaining ~70%. The proteins where BioReason could add the most value (uncharacterized, minimal annotations) are precisely where it performs worst.
