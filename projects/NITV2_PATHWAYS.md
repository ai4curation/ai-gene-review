# Nitratidesulfovibrio vulgaris Pathways Project

## Overview

This project focuses on reviewing gene annotations for key pathways in *Nitratidesulfovibrio vulgaris* (formerly *Desulfovibrio vulgaris*, strain Hildenborough). This sulfate-reducing bacterium is a model organism for studying anaerobic respiration using sulfate as the terminal electron acceptor.

## Model Organism

**Species:** *Nitratidesulfovibrio vulgaris* (strain Hildenborough)

- UniProt species code: DESVH (note: still uses old *Desulfovibrio vulgaris* code)
- NCBI Taxonomy ID: 882
- Genome: NC_002937.3
- Key metabolism: Dissimilatory sulfate reduction, hydrogen cycling

## Pathway 1: Sulfate Reduction

The dissimilatory sulfate reduction pathway is the core energy metabolism of this organism. Sulfate is reduced to sulfide in a multi-step process:

1. **Sulfate uptake** - via sulfate permeases
2. **Sulfate activation** - ATP sulfurylase generates adenylyl-sulfate (APS)
3. **APS reduction** - APS reductase (AprAB) reduces APS to sulfite
4. **Electron transfer** - QmoABC complex links APS reduction to quinone pool

### Genes for Review

| Locus     | Gene   | UniProt ID | Protein                                           |
|-----------|--------|------------|---------------------------------------------------|
| DVU0846   | aprB   | Q72DT3     | Adenylylsulfate reductase, beta subunit           |
| DVU0847   | aprA   | Q72DT2     | Adenylylsulfate reductase, alpha subunit          |
| DVU0848   | qmoA   | Q72DT1     | Quinone-interacting membrane-bound oxidoreductase |
| DVU0849   | qmoB   | Q72DT0     | Quinone-interacting membrane-bound oxidoreductase |
| DVU0850   | qmoC   | Q72DS9     | Quinone-interacting membrane-bound oxidoreductase |
| DVU0279   |        | Q72FD5     | Sulfate permease family protein                   |

## Pathway 2: Potassium Transport

Potassium homeostasis is critical for maintaining membrane potential and osmotic balance.

### Genes for Review

| Locus     | Gene   | UniProt ID | Protein                                           |
|-----------|--------|------------|---------------------------------------------------|
| DVU1606   |        | Q72BM9     | Potassium uptake protein, TrkA family             |
| DVU3335   |        | Q725U0     | Sensory box histidine kinase                      |
| DVU3336   | kdpD   | Q725T9     | Potassium channel histidine kinase domain protein |
| DVU3337   | kdpC   | Q725T8     | Potassium-transporting ATPase, C subunit          |
| DVU3338   | kdpB   | Q725T7     | Potassium-transporting ATPase, B subunit (ATP-binding) |
| DVU0412   |        | Q72F06     | Potassium uptake protein TrkA, putative           |
| DVU0413   | trkH   | Q72F05     | Potassium uptake protein, TrkH family             |

## Pathway 3: Sigma Factors

Sigma factors regulate gene expression by directing RNA polymerase to specific promoters.

### Genes for Review

| Locus     | Gene   | UniProt ID | Protein                                           |
|-----------|--------|------------|---------------------------------------------------|
| DVU1584   | rpoH   | Q72BQ0     | RNA polymerase sigma-70 factor (heat shock)       |
| DVU1628   | rpoN   | Q72BK7     | RNA polymerase sigma-54 factor                    |
| DVU1788   | rpoD   | Q72B50     | RNA polymerase sigma-70 factor (housekeeping)     |
| DVU2929   | rpoC   | Q727C6     | DNA-directed RNA polymerase, beta prime subunit   |
| DVU3229   | fliA   | Q726C4     | RNA polymerase sigma factor for flagellar operon  |

## Pathway 4: Hydrogen Metabolism

D. vulgaris Hildenborough possesses multiple hydrogenases for hydrogen cycling, which is central to its energy metabolism. The organism has four periplasmic hydrogenases for H2 uptake and two membrane-bound cytoplasmic hydrogenases for H2 production.

### Periplasmic Hydrogenases (H2 Uptake)

| Locus     | Gene   | UniProt ID | Protein                                           |
|-----------|--------|------------|---------------------------------------------------|
| DVU1769   | hydA   | P07598     | [Fe] hydrogenase large subunit                    |
| DVU1770   | hydB   | P07603     | [Fe] hydrogenase small subunit                    |
| DVU1917   | hysB   | Q72AS4     | [NiFeSe] hydrogenase small subunit                |
| DVU1918   | hysA   | Q72AS3     | [NiFeSe] hydrogenase large subunit                |
| DVU1921   | hynB1  | Q06173     | [NiFe] hydrogenase 1 small subunit                |
| DVU1922   | hynA1  | Q72AS0     | [NiFe] hydrogenase 1 large subunit                |

### Membrane-Bound Cytoplasmic Hydrogenases (H2 Production)

| Locus     | Gene   | UniProt ID | Protein                                           |
|-----------|--------|------------|---------------------------------------------------|
| DVU0434   | echA   | Q72EY4     | Ech hydrogenase, subunit EchA (catalytic)         |
| DVU0433   | echB   | Q72EY5     | Ech hydrogenase, subunit EchB                     |
| DVU2291   | cooH   | Q729Q8     | Coo hydrogenase, CooH subunit (catalytic)         |
| DVU2287   | cooK   | Q729R2     | Coo hydrogenase, CooK subunit (selenocysteine)    |

### Genes for Initial Review (Representative Subunits)

| Locus     | Gene   | UniProt ID | Protein                                           |
|-----------|--------|------------|---------------------------------------------------|
| DVU1769   | hydA   | P07598     | [Fe] hydrogenase large subunit (catalytic)        |
| DVU1918   | hysA   | Q72AS3     | [NiFeSe] hydrogenase large subunit (catalytic)    |
| DVU1922   | hynA1  | Q72AS0     | [NiFe] hydrogenase 1 large subunit (catalytic)    |
| DVU0434   | echA   | Q72EY4     | Ech hydrogenase, subunit EchA (catalytic)         |
| DVU2291   | cooH   | Q729Q8     | Coo hydrogenase, CooH subunit (catalytic)         |

## Key References

- [Genome of D. vulgaris Hildenborough (PMID:15077118)](https://pubmed.ncbi.nlm.nih.gov/15077118/)
- [Sulfate reduction pathway review (PMID:24106043)](https://pubmed.ncbi.nlm.nih.gov/24106043/)
- [QmoABC complex characterization (PMID:15304518)](https://pubmed.ncbi.nlm.nih.gov/15304518/)
- [Function of Periplasmic Hydrogenases (PMID:17586632)](https://pubmed.ncbi.nlm.nih.gov/17586632/)
- [NiFeSe hydrogenase characterization (PMID:16187073)](https://pubmed.ncbi.nlm.nih.gov/16187073/)
- [Fe-only hydrogenase deletion effects (PMID:11790737)](https://pubmed.ncbi.nlm.nih.gov/11790737/)

---
# STATUS

## Sulfate Reduction Pathway (Priority 1) - COMPLETED
- [x] aprB (Q72DT3) - APS reductase beta subunit (electron transfer)
- [x] aprA (Q72DT2) - APS reductase alpha subunit (catalytic FAD-containing)
- [x] qmoA (Q72DT1) - HdrA-like electron bifurcating subunit (note: NOT QmoA)
- [x] qmoB (Q72DT0) - HdrA/FAD-containing bifurcating subunit
- [x] qmoC (Q72DS9) - Membrane subunit of QmoABC complex
- [x] DVU0279 (Q72FD5) - SulP/SLC26 family transporter (likely dicarboxylate, not sulfate)

## Sigma Factors (Priority 3) - COMPLETED
- [x] rpoH (Q72BQ0) - Sigma-32 heat shock factor (RpoH)
- [x] rpoN (Q72BK7) - Sigma-54 factor (RpoN)
- [x] rpoD (Q72B50) - Sigma-70 housekeeping factor (RpoD)
- [x] rpoC (Q727C6) - RNA polymerase beta' subunit (NOT a sigma factor!)
- [x] fliA (Q726C4) - Sigma-28 flagellar factor (FliA)

## Potassium Transport (Priority 2) - COMPLETED
- [x] DVU1606 (Q72BM9) - TrkA family RCK regulatory subunit
- [x] DVU3335 (Q725U0) - KdpD-associated histidine kinase sensor
- [x] kdpD (Q725T9) - KdpD tandem kinase (His + Ser kinase)
- [x] kdpC (Q725T8) - KdpC catalytic chaperone subunit
- [x] kdpB (Q725T7) - KdpB P-type ATPase catalytic subunit
- [x] DVU0412 (Q72F06) - TrkA-type RCK regulatory subunit
- [x] trkH (Q72F05) - TrkH membrane channel pore

## Hydrogen Metabolism (Priority 4) - IN PROGRESS
- [ ] hydA (P07598) - [Fe] hydrogenase large subunit (periplasmic)
- [ ] hysA (Q72AS3) - [NiFeSe] hydrogenase large subunit (periplasmic)
- [ ] hynA1 (Q72AS0) - [NiFe] hydrogenase 1 large subunit (periplasmic)
- [ ] echA (Q72EY4) - Ech hydrogenase subunit A (cytoplasmic membrane-bound)
- [ ] cooH (Q729Q8) - Coo hydrogenase CooH subunit (cytoplasmic membrane-bound)

# NOTES

## 2026-01-15

**Project created.** Compiled gene list for three pathways in *Nitratidesulfovibrio vulgaris* (Hildenborough):

1. **Sulfate reduction pathway** (6 genes) - Core energy metabolism
   - APS reductase complex (AprAB): DVU0846-0847
   - QmoABC complex: DVU0848-0850
   - Sulfate permease: DVU0279

2. **Potassium transport** (7 genes) - Ion homeostasis
   - TrkA/TrkH systems: DVU0412-0413, DVU1606
   - Kdp system (ATP-driven): DVU3336-3338
   - Regulatory kinase: DVU3335

3. **Sigma factors** (5 genes) - Transcriptional regulation
   - Housekeeping (RpoD), heat shock (RpoH), nitrogen (RpoN), flagellar (FliA)
   - Note: RpoC is RNA polymerase subunit, not a sigma factor

**Priority:** Start with sulfate reduction pathway as this is the defining metabolic feature of this organism.

All UniProt IDs retrieved from UniProt REST API using DVU locus tags. Note that the organism name has been updated from *Desulfovibrio vulgaris* to *Nitratidesulfovibrio vulgaris* but UniProt IDs remain valid.

**Sulfate Reduction Pathway Reviews Completed:**

Key findings from annotation reviews:

1. **AprAB (APS Reductase)**:
   - **aprB (Q72DT3)**: Beta subunit with two [4Fe-4S] clusters. Core function is electron transfer (GO:0009055), not catalytic activity. Modified GO:0009973 (adenylyl-sulfate reductase activity) to electron transfer activity since AprB is the electron relay, not the catalytic subunit.
   - **aprA (Q72DT2)**: Alpha subunit containing FAD. This is the catalytic subunit. Accepted GO:0009973 (adenylyl-sulfate reductase activity). Added GO:0019420 (dissimilatory sulfate reduction).

2. **DVU0848-0850 (NOT QmoABC!)**:
   - **CRITICAL FINDING**: DVU0848-0850 are actually part of the **FlxABCD-HdrABC electron bifurcating complex**, NOT the QmoABC complex as initially annotated in the input list.
   - **DVU0848 (Q72DT1)**: HdrA-like protein with FAD/NAD-binding domains. Functions in electron bifurcation, coupling NADH oxidation with ferredoxin reduction. Essential for ethanol metabolism.
   - **DVU0849 (Q72DT0)**: HdrA/FAD-containing subunit of the Flx-Hdr complex.
   - **DVU0850 (Q72DS9)**: This IS QmoC - the membrane-integral subunit with heme b groups that transfers electrons from the quinone pool. Part of the actual QmoABC complex.

3. **DVU0279 (Q72FD5) - Sulfate Permease?**:
   - **ANNOTATION CONCERN**: Despite being annotated as "sulfate permease family protein", the SulP/SLC26 family is functionally diverse. Many members transport dicarboxylates, bicarbonate, or other anions rather than sulfate. The annotation GO:0055085 (transmembrane transport) was accepted but sulfate-specific transport needs experimental verification.

**Sigma Factor Pathway Reviews Completed:**

Key findings from annotation reviews:

1. **rpoC (Q727C6) is NOT a sigma factor**:
   - **CRITICAL CORRECTION**: rpoC encodes the RNA polymerase beta' (β') subunit, which is the DNA-binding core subunit of RNAP - NOT a sigma factor. This was incorrectly listed in the original gene set. RpoC provides DNA template binding and forms part of the catalytic core enzyme.

2. **Sigma factor family classification**:
   - **rpoH (Q72BQ0)**: Sigma-32 family (σ32), heat shock response
   - **rpoN (Q72BK7)**: Sigma-54 family (σ54), nitrogen regulation and alternative metabolism
   - **rpoD (Q72B50)**: Sigma-70 family (σ70), housekeeping transcription
   - **fliA (Q726C4)**: Sigma-28 family (σ28), flagellar gene expression

3. **Over-annotation patterns**:
   - Many sigma factors had GO:0003700 (DNA-binding transcription factor activity) which is incorrect - sigma factors recognize promoters but do not bind DNA themselves; the DNA-binding is performed by the RNAP core enzyme.
   - Proposed replacement with GO:0016987 (sigma factor activity).

**Potassium Transport Pathway Reviews Completed:**

Key findings from annotation reviews:

1. **Two distinct K+ transport systems identified**:
   - **KdpFABC system** (DVU3335-3338): High-affinity ATP-driven K+ pump induced under K+ limitation
   - **Trk/Ktr system** (DVU0412-0413, DVU1606): Constitutive K+ uptake channels

2. **KdpFABC Complex - Functional assignments**:
   - **kdpB (Q725T7)**: P-type ATPase motor - the ONLY subunit with catalytic activity. Contains the catalytic aspartate D307 that cycles through phosphorylation. Annotated with GO:0008556 (P-type K+ transporter activity).
   - **kdpC (Q725T8)**: Catalytic chaperone - does NOT have ATPase activity! Incorrectly annotated with ATP binding and hydrolase activity. Its actual function is GO:0001671 (ATPase activator activity) - it increases KdpB's ATP-binding affinity.
   - **kdpD (Q725T9)**: Tandem serine-histidine kinase sensor that controls KdpFABC expression in response to K+ levels and turgor.
   - **DVU3335 (Q725U0)**: KdpE-like response regulator partnered with KdpD for two-component signaling.

3. **Trk/Ktr System - Pore vs Regulator distinction**:
   - **trkH (Q72F05)**: Membrane channel pore - this is the actual K+ transporter with transmembrane domains.
   - **DVU0412 (Q72F06)** and **DVU1606 (Q72BM9)**: Cytosolic RCK (regulator of K+ conductance) regulatory subunits. These do NOT transport ions themselves - they form octameric gating rings that regulate the TrkH channel through ATP/ADP-dependent conformational changes.
   - **Key correction**: Both TrkA proteins were incorrectly annotated with GO:0008324 (transporter activity). They should have GO:0015459 (potassium channel regulator activity).

4. **c-di-AMP signaling**:
   - The second messenger c-di-AMP binds to RCK regulatory subunits to modulate K+ uptake capacity, linking potassium homeostasis to broader cellular signaling networks.
