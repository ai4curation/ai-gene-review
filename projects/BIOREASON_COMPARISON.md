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

## Tools

- Converter script: `~/.openclaw/workspace/scripts/bioreason_to_yaml.py`
- Local GO-GPT: `scripts/gogpt_predict.py` (same predictions as web, no reasoning trace)
- Batch comparison: `scripts/gogpt_batch.py`, `scripts/gogpt_compare_levels.py`

## PR

https://github.com/ai4curation/ai-gene-review/pull/168
