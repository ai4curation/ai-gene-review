---
title: "Parasite immune modulators: scoping from vampire bat saliva"
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

# Parasite immune modulators

Scoping GO curation of secreted host-modulating proteins, starting with vampire bat saliva

<span class="small">AI Gene Review · projects/PARASITE_IMMUNE_MODULATORS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Blood-feeders and parasites secrete proteins that **blunt host clotting, inflammation and immunity**.
- We scoped the **vampire bat (DESRO) Vampirome**: 45 salivary transcripts → **35 UniProt accessions, all unreviewed TrEMBL**.
- The reviews moved to **VAMPIROME**: **14 DESRO reviews**, 136 reviewed rows, and 12 core-function summaries. Non-bat parasites now route through **PARASITES**.

---

## From transcripts to reviews

![h:480](candidate-funnel.svg)

---

## What the reviewed saliva proteins are thought to do

![h:480](host-targets.svg)

---

## Where the review work stands (VAMPIROME)

| Action | Rows |
|---|---|
| ACCEPT | 66 |
| MODIFY | 27 |
| MARK_AS_OVER_ANNOTATED | 21 |
| KEEP_AS_NON_CORE | 8 |
| UNDECIDED | 7 |
| REMOVE | 3 |
| NEW (proposed) | 4 |

<span class="small">136 reviewed rows across 14 reviews in <code>genes/DESRO/</code>: 132 imported GOA rows plus 4 NEW proposals. UNDECIDED rows are mainly the K9IUF6 ADAMTS1 fragment; K9IUF6 and K9J2R0 still need core_functions.</span>

---

## Status and next steps

- ✅ Background, Table 4 extract and UniProt mapping (`projects/VAMPIROME/`).
- ✅ 14 DESRO reviews under `VAMPIROME`; ⬜ synthesize K9IUF6 and K9J2R0; ⬜ resolve `CALCA/vCGRP`.
- ⬜ Remaining ~20 mapped candidates (lipocalins, serpins, cystatin, TIMPs).
- ⬜ [#3994](https://github.com/ai4curation/ai-gene-review/issues/3994): finish the DESRO backlog.
- ⬜ Non-bat parasites: fold into the `PARASITES` umbrella as its host-modulation sub-topic ([#3992](https://github.com/ai4curation/ai-gene-review/issues/3992)).

**Read more:** `projects/PARASITE_IMMUNE_MODULATORS.md` · `projects/VAMPIROME.md` · `genes/DESRO/`
