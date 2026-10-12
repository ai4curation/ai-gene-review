---
title: "ClinGen Mendelian disease genes: a review campaign"
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

# ClinGen Mendelian disease genes

A one-gene-per-PR review campaign over 2,876 ClinGen-associated genes

<span class="small">AI Gene Review · projects/CLINGEN_MENDELIAN · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Seeded from the **2026-09-25 ClinGen Gene–Disease Validity** export: every gene with a Definitive, Strong, Moderate or Limited association, **2,876 genes**.
- Each gene gets its own PR reviewing its **molecular function and GO annotations**; a disease link alone does not establish a function.
- **201 genes are complete** at the 2026-10-03 16:43:30 UTC checkpoint; 2,675 remain and AKR1D1 is still excluded pending a source follow-up.

---

## The campaign at a glance

![h:500](clingen-campaign.svg)

---

## Why ClinGen

- ClinGen **grades the evidence** for each gene–disease link, so the seed set is explicit and reproducible (archived CSV, SHA-256, seed script).
- Limited associations are kept as candidates, not established causation; RNA genes and other loci get separate workflows.
- 747 of the 2,876 genes had a human review on 2026-09-27; the campaign **re-audits** them against current rules rather than assuming they are done.

---

## Initial cohort: actions, 2026-09-26

![h:470](clingen-actions-chart.svg)

<span class="small">The first 14 merged PRs reviewed 607 source annotations. All 26 REMOVEs were generic <code>protein binding</code> (17 on ABCC6), and justified UNDECIDED calls stayed explicit where evidence was inaccessible.</span>

---

## What a review looks like

![h:430](abcc6-review-table.jpg)

<span class="small">ABCC6: each generic <code>protein binding</code> row from a fragmentomics screen is removed with a partner-specific reason, after inspecting the full text and supplementary data.</span>

---

## Status and next steps

- ✅ Source archived and 2,876-gene inventory seeded (PR #3126).
- ✅ 201 of 2,876 genes complete; 202 original gene PRs merged; AKR1D1 still awaits a required source follow-up.
- ✅ Latest completion set: C1QA #3909, C1QB #3916, C1QTNF5 #3911, C2CD3 #3917, C1QBP #3914.
- ⬜ Continue recording independently verified merges; RNA genes and other HGNC locus types remain separate workflows.

**Read more:** `projects/CLINGEN_MENDELIAN.md` · `projects/CLINGEN_MENDELIAN/review-progress.md`
