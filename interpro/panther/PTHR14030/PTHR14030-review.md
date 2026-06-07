# PANTHER Family Review: PTHR14030

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR14030 |
| **Family Name** | MITOTIC CHECKPOINT SERINE/THREONINE-PROTEIN KINASE BUB1 |
| **InterPro Entry** | IPR015661 |
| **Total Proteins** | 7,703 |
| **Taxonomic Breadth** | 8,950 taxa |
| **Subfamilies** | 7 |
| **Representative Structure** | 6f7b (Human Bub1 kinase domain in complex with BAY 1816032) |

## Executive Summary

PTHR14030 is the **BUB1 / BUBR1 (Mad3) spindle-assembly-checkpoint (SAC) kinase family**. Members share an N-terminal tetratricopeptide-repeat (TPR / Mad3-like) region that targets the protein to kinetochores and a C-terminal protein-kinase fold. The conserved core function is **kinetochore-localized SAC signaling**: family members are recruited to unattached/tensionless kinetochores (downstream of Mps1/Mph1 phosphorylation of KNL1/Spc7 MELT motifs), where they scaffold assembly of the mitotic checkpoint complex and generate the diffusible "wait-anaphase" signal that inhibits the APC/C until all chromosomes are bioriented.

The family shows a notable **functional split / subfunctionalization**: the true BUB1 lineage retains an active kinase domain (phosphorylating histone H2A at the centromere to recruit shugoshin and promote biorientation), whereas the paralogous BUBR1/Mad3 lineage has, in many species, a degenerate/pseudokinase domain and acts chiefly as a structural component of the mitotic checkpoint complex. This pseudokinase divergence is the family's principal neo-functionalization and is the reason IBA propagation of catalytic terms must be evaluated carefully across subfamilies.

## Subfamily Analysis

### PTHR14030:SF4 - BUB1 KINASE, ISOFORM A-RELATED (anchor subfamily of S. pombe bub1)
**Members**: ~7 curated members — the largest subfamily, collecting BUB1/Mad3-type proteins

**Key Members** (from family member table):
- *S. pombe* bub1 (O94751) — **our anchor gene**
- *S. pombe* mad3 (O59767)
- *S. cerevisiae* BUB1 (P41695)
- *S. cerevisiae* MAD3 (P47074)
- *Arabidopsis thaliana* BUB1 (F4IVI0)
- *C. elegans* bub-1 (Q21776)
- *Dictyostelium discoideum* bub1 (Q54CV5)

**Function**: SAC kinase/scaffold. This is the subfamily to which **S. pombe bub1 (O94751) belongs** (UniProt: `DR PANTHER; PTHR14030:SF4`). Note this subfamily mixes both kinase-active BUB1 and Mad3-type members, which is relevant to the catalytic-term assessment below.

### PTHR14030:SF26 - MITOTIC CHECKPOINT SERINE/THREONINE-PROTEIN KINASE BUB1
**Members**: ~2 curated members

**Function**: Canonical kinase-active BUB1 orthologs. This subfamily seeds the protein-kinase-activity propagation onto the anchor (cross-subfamily seed).

### PTHR14030:SF25 - MITOTIC CHECKPOINT SERINE/THREONINE-PROTEIN KINASE BUB1 BETA (BUBR1)
**Members**: ~2 curated members

**Function**: BUBR1/BUB1B lineage — frequently a **pseudokinase** acting as a structural MCC component. A nucleus-localization seed for the anchor's nucleus term.

### PTHR14030:SF19 - MITOTIC SPINDLE CHECKPOINT PROTEIN BUBR1
**Members**: ~1 curated member

**Function**: Additional BUBR1-type checkpoint protein lineage.

## IBA Annotation Assessment

The following IBA (GO_REF:0000033) annotations were propagated to S. pombe bub1 (O94751). PANTHER node, seed subfamilies, and flags are from `iba_propagation.tsv`.

| GO ID | Label | Aspect | Node | Seed SFs | Our Action | Assessment |
|-------|-------|--------|------|----------|------------|------------|
| GO:0004672 | protein kinase activity | MF | PTN000361607 | SF26 | **MODIFY** | **Appropriate, refined.** The IBA assignment is correct — Bub1 is a bona fide kinase — but generic. We MODIFY to the more specific GO:0004674 (protein serine/threonine kinase activity), supported by direct experimental evidence (Bub1 phosphorylates histone H2A-S121 in fission yeast, PMID:19965387). The `CROSS_SUBFAMILY` seed (SF26, canonical kinase BUB1) is biologically valid here because the anchor is a true active kinase, not a pseudokinase. |
| GO:0005634 | nucleus | CC | PTN000361608 | SF25; SF26 | ACCEPT | **Appropriate.** Nuclear/kinetochore localization is the conserved compartment of SAC kinases; the `CROSS_SUBFAMILY;LOCALIZATION` flag is triage only, and the term is consistent with Bub1's nuclear/kinetochore biology in fission yeast. |
| GO:0051754 | meiotic sister chromatid cohesion, centromeric | BP | PTN000361607 | (no UniProt seeds) | KEEP_AS_NON_CORE | **Appropriate but non-core.** Bub1 supports protection of centromeric cohesin (via shugoshin recruitment) in meiosis — a genuine but specialized role secondary to its core mitotic SAC function. Propagation valid; downgraded to non-core. |

**Summary:** All three IBA propagations to bub1 are biologically sound. The protein-kinase term is correct but generic and is refined (MODIFY → serine/threonine kinase) on experimental grounds; the cross-subfamily kinase seed is appropriate because the anchor is a genuine active kinase rather than a BUBR1-type pseudokinase. No removals warranted.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, S. pombe bub1 GOA + ai-review, iba_propagation.tsv
