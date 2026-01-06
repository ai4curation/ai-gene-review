# SPA2 GO Annotation Curation Analysis

## Gene Summary
SPA2 (Polarity-associated protein) is a 1,466 amino acid scaffolding protein essential for establishing and maintaining cell polarity in budding yeast. The protein serves as a core structural component of the polarisome complex, organizing multiple functional modules for actin cytoskeleton organization, MAP kinase signaling, and bud site selection.

## Key Mechanistic Insights from Literature

### Core Functions (from PMID:12361575, PMID:9632790, PMID:9214378)
1. **Polarisome Scaffold**: Forms complex with Pea2p and Bud6p; functions as platform for actin cable assembly and signaling
2. **MAPK Pathway Scaffold**: Directly recruits Mkk1/Mkk2 and Mpk1p; localizes cell wall integrity pathway to growth sites
3. **Localization Hub**: Early marker of polarized growth sites; localizes to incipient bud site, bud tip, mating projection, and bud neck
4. **Protein Organization**: Regulates localization of multiple proteins through scaffold function

### Localization Context
- Localizes as discrete patch at sites of polarized growth
- Stably anchored at bud tips (FRAP analysis shows stable localization)
- Forms SHD-II domain interactions with Pea2p
- Contains conserved 150 amino acid localization domain essential for targeting

### Functional Interactions
- **Formin Bni1**: Together with Bud6p, facilitates actin cable nucleation and elongation
- **MAPK Components**: SHD-I domain interacts with Mkk1p, Mkk2p, Ste11p, Ste7p
- **Septin**: Interacts with Shs1p; involved in septin ring formation at mother-bud neck
- **GAP Proteins**: Msb3/Msb4 (Rab-GAPs) interact with Spa2p to coordinate polarity

## Annotation Curation Strategy

### Localization Annotations (Cellular Components)
These describe WHERE SPA2 is found and are supported by direct microscopy evidence:
- GO:0000131 (incipient cellular bud site) - ACCEPT: IDA/IBA supported
- GO:0005934 (cellular bud tip) - ACCEPT: IDA/IBA supported
- GO:0005935 (cellular bud neck) - ACCEPT: IDA supported
- GO:0043332 (mating projection tip) - ACCEPT: IDA supported
- GO:0000133 (polarisome) - ACCEPT: IDA supported, core component
- GO:0005938 (cell cortex) - ACCEPT: IDA supported
- GO:1902716 (cell cortex of growing cell tip) - ACCEPT: IBA supported
- GO:0005826 (actomyosin contractile ring) - REMOVE: SPA2 is at bud neck but not a core contractile ring protein

### Molecular Function Annotations
These describe WHAT functional activities SPA2 performs:
- GO:0005078 (MAP-kinase scaffold activity) - ACCEPT: Core direct function
- GO:0005515 (protein binding) - REMOVE: Too vague; specific interactions should replace this

### Biological Process Annotations
These describe WHICH cellular processes SPA2 is involved in:

**Cell Polarity & Morphogenesis (CORE):**
- GO:0030010 (establishment of cell polarity) - ACCEPT: Core IMP evidence
- GO:0030950 (establishment or maintenance of actin cytoskeleton polarity) - ACCEPT: NAS from ComplexPortal
- GO:0007121 (bipolar cellular bud site selection) - ACCEPT: IMP evidence
- GO:0007118 (budding cell apical bud growth) - ACCEPT: IMP evidence

**Mating & Morphogenesis:**
- GO:0000753 (cell morphogenesis involved in conjugation with cellular fusion) - ACCEPT: IMP evidence
- GO:0043332 as process (mating projection tip) - Already covered as location

**Filamentous Growth (SECONDARY):**
- GO:0007124 (pseudohyphal growth) - KEEP_AS_NON_CORE: SPA2 required but not primary function
- GO:0036267 (invasive filamentous growth) - KEEP_AS_NON_CORE: Secondary developmental process

**Stress Response (PERIPHERAL):**
- GO:0071468 (cellular response to acidic pH) - KEEP_AS_NON_CORE: Maintenance of polarity under stress
- GO:0071474 (cellular hyperosmotic response) - KEEP_AS_NON_CORE: Actin recovery in osmotic stress

**Regulation of Actin (CORE):**
- GO:0032956 (regulation of actin cytoskeleton organization) - ACCEPT: IMP/IGI evidence
- GO:0032880 (regulation of protein localization) - ACCEPT: Multiple IMP lines of evidence

**General Cellular Processes:**
- GO:0008360 (regulation of cell shape) - ACCEPT: IEA from keywords appropriate
- GO:0006903 (vesicle targeting) - KEEP_AS_NON_CORE: Indirect through polarisome
- GO:0000165 (MAPK cascade) - ACCEPT: IEA from GO:0005078 scaffold activity

**Bud Site Selection:**
- GO:0000131 as process - Already covered in localization

### Interpretation of Evidence Codes

**IBA (Inferred from Biological Aspect):**
- Phylogenetic ortholog evidence appropriate for well-characterized localization and scaffold functions
- Shows conservation across species

**IDA (Inferred from Direct Assay):**
- Microscopy evidence for localizations
- Biochemical evidence for physical interactions
- Strongest evidence for location and direct interactions

**IMP (Inferred from Mutant Phenotype):**
- Genetic knockouts show defects in polarity, budding, mating
- Demonstrates functional requirement

**IGI (Inferred from Genetic Interaction):**
- Synthetic interactions with actin cytoskeleton genes
- Interactions with formin, septin genes

**IPI (Inferred from Physical Interaction):**
- Protein-protein interaction data; should be replaced by more specific molecular function terms

**NAS (Non-Annotated Statement):**
- From literature statements; ComplexPortal annotations
- Appropriate for well-supported statements from reliable sources

**IEA (Inferred from Electronic Annotation):**
- Automated keyword/localization mapping
- Generally appropriate if not contradicted

## Recommended Actions Summary

**ACCEPT (21 annotations):** Core polarity and scaffolding functions with strong experimental support
- All localization annotations with IDA evidence
- MAP-kinase scaffold activity (core molecular function)
- Establishment of cell polarity (core process)
- Regulation of actin cytoskeleton organization
- Budding and bud site selection processes
- Establishment/maintenance of actin cytoskeleton polarity

**KEEP_AS_NON_CORE (7 annotations):** Valid but secondary functions
- Pseudohyphal and invasive filamentous growth
- Stress response processes (acid pH, osmotic)
- Vesicle targeting (indirect)

**REMOVE (4 annotations):** Inappropriate or overly vague terms
- GO:0005826 (actomyosin contractile ring) - SPA2 at neck but not contractile ring component
- GO:0005515 (protein binding) - Too generic; replace with specific functions

**UNDECIDED (if insufficient evidence):** None - all have adequate evidence

## Notes on Specific Problematic Annotations

### GO:0005826 (actomyosin contractile ring)
SPA2 localizes to the bud neck where the contractile ring forms, but it is NOT a component of the contractile ring itself. The contractile ring contains myosin (Myo1p), actin, and septins. SPA2's role at the neck involves septin interactions and polarity maintenance, not contractile ring assembly/contraction. This appears to be a false IBA inference from organism comparison.

### GO:0005515 (protein binding) duplicates
Multiple IPI entries for "protein binding" are uninformative. While SPA2 does bind proteins, this is better captured by:
- MAP-kinase scaffold activity (GO:0005078)
- Specific role in polarisome assembly
- Interactions documented in complex annotations

### Localization vs. Process Confusion
Some annotations conflate localization with process:
- GO:0000131, GO:0005934, GO:0043332 appear as both cellular component (localization) and biological process
- The component aspect (where it is) should be ACCEPTED
- The process aspect (what it does) should be distinguished

---

**Analysis Date:** 2025-12-31
**Curator Note:** This analysis prioritizes mechanistic accuracy over comprehensive annotation coverage. SPA2 is extensively studied with clear evidence for its scaffold functions; ambiguous or overly broad terms have been marked for removal or modification.
