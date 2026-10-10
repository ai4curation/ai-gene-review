---
title: "Nitratidesulfovibrio vulgaris: four pathways reviewed"
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

# *Nitratidesulfovibrio vulgaris* Hildenborough

GO review of four pathways in the model sulfate-reducing bacterium

<span class="small">AI Gene Review · projects/NITV2_PATHWAYS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- We reviewed **23 genes** in sulfate reduction, potassium transport, sigma factors and hydrogen metabolism; **20 have manual actions** (178 rows), 3 hydrogenase stubs are still `PENDING`.
- The main fix is **separating catalytic from accessory subunits**: AprB, KdpC and the TrkA-type RCK proteins lose inherited catalytic or transporter terms.
- A wrong reassignment of DVU0848–0849 to Flx–Hdr was reverted to **QmoA/QmoB** in PR #3226: they sit in the *aprBA–qmoABC* cluster; Flx–Hdr is DVU2399–2405.

---

## Why this organism

- **Model sulfate reducer**: sulfate is the terminal electron acceptor of anaerobic respiration.
- Annotation is almost entirely electronic, so each pathway is a test of how well pipelines assign subunit roles.
- Four pathways: sulfate reduction (AprAB, QmoABC, a SulP permease), K⁺ transport (Kdp, Trk), sigma factors, and periplasmic and cytoplasmic hydrogenases.

---

## Who does the work in K⁺ uptake

![h:500](potassium-systems.svg)

---

## KdpC is a chaperone, not an ATPase

![h:450](kdpC-review-table.jpg)

<span class="small">kdpC (Q725T8): process row accepted; `nucleotide binding`, `ATP binding` and `hydrolase activity` removed; transporter MF replaced by ATPase activator activity (GO:0001671).</span>

---

## Other corrections

- **AprB** (Q72DT3): adenylyl-sulfate reductase activity → **electron transfer activity**; AprA keeps the catalytic term and gains dissimilatory sulfate reduction.
- **AprA**: `succinate dehydrogenase activity` (IEA) **removed**.
- **Sigma factors**: DNA-binding TF activity → **sigma factor activity** (GO:0016987) on rpoD, rpoH, fliA; RNA polymerase activity removed from fliA.
- **rpoC** is the RNA polymerase β′ core subunit, not a sigma factor.
- **DVU0279**: a SulP-family transporter whose sulfate substrate is unproven.

---

## Results

![h:480](actions-bar.svg)

---

## Status and next steps

- ✅ Sulfate reduction (6), potassium transport (7), sigma factors (5) reviewed.
- ◐ Hydrogenases: hydA and hynA1 reviewed; hysA, echA, cooH still `PENDING`.
- ✅ DVU0848–0849 restored to QmoA/QmoB; QmoB dropped two unsupported `NEW` rows.
- ⬜ Finish hysA, echA and cooH (#3981).

**Read more:** `projects/NITV2_PATHWAYS.md` · `genes/DESVH/<accession>/`
