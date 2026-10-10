---
title: "Miscitation Audit"
maturity: IN_PROGRESS
last_reviewed: "2026-10-04"
tags: [PIPELINE, EVALUATION]
autolink_gene_symbols: false
manifest:
  slides:
    - href: MISCITATION_AUDIT/slides/MISCITATION_AUDIT-slides.html
      description: AI generated
---

# Miscitation Audit

**Bottom line:** a citation whose identifier resolves to a different paper cannot
support the annotation attached to it, and reviewers here had been flagging such
cases one gene at a time without anyone aggregating them. We wrote
`harvest_citations.py`, which collects every `reference_review.correctness` defect
flag across 5,625 review files and keys it on the citation rather than the gene,
and `detect_citation_anomalies.py`, which looks for defects nobody has flagged yet. We
keyed on the citation because one bad PMID can be copied across paralogs or complex
partners, so one correction may clear several genes and one discovery says where else to
look. The current register ([REPORT.md](MISCITATION_AUDIT/reports/REPORT.md)) holds 45
`WRONG_IDENTIFIER` rows on 35 distinct citations, 9 of which carry that flag on more
than one gene, plus 360 `MISCITED` rows and 293 distinct citations whose worst flag is
`MISCITED`. Most of the defects came from GOA (344 of 405 wrong-paper or miscited
rows), so the main deliverable is a bug report to the assigning groups, and those
reports have not been filed yet.

We did this because the existing validators only check internal consistency (the title
matches the PMID, the quote is in the paper), and a wrong PMID imported together with its
own title passes both. The unresolvable-identifier check found two dead PMIDs across
33,167 cited; the paralog-mismatch check is intentionally opt-in because literal symbol
matching has already proven too noisy to use as a finding generator.

The two classes are not interchangeable and this page keeps them apart throughout:
**`WRONG_IDENTIFIER` (45 rows / 35 worst-flag citations)** is mechanically checkable
and is the tier to act on; **`MISCITED` (360 rows / 293 worst-flag citations)** is a
judgement call that has not been sampled for precision.

## Why the citation, not the gene, is the right key

A single bad citation can damage more than one gene when it is copied across paralogs of
a family or partners in a complex, so one upstream correction can clear several genes at
once — and, more usefully, one *discovery* predicts where else to look.

Nine of the 35 distinct `WRONG_IDENTIFIER` citations are flagged on more than one
gene:

| Citation | Genes affected | What the paper is actually about |
|---|---|---|
| `PMID:34388369` | CUL1, RBX1 | the human signal peptidase complex structure |
| `PMID:10970790` | ELOVL1, ELOVL3 | cloning of "HELO1" — i.e. ELOVL5 |
| `PMID:17340523` | ACTB, ARID1A, ARID1B | a Fumaria alkaloid-separation paper |
| `PMID:25732826` | NAA10, NAA40 | the Naa60 acetyltransferase |
| `PMID:39329031` | NPLOC4, UFD1 | a clinical study of intellectual disability in Morocco |
| `PMID:10383829` | APAF1, CYCS | soluble PTP-kappa stimulation of neurite outgrowth |
| `PMID:23264731` | SERP1, SRPRB | MTR120/KIAA1383 |
| `PMID:17469741` | UPF1, UPF2 | a melanoma serum-marker study |
| `PMID:19037698` | TIM9, TIM10 | a colorectal-surgery article |

## Who owns the fix

This is the split that decides what the project is *for*. A citation that appears as
an annotation's `original_reference_id` came from GOA; one that appears only in a
review's `references` list was added here.

- **41 of the 45 `WRONG_IDENTIFIER` rows are GOA-sourced.** Four are review-only
  defects: `ADPRH`, `APOO`, `ECOLI/yrhB` and `PYROR/PoMZ_10221`.
- Across all wrong-paper and miscited rows the ratio is **344 GOA / 61 ours**.

So the primary deliverable is not an internal clean-up — it is a **bug report to the
assigning groups** (MGI, SGD, UniProt, IntAct, Reactome and GOA import owners). The
COX17 case found while reviewing the
[mitochondrial copper delivery pathway](MITO_INTERACTOME.md) is representative: a
`protein farnesylation` IDA on the copper chaperone COX17, citing a paper entirely
about **COX10** (heme A:farnesyltransferase, one digit away), assigned by **MGI**
against a *S. cerevisiae* accession — and with a term that is wrong even for COX10,
since that enzyme farnesylates heme rather than protein.

## Failure modes seen so far

| Mode | Example |
|---|---|
| **Off-by-one gene symbol** | COX17 ← a COX10 paper |
| **Paralog substitution** | ELOVL1/ELOVL3 ← an ELOVL5 paper; NAA10/NAA40 ← a NAA60 paper |
| **Gene-symbol collision** | ADPRH ← a paper whose "ARH1" is the hypercholesterolaemia gene; BRIP1 ← a paper on the bZIP factor BACH1, which shares BRIP1's alias |
| **Wholly unrelated paper** | gbpC ← a *Legionella* SidC effector study; TIM9/TIM10 ← colorectal surgery |
| **Identifier that resolves to nothing** | `PMID:34521819` on STAT2; `PMID:33831160` on CYP71A12/CYP71A13 |
| **Wrong organism or subject** | insc ← a review of zebrafish cardiac development |

## Tooling

### `harvest_citations.py` — the register

Aggregates every `reference_review.correctness` defect flag, keyed on citation.

```bash
uv run python projects/MISCITATION_AUDIT/harvest_citations.py
```

Outputs to [`MISCITATION_AUDIT/reports/`](MISCITATION_AUDIT/reports/REPORT.md):
`citation_flags.tsv` (one row per gene × citation, with the GOA/ours split),
`bad_citations.tsv` (one row per distinct defective citation) and `REPORT.md`.

Its most useful column is **contamination spread**: citations flagged
`WRONG_IDENTIFIER` in one review that are *still cited without a flag* elsewhere.
Ten such citations currently reach 30 unflagged uses.

**Spread is a triage queue, not a verdict.** The clearest illustration is
`PMID:10970790`, flagged wrong on ELOVL1/ELOVL3 and cited unflagged on **ELOVL2** and
**ELOVL5**; ELOVL5 is the *correct* citation, because it is what the paper actually
characterises, while ELOVL2 still needs triage. By contrast the two unflagged uses of
`PMID:34521819` (on JAK1 and STAT1) cannot be correct, because the identifier resolves
to nothing at all. Each row needs a human.

### `detect_citation_anomalies.py` — finding what nobody has flagged

```bash
uv run python projects/MISCITATION_AUDIT/detect_citation_anomalies.py --check-pubmed
```

**Check A — unresolvable identifiers. Works, and is nearly free.** The insight is that
`fetch-gene` already caches every citation it can resolve, so *absence from
`publications/` is itself the signal*; the network call only confirms it. Across the
whole repository **two** cited PMIDs have no cached record — `PMID:33831160` on
`CYP71A12`/`CYP71A13` and `PMID:34521819` on STAT2/JAK1/STAT1 — and NCBI confirms
they return no document summary. This check should run in CI.

**Check B — paralog mismatch. Does not work; recorded so nobody rebuilds it.** The idea
was to flag a citation whose cached text names some members of a numbered family but
not the gene citing it. Measured behaviour:

- **False negatives from alias drift.** It misses the motivating ELOVL case entirely:
  `PMID_10970790.md` contains zero occurrences of "ELOVL" and three of "HELO1", the
  historical name. Symbol matching cannot see through alias history.
- **False positives from complexes.** When tested, its candidates were dominated by
  legitimate complex-wide papers — CHMP/ESCRT, the mitochondrial proteome across COX
  and NDUFA subunits, PEX, EMC, VPS — where broad citation is correct and the cached
  abstract simply does not name every subunit.

Bare co-citation across a family is normal and is not a defect signal. A working
version of this check would need alias-aware matching (UniProt/HGNC synonym lists)
rather than literal symbols. The generated anomaly report does not run the check by
default; it stays opt-in so its low-precision output is not mistaken for a finding list.

## Scope and honest limits

- The **35 `WRONG_IDENTIFIER` citations are the high-confidence tier** and the right
  place to start: "this identifier resolves to a different paper" is checkable.
- The **293 `MISCITED` citations are a second tier**. "Right paper, does not support the
  claim" is a judgement call, some will be defensible on re-reading, and the class has
  not been sampled for precision. Do not report these upstream without re-checking.
- Everything here is **harvested from reviewer judgement**, so it inherits reviewer
  error and covers only genes that have been reviewed. It is a lower bound, and it is
  biased toward genes someone looked at carefully.
- `DISPUTED` (334) and `LOW_QUALITY` (196) are collected for context but are not citation
  defects — they describe the science, not the pointer.

## Next steps

1. Adjudicate the 30 unflagged uses of the 10 spreading citations.
2. Assemble the 41 GOA-sourced `WRONG_IDENTIFIER` rows into per-database reports (MGI,
   SGD, UniProt, IntAct, Reactome) and file them upstream.
3. Fix the four review-only `WRONG_IDENTIFIER` cases (`ADPRH`, `APOO`, `ECOLI/yrhB`,
   `PYROR/PoMZ_10221`).
4. Put Check A in CI — it is cheap, has no false positives by construction, and a
   non-resolving identifier is unambiguous.
5. Decide whether alias-aware matching is worth building for Check B, or whether the
   class is better caught by reviewers reading the cached text.
6. Track the cross-project schema, triage, neighbour-sweep and upstream-reporting work
   in [#4225](https://github.com/ai4curation/ai-gene-review/issues/4225), and the
   IntAct evidence-attachment schema discussion in
   [#1415](https://github.com/ai4curation/ai-gene-review/issues/1415).

## Relationship to other projects

- [REVIEW_QUALITY_AUDIT.md](REVIEW_QUALITY_AUDIT.md) — a different defect: templated
  *reasoning* and placeholder evidence. A review can have real citations and fake
  reasoning, or vice versa.
- [MITO_INTERACTOME.md](MITO_INTERACTOME.md) — where the COX17/COX10 case surfaced.
- [IBA_REVIEW.md](IBA_REVIEW.md) — propagation failure taxonomy; miscitation is one way
  a propagated annotation acquires unsound support.

---

# STATUS

- [x] Citation-keyed harvester and `WRONG_IDENTIFIER`/`MISCITED` reports
- [x] Unresolvable-PMID anomaly detector
- [ ] Triage 30 unflagged uses of the 10 spreading citations
- [ ] Report the 41 GOA-sourced `WRONG_IDENTIFIER` rows upstream in database batches
- [ ] Resolve the four review-only `WRONG_IDENTIFIER` rows
- [ ] Put the unresolvable-PMID check in CI
- [ ] Decide whether to keep or retire the low-precision paralog-mismatch detector
- [ ] Coordinate shared follow-up in [#4225](https://github.com/ai4curation/ai-gene-review/issues/4225)
      and [#1415](https://github.com/ai4curation/ai-gene-review/issues/1415)

Last updated: 2026-10-04

# NOTES

## 2026-10-04

Regenerated `REPORT.md`, `ANOMALIES.md`, `citation_flags.tsv`, `bad_citations.tsv`
and `unresolvable_pmids.tsv` against the current review tree. The citation-keyed
register now covers 5,625 review files and reports 45 `WRONG_IDENTIFIER` rows on
35 distinct citations, 360 `MISCITED` rows on 293 citations, 10 contamination-spread
PMIDs with 30 unflagged uses, and two PMIDs that NCBI cannot resolve.
