# PANTHER Family Review: PTHR24055

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR24055 |
| **Family Name** | MITOGEN-ACTIVATED PROTEIN KINASE |
| **InterPro Entry** | IPR050117 |
| **Total Proteins** | 62,692 |
| **Taxonomic Breadth** | 10,279 taxa |
| **Subfamilies** | 127 |
| **Representative Structure** | 3pze (JNK1 in complex with inhibitor) |
| **Anchor Gene** | S. pombe sty1 / Spc1 / Phh1 (Q09892) |

## Executive Summary

PTHR24055 is the eukaryote-wide **mitogen-activated protein kinase (MAPK)** family — the terminal Ser/Thr kinases of three-tier MAPKKK→MAPKK→MAPK signaling cassettes. All members share the conserved core: **MAP kinase activity** (Pro-directed Ser/Thr phosphotransfer) gated by **dual phosphorylation of the activation-loop TxY motif** by an upstream MAP2K. This family is very large (127 subfamilies) and spans all the canonical MAPK subtypes: the **ERK/MAPK1-3** mitogenic kinases, the **p38/MAPK11-14** and **JNK/MAPK8-10** stress kinases, the fungal **Hog1/Sty1** osmo/stress kinases, the **ERK5/MAPK7** clade, plant MPKs, and the divergent **NLK** kinases.

The deeply conserved chemistry (MAP kinase activity, ATP binding, TxY-dependent activation, MAPK-cascade participation) is shared family-wide; **neofunctionalization** is at the level of which upstream cascade and which downstream transcription factors/effectors a given subtype serves (mitogenic growth vs. stress/osmotic responses). The fission-yeast anchor **sty1** is the **Hog1/p38-type stress-activated MAPK (SAPK)**, the central effector of the core environmental stress response.

## Subfamily Analysis

The retrieved member table (246 proteins) does not carry per-row PANTHER subfamily IDs, so the groupings below summarize the protein-name distribution of real members in the table (counts are of the sampled members, not the full 127-subfamily family). PANTHER reports 127 subfamilies overall.

### Hog1/Sty1 stress-MAPK clade  *(ANCHOR CLADE)*
**Sampled members**: "Mitogen-activated protein kinase HOG1" (36 + 10 lowercase = ~46 sampled members), plus fungal stress MAPKs spm1, mpkC, etc.

**Key Members**:
- **S. pombe sty1 / Spc1 / Phh1 (Q09892)** — the anchor (Hog1/p38 ortholog)
- Fungal HOG1 orthologs across Ascomycota (e.g., *Ustilaginoidea virens*, *Aureobasidium melanogenum*)
- *Aspergillus* mpkC, *Cytospora* spm1

**Function**: Stress-activated MAPK (SAPK). Activated by hyperosmotic, oxidative, heat, and other stresses; drives the core environmental stress response (in S. pombe via the bZIP factor Atf1). This is the anchor gene's clade.

### ERK / MAPK1-3 mitogenic clade
**Sampled members**: "Mitogen-activated protein kinase 1/3" and related numbered MAPKs.

**Function**: Growth-factor / mitogenic ERK signaling (cell proliferation and differentiation).

### p38 (MAPK11-14) and JNK (MAPK8-10) stress clades
**Sampled members**: "Mitogen-activated protein kinase 8/9/12/13/14" etc.

**Function**: Metazoan stress- and cytokine-activated MAPKs; the animal counterparts of the fungal Hog1/Sty1 stress response (the representative structure 3pze is JNK1).

### ERK5 / plant MPK / NLK and other clades
**Sampled members**: "Mitogen-activated protein kinase 4/6/7/15", "Serine/threonine-protein kinase NLK", plant SIPK.

**Function**: ERK5 (MAPK7), plant MPK cascades, and the divergent NLK kinases — additional MAPK subtypes with specialized upstream/downstream wiring.

## IBA Annotation Assessment

IBAs (GO_REF:0000033) propagated to sty1, with the PANTHER seed node and our recorded action:

| GO ID | GO label | Aspect | Node | Our action | Assessment |
|-------|----------|--------|------|------------|------------|
| GO:0051403 | stress-activated MAPK cascade | BP | PTN001172058 | ACCEPT | **CORRECT.** This is precisely sty1's core role as a SAPK; node is shared with fungal Hog1 stress kinases. |
| GO:0034599 | cellular response to oxidative stress | BP | PTN001172058 | ACCEPT | **CORRECT.** Sty1 is activated by H2O2/menadione and drives the oxidative-stress transcriptional response (experimentally established). |
| GO:0007231 | osmosensory signaling pathway | BP | PTN001172058 | ACCEPT | **CORRECT.** Sty1/Spc1 is the osmostress MAPK (Hog1 ortholog); hyperosmotic activation is a defining property. |

**Triage flags.** All three IBAs carry the `GENE_NO_SUBFAMILY` flag: sty1's UniProt DR line lists only the family (`PTHR24055`) with no fine subfamily call, so propagation occurs at a high node (PTN001172058). Per calibration this is **triage, not a verdict**. Two considerations make these transfers safe:

1. **The seed node is the stress-MAPK (Hog1/p38/JNK) sub-clade, not the whole family.** All three terms are stress-response BPs that belong specifically to the SAPK branch that sty1 sits in — they are *not* mitogenic-ERK functions being mis-transferred. This is the key positive argument: the propagated processes match sty1's known clade and biology rather than crossing into the ERK growth-signaling clade.
2. **No localization (CC) or molecular-function terms with clade-specific risk are propagated by IBA here**, so there is no danger of transferring, e.g., a metazoan-specific nuclear-effector localization onto the fission-yeast kinase.

**No REMOVE or MODIFY warranted.** All three propagated stress-MAPK process terms are consistent with sty1's experimentally characterized role as the core stress-activated MAPK. Because PTHR24055 is enormous (127 subfamilies spanning all MAPK subtypes), SF-level granularity matters; here the propagation is appropriately confined to the stress-MAPK node and is biologically correct.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata, family entry table, S. pombe sty1 UniProt/GOA/AI-review, iba_propagation.tsv
