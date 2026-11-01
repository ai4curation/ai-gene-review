# Proposed ontology changes

A review can conclude that a GO (or UBERON, CL, CHEBI …) term is *itself* wrong,
not merely that an annotation used the wrong term. `proposed_ontology_changes`
is where that goes.

## What it is for, and what it is not

Three things in this repository look adjacent and are not interchangeable:

| You want to say | Use |
|---|---|
| this term should not exist, or should say something different | `proposed_ontology_changes` |
| a term that **does not exist** should be created | `proposed_new_terms` |
| an annotation **record** is wrong (wrong gene, wrong term, wrong evidence code) | `review.source_defects` |

The first two are requests to an ontology; the third is a request to whoever
curated an annotation. The distinction that matters most in practice: obsoleting
a term does **not** repoint the annotations that use it. A review that finds both
problems records both, and they go to different trackers.

`proposed_new_terms` is deliberately left alone — it covers creation, it is used
in several hundred reviews, and a `ProposedOntologyTerm` is a KGCL
`ClassCreation` in disguise that could fold in later if anyone wants it to.

## Where it lives

Three homes, in increasing scope:

- **a gene review** (`genes/*/*/*-ai-review.yaml`), top level — when the change
  was noticed while curating one gene;
- **a module review** (`modules/*.yaml`), top level — subtree-level obsoletions
  are usually noticed while curating a pathway rather than a single gene;
- **a project page's frontmatter** (`projects/**/*.md`) — when the change spans
  several terms and MOD groups and so belongs to no single gene or module. The
  `projects/*_OBSOLETION.md` pages are exactly that case.

A gene or module review is schema-validated, so `linkml-validate` checks the
block's structure. **A project page is markdown and LinkML never sees it**, so
the structure is checked by `validate_change_entries`, which reads the required
fields, the allowed fields and the permissible `change_type` values out of the
schema file rather than restating them. `tests/test_project_frontmatter.py`
applies it to every project page, and `render-projects` reports what it rejects
as page warnings.

### Structural errors exclude; policy violations do not

Two severities, and the distinction is deliberate. A **structural** problem — a
missing required field, an unknown field, a `change_type` outside the enum, a
term field with no `id` — makes the entry unusable: the renderer drops it, the
exporter will not ship it, and the frontmatter test fails. A **policy**
violation is advisory: the entry still renders and still exports, and it shows
up as a page warning and in `check_ontology_change_policy` at WARNING severity,
exactly as on a gene or module review.

Getting this wrong is what the first version of the project-page gate did: it
excluded an otherwise fine entry because its `report_status: FIXED` carried no
tracker link. A missing link is worth flagging and is not grounds for dropping
the record.

## It is KGCL, wrapped

`change_type` names a class from
[KGCL](https://github.com/INCATools/kgcl) (Knowledge Graph Change Language), and
each permissible value carries that class's URI as its `meaning`. The structured
slots carry the KGCL class's own fields, so a proposal can be emitted as KGCL and
applied with `oaklib apply`. `kgcl_schema` is already an indirect dependency via
`oaklib`, so this costs nothing extra.

What KGCL does *not* model is the argument for a change. `justification`,
`supported_by`, `confidence` and `report_status` are this repository's additions,
following the pattern `SourceDefect` already uses, and they are the reason to
record a proposal here rather than only in a tracker. `confidence` and
`report_status` reuse the source-defect enums deliberately: the values mean the
same thing, and a parallel enum would drift.

### The DSL is checked by KGCL's own parser

`change_dsl` holds the change in KGCL's controlled English
(`obsolete GO:0099022 with replacement GO:7770062`). It is redundant with the
structured slots **on purpose**, so that a disagreement between the two is
detectable rather than silent. Validation parses it with KGCL's own lark grammar
and reports three things: a statement that does not parse (`dsl_unparseable`),
one that names a different term from the slots (`dsl_disagrees`), and one that
parses as a different KGCL class from the declared `change_type`
(`dsl_wrong_kind`).

Leaning on the real grammar rather than a hand-written pattern matters, because
the grammar is narrower than it looks. **KGCL's DSL has no statement for a
merge, a mapping predicate change, or a mapping removal**, even though it has
classes for the first of those. For those change types leave `change_dsl` unset;
the structured slots and the justification carry the request. `kgcl_dsl()`
renders a statement only when KGCL's parser accepts it, so the exporter never
emits a string that looks like KGCL and is not.

Other grammar details worth knowing before hand-writing a `change_dsl`:

- a definition change is `change definition of X to '…'` — there is no `from` clause;
- there is **no syntax for a non-direct replacement** (`consider`), so a correct
  DSL for `NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT` is a bare
  `obsolete GO:…` even when `has_nondirect_replacement` lists alternatives.

### Direct versus non-direct replacement

This is the distinction to get right, because it decides whether anything can be
fixed mechanically.

- `has_direct_replacement` becomes GO's `term replaced by`. It says the two terms
  denote the same thing, so annotations can be repointed without re-curation.
- `has_nondirect_replacement` becomes `consider`. It is advice; a curator must
  choose per annotation.

A biological process obsoleted in favour of a molecular function is **never** a
direct replacement, however obviously the MF is "the" answer — the five vesicle
tethering BPs all point at `GO:7770062 vesicle membrane tethering activity`
through `consider`, and GO records no `term replaced by` for any of them.

## Example

From `modules/dmel_exocyst.yaml`:

```yaml
proposed_ontology_changes:
- change_type: NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT
  ontology: GO
  about_node:
    id: GO:0090522
    label: vesicle tethering involved in exocytosis
  has_nondirect_replacement:
  - id: GO:7770062
    label: vesicle membrane tethering activity
  change_dsl: obsolete GO:0090522
  justification: >-
    Tethering is a binding activity, not a process … recorded as a non-direct
    replacement because a biological process cannot be replaced outright by a
    molecular function.
  confidence: CONFIRMED
  report_status: FIXED
  term_tracker_issue: https://github.com/geneontology/go-annotation/issues/6375
```

## Reporting

```bash
just export-ontology-changes
```

Writes `reports/ontology-changes.tsv` plus one Markdown report per ontology in
`reports/ontology-changes/` — each ontology has its own tracker, so the report is
grouped the way the request is actually sent. Both paths are gitignored, for the
same reason the source-defect report is: they aggregate every review, so
committing them makes every curation PR conflict.

Rows with `report_status` `FIXED` or `DECLINED` are left out of the Markdown,
since there is nothing left to send; they stay in the TSV as a record.

## What is checked

`check_ontology_change_policy` warns (never blocks) on:

- an obsoletion-with-replacement or a merge that names no surviving term, and a
  non-direct obsoletion that names one anyway;
- a value change (definition, label, synonym, mapping predicate) missing its old
  or new value, or proposing a value identical to the current one;
- an edge change missing the other end of the edge or the relation — reparenting
  a term and adding a `part_of` link to it are different requests;
- a term offered as its own replacement;
- a `COMPLEX_CHANGE` or `OTHER` with a justification under 20 words: those carry
  no KGCL semantics, so the prose is the whole request. KGCL has
  `NodeDirectMerge` but no split, so a class split is a `COMPLEX_CHANGE` whose
  justification must name the terms that should replace it;
- a `report_status` saying the request was filed with no tracker issue linked;
- a `change_dsl` that does not parse, disagrees with the slots, or parses as the
  wrong KGCL class;
- a term proposed for obsoletion that the same review `ACCEPT`s on an annotation
  row — `ACCEPT` means the term is a core function of the gene, which contradicts
  asking for its obsoletion. `MODIFY` with the replacement is the consistent pair.

What is **not** checked: whether the ontology should actually make the change,
which no rule can settle, and whether `about_node` exists and carries the stated
label, which is the term validator's job.

## Two shapes, from the two projects backfilled so far

The direct/non-direct distinction is the thing to get right, and the two cases
already recorded show both answers to it.

**`VESICLE_TETHERING_OBSOLETION` — no direct replacement.** Five BPs obsoleted
in favour of one MF, `GO:7770062 vesicle membrane tethering activity`. GO records
**no** `replaced_by` for any of them: a biological process cannot be replaced
outright by a molecular function, so the MF is `consider` and a curator picks the
transport process to hang it on. All five are
`NODE_OBSOLETION_WITH_NO_DIRECT_REPLACEMENT` with one
`has_nondirect_replacement`.

**`AMINO_ACID_ACTIVATION_OBSOLETION` — a direct replacement *and* advice.** 43
substrate-specific tRNA aminoacylation BPs, each obsoleted with a formal
`replaced_by` pointing at its block's generic process (`GO:0006418` cytosolic,
`GO:0070127` mitochondrial) — a BP replaced by a BP, which is legitimate — while
GO's obsoletion comment separately names the 1:1 molecular function to annotate
instead. So each entry carries `has_direct_replacement` (the BP) *and* a
`has_nondirect_replacement` (the MF). Both, on one entry.

The rule that survives both: **what can be repointed mechanically goes in
`has_direct_replacement`; what needs a curator's judgement per annotation goes in
`has_nondirect_replacement`.** Whether the replacement happens to be in the same
GO aspect is a consequence, not the test.

## What is still open

**A large uniform batch should be generated, not transcribed.** Only four of the
43 amino-acid-activation terms are recorded structurally — two cytosolic, two
mitochondrial, enough to pin both shapes. The other 39 are mechanically derivable
from the markdown tables already on that page, and hand-writing them would
duplicate those tables in a second format with no new information. A generator
that reads a project's own tables is the right answer; nobody has written one.

**Both pages' audits were stale, and in the same direction.** Vesicle tethering
recorded two of five terms obsolete as of 2026-09-26; all five are. Amino acid
activation recorded all 43 live as of 2026-08-29; the four rechecked are
obsolete. In both cases the ontology moved and the page did not. Nothing here
detects that: `report_status` is a curator's assertion, and no check compares it
against the live ontology. A periodic audit that re-queries each `about_node` and
flags a `NOT_REPORTED` change whose term is already obsolete would close the
loop, and would have caught both.
