---
id: MF-2
title: Annotate at the depth this row's evidence supports, and refine only on that evidence
status: proposed
topic: MF
provenance: GOC_PLUS
aspects:
- F
evidence_codes:
- IDA
- IEA
go_terms:
- term_id: GO:0004930
  label: G protein-coupled receptor activity
- term_id: GO:0004941
  label: beta2-adrenergic receptor activity
- term_id: GO:0003674
  label: molecular_function
- term_id: GO:0005488
  label: binding
related:
- MF-11
differences:
- prior_source: CLAUDE.md before the 2026-11-14 ruling
  prior_said: '`TOO_GENERAL` usable for any general term with a specific term elsewhere, including `GO:0004930`'
  we_recommend: '`TOO_GENERAL` only for terms imprecise on their own; `MODIFY` needs the row''s own evidence'
  why: Two reviews read the enum in opposite ways; earlier reviews are not retroactively defective
sources:
- kind: repo
  title: CLAUDE.md
  path: CLAUDE.md
- kind: repo
  title: action consistency
  path: docs/action_consistency.md
- kind: wiki
  title: Guidelines for catalytic activity terms
  url: https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms
date: '2026-11-15'
---

# MF-2. Annotate at the depth this row's evidence supports, and refine only on that evidence

## Decision

Choose the most specific term that the cited evidence supports. In review, a correct
but general term is `MODIFY` only when the row's own evidence supports a named deeper
term; otherwise keep it. `TOO_GENERAL` is for terms that are imprecise on their own
once a more specific term is asserted elsewhere.

## Context

Electronic and family-level rows legitimately stop at the level their
signature can justify. Refining such a row to the specific term invents evidence. The
2026-11-14 maintainer ruling in [CLAUDE.md](../../../../CLAUDE.md) settled a split between
reviews that read the action enum two ways: `MODIFY` needs both a deeper replacement
and this row's evidence for it.

## Application

Worked example. An InterPro2GO row maps a generic GPCR signature to `GO:0004930` G
protein-coupled receptor activity on ADRB2. The signature cannot identify the ligand,
so the row stays at `GO:0004930` (`ACCEPT` if core). A separate IDA row from a
ligand-binding and signaling paper supports `GO:0004941` beta2-adrenergic receptor
activity. The IEA row is not `TOO_GENERAL`: a receptor class term is respectably
specific. By contrast, a `GO:0003674` molecular_function-level grouping term or bare
`GO:0005488` binding beside a specific term is imprecise on its own.

When a pleiotropic gene has several supported specific activities, list each one
rather than picking one ([CLAUDE.md](../../../../CLAUDE.md)). Lateral corrections (wrong
substrate, wrong cofactor) are also `MODIFY`, and their replacement need not be a
descendant ([MF-11](MF-11.md)).

<!-- BEGIN GENERATED: edit the frontmatter, then run `just build-guidelines` -->

## Record

| | |
|---|---|
| Status | proposed |
| Provenance | [GOC+] |
| Date | 2026-11-15 |
| Related | [MF-11](MF-11.md) |
| Evidence codes | IDA, IEA |
| GO terms | `GO:0004930` G protein-coupled receptor activity; `GO:0004941` beta2-adrenergic receptor activity; `GO:0003674` molecular_function; `GO:0005488` binding |

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| CLAUDE.md before the 2026-11-14 ruling | `TOO_GENERAL` usable for any general term with a specific term elsewhere, including `GO:0004930` | `TOO_GENERAL` only for terms imprecise on their own; `MODIFY` needs the row's own evidence | Two reviews read the enum in opposite ways; earlier reviews are not retroactively defective |

## Sources

- repo: [CLAUDE.md](../../../../CLAUDE.md)
- repo: [action consistency](../../../../docs/action_consistency.md)
- wiki: [Guidelines for catalytic activity terms](https://wiki.geneontology.org/index.php/Guidelines_for_catalytic_activity_terms)

<!-- END GENERATED -->
