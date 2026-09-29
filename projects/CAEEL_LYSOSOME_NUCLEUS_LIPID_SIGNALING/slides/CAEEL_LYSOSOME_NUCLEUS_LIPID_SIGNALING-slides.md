---
title: "C. elegans lysosome-to-nucleus OEA signalling"
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

# Lysosome-to-nucleus lipid signalling in *C. elegans*

Reviewing GO annotations for the four genes of the OEA longevity pathway

<span class="small">AI Gene Review · projects/CAEEL_LYSOSOME_NUCLEUS_LIPID_SIGNALING · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **LIPL-4** releases OEA in the lysosome, **LBP-8** carries it to the nucleus, and **NHR-80** with **NHR-49** turns on lipid genes that extend lifespan (PMID:25554789).
- All four genes reviewed: **74 rows**, 60 ACCEPT, 6 MODIFY, 4 NEW.
- Corrections make the signal explicit: LBP-8 gets **lipid transfer activity** in place of a transmembrane transporter term, **ligand-modulated** TF activity for NHR-80. Downstream targets are not yet reviewed.

---

## The pathway

![h:500](oea-pathway.svg)

---

## Why this pathway

- Short and well characterised: one enzyme, one chaperone, one receptor pair.
- A direct binding measurement: NHR-80 binds OEA with Kd about 7.8 µM.
- Needed for germline-loss (glp-1) longevity, separable from insulin/IGF and dietary restriction.
- Test: can GO terms express a **lipid messenger** moving from lysosome to nucleus?

---

## A MODIFY in practice

![h:440](nhr-80-review-table.jpg)

<span class="small">nhr-80: the IEA DNA-binding transcription factor row is modified to ligand-modulated transcription factor activity or nuclear receptor activity.</span>

---

## Results per gene

| Gene | Role | Rows | ACCEPT | Non-core | Over-ann. | MODIFY | NEW |
|---|---|---|---|---|---|---|---|
| lipl-4 | lysosomal acid lipase | 14 | 13 | 1 | 0 | 0 | 0 |
| lbp-8 | FABP lipid chaperone | 17 | 15 | 0 | 0 | 1 | 1 |
| nhr-80 | OEA receptor | 15 | 10 | 2 | 0 | 1 | 2 |
| nhr-49 | NHR-80 partner | 28 | 22 | 0 | 1 | 4 | 1 |

<span class="small">No REMOVE actions. NEW: intracellular lipid transport (lbp-8), ligand-modulated TF activity and nuclear receptor binding (nhr-80), cellular response to hypoxia (nhr-49).</span>

---

## Status and next steps

- ✅ lipl-4, lbp-8, nhr-80, nhr-49 reviewed.
- ⬜ Review downstream targets fat-5, fat-6, fat-7, acs-2 and the glp-1 longevity context.
- Related reviews already in the repo: hlh-30 (TFEB, regulates lipl-4) and daf-16.

**Read more:** `projects/CAEEL_LYSOSOME_NUCLEUS_LIPID_SIGNALING.md` · `genes/worm/<gene>/`
