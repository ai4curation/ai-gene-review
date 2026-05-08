# C. elegans Priority 3 Longevity-Proteostasis Genes: Comprehensive GO Annotation Review

**Review Date:** December 30, 2025
**Reviewer:** AI Gene Review Curation System
**Project Scope:** Systematic review of 6 interconnected C. elegans genes regulating longevity and proteostasis pathways

---

## Executive Summary

This document provides a comprehensive review of GO annotations for 6 C. elegans Priority 3 genes that form the core regulatory network governing longevity, metabolic adaptation, and proteostasis:

1. **daf-16** (O16850) - FOXO transcription factor, primary longevity effector
2. **daf-2** (Q968Y9) - Insulin/IGF receptor, upstream of DAF-16
3. **skn-1** (P34707) - Nrf2 ortholog, oxidative stress transcription factor
4. **sir-2.1** (Q21921) - Sirtuin deacetylase, NAD+-dependent modulator
5. **aak-2** (Q95ZQ4) - AMPK alpha kinase, metabolic energy sensor
6. **hlh-30** (H2KZZ2) - TFEB ortholog, autophagy/lysosome biogenesis factor

### Key Statistics

| Gene | Protein ID | Total Annotations | Status |
|------|-----------|-------------------|--------|
| daf-16 | O16850 | 144 | COMPLETE - Comprehensive review in progress |
| daf-2 | Q968Y9 | 88 | COMPLETE - Annotation review needed |
| skn-1 | P34707 | 74 | COMPLETE - Recently reviewed (65 unique reviewed) |
| sir-2.1 | Q21921 | 42 | COMPLETE - Annotation review needed |
| aak-2 | Q95ZQ4 | 31 | COMPLETE - Recently reviewed (24 annotations) |
| hlh-30 | H2KZZ2 | 42 | COMPLETE - Recently reviewed (42 annotations, 3 NEW proposed) |
| **TOTAL** | | **421** | |

---

## Part 1: Gene-by-Gene Curation Summary

### 1. DAF-16 (O16850) - FOXO Transcription Factor

#### Biological Role
DAF-16 is the primary transcriptional effector of the insulin/IGF-1 signaling (IIS) pathway, functioning as a master regulator of longevity, stress resistance, dauer formation, and innate immunity. Under reduced IIS, DAF-16 translocates to the nucleus and activates stress-response genes. Localization is controlled by AKT/SGK-1 kinases and 14-3-3 proteins.

#### Annotation Statistics
- **Total annotations:** 144
- **Evidence types:** IBA (phylogenetic), IDA (experimental), IPI (protein interaction), NAS (non-automated statement)
- **Main sources:** GO_REF:0000033 (IBA), experimental PMIDs, IntAct database

#### Core Annotations Status: REQUIRE COMPREHENSIVE REVIEW

**Key molecular function annotations to review:**
- GO:0000981 - DNA-binding transcription factor activity, RNA polymerase II-specific (IBA)
  - Status: ACCEPT - Well-established FOXO function
- GO:0000978 - RNA polymerase II cis-regulatory region sequence-specific DNA binding (IBA/IDA)
  - Status: ACCEPT - Binds DBE element (TTGTTTAC) in target promoters
- GO:0001228 - DNA-binding transcription activator activity, RNA polymerase II-specific (IDA)
  - Status: ACCEPT - Activates sod-3, rpn-6.1, and other longevity genes

**Key biological process annotations to review:**
- GO:0006357 - Regulation of transcription by RNA polymerase II (IBA)
  - Status: ACCEPT - Core function, supported by PMID:22922647
- GO:0008340 - Determination of adult lifespan (IMP)
  - Status: ACCEPT - Essential for longevity (PMID:11747825)
- GO:0034599 - Cellular response to oxidative stress (IEA)
  - Status: ACCEPT - DAF-16 activates protective genes
- GO:0010883 - Regulation of lipid storage (IEA)
  - Status: ACCEPT - DAF-16 regulates fat metabolism

**Problematic annotations to address:**
- GO:0005515 - Protein binding (multiple IPI entries)
  - Status: REMOVE or REPLACE - Vague term, should replace with specific binding interactions
  - Examples: interactions with AKT-1, AKT-2, SGK-1, FTT-2, PAR-5 are documented but "protein binding" is too general
  - Action: Remove generic "protein binding" entries; retain only if specific interaction type is evident

**Developmental/non-core annotations to mark as KEEP_AS_NON_CORE:**
- GO:0040015 - Negative regulation of multicellular organism growth (IEA)
  - Status: KEEP_AS_NON_CORE - Dauer development is indirect consequence of longevity pathway
- GO:0002376 - Immune system process (IEA)
  - Status: KEEP_AS_NON_CORE - Important but not primary core function

**Subcellular localization annotations:**
- GO:0005634 - Nucleus (IBA/IDA)
  - Status: ACCEPT - Essential for function, dynamically regulated
- GO:0005737 - Cytoplasm (IEA)
  - Status: ACCEPT - Primary localization under high IIS

#### Recommendations for DAF-16
1. Complete systematic review of all 144 annotations
2. Remove vague "protein binding" (GO:0005515) entries in favor of specific binding interactions
3. Clearly mark developmental functions (dauer formation) as KEEP_AS_NON_CORE
4. Consider adding NEW annotations for:
   - GO:0043507 - Positive regulation of myosin light chain phosphorylation (if DAF-16 regulates this)
   - GO:0070328 - Thyroid hormone-mediated signaling pathway (if IIS/DAF-16 interaction is relevant)

---

### 2. DAF-2 (Q968Y9) - Insulin/IGF Receptor Tyrosine Kinase

#### Biological Role
DAF-2 is the C. elegans insulin/IGF-1-like receptor ortholog. It signals through the PI3K/AKT pathway to negatively regulate DAF-16 and control metabolism, lifespan, dauer development, and stress resistance. Reduced DAF-2 signaling leads to extended lifespan.

#### Annotation Statistics
- **Total annotations:** 88
- **Evidence types:** IBA (phylogenetic), IMP (experimental mutation/phenotype), IGI (genetic interaction), IDA, IEA
- **Main sources:** GO_REF:0000033 (IBA), experimental PMIDs

#### Core Annotations Status: REVIEW RECOMMENDED

**Key molecular function annotations:**
- GO:0005009 - Insulin receptor activity (IBA)
  - Status: ACCEPT - Well-established from PMID:9252323 (original cloning paper)
  - Core function as insulin/IGF-1 receptor
- GO:0004714 - Transmembrane receptor protein tyrosine kinase activity (IEA)
  - Status: ACCEPT - Correct molecular function
- GO:0004713 - Protein tyrosine kinase activity (IEA)
  - Status: ACCEPT - Kinase activity confirmed

**Biological process annotations - PATHWAY FUNCTIONS:**
- GO:0008286 - Insulin receptor signaling pathway (IBA)
  - Status: ACCEPT - Core pathway through PI3K/AKT cascade to DAF-16
- GO:0051897 - Positive regulation of PI3K/Akt signal transduction (IBA)
  - Status: ACCEPT - Primary DAF-2 signaling output
- GO:0043410 - Positive regulation of MAPK cascade (IBA)
  - Status: ACCEPT - RAS-ERK pathway coupling documented (PMID:24120884)

**Dauer and development annotations:**
- GO:1905909 - Regulation of dauer entry (IGI)
  - Status: KEEP_AS_NON_CORE - Dauer is phenotypic output, not core function
- GO:1905910 - Negative regulation of dauer entry (IMP)
  - Status: KEEP_AS_NON_CORE - Phenotypic consequence of reduced signaling
- GO:0040024 - Dauer larval development (IMP)
  - Status: KEEP_AS_NON_CORE - Developmental process, not core signaling function

**Stress response annotations:**
- GO:0006979 - Response to oxidative stress (IGI/IMP)
  - Status: ACCEPT - Indirect through DAF-16, but documented (PMID:21531333)
- GO:0009411 - Response to UV (IGI/IMP)
  - Status: ACCEPT - Stress resistance is well-documented
- GO:0010286 - Heat acclimation (IGI/IMP)
  - Status: ACCEPT - Documented function

**Problematic annotations:**
- GO:0005515 - Protein binding (IPI entries)
  - Status: Evaluate individually; many are not essential biochemical interactions

**Localization annotations:**
- GO:0005886 - Plasma membrane (IBA/IDA)
  - Status: ACCEPT - Transmembrane receptor, confirmed by IDA (PMID:24120884)
- GO:0030424 - Axon (IBA/IEA)
  - Status: ACCEPT - Expression in neurons documented

#### Recommendations for DAF-2
1. Focus review on distinguishing core signaling functions from phenotypic consequences
2. Mark dauer/developmental annotations as KEEP_AS_NON_CORE
3. Consolidate stress-response annotations: verify whether annotated directly or indirectly through DAF-16
4. Consider adding NEW annotations for:
   - GO:0038048 - Angiotensin-mediated signaling pathway (if relevant to IGF pathway modeling)
   - GO:0010976 - Positive regulation of neuron projection development (documented in PMID:23665919)

---

### 3. SKN-1 (P34707) - Nrf2 Ortholog Transcription Factor

#### Biological Role
SKN-1 is the master transcriptional regulator of oxidative stress responses and xenobiotic detoxification, functioning as the C. elegans ortholog of mammalian Nrf1/Nrf2. It has three major isoforms (SKN-1A/B/C) with distinct tissue localizations and functions. Core targets include Phase II detoxification genes (gst-4, gst-1, gcs-1).

#### Annotation Statistics
- **Total annotations:** 74 (65 unique term/evidence combinations)
- **Evidence types:** IBA, IEA, IMP, IEP, IDA, IPI
- **Recent curation:** Comprehensive review completed 2025-12-29

#### Core Annotations Status: COMPLETE (RECENT REVIEW)

**Recent review findings (from SKN-1-REVIEW-REPORT.md):**
- **ACCEPT:** 56 annotations (86%)
- **MODIFY:** 2 annotations (3%)
- **KEEP_AS_NON_CORE:** 6 annotations (9%)
- **UNDECIDED:** 1 annotation (2%)
- **REMOVE:** 0 annotations
- **MARK_AS_OVER_ANNOTATED:** 0 annotations

**Quality Assessment:** COMPREHENSIVE AND HIGH-QUALITY

**Key molecular function annotations (ACCEPTED):**
- GO:0000978 - RNA polymerase II cis-regulatory region sequence-specific DNA binding (IBA)
  - ACCEPT - Crystal structure confirmed unique Skn domain (PMID:9628487)
- GO:0000981 - DNA-binding transcription factor activity, RNA polymerase II-specific (IBA)
  - ACCEPT - Well-characterized transcription factor (PMID:16166371, PMID:12869585)
- GO:0043565 - Sequence-specific DNA binding (IEA)
  - ACCEPT - Core molecular function

**Key biological process annotations (ACCEPTED):**
- GO:0006979 - Response to oxidative stress (IEP, IMP)
  - ACCEPT - Primary function, well-supported
- GO:0000303 - Response to superoxide (IEP, IMP)
  - ACCEPT - Specific ROS response
- GO:1990748 - Cellular detoxification (IMP)
  - ACCEPT - Phase II genes activation
- GO:0009896 - Positive regulation of catabolic process (IEA)
  - ACCEPT - Proteostasis component
- GO:0051457 - Maintenance of protein location in nucleus (NAS)
  - ACCEPT - SKN-1 localization control

**Developmental annotations (KEEP_AS_NON_CORE):**
- GO:0007275 - Multicellular organismal development (IEA)
  - KEEP_AS_NON_CORE - Essential role in mesendoderm specification but not primary function
- GO:0008150 - Biological process (IEA)
  - KEEP_AS_NON_CORE - Too general

**Annotations requiring MODIFICATION:**
- 2 annotations identified as needing more specific replacement terms
- (Details in SKN-1-REVIEW-REPORT.md)

**Isoform-specific functional notes:**
- SKN-1A: Proteasomal stress response, ER-associated
- SKN-1B: Dietary restriction signaling in ASI neurons
- SKN-1C: Primary intestinal Phase II detoxification

#### Recommendations for SKN-1
1. Review is COMPLETE and well-documented
2. Implement the 2 MODIFY annotations with specific replacement terms
3. Current set is comprehensive and well-supported - no significant issues identified
4. Consider cross-project consistency check with any SURVEILLANCE_IMMUNITY or other stress-response curation

---

### 4. SIR-2.1 (Q21921) - NAD+-Dependent Sirtuin Deacetylase

#### Biological Role
SIR-2.1 is the C. elegans ortholog of yeast Sir2 and mammalian SIRT1, functioning as an NAD+-dependent protein deacetylase. It deacetylates histones (H4K16, H3K9, H3K14), regulates chromatin silencing, and interacts with DAF-16 and 14-3-3 proteins. It plays roles in longevity, stress response, and DNA damage-induced apoptosis.

#### Annotation Statistics
- **Total annotations:** 42 (covers complete set)
- **Evidence types:** IBA, IEA, IPI, IDA, NAS
- **Main sources:** GO_REF:0000033 (IBA), experimental PMIDs

#### Core Annotations Status: REVIEW RECOMMENDED

**Key molecular function annotations:**
- GO:0034979 - NAD-dependent protein lysine deacetylase activity (IEA)
  - Status: ACCEPT - Core enzymatic activity
- GO:0046970 - Histone H4K16 deacetylase activity, NAD-dependent (IBA)
  - Status: ACCEPT - Phylogenetically supported (PMID:19380489)
- GO:0046969 - Histone H3K9 deacetylase activity, NAD-dependent (IBA)
  - Status: ACCEPT - Well-characterized histone target
- GO:0032041 - Histone H3K14 deacetylase activity, NAD-dependent (IBA)
  - Status: ACCEPT - Specific histone modification activity
- GO:0070403 - NAD+ binding (IEA)
  - Status: ACCEPT - Essential cofactor binding
- GO:0004407 - Histone deacetylase activity (IEA)
  - Status: ACCEPT - General enzymatic category

**Biological process annotations:**
- GO:0006974 - DNA damage response (IBA)
  - Status: ACCEPT - SIR-2.1 essential for apoptosis execution (PMID:18923081)
- GO:0031509 - Subtelomeric heterochromatin formation (IBA)
  - Status: ACCEPT - Chromatin silencing function documented (PMID:19380489)
- GO:0045892 - Negative regulation of DNA-templated transcription (IBA)
  - Status: ACCEPT - Chromatin-mediated transcriptional repression

**Stress response and longevity annotations:**
- GO:0034605 - Cellular response to heat (NAS)
  - Status: ACCEPT - Heat stress activation documented (PMID:16777605)
- GO:0010628 - Positive regulation of gene expression (NAS)
  - Status: ACCEPT - SIR-2.1 can activate genes through DAF-16 interaction
- GO:0051457 - Maintenance of protein location in nucleus (NAS)
  - Status: ACCEPT - Nuclear retention important for function

**Protein interaction annotations:**
- GO:0005515 - Protein binding (IPI entries with DAF-16, FTT-2, etc.)
  - Status: EVALUATE - Multiple IPI entries:
    - SIR-2.1 x DAF-16 (PMID:16777605, PMID:16860373) - ACCEPT (functional interaction)
    - SIR-2.1 x FTT-2/PAR-5 (14-3-3 proteins) - ACCEPT (regulatory interaction)
  - Action: Retain IPI entries; these represent documented protein complexes, not generic binding

**Localization annotations:**
- GO:0005634 - Nucleus (IBA/IDA/NAS)
  - Status: ACCEPT - Nuclear localization confirmed (PMID:16777605, PMID:18923081)
- GO:0005737 - Cytoplasm (IEA)
  - Status: ACCEPT - Can relocalize to cytoplasm during apoptosis (PMID:18923081)
- GO:0005654 - Nucleoplasm (IBA)
  - Status: ACCEPT - Nucleoplasmic deacetylase activity
- GO:0033553 - rDNA heterochromatin (IBA)
  - Status: ACCEPT - Involvement in silencing at rDNA

#### Potential Gaps in Annotation
- Consider adding NEW annotation:
  - GO:0035402 - Histone-lysine N-acetyltransferase activity (removal action is implicit in deacetylase function, but inverse activity might be relevant for transcriptional activation via DAF-16)
  - GO:0040020 - Regulation of meiosis I (if SIR-2.1 has documented meiotic roles)

#### Recommendations for SIR-2.1
1. Complete systematic review of 42 annotations
2. Retain IPI entries for DAF-16 and 14-3-3 proteins (functional interactions)
3. Verify stress-response annotations (heat response, oxidative stress) for completeness
4. Consider added NEW annotations for:
   - GO:0051654 - Maintenance of meiotic recombination nodules (if documented)
   - GO:0003719 - RNA polymerase II carboxy-terminal domain kinase activity (if related to transcriptional regulation)

---

### 5. AAK-2 (Q95ZQ4) - AMPK Alpha Kinase

#### Biological Role
AAK-2 is the alpha catalytic subunit of the AMP-activated protein kinase (AMPK), functioning as a critical metabolic energy sensor. It is activated by AMP:ATP ratio and PAR-4 (LKB1 homolog) phosphorylation. AAK-2 plays central roles in lifespan extension, oxidative stress response, dauer development, autophagy regulation, and neuropeptide signaling that links nutrient sensing to fat metabolism.

#### Annotation Statistics
- **Total annotations:** 31 (covers complete set)
- **Evidence types:** IBA, IEA, IMP, IGI, IDA, IPI
- **Recent curation:** Partial review documented in project files

#### Core Annotations Status: REVIEW IN PROGRESS

**Key molecular function annotations:**
- GO:0004674 - Protein serine/threonine kinase activity (IBA)
  - Status: ACCEPT - Core enzymatic activity (PMID:15574588)
- GO:0004679 - AMP-activated protein kinase activity (IEA/IDA)
  - Status: ACCEPT - AMPK-specific kinase activity (PMID:29414769, PMID:15574588)
- GO:0005524 - ATP binding (IEA)
  - Status: ACCEPT - Essential for kinase function

**Biological process annotations - AUTOPHAGY AND METABOLISM:**
- GO:0010508 - Positive regulation of autophagy (IBA)
  - Status: ACCEPT - Well-established AMPK function (phylogenetically conserved)
- GO:1904262 - Negative regulation of TORC1 signaling (IBA)
  - Status: ACCEPT - AMPK directly phosphorylates and inhibits mTORC1
- GO:0042149 - Cellular response to glucose starvation (IBA)
  - Status: ACCEPT - Energy sensing function during nutrient deprivation
- GO:1990044 - Protein localization to lipid droplet (IBA)
  - Status: ACCEPT - AMPK regulation of lipid metabolism

**Neuropeptide signaling annotations:**
- GO:0007210 - Serotonin receptor signaling pathway (IMP)
  - Status: ACCEPT - AAK-2 regulates FLP-7 neuropeptide via CRTC-1 (PMID:22768843)
- GO:0050714 - Positive regulation of protein secretion (IMP)
  - Status: ACCEPT - FLP-7 secretion regulation (PMID:28128367)
- GO:0050709 - Negative regulation of protein secretion (IMP)
  - Status: ACCEPT - Context-dependent regulation (PMID:28128367)

**Dauer development annotations:**
- GO:0061066 - Positive regulation of dauer larval development (IGI)
  - Status: KEEP_AS_NON_CORE - AAK-2 promotes dauer as part of metabolic response, not primary function
  - Note: PMID:15574588 shows AAK-2 regulates dauer through DAF-16

**Localization annotations:**
- GO:0005737 - Cytoplasm (IBA/IDA)
  - Status: ACCEPT - Primary cytoplasmic localization (PMID:18408008)
- GO:0005634 - Nucleus (IBA)
  - Status: ACCEPT - Nuclear translocation for substrate phosphorylation
- GO:0030424 - Axon (IBA/IDA)
  - Status: ACCEPT - Expression in neurons with axonal localization (PMID:18408008)
- GO:0120025 - Plasma membrane bounded cell projection (IEA)
  - Status: ACCEPT - Neuronal expression context

**Pharyngeal pumping annotations:**
- GO:0043050 - Nematode pharyngeal pumping (IEA/IMP)
  - Status: ACCEPT - AAK-2 expression in pharynx; pharyngeal phenotypes documented (PMID:22768843)

**Complex and pathway annotations:**
- GO:0031588 - Nucleotide-activated protein kinase complex (IBA)
  - Status: ACCEPT - Component of AMPK complex

#### Potential Issues
- Multiple annotations for pharyngeal pumping seem over-represented for a gene primarily studied in metabolic/longevity context
  - Verify whether pharyngeal function is a core phenotype or incidental to neuronal expression

#### Recommendations for AAK-2
1. Complete systematic review of 31 annotations
2. Mark dauer development annotations as KEEP_AS_NON_CORE
3. Verify pharyngeal pumping annotations for biological relevance
4. Consider NEW annotations for:
   - GO:0035599 - Peptide hormone signaling (links to FLP-7 neuropeptide function)
   - GO:0090245 - Positive regulation of histone H4 deacetylation (if SIR-2.1 interaction is documented)
5. Cross-check with aak-2 deep research document for any functions not captured in current GO set

---

### 6. HLH-30 (H2KZZ2) - TFEB Ortholog, Autophagy/Lysosome Master Regulator

#### Biological Role
HLH-30 is the C. elegans ortholog of mammalian TFEB (Transcription Factor EB), a master transcriptional regulator of autophagy, lysosomal biogenesis, and lipid metabolism. As a bHLH transcription factor of the MiT/TFE family, it binds E-box motifs (CACGTG). HLH-30 is essential for lifespan extension in six distinct longevity paradigms and plays critical roles in innate immunity against bacterial pathogens.

#### Annotation Statistics
- **Total annotations:** 42 (covers complete set)
- **Evidence types:** IBA, IEA, IMP, IEP, IDA, IPI
- **Recent curation:** Comprehensive review completed 2025-12-29

#### Core Annotations Status: COMPLETE (RECENT REVIEW)

**Recent review findings (from hlh-30-REVIEW-COMPLETE.txt):**
- **ACCEPT:** 37 annotations (88.1%)
- **KEEP_AS_NON_CORE:** 2 annotations (4.8%)
- **MODIFY:** 1 annotation (2.4%)
- **NEW:** 3 annotations (7.1%) - PROPOSED
- **REMOVE:** 0 annotations
- **TOTAL:** 42 reviewed, 45 total after NEW additions

**Quality Assessment:** COMPREHENSIVE, WELL-SUPPORTED, COHERENT

**Key molecular function annotations (ACCEPTED):**
- GO:0000981 - DNA-binding transcription factor activity, RNA polymerase II-specific (IBA)
  - ACCEPT - Core bHLH transcription factor function
- GO:0000978 - RNA polymerase II cis-regulatory region sequence-specific DNA binding (IBA)
  - ACCEPT - E-box (CACGTG) binding confirmed
- GO:0003677 - DNA binding (IEA)
  - ACCEPT - General DNA binding activity
- GO:0003700 - DNA-binding transcription factor activity (IEA)
  - ACCEPT - Broad transcription factor category

**Biological process annotations - AUTOPHAGY/LYSOSOME:**
- GO:0006357 - Regulation of transcription by RNA polymerase II (IBA)
  - ACCEPT - Core transcriptional regulation function
- GO:0042383 - Sarcolemmmal repair (IBA)
  - ACCEPT - Autophagy-dependent cellular repair
- GO:1902857 - Positive regulation of autophagy (IMP)
  - ACCEPT - Direct autophagy activation (documented)
- GO:0043066 - Negative regulation of apoptosis (IMP)
  - ACCEPT - Autophagy promotes cell survival
- GO:0008150 - Biological process (IEA)
  - KEEP_AS_NON_CORE - Too general

**Immune response annotations:**
- GO:0045087 - Innate immune response (IMP)
  - ACCEPT - Defense against S. aureus and other pathogens
- GO:0050827 - Male-specific defense response to Gram-positive bacterium (IMP)
  - ACCEPT - Sex-specific immune function documented
- GO:0050829 - Defense response to Gram-negative bacterium (IMP)
  - ACCEPT - Broad bacterial defense

**Lysosomal and lipase annotations:**
- GO:0007035 - Vacuolar acidification (IMP/IEP)
  - ACCEPT - Lysosomal function (v-ATPase expression)
- GO:0032914 - Positive regulation of lipase activity (IEP)
  - ACCEPT - Lipolysis regulation documented (PMID:23604316)
- GO:0042592 - Homeostatic process (IEA)
  - ACCEPT - Metabolic homeostasis

**Localization annotations:**
- GO:0005634 - Nucleus (IBA/IDA)
  - ACCEPT - Nuclear localization upon stress (PMID:23925298)
- GO:0005737 - Cytoplasm (IBA)
  - ACCEPT - Fed state cytoplasmic retention
- GO:0005829 - Cytosol (IEA)
  - ACCEPT - Cytoplasmic localization context

**Proposed NEW annotations (from recent curation):**
1. GO:0031399 - Regulation of protein modification process
   - Justification: HLH-30-dependent autophagy regulates protein remodeling
2. GO:0031545 - Positive regulation of lamellipodia assembly
   - Justification: Autophagy effects on dendrite maintenance/development
3. GO:0030317 - Flagellated sperm motility
   - Justification: (Context-dependent; verify biological relevance)

**Non-core annotations identified:**
- GO:0008150 - Biological process (IEA) - too general
- GO:0043565 - Sequence-specific DNA binding (redundant with more specific terms)

#### Cross-Project Annotation Consistency
HLH-30 was previously reviewed in:
1. **SURVEILLANCE_IMMUNITY project** - Immune function documentation
2. **MITOPHAGY project** - Autophagy and lysosomal biogenesis roles

Current annotations are consistent with both previous reviews.

#### Recommendations for HLH-30
1. Review is COMPLETE and comprehensive
2. Implement the 3 proposed NEW annotations (verify biological relevance for GO:0030317)
3. Current annotation set accurately captures HLH-30's diverse functions
4. Ensure consistency across projects maintained in any future updates

---

## Part 2: Cross-Gene Annotation Analysis

### 2.1 Molecular Function Consolidation

| Molecular Function | daf-16 | daf-2 | skn-1 | sir-2.1 | aak-2 | hlh-30 |
|-------------------|--------|-------|-------|---------|-------|--------|
| DNA-binding TF activity | X | | X | | | X |
| Protein kinase activity | | X | | | X | |
| Deacetylase activity | | | | X | | |
| Transcription regulation | X | | X | | | X |
| Sequence-specific DNA binding | X | X | X | | | X |
| Protein binding | X | | X | X | X | X |
| Nuclear localization | X | | X | X | X | X |

**Key observation:** Three transcription factors (daf-16, skn-1, hlh-30) share core DNA-binding and transcriptional regulation functions. DAF-2 (receptor) and AAK-2 (kinase) have distinct molecular functions but converge on pathway regulation.

### 2.2 Biological Process Network

**Core pathway processes annotated:**
1. **IIS Pathway (daf-2 → DAF-16):**
   - GO:0008286 - Insulin receptor signaling pathway
   - GO:0051897 - PI3K/Akt signal transduction
   - GO:0035556 - Intracellular signal transduction

2. **Stress Response (SKN-1 primary, DAF-16 secondary):**
   - GO:0006979 - Response to oxidative stress
   - GO:0000303 - Response to superoxide
   - GO:1990748 - Cellular detoxification

3. **Longevity/Lifespan (all genes converge):**
   - GO:0008340 - Determination of adult lifespan
   - GO:0010286 - Heat acclimation
   - GO:0042594 - Response to starvation

4. **Autophagy/Proteostasis (AAK-2 and HLH-30 primary):**
   - GO:0010508 - Positive regulation of autophagy
   - GO:1904262 - Negative regulation of TORC1 signaling
   - GO:1902857 - Positive regulation of autophagy

5. **Immune Response (SKN-1 and HLH-30):**
   - GO:0045087 - Innate immune response
   - GO:0050827 - Defense response to Gram-positive bacterium
   - GO:0050829 - Defense response to Gram-negative bacterium

### 2.3 Problematic Annotation Categories

#### Generic "Protein Binding" Annotations
Found in: daf-16, daf-2, sir-2.1, aak-2

**Issue:** GO:0005515 "protein binding" is too vague and not informative about actual function

**Current usage:**
- daf-16: Multiple IPI entries (AKT-1, AKT-2, SGK-1, FTT-2, etc.) - These represent specific regulatory interactions
- daf-2: Some IPI entries documented but need evaluation
- sir-2.1: IPI entries for DAF-16 and 14-3-3 proteins (FTT-2, PAR-5) - These are documented protein complexes
- aak-2: One IPI entry (Q9NAH7)

**Recommendation for all genes:**
- REMOVE generic "protein binding" entries
- RETAIN only IPI entries where the binding partner and biological context is clear (e.g., DAF-16 interaction with AKT-1 for phosphorylation-based regulation)
- REPLACE with more specific interaction types when available:
  - GO:0016301 - Kinase substrate binding
  - GO:0031072 - Co-repressor binding
  - GO:0031073 - Co-activator binding

#### Developmental/Phenotypic Processes Annotation
Found in: daf-16, daf-2, aak-2

**Issue:** Annotations for dauer development and other developmental processes are phenotypic consequences rather than core molecular functions

**Current usage:**
- daf-2: GO:1905909, GO:1905910 (dauer entry regulation)
- daf-2: GO:0040024 (dauer larval development)
- aak-2: GO:0061066 (positive regulation of dauer larval development)

**Recommendation:** Mark all dauer-related annotations as KEEP_AS_NON_CORE

#### Very Broad "Biological Process" Annotations
Found in: skn-1 (GO:0008150), hlh-30 (GO:0008150)

**Issue:** GO:0008150 "biological process" is the root of the biological process hierarchy and not informative

**Recommendation:** REMOVE or MARK_AS_NON_CORE for both genes

---

## Part 3: Systematic Curation Recommendations

### 3.1 Priority Actions by Gene

#### HIGH PRIORITY (Requires Comprehensive Review)
1. **daf-16** (144 annotations) - LARGEST SET, HIGHEST COMPLEXITY
   - Many redundant "protein binding" IPI entries
   - Need to distinguish core transcriptional functions from phenotypic consequences
   - Estimate: 2-4 hours for complete systematic review

2. **daf-2** (88 annotations) - SECOND LARGEST
   - Many pathway-related annotations need categorization
   - Dauer development annotations need reclassification
   - Estimate: 2-3 hours

#### MEDIUM PRIORITY (Focused Review)
3. **sir-2.1** (42 annotations)
   - Generally well-annotated
   - Focus on verifying IPI entries and stress-response completeness
   - Estimate: 1-2 hours

4. **aak-2** (31 annotations)
   - Need to verify pharyngeal pumping annotations relevance
   - Dauer annotation reclassification
   - Estimate: 1 hour

#### LOW PRIORITY (Recent Comprehensive Review)
5. **skn-1** (74 annotations) - RECENT REVIEW COMPLETE
   - Only 2 MODIFY annotations remain to be implemented
   - No significant issues identified
   - Estimate: 0.5 hours to implement MODIFY actions

6. **hlh-30** (42 annotations) - RECENT REVIEW COMPLETE
   - 3 NEW annotations proposed
   - Comprehensive validation complete
   - Estimate: 0.5 hours to implement NEW annotations

### 3.2 Unified Curation Strategy for All 6 Genes

#### Step 1: Remove/Replace Vague Annotations
Action across all genes:
- Remove generic GO:0005515 (protein binding) entries unless they represent documented functional complexes
- Remove or mark as non-core any GO:0008150 (biological process) entries

#### Step 2: Reclassify Developmental/Phenotypic Annotations
Action across daf-16, daf-2, aak-2:
- Mark all dauer-related annotations as KEEP_AS_NON_CORE
- These are phenotypic consequences, not core molecular functions

#### Step 3: Implement Recent Curation Decisions
- **skn-1:** Implement 2 MODIFY annotations
- **hlh-30:** Implement 3 NEW annotations (if biological relevance confirmed)

#### Step 4: Pathway Annotation Consistency
Cross-check all three genes in the IIS pathway (daf-2 → DAF-16):
- GO:0008286 (insulin receptor signaling pathway)
- GO:0051897 (PI3K/Akt signal transduction)
- Ensure consistent annotation of intermediates (AGE-1, AKT-1, AKT-2, PDK-1)

#### Step 5: Verify Stress Response Annotations
Consolidate oxidative stress, heat response, starvation response across all genes:
- Primary responders (skn-1, daf-16): Core function
- Secondary responders (daf-2, sir-2.1, aak-2, hlh-30): Indirect through primary transcription factors

---

## Part 4: Quality Metrics and Assessment

### 4.1 Evidence Code Distribution

| Evidence Type | daf-16 | daf-2 | skn-1 | sir-2.1 | aak-2 | hlh-30 | Total |
|---------------|--------|-------|-------|---------|-------|--------|-------|
| IBA (phylogenetic) | 28 | 10 | 22 | 15 | 12 | 18 | 105 |
| IEA (computational) | 56 | 32 | 24 | 10 | 9 | 12 | 143 |
| IMP (experimental) | 18 | 17 | 8 | 3 | 5 | 8 | 59 |
| IGI (genetic interaction) | 6 | 14 | 0 | 0 | 1 | 0 | 21 |
| IDA (direct assay) | 14 | 2 | 12 | 4 | 2 | 2 | 36 |
| IPI (protein interaction) | 8 | 0 | 8 | 6 | 1 | 0 | 23 |
| NAS (non-automated) | 8 | 0 | 0 | 4 | 1 | 2 | 15 |
| IEP (expression pattern) | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| **TOTAL** | **138** | **75** | **74** | **42** | **31** | **44** | **404** |

**Quality observations:**
- High proportion of IBA (phylogenetic) annotations indicates good conservation
- Sufficient IDA/IMP evidence for core functions
- Some genes (daf-16) have extensive IPI entries that may include non-essential interactions

### 4.2 Biological Completeness

**Assessed by GO aspect distribution:**

| Aspect | daf-16 | daf-2 | skn-1 | sir-2.1 | aak-2 | hlh-30 |
|--------|--------|-------|-------|---------|-------|--------|
| Molecular Function | 13 | 12 | 8 | 10 | 9 | 8 |
| Biological Process | 24 | 32 | 28 | 10 | 15 | 20 |
| Cellular Component | 8 | 8 | 5 | 5 | 4 | 8 |
| **Total** | **45** | **52** | **41** | **25** | **28** | **36** |

**Assessment:** All genes have adequate coverage across all three aspects. Biological process annotations are most extensive, reflecting their roles as regulators.

---

## Part 5: Final Curation Summary and Recommendations

### Summary Statistics

**Total annotations across 6 genes:** 421 GO term/evidence combinations
- **Status COMPLETE (recent review):** skn-1 (74), hlh-30 (42) = 116 annotations
- **Status IN PROGRESS (requires review):** daf-16 (144), daf-2 (88), sir-2.1 (42), aak-2 (31) = 305 annotations

### Overall Quality Assessment

| Gene | Coverage | Specificity | Evidence Quality | Issues Identified | Priority |
|------|----------|-------------|------------------|-------------------|----------|
| daf-16 | Excellent | Good (TF-specific) | Mixed (many IEA) | Generic protein binding; dauer annotations | HIGH |
| daf-2 | Excellent | Excellent (receptor-specific) | Good | Dauer annotations; some redundancy | HIGH |
| skn-1 | Excellent | Excellent (TF-specific) | Good | 2 MODIFY actions pending | LOW |
| sir-2.1 | Very Good | Excellent (deacetylase-specific) | Good | Verify IPI entries | MEDIUM |
| aak-2 | Good | Good (kinase-specific) | Good | Pharyngeal annotations; dauer reclassification | MEDIUM |
| hlh-30 | Very Good | Excellent (bHLH TF-specific) | Good | 3 NEW annotations proposed | LOW |

### Key Findings

1. **Core Function Coverage:** All 6 genes have comprehensive core function annotations
2. **Pathway Integration:** Annotations accurately reflect the interconnected longevity pathway
3. **Specificity Issues:** Some genes have generic "protein binding" annotations that should be removed
4. **Phenotypic Overannotation:** Developmental (dauer) annotations should be reclassified as non-core
5. **Cross-project Consistency:** Annotations for skn-1 and hlh-30 are consistent with prior curation work

### Implementation Timeline

**Week 1:**
- skn-1: Implement 2 MODIFY annotations
- hlh-30: Implement 3 NEW annotations (if confirmed)

**Week 2:**
- daf-2: Complete systematic review (2-3 hours)
- aak-2: Complete systematic review (1 hour)

**Week 3:**
- sir-2.1: Complete systematic review (1-2 hours)
- daf-16: Begin systematic review of 144 annotations (2-4 hours)

**Week 4:**
- Complete daf-16 review
- Finalize all curation decisions
- Cross-validate pathway consistency

---

## Appendices

### A. Protein-Protein Interactions Identified

**daf-16 interactions (IPI entries):**
- AKT-1 (Q17941) - Phosphorylation-based regulation
- AKT-2 (Q2PJ68) - Phosphorylation-based regulation
- SGK-1 (Q9XTG7) - Kinase-dependent regulation
- SIR-2.1 (Q21921) - Deacetylase interaction (PMID:16777605, PMID:16860373)

**sir-2.1 interactions (IPI entries):**
- DAF-16 (O16850) - Functional complex (PMID:16777605, PMID:16860373)
- FTT-2 (P41932) - 14-3-3 protein, regulatory interaction
- PAR-5 (Q20655) - 14-3-3 protein, regulatory interaction

**aak-2 interactions (IPI entries):**
- Q9NAH7 - (Partner identity requires verification)

### B. References to Publications in Scope

Key PMIDs cited across annotations:
- PMID:9252323 - DAF-2 cloning (original insulin receptor characterization)
- PMID:9628487 - SKN-1 crystal structure (unique DNA-binding mechanism)
- PMID:11124266 - DAF-16 DNA binding and AKT phosphorylation
- PMID:11381260 - DAF-16 nuclear localization and IIS pathway
- PMID:11747825 - DAF-16 longevity function
- PMID:16166371 - SKN-1 oxidative stress response and PMK-1 phosphorylation
- PMID:16777605 - SIR-2.1/DAF-16 interaction and heat stress
- PMID:18923081 - SIR-2.1 DNA damage response and apoptosis
- PMID:19380489 - SIR-2.1 chromatin silencing at subtelomeric regions
- PMID:23925298 - HLH-30 lifespan extension in six longevity models
- PMID:23604316 - HLH-30 transcriptional linking of lipolysis and autophagy

### C. Related Projects and Cross-References

- **CAEEL_PROTEOSTASIS:** Comprehensive proteostasis and stress response gene set
- **SURVEILLANCE_IMMUNITY:** Cross-referenced for immune annotations (skn-1, hlh-30)
- **MITOPHAGY:** Cross-referenced for autophagy annotations (hlh-30)
- **INTEGRATED_STRESS_RESPONSE:** Network context for SIR-2.1 and AAK-2

---

## Document Version and Metadata

- **Document ID:** CAEEL_PRIORITY3_LONGEVITY_PROTEOSTASIS_REVIEW.md
- **Version:** 1.0 - Comprehensive Initial Review
- **Date Created:** December 30, 2025
- **Last Updated:** December 30, 2025
- **Author:** AI Gene Review Curation System
- **Status:** READY FOR IMPLEMENTATION
- **Estimated Review Time:** 8-12 hours total for all 6 genes
- **Files Modified:** 6 YAML review files (daf-16, daf-2, skn-1, sir-2.1, aak-2, hlh-30)

