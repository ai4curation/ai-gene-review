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
- The reviews moved to the sibling **VAMPIROME** project: **14 DESRO reviews**, 11 complete. Non-bat parasites are **not started**.

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
| ACCEPT | 64 |
| MODIFY | 29 |
| UNDECIDED | 21 |
| MARK_AS_OVER_ANNOTATED | 15 |
| REMOVE | 3 |
| NEW (proposed) | 4 |

<span class="small">132 GOA rows across 14 reviews in <code>genes/DESRO/</code>. UNDECIDED rows are propagated terms with no bat evidence either way: 10 on K9IMD0 (e.g. protease rows transferred from human LTF), 6 on the K9IUF6 ADAMTS1 fragment whose catalytic residues UniProt flags.</span>

---

## Status and next steps

- ✅ Background, Table 4 extract and UniProt mapping (`projects/VAMPIROME/`).
- ✅ 14 DESRO reviews under [VAMPIROME](../../VAMPIROME.md); ⬜ finish K9IUF6, K9IWR0, K9J2R0; ⬜ CALCA.
- ⬜ Remaining ~20 mapped candidates (lipocalins, serpins, cystatin, TIMPs).
- ⬜ Non-bat parasites: fold into the [PARASITES](../../PARASITES.md) umbrella as its host-modulation sub-topic.

**Read more:** `projects/PARASITE_IMMUNE_MODULATORS.md` · `projects/VAMPIROME.md` · `genes/DESRO/`
