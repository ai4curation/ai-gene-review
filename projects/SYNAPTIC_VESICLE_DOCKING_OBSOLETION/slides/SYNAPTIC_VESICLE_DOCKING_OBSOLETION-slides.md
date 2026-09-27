---
title: "Regulation of synaptic vesicle docking obsoletion"
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

# Regulation of synaptic vesicle docking obsoletion

GO:0099148 retired as docking becomes a molecular function, GO:0160321

<span class="small">AI Gene Review · projects/SYNAPTIC_VESICLE_DOCKING_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO now treats vesicle docking as a **molecular function** (GO:0160321); **GO:0099148** regulation of synaptic vesicle docking is **obsolete**.
- Its SynGO rows sit on **Camk2a, Septin5 and tom-1**; a regulator should **not** inherit the docking MF.
- **Camk2a fixed in #3237 (open):** both GO:0099148 rows → MODIFY to **GO:0048172** regulation of short-term neuronal synaptic plasticity, not the docking MF.

---

## Where this term sits in the vesicle refactor

![h:480](vesicle-steps.svg)

---

## Why docking became a function

- Upstream reason: the term **"represents a molecular function"**, the binding activity of a docking protein.
- GO:0160321 is defined as binding that **stably attaches a vesicle** to its target membrane; it sits after tethering (**GO:7770062**) and before fusion.
- A *regulation of* process has **no 1:1 MF counterpart**, so each gene needs its own decision.
- Upstream spreadsheet: SynGO's 8 rows on GO:0099148, plus about 60 IEA ortholog rows that follow automatically.

---

## Regulator or docker?

![h:480](decision.svg)

---

## State in this repo

| Gene | Rows on GO:0099148 | Review here |
|---|---|---|
| Camk2a (mouse P11798) | IMP + IDA, PMID:17660813 | ACCEPT → **MODIFY** GO:0048172 (#3237, open) |
| Septin5 (mouse Q9Z2Q6) | IMP + IDA, PMID:20624595 | none |
| tom-1 (worm A0A0K3ATN9) | IMP ×2 + IDA ×2, PMID:16895441 | none |

<span class="small">Rat Camk2a and Septin5 carry ISO copies (RGD). #3237 also replaced the tangential Camk2a supporting text with the abstract's sentences on docked-vesicle number and short-term presynaptic plasticity.</span>

---

## Next steps

1. Merge **#3237** (Camk2a → GO:0048172).
2. Review **Septin5** (then human SEPTIN5, Q99719): the one candidate for GO:0160321.
3. Review **tom-1** as the negative-regulator case.

**Siblings:** `VESICLE_DOCKING_OBSOLETION` (parent, #6379) · `VESICLE_TETHERING_OBSOLETION` (#6375) · `VESICLE_TARGETING_OBSOLETION` (#6424)
**Upstream:** go-annotation#6415 · go-ontology#31880
