# Recovery and PR batches, 2026-09-22

The interrupted working tree contained 1,679 modified or new files, including
146 changed gene reviews, 343 publication caches, and 187 history records.
The complete recovered state was committed locally as
`2aa3ece27bb2a68b92629358e3eac23d20ff09b8` on
`recovery/iba-treegrafter-20260922` before splitting it. A separate local archive
was also made. This recovery publishes completed edits and their evidence; it
does not claim completion of the corpus-wide audit.

## Pull requests

Shared evidence lands first. The gene batches are independent of one another
and temporarily use the evidence branch as their base; they will target main
once the evidence PR lands. The tracker is merged after the curation batches.
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
| audit-tracker | 0 | Tracker PR (this change) |

## Validation and recovery fixes

- All 146 changed reviews passed source preservation: no original GOA assertion
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
- Strict gene validation, family validation, independent PR review, and CI are
  tracked on the PRs. A created PR is not evidence that these checks passed.

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
