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


We store raw RL exports in:

 `{GENE}-bioreason-rl-predictions.md`
 
 We are primarily interested in the higher precision RL results rather than just Supervised Fine Tuning (SFT)
 
 ## Structure of a bioreason report
 
 A bioreason report is structured as a markdown doc in these parts:
 
 * Metadata (organism and sequence)
 * Thinking/Reasoning trace -- the models exposed internal trace of thoughts as to why it arrived at its conclusions
 * Functional summary -- a concise summary of what the function of the gene is
 * Other details
    * UniProt-style summary (model-generated; not imported from UniProt)
    * Interpro domains (from running it as part of pipeline)
    * GO Terms (upstream ESM autoregressive transformer predictions -- high recall, low precision)

We are generally NOT interested in the GO terms in this report. We know in advance these over-predict; they are there to show provenance of the reasoner.

## File naming

| File | Content |
|------|---------|
| `{GENE}-bioreason-rl-predictions.md` | Raw RL web export (provenance) |
| `{GENE}-deep-research-bioreason-sft.md` | Raw SFT web export when available (provenance) |
| `{GENE}-gogpt-leaf-predictions.yaml` | GO-GPT leaf terms as PredictionReview YAML |
| `{GENE}-bioreason-rl-review.md` | Evaluation of RL reasoning trace vs curated review |

## Reviewing a reasoning trace

Create `{GENE}-bioreason-rl-review.md` with:

```markdown
# BioReason-Pro RL Review: {GENE} ({organism})

Source: {GENE}-bioreason-rl-predictions.md

- **Correctness**: X/5
- **Completeness**: X/5

## Functional Summary Review

{freeform analysis}

Comparison with interpro2go:

{comparison}

## Notes on thinking trace

{freeform analysis}

```

Make sure the main `-ai-review.yaml` is done first.

When doing the review DO NOT bother looking at the GO terms in the output. These are raw ESM results we know they over-predict. Not interesting.

You must focus on the functional summary and evaluate it for completeness and correctness. You must provide additional narrative details explaining why you arrived at the conclusions, and how the summary differs from what we know. Although the functional summary from bioreason is narrative and not ontology terms, your review may choose to align the narrative details with GO terminology (IDs not required, just text) for comparison purposes.

Your review should quote sections of the functional summary verbatim where you wish to highlight something. E.g.

> the functional summary said "kinase that acts on ..." but in fact it is a pseudokinase...

You can also look at the thinking trace and provide notes on it, but this is NOT score-driving. The main focus is the one-paragraph section "Functional Summary" in `{GENE}-bioreason-rl-predictions.md`

Also compare the narrative with the supplied InterPro domain/family labels. Where the AIGR file actually contains `GO_REF:0000002`, separately compare against that InterPro2GO mapping. Do not call the domain-label comparison an InterPro2GO baseline when no such annotation exists. Assess whether BioReason simply narrates its supplied domain evidence, recapitulates a mapping error, or adds biological insight.

### Scoring scope

Score only the one-paragraph **Functional Summary**. The reasoning trace, raw GO-GPT/ESM
terms, InterPro output, and model-generated UniProt-style summary may be discussed as
diagnostics, but they do not affect either score. The InterPro2GO comparison is likewise a
separate analysis, not a score component.

Treat correctness and completeness as independent axes:

- Missing true biology lowers **completeness only**. An accurate but narrow summary can be
  `5/2`.
- A false or unsupported claim lowers **correctness only**. If the summary nevertheless
  covers all important biology, it can be `4/5`.
- Do not lower correctness for omitted functions, specificity, mechanism, phenotype, or
  biological context. Do not lower completeness merely because a stated claim is wrong;
  lower completeness only when the correct core biology is itself absent.
- Do not charge errors found only in the reasoning trace, GO term list, or UniProt-style
  section to the Functional Summary scores.

### Correctness anchors

- **5/5**: Every substantive claim in the Functional Summary is supported by the current
  curated review; there are no material factual errors. The summary may still be incomplete.
- **4/5**: The central function is accurate, with one limited factual error, overstatement,
  or unsupported detail that does not change the main functional interpretation.
- **3/5**: The core interpretation is recognizable and mostly right, but one or more
  meaningful errors or unsupported extensions make the summary only partly reliable.
- **2/5**: Some relationship to the real protein is recognizable (for example the correct
  family, domain, or broad process), but a central mechanistic, catalytic, localization,
  organism-context, or functional claim is wrong.
- **1/5**: The protein's identity or core function is fundamentally mischaracterized, so
  the Functional Summary is largely unusable for this gene.

### Completeness anchors

- **5/5**: Covers all, or nearly all, core functions plus the major mechanism, location,
  and biological context established in the curated review.
- **4/5**: Covers all central functions but omits one secondary role or useful mechanistic
  or contextual detail.
- **3/5**: Covers at least one main function but omits another important core role, pathway,
  mechanism, or location.
- **2/5**: Captures only a narrow or generic fragment and misses most distinctive or
  important biology.
- **1/5**: Provides essentially no meaningful coverage of the gene's established core
  biology.

### Input and provenance checks

- Verify that the accession, organism, and input sequence match the reviewed gene. Record a
  wrong-input case as a pipeline/data-quality failure and flag it for exclusion from model
  performance aggregates rather than treating it as an ordinary model error.
- Check whether the sequence was truncated, especially at the BioReason 2,000-residue input
  limit. State which missing domains/functions could be affected and flag the case for a
  truncated-input stratum. Still score only what the Functional Summary actually says.
- The exported section titled `UniProt Summary` is generated by BioReason in a UniProt-like
  format. It is not evidence that the text came from UniProt. Never blame or credit UniProt
  for that text unless it has been independently verified against the cached UniProt record.
- Use the current `-ai-review.yaml`, not an older TODO or draft description quoted in a
  prior comparison. If the reference review has materially changed, re-adjudicate the
  narrative against the current file.
- Do not infer evidence from an output label. Support factual corrections with the curated
  review and its cited literature; when evidence is unresolved, say so rather than inventing
  a definitive correction.

Read BOTH the `-bioreason-rl-predictions.md` (reasoning trace) and `-ai-review.yaml` (curated review), then compare.

## Project doc

Full comparison results, failure modes, and SFT vs RL analysis in `projects/BIOREASON_COMPARISON.md`.
