# Cellulosome Project

## Overview

The cellulosome is a large extracellular multi-enzyme complex produced by anaerobic cellulolytic bacteria for efficient degradation of plant cell wall polysaccharides. It represents one of the most efficient natural systems for degrading crystalline cellulose and lignocellulosic biomass.

## Model Species Selection

**Primary model: *Acetivibrio thermocellus*** (formerly *Clostridium thermocellum*, also known as *Ruminiclostridium thermocellum* and *Hungateiclostridium thermocellum*)

- UniProt species code: ACET2 (or use taxonomy ID: 1515)
- The original organism in which cellulosomes were discovered (as "cellulose-binding factor")
- Best characterized cellulosome system with extensive structural and biochemical data
- ~79 cellulosomal genes including scaffoldins and dockerin-containing enzymes
- Thermophilic (optimal growth ~60°C) - industrially relevant
- Good UniProt coverage with many Swiss-Prot reviewed entries

**Alternative model: *Ruminococcus flavefaciens*** (FD-1 strain)

- UniProt taxonomy ID: 657322
- Most complex cellulosome described to date: 223 dockerin-containing proteins
- Important rumen bacterium for understanding gut microbiome cellulose degradation
- However, fewer reviewed UniProt entries available
- Unique cohesin-dockerin binding modes

**Recommendation**: Start with *A. thermocellus* due to better annotation coverage and foundational status in the field.

**Second model: *Clostridium cellulovorans*** (strain ATCC 35296 / DSM 3052 / 743B)

- UniProt species code: CLOCL (taxonomy ID: 573061 for strain, 1493 for species)
- Mesophilic organism (optimal growth ~37°C)
- Produces both cellulosomal and free (non-cellulosomal) cellulases
- Well-characterized cellulosome with 57 cellulosomal protein-encoding genes
- CbpA scaffoldin contains 9 cohesin domains and 4 SLH domains
- Gene cluster organization: cbpA-exgS-engH-engK-hbpA-engL-manA-engM-engN
- Good experimental literature on synergistic enzyme activities

## Cellulosome Architecture

The cellulosome consists of:
1. **Scaffoldins** - Non-catalytic proteins containing cohesins that organize the complex
2. **Catalytic subunits** - Enzymes containing dockerins that bind to cohesins
3. **Cell surface anchors** - Proteins that attach the cellulosome to the cell wall

Key interaction: Type I dockerin (on enzymes) binds Type I cohesin (on CipA scaffoldin)
Cell anchoring: Type II dockerin (on CipA) binds Type II cohesin (on anchor proteins)

## Genes for Review - *Acetivibrio thermocellus*

### Priority 1: Core Scaffoldins and Anchors

| Gene   | UniProt ID | Protein                                      |
|--------|------------|----------------------------------------------|
| cipA   | Q06851     | Cellulosomal-scaffolding protein A           |
| cipB   | Q01866     | Cellulosomal-scaffolding protein B           |
| sdbA   | P71143     | Scaffolding dockerin binding protein A       |
| ancA   | Q06848     | Cellulosome-anchoring protein                |

### Priority 2: Key Cellulases (GH Family Enzymes)

| Gene   | UniProt ID | Protein                                      |
|--------|------------|----------------------------------------------|
| celS   | P0C2S5     | Cellulose 1,4-beta-cellobiosidase CelS (GH48)|
| celK   | P0C2S1     | Cellulose 1,4-beta-cellobiosidase CelK       |
| celA   | P0C2S2     | Endoglucanase A                              |
| celC   | P0C2S3     | Endoglucanase C                              |
| celD   | P0C2S4     | Endoglucanase D                              |
| celX   | P15329     | Putative endoglucanase X                     |

### Priority 3: Hemicellulases and Other Activities

| Gene   | UniProt ID | Protein                                      |
|--------|------------|----------------------------------------------|
| xynY   | P51584     | Endo-1,4-beta-xylanase Y                     |
| xynX   | P38535     | Exoglucanase XynX                            |
| xghA   | Q70DK5     | Xyloglucanase Xgh74A                         |
| licB   | Q84C00     | Beta-glucanase (Lichenase)                   |

### Priority 4: Additional Cellulosomal Proteins

| Gene   | UniProt ID | Protein                                      |
|--------|------------|----------------------------------------------|
| celE   | P10477     | Cellulase/esterase CelE                      |
| xynZ   | P10478     | Xylanase Z (with feruloyl esterase domain)   |
| celM   | P55742     | Putative aminopeptidase                      |

## Genes for Review - *Clostridium cellulovorans*

### Priority 1: Core Scaffoldin

| Gene   | UniProt ID | Protein                                      |
|--------|------------|----------------------------------------------|
| cbpA   | P38058     | Cellulose-binding protein A (scaffoldin)     |

### Priority 2: Cellulosomal GH9 Endoglucanases

| Gene   | UniProt ID | Protein                                      |
|--------|------------|----------------------------------------------|
| engK   | Q9RGE8     | Glucanase/Endoglucanase K (GH9)              |
| engL   | Q9RGE6     | Endoglucanase L (GH9)                        |
| engO   | Q6DTY2     | Endoglucanase O (GH9, non-cellulosomal)      |

### Priority 3: Other Cellulosomal Proteins

| Gene   | UniProt ID | Protein                                      |
|--------|------------|----------------------------------------------|
| hbpA   | Q9RGE7     | Hydrophobic protein A                        |

Note: Many C. cellulovorans proteins (exgS, engE, engH, engM, engN, pelA) are not yet in UniProt/Swiss-Prot
or have only TrEMBL entries with incorrect/unverified taxonomy. Focus on the 5 genes with validated UniProt entries above.

## Why Study the Cellulosome?

1. **Biofuels/Biorefinery**: Consolidated bioprocessing for cellulosic ethanol production
2. **Industrial enzymes**: Understanding synergistic enzyme action
3. **Protein engineering**: Modular architecture enables designer cellulosomes
4. **Basic science**: Model for understanding supramolecular enzyme complexes
5. **Synthetic biology**: Engineering organisms for biomass conversion

## Key References

- [CAZypedia Cellulosome](https://www.cazypedia.org/index.php/Cellulosome)
- [Global View of the C. thermocellum Cellulosome](https://jb.asm.org/content/189/19/6787.full)
- [Enzymatic diversity of the C. thermocellum cellulosome](https://www.nature.com/articles/srep35709)
- [Cellulosome Wikipedia](https://en.wikipedia.org/wiki/Cellulosome)

---
# STATUS

## Priority 1 - Scaffoldins and Anchors
- [x] cipA (Q06851) - Primary scaffoldin - COMPLETE (validates with 1 warning)
- [x] cipB (Q01866) - Secondary scaffoldin - COMPLETE (validates with 7 warnings)
- [x] sdbA (P71143) - Dockerin binding protein - COMPLETE (validates with 8 warnings)
- [x] ancA (Q06848) - Anchoring protein - COMPLETE (pre-existing)

## Priority 2 - Cellulases
- [x] celS (A3DH67) - Major exoglucanase GH48 - COMPLETE (validates with 6 warnings)
- [x] celK - Exoglucanase - COMPLETE (validates)
- [x] celA - Endoglucanase A - COMPLETE (validates)
- [x] celC - Endoglucanase C - COMPLETE (validates)
- [x] celD - Endoglucanase D - COMPLETE (validates)
- [x] celX (P15329) - Endoglucanase X - COMPLETE (validates)

## Priority 3 - Hemicellulases
- [x] xynY (P51584) - Xylanase Y - COMPLETE (validates)
- [x] xynX (P38535) - Exoglucanase/Xylanase X - COMPLETE (validates with 1 warning)
- [x] xghA (Q70DK5) - Xyloglucanase - COMPLETE (validates)
- [x] licB (Q84C00) - Beta-glucanase - COMPLETE (validates with 3 warnings)

## Priority 4 - Additional
- [x] celE (P10477) - Cellulase/esterase - COMPLETE (validates with 3 warnings)
- [x] xynZ (P10478) - Xylanase Z with feruloyl esterase - COMPLETE (validates with 3 warnings)
- [x] celM (P55742) - Aminopeptidase - COMPLETE (validates with 8 warnings)

---

## *Clostridium cellulovorans* Status

### Priority 1 - Scaffoldin
- [x] cbpA (P38058) - Cellulose-binding protein A - COMPLETE (validated with 1 warning)

### Priority 2 - GH9 Endoglucanases
- [x] engK (Q9RGE8) - Glucanase K GH9 - COMPLETE (validated with 2 warnings)
- [x] engL (Q9RGE6) - Endoglucanase L GH9 - COMPLETE (validated with 2 warnings)
- [x] engO (Q6DTY2) - Endoglucanase O GH9 (non-cellulosomal) - COMPLETE (validated with 1 warning)

### Priority 3 - Other Cellulosomal Proteins
- [x] hbpA (Q9RGE7) - Hydrophobic protein A (accessory scaffoldin) - COMPLETE (validated with 1 warning)

**All 5 C. cellulovorans genes reviewed and validated.** Annotation reviews complete.

Note: Several UniProt IDs initially tested (Q9RGE5/engM, Q9RGE9, Q9L3K5/pelA) were found to map to incorrect organisms and were removed.

# NOTES

## 2025-12-27 (Session 4)

**Completed annotation reviews for all 5 C. cellulovorans genes.** All reviews pass validation with minor warnings.

Key findings from the reviews:

1. **CbpA (P38058) - Primary scaffoldin**:
   - Marked GO:0000272 (polysaccharide catabolic process), GO:0005975 (carbohydrate metabolic), GO:0030245 (cellulose catabolic) as over-annotated - CbpA is non-catalytic
   - Marked GO:0071555 (cell wall organization) for REMOVAL - incorrect annotation
   - Added GO:0043263 (cellulosome), GO:0044575 (cellulosome assembly), GO:1990308 (type-I dockerin domain binding)

2. **EngK (Q9RGE8) - Cellulosomal GH9 endoglucanase**:
   - Accepted GO:0008810 (cellulase activity), GO:0030245 (cellulose catabolic process)
   - Added GO:0043263 (cellulosome), GO:1990311 (type-I cohesin domain binding)

3. **EngL (Q9RGE6) - Cellulosomal GH9 endoglucanase**: Similar to EngK

4. **EngO (Q6DTY2) - NON-cellulosomal GH9 endoglucanase**:
   - Key distinction: EngO lacks dockerin and has its own CBM for substrate targeting
   - Functions as a free secreted enzyme that complements the cellulosome
   - Added GO:0030248 (cellulose binding) for its CBM function
   - No cellulosome annotations (unlike EngK/EngL)

5. **HbpA (Q9RGE7) - Accessory scaffoldin**:
   - Marked GO:0000272 (polysaccharide catabolic process) for REMOVAL - non-catalytic protein
   - Marked GO:0030246 (carbohydrate binding) as UNDECIDED - CBM annotation may be artifact
   - Added GO:1990308 (type-I dockerin domain binding), GO:0044575 (cellulosome assembly)

## 2025-12-26 (Session 3)

**Extended project to include *Clostridium cellulovorans* as second model organism.** Selected based on:

1. Mesophilic organism (complements thermophilic *A. thermocellus*)
2. Produces both cellulosomal AND free cellulases - interesting comparative biology
3. Well-characterized cellulosome with 57 cellulosomal protein-encoding genes
4. Good experimental literature including synergy studies, crystal structures
5. CbpA scaffoldin has unique architecture with 9 cohesins and 4 SLH domains
6. Gene cluster organization well documented: cbpA-exgS-engH-engK-hbpA-engL-manA-engM-engN

Key references for *C. cellulovorans*:
- [PMID:11004194](https://pubmed.ncbi.nlm.nih.gov/11004194/) - Large gene cluster for cellulosome
- [PMID:11916675](https://pubmed.ncbi.nlm.nih.gov/11916675/) - Cellulosome subunit composition
- [PMID:12107127](https://pubmed.ncbi.nlm.nih.gov/12107127/) - Synergistic effects between cellulases
- [PMID:19948806](https://pubmed.ncbi.nlm.nih.gov/19948806/) - Genome sequence of 743B strain

**Gene validation issues discovered:** Several UniProt IDs initially identified from literature were found to map to wrong organisms:
- Q9RGE5 (engM) - Empty UniProt file
- Q9RGE9 - Actually cysN from *Campylobacter jejuni*
- Q9L3K5 (pelA) - Actually cheA from *Bacillus cereus*
- O52427, O52428 - Empty/invalid entries
- Q9X2A5 (engE) - Actually argD from *Thermotoga maritima*
- P23661 (engB) - Actually celB from *Ruminococcus albus*

**Final validated set:** 5 genes with correct taxonomy (P38058, Q9RGE8, Q9RGE6, Q6DTY2, Q9RGE7). Deep research completed for all 5.

## 2025-12-26 (Session 2)

**All 17 genes reviewed and validated.** The cellulosome project is now complete with comprehensive reviews for all priority genes. All reviews pass validation (some with warnings that are informational only).

Key annotation insights from the reviews:

1. **Scaffoldins (cipA, cipB, sdbA)**: Multiple incorrect IEA annotations identified and marked for removal:
   - GO:0004553 (hydrolase activity) was incorrectly propagated from dockerin domains to non-catalytic scaffoldins
   - GO:0030246 (carbohydrate binding) incorrectly attributed to cohesin domains which bind dockerins (proteins), not carbohydrates
   - Recommended adding GO:0044575 (cellulosome assembly) as the core biological process
   - Recommended GO:1990308/1990309/1990311/1990312 for specific cohesin-dockerin binding functions

2. **Cellulases (celS, celA, celC, celD, celK, celX)**: Annotations mostly correct, with recommendations to:
   - Add GO:0043263 (cellulosome) as cellular component
   - Add GO:1990311 (type-I cohesin domain binding) for dockerin function
   - Mark overly general process terms (polysaccharide catabolic, carbohydrate metabolic) as over-annotated in favor of specific cellulose catabolic process

3. **Hemicellulases (xynY, xynX, xghA, licB)**: Reviews complete with appropriate xylanase and related activities documented

4. **Additional proteins (celE, xynZ, celM)**: Dual-function enzymes properly characterized

## 2025-12-26 (Session 1)

**Project created.** Selected *Acetivibrio thermocellus* (formerly *Clostridium thermocellum*) as the primary model organism for the cellulosome project based on:

1. Historical significance - cellulosomes were first discovered in this organism
2. Best-characterized cellulosome with extensive structural data
3. Good UniProt coverage with ~15 Swiss-Prot reviewed cellulosomal proteins
4. Industrial relevance for biofuel production

Compiled initial gene list of 17 proteins organized by priority:
- 4 scaffoldins/anchors (architectural proteins)
- 6 cellulases (core enzymatic function)
- 4 hemicellulases (auxiliary activities)
- 3 additional proteins

Alternative model *Ruminococcus flavefaciens* noted for future expansion - has the most complex cellulosome (223 dockerin proteins) but fewer reviewed UniProt entries.

Key architectural insight: The cellulosome uses a modular cohesin-dockerin system where Type I interactions organize enzymes on the CipA scaffoldin, and Type II interactions anchor the complex to the cell surface via OlpB/SdbA anchor proteins.
