---
title: "Reactome black box events: filling missing transporters"
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

# Reactome black box events

Can gene reviews name the missing transporters in pathway reactions?

<span class="small">AI Gene Review · projects/REACTOME_GAP_FILLING · 2026 · scoping, one pilot</span>

---

<!-- _class: bluf -->

## Bottom line

- Reactome **black box events** are reactions that must happen but have **no assigned catalyst or transporter**, often at an organelle membrane.
- **Pilot done: ABCD3** (81 annotations reviewed) gets a **NEW bile acid transmembrane transporter** term for peroxisomal import of C27 bile-acid CoA esters.
- **Scoped, not started** beyond that: no systematic black-box query yet; the other bile acid gaps have no candidate reviewed.

---

## The pilot pathway

![h:470](bile-acid-compartments.svg)

---

## How ABCD3 was resolved

![h:470](evidence-tiers.svg)

---

## Workflow and expansion targets

1. **Identify** black box events in a Reactome pathway; sort by reaction type and membrane.
2. **Candidates** from GO, expression, domain architecture, deep research.
3. **Converge** with a full gene review: activity, loss of function, structure, localization.
4. **Tier** the result and report to Reactome curators.

Next areas: mitochondrial SLC25 carriers, cholesterol and sphingolipid trafficking, other ABC families, peroxisomal SLCs.

---

## Status

- One gene review (`genes/human/ABCD3/`), proposing NEW `GO:0015125` (IMP).
- Reactome R-HSA-382575 lists ABCD3 for LCFA transport but not for bile-acid CoA esters: an update to propose.
- Collaboration with Reactome curators (P. D'Eustachio, L. Matthews).

**Read more:** `projects/REACTOME_GAP_FILLING.md` · `genes/human/ABCD3/ABCD3-ai-review.yaml`
