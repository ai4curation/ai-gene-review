---
title: "AlphaFold Database for annotation review"
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

# AlphaFold Database for annotation review

Using predicted monomers and complexes to test GO claims. Scoped, not yet built.

<span class="small">AI Gene Review · projects/ALPHAFOLD · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **Scoped, not started as a pipeline**: 0 of 6 action items done; no AFDB fetch step, no schema field.
- Idea: check each GO or ARBA claim against the predicted model (pocket, active site, TM helices, disorder, complex interface).
- One worked use so far: in the **BGC project**, AF3-predicted complexes corroborated three known enzyme complexes.

---

## Why predicted structures

- AFDB now includes **proteome-scale quaternary predictions**, not only monomers.
- 1,580 of the 2,529 pipeline genes have **no deposited PDB structure** (PDB project inventory).
- Five use cases: binding-site checks, transfer confidence for ARBA rules, interface evidence instead of `protein binding`, pLDDT disorder context, flagging implausible rules.

---

## Proposed workflow

![h:500](afdb-workflow.svg)

---

## The one worked example: BGC complexes

![h:420](bgc-iptm.svg)

<span class="small">Used as corroboration, not to drive the call. The screen's own validation set shows real complexes can score low, so a missing prediction is not evidence against a complex.</span>

---

## Next steps

- ⬜ Add an AFDB lookup to the bioinformatics pipeline (fetch by UniProt ID)
- ⬜ Script to extract features relevant to GO validation
- ⬜ Pilot on 5–10 ARBA rule reviews: does structure change the outcome?
- ⬜ Test quaternary predictions for complex membership; test pLDDT for domain claims
- ⬜ Consider a structural-evidence field in the review schema

<span class="small">Open tracker: ai4curation/ai-gene-review#3959</span>

**Read more:** `projects/ALPHAFOLD.md` · `projects/BGC.md` · `projects/PDB.md`
