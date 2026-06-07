# PANTHER Family Review: PTHR19918

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR19918 |
| **Family Name** | CELL DIVISION CYCLE 20 CDC20 FIZZY -RELATED |
| **InterPro Entry** | IPR033010 |
| **Total Proteins** | 16,158 |
| **Taxonomic Breadth** | 9,571 taxa |
| **Subfamilies** | 26 |
| **Representative Structure** | 4ggc (Human Cdc20 - multi-site degron recognition by APC/C) |

## Executive Summary

PTHR19918 is the **Cdc20/Fizzy/Cdh1 family of APC/C coactivators**. Members are **WD40 beta-propeller substrate-recognition adaptors** that bind and activate the **anaphase-promoting complex/cyclosome (APC/C)**, the RING E3 ubiquitin ligase driving cell-cycle progression. Through their WD40 propeller (and N-terminal C-box / C-terminal IR motifs) these proteins recognize **D-box and KEN-box degrons** on substrates and present them to the APC/C for polyubiquitination and proteasomal degradation. The family splits into the **Cdc20/Fizzy** branch (mitotic, metaphase-to-anaphase) and the **Cdh1/Fizzy-related (Hct1/Srw1/FZR/CCS52)** branch (late-mitosis/G1 and developmental), plus meiosis-specific activators (Ama1, Mfr1/Mfr2) and the *Drosophila/Lepidoptera* meiotic Cortex proteins.

The **conserved core function across the family is acting as an APC/C activator / substrate-recognition subunit** that promotes APC/C-dependent ubiquitin-mediated proteolysis. Neofunctionalization is at the level of **timing and substrate repertoire** (mitotic vs G1 vs meiotic activators), not the underlying biochemistry.

The fission yeast anchor **slp1 (P78972)** is the *S. pombe* **Cdc20/Fizzy ortholog**: it activates the APC/C at the metaphase-to-anaphase transition to degrade securin (Cut2) and cyclin B (Cdc13), and is the principal target of the spindle assembly checkpoint (sequestered in the Mad2-Mad3-Slp1 mitotic checkpoint complex). Slp1 is also the only APC/C coactivator essential for meiosis I.

## Subfamily Analysis

### PTHR19918:SF8 - FI02843P  *(ANCHOR SUBFAMILY; Cdc20/Fizzy branch)*
**Members**: 4+ of the 35 curated reference proteins (one of the largest subfamilies; several additional members appear with this assignment)

**Taxonomy**: The mitotic Cdc20/Fizzy clade across fungi, animals and plants.

**Key Members**:
- ***S. pombe* slp1 (P78972) - the anchor gene**
- *S. cerevisiae* CDC20 (P26309)
- *C. elegans* fzy-1 (Q09373)
- *Dictyostelium* cdc20 (Q54MZ3)
- Multiple *Arabidopsis* CDC20 cofactors (CDC20-1...CDC20-6: Q9SZA4, Q9S7I8, Q9S7H3, Q4PSE4, Q3E906, F4K5R6)

**Function**: Mitotic APC/C coactivator (Cdc20/Fizzy); substrate-recognition for securin and cyclin B at the metaphase-to-anaphase transition.

**Notes**: This is **slp1's subfamily**, confirmed from the UniProt record (`DR PANTHER; PTHR19918:SF8; FI02843P`). The cryptic name "FI02843P" is a sequence-derived label; functionally this is the Cdc20/Fizzy mitotic-activator clade. Note that *human* CDC20 (Q12834) is placed in the separate SF3 ("CELL DIVISION CYCLE PROTEIN 20 HOMOLOG"), so the Cdc20 orthology group is split across SF8 and SF3 in this family.

### PTHR19918:SF1 - FIZZY-RELATED PROTEIN HOMOLOG (Cdh1 branch)
**Members**: 7 proteins (largest subfamily)

**Key Members**: *S. pombe* srw1 (O13286), *S. cerevisiae* CDH1 (P53197), Human FZR1 (Q9UM11), Mouse Fzr1 (Q9R1K5), *Arabidopsis* FZR1 (Q8VZS9), *Dictyostelium* cdh1 (Q54KM3), *Medicago* CCS52A (Q9M7I2)

**Function**: Cdh1/Fizzy-related APC/C activator - late-mitosis/G1 and developmental APC/C substrate recognition (a distinct paralogous activity from the mitotic Cdc20 branch).

### PTHR19918:SF3 - CELL DIVISION CYCLE PROTEIN 20 HOMOLOG (metazoan Cdc20)
**Members**: 4 proteins

**Key Members**: Human CDC20 (Q12834), Mouse Cdc20 (Q9JJ66), Rat Cdc20 (Q62623), Pig CDC20 (Q5H7C0)

**Function**: Metazoan mitotic Cdc20 - same APC/C-activator role as slp1's SF8, in a separate orthology cluster.

### Other subfamilies
SF52 PROTEIN CORTEX (4; Lepidopteran/*Drosophila* meiotic activators), SF4 CDC20 HOMOLOG B (3-4; metazoan Cdc20B), SF5 AMA1 (2; meiosis-specific Ama1/mfr2), SF36 FIZZY-RELATED 3, SF61/SF63/SF66 (plant FZR / meiotic fizzy-related / uncharacterized). All are APC/C activators specialized to particular cell-cycle or meiotic stages.

## Functional Diversity Assessment

### Neo-functionalization: MODERATE (paralogous activators; conserved biochemistry)
The WD40-propeller / degron-recognition / APC/C-activation biochemistry is conserved family-wide. The major functional split is the **Cdc20/Fizzy (mitotic) vs Cdh1/Fizzy-related (G1/developmental) vs meiotic (Ama1/Cortex/Mfr)** specialization - a timing- and substrate-level diversification, not a change of mechanism. Slp1 is firmly in the mitotic Cdc20 branch.

## IBA Annotation Assessment

IBA annotations (GO_REF:0000033, node PTN000460086) propagated to slp1 (P78972).

| GO ID | Label | Aspect | Flags | Assessment |
|-------|-------|--------|-------|------------|
| GO:1990757 | ubiquitin ligase activator activity | MF | NO_UNIPROT_SEEDS | **APPROPRIATE.** This is slp1's curated core MF (APC/C activator). Family-defining function. |
| GO:0031145 | anaphase-promoting complex-dependent catabolic process | BP | CROSS_SUBFAMILY (SF1;SF3) | **APPROPRIATE.** CROSS_SUBFAMILY here is triage, not error: APC/C-dependent proteolysis is the shared function of all Cdc20/Cdh1 activators. slp1's curated core function. The seeds spanning SF1/SF3 are co-orthologs performing the same conserved process - correct to propagate. |
| GO:1905786 | positive regulation of anaphase-promoting complex-dependent catabolic process | BP | NO_UNIPROT_SEEDS | **APPROPRIATE.** slp1 positively activates the APC/C; consistent with curated function. |
| GO:0010997 | anaphase-promoting complex binding | MF | CROSS_SUBFAMILY (SF3) | **APPROPRIATE.** Binding the APC/C is required for all coactivators; the SF3 (human CDC20) seed is a true co-ortholog of slp1. CROSS_SUBFAMILY reflects the SF3/SF8 split of the Cdc20 group, not a wrong transfer. |
| GO:0005680 | anaphase-promoting complex | CC | LOCALIZATION; NO_UNIPROT_SEEDS | **APPROPRIATE.** slp1 transiently associates with / is a coactivator component of the APC/C; this localization is consistent with its biology (it binds the APC/C). No conflict. |

**Summary**: All five propagations are appropriate. The two `CROSS_SUBFAMILY` flags arise because the Cdc20 orthology group is split between SF8 (slp1, yeast CDC20) and SF3 (human CDC20), and because the broad APC/C-catabolic process is shared with the Cdh1/SF1 branch - both are genuinely conserved functions, so the triage flag does not indicate error. There is no inappropriate paralog-specific transfer (e.g. no Cdh1-specific G1/developmental term is wrongly forced onto slp1; the propagated terms are the generic APC/C-activator functions common to the whole family). Localization is consistent. Following the do-not-overrule principle and the calibrated rules, all IBA propagations to slp1 are endorsed.

## Key Literature

| PMID | Key Finding |
|------|-------------|
| PMID:26882497 | Slp1-APC/C-dependent ubiquitination of securin (Cut2); cohesin cleavage and sister separation downstream. |
| PMID:22437499 | Slp1/Cdc20 as the target of spindle-assembly-checkpoint inhibition (MCC). |

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER PTHR19918 metadata/entries, UniProt (P78972), slp1 ai-review, GOA IBA annotations, iba_propagation.tsv
