---
title: "Yeast metabolic engineering: scoped GO review"
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

# Yeast metabolic engineering

A scoped plan to review GO annotations for 10 central-carbon genes that strain engineers target

<span class="small">AI Gene Review · projects/YEAST_METABOLIC_ENGINEERING · scoping</span>

---

<!-- _class: bluf -->

## Bottom line

- **Scoped, not yet started:** 10 *S. cerevisiae* genes chosen, **0 reviewed**.
- The set covers ethanol production (PDC1, ADH1, ADH2), the glycerol byproduct (GPD1, GPD2), glycolysis (HXK1, PFK1, TDH1), anaplerosis (PYC1) and NADPH supply (ZWF1).
- Goal: check the annotations are accurate enough to support pathway design.

---

## Where the genes sit

![h:500](fermentation-map.svg)

---

## Why these genes

- Engineers raise ethanol or chemical yield by pushing flux to pyruvate and beyond, and by **cutting glycerol**, which yeast makes to reoxidise surplus NADH.
- Each step has **paralogs** (ADH1/ADH2, GPD1/GPD2, HXK1/HXK2, TDH1–3), so GO has to say which isoform does what.
- Well-characterised enzymes make a good test of whether annotations reach the right specific reaction terms.

---

## Status

![h:420](gene-status.svg)

---

## Next steps

- `just fetch-gene yeast <GENE>` for each of the 10, then deep research and annotation review.
- Check the list: on glucose, **HXK2** is the main hexokinase and **TDH3** the main GAPDH; consider reviewing paralog pairs together.
- Consider a yeast fermentation module (glucose to ethanol plus the glycerol branch) once the reviews exist.

**Read more:** `projects/YEAST_METABOLIC_ENGINEERING.md`
