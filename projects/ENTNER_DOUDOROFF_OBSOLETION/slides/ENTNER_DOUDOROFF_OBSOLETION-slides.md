---
title: "Entner-Doudoroff sub-pathway obsoletion"
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

# Entner-Doudoroff sub-pathway obsoletion

Four variant terms → GO:0061678 Entner-Doudoroff pathway

<span class="small">AI Gene Review · projects/ENTNER_DOUDOROFF_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted four ED sub-pathway terms** (GO:0009255, GO:0061679, GO:0061680, GO:0061681) and folded them into **GO:0061678**.
- Only **two repo reviews** needed direct fixes: *P. putida* **edd** and **eda**.
- PR **#3232** is merged: edd ACCEPT → MODIFY → GO:0061678, eda NEW → GO:0061678, and both `core_functions` now point to GO:0061678.

---

## Old terms → replacement

![h:480](term-map.svg)

---

## Why the variants went

- The four terms mirrored **MetaCyc variant pathways**: via 6-phosphogluconate, via gluconate, and two gluconate endpoints.
- GO's obsoletion comment: variants are **better captured as GO-CAMs** than as nested ontology terms.
- The parent GO:0061678 already covers **both intermediates** (gluconate or 6-phosphogluconate) and **both endpoints**.
- No molecular function terms change.

---

## What the variants described

![h:470](ed-variants.svg)

---

## The edd row before #3232

![h:400](edd-review.jpg)

<span class="small">genes/PSEPK/edd/edd-ai-review.html: the ACCEPT on GO:0009255 (main, before #3232). GOA ids are not rewritten, so #3232 makes it MODIFY → GO:0061678 rather than keeping ACCEPT.</span>

---

## Repo impact

| Gene | Row on GO:0009255 | Action | Also in |
|---|---|---|---|
| PSEPK **edd** | IEA, GO_REF:0000120 | ACCEPT → **MODIFY → GO:0061678** (#3232) | `core_functions.directly_involved_in` |
| PSEPK **eda** | proposed, from UniProt pathway line | NEW, now **GO:0061678** (#3232) | `core_functions.directly_involved_in` |

- No review uses GO:0061679, GO:0061680 or GO:0061681.
- The ED **module** and both PSEPK ED-enzyme reviews now use GO:0061678.
- Sibling term GO:0061688 (obsoleted in the same GO release) was proposed by PSEPK **glk**; #3232 drops it and ACCEPTs glk's GOA **GO:0006096** row, since Glk does no ED step.
- Upstream issue snapshot: EcoCyc 1 and UniProt 3 annotations, plus 7 external mappings.

---

## Next steps

1. Done in #3232: edd, eda → **GO:0061678** (rows and `core_functions`); glk → **GO:0006096**.
2. Later, as one batch tracked in #460: E. coli `edd`, E. coli `eda`, and a pass over `gnd`.

**Upstream:** go-annotation#6390 · go-ontology#31916
**Read more:** `projects/ENTNER_DOUDOROFF_OBSOLETION.md`
