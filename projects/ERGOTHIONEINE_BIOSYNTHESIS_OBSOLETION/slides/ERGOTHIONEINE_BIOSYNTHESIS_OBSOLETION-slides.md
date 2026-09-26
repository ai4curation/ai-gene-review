---
title: "Ergothioneine biosynthesis variant-term obsoletion"
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

# Ergothioneine biosynthesis variant-term obsoletion

GO:0052704 and GO:0140479 → GO:0052699 ergothioneine biosynthetic process

<span class="small">AI Gene Review · projects/ERGOTHIONEINE_BIOSYNTHESIS_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted both route-specific children** of GO:0052699: bacterial GO:0052704 and fungal GO:0140479.
- The only experimental rows are **4 IDA annotations** on the *M. smegmatis* **egtBCDE** operon (PMID:20420449); ~2,247 IEA rows re-infer automatically.
- **Scoped, not yet started:** no review here uses these terms and no *egt* gene is reviewed.

---

## Old terms → parent

![h:480](term-map.svg)

---

## Two routes, one product

![h:470](egt-pathway.svg)

---

## Why the routes went

- The children named the **intermediate** a pathway passes through, not a different outcome.
- GO's obsoletion note: these terms "represent a GO-CAM model".
- The route detail survives as **narrowMatch** links to MetaCyc PWY-7255 (bacteria) and PWY-7550 (fungi).
- Each enzyme's own **molecular function** still says which step it does.

---

## Next steps

1. If wanted, review the operon as one batch: **egtD, egtB, egtC, egtE** (A0R5M8, A0R5N0, A0R5M9, A0R5M7), sharing PMID:20420449.
2. Anchor each on its catalytic MF; BP on **GO:0052699**.
3. Confirm the species folder first: the repo has `genes/MYCSM/`, while the page proposes `MYCS2` for strain mc(2)155.
4. S. pombe egt1/egt2 are unaffected and optional.

**Upstream:** go-annotation#6402 · go-ontology#32018 · go-ontology#11163
**Read more:** `projects/ERGOTHIONEINE_BIOSYNTHESIS_OBSOLETION.md`
