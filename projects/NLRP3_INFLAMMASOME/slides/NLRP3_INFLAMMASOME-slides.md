---
title: "NLRP3 inflammasome: a scoped pathway project"
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

# NLRP3 inflammasome assembly

A scoped project: ten candidate genes, three already reviewed

<span class="small">AI Gene Review · projects/NLRP3_INFLAMMASOME · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **NLRP3** recruits **PYCARD (ASC)** to activate **caspase-1**, which matures IL-1β and IL-18 and cleaves **gasdermin D** to open pyroptotic pores.
- **Scoped, not yet started**: no project-specific review work has been done.
- **3 of 10** candidates already reviewed (NLRP3, CASP4, GSDMD; 364 annotations). PYCARD, CASP1 and five others have no gene folder; a draft **NLR signaling module** already includes NLRP3, PYCARD and CASP1.

---

## The mechanism and what is covered

![h:500](nlrp3-inflammasome.svg)

---

## Why this complex

- A **major therapeutic target**; gain-of-function NLRP3 causes **CAPS**, and inflammasome activity contributes to gout, atherosclerosis and Alzheimer disease.
- Post-2020 work on the **trans-Golgi activation site**, post-translational control, assembly structures and the **GSDMD pore** is likely under-represented in GO.
- A bounded complex with a clear order: sensor → adaptor → caspase → substrates.

---

## A gap in GO the NLRP3 review found

![h:420](nlrp3-proposed-term.jpg)

<span class="small">NLRP3 is activated by unrelated stimuli it does not bind, so GO:0140299 <em>molecular sensor activity</em> does not fit. The review proposes <em>inflammasome sensor activity</em>.</span>

---

## Status and next steps

| Gene | State |
|---|---|
| NLRP3 (188 ann.), CASP4 (99), GSDMD (77) | Reviewed (COMPLETE) |
| PYCARD, CASP1, CASP5, IL1B, IL18, NEK7, BRCC3 | No gene folder |

- ⬜ `just fetch-gene human <GENE>` for the seven missing genes, starting with **PYCARD** and **CASP1**.
- ⬜ Extend `modules/nlr_signaling.yaml` (DRAFT) with the reviewed inflammasome genes.

**Read more:** `projects/NLRP3_INFLAMMASOME.md` · `modules/nlr_signaling.yaml`
