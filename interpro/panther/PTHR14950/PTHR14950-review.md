# PANTHER Family Review: PTHR14950

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR14950 |
| **Family Name** | DICER-RELATED |
| **InterPro Entry** | (not integrated in metadata) |
| **Total Proteins** | 15,463 |
| **Taxonomic Breadth** | 10,854 taxa |
| **Subfamilies** | 23 |
| **Representative Structure** | 4ngd (Human Dicer Platform-PAZ-Connector Helix cassette in complex with 12-mer siRNA) |
| **Anchor Gene** | dcr1 (Q09884), *Schizosaccharomyces pombe* |
| **Anchor Subfamily** | PTHR14950:SF37 (ENDORIBONUCLEASE DICER) |

## Executive Summary

PTHR14950 (DICER-RELATED) groups the **ribonuclease III (RNase III) superfamily of dsRNA-specific endonucleases**, ranging from compact bacterial RNase III (gene *rnc*) through the large multidomain Dicer and Dicer-like (DCL) proteins of eukaryotes. The **conserved core function across the family is RNase III-type cleavage of double-stranded RNA** (GO:0004525), producing short RNA duplexes with characteristic 2-nt 3' overhangs.

The family shows clear architectural elaboration: bacterial members are minimal (a single RNase III catalytic domain plus a dsRNA-binding domain), whereas eukaryotic Dicers/DCLs add helicase, PAZ, DUF283, and tandem RNase III domains that allow processive, length-defined dicing of dsRNA and pre-miRNA into ~21-23 nt small RNAs. **Neo-functionalization is therefore primarily at the level of substrate handling and downstream pathway coupling** (siRNA biogenesis, miRNA biogenesis, antiviral RNAi, heterochromatic siRNA production) rather than a change in the underlying catalytic chemistry.

The anchor gene **dcr1** is the sole Dicer of fission yeast and the initiating nuclease of the RNAi pathway that drives pericentromeric heterochromatin assembly.

## Subfamily Analysis

### PTHR14950:SF37 - ENDORIBONUCLEASE DICER  **(anchor subfamily)**
**Members (sampled)**: 44 of 72 sampled entries (largest subfamily in the sample)

**Taxonomy**: Broad — metazoan canonical Dicers, fungal Dicer-like 2 (DCL2-type), and bacterial RNase III (*rnc*) all map here in the sample.

**Key Members**:
- *S. pombe* dcr1 (Q09884) — **anchor**
- Human DICER1 (Q9UPY3)
- Mouse Dicer1 (Q8R418)
- *D. melanogaster* Dcr-1 (Q9VCU9)
- *C. elegans* dcr-1 (P34529)
- Fungal Dicer-like protein 2 (e.g. Neurospora dcl-2 Q7SCC1)
- Bacterial RNase III (*rnc*; e.g. P47607, P75233)

**Function**: Ribonuclease III activity (GO:0004525); dsRNA cleavage feeding small-RNA pathways.

**Notes**: This subfamily is heterogeneous in the sample, mixing canonical metazoan Dicers, fungal DCL2-type proteins, and minimal bacterial RNase III. The fission yeast dcr1 sits with the metazoan Dicers and fungal DCL2 clade, consistent with its role as the single RNAi Dicer in *S. pombe*.

### PTHR14950:SF62 - DICER-LIKE PROTEIN 1
**Members (sampled)**: 12

**Taxonomy**: Fungal (Aspergillus, Neurospora, Pyricularia, Chaetomium, Coccidioides, Cryphonectria).

**Key Members**: Neurospora dcl-1 (Q7S8J7); Aspergillus fumigatus dcl1 (Q4WVE3); Cryphonectria DCL-1 (Q2VF19).

**Function**: RNase III / Dicer-type dsRNA processing; the DCL1-type paralog in fungi that typically have two Dicer-like genes.

### PTHR14950:SF49 - RIBONUCLEASE 3-LIKE PROTEIN 2-RELATED
**Members (sampled)**: 4 (plant RNase-III-like, RTL-type)

**Key Members**: Arabidopsis RTL2 (Q9LTQ0), RTL3 (Q9FKF0); rice Os01g0551100 (Q5JK90).

**Function**: Plant RNase-III-like proteins (RTL family) acting in dsRNA processing distinct from canonical DCLs.

### PTHR14950:SF70 / SF46 / SF15 / SF31 - PLANT DICER-LIKE (DCL2/DCL3/DCL4) CLADES
**Members (sampled)**: 2-3 each — plant Dicer-like proteins (Arabidopsis/rice DCL2, DCL3, DCL4 homologs).

**Function**: The diversified plant DCL paralogs, each specialized for distinct small-RNA pathways (e.g. DCL3→heterochromatic siRNA, DCL4→tasiRNA), but all retaining RNase III dicing chemistry.

## IBA Annotation Assessment

The following IBA annotations (GO_REF:0000033) are propagated to dcr1 (Q09884) from PANTHER node **PTN000383725**. Our curated actions (from `iba_propagation.tsv`) are shown.

| GO ID | Label | Aspect | Our action | Assessment |
|-------|-------|--------|-----------|------------|
| GO:0004525 | ribonuclease III activity | MF | **ACCEPT** | Correct and core. This is the defining catalytic activity of the entire family and is directly supported for dcr1; appropriate propagation. |
| GO:0030422 | siRNA processing | BP | **ACCEPT** | Correct and core. dcr1 generates the siRNAs that initiate RNAi-directed heterochromatin in *S. pombe*. Appropriate. |
| GO:0003723 | RNA binding | MF | **MARK_AS_OVER_ANNOTATED** | True but uninformative. dcr1 binds dsRNA, but the generic "RNA binding" parent adds little over the specific catalytic term; flagged as over-annotation rather than wrong. |
| GO:0005737 | cytoplasm | CC | **KEEP_AS_NON_CORE** | Localization transfer. Metazoan Dicers are largely cytoplasmic, but dcr1 function in *S. pombe* is critically nuclear (zinc-dependent nuclear retention is required for RNAi heterochromatin). Cytoplasmic localization is plausible but non-core for the fission yeast protein. |
| GO:0005634 | nucleus | CC | **ACCEPT** | Localization transfer, and here it is the biologically important one for dcr1: nuclear retention is required for heterochromatin assembly. Appropriate despite NO_UNIPROT_SEEDS flag (the node lacked UniProt seeds but the assignment matches known dcr1 biology). |

**Verdict**: The catalytic and process annotations (GO:0004525, GO:0030422) are clean, conserved-core propagations. The two localization terms illustrate the calibrated localization caveat — both compartments occur within the family, and for dcr1 the **nuclear** compartment is the functionally load-bearing one, so the cytoplasm transfer is retained only as non-core. No propagation here is biologically contradicted, so none warrants REMOVE.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt (dcr1 Q09884), dcr1 AI review, GOA IBA rows, iba_propagation.tsv
