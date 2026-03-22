# BioReason-Pro Predictions

BioReason-Pro (doi:10.64898/2026.03.19.712954) is a multimodal reasoning LLM for protein function prediction.

## Architecture
- **GO-GPT**: autoregressive transformer (ESM2 embeddings + organism → GO terms). This is the upstream predictor.
- **BioReason-Pro**: takes GO-GPT predictions + InterPro domains → chain-of-thought reasoning trace + functional summary. Two variants: **SFT** (supervised fine-tuning) and **RL** (reinforcement learning, better).
- Web app: app.bioreason.net (Google auth, model toggle top-left, default RL)
- Local GO-GPT (`scripts/gogpt_predict.py`) produces identical GO terms to the web. The web's added value is the reasoning trace.

## File naming
- `{GENE}-deep-research-bioreason-{rl|sft}.md` — raw web export (provenance). Contains: thinking trace, functional summary, InterPro domains, GO terms (full hierarchy).
- `{GENE}-bioreason-{rl|sft}-predictions.yaml` — structured PredictionReview YAML with leaf-only GO terms. References the md via `source_file` field.
- `{GENE}-gogpt-predictions.yaml` — from LOCAL GO-GPT model runs (same GO terms, no reasoning trace).

## Converting web exports to YAML
```bash
source .venv/bin/activate
python ~/.openclaw/workspace/scripts/bioreason_to_yaml.py --model rl [--dry-run] [--overwrite]
```
- Reads `*-deep-research-bioreason.md` from `~/worktrees/agr-bioreason/genes/`
- Filters to leaf terms via OAK IS_A ancestor removal (~65% reduction)
- Outputs PredictionReview-conformant YAML (no extra fields)
- Reasoning trace stays in the markdown file, not the YAML
