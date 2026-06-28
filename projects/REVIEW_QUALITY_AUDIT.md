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
- **Tier 2 (templated reasons):** no placeholder evidence, but one `reason`
  string dominates the file (unique-reason ratio ≤ 0.15 across ≥ 40% of
  annotations). The prose is boilerplate; the `supporting_text` may still be a
  real UniProt/literature quote, so severity is lower — but the per-annotation
  rationale is not trustworthy.

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

### Tier 2 — templated reasons (47 files)

One templated `reason` repeated across most annotations, but evidence is not the
generic placeholder. Largest cases include `mouse/Ctnnb1` (759 annotations, one
reason used 350×), `human/AKT1` (446), `mouse/Mtor` (372), `mouse/Bcl2` (359),
the Argonautes `human/AGO1–4`, the calmodulins `mouse/Calm1–3`, the RAS family
(`Kras`/`Hras`/`human/NRAS`/`KRAS`), `mouse/Pten`, `mouse/Nf1`, and
`mouse/Hsp90aa1`. See the full list in
[the report](REVIEW_QUALITY_AUDIT/reports/REPORT.md).

These are heavily weighted toward large, pleiotropic hub genes — exactly the
genes with the most annotations, where templating saves the most effort and
where over-annotation is most likely.

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
