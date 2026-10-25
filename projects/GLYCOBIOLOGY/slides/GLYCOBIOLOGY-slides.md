---
title: "Glycobiology: auditing GO annotation of glycogenes"
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

# Glycobiology

Auditing how GO annotates the enzymes and lectins of glycosylation, and mapping CAZy families to GO

<span class="small">AI Gene Review · projects/GLYCOBIOLOGY · reviewed 2026-10-04</span>

---

<!-- _class: bluf -->

## Bottom line

- We reviewed **376 annotations on 11 human glycogenes** and indexed **17 pathway modules** (100 more genes, 2,748 annotations).
- Only **4 removals**: the problem is **altitude and pleiotropy** (generic parent terms, downstream physiology), not wrong functions.
- A **CAZy→GO mapping** (`cazy2go`) yields a **60-row safe propagation set** and **34 hand-endorsed** `interpro2go` gaps.

---

## Why glycogenes

- Glycosylation decorates most secreted and cell-surface proteins; defects cause **>130 congenital disorders of glycosylation**.
- Glycosyltransferase families are **large and sequence-similar**, so propagated annotations can land on the wrong paralog or at the wrong level.
- Specialist resources (**CAZy, GlyGen, GlyConnect, GlyTouCan, GlycoCoO**) hold knowledge GO may lack.
- Question: where does GO **over-annotate** glycogenes, and where does it **under-represent** glycan biology?

---

## Actions per gene

![h:520](glyco-actions.svg)

---

## What the reviews found

1. **Generic MF → specific activity** is the dominant fix: MGAT1 → `GO:0003827`, ST6GAL1 → `GO:0003835`, B4GALT1 → `GO:0003831`.
2. The **cellular-component** version: bare `membrane` on Golgi transferases → `GO:0000139` Golgi membrane.
3. **Guilt by substrate**: PMM2 only supplies GDP-mannose, so N-linked glycosylation is non-core.
4. **Pleiotropy is not core**: 62 of LGALS3's 106 rows kept non-core; `lysophagy` added as NEW.
5. **8 new GO terms proposed** across the seven exemplars.

---

## Phase 3: mucin-type O-glycans

![h:520](mucin-o-glycan.svg)

---

## The module cohort

![h:430](n-glycan-module-page.jpg)

<span class="small">One of the 17 indexed glycobiology modules (N-glycan LLO lumenal assembly). The 100-gene module cohort shows the same skew: 0.8% REMOVE, 63.3% ACCEPT, 17.6% non-core, 14.0% over-annotated.</span>

---

## cazy2go: CAZy families → GO MF

| Step | Result (2026-06 snapshot) |
|---|---|
| Families with a GO MF via member ECs | 283 |
| Fully masked by `interpro2go` | 56 (20%) |
| Safe propagation set after filters and hand review | **60 rows** |
| Hand-reviewed true gaps | 34 ENDORSE · 13 CAUTION · 6 REJECT |
| Poly-specific families resolved to subfamily signatures | 66 of 90 |

<span class="small">Rejects were CBM (non-catalytic) families and one GT family carrying a protease EC from another domain; both are now filtered automatically.</span>

---

## Status and next steps

- Done: 11 exemplar reviews; 17 modules indexed; `cazy2go` safe set built.
- Next: run the **GOA closure query** to size the animal glycogene set and its baseline.
- Next: submit the **8 proposed terms** and the **34 endorsed** `interpro2go` gaps after curator sign-off.
- Next: remaining GALNT paralogues, core 3/4 and capping steps; re-review modules for new terms.

**Read more:** `projects/GLYCOBIOLOGY.md` · `projects/GLYCOBIOLOGY/`
