# BioReason-Pro Comparison Project

Systematic evaluation of BioReason-Pro reasoning traces and GO-GPT predictions (Fallahpour et al. 2026, doi:10.64898/2026.03.19.712954) against expert-curated AIGR gene reviews.

## Summary

We evaluate both the **GO-GPT predictions** (raw GO term lists) and the **BioReason-Pro reasoning traces** (chain-of-thought functional analysis) against our curated reviews across 139 genes and 16 organisms.

Key findings so far (139 RL reviews completed):
- **Correctness: 3.4/5 avg** — decent for core molecular function, unreliable for edge cases
- **Completeness: 2.4/5 avg** — consistently superficial, stays at InterPro-derivable level
- **No gene scored 5/5 on both axes** — BioReason never gives a complete picture
- **Well-studied model organisms score higher**: mouse (4.2) > rat (4.1) > bacteria (~2.8)
- **Critical blind spots**: pseudoenzymes, multi-complex biology, conditional activities, organism-specific context

The GO-GPT raw term lists are overly broad (full GO hierarchy dumps) and add little over existing IBA/IEA. The real value — and the real evaluation target — is the reasoning trace.

## Background

**Architecture (from paper):**
- **GO-GPT**: autoregressive transformer (ESM2 embeddings + organism → GO terms). Upstream predictor.
- **BioReason-Pro**: multimodal reasoning LLM (GO-GPT predictions + InterPro domains → chain-of-thought reasoning trace + functional summary). Two variants: **SFT** (richer mechanistic depth) and **RL** (fewer hallucinations, web app default).

**Key insight:** The GO term list in web exports is raw GO-GPT output (input to reasoning). Per the paper's architecture figure, BioReason-Pro produces its own GO terms as structured output after the `</think>` reasoning step (using Qwen3 backbone with chain-of-thought). However, the current web app export does not separately expose these post-reasoning GO terms — it only includes the GO-GPT input list. We assume this will be fixed before final publication. For now, we evaluate the reasoning traces and functional summaries, not the term lists.

**Web app:** app.bioreason.net (model toggle top-left: SFT / RL)

## Data

### BioReason-Pro web exports
- **139 genes, RL model**: `genes/<org>/<gene>/<gene>-deep-research-bioreason-rl.md`
- **SFT model**: collection in progress (~58/134 as of 2026-03-22 11:45)
- Collected via automated Chrome scraping with triple validation (organism, sequence, format)
- Contains: thinking trace, functional summary, InterPro domains, GO-GPT term list

### GO-GPT prediction YAMLs (139 genes)
- `genes/<org>/<gene>/<gene>-bioreason-rl-predictions.yaml`
- Leaf-filtered via OAK IS_A (17,963 raw → 6,299 leaf terms, 65% reduction)
- PredictionReview schema, `source_method: GO-GPT`
- Low-value for evaluation — same as local GO-GPT, overly broad

### BioReason-Pro RL reviews (139/139 complete)
- `genes/<org>/<gene>/<gene>-bioreason-rl-review.md`
- Agent-curated evaluation of reasoning trace vs curated review
- Scores: Correctness (1-5), Completeness (1-5), freeform analysis

### Test set gene reviews (in progress)
- 99 genes sampled from BioReason paper's test set (10 per organism)
- Standard AIGR reviews being created by 3 parallel agents
- Batch A: 33/33 ✅ | Batch B: 33/33 ✅ | Batch C: 4/33 in progress

## Evaluation rubric

### Correctness (1-5)
- 5: All claims supported by evidence
- 3: Core function right, some wrong claims
- 1: Fundamental mischaracterization

### Completeness (1-5)
- 5: Covers core functions, complexes, pathway context
- 3: Gets the basics, misses significant biology
- 1: Superficial or one-dimensional

### Review format
One markdown file per gene (`*-bioreason-rl-review.md`). Scores at top, freeform analysis below.

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
| Epe1 | 1 | 2 | Pseudoenzyme misclassified as active demethylase |
| SIR2 | 5 | 3 | Core function correct; misses RENT complex, lifespan biology |
| RidA | 3 | 3 | Describes right chemistry but assigns wrong GO function |

## Failure modes

- **Pseudoenzyme blind spot**: Assumes catalytic activity from conserved but degenerate domains
- **Fold/family name bias**: Defaults to protein binding when InterPro family emphasizes scaffold
- **Missing multi-complex biology**: Proteins in multiple complexes get only one described
- **Missing physiological context**: Stays at molecular/structural level, no pathway/organism biology
- **Conditional activity invisible**: Can't detect PTM-dependent or context-dependent functions
- **Negative evidence invisible**: No access to "protein X does NOT do Y" findings
- **Reasoning > term assignment**: Natural language descriptions often more accurate than GO term picks

## Paper case study proteins

Full reasoning traces provided in supplementary C.6–C.15 (SFT, RL, and GPT-5.2 comparisons):

| Protein | UniProt | Paper section | Traces | Key finding |
|---------|---------|---------------|--------|-------------|
| eEFSec | P57772 | Fig. 5, §2.6 | C.6 (SFT), C.7 (RL), C.8 (GPT-5.2) | De novo predicted SBP2 as binding partner, validated by 2.8 Å cryo-EM selenosome structure |
| CFAP61 | Q8NHU2 | Fig. 6, §2.7 | C.9 (SFT), C.10 (RL), C.11 (GPT-5.2) | Correctly identified pseudoenzyme scaffold despite catalytic domain signatures |
| EvoAcr1 | synthetic (169 aa) | §2.8 | C.12 (SFT), C.13 (RL) | AI-designed anti-CRISPR, no homology/domains. Predictions varied by organism label (ribosomal in E. coli, DNA-binding repressor in K12, TF in human). SFT fabricated InterPro entries. |
| EvoAcr2 | synthetic (157 aa) | §2.8 | C.14 (SFT), C.15 (RL) | AI-designed anti-CRISPR. RL predicted phage-encoded host modulator in O157:H7 — biologically coherent. Strong organism-label sensitivity. |

**AIGR review status:**
- eEFSec: not yet reviewed
- CFAP61: ✅ review complete (`feat/review-human-cfap61`)
- EvoAcr1/2: synthetic proteins, deferred for now

### CFAP61 vs Epe1 — same class, opposite results
Both are pseudoenzymes with catalytic domain signatures. BioReason **correctly** identifies CFAP61 as non-enzymatic (paper's featured result) but **fails** on Epe1, confidently calling it an active demethylase. Possible explanations: training data coverage, organism-specific context, or domain-specific cues (CFAP61's exapted residues may be more distinctive).

## Paper evaluation sets & overlap

### Their data
- **Test set**: 8,630 proteins (HuggingFace: `wanglab/bioreason-pro-test-data`), temporal holdout (post Nov 2022)
- **Human eval**: 192 randomly sampled, 162 by 27 external biologists. Protein list not published.
- **Models**: `wanglab/gogpt`, `wanglab/bioreason-pro-sft`, `wanglab/bioreason-pro-rl` on HuggingFace
- **Training data**: `wanglab/bioreason-pro-sft-reasoning-data` (124k), `wanglab/bioreason-pro-rl-reasoning-data` (9.2k)
- **Code**: `bowang-lab/BioReason-Pro` on GitHub

### Test set composition
Dominated by zebrafish (3,899), rat (1,675), human (1,648). These are heavily pre-annotated proteins (zebrafish avg 404 GO terms) — the "temporal holdout" means new experimental annotations were added post-2022, but IBA/IEA already covered most of the GO hierarchy. This makes their Fmax metric less informative than reasoning quality evaluation.

### Overlap with AIGR
Only 7 of our 1,211 reviewed genes appear in their 8,630 test set. Low overlap by design — their test set is newly annotated, ours is deeply characterized.

| UniProt | Gene | BioReason export? |
|---------|------|-------------------|
| Q9HDX8 | SCHPO/alo1 | ✓ RL |
| A0A8M9Q8E3 | DANRE/cryabb | — |
| Q8TCG5 | human/CPT1C | — |
| Q71F56 | human/MED13L | — |
| Q96AW1 | human/VOPP1 | — |
| Q22156 | worm/atf-4 | — |
| G5EED4 | worm/nipi-3 | — |

### Expanding overlap
99 genes sampled from their test set (10 per organism) are being reviewed through the standard AIGR pipeline to increase cross-comparison opportunity.

## SFT vs RL comparison

### Training difference
- **SFT** (Supervised Fine-Tuning): trained on 124k synthetic reasoning traces generated by GPT-5. Learns to mimic expert-style biological reasoning.
- **RL** (Reinforcement Learning): starts from SFT checkpoint, further optimized with DR-GRPO to maximize GO term accuracy. Produces shorter, more focused traces.

### Paper findings (27 external expert evaluators, 162 proteins)
- **SFT**: 8.0/10 avg across 7 axes. Preferred when richer mechanistic depth was needed.
- **RL**: 7.4/10 avg. Preferred when factual reliability mattered — fewer hallucinations, fewer major errors (enzyme misidentification, inverted pathway directionality).
- When experts preferred SFT: advantage in **Mechanistic Depth** (p=3×10⁻³)
- When experts preferred RL: advantage in **fewer claims/hallucinations** (p=4×10⁻²)
- SFT fabricated InterPro entries for novel proteins (EvoAcr); RL did not
- 79% tie-or-exceed rate vs UniProt (SFT), 73% (RL)

### Our observations (5-gene pilot comparison)
From comparing RL vs SFT traces on the same 5 genes (SlyD, Epe1, SIR2, TP53, spo0A):
- **Texts are clearly different** — same biological framework but different wording, emphasis, and detail level
- **SFT traces tend slightly longer** (~10% more text)
- **SFT is more specific**: e.g. spo0A SFT explicitly names "sporulation program" and "two-component signaling pathway" while RL stays generic
- **SFT can be wrong in new ways**: SlyD SFT claims "oligomeric" and "ATP-independent chaperone" — more specific but potentially incorrect
- **Both fail on pseudoenzymes**: Epe1 is called an active demethylase by both SFT and RL
- **RL plays it safe**: SIR2 RL correctly says "NAD-dependent deacetylase at chromatin"; SFT is more generic ("removes acyl groups from protein substrates")

### Hypothesis for full comparison
Based on the paper and our pilot, we predict SFT will score:
- **Higher completeness** (more mechanistic detail, more specific pathway context)
- **Lower correctness** (more hallucinations, more fabricated details)
- This mirrors the paper's finding: SFT = richer but riskier, RL = safer but shallower

### Data collection status
- RL exports: 139/139 ✅
- SFT exports: ~91/139 in progress (automated browser collection)

## Tools

- BioReason web scraper: `/tmp/bioreason_sft_batch.sh` (RL version: `/tmp/bioreason_final.sh`)
- YAML converter: `~/.openclaw/workspace/scripts/bioreason_to_yaml.py`
- Local GO-GPT: `scripts/gogpt_predict.py`
- Agent skill: `.claude/skills/bioreason-predictions.md`

## PR

https://github.com/ai4curation/ai-gene-review/pull/168
