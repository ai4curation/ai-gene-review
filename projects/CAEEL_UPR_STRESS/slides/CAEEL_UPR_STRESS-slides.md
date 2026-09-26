---
title: "C. elegans unfolded protein responses: reviewing 18 stress genes"
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

# Unfolded protein responses in *C. elegans*

Reviewing GO annotations for 18 genes of the ER and mitochondrial stress responses

<span class="small">AI Gene Review · projects/CAEEL_UPR_STRESS · 2026</span>

---

<!-- _class: bluf -->

## Bottom line

- ER stress is sensed by **IRE-1, PEK-1 and ATF-6**; mitochondrial stress by **ATFS-1** with DVE-1, UBL-5 and chromatin regulators.
- We reviewed **every GO annotation on 18 genes**: **421 rows**, 344 ACCEPT, 13 MODIFY, 5 REMOVE, 21 NEW.
- The five removals each fix a **specific error**, e.g. protein tag activity on UBL-5, which cannot be conjugated.

---

## Why the worm

- Non-cell-autonomous UPR was found here: neurons can switch on stress responses in the intestine.
- hsp-4::GFP and hsp-6::GFP are standard in vivo reporters.
- ATF-6 deletion extends lifespan through ER-mitochondrial calcium signalling.
- Test: does GO keep **sensors**, **transcription factors** and **reporter chaperones** apart?

---

## The two responses and the 18 genes

![h:500](upr-branches.svg)

---

## Actions per gene

![h:500](upr-actions.svg)

---

## The five removals

| Gene | Term | Evidence | Why |
|---|---|---|---|
| ubl-5 | protein tag activity | IBA | no C-terminal di-Gly; acts non-covalently |
| hsp-60 | RNA Pol II TF binding | IPI | paper showed DVE-1 on the *hsp-60* promoter |
| jmjd-3.1 | RNA Pol II cis-regulatory DNA binding | IBA | no intrinsic DNA-binding domain |
| met-2 | histone H3K36 methyltransferase activity | IMP | SETDB1-family enzymes are H3K9-specific |
| ire-1 | unfolded protein binding | IBA | obsolete term; sensing is not chaperone binding |

<span class="small">From review.reason in genes/worm/&lt;gene&gt;/&lt;gene&gt;-ai-review.yaml.</span>

---

## What was added

- **MET-2**: histone H3K9 dimethyltransferase activity, constitutive heterochromatin formation, transposable element silencing (IMP).
- **UBL-5**: splicing factor binding and transcription coactivator activity (IDA).
- **ATF-4**: integrated stress response signalling (IMP); **ATF-6**: ER calcium ion homeostasis (IMP).
- **HSP-6**: mitochondrial matrix (IDA), protein import into the matrix (ISS).

---

## Status and next steps

- ✅ 18/18 gene reviews and the pathway summary; atfs-1 and hsp-4 shared with CAEEL_MITOPHAGY and CAEEL_PROTEOSTASIS.
- ⬜ Listed but not reviewed: atf-5, abu-8, abu-11, jmjd-1.2 (hsp-3 has a review outside this project).

**Read more:** `projects/CAEEL_UPR_STRESS.md` · `projects/CAEEL_UPR_STRESS/CAEEL_UPR_STRESS-pathway.md` · `genes/worm/<gene>/`
