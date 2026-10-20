---
title: "Chimeric mRNA trans-fusions in immunity"
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

# Chimeric mRNA trans-fusions in immunity

One protein, two genes: what GSDMD:TMEM106A means for gene-function curation

<span class="small">AI Gene Review · projects/CHIMERIC_MRNA_IMMUNITY · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Inflamed mouse macrophages make a **trans-spliced GSDMD:TMEM106A** chimera that **speeds GSDMD pore formation and IL-1β release** (PMID:42686912).
- We reviewed both human parents, **GSDMD** (77 rows) and **TMEM106A** (10 rows), and recorded the chimera as a **knowledge gap**, not as an annotation of either.
- No human chimera has been shown; the remaining work is a set of **open questions**.

---

## How the chimera forms and acts

![h:490](trans-splicing-mechanism.svg)

---

## Why it matters for curation

1. **Attribution.** GO assumes one gene → one set of products. A chimera's function is not an annotation of either parent.
2. **The wrong-frame trap.** The TMEM106A part is an out-of-frame peptide, so canonical TMEM106A function does not transfer.
3. **Ortholog scope.** Characterized in mouse only; human reviews must flag it as unresolved.

| Phenomenon | DNA change? | Parent loci | Mechanism |
|---|---|---|---|
| Trans-spliced chimera | No | often different chromosomes | RNA trans-splicing |
| cis read-through | No | adjacent, same strand | transcription past gene 1 |
| DNA fusion gene | Yes | any | translocation |

---

## Where the function is recorded

![h:490](attribution.svg)

---

## Status and open questions

- ✅ GSDMD and TMEM106A reviews COMPLETE (54 ACCEPT, 18 non-core, 15 over-annotated across 87 rows).
- ⬜ Does a **human** GSDMD:TMEM106A chimera exist and function?
- ⬜ What specifies which transcript pairs are trans-spliced during inflammation?
- ⬜ By what criteria should a chimera be curated as a distinct gene product for GO?
- Source is **abstract-only** in the cache; no catalogue size is quoted.

**Read more:** `projects/CHIMERIC_MRNA_IMMUNITY.md` · `genes/human/GSDMD/` · `genes/human/TMEM106A/`
