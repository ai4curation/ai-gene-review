---
title: "UniProt proteome removal: which reviews lose their entry"
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

# UniProt proteome removal

Which gene reviews lose their UniProtKB entry

<span class="small">AI Gene Review · projects/PROTEOME_REMOVAL · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- UniProt listed **~58M TrEMBL entries** from redundant and non-reference proteomes for removal by **release 2026_02** (archived in UniParc).
- A check of the **896** accessions in the repo on 2026-02-03 found **15 reviews** on the list; **none has been re-keyed or archived**.
- On 2026-10-05, **5 are inactive** in UniProtKB REST and **10 are still live**. The repo is now 5,630 folders, so the scan needs re-running.

---

## Why it matters

![h:500](removal-flow.svg)

---

## The 15 flagged reviews today

![h:500](removal-status.svg)

---

## How the check was done

- Used UniProt's **explicit removal list** (`proteins_to_remove_from_UniProtKB.txt`, 578 MB), not proteome membership, which proved unreliable.
- Intersected with the repo's accessions using `LC_ALL=C comm -12` on sorted lists: linear time, but **locale-sensitive**.
- The `just` targets described on the project page are **not in the current justfiles**.

---

## Status and next steps

- ✅ Removal list checked against 896 accessions (Feb 2026): 15 hits.
- ⬜ For the **5 inactive** entries (merB, xdhB, fae1A, stx2A, Q1IFG0): find a retained accession or archive the review.
- ⬜ Decide whether a UniParc UPI is an acceptable review key.
- ⬜ Restore the check as a `just` target and re-run over all 5,630 gene folders.
- Tracked in ai-gene-review#4003.

**Read more:** `projects/PROTEOME_REMOVAL.md`
