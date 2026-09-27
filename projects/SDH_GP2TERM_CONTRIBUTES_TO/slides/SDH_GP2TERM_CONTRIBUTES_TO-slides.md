---
title: "Complex II: enables vs contributes_to"
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

# Complex II: `enables` → `contributes_to`

A relation fix for succinate dehydrogenase subunits

<span class="small">AI Gene Review · projects/SDH_GP2TERM_CONTRIBUTES_TO · scoping · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- No single subunit of **succinate dehydrogenase** performs GO:0008177; GO agreed (go-annotation#6414) that subunits get **`contributes_to`**, not `enables`.
- **5 repo reviews** carry GO:0008177. All say `contributes_to` in prose; only **SDHC** and **one SDHA row** have the structured qualifier.
- **Scoped, not yet started:** no review edited; SDHB (3 rows) and SDHD (1 row) are the concrete fixes.

---

## The mechanism behind the rule

![h:500](complex-ii-relations.svg)

---

## What the audit found

![h:480](qualifier-audit.svg)

---

## The SDHA nuance

- SDHA's FAD site can oxidise succinate with an **artificial acceptor**: the half-reaction.
- That matches the parent **GO:0000104** succinate dehydrogenase activity, so `enables` there is **defensible** for SDHA alone.
- The quinone-coupled **GO:0008177** still needs the whole complex: `contributes_to` for all four subunits.
- The current SDHA review MODIFYs three GO:0008177 rows to GO:0000104 and keeps one as `contributes_to`: this needs an explicit decision.

---

## Status and next steps

- ⬜ **Tier 1:** SDHB (3 rows) and SDHD (1 row) should end up `contributes_to`. The qualifier mirrors GOA (SDHC's comes from `SDHC-goa.tsv`), so record the intent in `review` now and re-fetch once GOA reflects #6414.
- ⬜ **Tier 2:** decide SDHA GO:0000104 vs GO:0008177; decide 9POAL NCGR_LOCUS67308 (MODIFY → GO:0009055 or keep with qualifier).
- ⬜ PSEPK **sdhA / sdhB** reviews (added later) carry GO:0008177 with `enables`; add to scope.
- Order: note intent in `review` → wait for GOA → `just fetch-gene` → `just validate`.

**Read more:** `projects/SDH_GP2TERM_CONTRIBUTES_TO.md`
