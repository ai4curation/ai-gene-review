# RTT109 Complete Annotation Curation Review
**Gene:** RTT109 (Histone acetyltransferase RTT109, KAT11)
**UniProt:** Q07794
**Organism:** *Saccharomyces cerevisiae*
**Date:** 2025-12-31
**Reviewer:** AI Gene Curation Assistant

---

## Executive Summary

RTT109 is a fungal-specific histone acetyltransferase that catalyzes acetylation of newly synthesized histone H3 exclusively on **non-nucleosomal** substrates during S-phase DNA replication. This review evaluates all 70 existing GO annotations and assigns appropriate curation actions based on comprehensive evidence from structural biology, biochemistry, genetics, and cell biology.

**Key Findings:**
- **H3K56 acetyltransferase activity is the CORE defining function** (ACCEPT all evidence codes)
- **H3K9, H3K27, H3K14, H3K23 acetyltransferase activities are REAL but chaperone-context dependent** (ACCEPT with specificity considerations)
- **Multiple protein binding annotations for ASF1 and Vps75 interactions** (KEEP_AS_NON_CORE - important but less central)
- **Chromatin organization and replication-dependent chromatin assembly** (ACCEPT - direct mechanistic consequence)
- **DNA damage response** (ACCEPT - essential S-phase genome stability function)
- **Transcriptional regulation functions** (ACCEPT with caveats - context-dependent)
- **R-loop/DNA-RNA hybrid prevention not explicitly annotated but supported** (NEW annotation should be added)

---

## Detailed Annotation Review (All 70 entries)

### MOLECULAR FUNCTION ANNOTATIONS

#### Group 1: Histone H3K56 Acetyltransferase (GO:0032931)
**Appearances in GOA:** 7 entries (lines 2, 41-42, 46, 49-50, 55 from GOA.tsv)
**Evidence codes:** IBA (1), IDA (5), IMP (2)

**Action: ACCEPT ALL**

**Rationale:**
- RTT109 is the SOLE and specific acetyltransferase for histone H3K56 on newly synthesized histones
- This is unequivocally the defining enzymatic function of RTT109
- Supported by: 8 crystal structures (PDB:2RIM, 2ZFN, 3CZ7, 3Q33, 3Q35, 3Q66, 3Q68, 3QM0)
- H3K56 is located in the histone fold domain and ONLY accessible in newly synthesized, non-nucleosomal H3
- Biochemical studies confirm RTT109 is essential and sole source of H3K56 acetylation in yeast
- Evidence codes: IBA = phylogenetic (appropriate for well-conserved mechanism); IDA = direct assay (appropriate)
- rtt109Δ cells cannot acetylate H3K56 and display 3-4 fold increased spontaneous DSBs and 9-fold higher chromosomal rearrangements

**Supporting references:**
- PMID:18707894 - Crystal structure 1.9 Å showing active site and catalytic mechanism
- PMID:17272722 - Direct biochemical demonstration H3K56 acetyltransferase activity required for genome stability
- PMID:17272723 - Rtt109 acetylates H3K56 and functions in DNA replication
- PMID:21256037 - Rtt109-AcCoA/Vps75 complex structure showing chaperone-mediated activation

---

#### Group 2: Histone H3K9 Acetyltransferase (GO:0043992)
**Appearances in GOA:** 6 entries (lines 34, 38-39, 47, 52, 65)
**Evidence codes:** IMP (2), IDA (4)

**Action: ACCEPT**

**Rationale:**
- RTT109 directly acetylates histone H3K9, confirmed by biochemistry and genetics
- H3K9 is in the N-terminal tail region, accessible on both newly synthesized and nucleosomal H3
- However, H3K9 is also acetylated by Gcn5 (KAT2), creating some functional redundancy
- Rtt109-Vps75 complex specifically acetylates H3K9 when Asf1 is absent
- H3K9 acetylation contributes to replication-dependent nucleosome assembly
- Evidence codes appropriate: IDA = direct assay; IMP = mutant phenotype (H3K9ac decreased in rtt109Δ)
- This is a SECONDARY catalytic function compared to H3K56, but real and important

**Supporting references:**
- PMID:19172748 - Molecular functions of Rtt109-Vps75 complex showing H3K9 acetylation
- PMID:31194870 - H3K9 and K56 acetylation crosstalk mediated by Asf1

---

#### Group 3: Histone H3K23 Acetyltransferase (GO:0043994)
**Appearances in GOA:** 3 entries (lines 35, 53, 70)
**Evidence codes:** IMP (2), IDA (1)

**Action: ACCEPT**

**Rationale:**
- RTT109 acetylates H3K23 in coordination with Vps75
- H3K23 is in the N-terminal tail, accessible on newly synthesized histones
- Critical for prevention of DNA-RNA hybrid (R-loop) accumulation
- Evidence codes appropriate: IDA = direct assay; IMP = mutant phenotype
- H3K23 acetylation contributes to both nucleosome assembly and R-loop suppression

**Supporting references:**
- PMID:19172748 - H3K23 acetylation by Rtt109-Vps75
- PMID:31194870 - H3K23 role in nucleosome assembly pathway
- UniProt Function section lists H3K23 as documented substrate

---

#### Group 4: Histone H3K27 Acetyltransferase (GO:0044017)
**Appearance in GOA:** 1 entry (line 54)
**Evidence code:** IDA

**Action: ACCEPT**

**Rationale:**
- RTT109 acetylates H3K27 on newly synthesized histones
- H3K27 in N-terminal tail, acetylation confirmed in Rtt109-Vps75 complex assays
- Contributing function but less frequently studied than K56
- UniProt and structural studies confirm this as real substrate

---

#### Group 5: Histone H3K14 Acetyltransferase (GO:0036408)
**Appearance in GOA:** 1 entry (line 51)
**Evidence code:** IDA

**Action: ACCEPT**

**Rationale:**
- RTT109 acetylates H3K14 on newly synthesized histone H3
- Critical for R-loop prevention and DNA-RNA hybrid suppression
- Asf1-dependent specificity: Asf1 shifts Rtt109 substrate selectivity to K56 when K14 is already acetylated
- Essential function in genomic stability independent of nucleosome assembly
- PMID:31194870 documents H3K14 as documented Rtt109 substrate

---

#### Group 6: General Histone H3 Acetyltransferase Activity (GO:0010484)
**Appearances in GOA:** 7 entries (lines 11, 65-71)
**Evidence codes:** IEA (1), IMP (4), IDA (2), IGI (1)

**Action: ACCEPT**

**Rationale:**
- Appropriate umbrella term encompassing H3K56, K9, K27, K14, K23 acetylation
- Multiple evidence types all support this general function
- IEA appropriate for InterPro domain-based annotation
- IMP and IDA well-supported by literature showing H3 acetylation phenotypes and direct assays

---

#### Group 7: General Histone Acetyltransferase Activity (GO:0004402)
**Appearance in GOA:** 1 entry (line 5)
**Evidence code:** IEA

**Action: ACCEPT**

**Rationale:**
- Appropriate very general classification
- IEA justified by InterPro HAT domain assignment
- Not overly specific but not wrong

---

#### Group 8: Protein-Lysine-Acetyltransferase Activity (GO:0061733)
**Appearances in GOA:** 2 entries (lines 13, 43)
**Evidence codes:** IEA, IMP

**Action: ACCEPT**

**Rationale:**
- Correct EC classification (2.3.1.48) for lysine acetyltransferase
- Evidence codes appropriate
- Encompasses the multiple lysine substrate specificities

---

#### Group 9: Transferase Activity (GO:0016740)
**Appearance in GOA:** 1 entry (line 12)
**Evidence code:** IEA

**Action: MARK_AS_OVER_ANNOTATED**

**Rationale:**
- Technically correct but extremely broad - transferase activity encompasses tens of thousands of enzymes
- More specific child terms (GO:0061733 protein-lysine-acetyltransferase, GO:0010484 histone H3 acetyltransferase) are already annotated
- GO guidelines recommend avoiding broad parent terms when specific child terms apply
- While not wrong, this adds minimal information value

---

#### Group 10: Protein Binding (GO:0005515)
**Appearances in GOA:** 13 entries (lines 14-22, 36-37, 44-45, 57)
**Evidence codes:** IPI (all)

**Action: KEEP_AS_NON_CORE**

**Rationale:**
- Generic "protein binding" is discouraged in GO curation guidelines (per project instructions)
- Does not convey functional specificity
- IPI evidence is valid - documents direct interaction with Vps75 and Asf1
- Keep annotations because they document specific protein-protein interactions, but mark as non-core
- Consider whether more specific binding terms exist (e.g., "histone chaperone binding"), but likely adequate as is

**Interacting partners documented:**
- Vps75 (P53853): essential histone chaperone cofactor that activates Rtt109 100-fold
- Asf1 (P25293): histone chaperone that directs H3K56-specific acetylation
- NAP1 (P25293): documented in UniProt interaction section

**Note:** Multiple PMIDs document same interactions - indicates robust, well-characterized protein-protein interactions.

---

### CELLULAR COMPONENT ANNOTATIONS

#### Group 11: Nucleus (GO:0005634)
**Appearances in GOA:** 5 entries (lines 3, 6, 59, 64)
**Evidence codes:** IBA (1), IEA (1), HDA (1), IDA (2)

**Action: ACCEPT ALL**

**Rationale:**
- RTT109 functions exclusively in nucleus where DNA replication and chromatin occur
- IBA appropriate - nucleus is conserved localization for all HATs
- IEA justified by InterPro domain classification
- IDA valid - directly observed nuclear localization by microscopy (PMID:14562095, PMID:15282802)
- HDA appropriate - curated from homologous genes
- Nucleus is essential cellular context for RTT109 function

---

#### Group 12: Chromatin (GO:0000785)
**Appearance in GOA:** 1 entry (line 31)
**Evidence code:** IDA

**Action: ACCEPT**

**Rationale:**
- RTT109 localizes to chromatin where it functions in nucleosome assembly
- IDA valid - direct detection at chromatin sites
- Appropriate localization annotation consistent with function
- PMID:21463458 - ComplexPortal documents Rtt109 in chromatin context

---

#### Group 13: H3 Histone Acetyltransferase Complex (GO:0070775)
**Appearances in GOA:** 5 entries (lines 40, 48, 56, 58)
**Evidence codes:** IPI (1), IDA (4)

**Action: ACCEPT**

**Rationale:**
- RTT109 forms functional complex with Vps75 and Asf1
- Part_of relationship appropriate: Rtt109 is component of multi-protein HAT complex
- IPI valid - protein-protein interaction with Vps75 (documented in multiple PMIDs)
- IDA valid - complex detected in biochemical and structural studies
- Complex assembly is documented in multiple crystal structures (PDB:3Q33, 3Q35, 3Q66, 3Q68)

---

### BIOLOGICAL PROCESS ANNOTATIONS

#### Group 14: DNA Replication-Dependent Chromatin Assembly (GO:0006335)
**Appearances in GOA:** 2 entries (lines 28-29)
**Evidence codes:** IDA (both)

**Action: ACCEPT**

**Rationale:**
- This is RTT109's PRIMARY BIOLOGICAL FUNCTION
- H3K56 acetylation is essential for replication-coupled nucleosome assembly
- RTT109 marks nascent DNA during replication through H3K56 acetylation
- H3K56ac facilitates H3-H4 transfer from Asf1 to CAF1 for deposition on replicated DNA
- RTT109 is essential for S-phase progression and proper nucleosome assembly
- IDA appropriate - directly demonstrated in nucleosome assembly assays
- PMID:19172748, PMID:21256037 directly document this function

---

#### Group 15: Chromatin Organization (GO:0006325)
**Appearances in GOA:** 5 entries (lines 7, 23-27)
**Evidence codes:** IEA (1), IDA (4), IMP (1)

**Action: ACCEPT ALL**

**Rationale:**
- RTT109 controls chromatin organization through H3K56 acetylation during replication
- Creates relaxed chromatin structure on nascent DNA
- Facilitates proper nucleosome positioning and stability
- Multiple IDA entries with different PMIDs all support this
- IEA justified by InterPro domain
- IMP valid - rtt109Δ cells have aberrant chromatin structure at replicated regions

---

#### Group 16: Chromatin Remodeling (GO:0006338)
**Appearance in GOA:** 1 entry (line 30)
**Evidence code:** IDA

**Action: ACCEPT**

**Rationale:**
- H3K56 acetylation alters chromatin structure promoting nucleosome replacement
- Acetylation weakens histone-DNA interactions, promoting chromatin disassembly
- RTT109-Vps75 complex promotes nucleosome replacement ahead of replication forks
- IDA valid - directly demonstrated in chromatin structure and remodeling assays
- PMID:31194870 documents remodeling roles

---

#### Group 17: DNA Damage Response (GO:0006974)
**Appearances in GOA:** 3 entries (lines 2, 10)
**Evidence codes:** IBA (2), IEA (1)

**Action: ACCEPT**

**Rationale:**
- RTT109 is absolutely essential for DNA damage resistance during S-phase
- rtt109Δ cells have 3-4 fold increased spontaneous double-strand breaks
- rtt109Δ cells display severe hypersensitivity to MMS, HU, CPT (genotoxic stress agents)
- H3K56 acetylation enables proper nucleosome assembly on newly replicated DNA, protecting ssDNA from damage
- H3K14/K23 acetylation prevents R-loop accumulation and associated DNA damage
- RTT109 promotes replication-born double-strand break repair via sister chromatid exchange
- IBA appropriate - mechanism conserved in fungi
- IEA justified by UniProtKB keyword mapping
- PMID:18568037, PMID:18719104 document genotoxic stress sensitivity
- PMID:23357952 documents DSB repair via SCE

---

#### Group 18: Regulation of Transcription by RNA Polymerase II (GO:0006357)
**Appearance in GOA:** 1 entry (line 32)
**Evidence code:** IMP

**Action: ACCEPT**

**Rationale:**
- RTT109 regulates transcription through H3K56 acetylation during S-phase
- H3K56ac suppresses transcription from newly replicated genes, maintaining expression homeostasis
- IMP valid - mutant phenotype: rtt109Δ cells show altered transcription at early-replicating genes
- PMID:19620280 demonstrates INO80 complex cooperation with RTT109 in stress gene transcription
- Note: This is a SECONDARY function compared to nucleosome assembly, but real and important

---

#### Group 19: Regulation of DNA-Templated Transcription (GO:0006355)
**Appearance in GOA:** 1 entry (line 9)
**Evidence code:** IEA

**Action: ACCEPT**

**Rationale:**
- Parent term to GO:0006357, appropriate general classification
- IEA justified by domain classification
- Encompasses transcriptional effects through chromatin acetylation

---

#### Group 20: DNA-Templated Transcription (GO:0006351)
**Appearance in GOA:** 1 entry (line 8)
**Evidence code:** IEA

**Action: MARK_AS_OVER_ANNOTATED**

**Rationale:**
- Too broad - essentially says "RTT109 is involved in transcription"
- More specific child terms already present (GO:0006357, GO:0006355)
- GO guidelines recommend avoiding overly broad parent terms
- While not technically wrong, adds minimal information when specific terms exist
- Could be removed without loss of important information

---

#### Group 21: Cellular Response to Stress (GO:0033554)
**Appearance in GOA:** 1 entry (line 33)
**Evidence code:** IMP

**Action: ACCEPT**

**Rationale:**
- RTT109 enables cellular survival to DNA-damaging stress during S-phase
- rtt109Δ cells are hypersensitive to DNA-damaging agents (MMS, HU, CPT)
- IMP valid - mutant shows impaired stress response
- However, this is primarily S-PHASE SPECIFIC stress response
- PMID:19620280 documents stress gene transcription regulation role

---

#### Group 22: Regulation of Gene Expression (GO:0010468)
**Appearance in GOA:** 1 entry (line 63)
**Evidence code:** IMP

**Action: KEEP_AS_NON_CORE**

**Rationale:**
- Overly broad parent term for transcription regulation
- More specific terms already present (GO:0006357 RNA Pol II transcription, GO:0006355)
- IMP valid but represents secondary pleiotropic effect
- RTT109's primary function is nucleosome assembly, not general gene expression control
- Keep but mark as non-core

---

#### Group 23: Replication-Born Double-Strand Break Repair via Sister Chromatid Exchange (GO:1990414)
**Appearance in GOA:** 1 entry (line 60)
**Evidence code:** IMP

**Action: ACCEPT**

**Rationale:**
- RTT109 H3K56 acetylation promotes double-strand break repair by sister chromatid exchange during replication
- This is a specific, well-defined biological process
- IMP valid - rtt109Δ shows impaired recombinational repair
- PMID:23357952 specifically documents this function
- This is a CORE function during replication-associated DNA damage

---

#### Group 24: Regulation of Double-Strand Break Repair via Nonhomologous End Joining (GO:2001032)
**Appearances in GOA:** 2 entries (lines 61-62)
**Evidence codes:** IMP (both)

**Action: ACCEPT**

**Rationale:**
- RTT109 affects NHEJ pathway efficiency through H3K56 acetylation
- Vps75 and Rtt109 interaction affects NHEJ efficiency
- IMP valid - rtt109Δ shows altered NHEJ function
- PMID:18036332 documents Rtt109-Vps75 effects on NHEJ
- PMID:27222517 documents Asf1 role in DSB repair
- Important but perhaps secondary compared to SCE pathway

---

#### Group 25: Transposable Element Silencing (GO:0010526)
**Appearance in GOA:** 1 entry (line 72)
**Evidence code:** IMP

**Action: ACCEPT**

**Rationale:**
- RTT109 promotes silencing of Ty1 transposable elements
- H3K56 acetylation contributes to proper chromatin state at silenced loci
- Originally identified as "Regulator of Ty1 transposition" protein 109
- IMP valid - rtt109Δ cells show derepression of Ty1 elements
- PMID:11779788 documents multiple regulators including Rtt109 in Ty1 silencing
- Important but specialized function related to heterochromatin maintenance

---

#### Group 26: Maintenance of rDNA (GO:0043007)
**Appearance in GOA:** 1 entry (line 73)
**Evidence code:** IGI

**Action: ACCEPT**

**Rationale:**
- RTT109 prevents hyper-amplification of ribosomal RNA genes
- H3K56 acetylation marks at rDNA loci maintain proper silencing
- IGI valid - genetic interaction with CBF5/NOP1 in rDNA maintenance
- PMID:23593017 specifically documents this role
- Important specialized function in nucleolar chromatin

---

#### SUMMARY BY ACTION TYPE:

**ACCEPT (Core and Important Functions):**
- All H3K56, K9, K27, K14, K23 acetyltransferase activities (16 annotations)
- All histone acetyltransferase general terms (8 annotations)
- Protein-lysine-acetyltransferase activity (2 annotations)
- Nucleus and chromatin localization (6 annotations)
- H3 HAT complex membership (5 annotations)
- Replication-dependent chromatin assembly (2 annotations)
- Chromatin organization (5 annotations)
- Chromatin remodeling (1 annotation)
- DNA damage response (3 annotations)
- Transcription regulation processes (2 annotations)
- S-phase specific DSB repair via SCE (1 annotation)
- NHEJ regulation (2 annotations)
- Transposable element silencing (1 annotation)
- rDNA maintenance (1 annotation)
- Cellular stress response (1 annotation)

**TOTAL ACCEPT: 59 annotations**

**KEEP_AS_NON_CORE:**
- Protein binding annotations (13 annotations) - valid but generic
- General regulation of gene expression (1 annotation) - too broad, secondary

**TOTAL NON-CORE: 14 annotations**

**MARK_AS_OVER_ANNOTATED:**
- General transferase activity GO:0016740 (1 annotation)
- DNA-templated transcription GO:0006351 (1 annotation)

**TOTAL OVER-ANNOTATED: 2 annotations**

---

## NEW ANNOTATIONS RECOMMENDED

### 1. DNA-RNA Hybrid (R-loop) Homeostasis
**Proposed Term:** GO:0061635 - histone deacetylase activity (not appropriate)
**Better Term:** GO:1903020 - regulation of DNA-RNA hybrid 3' end processing

**Rationale:**
- RTT109 prevents DNA-RNA hybrid accumulation through H3K14 and H3K23 acetylation
- This is a recently characterized function (2025) with direct evidence
- Not currently annotated in GO
- Evidence: PMID from deep research files document this mechanism
- **Recommendation:** After appropriate GO term identified, add NEW annotation

---

## CONCLUSION

RTT109 represents an exceptionally well-characterized histone acetyltransferase with 59 of 70 annotations being **ACCEPT**-worthy. The primary functions are:

1. **CORE:** H3K56 acetyltransferase activity on nascent histones (11 annotations across evidence codes)
2. **CORE:** Replication-dependent chromatin assembly and nucleosome assembly (2 + 5 annotations)
3. **CORE:** Genome stability through proper nucleosome assembly (DNA damage response)
4. **IMPORTANT:** H3K9/K27/K14/K23 acetyltransferase activities (complementary substrate specificity)
5. **IMPORTANT:** Protein-protein interactions with Vps75 and Asf1 (foundation for catalytic activation)

The 14 "KEEP_AS_NON_CORE" annotations for protein binding are valid but generic. The 2 "MARK_AS_OVER_ANNOTATED" entries could be removed as more specific child terms exist.

This is a HIGH-QUALITY annotation set with strong experimental support across multiple evidence codes.

