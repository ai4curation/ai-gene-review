---
title: "Pathway satisfiability: is the pathway wired up here?"
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

# Pathway satisfiability

Reading a curation module as a boolean formula, evaluated in a context

<span class="small">AI Gene Review · projects/PATHWAY_SATISFIABILITY · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Across **54 GTEx tissues**, the human gluconeogenesis module is satisfiable in exactly **liver, kidney cortex, small intestine**; every other tissue fails at **G6PC1**.
- The same engine resolves **within the liver** (periportal yes, pericentral no) and reproduces **GapMind-style** methionine reconstruction across genomes.
- Gaps crossed with independent activity data become **gene-localised leads**: intestinal gluconeogenesis → G6PC1; liver ketolysis → OXCT1.

---

## Why ask it this way

- Pathway tools (KEGG/Reactome coverage, GapMind, Pathway Tools hole filler) ask a **genome-level** question: does this organism encode the pathway?
- Right for a microbe. Wrong for a metazoan: **every cell has the whole genome**.
- The discriminating variable is **which isozyme is expressed in which context**.
- So keep GapMind's logic and swap the oracle: **genome content → context expression**.

---

## The module as a circuit

![h:500](module-circuit.svg)

---

## Between organs: 54 GTEx tissues

<div class="cols">

![h:540](fig-tissues.svg)

<div>

- Green: the whole module is satisfiable. **Liver, kidney cortex, small intestine** only.
- Every grey tissue fails at the **same gate atom**, G6PC1.
- The ubiquitous paralog **G6PC3** is not accepted for the step.
- Raising the threshold drops tissues in the order **liver → kidney → intestine**.

</div>
</div>

---

## Within an organ: liver zonation

![h:300](fig-lobule.svg)

- Halpern 2017 nine-layer porto-central axis (mouse). The route is **blocked at the pericentral pole** at the same G6PC1 gate.
- Orientation is inferred from **landmark genes**, not assumed.

---

## Across genomes: methionine

![h:330](fig-genomes.svg)

<span class="small">Only the oracle changed (KEGG ortholog presence). The engine picks the encoded route per organism: succinyl vs acetyl acylation, trans-sulfuration vs direct sulfhydrylation.</span>

---

## A gap is a hypothesis

<div class="cols">

![h:400](fig-abduction.svg)

<div>

- **Abduction targets**: *Synechocystis*, *M. jannaschii* make methionine with **no candidate** for a step.
- *Rickettsia* gap correctly read as **auxotrophy**.
- Eukaryotic side: **liver ketolysis** gap at OXCT1 (GTEx liver 0 TPM); **intestinal gluconeogenesis** flagged at G6PC1.

</div>
</div>

---

## Status and next steps

- ✅ Engine: `src/ai_gene_review/module_logic.py` (doctested) + `tests/test_module_logic.py`.
- ✅ Resolvers and figures: `modules/experimental/gluconeogenesis-context/`; demo `projects/PATHWAY_SATISFIABILITY/demo.html`.
- ✅ Spin-off: `taxon_absent_component/` flags JAK-STAT IBA rows in *Dictyostelium* (no JAK encoded).
- ⬜ Human liver zonation oracle (remove the mouse-ortholog step).
- ⬜ Run on more curated modules; promote resolvers into a CLI.

**Read more:** `projects/PATHWAY_SATISFIABILITY.md` · `methods.md` · `background.md`
