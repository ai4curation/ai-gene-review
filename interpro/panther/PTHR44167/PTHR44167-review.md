# PANTHER Family Review: PTHR44167

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR44167 |
| **Family Name** | Serine/Threonine Protein Kinase (Ser_Thr_protein_kinase); UniProt name "OVARIAN-SPECIFIC SERINE/THREONINE-PROTEIN KINASE LOK-RELATED" |
| **InterPro Entry** | (none integrated) |
| **Total Proteins** | 22,734 |
| **Taxonomic Breadth** | 13,062 taxa |
| **Subfamilies** | 13 |
| **Representative Structure** | 6ya7 (Cdc7-Dbf4 bound to an Mcm2-S40 derived bivalent substrate) |

## Executive Summary

PTHR44167 is a broad family of **serine/threonine protein kinases** whose major characterized clades are the **CHK2/Rad53/Cds1 DNA-damage and replication checkpoint kinases** and the **CDC7/DDK (Dbf4-dependent kinase) replication-initiation kinases**. The unifying activity is **protein serine/threonine kinase activity**; the family's defining biology centers on cell-cycle and genome-integrity control. The representative structure (6ya7) is a Cdc7-Dbf4 (DDK) complex, reflecting one of the two principal clades.

The S. pombe anchor gene, **cds1** (Q09170), is the fission-yeast **DNA-replication (intra-S) checkpoint effector kinase** and ortholog of human CHEK2, and is placed in subfamily **PTHR44167:SF24 (SERINE/THREONINE-PROTEIN KINASE CHK2)** by its UniProt PANTHER cross-reference. The CHK2 subfamily (SF24) is clearly distinct from the CDC7 subfamily (SF23) within the same PANTHER family — an important distinction, because Cds1 (CHK2-type checkpoint effector) and Hsk1 (CDC7-type DDK) have entirely different functions despite sharing the family. For cds1, the catalytic Ser/Thr-kinase MF and the checkpoint/DNA-damage BP transfer well within SF24; localization terms warrant the usual scrutiny.

## Subfamily Analysis

### PTHR44167:SF24 - SERINE/THREONINE-PROTEIN KINASE CHK2 (ANCHOR SUBFAMILY)
**Members**: 17 proteins (largest subfamily)

This is the subfamily of the S. pombe anchor gene **cds1 (Q09170)**, confirmed by `DR PANTHER; PTHR44167:SF24; SERINE_THREONINE-PROTEIN KINASE CHK2`.

**Key Members**:
- *S. pombe* cds1 (Q09170) - anchor; DNA-replication (S/M) checkpoint effector kinase
- *Homo sapiens* CHEK2 (O96017); *Mus musculus* Chek2 (Q9Z265)
- *Drosophila* lok/Chk2 (O61267)
- *S. cerevisiae* CAK1 (P43568), VHS1 (Q03785)
- *Candida glabrata* PTK2 (Q6FRE7)
- *Dictyostelium* fhkA (Q54BF0) and additional kinases (Q54R95, Q54R98, Q54SK3, Q55F27)
- Several herpesviral kinases (e.g. GaHV-2 US1206 Q05101, MDV092 Q9E6L8; PsHV-1 US3 Q6UDG0, UL13 Q6UDH7)
- *Sulfolobus acidocaldarius* arnS (Q4J9K4)

**Function**: Ser/Thr protein kinase activity; DNA-damage / replication checkpoint signaling for the CHK2/Cds1/Rad53 members. The subfamily also aggregates more divergent kinases (yeast CAK1, viral kinases, an archaeal kinase), so checkpoint-process terms are appropriate for the eukaryotic CHK2/Cds1 members but should not be assumed for the viral/archaeal outliers.

### PTHR44167:SF23 - CDC7 KINASE / DDK
**Members**: 8 proteins

**Key Members**: *Homo sapiens* CDC7 (O00311); *Mus musculus* Cdc7 (Q9Z0H0); *S. cerevisiae* CDC7 (P06243); *S. pombe* hsk1 (P50582) and spo4 (Q9UQY9); *Drosophila* Cdc7 (Q9W3Y1).

**Function**: Dbf4-dependent kinase (DDK) that phosphorylates MCM helicase subunits to license/activate DNA replication origins. This is the source of the representative structure 6ya7. **This is a functionally distinct clade from the anchor's CHK2 subfamily** — Hsk1 (CDC7-type) and Cds1 (CHK2-type) must not share replication-initiation vs. checkpoint-effector annotations.

### PTHR44167:SF30 - PHOSPHORYLASE KINASE
**Members**: 4 proteins

**Function**: Phosphorylase-kinase-type Ser/Thr kinases; a further functional offshoot within the family.

### PTHR44167:SF31 - PROTEIN CBG02007
**Members**: 3 proteins (Caenorhabditis-centric, uncharacterized clade)

## IBA Annotation Assessment

Cds1 receives the following IBA (GO_REF:0000033, PANTHER node PTN005196447) annotations. Seeds for the kinase/process terms include strong orthologs: human CHEK2 (UniProtKB:O96017), Drosophila lok (FB:FBgn0019686), mouse Chek2 (MGI:MGI:2152419), and PomBase entries.

| GO ID | Label | Aspect | Flags | Our action | Assessment |
|-------|-------|--------|-------|------------|------------|
| GO:0004674 | protein serine/threonine kinase activity | MF | (none) | ACCEPT | Correct and core. Family-wide catalytic activity, strongly seeded (2 seeds, same-subfamily). Cds1 kinase activity is experimentally established (Thr328 activation-loop autophosphorylation). |
| GO:0005634 | nucleus | CC | LOCALIZATION | ACCEPT | Correct. Cds1 acts in the nucleus at chromatin/stalled forks; multiple same-subfamily seeds support nuclear localization. |
| GO:0044773 | mitotic DNA damage checkpoint signaling | BP | (none) | MODIFY | Essence correct but term placement refined. Cds1's primary role is the **DNA replication / intra-S (S/M) checkpoint**; the curated review prefers a replication-checkpoint term (e.g. GO:0033314) over the generic DNA-damage checkpoint phrasing, hence MODIFY rather than plain ACCEPT. |
| GO:0005737 | cytoplasm | CC | LOCALIZATION | KEEP_AS_NON_CORE | Reasonable but non-core. Cds1 is an abundant soluble kinase; its functionally relevant site is the nucleus, so cytoplasm is retained as non-core. |

**CROSS_SUBFAMILY risk**: None of cds1's IBAs are flagged CROSS_SUBFAMILY; they originate within the CHK2 subfamily (PTN005196447) with several same-subfamily seeds. There is no leakage from the CDC7/DDK subfamily.

**Curatorial note**: The key risk in this family is not the cds1 IBAs themselves (which are sound for a CHK2-type checkpoint kinase) but cross-clade confusion between the CHK2 checkpoint-effector subfamily (SF24) and the CDC7/DDK replication-initiation subfamily (SF23). The MF (kinase activity) is family-wide and correct; the checkpoint BP is appropriate for SF24 and was refined (MODIFY) to the replication-checkpoint sense for cds1; the localization terms are accepted (nucleus) or kept non-core (cytoplasm) in line with the curated review.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER family metadata/members, UniProt, the cds1 gene review (genes/SCHPO/cds1), and the PANTHER IBA propagation table.
