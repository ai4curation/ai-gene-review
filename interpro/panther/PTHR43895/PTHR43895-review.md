# PANTHER Family Review: PTHR43895

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR43895 |
| **Family Name** | CALCIUM/CALMODULIN-DEPENDENT PROTEIN KINASE KINASE-RELATED |
| **InterPro Entry** | (none integrated) |
| **Total Proteins** | 25,910 |
| **Taxonomic Breadth** | 9,166 taxa |
| **Subfamilies** | 84 |
| **Representative Structure** | 8tuc (Unphosphorylated CaMKK2 in complex with CC-8977) |

## Executive Summary

PTHR43895 is a large and taxonomically broad family of **serine/threonine protein kinases** of the CaMKK-related/CAMK-group clade. Its 84 subfamilies span animal Ca2+/calmodulin-dependent protein kinase kinases (CaMKK1/2), the very large plant **CBL-interacting protein kinase (CIPK/SnRK3)** expansion, fungal checkpoint and stress kinases, and assorted "non-specific" Ser/Thr kinase clades. The unifying biochemical activity is **protein serine/threonine kinase activity** (the protein kinase catalytic domain); functional specialization across subfamilies is large and is driven by regulatory modules and pathway context rather than by the catalytic chemistry.

The S. pombe anchor gene, **chk1** (P34208), is the fission-yeast **DNA-damage checkpoint effector kinase**, and is placed in subfamily **PTHR43895:SF32 (SERINE/THREONINE-PROTEIN KINASE CHK1)** by its UniProt PANTHER cross-reference. Because this is a deep, multi-functional CAMK-group family, the safe IBA transfers to chk1 are the catalytic Ser/Thr-kinase MF and the checkpoint/DNA-damage-response BP shared by the CHK1 subfamily; localization terms and any process terms specific to other subfamilies (plant CIPKs, CaMKKs) should not be over-transferred.

## Subfamily Analysis

### PTHR43895:SF32 - SERINE/THREONINE-PROTEIN KINASE CHK1 (ANCHOR SUBFAMILY)
**Members**: 8 proteins (largest single subfamily in the sampled set)

This is the subfamily of the S. pombe anchor gene **chk1 (P34208)**, confirmed by `DR PANTHER; PTHR43895:SF32; SERINE_THREONINE-PROTEIN KINASE CHK1`.

**Key Members**:
- *S. pombe* chk1 (P34208) - anchor; G2/M DNA-damage checkpoint effector kinase
- *S. pombe* ppk1 (Q9HFF4)
- *S. cerevisiae* CHK1 (P38147), FRK1 (Q03002)
- *Mycosarcoma maydis* CHK1 (P0C198)
- *Xenopus laevis* chek1 (Q6DE87)
- *Arabidopsis* CIPK24/SOS2 (Q9LDI3); *Oryza sativa* CIPK24 (Q69Q47)

**Function**: Ser/Thr protein kinase activity; DNA-damage checkpoint signaling (in the fungal/metazoan Chk1 members). Note that this subfamily as sampled is heterogeneous: it co-clusters the fungal/animal Chk1 checkpoint kinases with plant CIPK24/SOS2 kinases, which act in the salt-overly-sensitive (Na+ homeostasis) pathway rather than DNA-damage checkpoints — a caution against transferring DNA-damage process terms to the plant members.

### PTHR43895:SF65 / SF104 / SF91 / SF84 / SF151 ... - CBL-INTERACTING PROTEIN KINASES (CIPK/SnRK3)
**Members**: Many subfamilies, a few members each (e.g. SF65 CIPK21 ×4, SF104 CIPK3 ×4, SF91 CIPK6 ×2, SF84 CIPK15 ×2, SF151 CIPK11 ×2, SF162 CIPK25 ×2, SF145 CIPK9 ×2, SF6 CIPK19 ×2, SF28 CIPK15 ×2)

**Taxonomy**: Plants (large CIPK gene-family expansion).

**Function**: CBL (calcineurin-B-like)-interacting Ser/Thr kinases of the SnRK3 group; signal in calcium/stress, ion homeostasis, and nutrient responses. These plant-specific processes do not transfer to fungal/animal members.

### PTHR43895:SF39 / SF26 - CALCIUM/CALMODULIN-DEPENDENT PROTEIN KINASE KINASE 1/2
**Members**: SF26 (CaMKK1) ×3, SF39 (CaMKK2) ×3

**Function**: Animal CaMKKs; upstream activators of CaMKI/IV and AMPK. These are the namesake clade of the family (and the source of the representative structure 8tuc, human CaMKK2).

### PTHR43895:SF152 - SERINE/THREONINE-PROTEIN KINASE TOS3
**Members**: 2 proteins

**Function**: Budding-yeast TOS3-type upstream AMPK-activating kinase, illustrating the family's CaMKK-like activating-kinase character in fungi.

## IBA Annotation Assessment

Chk1 receives the following IBA (GO_REF:0000033, PANTHER node PTN002389494) annotations. Seeds include PomBase:SPCC1259.13 (chk1 itself) and SGD:S000000478 (budding-yeast CHK1).

| GO ID | Label | Aspect | Flags | Our action | Assessment |
|-------|-------|--------|-------|------------|------------|
| GO:0007095 | mitotic G2 DNA damage checkpoint signaling | BP | NO_UNIPROT_SEEDS | ACCEPT | Correct and core. Chk1 is the experimentally defined effector kinase of the G2/M DNA-damage checkpoint in S. pombe; the BP transfers soundly within the CHK1 subfamily. |
| GO:0005634 | nucleus | CC | LOCALIZATION; NO_UNIPROT_SEEDS | ACCEPT | Correct. Chk1 is a nuclear kinase that forms foci at DSBs; localization term is supported. |
| GO:0035861 | site of double-strand break | CC | LOCALIZATION; NO_UNIPROT_SEEDS | ACCEPT | Correct. Chk1 is recruited (via Crb2) to DSB sites; consistent with the experimental focus-forming behavior. |
| GO:0005737 | cytoplasm | CC | LOCALIZATION; NO_UNIPROT_SEEDS | KEEP_AS_NON_CORE | Reasonable but non-core. Cytoplasmic localization is a generic transfer; the functionally relevant compartment is the nucleus, so this is retained as non-core rather than rejected. |

**CROSS_SUBFAMILY risk**: None of chk1's IBAs are flagged CROSS_SUBFAMILY; they derive from within the CHK1 subfamily (PTN002389494). The expected MF term (GO:0004674, protein Ser/Thr kinase activity) is the family-wide catalytic activity and is fully appropriate for chk1.

**Curatorial note**: This is a deep CAMK-group family in which subfamilies have markedly divergent biology (plant CIPK ion-homeostasis kinases, animal CaMKKs). The DNA-damage-checkpoint process terms above are correct **for chk1 and its CHK1-subfamily orthologs** but must not be propagated outward to CIPK/CaMKK subfamilies. The two localization CC terms (nucleus, site of double-strand break) are the type of transfer that warrants the most scrutiny in general, but here they are independently supported by the experimental S. pombe chk1 biology, so they are accepted.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER family metadata/members, UniProt, the chk1 gene review (genes/SCHPO/chk1), and the PANTHER IBA propagation table.
