---
title: "Peroxisome targeting signal binding obsoletion"
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

# Peroxisome targeting signal binding obsoletion

GO:0005052 · GO:0005053 · GO:0033328 → GO:0000268 peroxisome signal sequence receptor activity

<span class="small">AI Gene Review · projects/PEROXISOME_TARGETING_SIGNAL_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted three signal-specific binding terms** (PTS1, PTS2, mPTS) and merged them into the renamed parent **GO:0000268**.
- The change has **landed** (OLS shows all three obsolete); the page's "not yet applied" status is out of date.
- **Scoped, refresh not started:** 18 rows in the PEX5, PEX7 and PEX19 reviews still use the old ids, 17 of them ACCEPT.

---

## Three children, one parent

![h:480](term-map.svg)

---

## Why the terms went

- Upstream reason: each child "represents a **specific substrate**", the signal sequence.
- One receptor class does the same job for each signal, so the **sequence type is beyond GO's scope**.
- The parent was renamed from *peroxisome targeting sequence binding* to a **receptor activity** term.
- Upstream tally: **45 annotations** affected (UniProt 30, SGD 5, UniProt-extensions 5, AspGD 2, ComplexPortal 2, GeneDB 1), plus the InterPro mapping **IPR044536 → GO:0005053**.

---

## The receptors keep their jobs

![h:480](receptors.svg)

---

## What is in the repo today

| Gene | Obsolete term | Rows | Actions in review |
|---|---|---|---|
| PEX5 | GO:0005052 | 9 (6 IDA, IBA, IMP, IPI) | all ACCEPT |
| PEX5 | GO:0033328 | 1 (IPI) | UNDECIDED |
| PEX7 | GO:0005053 | 7 (5 IDA, IBA, IEA) | all ACCEPT |
| PEX19 | GO:0033328 | 1 (IBA) | ACCEPT |

<span class="small">Already on the parent GO:0000268: PEX5 (IDA, ACCEPT, old label) and PEX39 (IDA, MODIFY: PEX39 is a PTS2 co-receptor that does not bind cargo on its own).</span>

---

## Next steps

1. `just fetch-gene human PEX5` (then PEX7, PEX19) to pull GOA with GO:0000268 in place of the children.
2. Re-review the swapped rows; decide whether GO:0000268 is the right core MF for each receptor.
3. Note the IPR044536 redirect in the PEX7 review; leave SGD/AspGD orthologs to the broader peroxisome project.

**Upstream:** go-annotation#6401 · go-ontology#31419
**Read more:** `projects/PEROXISOME_TARGETING_SIGNAL_OBSOLETION.md` · `projects/PEROXISOME.md`
