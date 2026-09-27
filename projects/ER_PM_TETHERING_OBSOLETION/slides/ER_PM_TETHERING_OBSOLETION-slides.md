---
title: "ER-plasma membrane tethering obsoletion"
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

# ER-plasma membrane tethering obsoletion

GO:0061817 (process) → GO:0160214 adaptor activity (function)

<span class="small">AI Gene Review · projects/ER_PM_TETHERING_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted GO:0061817** because tethering the ER to the plasma membrane is a **molecular function**, now **GO:0160214**.
- **21 upstream annotations** (PomBase 13 done, CGD 4, TAIR 2, UniProt 2) move; InterPro already dropped **8 mappings**.
- **Scoped, not yet started:** no review YAML uses either term and no dedicated ER-PM tether is reviewed. **VAPA** was assessed for GO:0160214 and **not annotated** (PR #3220): the partner's PH domain, not VAPA, binds the PM lipids. VAPA never had GO:0061817 in GOA; only its cached UniProt DR line lists it.

---

## Old term → replacements

![h:480](term-map.svg)

---

## What the new function term describes

![h:470](esyt-tether.svg)

---

## Why the change is right

- The old term was a **process** whose definition was the **attachment** itself: a single-step activity.
- GO:0160214 is defined as the **binding activity** that brings the two membranes together via lipid binding.
- A true process consequence, where one exists, goes to **GO:0051643** ER localization.
- The same pattern applies across the three families: E-Syts, tricalbins and plant SYTs.

---

## Next steps

1. ✅ **VAPA**: GO:0160214 not added (PR #3220); the scs2/scs22 and VAPB precedent is a suggested question.
2. Anchor reviews: **ESYT2** (human) and **TCB3** (yeast) via `just fetch-gene`; check the new MF term against the literature.
3. Then the rest as one batch: ESYT1, ESYT3, TCB1, TCB2.
4. Plant SYT1/SYT5 (ARATH) last; separate stress phenotypes from the core contact-site function.

**Upstream:** go-annotation#6383 · go-ontology#31873
**Read more:** `projects/ER_PM_TETHERING_OBSOLETION.md`
