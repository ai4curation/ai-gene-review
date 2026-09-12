# PANTHER Family Review: PTHR24056

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR24056 |
| **Family Name** | Cyclin-dependent kinase (CDK) |
| **InterPro Entry** | IPR050108 |
| **Total Proteins** | 80,839 |
| **Taxonomic Breadth** | 11,482 taxa |
| **Subfamilies** | 155 |
| **Representative Structure** | 6oqo (CDK6 in complex with an inhibitor) |
| **Anchor Gene** | S. pombe cdc2 / Cdk1 (P04551) |

## Executive Summary

PTHR24056 is the eukaryote-wide **cyclin-dependent kinase (CDK)** family — Ser/Thr protein kinases that are catalytically inert as monomers and become active only upon binding a **cyclin** (often with a Cks/Suc1 subunit), forming the cyclin-CDK holoenzyme. The deeply conserved core is **cyclin-dependent protein serine/threonine kinase activity** directed at Ser/Thr-Pro motifs, gated by activation-loop (T-loop) phosphorylation by CAK and by inhibitory Tyr15/Thr14 phosphorylation.

This is one of the largest PANTHER families (155 subfamilies) and is strongly **neofunctionalized** across two broad CDK classes: **cell-cycle CDKs** (CDK1/CDK2/CDK4/CDK6 and orthologs) that drive cell-cycle transitions, and **transcriptional CDKs** (CDK7/CDK8/CDK9/CDK12/CDK13) that phosphorylate the RNA Pol II C-terminal domain. Additional clades include CDK5 (neuronal), CDK11, CDK14/CDK20, and plant CDKA/CDKB. The fission-yeast anchor **cdc2** is the founding CDK1 — the single master cell-cycle kinase driving both G1/S and G2/M (and the meiotic divisions) in fission yeast.

## Subfamily Analysis

Based on the family entry table (281 members with PANTHER subfamily IDs); the largest sampled subfamilies are listed.

### PTHR24056:SF495 — CYCLIN-DEPENDENT KINASE 8-RELATED
**Members**: 31 (largest sampled). Transcriptional CDK8 / Mediator-kinase-module clade.

### PTHR24056:SF46 — CYCLIN-DEPENDENT KINASE 5
**Members**: 29. CDK5 (post-mitotic / neuronal, cyclin-independent activation by p35/p39).

### PTHR24056:SF233 — CYCLIN-DEPENDENT KINASE 9
**Members**: 22. Transcriptional elongation CDK9 (P-TEFb; Pol II CTD Ser2).

### PTHR24056:SF334 — CYCLIN-DEPENDENT KINASE 1
**Members**: 17. The CDK1 clade containing **human CDK1 (P06493)**, mouse Cdk1 (P11440), and other metazoan CDK1 orthologs — the direct functional counterparts of fission-yeast cdc2.

### PTHR24056:SF254 — CYCLIN-DEPENDENT KINASE 2  *(ANCHOR SUBFAMILY)*
**Members**: 16

**Key Members**:
- **S. pombe cdc2 / Cdk1 (P04551)** — the anchor
- S. cerevisiae CDC28 (P00546), Candida CDC28 (P43063)
- *Aspergillus* nimX (Q00646), *Ajellomyces* CDC2 (P54119)
- C. elegans cdk-2 (O61847), Drosophila Cdk2 (P23573)
- Xenopus cdk2 (P23437), plant CDKB1 (Arabidopsis Q2V419, rice Q8L4P8)

**Function**: Cyclin-dependent cell-cycle kinase. **Note (subfamily naming):** PANTHER places the founding fission-yeast Cdk1 (cdc2) and budding-yeast CDC28 in SF254, labeled "CYCLIN-DEPENDENT KINASE 2," while metazoan CDK1 sits in a separate subfamily (SF334). This reflects the fact that the single yeast cell-cycle CDK (cdc2/CDC28) is the common ancestor of the metazoan CDK1/CDK2 pair; the SF254 label is a metazoan-centric name, and **cdc2 is functionally the CDK1 (master mitotic) kinase** of fission yeast despite the subfamily name. This is the anchor gene's subfamily.

### Other notable subfamilies
SF0 (CDK7, 13), SF548 (plant CDKA-1, 11), SF107 (CDK11A-related, 11), SF546 (CDK12, 9), SF171 (CDK20, 9), SF154 (CDK14, 8), SF129 (CDK4, 7) — spanning transcriptional, neuronal, and additional cell-cycle CDK clades.

## IBA Annotation Assessment

IBAs (GO_REF:0000033) propagated to cdc2, with the PANTHER seed node and our recorded action:

| GO ID | GO label | Aspect | Node | Our action | Assessment |
|-------|----------|--------|------|------------|------------|
| GO:0004693 | cyclin-dependent protein serine/threonine kinase activity | MF | PTN000623980 | ACCEPT | **CORRECT.** The defining, deeply conserved molecular function of the entire CDK family and of cdc2 specifically. |
| GO:0000307 | cyclin-dependent protein kinase holoenzyme complex | CC | PTN000623980 | ACCEPT | **CORRECT (localization flag).** cdc2 functions only as the catalytic subunit of the cyclin-CDK (MPF) holoenzyme; the CC matches its experimentally established biology. |
| GO:0000086 | G2/M transition of mitotic cell cycle | BP | PTN000623979 | ACCEPT | **CORRECT.** cdc2 is the rate-limiting G2/M (mitotic-entry) kinase — the canonical CDK1 function. |

**Triage flags.** GO:0000307 and GO:0004693 carry `CROSS_SUBFAMILY` (other_sf seeds include PTHR24056:SF129/SF130/SF462/SF521, i.e., CDK4 and other CDK subfamilies); GO:0000307 also carries `LOCALIZATION`. Per calibration these are **triage, not verdicts**, and here they are expected and benign:

1. **Cyclin-binding holoenzyme formation and CDK catalytic activity are pan-family conserved functions.** Every cell-cycle CDK across SF129/SF130/SF254/SF334/SF462/SF521 forms a cyclin-dependent holoenzyme and phosphorylates Ser/Thr-Pro substrates. Transfer of GO:0004693 and GO:0000307 from a node spanning multiple CDK subfamilies is therefore biologically correct, not a paralog error — these are exactly the conserved CDK core, the kind of cross-subfamily transfer the calibration flags as normally correct (analogous to "cyclin-dependent protein kinase holoenzyme complex / kinase activity" being expected-correct for cdc2).
2. **The LOCALIZATION flag on GO:0000307 is not a conflict.** "Holoenzyme complex" is a functional assembly, not a sub-cellular compartment, and cdc2's obligate cyclin association is well established. There is no transfer of a clade-specific compartment that would contradict cdc2's known nuclear/SPB/spindle localization.
3. PTHR24056 is enormous (155 subfamilies covering cell-cycle AND transcriptional CDKs), so SF-crossing is expected. Crucially, **none of the three propagated terms is a transcriptional-CDK-specific function** (e.g., RNA Pol II CTD phosphorylation / Pol II elongation) being mis-transferred onto the cell-cycle kinase cdc2 — the propagated set is confined to the cell-cycle CDK core.

**No REMOVE or MODIFY warranted.** All three IBAs are consistent with cdc2's experimentally established role as the founding cell-cycle CDK. We defer to curators; the cross-subfamily flags reflect the breadth of the CDK family, not annotation error.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata, family entry table, S. pombe cdc2 UniProt/GOA/AI-review, iba_propagation.tsv
