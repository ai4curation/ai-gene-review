---
title: "Autoimmune Genetics - Greatest Hits"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [human]
genes: [PTPN22, CTLA4, IL2RA, IL4, STAT4, IL13, IL23R, IL7R, ORMDL3, TNFAIP3, TNFRSF1A, EGR2, BACH2, IRF4, STAT3, IKZF1, CD28, GATA3, SMAD3, IL10]
manifest:
  slides:
    - href: AUTOIMMUNE/slides/AUTOIMMUNE-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/8N7vPAZj25wxqZfyQbJ2Rs
      title: Project brief
---

# Autoimmune Genetics - Greatest Hits

**Bottom line:** GWAS and functional studies have converged on a small set of
immune-regulation genes whose variants raise risk for several autoimmune
diseases at once (type 1 diabetes, rheumatoid arthritis, multiple sclerosis,
inflammatory bowel disease, lupus). We reviewed every existing GO annotation on
20 of the best-replicated of these human genes, covering T cell
co-stimulation and inhibition, cytokine receptors, Th1/Th2/Th17 transcription
factors and NF-kB control. All 20 reviews exist, have every row actioned and
validate: 2,303 annotations, with 1,464 ACCEPT, 390 KEEP_AS_NON_CORE, 142
MARK_AS_OVER_ANNOTATED, 100 MODIFY, 180 REMOVE, 11 UNDECIDED and 16 NEW. Most
removals (150 of 180) are generic `protein binding` IPI rows, 134 of them on
STAT3 and SMAD3; others are propagation errors such as prolactin receptor
activity on IL23R. The per-gene review files are not uniformly finalised (10
COMPLETE, 5 DRAFT, 5 IN_PROGRESS), and #4041 tracks that status cleanup
together with the remaining validation warnings.

We did this because these genes are shared across many autoimmune diseases and
are among the most heavily annotated immune genes (STAT3 456 rows, SMAD3 349,
GATA3 258), so they test whether review can find the core immune-regulatory
function under a large body of interaction and propagated annotations.

## Overview

This project reviews the GO annotations for the most well-established autoimmune susceptibility genes identified through GWAS and functional studies. These genes represent the core molecular machinery of immune regulation, and variants in them confer risk for multiple autoimmune diseases including type 1 diabetes, rheumatoid arthritis, multiple sclerosis, inflammatory bowel disease, and systemic lupus erythematosus.

## Model Species

**Primary: Homo sapiens (human)**

## Gene Categories

### Tier 1: "Greatest Hits" of Autoimmune Genetics

These genes harbor the most strongly replicated and functionally validated autoimmune risk variants:

| Gene | UniProt | Key Function | Associated Diseases |
|------|---------|-------------|-------------------|
| PTPN22 | Q9Y2R2 | T cell receptor signaling phosphatase | T1D, RA, SLE |
| CTLA4 | P16410 | T cell co-inhibitory receptor | T1D, Graves, RA |
| IL2RA | P01589 | IL-2 receptor alpha chain (CD25) | T1D, MS |
| IL4 | P05112 | Th2 cytokine | Asthma, atopy |
| STAT4 | Q14765 | IL-12/IFN signaling transcription factor | RA, SLE |
| IL13 | P35225 | Th2 cytokine | Asthma, IBD |
| IL23R | Q5VWK5 | IL-23 receptor | IBD, psoriasis, AS |
| IL7R | P16871 | IL-7 receptor alpha | MS, T1D |
| ORMDL3 | Q8N138 | ER membrane protein, sphingolipid regulation | Asthma, IBD |
| TNFAIP3 | P21580 | A20, NF-kB negative regulator | SLE, RA, IBD |
| TNFRSF1A | P19438 | TNF receptor 1 | TRAPS, MS |

### Tier 2: Well-Established Autoimmune Risk Genes

| Gene | UniProt | Key Function | Associated Diseases |
|------|---------|-------------|-------------------|
| EGR2 | P11161 | Early growth response TF, T cell anergy | SLE |
| BACH2 | Q9BYV9 | TF regulating B/T cell differentiation | T1D, MS, celiac |
| IRF4 | Q15306 | Interferon regulatory factor | SLE, RA |
| STAT3 | P40763 | JAK-STAT signaling | IBD, hyper-IgE |
| IKZF1 | Q13422 | Ikaros, lymphocyte development TF | SLE, T1D |
| CD28 | P10747 | T cell co-stimulatory receptor | RA, MS |
| GATA3 | P23771 | Th2 lineage TF | Asthma, HDR syndrome |
| SMAD3 | P84022 | TGF-beta signaling | IBD, allergy |
| IL10 | P22301 | Anti-inflammatory cytokine | IBD, SLE |

## Key Pathways

1. **T cell activation/inhibition**: PTPN22, CTLA4, CD28, IL2RA, IL7R
2. **Th1/Th2 polarization**: IL4, IL13, GATA3, STAT4, IRF4
3. **Th17/regulatory T cell balance**: IL23R, STAT3, SMAD3, BACH2
4. **NF-kB/TNF signaling**: TNFAIP3, TNFRSF1A
5. **Immune tolerance**: IL10, EGR2, IKZF1
6. **ER sphingolipid control**: ORMDL3

## Review Status

| Gene | Fetch | Deep Research | Review | Validates | Notes |
|------|-------|--------------|--------|-----------|-------|
| PTPN22 | DONE | DONE (falcon) | DONE | PASS (0w) | Clean |
| CTLA4 | DONE | DONE (falcon) | DONE | PASS (14w) | GO:0005515 policy |
| IL2RA | DONE | DONE (falcon) | DONE | PASS (1w) | Deep research not cited |
| IL4 | DONE | DONE (falcon) | DONE | PASS (0w) | Clean |
| STAT4 | DONE | DONE (falcon) | DONE | PASS (3w) | GO:0005515 policy; deep research not cited |
| IL13 | DONE | DONE (falcon) | DONE | PASS (0w) | Clean |
| IL23R | DONE | DONE (falcon) | DONE | PASS (0w) | Clean |
| IL7R | DONE | DONE (falcon) | DONE | PASS (3w) | GO:0005515 policy; deep research not cited |
| ORMDL3 | DONE | DONE (falcon) | DONE | PASS (1w) | GO:0005515 policy |
| TNFAIP3 | DONE | DONE (falcon) | DONE | PASS (21w) | GO:0005515 policy; deep research not cited |
| TNFRSF1A | DONE | DONE (falcon) | DONE | PASS (1w) | Deep research not cited |
| EGR2 | DONE | DONE (falcon) | DONE | PASS (2w) | Deep research/core-function coverage |
| BACH2 | DONE | DONE (falcon) | DONE | PASS (3w) | Deep research/core-function coverage |
| IRF4 | DONE | DONE (falcon) | DONE | PASS (3w) | GO:0005515 policy; deep research not cited |
| STAT3 | DONE | DONE (falcon) | DONE | PASS (0w) | Clean |
| IKZF1 | DONE | DONE (falcon) | DONE | PASS (8w) | GO:0005515 policy |
| CD28 | DONE | DONE (falcon) | DONE | PASS (0w) | Clean |
| GATA3 | DONE | DONE | DONE | PASS (0w) | Clean |
| SMAD3 | DONE | DONE (falcon) | DONE | PASS (1w) | Deep research not cited |
| IL10 | DONE | DONE (falcon) | DONE | PASS (0w) | Clean |

---
# STATUS

All 20 genes are fetched, deep-researched with Falcon, reviewed, actioned, and validated. All pass with 0 errors; 10 are COMPLETE and #4041 tracks the 5 DRAFT and 5 IN_PROGRESS reviews that still need final status cleanup.

- [x] Fetch all genes
- [x] Deep research all genes (falcon)
- [x] Initial annotation reviews for all genes
- [x] Fix IL23R validation error (core_functions schema + supporting_text)
- [x] Resolve inconsistent review actions (IL4, IL7R, CD28, IL10)
- [x] Final validation pass - all 20 genes PASS (0 errors)
- [x] STAT3 deep research (falcon)
- [ ] Finalise remaining DRAFT/IN_PROGRESS reviews (#4041)
- [ ] Migrate remaining GO:0005515 MARK_AS_OVER_ANNOTATED calls (#4041)
- [ ] Resolve Falcon evidence-linkage and core-function coverage warnings (#4041)

# NOTES

## 2026-02-14

- All reviews in the then-current duplicated-row table had actions set; the 2026-10-04 audit covers 20 unique genes
- IL23R had invalid core_functions schema (used old format with term/statement/evidence_summary instead of molecular_function/directly_involved_in/description) - fixed
- IL23R also has ~35 supporting_text errors (case sensitivity, paraphrasing instead of exact quotes) - fixing via annotation-reviewer agent
- Inconsistent review actions found in IL4, IL7R, CD28, IL10 - typically UNDECIDED annotations where publications weren't cached at review time but are now available
- GATA3 is the only gene that validates cleanly with 0 warnings
- Most warnings are about references with findings lacking supporting_text (exact quotes from publications)

## 2026-02-15

- All validation errors resolved across the then-current review set - every gene now PASS with 0 errors
- IL23R: Fixed core_functions schema (old format → new), fixed ~35 supporting_text errors (non-contiguous quotes, case mismatches). Now PASS (12w)
- IL4: Resolved UNDECIDED annotations → ACCEPT/KEEP_AS_NON_CORE for GO:0045893, GO:0030335, GO:0045892. Now PASS (14w)
- IL7R: Resolved UNDECIDED → ACCEPT for GO:0004896, MODIFY for GO:0019725. Added supporting_text to 17 refs. Now PASS (2w)
- CD28: Resolved GO:0042110 inconsistency (IGI UNDECIDED→ACCEPT). Added supporting_text to ~40 reference findings. Down from 42w to 2w
- IL10: Resolved UNDECIDED → ACCEPT/KEEP_AS_NON_CORE for GO:0140105, GO:0045944, GO:0045893. Now PASS (34w)
- Remaining work at that point was supporting_text coverage improvements plus STAT3 deep research; superseded by the 2026-10-04 validator-warning snapshot below.

## 2026-10-04

- Re-audited the 20 human AUTOIMMUNE reviews against the current YAML. The cohort now has 2,303 review rows: 2,287 existing GOA annotations and 16 proposed NEW annotations.
- Current action totals are 1,464 ACCEPT, 390 KEEP_AS_NON_CORE, 142 MARK_AS_OVER_ANNOTATED, 100 MODIFY, 180 REMOVE, 11 UNDECIDED, and 16 NEW.
- Updated stale project/deck statistics after downstream gene-review edits, corrected the ORMDL3 UniProt accession to Q8N138, and removed the stale STAT3 deep-research TODO now that `STAT3-deep-research-falcon.md` exists.
- Opened #4041 to track the remaining non-COMPLETE statuses (5 DRAFT, 5 IN_PROGRESS) and outstanding validation warnings: old GO:0005515 policy calls, missing Falcon evidence links, and BACH2/EGR2 core-function coverage warnings.
