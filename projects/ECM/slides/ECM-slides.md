---
title: "Extracellular matrix: reviewing ten ECM genes"
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

# The extracellular matrix

GO annotation review of ten human basement-membrane and interstitial matrix genes

<span class="small">AI Gene Review · projects/ECM · IN_PROGRESS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **All 10 planned genes have actioned rows**; 8 are `COMPLETE`, with AGRN/NID1 still needing metadata closure.
- **635 review rows**: 284 ACCEPT, 193 non-core, 70 REMOVE, 63 MODIFY, 13 NEW, 5 over-annotated, 7 undecided.
- **FN1 carries most corrections**: 52 `protein binding` rows removed, 38 `extracellular region` rows sharpened to `extracellular matrix`.

---

## Where the genes sit

![h:470](ecm-architecture.svg)

---

## Why the ECM

- ECM proteins are large, multi-domain and **heavily annotated from interaction screens**, so generic rows pile up.
- Their core role is **structural and extracellular**, while many rows describe downstream developmental outcomes.
- The testicans (SPOCK1-3) test whether a review can capture a **paralog with the opposite effect**.

---

## Results by gene

![h:470](ecm-actions.svg)

---

## What a review looks like

![h:440](fn1-review-table.jpg)

<span class="small">FN1 review page: nervous system development is kept as non-core; cell-substrate junction assembly is accepted as core.</span>

---

## Key findings

1. **FN1**: 52 IPI `protein binding` rows REMOVE; 38 `extracellular region` rows MODIFY → `extracellular matrix`.
2. **SPOCK2**: metalloendopeptidase inhibitor rows MODIFY (→ endopeptidase regulator / negative regulation of endopeptidase activity), because SPOCK2 counter-inhibits SPOCK1/3.
3. **EPYC**: NEW `collagen binding`, `collagen fibril organization`, `extracellular matrix structural constituent`; TAS glycosaminoglycan binding REMOVE.
4. **SPOCK3**: NEW `collagen binding`, `extracellular matrix binding`, negative regulation of endopeptidase activity.

---

## Status and next steps

- ✅ 10/10 planned genes have every row actioned; 8/10 are `COMPLETE`.
- ⬜ Finalize `AGRN` and `NID1` review status.
- ⬜ Add **DCN** `core_functions`.
- ⬜ Draft the first ECM module: NID1/HSPG2/AGRN with laminin and collagen IV.
- ⬜ Issue #4070 tracks the remaining ECM closure work.

**Read more:** `projects/ECM.md` · `genes/human/FN1/` · `genes/human/SPOCK2/`
