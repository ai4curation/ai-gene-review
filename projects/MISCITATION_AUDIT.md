---
title: "Miscitation Audit"
maturity: IN_PROGRESS
tags: [PIPELINE]
autolink_gene_symbols: false
---

# Miscitation Audit

**A cited identifier that resolves to a different paper cannot support the annotation
it is attached to. Reviewers here have flagged 284 such defects one gene at a time
over the life of the repository, and they have never been aggregated. This project
collects them, keys them on the *citation* rather than the gene, and separates the
ones we can fix from the ones only the assigning group can.**

## Why the citation, not the gene, is the right key

A single bad citation rarely damages one gene. It is copied across paralogs of a
family or partners in a complex, so one upstream correction clears several genes at
once — and, more usefully, one *discovery* predicts where else to look.

Seven of the twenty distinct `WRONG_IDENTIFIER` citations already span multiple genes:

| Citation | Genes affected | What the paper is actually about |
|---|---|---|
| `PMID:23209302` | ACOX1, NDUFA8, SLC25A3 | KIF14/Radil/Rap1a signalling in breast cancer |
| `PMID:10970790` | ELOVL1, ELOVL2, ELOVL3 | cloning of "HELO1" — i.e. ELOVL5 |
| `PMID:25732826` | NAA10, NAA40 | the Naa60 acetyltransferase |
| `PMID:39329031` | NPLOC4, UFD1 | a clinical study of intellectual disability in Morocco |
| `PMID:23264731` | SERP1, SRPRB | MTR120/KIAA1383 |
| `PMID:17469741` | UPF1, UPF2 | a melanoma serum-marker study |
| `PMID:19037698` | TIM9, TIM10 | a colorectal-surgery article |

## Who owns the fix

This is the split that decides what the project is *for*. A citation that appears as
an annotation's `original_reference_id` came from GOA; one that appears only in a
review's `references` list was added here.

- **26 of the 27 `WRONG_IDENTIFIER` rows are GOA-sourced.** Only one (`ADPRH`) is ours.
- Across all defect flags the ratio is **232 GOA / 52 ours**.

So the primary deliverable is not an internal clean-up — it is a **bug report to the
assigning groups** (MGI, SGD, UniProt, GOA). The COX17 case found while reviewing the
[mitochondrial copper delivery pathway](MITO_INTERACTOME.md) is representative: a
`protein farnesylation` IDA on the copper chaperone COX17, citing a paper entirely
about **COX10** (heme A:farnesyltransferase, one digit away), assigned by **MGI**
against a *S. cerevisiae* accession — and with a term that is wrong even for COX10,
since that enzyme farnesylates heme rather than protein.

## Failure modes seen so far

| Mode | Example |
|---|---|
| **Off-by-one gene symbol** | COX17 ← a COX10 paper |
| **Paralog substitution** | ELOVL1/2/3 ← an ELOVL5 paper; NAA10/NAA40 ← a NAA60 paper |
| **Gene-symbol collision** | ADPRH ← a paper whose "ARH1" is the hypercholesterolaemia gene; BRIP1 ← a paper on the bZIP factor BACH1, which shares BRIP1's alias |
| **Wholly unrelated paper** | gbpC ← a *Legionella* SidC effector study; TIM9/TIM10 ← colorectal surgery |
| **Identifier that resolves to nothing** | `PMID:34521819` on STAT2 |
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
Six such citations currently reach thirteen unflagged genes.

**Spread is a triage queue, not a verdict.** The clearest illustration is
`PMID:10970790`, flagged wrong on ELOVL1/2/3 and cited unflagged on **ELOVL5** — where
it is the *correct* citation, because ELOVL5 is what the paper actually characterises.
By contrast the two unflagged uses of `PMID:34521819` (on JAK1 and STAT1) cannot be
correct, because the identifier resolves to nothing at all. Each row needs a human.

### `detect_citation_anomalies.py` — finding what nobody has flagged

```bash
uv run python projects/MISCITATION_AUDIT/detect_citation_anomalies.py --check-pubmed
```

**Check A — unresolvable identifiers. Works, and is nearly free.** The insight is that
`fetch-gene` already caches every citation it can resolve, so *absence from
`publications/` is itself the signal*; the network call only confirms it. Across the
whole repository exactly **one** cited PMID has no cached record — `PMID:34521819` —
and NCBI confirms it returns no document summary. It is cited by three genes and was
flagged on only one. This check should run in CI.

**Check B — paralog mismatch. Does not work; recorded so nobody rebuilds it.** The idea
was to flag a citation whose cached text names some members of a numbered family but
not the gene citing it. Measured behaviour:

- **False negatives from alias drift.** It misses the motivating ELOVL case entirely:
  `PMID_10970790.md` contains zero occurrences of "ELOVL" and three of "HELO1", the
  historical name. Symbol matching cannot see through alias history.
- **False positives from complexes.** Its 356 candidates are dominated by legitimate
  complex-wide papers — CHMP/ESCRT, the mitochondrial proteome across COX and NDUFA
  subunits, PEX, EMC, VPS — where broad citation is correct and the cached abstract
  simply does not name every subunit.

Bare co-citation across a family is normal and is not a defect signal. A working
version of this check would need alias-aware matching (UniProt/HGNC synonym lists)
rather than literal symbols. Output is retained in `paralog_mismatches.tsv` and
`family_clusters.tsv` but should not be treated as findings.

## Scope and honest limits

- The **20 `WRONG_IDENTIFIER` citations are the high-confidence tier** and the right
  place to start: "this identifier resolves to a different paper" is checkable.
- The **215 `MISCITED` citations are a second tier**. "Right paper, does not support the
  claim" is a judgement call, some will be defensible on re-reading, and the class has
  not been sampled for precision. Do not report these upstream without re-checking.
- Everything here is **harvested from reviewer judgement**, so it inherits reviewer
  error and covers only genes that have been reviewed. It is a lower bound, and it is
  biased toward genes someone looked at carefully.
- `DISPUTED` (75) and `LOW_QUALITY` (99) are collected for context but are not citation
  defects — they describe the science, not the pointer.

## Next steps

1. Adjudicate the 13 unflagged uses of the 6 spreading citations.
2. Assemble the GOA-sourced `WRONG_IDENTIFIER` set into per-database reports (MGI, SGD,
   UniProt) and file them upstream.
3. Fix the one review-only case (`ADPRH`).
4. Put Check A in CI — it is cheap, has no false positives by construction, and a
   non-resolving identifier is unambiguous.
5. Decide whether alias-aware matching is worth building for Check B, or whether the
   class is better caught by reviewers reading the cached text.

## Relationship to other projects

- [REVIEW_QUALITY_AUDIT.md](REVIEW_QUALITY_AUDIT.md) — a different defect: templated
  *reasoning* and placeholder evidence. A review can have real citations and fake
  reasoning, or vice versa.
- [MITO_INTERACTOME.md](MITO_INTERACTOME.md) — where the COX17/COX10 case surfaced.
- [IBA_REVIEW.md](IBA_REVIEW.md) — propagation failure taxonomy; miscitation is one way
  a propagated annotation acquires unsound support.
