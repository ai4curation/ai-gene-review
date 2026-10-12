---
title: "Cargo receptor ligand activity obsoletion"
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

# Cargo receptor ligand activity is going

GO:0140355 is obsoleted with no replacement term

<span class="small">AI Gene Review · projects/CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Being recognised by a receptor is not an activity. The **receptor** gets `GO:0038024 cargo receptor activity` with the ligand as **has_input**.
- **172** annotations, but **157** are Ensembl projections from **3 seeds**. The real job is **6 experimental rows**.
- Here, **TCN2** and **CBLIF** list the obsolete term in `core_functions`; **TCN1** still carries a non-core row.

---

## The B12 uptake system

![h:480](b12-uptake.svg)

---

## Why GO is dropping the term

- Definition: "interacts with a cargo receptor and **initiates endocytosis**", which describes what happens to the protein.
- It is `is_a protein binding` with **no logical link** to `GO:0038024`.
- The resemblance to "receptor ligand" terms is nominal: those sit in the **signaling** receptor branch, which is disjoint from cargo receptors.
- Minted in 2019 for ApoB as the LDLR ligand; **no apolipoprotein carries it today**.

---

## The footprint

![h:480](footprint.svg)

---

## Impact on this repo

| Review | Row action | core_functions | Tier |
|---|---|---|---|
| human TCN2 | ACCEPT (EXP) | GO:0140355 MF | 1: breaks validation |
| human CBLIF | ACCEPT (EXP) | GO:0140355 MF | 1: breaks validation |
| human TCN1 | KEEP_AS_NON_CORE (EXP) | none | 2: re-term row |
| human HSPA12A | prose only | none | 3: reword |
| CD320, CUBN, AMN | carry GO:0038024 | receptor side | 4: check lossless |

<span class="small">TCN2 also marks its protein-binding row over-annotated because GO:0140355 is "the informative MF"; that reasoning needs rewriting.</span>

---

## Status and next steps

1. **go-ontology#32466 closed**; go-annotation#6533 remains open for Reactome + SGD cleanup.
2. Fix **TCN2** and **CBLIF** together: `REMOVE` the rows, re-point `core_functions` to `GO:0031419` and possibly `GO:0140104`.
3. Decide GO:0140104 once and apply the B12-carrier pattern to **TCN1** too.
4. Flag upstream: yeast **ATG5** IDA and orphaned mouse **Hpse** ISO.

**Read more:** `projects/CARGO_RECEPTOR_LIGAND_ACTIVITY_OBSOLETION.md`
