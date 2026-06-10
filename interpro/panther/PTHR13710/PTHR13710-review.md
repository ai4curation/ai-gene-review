# PANTHER Family Review: PTHR13710

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR13710 |
| **Family Name** | RecQ Helicase (DNA HELICASE RECQ FAMILY MEMBER) |
| **InterPro Entry** | (not integrated; PANTHER-only entry) |
| **Total Proteins** | 65,529 |
| **Taxonomic Breadth** | 33,164 taxa |
| **Subfamilies** | 18 |
| **Representative Structure** | 9og8 (Crystal structure of WRN in complex with compound 43) |

## Executive Summary

PTHR13710 is the **RecQ-family of ATP-dependent 3'-to-5' DNA helicases**, present from bacteria to humans and central to genome stability. Members couple ATP hydrolysis to 3'-5' unwinding of duplex DNA (SF2 helicase core: Walker-A ATP-binding motif and DEAH box) and are characterized by a RecQ-specific RQC/zinc-binding region and a C-terminal HRDC domain. The conserved core function is **DNA unwinding in service of replication, repair, recombination, and genome-stability maintenance** — resolving stalled/collapsed replication forks, dissolving recombination intermediates (D-loops, double Holliday junctions, often acting together with topoisomerase III), and suppressing hyper-recombination.

This is a large, deeply branched family with substantial **subfunctionalization**: humans alone have five RecQ paralogs (RECQL1, BLM, WRN, RECQL4, RECQL5) that occupy distinct subfamilies and have partly distinct roles (e.g. WRN uniquely carries a 3'-5' exonuclease domain; RECQL4 functions in replication initiation). Single-RecQ organisms such as budding yeast (Sgs1) and fission yeast (Rqh1) carry the combined functions in one protein. Because the family is broad and fine-grained, IBA propagation can occasionally pull lineage-specific properties (notably localization) across subfamily boundaries — this family contains a documented true-positive over-propagation (see IBA assessment).

## Subfamily Analysis

### PTHR13710:SF153 - RECQ-LIKE DNA HELICASE BLM (anchor subfamily of S. pombe rqh1)
**Members**: ~9 curated members — the BLM/Sgs1/Rqh1 orthologous group

**Key Members** (from family member table):
- *S. pombe* rqh1 (Q09811) — **our anchor gene**
- *Homo sapiens* BLM (P54132)
- *Mus musculus* Blm (O88700)
- *S. cerevisiae* SGS1 (P35187)
- *C. elegans* him-6 (O18017)
- *Drosophila melanogaster* Blm (Q9VGI8)
- *Gallus gallus* BLM (Q9I920)
- *Xenopus laevis* blm (Q9DEY9)
- *Arabidopsis thaliana* RECQL1 (Q9FT74)

**Function**: BLM/Sgs1/Rqh1-type RecQ helicase acting (often with Top3) to dissolve recombination intermediates and process replication forks in the nucleus. This is the subfamily to which **S. pombe rqh1 (Q09811) belongs** (UniProt: `DR PANTHER; PTHR13710:SF153`).

### PTHR13710:SF105 - ATP-DEPENDENT DNA HELICASE Q1
**Members**: ~13 curated members (largest subfamily)

**Function**: RECQL1-type helicases. The largest subfamily; a sibling lineage to the anchor's BLM subfamily and a source of cross-subfamily IBA seeds.

### PTHR13710:SF120 - BIFUNCTIONAL 3'-5' EXONUCLEASE / ATP-DEPENDENT HELICASE WRN
**Members**: ~5 curated members

**Function**: WRN-type helicases, distinguished by an additional N-terminal 3'-5' exonuclease domain — a clear neo-functionalization within the family.

### PTHR13710:SF152 / SF108 / SF149 - DNA HELICASE Q5 / Q4 / TLH2
**Members**: 3 members each

**Function**: RECQL5 (SF152) and RECQL4 (SF108) paralog lineages plus telomere-linked helicase (TLH2, SF149). These siblings provide additional IBA seeds for several rqh1 annotations.

## IBA Annotation Assessment

The following IBA (GO_REF:0000033) annotations were propagated to S. pombe rqh1 (Q09811). PANTHER node, seed subfamilies, and flags are from `iba_propagation.tsv`.

| GO ID | Label | Aspect | Node | Seed SFs | Our Action | Assessment |
|-------|-------|--------|------|----------|------------|------------|
| GO:0005737 | **cytoplasm** | CC | PTN000344873 | SF105; SF152 | **REMOVE** | **Over-propagation (TRUE POSITIVE).** This cytoplasm term was propagated from sibling RecQ subfamilies (RECQL1/SF105 and RECQL5/SF152), not from the BLM/Rqh1 lineage. All experimental *S. pombe* data place Rqh1 in the nucleus (nuclear chromosome, nucleolus, replication forks, DSB sites); there is no support for a cytoplasmic site of action. This is a `CROSS_SUBFAMILY;LOCALIZATION` case where the flag correctly signals a genuine error, and we **REMOVE** it. |
| GO:0005634 | nucleus | CC | PTN001415789 | SF152 | ACCEPT | **Appropriate.** Nuclear localization is the experimentally established compartment for Rqh1 and the conserved site of RecQ function. Correct despite cross-subfamily seeding. |
| GO:0005694 | chromosome | CC | PTN000344873 | SF105; SF108; SF120; SF152 | ACCEPT | **Appropriate.** RecQ helicases act on chromosomal DNA; chromosome localization is a broadly conserved, experimentally supported property of Rqh1. The cross-subfamily flag is triage only here. |
| GO:0006260 | DNA replication | BP | PTN000344874 | SF105; SF108; SF120; SF152 | KEEP_AS_NON_CORE | **Appropriate but non-core.** Rqh1 processes replication forks, so involvement in DNA replication is real but is a secondary, supporting role relative to its core helicase/recombination-suppression function. Propagation valid; downgraded to non-core. |

**Summary:** Three of four propagations are correct; the standout is **GO:0005737 (cytoplasm)**, a genuine cross-subfamily over-propagation from RECQL1/RECQL5 siblings that contradicts the experimentally nuclear localization of Rqh1, which we therefore **REMOVE**. This illustrates the calibrated rule that `LOCALIZATION` terms imported from a sibling subfamily can be true over-annotations when they contradict known localization — in contrast to the broadly conserved nuclear/chromosome terms, which are retained.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, S. pombe rqh1 GOA + ai-review, iba_propagation.tsv
