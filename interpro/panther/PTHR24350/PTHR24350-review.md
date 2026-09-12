# PANTHER Family Review: PTHR24350

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR24350 |
| **Family Name** | SERINE/THREONINE-PROTEIN KINASE IAL-RELATED (Aurora kinases) |
| **InterPro Entry** | IPR030616 |
| **Total Proteins** | 18,761 |
| **Taxonomic Breadth** | 10,290 taxa |
| **Subfamilies** | 14 |
| **Representative Structure** | 5orl (Aurora-A kinase in complex with an allosterically binding fragment) |
| **Anchor gene (S. pombe)** | ark1 (O59790), no subfamily assignment in UniProt/entries |

## Executive Summary

PTHR24350 is the **Aurora kinase** family (also "IAL-related", after the Ipl1/Aurora-like kinases): serine/threonine kinases (EC 2.7.11.1) that are central regulators of mitosis. Aurora kinases phosphorylate kinetochore, chromatin and spindle substrates to drive chromosome condensation, correct erroneous kinetochore-microtubule attachments, support the spindle-assembly checkpoint, and execute chromosome segregation and cytokinesis. The metazoan family has diversified into **Aurora A** (centrosome/spindle-pole; spindle assembly) and **Aurora B/C** (the catalytic subunit of the **Chromosomal Passenger Complex**, CPC), whereas most fungi and many protists have a **single Aurora** (Ipl1 in S. cerevisiae, Ark1 in S. pombe) that combines both roles.

Because the Aurora catalytic and CPC/mitotic functions are deeply conserved (calibration: ark1 Aurora-kinase function = expected correct), cross-subfamily IBA transfer of catalytic activity and core mitotic processes to the single fungal Aurora is normally appropriate. The main review risk is **Aurora A-specific spindle-pole/centrosome localization** terms, which in fungi map to the SPB and need not be the core annotation.

## Subfamily Analysis

Note: the PTHR24350 entries table in this repository does not carry per-member PANTHER subfamily (SFn) suffixes, so subfamilies are described here by gene-name clade (member counts from `PTHR24350-entries.csv`).

### Single-Aurora / Ipl1 clade (ANCHOR clade)
**Members**: e.g. S. pombe ark1 (O59790, anchor), S. cerevisiae IPL1 (P38991), Candida IPL1 (Q59S66), Kluyveromyces/Yarrowia/Debaryomyces IPL1 (Q6CWQ4, Q6C3J2, Q6BVA0), Dictyostelium aurK (Q54WX4), Trypanosoma AUK1 (Q384J7). Ipl1-named Aurora kinases are numerous among the fungal members.

**Function**: The single fungal/protist Aurora. **Ark1** is the catalytic subunit of the S. pombe CPC (with INCENP/Pic1, Survivin/Bir1, Borealin-like Nbl1); it concentrates at centromeres/kinetochores in early mitosis and relocates to the anaphase spindle midzone. It corrects syntelic/merotelic attachments to promote biorientation, contributes to checkpoint signaling, drives condensin loading and H3-Ser10 phosphorylation, and acts in chromosome segregation, cytokinesis and meiosis.

### Aurora A clade (AURKA)
**Members**: e.g. human AURKA (O14965), mouse Aurka (P97477), rat Aurka (P59241), Bos taurus AURKA (Q2TA06), dog AURKA (A0A8I3S724), Sus AURKA (A5GFW1).

**Function**: Centrosome/spindle-pole Aurora; mitotic entry, centrosome maturation and bipolar spindle assembly. Localizes to centrosomes and spindle microtubules.

### Aurora B clade (AURKB)
**Members**: e.g. human AURKB (Q96GD4), mouse Aurkb (O70126), rat Aurkb (O55099), zebrafish aurkb (Q6NW76), Xenopus aurkb (A4IGM9, Q6DE08), C. elegans air-2 (O01427).

**Function**: The metazoan CPC catalytic subunit - the closest functional counterpart of Ark1; chromosome biorientation, error correction, spindle-midzone and cytokinesis functions.

### Aurora C clade (AURKC)
**Members**: human AURKC (Q9UQB9), mouse Aurkc (O88445).

**Function**: Germline-enriched CPC kinase (meiosis); paralog of Aurora B in mammals.

### Plant Aurora and divergent kinases
**Members**: Arabidopsis AUR2 (Q683C9), AUR3 (O64629); and divergent, non-Aurora kinases that fall in this family in some clades - S. cerevisiae TOS3 (P43637), RAD53 (P22216), YPL150W (Q12152).

**Function**: Plant Aurora kinases (AUR1-3) perform mitotic/cytokinetic roles. The TOS3/RAD53/YPL150W members are more diverged (e.g. RAD53 is a DNA-damage checkpoint kinase) and represent boundary cases where Aurora-specific process terms should not be transferred.

## Functional Diversity Assessment

- **Conserved across the Aurora core (Ipl1/AURKB/AURKC and AURKA):** protein serine/threonine kinase activity, ATP binding, chromosome-passenger/centromere localization, and mitotic chromosome segregation/cytokinesis processes.
- **Diverged:** Aurora A's centrosome-maturation/spindle-pole specialization (metazoa), germline AURKC (meiosis), and divergent fungal kinases (TOS3/RAD53) that are not true Aurora orthologs.

## IBA Annotation Assessment

Seven IBA (GO_REF:0000033) annotations were propagated to **ark1 (O59790)**. Because ark1 has **no PANTHER subfamily assignment** here, all carry `GENE_NO_SUBFAMILY`; several also carry `LOCALIZATION`. Per calibration, the Aurora catalytic/CPC core is expected correct, so the review accepts the CPC-defining terms and down-weights generic/spindle-pole localizations to non-core.

| GO ID | Label | Aspect | Node | Seeds | Our action |
|-------|-------|--------|------|-------|------------|
| GO:0032133 | chromosome passenger complex | CC | PTN000681967 | 3 | **ACCEPT** |
| GO:0051233 | spindle midzone | CC | PTN000681967 | 2 | **ACCEPT** |
| GO:0000776 | kinetochore | CC | PTN000681968 | 1 | **ACCEPT** |
| GO:0007052 | mitotic spindle organization | BP | PTN000681967 | 3 | **KEEP_AS_NON_CORE** |
| GO:0032465 | regulation of cytokinesis | BP | PTN000681967 | 3 | **KEEP_AS_NON_CORE** |
| GO:0000922 | spindle pole | CC | PTN000681968 | 4 | **KEEP_AS_NON_CORE** |
| GO:0005876 | spindle microtubule | CC | PTN000681967 | 2 | **KEEP_AS_NON_CORE** |

**GO:0032133 (chromosome passenger complex) - ACCEPT.** This is the defining localization of Ark1 (it has a direct experimental annotation; the IBA seeds include FB, MGI, SGD and Aurora B/C UniProt entries). Strongly correct and core for the single fungal Aurora.

**GO:0051233 (spindle midzone) and GO:0000776 (kinetochore) - ACCEPT.** Both match the established CPC dynamics of Ark1 (centromere/kinetochore in early mitosis, midzone at anaphase). Conserved, paralog-appropriate localizations.

**GO:0007052 (mitotic spindle organization) and GO:0032465 (regulation of cytokinesis) - KEEP_AS_NON_CORE.** These are real Aurora-associated processes and consistent with Ark1 biology, but they are downstream/secondary relative to the kinase's core error-correction and CPC functions; retained as non-core.

**GO:0000922 (spindle pole) and GO:0005876 (spindle microtubule) - KEEP_AS_NON_CORE.** These are the localizations most characteristic of the **Aurora A** branch (centrosome/spindle pole). For the single fungal Aurora the SPB/spindle is plausible but not the primary, experimentally foregrounded location (centromere/kinetochore -> midzone). Rather than remove them - the spindle is part of Aurora biology and the transfer is not a paralog error - they are kept as non-core, flagging that the spindle-pole emphasis derives partly from the Aurora A clade.

**Calibration note.** No CPC/Aurora catalytic term was removed; this is the expected-correct case for a conserved Aurora kinase. The only adjustments are demoting generic spindle/cytokinesis-process and Aurora-A-leaning spindle-pole localizations to non-core, not asserting any paralog mis-attribution.

## Key Considerations for Curators

1. CPC membership, centromere/kinetochore and midzone localization, and Aurora catalytic activity are conserved and core for single-Aurora fungal members.
2. Spindle-pole/spindle-microtubule localization is weighted toward the Aurora A branch; treat as non-core for combined single-Aurora kinases.
3. Divergent members (TOS3, RAD53, YPL150W) are not true Aurora orthologs - do not propagate Aurora-specific process terms to them.

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, S. pombe ark1 curated review, GOA IBA annotations, PANTHER_IBA_REVIEW propagation table
