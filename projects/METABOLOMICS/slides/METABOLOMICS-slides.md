---
title: "Interpreting metabolomics with GO"
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

# Metabolomics with GO and GO-CAM

Bridging metabolite lists to GO functions and processes through ChEBI and Rhea

<span class="small">AI Gene Review · projects/METABOLOMICS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- A working bridge: **metabolite → Rhea → GO MF → human enzymes → GO BP**, with closure-aware enrichment.
- The obstacle is **identifiers**: exact ChEBI matching connects **8/64** MTBLS1 metabolites; protonation + structure normalization reaches **58/64**.
- Four MetaboLights studies: **53–91%** coverage, study-specific GO processes. Remaining lipid, Reactome, GO-CAM and demo work is tracked in #4125.

---

## Why GO is absent from metabolomics

- Standard interpretation: **KEGG / SMPDB** pathway ORA, MSEA, **mummichog** for untargeted MS (packaged in MetaboAnalyst).
- GO annotates **gene products**, so it says nothing about a list of ChEBI ids out of the box.
- But GO MF terms *are* enzyme activities, and Rhea reactions are written in ChEBI. ChEBI is the bridge.

---

## The bridge and where it breaks

![h:470](chebi-bridge.svg)

---

## Normalization is decisive in every study

![h:470](coverage-tiers.svg)

---

## What GO adds over KEGG (MTBLS1, same test)

| KEGG pathway | GO molecular function | GO biological process |
|---|---|---|
| Ala, Asp & Glu metabolism | amino-acid transaminase | amino acid metabolic process (4.3×, FDR 9e-44) |
| Citrate cycle (TCA) | L-/D-amino-acid oxidase | dicarboxylic acid metabolic process (6.0×) |
| Pyruvate metabolism | amino-acid racemase | amino acid transport (5–7×) |
| Nicotinate & nicotinamide | primary methylamine oxidase | proteinogenic amino acid metabolism (4.2×) |

<span class="small">Serum LC-MS study MTBLS90 instead returns lipid metabolic process (2.9×, FDR 3e-89). GO resolves specific activities and processes, not only pathway buckets.</span>

---

## Status and next steps

- Done: probe pipeline (`projects/METABOLOMICS/probe/`), two-tier normalization, KEGG / GO-MF / GO-BP enrichment, 4 studies.
- Next: complex lipids (LIPID MAPS / SwissLipids); Reactome as a curated BP cross-check; GO-CAM causal trace (Approach B); feed implicated reactions to Reactome black-box gap filling.
- Planned: interactive demo (static showcase + Streamlit app), see `DEMO-PLAN.md`.

**Read more:** `projects/METABOLOMICS.md` · `projects/METABOLOMICS/CROSS-STUDY.md`
