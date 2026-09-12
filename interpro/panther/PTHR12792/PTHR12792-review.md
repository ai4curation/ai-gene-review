# PANTHER Family Review: PTHR12792

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR12792 |
| **Family Name** | EXTRA SPINDLE POLES 1-RELATED |
| **InterPro Entry** | IPR005314 |
| **Total Proteins** | 5,038 |
| **Taxonomic Breadth** | 8,522 taxa |
| **Subfamilies** | 2 |
| **Representative Structure** | 5fc2 (separase in complex with a pAMK phospho-serine peptide) |

## Executive Summary

PTHR12792 is the **separase (separin / ESPL1 / Esp1) family**. Its members are large CD-clan **cysteine endopeptidases** (peptidase family C50, EC 3.4.22.49) that trigger the metaphase-to-anaphase transition by proteolytically cleaving the kleisin (alpha-kleisin/Rad21/Scc1 in mitosis, Rec8 in meiosis) subunit of cohesin. Cleavage opens the cohesin ring and allows sister chromatids (or homologs) to separate. The catalytic activity resides in a C-terminal peptidase C50 domain bearing a His/Cys catalytic dyad; the bulk of the protein is an N-terminal alpha-solenoid (TPR-like / ARM-repeat) region that mediates regulation and substrate engagement.

The family is **highly conserved in core function** with minimal neo-functionalization: across eukaryotes separase performs the same essential cohesin-cleavage role. Regulation is conserved too — separase is held inactive through most of the cell cycle by its inhibitory chaperone securin (Cut2/Pds1/PTTG), which is destroyed by the APC/C at anaphase onset to liberate the protease. Beyond chromosome segregation, separases participate in spindle/spindle-pole-body functions and (in some lineages) centriole disengagement.

## Subfamily Analysis

The family resolves into only **2 PANTHER subfamilies**, and essentially all curated members fall into a single separin subfamily.

### PTHR12792:SF0 - SEPARIN (anchor subfamily of S. pombe cut1)
**Members**: the separase/separin orthologs across eukaryotes (the dominant subfamily)

**Key Members** (from family member table):
- *S. pombe* cut1 (P18296) — **our anchor gene**
- *S. cerevisiae* ESP1 (Q03018)
- *Homo sapiens* ESPL1 (Q14674)
- *Mus musculus* Espl1 (P60330)
- *C. elegans* sep-1 (G5ED39)
- *Emericella nidulans* bimB (P33144)
- *Arabidopsis thaliana* ESP1 (Q5IBC5)

**Function**: Cysteine-type endopeptidase (EC 3.4.22.49) that cleaves cohesin kleisin to trigger anaphase. This is the subfamily to which **S. pombe cut1 (P18296) belongs** (UniProt: `DR PANTHER; PTHR12792:SF0`). Because the family has so few subfamilies and a single conserved enzymatic activity, the anchor sits squarely in the canonical separase clade.

## IBA Annotation Assessment

The following IBA (GO_REF:0000033) annotations were propagated to S. pombe cut1 (P18296). PANTHER node and seed information is from `iba_propagation.tsv`.

| GO ID | Label | Aspect | Node | Our Action | Assessment |
|-------|-------|--------|------|------------|------------|
| GO:0004197 | cysteine-type endopeptidase activity | MF | PTN000300670 | ACCEPT | **Appropriate.** This is the defining catalytic activity of the separase family (EC 3.4.22.49) and is experimentally established for Cut1. Correct propagation. |
| GO:0005634 | nucleus | CC | PTN000300670 | ACCEPT | **Appropriate.** Separase acts on chromosomal cohesin and is nuclear during the relevant cell-cycle window; the `LOCALIZATION` flag is triage only. Consistent with experimental data. |
| GO:0005737 | cytoplasm | CC | PTN000300670 | ACCEPT | **Appropriate.** Cut1 is documented as cytoplasmic during interphase before relocating to spindle structures; the cytoplasmic IBA is consistent with experimental localization, not a contradicting over-propagation. |
| GO:0072686 | mitotic spindle | CC | PTN000300670 | ACCEPT | **Appropriate.** Cut1 relocalizes to the mitotic spindle and spindle midzone during anaphase; supported in fission yeast. |
| GO:0044732 | mitotic spindle pole body | CC | PTN000980533 | ACCEPT | **Appropriate.** Cut1 associates with the spindle pole body upon mitotic entry; this localization is experimentally documented for fission yeast and the SPB-bearing node propagation is valid. |

**Summary:** All five IBA propagations to cut1 are biologically correct, including all four localization terms. The multiple `LOCALIZATION` flags reflect the dynamic, cell-cycle-staged localization of separase (cytoplasm → SPB → spindle/midzone) rather than spurious sibling-subfamily contamination. No removals warranted.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, S. pombe cut1 GOA + ai-review, iba_propagation.tsv
