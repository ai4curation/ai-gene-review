# PANTHER Family Review: PTHR19304

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR19304 |
| **Family Name** | Basic leucine zipper (bZIP) transcription factors (CYCLIC-AMP RESPONSE ELEMENT BINDING PROTEIN) |
| **InterPro Entry** | IPR051027 |
| **Total Proteins** | 10,160 |
| **Taxonomic Breadth** | 6,903 taxa |
| **Subfamilies** | 9 |
| **Representative Structure** | 8ype (inactive p38 complexed with ATF2 residues 46-80) |

## Executive Summary

PTHR19304 is the **ATF/CREB subgroup of basic leucine zipper (bZIP) transcription factors**, including the ATF-2/ATF-7/CREB5 metazoan proteins, the fungal ATF/CREB activators (yeast ACA1, CST6, SKO1; *S. pombe* atf1, atf21, atf31, pcr1), and fungal stress bZIPs (Aspergillus atfB). All members share the **bZIP domain**, a basic region that contacts DNA fused to a leucine-zipper that mediates homo- and hetero-dimerization. They bind CRE/ATF-type sites (the cAMP response element, consensus TGACGTCA / the M26 ATGACGT site) and AP-1-related elements to activate or repress RNA polymerase II transcription.

The **conserved core function across the family is sequence-specific RNA Pol II DNA-binding transcription factor activity** acting on CRE/ATF cis-regulatory elements, with the downstream biology (stress response, cAMP/calcium signalling, DNA-damage response, developmental and metabolic programs) tuned by lineage-specific upstream kinases and dimerization partners. Neofunctionalization is largely at the level of **regulatory inputs and target regulons** rather than the biochemistry of DNA binding.

The fission yeast anchor **atf1 (P52890)** is the principal ATF/CREB bZIP of *S. pombe*, strongly homologous to mammalian ATF-2/CRE-BP1. It heterodimerizes with Pcr1, binds CRE/M26 sites, is the major nuclear substrate of the Sty1/Spc1 SAPK, and drives the core environmental stress response, sexual differentiation/meiosis, the ade6-M26 recombination hotspot, and RNAi-independent mating-type heterochromatin nucleation.

## Subfamily Analysis

**Note on subfamily assignment**: In the curated reference set for PTHR19304, the `subfamily` / `subfamily_name` columns are not populated for any of the 23 reference proteins, and the *S. pombe* atf1 UniProt record carries only the family-level `DR PANTHER; PTHR19304` annotation **without an :SFn subfamily**. The iba_propagation analysis accordingly flags atf1 as `GENE_NO_SUBFAMILY`. The analysis below therefore groups members by orthology/function rather than by formal PANTHER subfamily IDs, and the anchor's "subfamily" is the family node itself (PTN004510459).

### Metazoan ATF-2 / ATF-7 / CREB5 group
**Key Members**:
- Human ATF2 (P15336), Mouse Atf2 (P16951), Rat Atf2 (Q00969), Chicken ATF2 (O93602)
- Human ATF7 (P17544), Mouse Atf7 (Q8R0S1), Orangutan ATF7 (Q5R9C9)
- Human CREB5 (Q02930), Mouse Creb5 (Q8K1L0)
- *C. elegans* atf-7 (Q86MD3)

**Function**: Stress- and signal-responsive CRE-binding transcription factors; ATF-2/ATF-7 are p38/JNK MAPK substrates (consistent with the 8ype p38-ATF2 representative structure).

### Fungal ATF/CREB activators (incl. ANCHOR)
**Key Members**:
- ***S. pombe* atf1 (P52890) - the anchor gene**
- *S. pombe* atf21 (P78962), atf31 (Q09771), pcr1 (Q09926, the atf1 dimerization partner)
- *S. cerevisiae* ACA1 (P39970), CST6 (P40535), SKO1 (Q02100)
- *Candida albicans* SKO1 (Q59VR1)

**Function**: bZIP transcription factors of the fungal stress/CRE regulons. atf1 is the *S. pombe* ATF-2 ortholog; pcr1 is its obligate heterodimer partner at M26 sites.

### Fungal atfB stress bZIPs
**Key Members**: Aspergillus atfB (Q4WVQ7, B8NLU5, Q2U616, A0A0F0IP79), *Penicillium expansum* Atf1 (A0A0A2J9B3)

**Function**: bZIP factors governing oxidative-stress and secondary-metabolism (e.g. aflatoxin) gene expression in filamentous fungi.

## Functional Diversity Assessment

### Neo-functionalization: MODERATE (regulatory, not biochemical)
All members are bZIP CRE/ATF-binding transcription factors. The diversity lies in **which kinase activates them** (p38/JNK in mammals; Sty1/Spc1 SAPK for atf1), **which partner they dimerize with** (atf1-Pcr1), and **which regulon they control** (stress, cAMP, differentiation, secondary metabolism). The DNA-binding/dimerization biochemistry is conserved family-wide.

## IBA Annotation Assessment

IBA annotations (GO_REF:0000033, node PTN004510459) propagated to atf1 (P52890). All carry the `GENE_NO_SUBFAMILY` flag because atf1 has no :SFn assignment; propagation is from the family node.

| GO ID | Label | Aspect | Flags | Assessment |
|-------|-------|--------|-------|------------|
| GO:0000981 | DNA-binding transcription factor activity, RNA polymerase II-specific | MF | GENE_NO_SUBFAMILY | **APPROPRIATE.** Defining family-wide function; matches atf1's curated core function as a sequence-specific Pol II TF. Seeded by 2 in-family proteins. |
| GO:0000978 | RNA polymerase II cis-regulatory region sequence-specific DNA binding | MF | GENE_NO_SUBFAMILY | **APPROPRIATE.** atf1 binds CRE/M26 (ATGACGT) cis-regulatory sites; this is exactly the conserved bZIP DNA-binding activity. |
| GO:0006357 | regulation of transcription by RNA polymerase II | BP | GENE_NO_SUBFAMILY | **APPROPRIATE.** Core conserved process; atf1 activates/represses the stress regulon via Pol II. |
| GO:0005634 | nucleus | CC | LOCALIZATION; GENE_NO_SUBFAMILY | **APPROPRIATE.** atf1 is a nuclear transcription factor (and the major nuclear SAPK substrate). Localization transfer is consistent with known biology - no conflict. |

**Summary**: All four propagations are clean and consistent with atf1's curated function. The `GENE_NO_SUBFAMILY` flag reflects missing fine-grained subfamily structure for this family, not an error; because the entire family is the ATF/CREB bZIP group, family-node propagation of generic TF/DNA-binding/nucleus terms is biologically appropriate. The IBA set is intentionally generic (it does not, and should not, transfer atf1-specific roles such as heterochromatin nucleation or the M26 recombination hotspot, which are not conserved family-wide).

## Key Literature

| PMID | Key Finding |
|------|-------------|
| PMID:8824588 | atf1 target genes induced via Sty1 kinase and Atf1. |
| PMID:18375981 | Atf1-Pcr1 heterodimer binds M26 (ATGACGT) with ~1 nM affinity. |
| PMID:8557039 | Atf1 drives exit from mitotic cycle into differentiation/resting state under stress. |
| PMID:9391101 | Mts1/Mts2 (Atf1/Pcr1) heterodimer essential for ade6-M26 hotspot activity. |
| PMID:15218150 | Atf1/Pcr1 target H3K9me and Swi6 to the mating-type region. |

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER PTHR19304 metadata/entries, UniProt (P52890), atf1 ai-review, GOA IBA annotations, iba_propagation.tsv
