---
name: fill-gene-review-checklist
description: Fill in and check the gene-review checklist (rubrics/gene_review.yaml, linkml-checklist-validator / `lcv`) for each gene review a PR changes, with honest reasons and verbatim evidence. Use after a gene review YAML is final and before opening its PR.
---

# Filling the gene-review checklist

The checklist is a receipt for one gene review. A reviewer reads it to decide
where to look, so a `fail` that you report and fix is worth more than a `pass`
you cannot back up. This is a warn-only pilot: no CI job runs it yet, but
`lcv check` must pass before you open the PR.

## Setup

```bash
uv tool install git+ssh://git@github.com/ai4curation/linkml-checklist-validator   # provides `lcv`
```

## Steps

1. Finish the review first: `just validate <org> <GENE>` passes and the
   history record exists (`just new-history ... --agent-tool <tool> --model <model-id>`).
   Checklist keys follow the review's annotations, including WITH/FROM, so if you
   edit or refetch the review afterwards, regenerate or re-check.
2. Write the skeleton under `rubrics/checklists/`, named by the history record's session id
   (not under `history/`, where every YAML file is validated as a history record):

   ```bash
   SID=<session id of this PR's history record, e.g. 2026-11-25T151334Z-claude-code-51526b>
   lcv skeleton rubrics/gene_review.yaml genes/<org>/<GENE>/<GENE>-ai-review.yaml \
     -o rubrics/checklists/genes/<org>/<GENE>/$SID.checklist.yaml
   ```

   One checklist per changed gene review. Never retype or invent keys.
3. Fill every `FILL_IN` and every reason starting `INSTRUCTIONS:`. The comment
   above each item is its requirement. An empty list is `[]`. Set
   `status: completed`, `reviewer` (agent tool and model id, e.g.
   `claude-code / claude-opus-5-5`) and a quoted `timestamp`.
4. Check it, and fix every line it prints:

   ```bash
   lcv check rubrics/gene_review.yaml rubrics/checklists/genes/<org>/<GENE>/$SID.checklist.yaml \
     genes/<org>/<GENE>/<GENE>-ai-review.yaml
   ```

   `missing:` means an annotation or reference you have not covered.
   `duplicate:` means two annotations are identical on every key field; that is
   a defect in the review (often per-partner IPI rows whose `supporting_entities`
   were dropped), so fix the review rather than the checklist.

## Verdicts

- `pass`: you checked this artifact and the requirement holds. The reason names
  what you looked at.
- `fail`: it does not hold. Give `remediation`. If you fix the review before the
  PR, re-check and change the verdict to `pass`, saying what changed.
- `not_applicable`: the requirement does not apply (e.g. `goa_empty_explained`
  when the GOA file has rows). Never use it for "I did not get to this" and
  never guess: an item you could not check is a `fail` with a remediation, or an
  entry under `not_examined` with its reason.

## What each item asks

- `review_file_validates`: run `just validate <org> <GENE>`; the evidence is the
  command and the real closing line of its output.
- `history_record_names_model`: the record's `actors[]` name the agent tool and
  the model that actually did the work. Cite the record's path and the line of
  the `model:` entry.
- `goa_empty_explained`: only applies when `<GENE>-goa.tsv` is empty or header-only.
- `curated_lines_weighed`: you read the UniProt FUNCTION / CATALYTIC ACTIVITY /
  SUBUNIT / SUBCELLULAR LOCATION lines and the experimental GOA rows, and no
  experimental row was REMOVEd from an abstract-only reading (CLAUDE.md, "Do not
  overrule curators from incomplete evidence").
- `publications_checked`: every `references[].id` is under `examined` or under
  `not_examined` with its own reason.
- `annotation_reviews`: one entry per judged row. `decision_has_evidence` repeats
  a `supporting_text` quote verbatim; `supporting_text_not_title` fails if a quote
  is only the cited paper's (or Reactome event's) title; `action_matches_reason`
  fails if, say, an ACCEPT's reason argues the term is too general. A row whose
  quotes all come from a source other than its own `original_reference_id` fails
  `decision_has_evidence` unless the reason explains why.
- `new_annotation_reviews`: one entry per `NEW` row, for the CLAUDE.md bar (the
  gene does the work, comparators checked with a query shown able to return a
  positive, parents and GO-CAMs read, no redundancy). `{}` when there are none.
- `source_defects_confident_enough`: CONFIRMED wrong-gene or wrong-reference
  claims need a full read or an obvious abstract/record.

## Reasons and evidence

- A reason is specific: "The REMOVE quotes PMID:19663506 saying NOS inhibitors
  were tested against DDAH1, so the row has the direction reversed", not "Checked".
- `reference_id` + `excerpt`: copy the excerpt verbatim from the source. Do not
  paraphrase, tidy or join sentences, and never use a title as the excerpt.
- `file_path` + `line` + `excerpt`: a real path, line number and the line's text, so
  the receipt still checks if a refetch moves the line. Nothing in the repo checks
  excerpts for you (`just validate-quotes` reads only `supporting_text`): copy tabs
  as tabs.
- `command` + `output_digest`: a command you actually ran and part of its real output.
- `entity_id` + `entity_label`: the label as the source gives it.

See `rubrics/examples/` for a filled example and `docs/gene_review_checklists.md`
for the convention.
