---
title: "Vesicle docking subtree obsoletion"
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

# Vesicle docking subtree obsoletion

GO:0048278 and 8 related process terms → MFs GO:0160321 docking and GO:7770062 tethering

<span class="small">AI Gene Review · projects/VESICLE_DOCKING_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **retired the vesicle docking process subtree** (9 terms) and minted two MFs: **GO:0160321** docking and **GO:7770062** tethering activity.
- This is the **parent tracker** (#6379): 130 upstream annotations, 96 still pending; siblings cover regulation, tethering and targeting.
- **Refresh fixed in #3237 (merged):** **USO1** → GO:7770062 tethering; **STX12** → GO:0005484 SNAP receptor activity, obsolete BP out of `core_functions`.

---

## Docking is one step of vesicle delivery

![h:480](vesicle-steps.svg)

---

## Why a process became a function

- Upstream: each term **"represents a molecular function"**, the binding of a protein that attaches the vesicle to its target.
- The OLS text says annotations go to **GO:0160321 or GO:7770062**, so each row needs a choice between docking and tethering.
- *Regulation of vesicle docking* terms (GO:0106020-22) are obsolete too, with only a `consider` pointer to GO:0160321, so each regulatory row needs a curator's choice.
- Do not reuse **GO:0099023** vesicle tethering complex: it is a cellular component.

---

## Who holds the rows

![h:470](groups.svg)

---

## State in this repo

| Review | Obsolete term | Row | Action (#3237, merged) | New target |
|---|---|---|---|---|
| `human/USO1` (p115) | GO:0048211 Golgi vesicle docking | IBA | ACCEPT → MODIFY | GO:7770062 vesicle membrane tethering activity |
| `human/STX12` | GO:0048278 vesicle docking (also in `core_functions`) | IBA | ACCEPT → MODIFY | GO:0005484 SNAP receptor activity; core BP dropped |
| `mouse/Camk2a` | GO:0099148 (sibling tracker) | IMP, IDA | ACCEPT → MODIFY | GO:0048172 regulation of short-term neuronal synaptic plasticity |

<span class="small">STX12 was reviewed in June 2026 (#1217), after this page's impact scan. GOA `term.id`s stay as GOA supplies them; only actions and targets change.</span>

---

## Next steps

1. **#3237** merged (USO1, STX12, plus Camk2a and TMF1 for the sibling trackers).
2. Queue new reviews: **STX1A, STXBP1, EXOC4, EXOC6, NSF**; yeast Uso1 and Sec1 later.

**Siblings:** `SYNAPTIC_VESICLE_DOCKING_OBSOLETION` (#6415) · `VESICLE_TETHERING_OBSOLETION` (#6375) · `VESICLE_TARGETING_OBSOLETION` (#6424) · ciliary, ER-PM, mito-ER trackers
**Upstream:** go-annotation#6379 · go-ontology#31880
