---
species: [human, mouse, rat, worm, yeast, SCHPO, DROME, ARATH, ECOLI, BACSU, PSEPK, DANRE]
sidecars:
  genes: BIOREASON_COMPARISON/genes.csv
---
# BioReason-Pro Comparison Project

Systematic evaluation of BioReason-Pro functional summaries and reasoning traces (Fallahpour et al. 2026, [doi:10.64898/2026.03.19.712954](https://doi.org/10.64898/2026.03.19.712954)) against expert-curated AIGR gene reviews.

## Summary

We evaluate **BioReason-Pro functional summaries and reasoning traces** — chain-of-thought analyses that reason from InterPro domains, PPI data, and organism context to predict protein function — against our curated reviews across 139 genes and 16 organisms.

Key findings (139 RL reviews):
- **Correctness: 3.4/5** — decent for core molecular function, unreliable for edge cases
- **Completeness: 2.4/5** — consistently superficial, stays at InterPro-derivable level
- **No gene scored 5/5 on both axes** — BioReason never gives a complete picture
- **Model organisms score higher**: mouse (4.2) > rat (4.1) > bacteria (~2.8)
- **Critical blind spots**: pseudoenzymes, multi-complex biology, conditional activities, organism-specific context

## Background

**Architecture:**
- **GO-GPT**: autoregressive transformer (ESM2 embeddings + organism → GO terms). Upstream predictor.
- **BioReason-Pro**: Qwen3-based multimodal reasoning LLM. Takes GO-GPT predictions + InterPro + PPI + organism context → chain-of-thought reasoning trace + functional summary. Two variants: **SFT** (richer mechanistic depth) and **RL** (fewer hallucinations).

The GO term list in web exports is raw GO-GPT output (input to reasoning). BioReason-Pro produces its own GO terms after the reasoning step, but the current web app does not separately expose these.

**Web app:** [app.bioreason.net](https://app.bioreason.net) | **Code:** [bowang-lab/BioReason-Pro](https://github.com/bowang-lab/BioReason-Pro) | **Models:** [HuggingFace wanglab collection](https://huggingface.co/collections/wanglab/bioreason-pro)

## Data

Per gene, the following files are available (example: [ECOLI/SlyD](https://github.com/ai4curation/ai-gene-review/tree/main/genes/ECOLI/SlyD)):

| File | Description |
|------|-------------|
| [`{GENE}-deep-research-bioreason-rl.md`](https://github.com/ai4curation/ai-gene-review/blob/main/genes/ECOLI/SlyD/SlyD-deep-research-bioreason-rl.md) | Raw BioReason-Pro RL web export (reasoning trace, functional summary, InterPro, GO-GPT terms) |
| [`{GENE}-bioreason-rl-review.md`](https://github.com/ai4curation/ai-gene-review/blob/main/genes/ECOLI/SlyD/SlyD-bioreason-rl-review.md) | Evaluation of reasoning trace vs curated review (correctness/completeness scores + analysis) |
| [`{GENE}-bioreason-rl-predictions.yaml`](https://github.com/ai4curation/ai-gene-review/blob/main/genes/ECOLI/SlyD/SlyD-bioreason-rl-predictions.yaml) | GO-GPT leaf terms as PredictionReview YAML |
| [`{GENE}-ai-review.yaml`](https://github.com/ai4curation/ai-gene-review/blob/main/genes/ECOLI/SlyD/SlyD-ai-review.yaml) | Expert-curated AIGR review (ground truth for comparison) |

## Evaluation rubric

### Correctness (1-5)
- 5: All claims supported by evidence
- 3: Core function right, some wrong claims
- 1: Fundamental mischaracterization

### Completeness (1-5)
- 5: Covers core functions, complexes, pathway context
- 3: Gets the basics, misses significant biology
- 1: Superficial or one-dimensional

One markdown file per gene with scores at top and freeform analysis below.

## Results (139 genes)

### Score distribution

| Score | Correctness | Completeness |
|-------|-------------|--------------|
| 5 | 15 (11%) | 0 (0%) |
| 4 | 57 (41%) | 5 (4%) |
| 3 | 37 (27%) | 57 (41%) |
| 2 | 22 (16%) | 67 (48%) |
| 1 | 8 (6%) | 10 (7%) |

### By organism

| Organism | Correctness | Completeness | n |
|----------|-------------|--------------|---|
| mouse | 4.2 | 2.7 | 11 |
| rat | 4.1 | 2.8 | 12 |
| human | 3.7 | 2.4 | 19 |
| yeast | 3.5 | 2.5 | 11 |
| DROME | 3.5 | 2.2 | 8 |
| worm | 3.3 | 2.1 | 15 |
| ECOLI | 3.1 | 2.5 | 13 |
| SCHPO | 2.9 | 2.5 | 23 |
| BACSU | 2.8 | 2.2 | 13 |
| PSEPK | 2.8 | 2.4 | 8 |

### Critical failures (correctness ≤ 1)
Epe1 (pseudoenzyme), Spy, Shu1, atg16, pol5, csr-1, pgl-1, pmp20

### Highlighted reviews

| Gene | Correctness | Completeness | Key finding |
|------|-------------|--------------|-------------|
| [Epe1](https://github.com/ai4curation/ai-gene-review/blob/main/genes/SCHPO/Epe1/Epe1-bioreason-rl-review.md) | 1 | 2 | Pseudoenzyme misclassified as active demethylase |
| [SIR2](https://github.com/ai4curation/ai-gene-review/blob/main/genes/yeast/SIR2/SIR2-bioreason-rl-review.md) | 5 | 3 | Core function correct; misses RENT complex, lifespan biology |
| [RidA](https://github.com/ai4curation/ai-gene-review/blob/main/genes/ECOLI/RidA/RidA-bioreason-rl-review.md) | 3 | 3 | Describes right chemistry but assigns wrong GO function |

## Detailed examples of disagreement

### Pseudoenzyme misclassification: Epe1

BioReason says: *"JmjC catalytic center dictates a lysine demethylase mechanism that consumes Fe(II) and 2-oxoglutarate."*

Our review: Epe1 has **degenerate active site residues** (HVD instead of HXD motif, Tyr307 instead of catalytic His). Mass spectrometry assays show **no detectable demethylase activity**. It functions through protein-protein interactions (HP1/Swi6 binding, SAGA recruitment), not catalysis.

### Right chemistry, wrong function: RidA

BioReason says: *"Non-enzymatic yet catalytic chaperone-like module that binds and dissipates reactive enamine/imine intermediates, accelerating their hydrolysis."*

Our review: The description of the chemistry is **correct** — but RidA IS an enzyme (EC 3.5.99.10, deaminase). BioReason's own words describe the enzymatic activity ("accelerating their hydrolysis") then assigns GO:0005515 (protein binding) instead of GO:0019239 (deaminase activity). The InterPro family name emphasizes the scaffold, biasing the model away from recognizing catalysis.

### Localization errors: ETR1, CpxP, Skp, Spy

BioReason systematically misassigns **membrane/periplasmic proteins as cytoplasmic** when InterPro annotations lack transmembrane domains:
- **ETR1** (Arabidopsis ethylene receptor): Called "soluble cytoplasmic signal transducer." Actually an ER membrane integral protein with 3 TM helices forming the ethylene-binding site.
- **CpxP**: Called cytoplasmic. Actually periplasmic (has signal peptide, confirmed by crystal structure).
- **Skp**: Reasoning concludes cytoplasmic chaperone while the GO terms listed include periplasmic space — internal contradiction.
- **Spy**: Misidentified as Cpx signaling adaptor. Actually a periplasmic holdase/foldase chaperone.

### Anti-folding chaperone: SecB

BioReason assigns GO:0006457 (protein folding). Our review flags this as **wrong** — SecB is an *anti-folding* holdase that actively prevents stable tertiary contacts. The curated review cites Bechtluft et al. showing SecB "completely prevents stable tertiary contacts." This is a frequency-bias error where chaperone family associations pull in protein folding terms.

### Cross-kingdom fold bias: aprE (B. subtilis subtilisin)

BioReason correctly identifies the serine endopeptidase activity but then predicts **human hemostasis/blood coagulation** biological processes for a B. subtilis enzyme. This fold-bias artifact comes from subtilisin-family annotations dominated by human proteins in the training data.

### Means vs. ends: comK

BioReason assigns protein homooligomerization (GO:0051260) as the primary biological process. While ComK does tetramerize, that's the **means** — the actual function is competence establishment (GO:0030420). BioReason confuses the structural mechanism with the biological purpose.

## Failure modes

- **Pseudoenzyme blind spot**: Assumes catalytic activity from conserved but degenerate domains
- **Fold/family name bias**: Defaults to protein binding when InterPro family emphasizes scaffold
- **Missing multi-complex biology**: Proteins in multiple complexes get only one described
- **Missing physiological context**: Stays at molecular/structural level, no pathway/organism biology
- **Conditional activity invisible**: Can't detect PTM-dependent or context-dependent functions
- **Negative evidence invisible**: No access to "protein X does NOT do Y" findings
- **Reasoning > term assignment**: Natural language descriptions often more accurate than GO term picks

## Paper case study proteins

Full reasoning traces in supplementary C.6–C.15:

| Protein | UniProt | Paper section | Key finding |
|---------|---------|---------------|-------------|
| eEFSec | P57772 | Fig. 5, §2.6 | De novo predicted SBP2 as binding partner, validated by cryo-EM |
| CFAP61 | Q8NHU2 | Fig. 6, §2.7 | Correctly identified pseudoenzyme scaffold despite catalytic domains |
| EvoAcr1 | synthetic | §2.8 | No homology/domains. Predictions varied by organism label. SFT fabricated InterPro. |
| EvoAcr2 | synthetic | §2.8 | RL predicted phage-encoded host modulator — biologically coherent |

### CFAP61 vs Epe1 — same class, opposite results

Both are pseudoenzymes with catalytic domain signatures. BioReason **correctly** identifies CFAP61 as non-enzymatic (paper's featured result) but **fails** on Epe1, confidently calling it an active demethylase.

### Section 2.8: short proteins and peptides

| Protein | Size | Result |
|---------|------|--------|
| HLA-A, p53, BRINP2, IA-2 | full | Accurate |
| preproinsulin, CCK, GDF15 | ~110 aa | Mixed — correct family, missed key functions |
| GLP-1 | 30 aa | Failed — conflated with glucagon |
| GAD65/IA-2 epitopes | short | SFT fabricated InterPro entries; RL did not |

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
- **Overlap with AIGR**: 7 of 1,211 genes. Low by design — their test set is newly annotated, ours is deeply characterized.
- 99 additional genes from their test set are being reviewed to expand overlap.

## PR

https://github.com/ai4curation/ai-gene-review/pull/168
