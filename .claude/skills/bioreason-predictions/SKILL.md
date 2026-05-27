---
name: bioreason-predictions
description: >
  Work with BioReason-Pro predictions and reasoning traces for protein function.
  Use when: comparing BioReason outputs against curated reviews, converting web exports
  to YAML, reviewing reasoning trace quality, or running the SFT/RL comparison.
  Triggers: "bioreason", "GO-GPT predictions", "reasoning trace review",
  "bioreason comparison", "SFT vs RL".
---

# BioReason-Pro-RL Predictions

## About

BioReason-Pro-RL is a pipeline for producing functional summaries of genes, along with reasoning traces, and other raw material (including high recall function predictions)

- Web app: app.bioreason.net (model toggle top-left). Default: RL.
- Paper: doi:10.64898/2026.03.19.712954


We store these in:

 `{GENE}-deep-research-bioreason-{rl,sft}.md`
 
 We are primarily interested in the higher precision RL results rather than just Supervised Fine Tuning (SFT)
 
 ## Structure of a bioreason report
 
 A bioreason report is structured as a markdown doc in these parts:
 
 * Metadata (organism and sequence)
 * Thinking/Reasoning trace -- the models exposed internal trace of thoughts as to why it arrived at its conclusions
 * Functional summary -- a consise summary of what the function of the gene is
 * Other details
    * Uniprot summary (imported)
    * Interpro domains (from running it as part of pipeline)
    * GO Terms (upstream ESM autoregressive transformer predictions -- high recall, low precision)

We are generally NOT interested in the GO terms in this report. We know in advance these over-predict, they are just their to show provenance of the reasoner.

## File naming

| File | Content |
|------|---------|
| `{GENE}-deep-research-bioreason-{rl,sft}.md` | Raw RL web export (provenance) |
| `{GENE}-gogpt-leaf-predictions.yaml` | GO-GPT leaf terms as PredictionReview YAML (renamed from bioreason-rl-predictions.yaml) |
| `{GENE}-bioreason-rl-review.md` | Evaluation of RL reasoning trace vs curated review |

## Reviewing a reasoning trace

Create `{GENE}-bioreason-rl-review.md` with:

```markdown
# BioReason-Pro RL Review: {GENE} ({organism})

Source: {GENE}-deep-research-bioreason-rl.md

- **Correctness**: X/5
- **Completeness**: X/5

## Functional Summary Review

{freeform analysis}

Comparison with interpro2go:

{comparison{

## Notes on thinking trace

{freeform analysis}

```

Make sure the main `-ai-review.yaml` is done first.

When doing the review DO NOT bother looking at the GO terms in the output. These are raw ESM results we know they over-predict. Not interesting.

You must focus on the functional summary and evaluate it for completeness and correctness. You must provide additional narrative details explaining why you arrived at the conclusions, and how the summary differs from what we know. Although the functional summary from bioreason is narrative and not ontology terms, your review may choose to align the narrative details with GO terminology (IDs not required, just text) for comparison purposes.

Your review should quote sections of the functional summary verbatim where you wish to highlight something. E.g.

> the functional summary said "kinase that acts on ..." but in fact it is a pseudokinase...

You can also look at the thinking trace and provide notes on it, but this is NOT score-driving. The main focus is the one-paragraph section "Functional Summary" in `{GENE}-deep-research-bioreason-rl.md`

Also perform a comparison with interpro2go GO_REF:0000002, which you will find in the ai-review.yaml. I am particularly interested in whether BioReason is just doing a fancy recapitulation of interpro2go (and whether it recapitulates the same mistakes) or if there is additional biological insight.

Scoring:
- **Correctness** (1-5): Are claims accurate? 5=all supported, 3=core right with errors, 1=fundamentally wrong
- **Completeness** (1-5): Important biology covered? 5=comprehensive, 3=basics only, 1=superficial

Read BOTH the `-deep-research-bioreason-rl.md` (reasoning trace) and `-ai-review.yaml` (curated review), then compare.

## Project doc

Full comparison results, failure modes, and SFT vs RL analysis in `projects/BIOREASON_COMPARISON.md`.
