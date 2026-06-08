# PANTHER Family Review: PTHR22891

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR22891 |
| **Family Name** | Argonaute/Piwi (EUKARYOTIC TRANSLATION INITIATION FACTOR 2C) |
| **InterPro Entry** | (none integrated in metadata) |
| **Total Proteins** | 36,450 |
| **Taxonomic Breadth** | 9,485 taxa |
| **Subfamilies** | 68 |
| **Representative Structure** | 9bf2 (MID domain of Ago2 bound to UMP) |
| **Anchor Gene** | S. pombe ago1 (O74957) |

## Executive Summary

PTHR22891 is the **Argonaute/Piwi** superfamily, the protein effectors of small-RNA-guided gene silencing across eukaryotes (with prokaryotic Argonautes outside the typical eukaryotic clades). Members share the canonical four-domain architecture (N, PAZ, MID, PIWI). The **PAZ domain** anchors the 3' end of a small RNA guide; the **MID domain** binds the 5' phosphate; and the **PIWI domain** adopts an RNase H-like fold that, in catalytically competent ("slicer") members, carries a conserved Asp-Asp-His/Asp-Glu-Asp-His catalytic tetrad and cleaves target RNAs base-paired to the guide.

The conserved core function is **small-RNA-guided recognition of complementary nucleic acid** leading to silencing — either post-transcriptional (mRNA cleavage / translational repression, the AGO clade with miRNA/siRNA) or transcriptional/co-transcriptional (chromatin/heterochromatin silencing, and the PIWI clade with piRNA-directed transposon repression in animal germlines). The family shows clear **neofunctionalization** between the AGO and PIWI clades and, in many lineages, between slicer-competent and slicer-dead paralogs. The fission-yeast anchor **ago1** is unusual in being the **sole Argonaute** of its organism and acting primarily in **RNAi-directed heterochromatin assembly** (RITS complex) at centromeres, the mating-type locus, and subtelomeres, in addition to canonical slicing.

## Subfamily Analysis

PTHR22891 has 68 subfamilies. The retrieved member table (80 proteins) does not carry per-row PANTHER subfamily IDs, so the groupings below are summarized from the protein-name distribution of real members in the table (counts are of the sampled members, not the full family).

### AGO clade — "Protein argonaute" (argonaute-1/-2/-3/-4 and plant/protist AGOs)
**Sampled members**: argonaute-2 (8), argonaute-3 (6), argonaute-4 (4), argonaute-1 (2), plus plant and protist AGOs.

**Key Members**:
- Human AGO2 (slicer; UMP-bound MID structure 9bf2 is from this clade)
- Arabidopsis AGO1 (O04379), AGO6 (O48771)
- *Leishmania* AGO1 (G8XR08), *Giardia* Ago (A8BCK6, C6LTG5)
- C. elegans WAGO clade (wago-1 Q21770, wago-4 O62275, hrde-1 Q09249)

**Function**: miRNA/siRNA-guided post-transcriptional silencing (mRNA slicing or translational repression); plant/protist AGOs also direct chromatin-level silencing.

### PIWI clade — "Piwi-like protein" (PIWIL1-4, Aubergine, Siwi, Ago3)
**Sampled members**: Piwi-like protein 2 (6), Piwi-like protein 1 (5), Piwi-like protein 4 (3), plus *Bombyx* Siwi (A8D8P8) and Ago3 (A9ZSZ2), *Drosophila* Aubergine and Piwi.

**Key Members**:
- Zebrafish piwil2 (A2CEI6), chicken PIWIL1 (A6N7Y9)
- *Bombyx mori* Siwi (A8D8P8), AGO3 (A9ZSZ2)
- C. elegans ergo-1 (O61931, a 26G/piRNA-associated Argonaute)

**Function**: piRNA-guided silencing of transposable elements, primarily in the animal germline; participates in the ping-pong amplification loop.

### Anchor subfamily — S. pombe ago1 (Argonaute)
**Anchor**: O74957 (ago1), "Protein argonaute", 834 aa, S. pombe.

ago1 is the **sole Argonaute** in fission yeast and falls within the broad eukaryotic **AGO clade** (canonical Argonaute, not a PIWI-clade protein). It is the catalytic core of the **RITS** (RNA-induced transcriptional silencing) and **ARC** (Argonaute siRNA chaperone) complexes. Unlike the metazoan AGO subfamilies whose dominant output is mRNA slicing, ago1's principal role is **siRNA-directed (co-transcriptional) heterochromatin assembly**, although it retains a functional slicer (PIWI Asp-Asp-His triad: Asp580, Asp651, His788). It thus represents a lineage where the conserved Argonaute MF (small-RNA binding + slicing) is coupled to a chromatin-silencing BP output.

## IBA Annotation Assessment

Only one IBA (GO_REF:0000033) is propagated to ago1 in the current GOA:

| GO ID | GO label | Aspect | PANTHER node | Our action | Assessment |
|-------|----------|--------|--------------|------------|------------|
| GO:0003727 | single-stranded RNA binding | MF | PTN000527276 | ACCEPT | **CORRECT.** ssRNA binding is the deepest conserved molecular function of the entire Argonaute/Piwi family (binding the single-stranded small-RNA guide). It is fully consistent with ago1's experimentally characterized siRNA-binding slicer activity. Seeds are drawn from across the family (Drosophila, human AGO/PIWI, C. elegans), an expected pan-family core function. |

**Triage flags.** The propagation carries the `GENE_NO_SUBFAMILY` flag, meaning ago1's UniProt record places it at the family level (PTHR22891) without a fine subfamily call in the entries table (its UniProt DR line reads `PTHR22891` only). This is a triage signal, **not** a verdict: GO:0003727 is a family-wide conserved function and crossing subfamily boundaries here is expected and harmless, because every member binds a single-stranded small RNA.

**Notable absences (no positive error, but worth flagging for curators).** The single IBA does **not** capture ago1's better-characterized molecular function — endoribonuclease/slicer activity (RNA-guided target cleavage) — nor its heterochromatin/RITS roles. These are present in ago1's experimental annotations and are appropriately handled there rather than by IBA. No IBA should be **removed**: the lone propagated term is correct and conservative.

**No localization conflicts.** No CC term is propagated by IBA, so there is no risk of transferring a clade-specific localization (e.g., a PIWI-clade germline/nuage localization) onto the fission-yeast protein.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata, family entry table, S. pombe ago1 UniProt/GOA/AI-review, iba_propagation.tsv
