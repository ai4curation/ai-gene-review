---
title: "SNIPE: a membrane nuclease against phage"
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

# SNIPE

A membrane-bound nuclease that cuts phage DNA during injection

<span class="small">AI Gene Review · projects/SNIPE · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- **SNIPE** cuts phage DNA **as it crosses the inner membrane**, using the phage tape measure protein to aim its GIY-YIG nuclease (Saxton et al. 2026, PMID:41741653).
- The *E. coli* protein (A0A8T9CRB7) had **no GO annotations**; our review proposes **7 annotations** and **2 new process terms**.
- GO has **no SNIPE-specific process**: anti-phage nucleic-acid defence is framed as clearing *intracellular* DNA. A GO issue is drafted; the review is still DRAFT.

---

## The mechanism

![h:490](snipe-mechanism.svg)

---

## Why it matters

- A third way to tell self from non-self: **location**, not sequence (CRISPR) or modification (R-M).
- Homologues in **~33% of well-sequenced bacterial clades**; IPR025280 (ex-DUF4041) has 1,612 protein matches.
- **Direct** defence: the infected cell survives, unlike abortive infection.
- InterPro2GO needs the full architecture: `IPR025280`, a GIY-YIG co-feature, and membrane-targeting evidence.

---

## What the review proposes

| Aspect | Term (all NEW, IDA, PMID:41741653) |
|---|---|
| MF | `GO:0004520` DNA endonuclease activity · `GO:0003690` dsDNA binding |
| BP | `GO:0051607` defense response to virus · `GO:0045071` neg. reg. of viral genome replication |
| BP | `GO:0046597` host-mediated suppression of symbiont invasion · `GO:0006308` DNA catabolic process |
| CC | `GO:0005886` plasma membrane |

<span class="small">GOA held no rows for A0A8T9CRB7, so every annotation is proposed.</span>

---

## GO cannot place it yet

![h:490](go-hierarchy-gap.svg)

---

## Two new terms, as rendered

![h:440](snipe-proposed-terms.jpg)

---

## Status and next steps

- ✅ Paper summarized; full gene review (`genes/ECOLX/SNIPE/`, DRAFT) with bioinformatics.
- ✅ GO issue drafted: [GO hierarchy NTR](../go-issue-antiviral-nucleic-acid-defense.html) (no filed number recorded).
- ✅ Architecture-aware IPR025280 analysis for conservative InterPro2GO design.
- ⬜ Check GO annotations on SNIPE homologues; cross-reference DefenseFinder.
- ⬜ Propose architecture-aware InterPro2GO mappings for PF13250 / IPR025280.

**Read more:** `projects/SNIPE.md` · `genes/ECOLX/SNIPE/SNIPE-ai-review.yaml`
