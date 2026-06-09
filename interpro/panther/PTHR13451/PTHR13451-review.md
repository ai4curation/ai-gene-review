# PANTHER Family Review: PTHR13451

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR13451 |
| **Family Name** | CLASS II CROSSOVER JUNCTION ENDONUCLEASE MUS81 |
| **InterPro Entry** | IPR033309 |
| **Total Proteins** | 5,163 |
| **Taxonomic Breadth** | 7,690 taxa |
| **Subfamilies** | 8 |
| **Representative Structure** | 7bu5 (Crystal structure of human SLX4 and MUS81) |

## Executive Summary

PTHR13451 is the **MUS81 structure-specific endonuclease family**, a member of the XPF/ERCC4 nuclease superfamily. Members carry an ERCC4 (XPF-type) nuclease domain with an essential catalytic aspartate pair and a tandem helix-hairpin-helix (HhH) region used for DNA binding and heterodimerization. The conserved core function is **crossover-junction / branched-DNA endonuclease activity**: as an obligate heterodimer (with Eme1/Mms4/EME1), MUS81 cleaves branched DNA intermediates bearing a free 5'-end at the branch point — nicked Holliday junctions (its preferred substrate), 3'-flaps, D-loops, model replication forks, and (as a backup) intact Holliday junctions. Through this activity the family resolves recombination intermediates and joint molecules, processes stalled/collapsed replication forks, and supports double-strand break repair.

The family is **strongly conserved in biochemical function** with little neo-functionalization: the dominant subfamily (SF0) collects MUS81 orthologs across fungi, plants, and animals, all performing the same resolvase role. In meiosis, MUS81-Eme1 is the principal nuclear resolvase generating crossovers, a role that is especially central in organisms (such as *S. pombe*) that lack the MSH4-MSH5 crossover pathway.

## Subfamily Analysis

### PTHR13451:SF0 - CROSSOVER JUNCTION ENDONUCLEASE MUS81 (anchor subfamily of S. pombe mus81)
**Members**: ~23 curated members — by far the largest subfamily, collecting canonical MUS81 orthologs

**Key Members** (from family member table):
- *S. pombe* mus81 (P87231) — **our anchor gene**
- *Homo sapiens* MUS81 (Q96NY9)
- *Mus musculus* Mus81 (Q91ZJ0)
- *S. cerevisiae* MUS81 (Q04149)
- *Arabidopsis thaliana* MUS81 (Q5W9E7)
- *Oryza sativa* MUS81 (Q8GT06)
- *Neurospora crassa* mus-81 (Q7SD49)
- (also numerous African swine fever virus members, e.g. Ba71V-059 Q65151)

**Function**: ERCC4-domain crossover-junction DNA endonuclease that resolves branched DNA intermediates. This is the subfamily to which **S. pombe mus81 (P87231) belongs** (UniProt: `DR PANTHER; PTHR13451:SF0`). The anchor occupies the central, canonical MUS81 clade.

### PTHR13451:SF8 - CROSSOVER JUNCTION ENDONUCLEASE MUS81-RELATED
**Members**: small set of MUS81-related variants

**Function**: Divergent MUS81-like proteins; retain the ERCC4-nuclease architecture but are placed in a separate phylogenetic subfamily. Same general resolvase role inferred.

## IBA Annotation Assessment

The following IBA (GO_REF:0000033) annotations were propagated to S. pombe mus81 (P87231). PANTHER node and seed information is from `iba_propagation.tsv`.

| GO ID | Label | Aspect | Node | Our Action | Assessment |
|-------|-------|--------|------|------------|------------|
| GO:0008821 | crossover junction DNA endonuclease activity | MF | PTN000335543 | ACCEPT | **Appropriate.** This is the defining catalytic activity of the MUS81 family and is experimentally established for fission yeast Mus81-Eme1. Correct propagation. |
| GO:0048476 | Holliday junction resolvase complex | CC | PTN000335543 | ACCEPT | **Appropriate.** Mus81 functions as part of a Holliday-junction resolvase (Mus81-Eme1) complex; the `LOCALIZATION` flag is triage only. Consistent with experimental data. |
| GO:0000712 | resolution of meiotic recombination intermediates | BP | PTN000335543 | ACCEPT | **Appropriate.** Mus81-Eme1 is the principal meiotic resolvase in *S. pombe*; this propagation captures a well-supported core process. |
| GO:0031573 | mitotic intra-S DNA damage checkpoint signaling | BP | PTN000335543 | ACCEPT | **Appropriate.** Mus81 acts with the replication checkpoint (Cds1) during S phase; supported in fission yeast. Correct propagation. |
| GO:0000727 | double-strand break repair via break-induced replication | BP | PTN000335543 | KEEP_AS_NON_CORE | **Appropriate but non-core.** BIR/fork-processing is a genuine but secondary role relative to junction resolution. Propagation valid; downgraded to non-core. |

**Summary:** All five IBA propagations to mus81 are biologically correct. The single shared node (PTN000335543) and the tight, single-function dominant subfamily make these propagations high-confidence. No removals warranted.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, S. pombe mus81 GOA + ai-review, iba_propagation.tsv
