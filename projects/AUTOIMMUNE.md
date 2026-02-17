# Autoimmune Genetics - Greatest Hits

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
| ORMDL3 | Q9P0S3 | ER membrane protein, sphingolipid regulation | Asthma, IBD |
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
6. **ER stress/UPR (immune context)**: ORMDL3

## Review Status

| Gene | Fetch | Deep Research | Review | Validates | Notes |
|------|-------|--------------|--------|-----------|-------|
| PTPN22 | DONE | DONE (falcon) | DONE | PASS (4w) | |
| CTLA4 | DONE | DONE (falcon) | DONE | PASS (1w) | |
| IL2RA | DONE | DONE (falcon) | DONE | PASS (34w) | Refs need supporting_text |
| IL4 | DONE | DONE (falcon) | DONE | PASS (14w) | Inconsistencies resolved |
| STAT4 | DONE | DONE (falcon) | DONE | PASS (12w) | |
| IL13 | DONE | DONE (falcon) | DONE | PASS (17w) | |
| IL23R | DONE | DONE (falcon) | DONE | PASS (12w) | core_functions + supporting_text fixed |
| IL7R | DONE | DONE (falcon) | DONE | PASS (2w) | Inconsistencies resolved |
| ORMDL3 | DONE | DONE (falcon) | DONE | PASS (1w) | |
| TNFAIP3 | DONE | DONE (falcon) | DONE | PASS (32w) | Refs need supporting_text |
| TNFRSF1A | DONE | DONE (falcon) | DONE | PASS (13w) | |
| EGR2 | DONE | DONE (falcon) | DONE | PASS (3w) | |
| BACH2 | DONE | DONE (falcon) | DONE | PASS (15w) | |
| IRF4 | DONE | DONE (falcon) | DONE | PASS (9w) | |
| STAT3 | DONE | DONE (falcon) | DONE | PASS (0w) | Clean |
| IKZF1 | DONE | DONE (falcon) | DONE | PASS (1w) | |
| CD28 | DONE | DONE (falcon) | DONE | PASS (2w) | Inconsistencies resolved, supporting_text added |
| GATA3 | DONE | DONE | DONE | PASS (0w) | Clean |
| SMAD3 | DONE | DONE (falcon) | DONE | PASS (2w) | |
| IL10 | DONE | DONE (falcon) | DONE | PASS (34w) | Inconsistencies resolved |

---
# STATUS

All 19 unique genes (20 rows) fetched, deep-researched (falcon), reviewed, and validated. All pass with 0 errors.

- [x] Fetch all genes
- [x] Deep research all genes (falcon)
- [x] Initial annotation reviews for all genes
- [x] Fix IL23R validation error (core_functions schema + supporting_text)
- [x] Resolve inconsistent review actions (IL4, IL7R, CD28, IL10)
- [x] Final validation pass - all 19 genes PASS (0 errors)
- [ ] Address remaining supporting_text warnings (mostly IL2RA, IL10, TNFAIP3)
- [ ] STAT3 deep research (falcon)

# NOTES

## 2026-02-14

- All 19 unique genes (20 rows including STAT3) have reviews completed with actions set
- IL23R had invalid core_functions schema (used old format with term/statement/evidence_summary instead of molecular_function/directly_involved_in/description) - fixed
- IL23R also has ~35 supporting_text errors (case sensitivity, paraphrasing instead of exact quotes) - fixing via annotation-reviewer agent
- Inconsistent review actions found in IL4, IL7R, CD28, IL10 - typically UNDECIDED annotations where publications weren't cached at review time but are now available
- GATA3 is the only gene that validates cleanly with 0 warnings
- Most warnings are about references with findings lacking supporting_text (exact quotes from publications)

## 2026-02-15

- All validation errors resolved across all 19 genes - every gene now PASS with 0 errors
- IL23R: Fixed core_functions schema (old format → new), fixed ~35 supporting_text errors (non-contiguous quotes, case mismatches). Now PASS (12w)
- IL4: Resolved UNDECIDED annotations → ACCEPT/KEEP_AS_NON_CORE for GO:0045893, GO:0030335, GO:0045892. Now PASS (14w)
- IL7R: Resolved UNDECIDED → ACCEPT for GO:0004896, MODIFY for GO:0019725. Added supporting_text to 17 refs. Now PASS (2w)
- CD28: Resolved GO:0042110 inconsistency (IGI UNDECIDED→ACCEPT). Added supporting_text to ~40 reference findings. Down from 42w to 2w
- IL10: Resolved UNDECIDED → ACCEPT/KEEP_AS_NON_CORE for GO:0140105, GO:0045944, GO:0045893. Now PASS (34w)
- Remaining work: supporting_text coverage improvements (IL2RA 34w, IL10 34w, TNFAIP3 32w highest), STAT3 deep research
