# BioReason-Pro Comparison Project

Systematic evaluation of BioReason-Pro (Fallahpour et al. 2026, doi:10.64898/2026.03.19.712954) predictions against curated AIGR gene reviews.

## Background

BioReason-Pro is a multimodal reasoning LLM for protein function prediction from Arc Institute / UHN / Vector / UofT.

**Architecture:**
- **GO-GPT**: autoregressive transformer (ESM2 embeddings + organism → GO terms). Upstream predictor.
- **BioReason-Pro**: multimodal reasoning LLM (GO-GPT predictions + InterPro domains → chain-of-thought reasoning trace + functional summary). Two variants: SFT and RL (RL is better, web app default).

**Web app:** app.bioreason.net (model toggle top-left: SFT / RL)

**Key insight:** The GO term list in the web export is raw GO-GPT output (input to reasoning). The real BioReason-Pro output is the reasoning trace and functional summary.

## Data

### Raw web exports (139 genes, RL model)
- `genes/<org>/<gene>/<gene>-deep-research-bioreason-rl.md`
- Collected 2026-03-22 via automated browser scraping
- Contains: thinking trace, functional summary, InterPro domains, GO-GPT term list

### GO-GPT prediction YAMLs (139 genes)
- `genes/<org>/<gene>/<gene>-bioreason-rl-predictions.yaml`
- Leaf-filtered (17,963 raw → 6,299 via OAK IS_A ancestor removal)
- PredictionReview schema, `source_method: GO-GPT`
- Low-value — same as local GO-GPT, overly broad

### BioReason-Pro RL reviews (in progress)
- `genes/<org>/<gene>/<gene>-bioreason-rl-review.md`
- Manual/agent-curated evaluation of reasoning trace quality
- Scores: Correctness (1-5), Completeness (1-5), freeform analysis

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
One markdown file per gene. Scores at top, freeform analysis below. Suggested sections:
- What it got right
- What it got wrong
- What it missed
- Failure modes
- Comparison with curated review

## Results so far

| Gene | Organism | Correctness | Completeness | Key finding |
|------|----------|-------------|--------------|-------------|
| Epe1 | S. pombe | 1 | 2 | Pseudoenzyme misclassified as active demethylase |
| SIR2 | S. cerevisiae | 5 | 3 | Core function correct; misses RENT complex, lifespan biology |
| RidA | E. coli | 3 | 3 | Describes right chemistry but assigns wrong GO function |

## Emerging failure modes

- **Pseudoenzyme blind spot**: Assumes catalytic activity from conserved but degenerate domains
- **Fold/family name bias**: Defaults to protein binding when InterPro family emphasizes scaffold
- **Missing multi-complex biology**: Proteins in multiple complexes get only one described
- **Missing physiological context**: Stays at molecular/structural level, no pathway/organism biology
- **Conditional activity invisible**: Can't detect PTM-dependent or context-dependent functions
- **Negative evidence invisible**: No access to "protein X does NOT do Y" findings
- **Reasoning > term assignment**: Natural language descriptions often more accurate than GO term picks

## Paper case study proteins

The paper features two detailed case studies with structural validation:

| Protein | UniProt | Organism | Paper section | Key finding |
|---------|---------|----------|---------------|-------------|
| eEFSec | P57772 | Human | Fig. 5, §2.6 | De novo predicted SBP2 as binding partner, validated by 2.8 Å cryo-EM selenosome structure. Attention maps localize to contact residues. |
| CFAP61 | Q8NHU2 | Human | Fig. 6, §2.7 | Non-enzymatic axonemal scaffold with exapted active site. BioReason correctly overrides superfamily-level catalytic annotation — attention enriched at repurposed residues. |

### Paper evaluation sets
- **Temporal holdout test set**: 8,630 proteins (HuggingFace: `wanglab/bioreason-pro-test-data`), post Nov 2022, avg 26.75 GO terms/protein
- **Human expert evaluation**: 192 proteins randomly sampled from test set; 162 evaluated by 27 external (non-team) biologists
- **DNA-binding attention analysis**: 63 non-training BioLiP proteins
- Test set available on HuggingFace: `wanglab/bioreason-pro-test-data` (parquet)
- **Human eval protein list NOT published** — 192 randomly sampled, only aggregate scores reported
- Code repo: `bowang-lab/BioReason-Pro` on GitHub
- Models on HuggingFace: `wanglab/gogpt`, `wanglab/bioreason-pro-sft`, `wanglab/bioreason-pro-rl`
- Training data: `wanglab/bioreason-pro-sft-reasoning-data` (124k), `wanglab/bioreason-pro-rl-reasoning-data` (9.2k)

### Human eval key findings (from paper)
- 79% tie-or-exceed rate vs UniProt (SFT), 73% (RL)
- Avg 8.0/10 overall (SFT), 7.4/10 (RL) across 7 axes
- SFT preferred when: richer mechanistic depth
- RL preferred when: fewer hallucinations, fewer major errors (enzyme misID, inverted pathway directionality)
- Performance stable across sequence similarity, organism, protein length
- TODO: request 192-protein list from authors for direct comparison

### Overlap with AIGR
Only 7 of our 1,211 reviewed genes appear in their 8,630 test set:

| UniProt | Gene | BioReason export? |
|---------|------|-------------------|
| A0A8M9Q8E3 | DANRE/cryabb | No |
| Q9HDX8 | SCHPO/alo1 | ✓ |
| Q8TCG5 | human/CPT1C | No |
| Q71F56 | human/MED13L | No |
| Q96AW1 | human/VOPP1 | No |
| Q22156 | worm/atf-4 | No |
| G5EED4 | worm/nipi-3 | No |

Low overlap — their test set is temporal holdout (newly annotated post-2022), while our KB focuses on well-studied genes. The value of our comparison is different: we have deep expert-curated reviews to judge reasoning quality, not just GO term F-max.

### Notable: CFAP61 (paper) vs Epe1 (our review) — same class, opposite results
Both are pseudoenzymes with catalytic domain signatures. The paper highlights CFAP61 as a case where BioReason **correctly** overrides the superfamily catalytic annotation and identifies it as a non-enzymatic scaffold. Our Epe1 review (SCHPO) shows BioReason **fails** at the same task — it confidently calls Epe1 an active histone demethylase when it's actually a pseudoenzyme with degenerate active site residues. The difference may be in training data coverage or organism-specific context.

## Tools

- Converter script: `~/.openclaw/workspace/scripts/bioreason_to_yaml.py`
- Local GO-GPT: `scripts/gogpt_predict.py` (same predictions as web, no reasoning trace)
- Batch comparison: `scripts/gogpt_batch.py`, `scripts/gogpt_compare_levels.py`

## PR

https://github.com/ai4curation/ai-gene-review/pull/168
