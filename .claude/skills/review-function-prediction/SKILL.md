---
name: review-function-prediction
description: >
  Review computational protein or gene function predictions and fill PredictionReview
  YAML files using the COR/CNN/LSP/UNC/PLI/NPI/REP biological-validity taxonomy.
  Use for DeepECTF, BioReason/GO-GPT, InterPro2GO, PANTHER/IBA, CLEAN, GloEC,
  MAPred, ProteinInfer, or other predicted EC/GO annotations.
---

# Review Function Prediction

Use this skill to review computational function predictions against allowed evidence and write schema-compatible `PredictionReview` YAML.

the predictions are in YAML alongside the main curation review YAMLs:

`genes/<TAXON>/<GENE>/<GENE>-<TOOL>-predictions-review.yaml`

```yaml
id: <UniProt accession>
gene_symbol: <gene symbol>
locus_tag: <locus tag if available>
taxon:
  id: NCBITaxon:<taxon id>
  label: <organism>
status: COMPLETE
description: >-
  Brief summary of the prediction review outcome, based only on the allowed
  evidence for this review mode.
source_documents:
  - <allowed file path used>
predictions:
  - source_method: <do not change>
    source_version: <do not change>
    source_reference_id: <do not change if present>
    predicted_term:
      id: <do not change>
      label: <do not change>
    predicted_term_type: <EC | GO_MF | GO_BP | GO_CC>
    review:
      assessment: <COR | CNN | LSP | UNC | PLI | NPI | REP>
      confidence_score: <0 | 1 | 2>
      error_type: <omit unless applicable>
      summary: >-
        Explain the decision in 3-8 sentences. State what allowed evidence was
        used, whether the prediction is already present in curated annotations,
        whether it is more or less specific than existing annotations, and why
        the chosen category is justified. If using UNC, explicitly say what
        evidence is missing and avoid speculation.
```

The PMIDs supporting your judgment may come from existing gene reviews

## Assessment Categories

Use these categories for `review.assessment`.

**COR: correct novel prediction.** The predicted function is supported by allowed evidence and is not already present in UniProt/GOA as an equivalent annotation. Be conservative. In curated-annotation-only mode, `COR` requires strong non-literature curated support such as a specific reviewed UniProt functional statement, diagnostic domain/subfamily annotation, or local pathway context. Do not call `COR` merely because the prediction sounds plausible.

**CNN: correct but not novel.** The predicted term is already present in UniProt/GOA, or is an obvious synonym/equivalent of an existing curated annotation. This is correct but not a new discovery.

**LSP: less precise.** The prediction is broadly correct but less specific than an existing curated annotation. Example: predicting generic oxidoreductase activity when the curated annotation specifies the exact substrate or EC reaction.

**UNC: uncertain.** The allowed evidence cannot validate or refute the prediction. This is the default for plausible predictions absent from curated annotations when no allowed evidence establishes them. In curated-annotation-only mode, `UNC` should be common and is not a failure mode.

**PLI: paralog incorrect.** The prediction appears to come from over-propagation within a homologous family or paralog group, and allowed evidence indicates this gene belongs to a different paralog/subfamily/function than the predicted one. Set `error_type: PARALOG_OVERANNOTATION`.

**NPI: nonparalog incorrect.** The prediction is refuted for reasons other than paralog confusion: pathway absent in the organism, predicted process incompatible with taxon or compartment, curated function clearly different, activity belongs to an unrelated gene, or the prediction contradicts allowed evidence. Choose the most specific error type, often `PATHWAY_CONTEXT_IGNORED`, `MULTIPLE_FUNCTIONS`, `CURATION_MISTAKE`, or another schema enum value.

**REP: repetition / frequency bias.** The prediction looks like a high-frequency/default label assigned without supporting sequence or curated evidence, especially common generic enzyme classes such as histidine kinase or PTS transporter. Set `error_type: FREQUENCY_BIAS`.

## Confidence Score

- `2`: concordant with allowed evidence. Use with `COR`, `CNN`, or `LSP`.
- `1`: uncertain. Use with `UNC`.
- `0`: discordant with allowed evidence. Use with `PLI`, `NPI`, or `REP`.

## Judgment Rules

- Prefer `UNC` over confident correctness when the prediction is absent from curated annotations and only weakly suggested by domains.
- Prefer `CNN` over `COR` when the prediction is already in GOA/UniProt, even if the model predicted it correctly.
- Prefer `LSP` over `CNN` when the prediction is correct but materially less specific than the curated annotation.
- Use `PLI` only when the error is specifically homolog/paralog/subfamily confusion.
- Use `NPI` for pathway absence, wrong organismal context, wrong compartment/process, or contradiction by curated function.
- Use `REP` only when the best explanation is a generic high-frequency label rather than a specific biological confusion.
- Do not invent identifiers, publications, or supporting quotes.
