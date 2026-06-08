# PANTHER Family Review: PTHR40621

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR40621 |
| **Family Name** | bZIP YAP Transcription Factors (bZIP_YAP_TF) |
| **InterPro Entry** | IPR050936 |
| **Total Proteins** | 11,010 |
| **Taxonomic Breadth** | 3,258 taxa |
| **Subfamilies** | 6 |
| **Representative Structure** | 1gd2 (Crystal structure of bZIP transcription factor Pap1 bound to DNA) |

## Executive Summary

PTHR40621 is a fungal-centric family of **basic-leucine-zipper (bZIP) transcription factors of the Yap1/AP-1 (YAP) type**. Its members are sequence-specific RNA polymerase II transcriptional activators that bind AP-1/TRE-like core elements and govern the **oxidative-stress / redox-homeostasis response** and **multidrug/xenobiotic resistance**. The defining regulatory feature of the canonical Yap1/Pap1 members is redox control of nucleocytoplasmic shuttling: oxidation of cysteine-rich domains (via a thioredoxin-peroxidase relay) masks a Crm1-dependent nuclear export signal, driving nuclear accumulation and induction of antioxidant and drug-efflux genes.

The S. pombe anchor gene, **pap1** (Q01663), is the founding structurally characterized member (PDB 1gd2) and sits in subfamily **PTHR40621:SF6 (AP-1-LIKE TRANSCRIPTION FACTOR YAP1-RELATED)**, alongside S. cerevisiae Yap1 and Candida Cap1. The family also contains the budding-yeast YAP paralog expansion (Yap1–Yap7, Cad1/Yap2, Cin5/Yap4, Arr1/Yap8), which have subfunctionalized toward distinct stress and metal-regulatory roles (e.g. Yap5/Yap7 in iron regulation, Arr1/Yap8 in arsenic resistance). Despite this paralog diversification, the shared molecular function across the family is sequence-specific dbTF activity, so the core MF/BP transcription terms transfer well; the principal caveats concern paralog-specific *target-gene* / *stress-specific* biological processes rather than the molecular function itself.

## Subfamily Analysis

### PTHR40621:SF6 - AP-1-LIKE TRANSCRIPTION FACTOR YAP1-RELATED (ANCHOR SUBFAMILY)
**Members**: 16 proteins (largest subfamily)

This is the subfamily containing the S. pombe anchor gene **pap1 (Q01663)**, confirmed by its UniProt cross-reference `DR PANTHER; PTHR40621:SF6`.

**Key Members**:
- *S. pombe* pap1 (Q01663) - anchor; redox-regulated oxidative-stress / MDR activator
- *S. cerevisiae* YAP1 (P19880), CAD1/YAP2 (P24813), CIN5/YAP4 (P40917), YAP5 (P40574), YAP6 (Q03935), YAP7 (Q08182), ARR1/YAP8 (Q06596)
- *K. lactis* YAP1 (P56095)
- *Candida albicans* CAP1 (Q5AJU7); *Candida glabrata* AP1 (Q6FRZ8)
- *Aspergillus* spp. yap1 (B8NNN3, Q2UMT9, Q4WMH0); *A. nidulans* napA (Q5AW17)
- *Cryptococcus neoformans* yap1 (J9VEC2)

**Function**: Sequence-specific AP-1/TRE-like dbTF activity; redox-regulated activator of antioxidant and drug-efflux genes. Note that this subfamily aggregates the budding-yeast YAP paralog set, which has diverged toward distinct stress/metal-regulatory programs (Yap5/Yap7 iron, Arr1/Yap8 arsenic).

### PTHR40621:SF11 - TRANSCRIPTION FACTOR KAPC-RELATED
**Members**: 7 proteins

**Taxonomy**: Aspergillus / Eurotiomycete filamentous fungi.

**Key Members**: *A. clavatus* kapC (A1C9M5), *Neosartorya fischeri* kapC (A1D9Z7), *A. niger* kapC (A2R346).

**Function**: bZIP transcription factors; this clade lends the family its overall PANTHER name component. Functional details are less characterized than the Yap1/Pap1 clade.

### PTHR40621:SF8 - AP-1-LIKE TRANSCRIPTION FACTOR YAP3
**Members**: 2 proteins

**Function**: A YAP3-type AP-1-like clade; bZIP transcription factor.

### PTHR40621:SF7 - BZIP DOMAIN-CONTAINING PROTEIN (includes hapX-like members)
**Members**: 2 proteins

**Key Members**: *Arthroderma benhamiae* hapX (D4AQY2). HapX-type bZIP factors are iron-responsive regulators in fungi, illustrating subfunctionalization within the broader family toward metal/iron homeostasis.

## IBA Annotation Assessment

Pap1 receives the following IBA (GO_REF:0000033, PANTHER node PTN008082960) annotations. All three were **ACCEPTed** in the pap1 review.

| GO ID | Label | Aspect | Flags | Our action | Assessment |
|-------|-------|--------|-------|------------|------------|
| GO:0000976 | transcription cis-regulatory region binding | MF | NO_UNIPROT_SEEDS | ACCEPT | Correct. Pap1 binds AP-1/TRE-like cis-regulatory elements (TTACGTAA) experimentally. A more specific term (GO:0000978) better captures the activity, but the IBA is not wrong. |
| GO:0001228 | DNA-binding transcription activator activity, RNA polymerase II-specific | MF | NO_UNIPROT_SEEDS | ACCEPT | Correct and core. Pap1 is a sequence-specific Pol II transcriptional activator; this is the defining molecular function of the YAP subfamily and transfers soundly across SF6. |
| GO:0090575 | RNA polymerase II transcription regulator complex | CC | LOCALIZATION; NO_UNIPROT_SEEDS | ACCEPT | Acceptable. As an activator, Pap1 acts within the Pol II transcription regulator machinery; this is a localization-type term but is biologically consistent with the well-supported MF. |

**CROSS_SUBFAMILY risk**: None of pap1's IBAs are flagged CROSS_SUBFAMILY; they propagate within the YAP/AP-1 dbTF clade. The `NO_UNIPROT_SEEDS` flag reflects that the supporting seeds are PomBase/SGD/CGD entries (e.g. PomBase:SPAC1783.07c, SGD:S000006403/S000002831, CGD:CAL0000188360) rather than UniProt accessions; the seed orthologs are themselves YAP-family transcription factors, so the transfer is appropriate.

**Paralog caveat (curatorial note)**: The general dbTF / cis-regulatory-binding terms transfer well across the family because all members are AP-1-type transcription factors. What does **not** transfer cleanly are *paralog-specific biological processes* and *specific target/stress programs* — e.g. iron regulation (Yap5/Yap7), arsenic resistance (Arr1/Yap8), or pap1's particular oxidative-stress and multidrug-resistance regulons. IBA propagation of such process-specific or stress-specific terms across SF6 should be scrutinized, but the molecular-function and generic transcription terms reviewed above are correct for pap1.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER family metadata/members, UniProt, the pap1 gene review (genes/SCHPO/pap1), and the PANTHER IBA propagation table.
