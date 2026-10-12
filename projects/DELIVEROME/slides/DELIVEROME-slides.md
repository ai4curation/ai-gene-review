---
title: "Deliverome and GO: delivery addresses and routes"
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

# Deliverome and GO

How GO can describe, and learn from, an atlas of therapeutic delivery addresses

<span class="small">AI Gene Review · projects/DELIVEROME · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- The **Deliverome** atlas wants surface proteins that cargo can use as a **delivery address**: present, internalized, and routed somewhere useful.
- The first phase defined the term, mapped it to **17 GO anchor terms**, and compared **human RAB7A** with **mouse Rab7** as a worked post-uptake routing example.
- The two reviews **agree** on core Rab7 biology; mouse adds in vivo evidence that **Rab7 loss increases LNP escape**.

---

## A delivery route in GO terms

![h:520](delivery-route.svg)

---

## Where GO annotation stops

| Deliverome evidence | Possible GO use | Caution |
|---|---|---|
| Surface proteomics, endogenous protein | cell surface / plasma membrane | needs cell-type context |
| Endogenous receptor uptake | receptor internalization | cargo uptake alone is a delivery phenotype |
| Receptor tracked to lysosome | routing annotations | not if only the payload was tracked |
| Perturbation screen hits | trafficking machinery review | separate direct from viability effects |
| Expected receptor fails to internalize | NOT, rarely | failed delivery is not enough |

<span class="small">Engineered-cargo outcomes (for example cytosolic escape) belong in GO-CAM-like Deliverome models, not canonical GO.</span>

---

## Worked example: mouse Rab7

![h:470](rab7-review-table.jpg)

<span class="small">Mouse Rab7 review: 119 rows, 80 accepted. Endosome-to-lysosome transport is core, supported by the liver LNP study (PMID:41814093).</span>

---

## Human RAB7A vs mouse Rab7

| | Human RAB7A | Mouse Rab7 |
|---|---|---|
| Annotations reviewed | 124 | 119 |
| ACCEPT / non-core / REMOVE | 70 / 24 / 26 | 80 / 29 / 8 |
| Best use | disease genetics (CMT2B) | in vivo delivery routing |

- Shared core: Rab GTPase activity, early-to-late endosome maturation, endosome-to-lysosome transport, retromer binding.
- Mouse SynGO rows (AMPA-receptor traffic, PMID:24217640) kept **non-core**: the paper centres on stargazin and AP-2/AP-3A.

---

## Status and next steps

- ✅ Delivery address defined; GO anchors; model-system stance (human primary, pombe for machinery, mouse for in vivo routing).
- ✅ RAB7A and Rab7 harmonized; SynGO rows revisited.
- ⬜ Build a GO-derived human surfaceome prior.
- ⬜ Pick a small address pilot set.
- ⬜ Draft a GO-CAM-like delivery-route template.

Issue #4062 tracks the remaining three tasks.

**Read more:** `projects/DELIVEROME.md` · `genes/human/RAB7A/` · `genes/mouse/Rab7/`
