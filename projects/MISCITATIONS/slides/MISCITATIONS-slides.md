---
title: "Miscitations: citations that pass every check and are still wrong"
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-family: "Source Sans 3", "Helvetica Neue", Arial, sans-serif; font-size: 26px; color: #15201e; background: #f4f7f6; padding: 56px 64px; }
  h1, h2 { font-family: "Literata", Georgia, serif; color: #0e6b66; font-weight: 600; }
  h1 { font-size: 46px; } h2 { font-size: 34px; margin-bottom: 18px; }
  strong { color: #0e6b66; }
  code { font-family: "IBM Plex Mono", Menlo, monospace; font-size: .85em; background: #e3ece9; padding: 0 .25em; border-radius: 3px; }
  table { font-size: 19px; border-collapse: collapse; } th { background: #dcefec; } td, th { padding: 4px 10px; }
  img { border-radius: 4px; }
  section.lead { justify-content: center; }
  section.lead h1 { font-size: 54px; }
  section.bluf { background: #0e6b66; color: #f4f7f6; }
  section.bluf h2, section.bluf strong { color: #ffffff; }
  section.bluf code { background: rgba(255,255,255,.18); color: #ffffff; }
  footer, header { color: #56655f; font-size: 14px; }
  .small { font-size: 18px; color: #56655f; }
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; align-items: start; }
---

<!-- _class: lead -->

# Miscitations

Citations that resolve, match their title, quote verbatim, and are still wrong

<span class="small">AI Gene Review · projects/MISCITATIONS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- We aggregated every `reference_review` in the repo: **33,255** adjudicated references, **1,085 flagged** (3.3% of an enriched sample, not an error rate).
- Six seed cases re-verified live: **all six stand**, and all six errors live in **GOA, IntAct or UniProt**, not in this repo.
- **4 of 6** are defects in how a correct paper was **attached** (WITH/FROM, evidence code, missing `NOT`), and the schema has **no field** for that yet.

---

## Why the validators cannot see this

- **Check 1:** fetched title must match recorded title. A wrong PMID imported with its own title passes.
- **Check 2:** every quote must be verbatim in the cached paper. A verbatim quote can support the **opposite** conclusion.
- **Skipped prefixes:** `file:`, `GO_REF:`, `Reactome:` are not checked by the external snippet validator; **347 of 1,085** flags are on them.

So the flag is a manual judgement, recorded in `references[].reference_review.correctness`.

---

## Where the error lives

![h:470](gaf-row-anatomy.svg)

---

## NLRP3: a dropped digit

- Two IDA rows (`GO:0060090`, `GO:0030674`) cite **PMID:1189953**.
- That PMID is *"[Profanities and the profane person]"*, a 1975 psychiatry abstract.
- Intended: **PMID:31189953**, the 2019 NEK7-NLRP3 structure paper, already cited for five other NLRP3 rows.
- Live QuickGO returns the same two rows: current GOA, not a stale snapshot.

<span class="small">The review records the correct title for 1189953. Internally perfect, externally absurd.</span>

---

## PNPLA3: the paper reports the negative

- GOA: `GO:0003841` LPAAT activity, **EXP** from PMID:21878620, no `NOT`.
- The paper assayed that exact reaction with a positive control:

> "Neither the wild-type nor mutant enzyme catalyzed transfer of oleic acid from oleoyl-CoA to glycerophosphate, lysophosphatidic acid, or diacylglycerol"

- The quote is verbatim, so check 2 passes; the annotation asserts the reverse of what was measured.

---

## What the register holds

![h:470](correctness-counts.svg)

---

## Patterns

- **A wrong identifier is rarely wrong once:** 27 of 56 `WRONG_IDENTIFIER` rows come from twelve PMIDs.
  - paralog spread: ELOVL1/ELOVL3 ← an ELOVL5 paper; NAA10/NAA40 ← a NAA60 paper
  - complex-partner spread: NPLOC4/UFD1, SERP1/SRPRB, UPF1/UPF2, CUL1/RBX1
- **Symbol collision:** ADPRH ← "ARH1" hypercholesterolaemia; BRIP1 ← transcription factor BACH1.
- **Not only PMIDs:** P2RX7 takes a localisation from a Reactome **P2X1** event.

---

## Status and next steps

- ✅ Aggregator, generated register and TSV; six seed cases verified and written up.
- ✅ Two-kind taxonomy: reference-level vs evidence-attachment miscitation.
- ⬜ **Decide where attachment defects go** (per-annotation flag, `FindingReviewStatusEnum`, or an `evidence_review` slot).
- ⬜ Triage 417 `MISCITED` + 56 `WRONG_IDENTIFIER`; neighbour sweep on recurring PMIDs.
- ⬜ Track schema and upstream-reporting follow-ups in ai4curation/ai-gene-review#4225.

**Read more:** `projects/MISCITATIONS.md` · `MISCITATIONS/miscitation-register.md` · sibling `projects/MISCITATION_AUDIT.md`
