---
title: "Geranylgeranyl reductase activity obsoletion"
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

# Geranylgeranyl reductase activity obsoletion

GO:0045550 → GO:0102067 geranylgeranyl diphosphate reductase activity

<span class="small">AI Gene Review · projects/GERANYLGERANYL_REDUCTASE_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted GO:0045550**, which lacked an enzyme cross-reference, and merged it into **GO:0102067** (EC 1.3.1.83).
- Of **4 experimental rows**, the two **plant CHLP** rows fit; the two **human AKR** rows (AKR1C3, AKR1B10) need a substrate check before moving.
- **Scoped, not yet started:** none of the four genes has a review in this repo.

---

## Old term → replacement

![h:480](term-map.svg)

---

## The reaction the new term names

![h:470](ggr-reaction.svg)

---

## Why this is not a pure rename

- The old label said "geranylgeranyl"; the new one says **geranylgeranyl diphosphate**.
- GO:0102067 also covers reduction of **geranylgeranyl-chlorophyll a**, the other in vivo substrate.
- An enzyme shown to reduce a different geranylgeranyl compound does **not** automatically fit.
- The archaeal **IPR023590** family reduces a glycerophospholipid, not free GGPP; its mapping deserves the same question.

---

## Next steps

1. Review **AKR1C3** (human, P42330) first, reading PMID:21187079 for the substrate actually tested.
2. Then **AKR1B10** (same paper).
3. Arabidopsis **CHLP** as the positive control for GO:0102067; treat the tobacco NAS row separately.
4. Raise the IPR023590 fit on go-annotation#6394.

**Upstream:** go-annotation#6394 · go-ontology#31963
**Read more:** `projects/GERANYLGERANYL_REDUCTASE_OBSOLETION.md`
