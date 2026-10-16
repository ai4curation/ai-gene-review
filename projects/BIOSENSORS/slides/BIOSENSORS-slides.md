---
title: "Plant-encoded biosensors"
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

# Plant-encoded biosensors

Borrowing plant immune receptors to sense microbes (scoping notes)

<span class="small">AI Gene Review · projects/BIOSENSORS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- ORNL's **SEED SFA** builds plant biosensors that sense microbes through **immune receptors** and report or respond.
- Flagship: a **chitin sensor** that splits GFP across **LYK5** and kinase-dead **CERK1**; chitin pairing rebuilds fluorescence.
- **Scoped, not started** as curation: 12 of the 20 listed Arabidopsis genes already have reviews from other work; none of the TODOs is done.

---

## The engineered chitin sensor

![h:490](chitin-split-gfp.svg)

---

## Why curate the parts

- A sensor inherits the **specificity of its receptors** and the **wiring of the pathway** it taps.
- Receptor classes of interest: LRR-RLKs (FLS2, EFR, BAK1), LysM-RLKs (CERK1, LYK5, LYK4), lectin RLKs (Populus PtLecRLK1).
- Downstream responses the page tracks: ROS burst (RBOHD), MAPK activation, SA/SAR genes (NPR1, PR genes); defense promoters can drive reporters.
- Other SEED designs noted: split-intein dimerization sensor, Plant RNA Vision RNA biosensor.

---

## Which parts have reviews

![h:490](sense-response-coverage.svg)

---

## Status and next steps

- ⬜ Map genes to UniProt/TAIR IDs.
- ⬜ Review the missing receptors first: **LYK5, LYK4** (the chitin sensor's own parts), PEPR1/2.
- ⬜ Cross-reference Arabidopsis defense pathway annotations; move EFR and BIK1 off `INITIALIZED`.
- ⬜ Identify orthologs in *Populus trichocarpa*.

**Read more:** `projects/BIOSENSORS.md` · `genes/ARATH/CERK1/`
