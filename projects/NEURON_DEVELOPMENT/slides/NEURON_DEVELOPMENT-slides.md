---
title: "Neural and glial cell fate: reviewing GO fate-stage annotations"
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

# Neuron or glia?

Reviewing GO annotations for the genes that decide neural cell fate

<span class="small">AI Gene Review · projects/NEURON_DEVELOPMENT · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO describes fate choice with **specification → determination → commitment** terms from classical embryology; we asked whether the evidence behind each annotation supports the rung it claims.
- **13 of 38** planned human genes reviewed (all 12 master regulators + DLX1): **1,652 annotations**, 960 accepted, 138 removed.
- Fate-stage terms mostly **held up**; the removals were almost all generic `protein binding` (129 of 138). Priorities 2–4 (25 genes) are **not started**.

---

## The decision being annotated

![h:520](fate-decision.svg)

---

## Why these terms are a curation risk

- Telling **specification** from **commitment** needs transplant or neutral-environment assays, which most papers lack.
- Single-cell studies (Velten 2017, Weinreb 2020) show **continuous trajectories**, not discrete stages.
- Some cell-type commitment terms were added on request for one gene, e.g. GO:0072154 *proximal convoluted tubule segment 1 cell fate commitment*.
- Neuron vs glia is the **clearest binary choice** (Notch lateral inhibition), so it is the right test case.

---

## What the reviews decided on the fate ladder

![h:520](term-ladder.svg)

---

## Review actions

![h:520](actions.svg)

---

## What a review looks like

![h:480](ascl1-review-table.jpg)

<span class="small">ASCL1 review page: each GOA row gets an action and a written reason with quoted evidence.</span>

---

## Gene-level findings

- **HES1** is a repressor: projected *positive regulation of transcription* rows marked **over-annotated**.
- **ASCL1**: *negative regulation of glial cell differentiation* (GO:0045686) proposed as **NEW**.
- **OLIG2**: specification accepted; *oligodendrocyte cell fate commitment* (GO:0021779) added as **NEW**.
- **NEUROD1**: *endocrine pancreas development* accepted alongside neuronal roles; insulin-secretion and glucose rows kept as non-core.
- **STAT3** (456 rows) and **NOTCH1** (378 rows): 66 and 33 removals, all generic `protein binding`.

---

## Status and next steps

- ✅ Priority 1 (12 master regulators) and DLX1 reviewed; all validate.
- ⬜ Priority 2 subtype genes: DLX2, LHX6, TBR1, NR4A2, PITX3, ISL1, MNX1, OLIG1, SOX10.
- ⬜ Priority 3–4 signalling and oligodendrocyte genes (SHH already reviewed under the cerebellum work).
- ⬜ Decide whether granular commitment terms should give way to general terms plus Cell Ontology extensions.

**Read more:** `projects/NEURON_DEVELOPMENT.md` · `genes/human/<GENE>/`
