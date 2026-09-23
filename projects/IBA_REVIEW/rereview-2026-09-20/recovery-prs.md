# Recovery and PR batches, 2026-09-22

The interrupted working tree contained 1,679 modified or new files, including
146 scientific gene re-reviews, 343 publication caches, and 187 history records.
The complete recovered state was committed locally as
`2aa3ece27bb2a68b92629358e3eac23d20ff09b8` on
`recovery/iba-treegrafter-20260922` before splitting it. A separate local archive
was also made. This recovery publishes completed edits and their evidence; it
does not claim completion of the corpus-wide audit.

## Pull requests

Ten initial batches merged independently. The remaining curation batches were
stacked in the order microbial enzymes (#3109), TreeGrafter (#3110), then
autophagy (#3114), with this tracker (#3120) last. Each returns to main after
its parent merges; auto-merge is disabled while its base is another recovery
branch. This preserves one consistent derived GO-GPT report and benchmark
sidecars at every step, including the article's matching Table S8.
Each batch retains the relevant gene history, research, hypothesis reports, and
analytical evidence. Family-review changes travel with the genes they discuss.

| Batch | Genes | PR |
| --- | ---: | --- |
| evidence-cache | 0 | [#3107](https://github.com/ai4curation/ai-gene-review/pull/3107) |
| csr1-identity | 1 | [#3108](https://github.com/ai4curation/ai-gene-review/pull/3108) |
| microbial-enzymes | 20 | [#3109](https://github.com/ai4curation/ai-gene-review/pull/3109) |
| treegrafter-divergence | 13 | [#3110](https://github.com/ai4curation/ai-gene-review/pull/3110) |
| dictyostelium | 10 | [#3111](https://github.com/ai4curation/ai-gene-review/pull/3111) |
| plastid-and-plant | 8 | [#3112](https://github.com/ai4curation/ai-gene-review/pull/3112) |
| chaperones | 12 | [#3113](https://github.com/ai4curation/ai-gene-review/pull/3113) |
| autophagy-and-organelles | 14 | [#3114](https://github.com/ai4curation/ai-gene-review/pull/3114) |
| lipid-metabolism | 13 | [#3115](https://github.com/ai4curation/ai-gene-review/pull/3115) |
| enzyme-and-rna-specificity | 17 | [#3116](https://github.com/ai4curation/ai-gene-review/pull/3116) |
| signaling-and-pseudoenzymes | 20 | [#3117](https://github.com/ai4curation/ai-gene-review/pull/3117) |
| localization-and-divergence | 18 | [#3118](https://github.com/ai4curation/ai-gene-review/pull/3118) |
| fulltext-flags | 5 | [#3119](https://github.com/ai4curation/ai-gene-review/pull/3119) |
| audit-tracker | 0 | [#3120](https://github.com/ai4curation/ai-gene-review/pull/3120) |

## Validation and recovery fixes

- The 146 scientific re-reviews and five additional reference-availability-only
  edits make 151 changed gene reviews. The latter do not advance scientific audit
  status. All 151 passed source preservation: no original GOA assertion
  was lost or mutated. CSR-1 is the explicitly registered exception, with the
  original mixed-identity files preserved byte-for-byte and the canonical fetched
  sources and seed checked by SHA-256.
- The retired CSR-1 review now ends in `.yaml.snapshot`, preventing active-review
  discovery from treating the archived record as another curated gene. Its bytes
  and recorded hash are unchanged.
- Every changed gene has matching history. The 1,319 history records present at
  recovery passed schema validation; recovery follow-ups are validated separately.
- The SAMD8 focused follow-up had been copied both into its full-gene assessment
  and into a second top-level gene record, causing `inventory.py` to fail on a
  duplicate. The latter is now retained under `focused_followups`; its content is
  identical to the incorporated follow-up. The progress generator succeeds and
  counts each gene once.
- All 146 original scientific re-reviews passed strict local gene validation.
  All 244 family records passed; the residue audit had 1,411 passes and one
  pre-existing unresolved negative control. Project frontmatter tests passed
  (636 tests). Subsequent gene fixes and history additions are validated before
  completion. Independent approval and CI remain separate PR merge gates.
- The source checker refuses an incomplete batch checkout before writing its
  output. Run it on the assembled recovery branch, or main after all gene batches
  have merged; a tracker-only checkout cannot regenerate the full report.

## Unfinished scientific work

The regenerated progress report records **81 reviewed**,
**65 awaiting adjudication**, and **3281 unreviewed** genes
against the immutable 3,427-gene baseline. These are audit statuses, not merge
statuses. `reviewed` can still carry explicit human follow-up questions.

The recovered local runner records contain 90 `report_ready` outputs and one
`report_recovered_from_cancelled_job` output. These are the statuses recorded on
disk, not a fresh assertion about remote jobs. Availability of a report does not
establish that its reasoning has been incorporated. For entries still awaiting
adjudication, inspect the existing report and primary evidence before launching
another request. No new provider jobs were commissioned during PR packaging.

`active-work.yaml` preserves historical worker assignments and execution handles
from the interrupted session. They are not live coordination state. Consult the
per-gene audit records, notes, hypothesis directories, and
`adjudication-requests.yaml` for the actual unresolved questions.

The main IBA and TreeGrafter project findings pages are unchanged by this recovery.

## Second opinions and follow-ups from PR review

- The ATG2A report argues that loss of yeast Nvj1/Vac8 junction machinery
  excludes nuclear microautophagy. Resolve lysosomal route equivalence and the
  report's acknowledged orthology limits before changing UNDECIDED.
- WIPI2's existing report supports shared selective-autophagy machinery but
  leaves paralog-specific dependence unresolved. Gene reasons now explicitly
  incorporate this alternative; no new report is needed.
- A1BG receptor capacity remains unresolved despite supported peripheral
  membrane association. CDH23 direct catenin binding and indirect complex
  membership remain separate questions; the report's false no-catenin claim is
  not supporting evidence.
- Inspect the donor chemistry in RHEA:36079 versus GO:0002950 before changing
  projects/RHEA/rhea2go.sssom.yaml or RHEA-GAP-CASES.md. Phosphatidylethanolamine
  and CDP-ethanolamine donors are chemically different; changing exactMatch to
  broadMatch alone does not establish a valid mapping.
- Availability-only edits do not constitute fresh full-text scientific review.
  Empty findings and abstract-derived findings may merit later enrichment.

Superseded ACTL8 and Pmp20 donor assessments are preserved in explicitly labeled
comparison artifacts alongside the current gene reviews. They retain the
historical evidence trail without reinstating unsupported conclusions.

Two initial recovery history filenames retain the scaffolder default claude-code
actor slug. Their agent metadata correctly identifies Codex; the immutable
scaffolded session identifiers were retained.

## Completion checks

All 1,679 originally recovered paths are assigned to the batches above, except
for the intentionally renamed CSR-1 archive whose bytes and hash are preserved.
The comparison JSON, figure, Table S8 and deterministic benchmark sidecars are
regenerated together. The full audit remains at 81 reviewed, 65 awaiting
adjudication and 3,281 unreviewed; publishing these batches does not change that
scientific-work denominator. Final merge status is recorded on the linked PRs.


## Provenance formatting repairs

The tracking PR also repairs 101 inspected separators/word boundaries across 27 recovered gene
reviews and notes, including already merged batches. This does not add scientific
re-reviews or change annotation actions. Parsed source fields, term objects and
verbatim supporting quotations are unchanged; filenames and accession namespaces
are preserved. The exact before/after tokens are recorded in
[prose-identifier-repairs.json](prose-identifier-repairs.json). Two existing comparator
citations now have fetched publication caches (PMID:7558035 and PMID:9678974).
The NCGR_LOCUS1270 identity fractions retain their original digits and gain readable
spacing. Each changed gene has a matching history record.

The repair map is an explicit, bounded log. It also records the inspected residual
Bcl2 citations and quantitative/figure spacing; it does not claim that every
stylistic spacing choice in the corpus was normalized.
