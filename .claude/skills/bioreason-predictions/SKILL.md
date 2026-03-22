---
name: bioreason-predictions
description: >
  Work with BioReason-Pro predictions and reasoning traces for protein function.
  Use when: comparing BioReason outputs against curated reviews, converting web exports
  to YAML, reviewing reasoning trace quality, or running the SFT/RL comparison.
  Triggers: "bioreason", "GO-GPT predictions", "reasoning trace review",
  "bioreason comparison", "SFT vs RL".
---

# BioReason-Pro Predictions

## Architecture

- **GO-GPT**: autoregressive transformer (ESM2 + organism → GO terms). Upstream predictor.
- **BioReason-Pro**: Qwen3-based reasoning LLM (GO-GPT + InterPro + PPI + organism → chain-of-thought reasoning trace + functional summary + GO terms). Two variants: **SFT** and **RL**.
- Web app: app.bioreason.net (model toggle top-left). Default: RL.
- Paper: doi:10.64898/2026.03.19.712954

## Key distinction

The GO term list in web exports (`### GO Terms`) is raw **GO-GPT input**, not BioReason-Pro output. The true BioReason-Pro output is the reasoning trace, functional summary, and post-reasoning GO terms (not yet exposed in web export).

## File naming

| File | Content |
|------|---------|
| `{GENE}-deep-research-bioreason-rl.md` | Raw RL web export (provenance) |
| `{GENE}-deep-research-bioreason-sft.md` | Raw SFT web export (provenance) |
| `{GENE}-bioreason-rl-predictions.yaml` | GO-GPT leaf terms as PredictionReview YAML |
| `{GENE}-bioreason-rl-review.md` | Evaluation of RL reasoning trace vs curated review |
| `{GENE}-gogpt-predictions.yaml` | Local GO-GPT model predictions (same terms as web) |

## Reviewing a reasoning trace

Create `{GENE}-bioreason-rl-review.md` with:

```markdown
# BioReason-Pro RL Review: {GENE} ({organism})

Source: {GENE}-deep-research-bioreason-rl.md

- **Correctness**: X/5
- **Completeness**: X/5

{freeform analysis}
```

Scoring:
- **Correctness** (1-5): Are claims accurate? 5=all supported, 3=core right with errors, 1=fundamentally wrong
- **Completeness** (1-5): Important biology covered? 5=comprehensive, 3=basics only, 1=superficial

Read the `-deep-research-bioreason-rl.md` (reasoning trace) and `-ai-review.yaml` (curated review), then compare.

## Converting web exports to YAML

```bash
python ~/.openclaw/workspace/scripts/bioreason_to_yaml.py --model rl [--dry-run] [--overwrite]
```

Leaf-filters via OAK IS_A ancestors (~65% reduction). See `references/converter.md` for details.

## Project doc

Full comparison results, failure modes, and SFT vs RL analysis in `projects/BIOREASON_COMPARISON.md`.
