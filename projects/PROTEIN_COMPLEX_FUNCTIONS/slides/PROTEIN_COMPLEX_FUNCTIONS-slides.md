---
title: "Protein complex functions: who does the work in a complex?"
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

# Protein complex functions

Which subunits should carry a complex's molecular function?

<span class="small">AI Gene Review · projects/PROTEIN_COMPLEX_FUNCTIONS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Complex activities get assigned to **every subunit**, turning membership into a false catalytic function.
- We wrote a **decision framework** and backed a GO-CAM split into **active** vs **accessory/structural** members, so only active members export MF.
- Tested on the proteasome (**PSMB5 vs PSMA1**) and BGC heterodimers; structure prediction gave **no curation-grade interface**.

---

## Same complex, different roles

![h:470](attribution-roles.svg)

---

## Working principles

1. Complex membership alone is **not evidence** for a molecular function.
2. Essential for an activity ≠ the **executor** of it.
3. `contributes_to` only for direct participants: catalytic core, electron relay, substrate binding, mechanical coupling.
4. Assembly factors get **assembly** terms unless they stay in the active complex.
5. Multi-activity complexes (ribosome, proteasome): assign roles **per activity**.

---

## A catalytic subunit, reviewed

![h:440](psmb5-review.jpg)

<span class="small">PSMB5 (β5): threonine-type endopeptidase activity ACCEPTed; generic endopeptidase MODIFY to the specific term. Its alpha-ring partner PSMA1 carries no peptidase rows.</span>

---

## Worked examples from BGC heterodimers

| Complex | Catalytic member (`enables`) | Partner's role |
|---|---|---|
| PqsBC | PqsC, acyltransferase | PqsB: `contributes_to` |
| Act KS-CLF | ActI-ORF1, polyketide synthase | CLF: chain-length factor |
| EryCII-EryCIII | EryCIII, glycosyltransferase | EryCII: `enzyme activator activity` |

<span class="small">All three had the catalytic MF on the non-catalytic partner in GOA via domain-signature propagation.</span>

---

## Can structure prediction assign roles?

![h:470](pilot-iptm.svg)

---

## Status and next steps

- Done: framework, rubric, GO-CAM export position, PSMA1/PSMB5 reviews, Boltz2 and ESMFold2 pilots.
- Open: **OXPHOS attribution matrix**; audit OXPHOS reviews for `contributes_to` and assembly-factor consistency; guidance for enrichment and ML-label users.

**Read more:** `projects/PROTEIN_COMPLEX_FUNCTIONS.md` · `projects/OXPHOS.md` · `projects/PROTEIN_COMPLEX_FUNCTIONS/esmfold2/`
