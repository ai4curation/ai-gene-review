---
title: "UniPathway unique terms: auditing a legacy pathway mapping"
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

# UniPathway unique terms

Auditing GO_REF:0000041, a legacy pathway-vocabulary mapping, where it is the only source

<span class="small">AI Gene Review · projects/UNIPATHWAY · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **Closure filtering** removes rows already supported at the same or a more specific term: human UniPathway rows drop from **1,129 to 247** truly unique.
- **32 exemplar rows** across 9 organisms reviewed: **24 ACCEPT**. UniPathway is a net positive pathway gap filler, strongest in microbes.
- Errors are specific, not systemic: **UBA7** (ISG15, not ubiquitin) MODIFY; **nrfA** (not nitrate assimilation) REMOVE; **NorR** regulators over-annotated to denitrification.

---

## Why audit UniPathway

- `GO_REF:0000041` maps UniPathway pathways to GO BP terms. UniPathway is **archived and unmaintained**, yet its rows still sit in GOA.
- Question: is it a source to **trust, clean, or retire**?
- Same approach as the SPKW project: a row only counts as uniquely informative if **no other source** supports the gene at that term **or a descendant**.
- Review by biologically coherent **term groups** (ubiquitination, nitrogen cycle, plant cell wall), not random sampling.

---

## Most UniPathway rows are already covered

![h:470](unipathway-closure-filter.svg)

---

## The hard case: protein ubiquitination

![h:470](ubiquitination-boundary.svg)

---

## Nitrogen cycle: enzymes vs regulators vs wrong endpoint

| Gene (organism) | UniPathway term | Action |
|---|---|---|
| nirK1, nirK2, nosZ (*R. palustris*) | denitrification pathway | ACCEPT |
| Ferp_0128 (*Ferroglobus*) | denitrification pathway | ACCEPT |
| ureC1, ureC2 (*N. viennensis*) | urea catabolic process | ACCEPT |
| norR1, norR2 (*Cupriavidus*) | denitrification pathway | MARK_AS_OVER_ANNOTATED |
| nrfA (*Desulfotalea*) | nitrate assimilation | REMOVE |
| AJ80_06654 (fungus, singleton) | denitrification pathway | UNDECIDED |

<span class="small">nrfA is an ammonia-forming cytochrome c nitrite reductase (GO:0042279), a dissimilatory enzyme. NorR is an NO-responsive sigma-54 activator, not a pathway enzyme.</span>

---

## Outcome across all exemplars

![h:470](unipathway-exemplar-actions.svg)

---

## Patterns

1. **Metabolic enzyme in its pathway → ACCEPT** (COX5B, catA, algE, Brachypodium PAL and UXS).
2. **Modification buckets need the mechanism**: E3s and substrate adaptors yes; UBL enzymes and DUBs no.
3. **Broad lipid parents** are correct but not core (GK5, PM20D1 non-core; LPCAT1 over-annotated).
4. **Regulators are not pathway enzymes** (norR1, norR2).
5. **Microbial signal dwarfs vertebrate**: 165,344 TRUE-unique bacterial rows vs 247 in human.

---

## Status and next steps

- Scans done: 13 single-species databases + 6 clade aggregates; **32 exemplar reviews** in `genes/`.
- Not yet done: full human `UPA00143` audit (124 genes), retinol/cholesterol CYP subset, bacterial denitrification set (615 rows, 530 taxa), nrfA nitrate-assimilation tail (14 rows).
- Recommendation: keep closure filtering as default; review microbial rows by term group.

**Read more:** `projects/UNIPATHWAY.md` · `genes/human/UBA7/` · `genes/DESPS/nrfA/`
