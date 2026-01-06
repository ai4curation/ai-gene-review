# TOR1 GO Annotation Curation Summary

## Overview
Comprehensive curation review of 79 GO annotations for yeast TOR1 (P35169), the serine/threonine kinase and core component of TORC1 complex.

## Curation Statistics

| Category | Count | Action | Rationale |
|----------|-------|--------|-----------|
| **MOLECULAR FUNCTIONS** | | | |
| Kinase catalytic activity | 5 | ACCEPT | GO:0004674 (IBA, IDA x3), GO:0004672 (EXP, IMP), GO:0106310 (IEA). Core function. |
| Nucleotide/ATP binding | 3 | ACCEPT | GO:0000166, GO:0005524, GO:0016301. Essential cofactor binding for kinase. |
| Transferase activity | 1 | ACCEPT | GO:0016740. Phosphoryl transfer mechanism. |
| Complex binding | 1 | ACCEPT | GO:0044877. FRB domain mediates FKBP-rapamycin binding. |
| **Protein binding (generic)** | **15** | **MARK_AS_OVER_ANNOTATED** | Generic GO:0005515 from multiple IPI sources redundant with GO:0031931 (TORC1 complex) and GO:0044877 (complex binding) |
| **CELLULAR COMPONENTS** | | | |
| Nucleus | 2 | ACCEPT | GO:0005634 (IBA, IDA). TOR1 translocates to nucleus for rDNA transcription control. |
| Cytoplasm | 3 | ACCEPT | GO:0005737 (IBA, IDA x2). Core subcellular location. |
| Vacuolar membrane | 5 | ACCEPT | GO:0000329 (IEA, IDA x4, HDA). Critical for TORC1 nutrient sensing. |
| Plasma membrane | 2 | ACCEPT | GO:0005886 (IEA, IDA). TOR1 peripheral membrane protein. |
| Vacuole membrane | 1 | ACCEPT | GO:0005774 (IEA). Parent term to fungal-type vacuole. |
| Golgi membrane | 1 | ACCEPT | GO:0000139 (IDA). TOR1 localizes to multiple membrane compartments. |
| Endosome membrane | 1 | ACCEPT | GO:0010008 (IDA). Nutrient sensing from endosomal compartments. |
| **COMPLEX MEMBERSHIP** | | | |
| TOR complex | 1 | ACCEPT | GO:0038201 (IBA). TOR1 core component. |
| TORC1 complex | 2 | ACCEPT | GO:0031931 (IEA, IPI). Core TORC1 component (TOR1, KOG1, LST8, TCO89). |
| **BIOLOGICAL PROCESSES** | | | |
| TORC1/TOR signaling | 5 | ACCEPT | GO:0038202 (IBA), GO:0031929 (IEA, NAS, IMP x2). Core pathway. |
| Nutrient response | 1 | ACCEPT | GO:0007584 (NAS). TOR1 master nutrient sensor. |
| Nitrogen starvation response | 2 | ACCEPT | GO:0006995 (IEA, IGI). TORC1 controls autophagy/anabolic responses to N-availability. |
| Autophagy inhibition | 3 | ACCEPT | GO:0016242 (IBA), GO:0010507 (IEA, IGI). Core TORC1 output. |
| Translation initiation | 1 | ACCEPT | GO:0006413 (IMP). TOR loss blocks translation initiation. |
| Ribosome biogenesis | 2 | ACCEPT | GO:0042254 (IEA, IMP). Major TORC1 function (rRNA synthesis, r-protein transcription). |
| rRNA transcription | 1 | ACCEPT | GO:0042790 (IMP). TOR1 nuclear localization regulates rDNA. |
| S6 phosphorylation | 1 | ACCEPT | GO:0018105 (IDA). Major translation control output via ribosomal protein S6. |
| Cell growth regulation | 1 | ACCEPT | GO:0001558 (NAS). Master regulator of growth. |
| Cell cycle regulation | 2 | ACCEPT | GO:0051726 (NAS, IMP). Controls G1/S progression. |
| Meiotic cell cycle | 1 | ACCEPT | GO:0051321 (IMP). TOR kinase activity required for meiosis. |
| **STRESS RESPONSES** | 3-4 | KEEP_AS_NON_CORE | GO:0034976, GO:0034599, GO:0034605, GO:0006974. Peripheral to primary nutrient sensing. |
| **BIOSYNTHETIC PROCESSES** | 3 | KEEP_AS_NON_CORE | GO:0031505 (cell wall), GO:0090153 (sphingolipids), GO:1905356 (snRNA modification). Downstream outputs. |
| **MITOCHONDRIAL SIGNALING** | 1 | KEEP_AS_NON_CORE | GO:0031930 (RTG retrograde). Specific nutrient-dependent output. |

## Detailed Curation Decisions

### ACCEPT Annotations (60 annotations)

#### Molecular Functions - Kinase Activity
All kinase activity annotations should be accepted as they represent core function:
- **GO:0004674** (protein serine/threonine kinase activity): IBA, IEA, IDA(3)
  - Core activity with EC 2.7.11.1 confirmation in UniProt
  - Experimental evidence from PMID:38127619, PMID:36691768, PMID:26582391

- **GO:0004672** (protein kinase activity): EXP, IMP
  - EXP from PMID:18270585
  - IMP from Tap42 phosphorylation (PMID:10329624)

- **GO:0106310** (protein serine kinase activity): IEA
  - Rhea-based mapping for serine-specific phosphorylation

All kinase related terms are core functions.

#### Nucleotide and Cofactor Binding
- **GO:0000166** (nucleotide binding): IEA
- **GO:0005524** (ATP binding): IEA
- **GO:0016301** (kinase activity): IEA
- **GO:0016740** (transferase activity): IEA

These are essential for kinase function and should be accepted.

#### Cellular Localization

**Nucleus** - ACCEPT
- GO:0005634: IBA, IDA(2)
- Evidence: PMID:16900101 demonstrates nuclear translocation and rDNA association in response to nutrients
- Function: Nuclear localization required for ribosomal protein gene transcription control

**Cytoplasm** - ACCEPT
- GO:0005737: IBA, IDA(2)
- Evidence: Multiple observations of cytoplasmic TOR1 localization
- Function: Primary site of TORC1 complex assembly and signaling

**Vacuolar Membrane** - ACCEPT
- GO:0000329: IEA, IDA(4), HDA
- Evidence: PMID:25046117, PMID:19748353, PMID:18723607, PMID:12719473
- Function: Critical site for amino acid sensing via EGO complex and PIB2 glutamine sensor

**Plasma Membrane** - ACCEPT
- GO:0005886: IEA, IDA
- Evidence: PMID:10973982 shows TOR2 (TOR1-related) plasma membrane localization via HEAT repeats
- Function: TORC1 can sense growth factors at plasma membrane

**Other Compartments** - ACCEPT
- GO:0005774 (vacuolar membrane): IEA - parent term
- GO:0000139 (Golgi membrane): IDA - nutrient sensing from multiple compartments
- GO:0010008 (endosome membrane): IDA - endosomal nutrient sensing

#### TORC1 Complex Membership - ACCEPT

- **GO:0038201** (TOR complex): IBA
- **GO:0031931** (TORC1 complex): IEA, IPI (PMID:12408816)

Evidence: PMID:12408816 seminal paper identifying TORC1 composition: TOR1/TOR2 + KOG1 + LST8 [+ TCO89]

#### Major Biological Processes - ACCEPT

**TORC1/TOR Signaling** - ACCEPT (multiple annotations, all core)
- GO:0038202 (TORC1 signaling): IBA
- GO:0031929 (TOR signaling): IEA, NAS, IMP(2)
- These are the primary pathway controlled by TOR1

**Nutrient Sensing** - ACCEPT
- GO:0006995 (cellular response to nitrogen starvation): IEA, IGI
- GO:0007584 (response to nutrient): NAS
- Evidence: PMID:9461583 - foundational autophagy control paper
- TOR1 acts as nutrient availability sensor

**Autophagy Regulation** - ACCEPT (core function)
- GO:0016242 (negative regulation of macroautophagy): IBA
- GO:0010507 (negative regulation of autophagy): IEA, IGI
- Evidence: PMID:9461583 classic paper demonstrating TOR inhibits autophagy
- Under nutrient-rich conditions, TORC1 suppresses autophagy

**Protein Synthesis Regulation** - ACCEPT
- GO:0006413 (translational initiation): IMP (PMID:8741837)
- Evidence: TOR loss causes block of translation initiation
- GO:0042254 (ribosome biogenesis): IEA, IMP (PMID:10198052)
- Evidence: PMID:10198052 demonstrates TOR controls rRNA transcription, r-protein gene expression, rRNA processing
- GO:0042790 (nucleolar large rRNA transcription): IMP (PMID:16900101)
- Evidence: TOR1 translocates to nucleus and associates with rDNA promoters
- GO:0018105 (peptidyl-serine phosphorylation): IDA (PMID:26582391)
- Evidence: Direct phosphorylation of ribosomal protein S6

**Cell Growth and Cycle Control** - ACCEPT
- GO:0001558 (regulation of cell growth): NAS
- GO:0051726 (regulation of cell cycle): NAS, IMP (PMID:8741837)
- GO:0051321 (meiotic cell cycle): IMP (PMID:9096347)
- Evidence: TOR depletion arrests cells in G1; rapamycin similarly blocks growth
- TOR kinase activity required for meiotic progression

---

### KEEP_AS_NON_CORE Annotations (7-8 annotations)

These annotations are likely correct but represent peripheral functions rather than core TOR1 roles:

**Stress Responses**
- GO:0034976 (response to ER stress): IMP (PMID:31144305)
  - Hyperactive TORC1 sensitizes to ER stress
  - Reason: TOR is sensor, but ER stress response is secondary

- GO:0034599 (cellular response to oxidative stress): IGI (PMID:27922823)
- GO:0034605 (cellular response to heat): IGI (PMID:27922823)
  - Via Slm35-TOR-longevity link
  - Reason: Peripheral stress adaptation via TOR, not primary function

- GO:0006974 (DNA damage response): IMP (PMID:17698581)
  - TOR as survival checkpoint
  - Reason: Secondary to primary nutrient sensing

**Biosynthetic Processes**
- GO:0031505 (fungal-type cell wall organization): IMP (PMID:14736892)
  - TORC1 controls cell wall integrity via Ssd1p
  - Reason: Downstream anabolic output, not core function

- GO:0090153 (regulation of sphingolipid biosynthesis): IMP (PMID:23363605)
  - TORC1 phosphorylates Npr1, which phosphorylates Orm
  - Reason: Specific lipid biosynthesis output of nutrient sensing

- GO:1905356 (regulation of snRNA pseudouridine synthesis): IEA, IGI
  - TOR-dependent ribosome biogenesis output
  - Reason: Specific ribosomal modification, consequence not core driver

**Retrograde Signaling**
- GO:0031930 (mitochondria-nucleus signaling pathway): IMP (PMID:11997479)
  - TOR controls RTG1/RTG3 nuclear localization
  - Reason: Specific downstream output of amino acid sensing

---

### MARK_AS_OVER_ANNOTATED Annotations (15 annotations)

**Generic "Protein Binding" Annotations (GO:0005515)**

All IPI annotations for generic GO:0005515 should be marked as over-annotated:

From IntAct database with PMIDs:
- PMID:12408816: FPR1, KOG1, LST8
- PMID:14736892: KOG1, LST8, TCO89
- PMID:16429126: (generic interaction screen)
- PMID:16554755: (generic interaction screen)
- PMID:18812505: FPR1 (superoxide-TORC1 interaction)
- PMID:20489023: multiple partners (NPR1, MKS1, KSP1, NNK1, FMP48, SKY1, TCO89)

**Rationale for Over-Annotation:**

1. **GO Curation Best Practices**: Generic "protein binding" (GO:0005515) is discouraged because it is uninformative without mechanistic detail.

2. **Redundancy with Existing Annotations**:
   - TORC1 complex membership is captured by: **GO:0031931** (TORC1 complex, part_of relation)
   - FKBP-rapamycin binding is captured by: **GO:0044877** (protein-containing complex binding, enables relation)

3. **Information Loss**: Multiple partner-specific IPI annotations collapse into single generic term. Better to use:
   - **GO:0031931** (TORC1 complex) for core complex members (KOG1, LST8, TCO89)
   - **GO:0044877** (protein-containing complex binding) for FBP-rapamycin interaction
   - Or define more specific MF terms if available (e.g., "rapamycin-binding activity")

4. **Solution**: Consolidate these 15 IPI/GO:0005515 annotations. Retain the more informative:
   - GO:0031931 (TORC1 complex): captures core component interactions
   - GO:0044877 (protein-containing complex binding): captures FKBP interaction

**Conclusion**: The 15 generic protein binding annotations should be marked as OVER_ANNOTATED and consolidated into more specific functional annotations already present.

---

## Summary by Evidence Code Quality

| Evidence | Count | Quality | Retention |
|----------|-------|---------|-----------|
| IBA | ~10 | High (phylogenetic) | ACCEPT |
| IDA | ~20 | High (direct observation) | ACCEPT |
| IMP | ~20 | High (mutant phenotype) | ACCEPT/NON-CORE |
| IGI | ~8 | Medium-High (genetic interaction) | ACCEPT/NON-CORE |
| IPI | ~15 | Medium (interaction) | MARK_AS_OVER_ANNOTATED |
| IEA | ~12 | Medium (electronic) | ACCEPT |
| EXP | 1 | High (experimental) | ACCEPT |
| NAS | 4 | Low (non-traceable) | ACCEPT |
| HDA | 1 | Low (homology) | ACCEPT |

---

## Core Functions Summary

**Primary Functions (ACCEPT - absolutely essential)**:
1. Serine/threonine kinase activity (GO:0004674)
2. ATP binding (GO:0005524)
3. TORC1 complex membership (GO:0031931)
4. TORC1 signaling pathway (GO:0038202)
5. Negative regulation of autophagy (GO:0016242, GO:0010507)
6. Ribosome biogenesis control (GO:0042254)
7. Translation initiation control (GO:0006413)
8. Nutrient sensing (GO:0007584, GO:0006995)
9. Cell growth regulation (GO:0001558)
10. Cell cycle regulation (GO:0051726)

**Supporting Localizations (ACCEPT)**:
- Vacuolar membrane (GO:0000329) - nutrient sensing
- Nucleus (GO:0005634) - rDNA transcription
- Cytoplasm (GO:0005737) - signaling hub
- Plasma membrane (GO:0005886) - growth factor sensing

**Peripheral but Retained (KEEP_AS_NON_CORE)**:
- Stress responses (ER, oxidative, heat)
- Cell wall and sphingolipid biosynthesis
- Meiotic cell cycle
- Mitochondrial retrograde signaling

**To Remove/Consolidate (MARK_AS_OVER_ANNOTATED)**:
- 15 generic GO:0005515 (protein binding) annotations - redundant with GO:0031931 and GO:0044877

---

## Recommendations for GO Annotation Improvement

1. **Consolidate protein binding**: Replace 15 GO:0005515 annotations with existing complex membership (GO:0031931) and complex binding (GO:0044877) terms.

2. **Add missing annotations**: Consider additions for:
   - TORC1-specific substrate binding (Tap42, Sch9, Ypk3, Stm1)
   - Amino acid sensing specificity (glutamine, leucine, cysteine)
   - Rapamycin resistance mechanism

3. **Standardize evidence**: Multiple evidence codes for same term (e.g., GO:0004674 has IBA + IEA + IDA) is appropriate and reflects multi-method confirmation.

4. **Improve specificity**: Where possible, use specific transactivation terms rather than generic "regulation of" terms.

---

## References for Major Claims

- **TORC1 Complex Discovery**: PMID:12408816
- **Autophagy Control**: PMID:9461583
- **Nutrient Sensing - Nitrogen**: PMID:9461583
- **Translation Initiation**: PMID:8741837
- **Ribosome Biogenesis**: PMID:10198052
- **Tap42 Phosphorylation**: PMID:10329624
- **Nuclear Localization/rDNA**: PMID:16900101
- **Meiotic Function**: PMID:9096347
- **S6 Phosphorylation**: PMID:26582391
- **Stm1/Ribosome Preservation**: PMID:36691768
- **Glutamine Sensing**: PMID:38127619, PMID:34535752

