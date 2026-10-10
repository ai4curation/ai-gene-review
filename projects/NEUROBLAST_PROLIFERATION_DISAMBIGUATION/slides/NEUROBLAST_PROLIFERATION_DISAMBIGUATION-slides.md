---
title: "Neuroblast proliferation: two cells behind one word"
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

# Neuroblast proliferation

A fly stem-cell term applied to vertebrate genes

<span class="small">AI Gene Review · projects/NEUROBLAST_PROLIFERATION_DISAMBIGUATION · scoping · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO's neuroblast proliferation and division terms describe the **fly** neuroblast, a dividing stem cell; the **vertebrate** neuroblast does not divide.
- All **42** annotations to the six terms are on **vertebrate** genes (35 mouse, 4 human, 3 rat). The planned fix is per-gene **MODIFY** to GO:0061351 *neural precursor cell proliferation*.
- **Scoped, not started.** Five existing vertebrate reviews touching these rows kept them as non-core instead.

---

## One word, two cells

![h:520](two-neuroblasts.svg)

---

## Where the 42 rows sit

![h:520](rows-by-term.svg)

---

## What existing reviews already say

| Gene | Term | Evidence | Action in repo |
|---|---|---|---|
| DROME/N | GO:0007405 neuroblast proliferation | IMP | KEEP_AS_NON_CORE |
| DROME/Lis-1 | GO:0007405 neuroblast proliferation | IMP | KEEP_AS_NON_CORE |
| DROME/insc | GO:0055059 asymmetric neuroblast division | IGI | ACCEPT |
| DROME/Lkb1 | GO:0055059 asymmetric neuroblast division | IMP | KEEP_AS_NON_CORE |
| human/FGFR2 | GO:0021847 VZ neuroblast division | ISS | KEEP_AS_NON_CORE |
| human/PAFAH1B1 | GO:0007405 neuroblast proliferation | ISS | KEEP_AS_NON_CORE |
| human/SHH | GO:0007405 neuroblast proliferation | ISS | KEEP_AS_NON_CORE |
| human/TP53 | GO:0007405 neuroblast proliferation | IEA | KEEP_AS_NON_CORE |
| mouse/Ctnnb1 | GO:0007405 neuroblast proliferation | IGI | KEEP_AS_NON_CORE |

<span class="small">These reviews were made for other projects. The fly rows fit the term; the five vertebrate rows are the ones this project would revisit.</span>

---

## Status and next steps

- Upstream: [geneontology/go-annotation#6393](https://github.com/geneontology/go-annotation/issues/6393), still in discussion; no ontology ticket yet.
- ⬜ Revisit FGFR2 (GO:0021847) under the MODIFY rule.
- ⬜ Review the human set: SOX5, ARHGEF2, DOCK7, TEAD3.
- ⬜ Review mouse progenitor genes: Pafah1b1 (LIS1), Aspm, Nde1, Shh, Ascl1.
- ⬜ Add the pattern to `projects/OVER_ANNOTATION_PATTERNS.md` after 3–4 reviews.

**Read more:** `projects/NEUROBLAST_PROLIFERATION_DISAMBIGUATION.md`
