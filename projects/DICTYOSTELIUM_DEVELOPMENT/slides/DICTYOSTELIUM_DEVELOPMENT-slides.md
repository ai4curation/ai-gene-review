---
title: "Dictyostelium development: 14 modules, 54 reviews"
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

# Dictyostelium development

From single amoebae to a fruiting body: 14 modules and 54 development reviews

<span class="small">AI Gene Review · projects/DICTYOSTELIUM_DEVELOPMENT · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Starving *Dictyostelium* amoebae **aggregate by cAMP relay** and build a **stalk and spore** fruiting body in about a day.
- We split development into **14 modules**, completed a **52-gene review batch**, and folded in **mlcD + rdeA** to ground **8 DRAFT ModuleReviews**.
- **1,478 annotations:** 797 accepted, 546 non-core, 42 modified, 37 over-annotated, **19 removed**, 37 undecided.

---

## The program and its modules

![h:480](dicty-lifecycle.svg)

---

## Why Dictyostelium

- The standard model for the step from **unicellular to multicellular** life.
- Development is driven by **cell–cell signalling** (cAMP, DIF-1, SDF-2), chemotaxis and a binary **prestalk / prespore** fate choice.
- Large **paralog families** (cAR1–4, three adenylyl cyclases, ~15 histidine kinases) test how IBA/IEA propagation behaves within a genome.

---

## Actions by review batch

![h:470](dicty-actions.svg)

---

## What the reviews found

- **Paralog propagation**: *adenylate cyclase activator activity* over-annotated on **cAR3**; purinergic-receptor IEA **removed** from cAR1–3; phosphorelay IEAs **removed** from ACR.
- **statC**: metazoan *JAK-STAT* signalling → *receptor signalling via STAT* (GO:0097696).
- Other removals include *mitotic cytokinesis* (IBA) on RasC, *fatty acid* and *flavonoid biosynthesis* on the DIF-1 polyketide synthase StlB, and *DNA binding* on spore-coat CotB.
- High non-core share (546) reflects many pleiotropic developmental and motility rows kept but not core.

---

## A Dictyostelium module

![h:440](dicty-sdf2-module-page.jpg)

<span class="small">dicty_sdf2_encapsulation_relay: AcbA → TagC → SDF-2 ⊣ DhkA → RdeA → RegA ⊣ PKA; one of 8 DRAFT modules grounded in the gene reviews.</span>

---

## Status and next steps

- ✅ 52-gene batch reviewed; mlcD + rdeA integrated; all 14 modules represented; 8 ModuleReviews.
- ⬜ Per-gene notes journals; expert second-pass QA.
- ⬜ Deeper paralogs: *tgr* locus, Ras/Rap, dhk/grl, ecm/cot, statB/statD.

**Read more:** `projects/DICTYOSTELIUM_DEVELOPMENT.md` · `modules/dicty_*.yaml` · `genes/DICDI/`
