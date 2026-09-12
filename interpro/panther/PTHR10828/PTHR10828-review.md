# PANTHER Family Review: PTHR10828

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR10828 |
| **Family Name** | M-phase inducer phosphatase (MPI_phosphatase) |
| **InterPro Entry** | (none integrated in metadata) |
| **Total Proteins** | 10,135 |
| **Taxonomic Breadth** | 8,904 taxa |
| **Subfamilies** | 11 |
| **Representative Structure** | 2a2k (Crystal structure of active-site mutant C473S of Cdc25B phosphatase catalytic domain) |
| **S. pombe anchor gene** | cdc25 (P06652) |

## Executive Summary

PTHR10828 is the **M-phase inducer phosphatase (Cdc25)** family, plus a related clade of small **rhodanese-fold** enzymes. The defining members are **dual-specificity / protein-tyrosine phosphatases** that trigger mitotic (and meiotic) entry by **dephosphorylating the inhibitory Tyr15 (and Thr14) of CDK1 (Cdc2)**, thereby activating the cyclin B-CDK1 complex. They are the positive counterpart of the inhibitory Wee1/Myt1 kinases and act as dosage-dependent mitotic inducers that couple cell size and checkpoint status to the timing of division. Catalysis uses a **rhodanese-fold catalytic domain** with an essential active-site cysteine that forms a phosphocysteine intermediate.

The family also contains a divergent set of **arsenate reductase / arsenical-resistance proteins** (e.g. yeast ACR2/ARR2-type) that share the rhodanese fold and active-site cysteine chemistry but act on arsenate rather than phosphoproteins — a clear case of **catalytic-scaffold reuse / neofunctionalization** within one PANTHER family. Among the bona fide Cdc25 phosphatases, divergence is by **isozyme specialization** (the metazoan CDC25A/B/C trio) rather than by change of core reaction. The G2/M-induction function is well conserved from yeast Cdc25/Mih1 to human CDC25A/B/C, so the core cell-cycle annotations propagate cleanly among the Cdc25 subfamilies; the genuine risk is propagating Cdc25 cell-cycle terms onto the arsenate-reductase clade (or vice versa).

## Subfamily Analysis

### PTHR10828:SF17 — PROTEIN-TYROSINE-PHOSPHATASE (the anchor's subfamily)
**Members:** ~4 proteins

**Representative members (real, from the CSV):**
- *S. pombe* cdc25 (P06652) — the anchor
- *S. cerevisiae* MIH1 (P23748)
- *Emericella (Aspergillus) nidulans* nimT (P30303)
- *Dictyostelium discoideum* cdc25 (Q54QM6)

**Function:** Fungal/protist single Cdc25-type M-phase inducer phosphatase — the CDK1-Tyr15 phosphatase that triggers the G2/M transition. This subfamily holds the non-metazoan Cdc25 orthologs.

**Anchor placement:** The cdc25 UniProt record assigns it to **PTHR10828:SF17** (`PROTEIN-TYROSINE-PHOSPHATASE`), grouping it with budding-yeast Mih1, *Aspergillus* NimT and *Dictyostelium* Cdc25 — the correct (non-metazoan) Cdc25 ortholog group.

### PTHR10828:SF64 — M-PHASE INDUCER PHOSPHATASE 3 (CDC25C)
**Members:** ~9 proteins (largest subfamily)

**Representative members:** Human CDC25C (P30307), mouse Cdc25c (P48967).

**Function:** Metazoan CDC25C, the mitotic-entry Cdc25 isozyme; checkpoint-regulated nuclear/cytoplasmic shuttling protein.

### PTHR10828:SF46 — M-PHASE INDUCER PHOSPHATASE 1 (CDC25A)
**Members:** ~4 proteins

**Representative members:** Human CDC25A (P30304), mouse Cdc25a (P48964).

**Function:** Metazoan CDC25A, acting at both G1/S and G2/M.

### PTHR10828:SF48 / SF76 / SF43 — additional MPI phosphatase clades
**Representative members:** human CDC25B (SF48) and other M-phase inducer phosphatase isozymes; *C. elegans* CDC-25.1 (SF43).

**Function:** Further metazoan/invertebrate Cdc25 isozyme clades, all retaining CDK-Tyr15 phosphatase activity.

### PTHR10828:SF38 / SF67 — ARSENICAL-RESISTANCE / ARSENATE REDUCTASE clade
**Members:** ~5 proteins (SF38)

**Representative members:** *S. cerevisiae* YCH1 (P42937), ARR2/ACR2 (Q06597), *Oryza sativa* ACR2.2 (Q10SX6).

**Function:** Rhodanese-fold arsenate reductases / arsenical-resistance proteins — same fold and catalytic cysteine but a different substrate (arsenate), representing neofunctionalization away from the cell-cycle phosphatase role.

## Functional Diversity Assessment

- **Conserved core (Cdc25 subfamilies):** protein-tyrosine/dual-specificity phosphatase activity, CDK1-Tyr15 dephosphorylation, positive regulation of the G2/M transition.
- **Neofunctionalization:** PRESENT — the arsenate-reductase / arsenical-resistance clade (SF38/SF67) reuses the rhodanese fold for arsenic detoxification, not cell-cycle control. Cell-cycle GO terms must NOT be propagated onto this clade.
- **Subfunctionalization (within Cdc25):** metazoan CDC25A/B/C isozyme specialization (G1/S vs G2/M, distinct checkpoint regulation).

## IBA Annotation Assessment

The following IBA (GO_REF:0000033) annotations are propagated to **cdc25** (P06652). Node and seed data from `cdc25-goa.tsv` and `iba_propagation.tsv`.

| GO ID | Label | Aspect | PANTHER node | Our action | Flags | Verdict |
|-------|-------|--------|--------------|-----------|-------|---------|
| GO:0000086 | G2/M transition of mitotic cell cycle | BP | PTN000089071 | ACCEPT | (none) | **Appropriate** |
| GO:0010971 | positive regulation of G2/M transition of mitotic cell cycle | BP | PTN000089071 | ACCEPT | CROSS_SUBFAMILY | **Appropriate** |
| GO:0005634 | nucleus | CC | PTN000850864 | ACCEPT | CROSS_SUBFAMILY;LOCALIZATION | **Appropriate** |
| GO:0005737 | cytoplasm | CC | PTN000850864 | ACCEPT | LOCALIZATION;NO_UNIPROT_SEEDS | **Appropriate** |
| GO:0110032 | positive regulation of G2/MI transition of meiotic cell cycle | BP | PTN000089071 | KEEP_AS_NON_CORE | NO_UNIPROT_SEEDS | **Appropriate (non-core)** |

**GO:0000086 / GO:0010971 (G2/M transition; positive regulation).** These are the defining biological roles of Cdc25. Seeds at PTN000089071 include human CDC25A (P30304), CDC25C (P30307) and *Drosophila* string (FBgn0003525) — true M-phase inducers spread across the CDC25A/B/C metazoan subfamilies. The CROSS_SUBFAMILY flag on GO:0010971 reflects transfer between Cdc25 isozyme subfamilies (SF46/SF48), all of which share the mitosis-inducing function; this is a correct propagation, supported by cdc25's experimentally established role as the rate-limiting G2/M trigger. **Appropriate — core.**

**GO:0005634 (nucleus) / GO:0005737 (cytoplasm).** Both flagged LOCALIZATION (and GO:0005634 CROSS_SUBFAMILY from SF64/CDC25C). These are consistent with cdc25's documented nucleocytoplasmic shuttling, with nuclear accumulation peaking in G2 and 14-3-3-mediated nuclear exclusion under checkpoint control. The localization matches known cdc25 biology rather than contradicting it, so the cross-subfamily/no-seed flags do not indicate error. **Appropriate.**

**GO:0110032 (positive regulation of G2/MI transition of meiotic cell cycle).** NO_UNIPROT_SEEDS (PomBase-only support). cdc25's Tyr15-dephosphorylating activity is indeed required for meiotic nuclear divisions, but this is a context-specific extension rather than the gene's core mitotic role, hence retained as **KEEP_AS_NON_CORE**. Appropriate.

**Verdict:** All cdc25 IBAs are well-supported by the family tree and match its curated biology. The CROSS_SUBFAMILY flags arise from propagation among the equivalent metazoan/fungal Cdc25 isozyme subfamilies and are correct. Critically, none of cdc25's IBAs derive from the arsenate-reductase (SF38/SF67) clade — the one place where over-propagation would be a real hazard — so there is no neofunctionalization leakage. No over-propagations detected.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/member table, UniProt (P06652), cdc25 GOA IBA rows, iba_propagation.tsv, cdc25-ai-review.yaml
