---
title: "Metabolic models as a check on GO function annotations"
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

# Metabolic model analysis

Using genome-scale metabolic models to catch GO molecular-function errors

<span class="small">AI Gene Review · projects/METABOLIC_MODEL_ANALYSIS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Compared EC numbers in **3 GEMs** (M. extorquens iRP911, E. coli iML1515, human Recon3D) with UniProt: **42 / 51 / 61%** of aligned genes disagree.
- Much is expected (EC class 7, complex-subunit EC propagation), but **8 gene reviews** found real errors on both sides.
- GO wrong: **mdcD** (7 rows removed), **ecm**, **HADHB**. Model wrong: **rbsD**, **glgX**, **HADHB**, **CPT1C**. FBA shows the errors matter.

---

## How often models and UniProt disagree

![h:470](gem-discrepancy-rates.svg)

---

## Not every disagreement is an error

- **EC class 7** (translocases) was created in 2018; iRP911 is from 2011. Cytochrome c oxidase 1.9.3.1 → 7.1.1.9 is a reclassification.
- **Complex convention:** a GPR lists every subunit, so every EC of the complex lands on each gene. E. coli *lpd* picks up 10 ECs.
- So GEM gene→EC pairs must be **filtered** before they can validate GO MF terms.

---

## When UniProt and GO were wrong

| Gene (organism) | Model says | GO/UniProt said | Review |
|---|---|---|---|
| mdcD (*M. extorquens*) | 4.1.1.89 decarboxylase | 6.4.1.3 carboxylase (ligase) | 7 REMOVE; carboxy-lyase ACCEPT; malonate catabolism NEW |
| ecm (*M. extorquens*) | noEC (2011) | methylmalonyl-CoA mutase | MODIFY to GO:0016866 intramolecular transferase; no GO term for EC 5.4.99.63 yet |
| HADHB (human) | — | hydratase, dehydrogenase (TAS) | REMOVE: those are HADHA's |

<span class="small">mdcD shares 35% identity with an acetyl-CoA carboxylase subunit; one wrong EC cascaded into GO, keywords and family assignments.</span>

---

## When the model was wrong

![h:470](recon3d-mtp-cpt1.svg)

---

## FBA: do the errors matter?

| Test | Original model | Corrected / reality |
|---|---|---|
| E. coli *rbsD* KO on ribose | 100% growth (rbsD in transporter GPR) | 0% after adding the pyranase step |
| Recon3D HADHA KO, FAOXC5C3x | flux 1000 → 0 | essential, as expected |
| Recon3D HADHB KO | blocks only HISDr (histidase) | should block thiolase steps |

<span class="small">E. coli glgX was also wrong in iML1515: a debranching enzyme modelled as branching enzyme (2.4.1.18 vs 3.2.1.196).</span>

---

## Status and next steps

- Reviews: `genes/METEA/{ecm,sucB,mdcD,gcvP}`, `genes/ECOLI/{rbsD,glgX}`, `genes/human/{HADHB,CPT1C}`.
- Open: *M. extorquens* mdcB, ilvC, purK; remaining Recon3D CLASS_CHANGE genes.
- Caveat: the `models/metabolic/` files and FBA scripts cited on the page are **not in this repository**.

**Read more:** `projects/METABOLIC_MODEL_ANALYSIS.md`
