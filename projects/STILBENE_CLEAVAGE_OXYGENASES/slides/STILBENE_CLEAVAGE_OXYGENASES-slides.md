---
title: "Stilbene cleavage oxygenases: a family-level over-annotation"
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

# Stilbene cleavage oxygenases

How a carotenoid term spread to every stilbene cleaver in the family

<span class="small">AI Gene Review · projects/STILBENE_CLEAVAGE_OXYGENASES · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- SCOs split **resveratrol-type stilbenes** into two aldehydes, but share a fold and PANTHER family (PTHR10543) with **carotenoid** cleavers.
- We reviewed **7 members** (6 stilbene cleavers from fungi and bacteria, plus the carotenoid cleaver **cao-2** as control).
- `GO:0010436` *carotenoid dioxygenase activity* was **REMOVED on all six** stilbene cleavers, whether it came by IBA or TreeGrafter IEA; it was **accepted on cao-2**.

---

## The propagation error

![h:480](sco-propagation.svg)

---

## Why this family

- **Paralog positive controls** in two fungi: *Neurospora* cao-2 (carotenoid) vs cao-1 (stilbene); *Ustilago* Cco1 vs Rco1.
- The same family term is right for one paralog and wrong for the other; only **target-specific experiments** separate them.
- GO was revising this area in **July 2026**: `GO:1905594` *resveratrol binding* being obsoleted, `GO:7770086` *resveratrol dioxygenase activity* added.

---

## Actions per gene

![h:470](sco-actions.svg)

---

## Carotene catabolism rows

| Gene | Organism | Propagation | `GO:0016121` carotene catabolic |
|---|---|---|---|
| cao-1 | *N. crassa* | IBA | MODIFY → `GO:0046272` stilbene catabolic |
| Rco1 | *U. maydis* | IBA | MODIFY → `GO:0046272` |
| NOV1 (Saro_0802) | *N. aromaticivorans* | TreeGrafter IEA | MODIFY → `GO:0046272` |
| NOV2 (Saro_2809) | *N. aromaticivorans* | TreeGrafter IEA | MODIFY → `GO:0046272` |
| LSD-III (lsdB) | *S. paucimobilis* | TreeGrafter IEA | REMOVE |
| LSD-I (Q53353) | *S. paucimobilis* | TreeGrafter IEA | REMOVE |

<span class="small">On LSD-I and LSD-III the carotenoid IEA rows sit beside the genes' own IDA lignostilbene-dioxygenase annotations.</span>

---

## A proposed grouping term

![h:440](cao1-review-table.jpg)

<span class="small">From the cao-1 review: a *hydroxystilbene α,β-dioxygenase activity* grouping term as parent of GO:7770086 and GO:0050054, to carry the family-level annotation.</span>

---

## Status and next steps

- ✅ 7 reviews written (all still status IN_PROGRESS); cao-1 structure analysis explains its substrate panel (two-ring anchor).
- ⬜ Propose the grouping term to GO; switch structured slots to `GO:7770086` once the validation snapshot has it.
- ⬜ Compare bacterial (NOV1/NOV2/LsdA) and fungal (CAO-1/Rco1) anchor residues.
- ⬜ Fix at the family node: a stilbene-cleavage subfamily in PTHR10543.

**Read more:** `projects/STILBENE_CLEAVAGE_OXYGENASES.md` · `genes/NEUCR/cao-1/` · `projects/IBA_REVIEW.md`
