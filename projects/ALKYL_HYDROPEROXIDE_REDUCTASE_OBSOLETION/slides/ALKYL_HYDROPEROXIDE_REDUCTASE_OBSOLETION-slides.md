---
title: "Alkyl hydroperoxide reductase activity obsoletion"
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

# Alkyl hydroperoxide reductase activity obsoletion

GO:0008785 → GO:0102039 NADH-dependent peroxiredoxin activity

<span class="small">AI Gene Review · projects/ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- GO **obsoleted GO:0008785**, a term tied to one substrate (octane hydroperoxide), and merged it into **GO:0102039** (EC 1.11.1.26).
- The ontology change is **merged**; only **2 experimental annotations** (E. coli AhpF, P. aeruginosa PA3529) still need moving.
- **Scoped, not yet started:** neither gene is reviewed in this repo, so no existing review is affected.

---

## Old term → replacement

![h:480](term-map.svg)

---

## Why the term went

- GO:0008785 was defined by **one stoichiometry**: octane hydroperoxide + NADH → 1-octanol.
- No known gene product is that specific; the enzymes reduce a **range of peroxides**.
- Expasy lists "alkyl hydroperoxide reductase" as a **synonym of EC 1.11.1.26**, which is exactly GO:0102039.
- The **complex** term GO:0009321 stays; only its comment now points to GO:0102039.

---

## The biology does not change

![h:470](ahpcf-mechanism.svg)

---

## What is in the repo today

- `genes/ECOLI/` and `genes/PSEAE/`: **no AhpF or PA3529 review**.
- `genes/PSEPK/ahpC/`: the one review that touches GO:0102039. Its IEA row is **MODIFY → GO:0051920** *peroxiredoxin activity*, because AhpC alone is the peroxidase and AhpF supplies the NADH electrons.
- Priority is **low**: the value is extending bacterial coverage, not unblocking a review.

---

## Next steps

1. `just fetch-gene ECOLI` for **AhpF**; check that GOA shows GO:0008785 as obsolete and review per CLAUDE.md.
2. Then **PA3529 / Q9HY81**; confirm the symbol UniProt uses before creating the folder.
3. Defer PTHR10681 IBA review until GOA reflects the obsoletion.

**Upstream:** go-annotation#6396 (open) · go-ontology#31961 · PR #32015 (merged)
**Read more:** `projects/ALKYL_HYDROPEROXIDE_REDUCTASE_OBSOLETION.md`
