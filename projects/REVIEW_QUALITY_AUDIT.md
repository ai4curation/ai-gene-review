---
title: "Review Quality Audit"
maturity: IN_PROGRESS
tags: [PIPELINE]
---

# Review Quality Audit

**Some `*-ai-review.yaml` files were produced by a generation pass that filled
every annotation's reasoning from a handful of templated strings and attached
the *same* generic evidence to every annotation. This project detects that
boilerplate so it can be re-reviewed.**

## The defect

A genuine annotation review needs term-specific reasoning and `supporting_text`
that actually supports *that* term. Some reviews instead carry, on every
annotation:

- a `review.reason` drawn from a tiny templated set (e.g. *"Supported secondary
  or context-specific role"*, *"Directly supported core function, process, or
  location"*), and
- a `supported_by` whose `supporting_text` is a generic placeholder — literally
  *"… deep research report reviewed for GO term specificity, core-function
  context, and evidence synthesis."* — that says nothing about the specific
  claim, plus the same UniProt FUNCTION blob repeated verbatim regardless of the
  term.

The *action* labels (ACCEPT / KEEP_AS_NON_CORE / …) may be roughly sensible, but
the reasoning and evidence are not real curation. This was first found and fixed
on **mouse Fyn** (247 annotations, all templated; it also contained
contradictory REMOVE/ACCEPT pairs on the same core terms). This audit asks how
widespread the pattern is.

## Detector

[`REVIEW_QUALITY_AUDIT/scan_boilerplate.py`](REVIEW_QUALITY_AUDIT/scan_boilerplate.py)
scans every `genes/**/*-ai-review.yaml` and flags two severities:

- **Tier 1 (critical):** ≥ 3 annotations carry the generic placeholder
  `supporting_text`. The *evidence is fake/non-specific* — the same defect class
  as Fyn. These should be re-reviewed (or reverted to unreviewed stubs).
- **Tier 2 (genuine rework):** *both* the `summary` and the `reason` are drawn
  from a tiny templated set (unique-summary ratio ≤ 0.15 **and** unique-reason
  ratio ≤ 0.15). The per-annotation rationale carries no real curation signal,
  even though the `supporting_text` may be a real quote. Needs full re-curation.
- **Tier 3 (reason-only, low severity):** only the one-line `reason` is
  templated; the `summary` is term-specific and `supporting_text` is a real
  quote. The substantive review is genuine — only the `reason` field is lazy.
  Low priority; can be tightened in bulk later.

```bash
uv run python projects/REVIEW_QUALITY_AUDIT/scan_boilerplate.py \
    --genes-dir genes --out-dir projects/REVIEW_QUALITY_AUDIT/reports
```

Outputs (regenerated, not hand-edited):
[`REVIEW_QUALITY_AUDIT/reports/REPORT.md`](REVIEW_QUALITY_AUDIT/reports/REPORT.md)
and `boilerplate_flags.csv`.

## Findings

The first run flagged **51 of 2801** review files: **4 Tier 1**, **47 Tier 2**.

### Tier 1 — critical (fake placeholder evidence) — RESOLVED

All four were mouse genes from the same generation pass that produced Fyn, with
the identical templated reason set and placeholder evidence. **All four have now
been fully re-reviewed** (genuine per-term actions, summaries, reasons, and
verified `supporting_text`), so Tier 1 is now empty:

| Gene | reviewed annotations | status |
|---|---|---|
| Egfr (receptor tyrosine kinase) | 304 | re-reviewed |
| Grb2 (adaptor) | 188 | re-reviewed |
| Cbl (E3 ubiquitin ligase) | 140 | re-reviewed |
| Egf (ligand) | 129 | re-reviewed |

(Fyn was re-reviewed first and seeded this audit.) Re-running the scanner now
reports **Tier 1: 0**.

### Tier 2 — genuine rework (13 files)

Both `summary` and `reason` templated — no real per-annotation curation signal.
These are the real worklist after Tier 1: `mouse/Ctnnb1` (759), `mouse/Mtor`
(372), `human/YWHAZ` (220), `mouse/Nf1` (195), `human/SORL1` (168),
`mouse/Brca1` (167), `human/ADAM10` (151), `human/ABCA1` (145), `mouse/Tert`
(143), `human/NCSTN` (99), `human/FERMT2` (85), `mouse/Ccnt1` (50),
`yeast/NTE1` (17).

### Tier 3 — reason-only boilerplate (34 files, low severity)

Only the one-line `reason` is lazy; the `summary` is term-specific and the
`supporting_text` is a real quote, so the substantive review is genuine. This
group includes many large hub genes that *look* templated by reason alone but
are actually fine — e.g. `human/AKT1`, `mouse/Bcl2`, `mouse/Pten`,
`mouse/Hsp90aa1`, the Argonautes `AGO1–4`, the calmodulins `Calm1–3`, and the
RAS family. Low priority. See the full split in
[the report](REVIEW_QUALITY_AUDIT/reports/REPORT.md).

The flagged genes are heavily weighted toward large, pleiotropic hub genes —
exactly the genes with the most annotations, where templating saves the most
effort and where over-annotation is most likely.

## Recommended actions

1. **Tier 1:** re-review (as was done for Fyn) — these carry no usable evidence.
   The action labels can seed the re-review, but every `reason` and
   `supporting_text` must be regenerated against real sources.
2. **Tier 2:** lower priority; spot-check that the dominant `reason` is at least
   defensible and that `supporting_text` is genuine. Prioritise by annotation
   count (the largest files have the most leverage).
3. Treat the placeholder string and a low unique-reason ratio as a **CI smell
   test** for future review submissions.

## Related projects

- [OVER_ANNOTATION_PATTERNS](OVER_ANNOTATION_PATTERNS.md) — the substantive
  over-annotation patterns these hub-gene reviews tend to contain.
- [BEHAVIOR](BEHAVIOR.md) — behaviour over-annotations; several flagged genes
  (Mtor, Hsp90aa1, Pten, Drd1) also carry behaviour terms.
