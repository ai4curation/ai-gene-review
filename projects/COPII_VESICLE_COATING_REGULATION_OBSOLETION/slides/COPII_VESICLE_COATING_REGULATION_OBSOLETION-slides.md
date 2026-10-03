---
title: "Regulation of COPII vesicle coating obsoletion"
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

# Regulation of COPII vesicle coating obsoletion

GO:0003400 → GO:0048208 COPII vesicle coat assembly

<span class="small">AI Gene Review · projects/COPII_VESICLE_COATING_REGULATION_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted** GO:0003400: its proteins are **parts of** COPII coat assembly, not regulators of it. Rows move to **GO:0048208**, renamed *COPII vesicle coat assembly*.
- **11 experimental rows**: 10 move, 1 disputed (human MAPK15) is to be removed; one UniRule needs redirecting.
- **Scoped, not yet started:** no affected gene is reviewed here; **SAR1A** and **SEC23A** are queued.

---

## Why "regulation of" was wrong

- Upstream (go-ontology #31945, closed; PR #32013): SAR1, SEC12, SEC23, SEC16, SED4, PEF1, PREB **act part_of** the coating pathway.
- GO:0048208 and its parent GO:0006901 were relabelled "coat assembly" in the same PR.
- Fix type: terminological. The replacement stays in the same BP branch, so parent classes are preserved.

---

## The proteins build the coat

![h:470](copii-assembly.svg)

---

## Old term → replacement, and the repo today

![h:480](term-map.svg)

---

## Review plan

- **SAR1A** (Q9NR31): anchor. COPII GTPase; the yeast SAR1 rows describe the same biology.
- **SEC23A** (Q15436): inner coat and SAR1 GAP; pairs with SAR1A.
- **SEC16A** (O15027) and **PREB** (Q9HCU5): the human rows actually on the upstream list.
- Defer the yeast-only entries and MAPK15 (upstream removal stands on its own).

---

## Status and next steps

1. `just fetch-gene human SAR1A`, then SEC23A; use the live GO:0048208 id.
2. Keep the TRAPP MODIFY calls (to GO:0006888) consistent with any COPII core reviews.
3. Watch UniRule UR001628761 for the redirect.

**Upstream:** go-annotation#6389 · go-ontology#31945, PR #32013
**Siblings:** `VESICLE_TETHERING_OBSOLETION` (TRAPP rows) · `VESICLE_TARGETING_OBSOLETION` · `ER_EXIT_SITE_LOCALIZATION_OBSOLETION`
**Page:** `projects/COPII_VESICLE_COATING_REGULATION_OBSOLETION.md`
