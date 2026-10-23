---
title: "Enzyme specificity: right class, wrong substrate, cofactor or reaction"
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

# Enzyme specificity

Right enzyme class, wrong substrate, cofactor, donor or reaction

<span class="small">AI Gene Review · projects/ENZYME_SPECIFICITY · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- A GO MF term can name the right kind of enzyme and still get the **substrate, cofactor or reaction** wrong.
- We reviewed **14 genes**: four exemplars (LPL1, GND1, PHYKPL, EryCIII) and all **ten human β-oxidation enzymes**, where chain length decides the term.
- Errors caught: too-narrow substrate, wrong reaction, wrong donor, wrong chain length, wrong subunit, a nickname collision. GND1 was a **negative control**. Complete.

---

## Why specificity

- Specificity errors survive because the **fold and enzyme class are right**; nothing looks wrong until someone checks the substrate.
- They mislead **pathway reconstruction** and propagate by **IBA**.
- Four categories: substrate, reaction mechanism, cofactor, non-enzymatic homolog (e.g. Epe1).
- Principle: **use the specific term where one exists**, fall back to the general term where GO has none.

---

## Four exemplars

![h:470](error-types.svg)

---

## β-oxidation: specificity inside a paralog set

![h:470](beta-oxidation-specificity.svg)

---

## Proposing the missing terms

![h:430](phykpl-review-table.jpg)

<span class="small">PHYKPL review: GO has no term for its reaction, so the review proposes <em>5-phosphooxy-L-lysine phospho-lyase activity</em> and a matching catabolic process, and adds the general GO:0016838 carbon-oxygen lyase activity, acting on phosphates, as NEW.</span>

---

## Findings

1. **Family membership is the usual culprit**: PHYKPL (aminotransferase III), EryCIII (IEA UDP-GT), GND1 D-gluconate (UniProt keyword via ARBA rule).
2. **Wrong subunit or evidence-scope** errors cluster in complexes and families: HADHA thiolase, HADH long-chain, ACAD9 C16 assays.
3. **Name collisions** create errors no sequence check finds: "ACAT1" = SOAT1 vs mitochondrial T2.
4. A **GO → RHEA** gap: hydratase GO:0004300 maps to RHEA:20724 (3E), not the canonical (2E) RHEA:16105.

---

## Status and next steps

- ✅ 14/14 reviews complete; `MODULE:fatty_acid_beta_oxidation` built.
- ⬜ If extended: keyword-derived substrate terms on other PPP enzymes (ZWF1); NAD vs NADP dehydrogenase pairs.

**Read more:** `projects/ENZYME_SPECIFICITY.md` · `modules/fatty_acid_beta_oxidation.yaml` · `projects/RHEA/RHEA-EC-SPECIFICITY.md`
