# PANTHER Family Review: PTHR10763

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR10763 |
| **Family Name** | Origin Recognition Complex 1/Cell Division Control Protein 6 (ORC1/CDC6) |
| **InterPro Entry** | IPR050311 (integrated) |
| **Total Proteins** | 14,107 |
| **Taxonomic Breadth** | 10,679 taxa |
| **Subfamilies** | 4 |
| **Representative Structure** | 1fnn (Crystal structure of Cdc6p from *Pyrobaculum aerophilum*) |
| **S. pombe anchor gene** | cdc18 (P41411) |

## Executive Summary

PTHR10763 is the **ORC1/CDC6** family of **AAA+ ATPases** that initiate eukaryotic (and archaeal) DNA replication. Its members bind replication origins and, in an ATP-dependent manner, drive assembly of the **pre-replicative complex (pre-RC)**, the licensing step that loads the MCM2-7 replicative helicase onto origins exactly once per cell cycle. The family comprises two closely related paralog groups that arose from a shared archaeal Orc1/Cdc6 ancestor: **Cdc6/Cdc18** (the loader that cooperates with Cdt1 to load MCM2-7) and **ORC1** (the largest, ATPase-active subunit of the six-subunit origin recognition complex).

Functional divergence within the family is **moderate**: all members retain the AAA+ ATPase core and origin-association activity, but Cdc6-type and Orc1-type proteins have specialized into the loader vs. origin-recognition roles, and some Orc1-related members (e.g. yeast SIR3) have been recruited to chromatin silencing. The deep conservation of the licensing function means the core DNA-replication-initiation annotations propagate reliably across the family, including between the Cdc6 and Orc1 subfamilies, which is biologically expected given their shared ancestry and overlapping origin-binding activity.

## Subfamily Analysis

### PTHR10763:SF26 — CELL DIVISION CONTROL PROTEIN 6 HOMOLOG (the anchor's subfamily)
**Members:** ~27 proteins

**Representative members (real, from the CSV):**
- *S. pombe* cdc18 (P41411) — the anchor
- Human CDC6 (Q99741)
- Mouse Cdc6 (O89033)
- *S. cerevisiae* CDC6 (P09119)

**Function:** Eukaryotic Cdc6/Cdc18 — the rate-limiting pre-RC loading factor that recruits Cdt1 and MCM2-7 to ORC-bound origins; also contributes to replication-checkpoint signaling.

**Anchor placement:** The cdc18 UniProt record assigns it to **PTHR10763:SF26** (`CELL DIVISION CONTROL PROTEIN 6 HOMOLOG`), grouping it with the human/mouse/budding-yeast Cdc6 orthologs. This is the correct ortholog group: cdc18 is the fission-yeast Cdc6.

### PTHR10763:SF22 — ORC1-TYPE DNA REPLICATION PROTEIN
**Members:** ~34 proteins (largest subfamily)

**Representative members:** archaeal Orc1/Cdc6 proteins, e.g. *Archaeoglobus fulgidus* cdc6-1 (O29995), *Halobacterium salinarum* orc9-2 (O51974), *Thermococcus onnurineus* cdc6 (B6YUE9).

**Function:** Archaeal Orc1/Cdc6 proteins — the single-protein ancestral form combining origin recognition and helicase-loading roles. This is the most populous subfamily and reflects the archaeal radiation.

### PTHR10763:SF23 — ORIGIN RECOGNITION COMPLEX SUBUNIT 1
**Members:** ~17 proteins

**Representative members:** Human ORC1 (Q13415), *S. cerevisiae* ORC1 (P54784), *S. pombe* orc1 (P54789), *S. cerevisiae* SIR3 (P06701).

**Function:** Eukaryotic ORC1, the large ATPase subunit of the origin recognition complex that nucleates pre-RC assembly. SIR3 is a divergent member recruited to transcriptional silencing.

### PTHR10763:SF31 — ORC1-TYPE DNA REPLICATION PROTEIN 2
**Members:** ~4 proteins

**Function:** A small Orc1-related clade; same AAA+/origin-association architecture.

## Functional Diversity Assessment

- **Conserved core:** AAA+ ATPase, ATP-dependent origin/DNA binding, role in DNA replication initiation / pre-RC assembly.
- **Subfunctionalization:** MODERATE — Cdc6-type (loader) vs. Orc1-type (origin-recognition) division of labor; SIR3-type recruitment to silencing is the clearest neofunctionalization.

## IBA Annotation Assessment

The following IBA (GO_REF:0000033) annotations are propagated to **cdc18** (P41411). Node and seed data from `cdc18-goa.tsv` and `iba_propagation.tsv`.

| GO ID | Label | Aspect | PANTHER node | Our action | Flags | Verdict |
|-------|-------|--------|--------------|-----------|-------|---------|
| GO:0005634 | nucleus | CC | PTN000080129 | ACCEPT | LOCALIZATION | **Appropriate** |
| GO:0006270 | DNA replication initiation | BP | PTN000080056 | ACCEPT | CROSS_SUBFAMILY | **Appropriate** |
| GO:0003688 | DNA replication origin binding | MF | PTN000080056 | ACCEPT | CROSS_SUBFAMILY | **Appropriate** |
| GO:0033314 | mitotic DNA replication checkpoint signaling | BP | PTN000080056 | ACCEPT | NO_UNIPROT_SEEDS | **Appropriate** |

**GO:0005634 (nucleus).** Flagged LOCALIZATION but same-subfamily (seeds within SF26, e.g. human CDC6 Q99741, plus PomBase SPBC14C8.07c and SGD CDC6). Cdc6/Cdc18 is a nuclear, chromatin-associated pre-RC component; the localization is consistent with cdc18's known biology. **Appropriate.**

**GO:0006270 (DNA replication initiation) and GO:0003688 (DNA replication origin binding).** Both flagged CROSS_SUBFAMILY because seeds also fall in **SF23 (ORC1)** (e.g. human ORC1 Q13415, SGD ORC1). Per the calibrated rules, this is exactly the case where cross-subfamily propagation is *correct*: origin binding and replication initiation are the deep, shared functions of the entire ORC1/CDC6 family, and Cdc6/Cdc18 genuinely binds ORC-bound origins and is the rate-limiting initiator of S phase. There is a positive biological argument FOR the transfer, not against it. **Appropriate.**

**GO:0033314 (mitotic DNA replication checkpoint signaling).** Flagged NO_UNIPROT_SEEDS, but the with/from field includes PomBase nodes (SPBC14C8.07c, SPBC29A10.15) and the propagation is supported by cdc18's documented role anchoring the Rad3-Rad26 (ATR-ATRIP) checkpoint on chromatin at stalled forks. Consistent with the curated cdc18 review. **Appropriate.**

**Verdict:** All four cdc18 IBAs are well-supported by the family tree. The two CROSS_SUBFAMILY flags (origin binding, replication initiation) are correct propagations of a deeply conserved ORC1/CDC6 function, not over-annotations. No localization or paralog-specific over-propagation detected.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/member table, UniProt (P41411), cdc18 GOA IBA rows, iba_propagation.tsv, cdc18-ai-review.yaml
