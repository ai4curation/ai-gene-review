# Prediction browser

Open [the shared prediction browser](../app/predictions/index.html) to explore
computational predictions across methods, species, and evaluation projects.
The same files work directly from a local checkout and on GitHub Pages.

The **Prediction sets** view contains one record per source document, method,
and source version. It includes GO/EC outputs, explicitly empty prediction
lists, and functional summaries with or without reviews. An empty list has zero term claims;
an absent list is unknown, and a narrative has no term-claim count. A reviewed
empty output can describe supported omissions without inventing a prediction
or assigning it a correctness score.

The **Claims** view contains emitted GO/EC predictions, with their recorded
VDCL categories, review scores, error types, rationale, and evidence. Each
claim links back to its prediction set. BioReason narrative correctness and
completeness use a separate 1–5 scale, visible in set cards and TSV exports.
The model's functional summary and the review evaluation are separate fields.
ProtNLM narrative categories describe judgments present within a narrative;
they do not supply a whole-record score or add GO claims.

Use facets for method, source version, species, project, cohort, output type,
output state, and review state. The Claims view also offers assessment and
error facets. Search, filters, and the selected view are stored in the URL,
so a project can link to a saved selection. For example:

- [ProtNLM fly records](../app/predictions/index.html?source_method=ProtNLM2&species=DROME)
- [BioReason comparison records](../app/predictions/index.html?projects=BIOREASON_COMPARISON)
- [DeepECTF claims](../app/predictions/index.html?dataset=claims&source_method=DeepECTF)

The visible **Current representation** filter prefers a leaf-term file only
when a full-term file identifies the same gene, method, and source version.
Clearing that filter reveals both; distinct versions remain separate. Copied
experiment files under `projects/` are not counted as additional observations.
The catalog discovers canonical prediction YAML and supported ProtNLM/BioReason
narrative formats under `genes/`; it does not turn ordinary GOA annotations
into predictions. A missing sidecar does not establish empty model output.

An explicit pending rationale remains **Awaiting review**, including a seeded
`UNC`; automatic comparison summaries remain **Automatic comparison**. These
states are distinct from a substantive reviewed `UNC`. Existing assessments
and scores are preserved, with inconsistencies flagged in quality notes.
Narrative registry hashes and BioReason input-quality metadata are checked
where available; stale metadata and wrong-input cases remain visible.

Run `just deploy-predictions-browser` to regenerate `app/predictions/`.
`just build-pages` and the scheduled page-generation workflow also regenerate
it. The exporter reads canonical sources and generates `data.js`; it does not
edit curated reviews. `source-files.json` lists dynamically linked repository
files so Pages staging includes the underlying reviews and model outputs.
