---
title: "Allergens: know what it does before you knock it out"
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

# Allergens

Know what a protein does before you knock it out

<span class="small">AI Gene Review · projects/ALLERGENS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- Allergens are being **knocked out, neutralized and engineered**, yet many have **no known native function**.
- We built an allergen→UniProt index, a UniProt registry worklist and an IEDB epitope ETL, then reviewed **24 genes** (cat, dog, horse, cow, mouse, rat, mite, birch + Scgb1a1): **219 existing rows (0 removed, 60 over-annotated) plus 18 new**.
- The top priorities, **Bet v 1, Fel d 1, Can f 1**, are heavily IgE-targeted and their native role is **still unknown**.

---

## Why an allergens cohort

- **CRISPR** knockout of Fel d 1 genes (CH1/CH2) for hypoallergenic cats (PMID:35386981); **antibody** neutralization; **immunotherapy**.
- Each intervention abolishes or suppresses a protein. The safety question is a gene-function question: **what do we lose?**
- Allergenicity is an IgE property of a sensitized human, **not an evolved function**. The label only selects genes; it never changes a GO annotation.

---

## The triage layer

![h:490](triage-pipeline.svg)

---

## Where the priorities fall

![h:490](priority-quadrant.svg)

---

## What a review looks like

![h:430](ch1-review-table.jpg)

<span class="small">Fel d 1 chain 1 (CH1): secretion accepted, IBA steroid binding kept as non-core; NEW rows add Ca²⁺ binding, LPS binding and TLR4 enhancement.</span>

---

## Findings

- **Fel d 1** and **Der p 2** both get NEW `GO:0001530` LPS binding and `GO:0034145` positive regulation of TLR4 signalling: two unrelated allergens acting as **auto-adjuvants**.
- **Mus m 1 / Rat n 1** (MUPs): 20 over-annotated rows each, mostly ISS metabolic and insulin-signalling terms.
- **Bet v 1**: ABA-receptor, phosphatase-inhibitor and signalling-receptor rows marked over-annotated (fold-based IEA).
- **Der p 23**: GOA's NOT chitin binding (IDA) accepted; the peritrophin-like domain does not bind chitin.

---

## Status and next steps

- ✅ 24 gene reviews (all DRAFT); index 32 genes / 31 molecules; IEDB axis live.
- ⬜ Registry coverage is small: 6 of 1,020 reviewed UniProt allergen entries when last counted; 1,014 on the worklist.
- ⬜ Extend the IEDB name-join to protein-name-labelled allergens (human `Hom s …`).
- ⬜ Continue the backlog by priority: pollens, foods, molds, insects.

<span class="small">Open tracker: ai4curation/ai-gene-review#4033</span>

**Read more:** `projects/ALLERGENS.md` · `projects/ALLERGENS/allergen_index.tsv`
