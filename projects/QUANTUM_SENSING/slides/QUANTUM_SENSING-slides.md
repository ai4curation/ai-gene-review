---
title: "Quantum sensing proteins: scoping radical-pair magnetoreception"
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

# Quantum sensing proteins

Scoping cryptochromes and engineered flavoproteins as magnetic sensors

<span class="small">AI Gene Review · projects/QUANTUM_SENSING · scoping · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- The best-supported quantum sensor is the **radical-pair compass** in cryptochromes: light-made spin pairs whose chemistry feels weak magnetic fields.
- From one deep-research report we shortlisted **5 proteins** (robin CRY4, monarch CRY1, human CRY2, fly CRY, MagLOV) and **5 chassis**, and flagged contested areas.
- **Scoped, not started** as a native-robin / monarch / MagLOV review set; existing fly and Arabidopsis CRY reviews keep magnetoreception as **non-core**.

---

## How the compass is thought to work

![h:520](radical-pair.svg)

---

## Mechanisms and their GO terms

![h:520](mechanisms-go.svg)

---

## Open scoping questions

- Biological sensor (behaviour, cell signalling) or an in vitro spin-chemistry module?
- Geomagnetic-field sensing only, or broader coherence and tunnelling effects?
- Which chassis: purified protein, yeast or mammalian cells, insect cells, plants, or magnetotactic bacteria?
- Treat fly behaviour and vibrational olfaction as **contested**; photosynthetic coherence is energy transfer, not sensing.

---

## Status and next steps

- ✅ Deep-research synthesis, candidate shortlist, chassis options (Jan 2026).
- ⬜ Triage pipeline described on the page is **not in the repo** (`projects/quantum-sensing-bioinformatics/`).
- ⬜ Triage robin CRY4 and monarch CRY1 accessions; decide whether engineered MagLOV constructs belong in a gene-review project.
- ⬜ Reassess fly and plant CRY magnetoreception rows before treating them as more than contested, non-core outputs.
- Side note in the folder: `LIGHT_SOURCE_OPEN_DATASETS.md` (open X-ray datasets), unrelated to the review.

**Read more:** `projects/QUANTUM_SENSING.md`
