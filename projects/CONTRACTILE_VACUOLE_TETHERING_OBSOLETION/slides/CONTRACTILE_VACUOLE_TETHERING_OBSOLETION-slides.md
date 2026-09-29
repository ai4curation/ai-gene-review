---
title: "Contractile vacuole tethering obsoletion"
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

# Contractile vacuole tethering obsoletion

BP GO:0140025 → MF GO:7770067 contractile vacuole-plasma membrane tether activity

<span class="small">AI Gene Review · projects/CONTRACTILE_VACUOLE_TETHERING_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted** the process GO:0140025 and replaced it with a **new molecular function**, GO:7770067 (is_a GO:0140177 membrane-membrane adaptor activity).
- Only **2 annotations** move, both *Dictyostelium* IMP: **rab8A** and **p2xA**.
- **Scoped, not yet started:** neither gene is reviewed here; p2xA needs a careful look.

---

## Why a process became a function

- Tethering is a **binding activity** that bridges two membranes, so GO models it as an MF.
- Same pattern as the sibling tether obsoletions: **ER-PM**, **mito-ER**, **vesicle tethering** (GO:7770062).
- Upstream: go-ontology #31870; new term PR #31942; obsoletion PR #31950.
- No InterPro2GO, UniProt keyword or UniRule mappings to redirect.

---

## What the tether does

![h:470](cv-discharge.svg)

---

## Old term → new term, and the two rows

![h:480](term-map.svg)

---

## Review plan

- **rab8A** (P20790): anchor review. PMID:22323285 is the paper cited in the **new term's definition**; the new MF is the likely core function, with the exocyst link and contractile vacuole discharge (GO:0070177) as context.
- **p2xA** (Q86JM7): P2X receptors are **cation channels**. Check that PMID:24335649 shows tethering and not a channel-dependent regulatory role before accepting the MF.
- `genes/DICDI/` has 56 reviews; neither gene is among them.

---

## Status and next steps

1. Confirm dictyBase has migrated the two IMP rows to GO:7770067 (upstream said they "may be automatically transferred").
2. `just fetch-gene DICDI rab8A`, then `p2xA`.
3. These two reviews close the whole GO:0140025 migration.

**Upstream:** go-annotation#6387 · go-ontology#31870, #31942, #31950
**Siblings:** `ER_PM_TETHERING_OBSOLETION` · `MITO_ER_TETHERING_OBSOLETION` · `VESICLE_TETHERING_OBSOLETION`
**Page:** `projects/CONTRACTILE_VACUOLE_TETHERING_OBSOLETION.md`
