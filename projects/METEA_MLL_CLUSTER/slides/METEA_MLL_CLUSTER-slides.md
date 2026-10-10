---
title: "The mll cluster: a lanthanophore, not a siderophore"
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

# The *mll* lanthanophore cluster

Re-annotating an "iron-siderophore" system in *Methylorubrum extorquens* AM1 as lanthanide acquisition

<span class="small">AI Gene Review · projects/METEA_MLL_CLUSTER · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- The *mll* cluster makes and imports **methylolanthanin**, a lanthanide chelator that feeds the **XoxF methanol dehydrogenase**.
- Databases call it **iron-siderophore** machinery (homology to aerobactin and petrobactin genes). We reviewed all **10 genes** to replace that story.
- **31 rows**: iron-transport rows on MluA removed or generalised, 8 NEW rows for genes with little or no GOA; GO has **no lanthanophore term**, so one is proposed.

---

## How the system works

![h:500](lanthanophore-system.svg)

---

## Why it was misannotated

| Feature | Iron siderophores | Methylolanthanin |
|---|---|---|
| Metal | Fe³⁺ | La³⁺, Ce³⁺, Nd³⁺ ... |
| Induced by | iron limitation | lanthanide limitation (~32-fold) |
| Enzyme families | IucA/IucC, AsbD/AsbE | MllA (IucA-like), MllBC (AsbD/E-like) |
| Receptor | FepA, FpvA (TonB) | MluA (TonB) |
| Regulation | Fur | MluI / MluR (ECF σ / anti-σ) |

<span class="small">Homology to the iron enzymes is real; the substrate and product are not iron.</span>

---

## Correcting MluA

![h:450](mluA-review-table.jpg)

<span class="small">mluA review: `iron ion transport` removed; `siderophore-iron transmembrane transporter activity` generalised to transmembrane transporter activity.</span>

---

## What changed across 10 genes

| Action | Rows | Where |
|---|---|---|
| ACCEPT | 8 | acid-amino acid ligase (MllA, MllBC), outer membrane, sigma / anti-sigma |
| KEEP_AS_NON_CORE | 7 | e.g. MllA siderophore biosynthesis (analogous chemistry) |
| NEW | 8 | mllDE, mllF, mllJ had no GOA; one on mllH |
| REMOVE | 4 | 3 iron rows on MluA; wrong EC ligase on MllBC |
| MODIFY | 3 | 2 iron-transporter MF on MluA; MllH acyltransferase |
| MARK_AS_OVER_ANNOTATED | 1 | MluI generic TF activity |

<span class="small">mllG has no GOA and no molecular function asserted: DUF2218, and the only name is a machine prediction.</span>

---

## Status and next steps

- ✅ 10/10 reviews exist; deep research from Perplexity and Falcon for each gene.
- ⬜ Review files are `DRAFT` or `INITIALIZED` except mllDE; six per-gene follow-ups plus mllF/mllG/mllJ finishing work are tracked in #4126.
- ⬜ Consolidate the **lanthanophore biosynthetic process** NTR; decide whether MluA can support a lanthanide-metallophore transport term.

**Read more:** `projects/METEA_MLL_CLUSTER.md` · `genes/METEA/mll*/` · `genes/METEA/mlu*/` · related: `projects/REE.md`
