# Curated-Annotation-Only Recapitulation Prompt

Use this prompt for **Arm A** of the `ESR-ECOLI-DET-Mini` recapitulation experiment: a blinded, curated-annotation-only review of computational predictions.

````text
You are performing a blinded, curated-annotation-only prediction review.

Goal:
For each gene, review the computational prediction(s) in the assigned `*-predictions-review.yaml` stub and fill in the `review:` section using only the allowed local evidence. The purpose is to test whether an agent can approximate a curator's biological-validity classification from curated database annotations, without literature review and without access to the published de Crécy-Lagard answer key.

Hard restrictions:
- Do not use web search.
- Do not inspect git history.
- Do not open project-level benchmark files, manuscripts, slides, notebooks, or summary tables.
- Do not open prior completed review files if present, including completed `*-ai-review.yaml`, completed `*-predictions-review.yaml`, `*-notes.md`, `*-deep-research*.md`, or any derived review/report files.
- Do not open the `publications/` folder.
- Do not use PMID:40703034 or any de Crécy-Lagard paper text, labels, or rationale.
- If the allowed evidence is insufficient, use `UNC`. Do not infer hidden literature support.

Allowed evidence:
- The assigned prediction stub itself: method, predicted EC/GO term, predicted label.
- UniProt flat file for the gene.
- GOA/QuickGO annotation table for the gene.
- InterPro/domain/family annotations if present locally.
- Organism/taxon identity.
- Local pathway/database summaries only if explicitly included in the blind bundle.
- Ontology term definitions for EC/GO terms, if needed to understand term meaning.

Task:
Fill the prediction review YAML in the schema-compatible format. Keep the prediction metadata unchanged. Fill or update:
- top-level `description`
- each prediction's `review.assessment`
- `review.confidence_score`
- `review.error_type` when applicable
- `review.summary`
- omit `review.supported_by` unless the blind bundle contains a citable local source with exact quoted text.

Assessment categories:

COR = Correct novel prediction.
Use when the predicted function appears correct from allowed evidence, but is not already present in UniProt/GOA as an equivalent annotation. Be conservative. In this no-literature arm, COR requires strong curated non-literature support such as a highly specific protein name, reviewed UniProt functional statement, diagnostic domain/subfamily annotation, or pathway context. Do not call COR merely because the prediction sounds plausible.

CNN = Correct but not novel.
Use when the predicted term is already present in UniProt/GOA, or is an obvious synonym/equivalent of an existing curated annotation. This is correct but not a new discovery. Confidence score should usually be 2.

LSP = Less precise.
Use when the prediction is broadly correct but less specific than an existing curated annotation. Example: predicting "oxidoreductase activity" when the curated annotation already specifies the exact substrate or EC reaction. This is not wrong, but adds little value. Confidence score should usually be 2.

UNC = Uncertain.
Use when the allowed curated evidence cannot validate or refute the prediction. This is the default for plausible predictions absent from GOA/UniProt when no allowed evidence establishes them. Use UNC for "could be true, but I cannot tell from curated annotations alone." Confidence score must be 1.

PLI = Paralog incorrect.
Use when the prediction appears to come from over-propagation within a homologous family or paralog group, and allowed evidence indicates this gene belongs to a different paralog/subfamily/function than the predicted one. Look for mismatched gene names, family/subfamily names, domain combinations, known paralog functions in UniProt/InterPro, or curated annotations assigning the activity to a different related protein. Confidence score must be 0. Set `error_type: PARALOG_OVERANNOTATION`.

NPI = Nonparalog incorrect.
Use when the prediction is refuted for reasons other than paralog confusion: the organism lacks the pathway, the predicted process is biologically incompatible with the taxon or compartment, the curated function is clearly different, the activity belongs to an unrelated gene, or the prediction contradicts UniProt/GOA/InterPro evidence. Confidence score must be 0. Choose the best error type, often `PATHWAY_CONTEXT_IGNORED`, `MULTIPLE_FUNCTIONS`, `CURATION_MISTAKE`, or another enum value if appropriate.

REP = Repetition / frequency bias.
Use when the prediction looks like a high-frequency/default label assigned without supporting sequence or curated evidence, especially common generic enzyme classes such as histidine kinase or PTS transporter, and allowed evidence gives no matching domain/family/function. Confidence score must be 0. Set `error_type: FREQUENCY_BIAS`.

Confidence score:
- 2 = concordant with allowed curated evidence: COR, CNN, or LSP.
- 1 = uncertain: UNC.
- 0 = discordant with allowed curated evidence: PLI, NPI, or REP.

YAML shape:

```yaml
id: <UniProt accession>
gene_symbol: <gene symbol>
locus_tag: <locus tag if available>
taxon:
  id: NCBITaxon:<taxon id>
  label: <organism>
status: COMPLETE
description: >-
  Brief summary of the prediction review outcome, based only on curated
  annotations and other allowed local evidence.
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
        whether it is more/less specific than existing annotations, and why the
        chosen category is justified. If using UNC, explicitly say what evidence
        is missing and avoid speculation.
```

Important judgment rules:
- Prefer `UNC` over confident correctness when the prediction is absent from curated annotations and only weakly suggested by domains.
- Prefer `CNN` over `COR` when the prediction is already in GOA/UniProt, even if the model predicted it correctly.
- Prefer `LSP` over `CNN` when the prediction is correct but materially less specific than the curated annotation.
- Use `PLI` only when the error is specifically homolog/paralog/subfamily confusion.
- Use `NPI` for pathway absence, wrong organismal context, wrong compartment/process, or contradiction by curated function.
- Do not cite or mention de Crécy-Lagard, PMID:40703034, `ESR-ECOLI-DET-Mini`, or any published label/rationale.
- End by validating the YAML if the validation command is available.
````

## Experimental Note

This arm intentionally withholds literature. `UNC` should therefore be common and is not a failure mode. The output should measure what can be recovered from curated annotations and local database context alone.
