---
title: "ER-phagy: a scoped project"
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

# ER-phagy

Selective autophagy of the endoplasmic reticulum: a scoped project

<span class="small">AI Gene Review · projects/ER_PHAGY · SCOPING · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **Scoped, not started.** No ER-phagy module and no review made for this project.
- **16 seed/related human genes** listed; **7 COMPLETE**, **2 INITIALIZED**, **7 not started**.
- The defining receptors **RETREG1 (FAM134B), RTN3, CCPG1, TEX264** have **no review yet**.
- GO-CAM already covers one **UFMylation/CYB5R3 reticulophagy** branch.

---

## The biology

![h:470](er-phagy-receptors.svg)

<span class="small">Schematic from the gene roles listed on the project page. Membrane receptors and soluble cargo adaptors bind LC3B/GABARAP through LIR- or UDS-type motifs.</span>

---

## Why this is worth doing

- A **young field**: many receptors were characterized from the mid-2010s into the 2020s, so GO coverage is likely to lag.
- Receptors are **dual-function** membrane proteins (SEC62 is a translocon subunit; ATL3 an ER-fusion GTPase), so the core-vs-non-core call matters.
- Disease links: hereditary sensory neuropathy (RETREG1/FAM134B), ER storage disease, flavivirus infection.

---

## Where the candidate genes stand

![h:470](candidate-coverage.svg)

---

## What the existing reviews already say

- **SEC62**: IMP `reticulophagy` (GO:0061709) kept as **KEEP_AS_NON_CORE**; the core function is the Sec61 translocon.
- **CALCOCO1, RETREG2, UBAC2**: ER-phagy receptor/adaptor reviews now add core reticulophagy biology.
- **CDK5RAP3**: captures the UFM1-dependent positive regulation of reticulophagy.
- **ATL3**: a reticulophagy projection was **not** promoted to a new annotation; the review keeps ER membrane fusion as core and asks for receptor-mutant rescue experiments.
- **ULK1, ATG9A**: initialized in the CONDENSATES phagophore-membrane audit, not ER_PHAGY.

---

## Next steps

1. `just fetch-gene human RETREG1` (and RTN3, CCPG1, TEX264); review them first.
2. Review MAP1LC3B, GABARAP and ERN1.
3. Decide whether an ER-phagy receptor/adaptor module is warranted, alongside `modules/phagophore_assembly_site.yaml`.

**Read more:** `projects/ER_PHAGY.md` · `genes/human/SEC62/` · `genes/human/ATL3/` · `genes/human/CALCOCO1/`
