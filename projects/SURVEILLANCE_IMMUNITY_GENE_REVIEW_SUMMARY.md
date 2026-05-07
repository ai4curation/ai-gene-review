# GO Annotation Review Summary: C. elegans Priority 3 Surveillance Immunity Genes

**Date:** 2025-12-29
**Reviewer:** AI Gene Review Curator
**Scope:** Systematic review of 6 C. elegans innate immunity genes for GO annotation quality

## Overview

This document provides a comprehensive curation summary for 6 Priority 3 C. elegans surveillance immunity genes. The genes encompass the major pathway components: master stress/immune transcription factor (daf-16), TGF-beta ligand (dbl-1), STAT-like transcription factor (sta-2), Tribbles kinase adapter (nipi-3), lysozyme effector (lys-7), and C-type lectin effector (clec-60).

**Total annotations across 6 genes: 238**
- daf-16: 144 annotations (IBA, IDA, IMP, IGI, IPI, NAS, TAS, IEA, IEP, IEP)
- dbl-1: 32 annotations (IBA, IMP, IGI, ISS, IEA)
- sta-2: 27 annotations (IBA, IMP, IDA, IPI, IEA)
- nipi-3: 18 annotations (IBA, IEA, IMP, IPI)
- lys-7: 18 annotations (IBA, IEA, IMP, IGI)
- clec-60: 1 annotation (IGI)

## Summary of Curation Recommendations by Gene

---

## 1. DAF-16 (O16850) - FOXO Transcription Factor (144 annotations)

### Gene Summary
DAF-16 is the C. elegans FOXO ortholog and master transcription factor downstream of the DAF-2/insulin-like signaling pathway. It integrates stress responses (oxidative stress, heat, starvation, UV) and immune defense. DAF-16 is a pluripotent regulator with roles spanning longevity, dauer formation, innate immunity, metabolism, and development. It functions as both a transcriptional activator and repressor depending on context.

### Overall Assessment
The annotation set is comprehensive and well-curated, reflecting both IBA phylogenetic inferences and extensive experimental evidence. The collection includes some over-annotations and pleiotropic developmental roles that should be categorized as NON-CORE. The large annotation set (144) accurately reflects the pleiotropic nature of FOXO transcription factors.

### Key Curation Issues

#### ISSUE 1: Protein Binding Annotations (Multiple entries)
**Problem:** Multiple generic GO:0005515 (protein binding) annotations with IPI evidence codes (rows 25-32, 108, 140)
**Scope:** At least 8-9 annotations
**Recommendation:**
- Action: REMOVE (generic) or MODIFY to specific interactions
- Rationale: Generic "protein binding" annotations lack functional specificity. Review each IPI interaction:
  - PMID:15068796 with Q17941/Q2PJ68/Q9XTG7: These appear to be high-throughput yeast-two-hybrid interactions. Determine if mechanistically relevant.
  - PMID:16777605, PMID:16860373, PMID:18358814: Map Q21921 interaction - this is FKH-1 (another forkhead protein). Keep but annotate as "forkhead protein binding" if validated.
  - PMID:11124266 with P63101: Map to specific interacting protein. If it's 14-3-3, keep as specific GO:0071889.

**Action Needed:** Cross-reference with publications and InterAct database to replace with specific binding interactions (GO:0071889 for 14-3-3 binding, etc.)

#### ISSUE 2: Non-core Developmental/Pleiotropic Roles
**Problem:** Multiple developmental annotations (dauer, larval development, synaptic assembly) represent important biological roles but are peripheral to the core immune function for this review
**Scope:**
- GO:0040024 (dauer larval development) - rows 102, 145
- GO:0002119 (nematode larval development) - row 125
- GO:0061065/GO:0061066 (regulation of dauer larval development) - rows 92-93, 105
- GO:0008582/GO:0045887 (synaptic assembly at neuromuscular junction) - rows 71-73
- GO:0007614 (short-term memory) - row 94
- GO:0030431 (sleep) - rows 59-60
- GO:0060537 (muscle tissue development) - row 124

**Recommendation:**
- Action: KEEP_AS_NON_CORE (for all developmental annotations)
- Rationale: These represent well-documented pleiotropic roles of DAF-16, but in the context of the surveillance immunity pathway, they are secondary to immune function. Mark as non-core to focus annotation on the immune/stress resistance pathway.

#### ISSUE 3: Lifespan/Aging Annotations (Heavy over-representation)
**Problem:** GO:0008340 (determination of adult lifespan) appears excessively (rows 15, 50, 70, 84-86, 89, 95, 100, 111-112, 114, 133-134, 142-143 = 13+ entries with mixed evidence codes)
**Scope:** 13-14 distinct annotations
**Recommendation:**
- Action: CONSOLIDATE - Keep 3-4 strongest evidence entries (IMP codes); REMOVE redundant duplicates with weaker evidence
- Rationale: This massive over-representation reflects both the biological importance of DAF-16 in longevity and potential annotation redundancy. Multiple studies demonstrate DAF-16's role in lifespan through IMP/IGI evidence. The older IEP entries (row 136) are weak and redundant with IMP/IGI data.
- Specific guidance:
  - KEEP: PMID:11747825 (IMP), PMID:11381260 (IMP), PMID:23665919 (IGI), PMID:22560223 (IMP)
  - REMOVE: PMID:11747821 (IMP but older and superseded), row 136 (IEP - weak evidence)
  - MODIFY: Some IGI entries may be context-specific (Worm var genetic backgrounds)

#### ISSUE 4: Vague/Overly Broad Process Terms
**Problem:** Several annotations are too general for specific function
**Scope:**
- GO:0010468 (regulation of gene expression) - row 58 (IMP, PMID:32963007)
- GO:0006355 (regulation of DNA-templated transcription) - rows 13, 120, 131
- GO:0006351 (DNA-templated transcription) - row 12

**Recommendation:**
- Action: MODIFY to specific processes
- Rationale: For a transcription factor, these broad terms are redundant with more specific annotations. Replace with specific pathway/target genes when possible.
- Examples: GO:0045087 (innate immune response), GO:0034599 (cellular response to oxidative stress), GO:0008286 (insulin receptor signaling pathway) are more informative.

#### ISSUE 5: Specific Immunity Annotations - WELL SUPPORTED
**Annotations to ACCEPT with confidence:**
- GO:0045087 (innate immune response) - rows 115, 23 (IMP, IEA with strong support)
- GO:0050829 (defense response to Gram-negative bacterium) - rows 57, 63, 117 (IMP/IGI)
- GO:0050830 (defense response to Gram-positive bacterium) - row 67 (IMP)
- GO:0031349 (positive regulation of defense response) - row 18 (IEA)
- GO:0002821 (positive regulation of adaptive immune response) - rows 121, 126 (IMP)
- GO:1900426 (positive regulation of defense response to bacterium) - row 98 (IMP)

These annotations are core functions with solid experimental evidence and should be retained as ACCEPT.

#### ISSUE 6: IBA Annotations Quality Check
**IBA annotations present:** Rows 2-5, 9-24 (multiple molecular_function, cellular_component, biological_process)
**Assessment:** Most IBA annotations are appropriately broad and phylogenetically sound:
- GO:0000981 (DNA-binding transcription factor activity, RNA polymerase II-specific) - ACCEPT (row 2)
- GO:0005634 (nucleus) - ACCEPT as is_active_in relationship (row 3)
- GO:0006357 (regulation of transcription by RNA polymerase II) - ACCEPT (row 4)
- GO:0008286 (insulin receptor signaling pathway) - ACCEPT (row 14, core pathway)
- GO:0008340 (determination of adult lifespan) - MODIFY (see above - over-annotated)
- GO:0009896, GO:0010883, GO:0034599, GO:0040015, GO:0042594, GO:0050778 - All reasonable IEA/ARBA annotations based on functional evidence

#### ISSUE 7: Location Annotations (nucleus/cytoplasm)
**Problem:** Multiple entries for nuclear (GO:0005634) and cytoplasmic (GO:0005737) localization with both is_active_in and located_in/colocalizes_with relationships
**Scope:** ~8-10 entries with multiple relationships
**Recommendation:**
- Action: CONSOLIDATE and standardize relationships
- Rationale: DAF-16 shuttles between cytoplasm and nucleus. Keep IDA entries from key studies (PMID:11124266, PMID:11381260, PMID:11747821). Use relationship types consistently:
  - is_active_in for nucleus (transcriptional function)
  - located_in for both when present
  - Remove redundant NAS entries if IDA entries exist

#### ISSUE 8: Heat/Stress Response Annotations
**Well-supported core functions:**
- GO:0034605 (cellular response to heat) - rows 39, 138-139 (IMP/IDA) - ACCEPT
- GO:0006979 (response to oxidative stress) - row 79 (IGI)
- GO:0034599 (cellular response to oxidative stress) - rows 19, 101 (IEA/IGI) - ACCEPT
- GO:0009411 (response to UV) - rows 80, 135 (IGI/IDA) - ACCEPT
- GO:0042594 (response to starvation) - rows 21, 97 (IEA/IMP) - ACCEPT

These are core stress-response functions aligned with the surveillance immunity role and should all be ACCEPTED.

### Recommended Actions Summary for DAF-16

| Action | Count | GO Terms | Evidence |
|--------|-------|----------|----------|
| ACCEPT (core immune) | ~15-18 | GO:0045087, GO:0050829, GO:0050830, GO:0031349, stress responses | IMP, IGI, IEA |
| KEEP_AS_NON_CORE | ~20 | Dauer, larval dev, synaptic assembly, memory, sleep | IMP, IGI |
| MODIFY (broad to specific) | ~5 | GO:0010468, GO:0006355, GO:0006351 | IMP |
| REMOVE (redundant) | ~5-8 | Duplicate lifespan entries, generic protein binding | IEA, IPI |
| CONSOLIDATE | ~15 | Nuclear/cytoplasmic localization, 14-3-3 binding | IDA, NAS, IPI |

---

## 2. DBL-1 (G5EEL5) - TGF-beta/BMP Ligand (32 annotations)

### Gene Summary
DBL-1 is the C. elegans ortho log of Drosophila *decapentaplegic* (Dpp) and vertebrate BMP2/4. It's a secreted TGF-beta superfamily ligand expressed primarily in neurons, signaling non-cell-autonomously to hypodermal cells through SMA-6 (type I) and DAF-4 (type II) receptors, activating the SMAD pathway for body size regulation. Beyond growth control, DBL-1 regulates innate immunity, lipid metabolism, and sexual differentiation.

### Overall Assessment
The 32 annotations are well-organized with good balance between molecular function (growth factor/cytokine activity, receptor binding), cellular component (extracellular space), and biological processes (BMP pathway, immune responses, growth regulation). The annotations appropriately capture both developmental and immune roles.

### Key Curation Issues

#### ISSUE 1: Growth/Development vs. Immune Annotations Balance
**Problem:** Most annotations (rows 4-27, 29-32) focus on body size/growth regulation and male tail morphogenesis, which represent the most extensively studied dbl-1 function, but are NOT core to surveillance immunity
**Scope:**
- GO:0040018 (positive regulation of multicellular organism growth) - rows 21, 26-27, 32 (4 entries)
- GO:0045138 (nematode male tail tip morphogenesis) - row 28
- GO:0045793 (positive regulation of cell size) - row 30
- GO:0046622 (positive regulation of organ growth) - row 31
- GO:0002119 (nematode larval development) - row 29
- GO:0042661 (regulation of mesodermal cell fate specification) - row 12
- GO:0032877 (positive regulation of DNA endoreduplication) - row 23

**Recommendation:**
- Action: KEEP_AS_NON_CORE (for all growth-related annotations)
- Rationale: These represent well-studied but non-immune dbl-1 functions. Appropriate to keep but mark as secondary to immune role in surveillance immunity context.

#### ISSUE 2: Immune Response Annotations - Core Functions
**Annotations to ACCEPT:**
- GO:0050832 (defense response to fungus) - row 14 (IMP, PMID:19198592)
- GO:0050829 (defense response to Gram-negative bacterium) - rows 15-16 (IMP, PMID:17975555) - Duplicate entries
- GO:0050830 (defense response to Gram-positive bacterium) - row 17 (IMP, PMID:17975555)
- GO:0045087 (innate immune response) - row 22 (IMP, PMID:19198592)
- GO:0010628 (positive regulation of gene expression) - row 7 (IMP, PMID:18158917) - in immune context

**Recommendation:**
- Action: ACCEPT all immune annotations
- Rationale: These demonstrate dbl-1's role in TGF-beta-mediated innate immunity. The fungal and bacterial defense responses are well-supported experimentally.
- Note: Rows 15-16 are duplicates (same GO term, evidence, and reference but recorded twice). Consolidate to single entry.

#### ISSUE 3: TGF-beta/BMP Pathway Core Annotations
**Annotations to ACCEPT:**
- GO:0030509 (BMP signaling pathway) - rows 4, 19 (IBA, ISS with phylogenetic support)
- GO:0005125 (cytokine activity) - row 2 (IBA)
- GO:0008083 (growth factor activity) - row 6 (IEA via InterPro)
- GO:0070700 (BMP receptor binding) - row 20 (ISS, PMID:9847238)
- GO:0005615 (extracellular space) is_active_in - row 3 (IBA)
- GO:0005576 (extracellular region) - row 5 (IEA)

**Recommendation:**
- Action: ACCEPT all pathway annotations
- Rationale: These capture the core molecular function of DBL-1 as a TGF-beta/BMP-like secreted signaling molecule.

#### ISSUE 4: Lipid Metabolism Annotations
**Annotations present:**
- GO:0019216 (regulation of lipid metabolic process) acts_upstream_of - row 8 (IMP, PMID:29162682)

**Recommendation:**
- Action: KEEP_AS_NON_CORE
- Rationale: Important but not core to surveillance immunity. DBL-1's role in lipid metabolism represents a secondary pleiotropic function.

#### ISSUE 5: Miscellaneous Process Annotations
**Annotations to evaluate:**
- GO:0010468 (regulation of gene expression) - row 13 (IMP, PMID:17526726)
- GO:0022604 (regulation of cell morphogenesis) - row 9 (IMP, PMID:24690231)
- GO:0030511 (positive regulation of TGF-beta receptor signaling pathway) - row 11 (IGI, PMID:28068334)
- GO:0045944 (positive regulation of transcription by RNA polymerase II) - row 10 (IMP, PMID:19198592)

**Recommendation:**
- Action: MODIFY or CONSOLIDATE
- Rationale: Some overlap with immune response annotations above. Rows 10 and 45944 likely redundant with immune pathway activation. Row 13 is too general; prefer specific processes.

#### ISSUE 6: ISS (Sequence Similarity) Annotations Quality
**Annotations present:** Rows 18-20 (ISS with PMID:9847238 reference to ortholog studies)

**Recommendation:**
- Action: ACCEPT with caution
- Rationale: ISS annotations (rows 18-20) are phylogenetically sound but refer to mammalian/Drosophila ortholog studies. The references are appropriate for TGF-beta/BMP pathway component inference. These are weaker than IMP evidence but reasonable.

### Recommended Actions Summary for DBL-1

| Action | Count | GO Terms | Evidence |
|--------|-------|----------|----------|
| ACCEPT (core function) | ~8 | GO:0030509, GO:0005125, GO:0008083, immune responses | IBA, IEA, IMP |
| KEEP_AS_NON_CORE | ~10 | Growth (0040018, 0045793, 0046622), development, morphogenesis | IMP, IGI |
| CONSOLIDATE | ~2 | Duplicate rows 15-16 (GO:0050829) | IMP |
| REMOVE | ~1 | Redundant lipid metabolism if other pathway captured | IMP |

---

## 3. STA-2 (Q20977) - STAT-like Transcription Factor (27 annotations)

### Gene Summary
STA-2 is a STAT-like transcription factor that uniquely functions in C. elegans epidermal immunity without JAK kinases (absent in C. elegans). Activated through unconventional SNF-12 transporter mechanism, STA-2 is sequestered at hemidesmosomes in normal conditions and released upon epidermal damage or fungal infection. It translocates to nuclei and activates antimicrobial peptide genes (especially nlp-29). STA-2 also participates in developmental signaling (ECM-to-nucleus pathway) during molts.

### Overall Assessment
27 annotations are well-distributed and appropriate. The review must distinguish between sta-2's core epidermal immunity function and its secondary developmental roles. IBA annotations are phylogenetically reasonable given STAT family conservation, but some are over-applied to C. elegans specificity.

### Key Curation Issues

#### ISSUE 1: Redundant IBA Annotations
**Annotations present:** Rows 2-9 (multiple IBA entries with GO_REF:0000033)
- GO:0005737 (cytoplasm) is_active_in
- GO:0006952 (defense response)
- GO:0042127 (regulation of cell population proliferation)
- GO:0005634 (nucleus) is_active_in
- GO:0000978 (RNA polymerase II cis-regulatory region sequence-specific DNA binding)
- GO:0006357 (regulation of transcription by RNA polymerase II)
- GO:0007259 (cell surface receptor signaling pathway via JAK-STAT)
- GO:0000981 (DNA-binding transcription factor activity, RNA polymerase II-specific)

**Recommendation:**
- Action: ACCEPT most with caveats on specific terms
- Rationale:
  - Rows 5, 7, 9: ACCEPT (nuclear localization, transcription regulation, TF activity are core)
  - Row 8 (JAK-STAT pathway): MODIFY to note that C. elegans lacks JAK but uses SNF-12 instead. Consider GO:0007165 (signal transduction) as substitute or annotation to modified pathway term if available.
  - Row 4 (cell proliferation): KEEP_AS_NON_CORE (phylogenetically inferred but undemonstrated in C. elegans sta-2)
  - Rows 2-3: ACCEPT (constitutive localization to cytoplasm and nucleus appropriate for STAT protein shuttling)

#### ISSUE 2: Defense Response Annotations - Core Functions
**Annotations to ACCEPT:**
- GO:0050832 (defense response to fungus) - row 21 (IMP, PMID:22470487)
- GO:0006952 (defense response) - row 3 (IBA but well-supported by IMP below)
- GO:0009611 (response to wounding) - row 19 (IMP, PMID:22470487)
- GO:0010628 (positive regulation of gene expression) - row 20 (IMP, PMID:22470487) in immune context

**Recommendation:**
- Action: ACCEPT all
- Rationale: These are core STA-2 functions with solid experimental evidence. PMID:22470487 is key study on sta-2 in epidermal immunity.

#### ISSUE 3: Problematic Cellular Component Annotations
**Annotations present:**
- GO:0030056 (hemidesmosome) located_in - row 23 (IDA, PMID:25692704)
- GO:0098733 (hemidesmosome associated protein complex) part_of - row 24 (IDA, PMID:25692704)
- GO:0030139 (endocytic vesicle) located_in - row 26 (IDA, PMID:21575913)
- GO:0045177 (apical part of cell) located_in - row 27 (IDA, PMID:21575913)

**Recommendation:**
- Action: KEEP_AS_NON_CORE or MODIFY relationships
- Rationale: STA-2's localization at hemidesmosomes is mechanistically important for understanding how it's sequestered and activated (row 23 well-supported by PMID:25692704). However, these represent structural/localization details rather than functional roles. Keep IDA annotations but categorize as non-core cellular context annotations. Rows 26-27 (endocytic vesicle, apical part) may reflect trafficking/localization during activation - keep but note as secondary.

#### ISSUE 4: Antimicrobial Peptide Production Annotation
**Annotation present:**
- GO:0002804 (positive regulation of antifungal peptide production) - row 28 (IMP, PMID:21575913)

**Recommendation:**
- Action: ACCEPT as core
- Rationale: This is the primary functional readout of STA-2 activation. PMID:21575913 demonstrates sta-2 is required for nlp-29 (antifungal peptide) induction upon infection. This is a key core annotation.

#### ISSUE 5: Transcription Factor DNA Binding Annotations
**Annotations present:**
- GO:0000978 (RNA pol II cis-regulatory region binding) - rows 6, 42 (IBA, IDA)
- GO:0000981 (DNA-binding transcription factor activity, RNA pol II-specific) - row 9 (IBA)
- GO:0003677 (DNA binding) - row 10 (IEA)
- GO:0003700 (DNA-binding transcription factor activity) - row 11 (IEA)

**Recommendation:**
- Action: CONSOLIDATE and ACCEPT
- Rationale: Multiple overlapping DNA binding annotations. Keep GO:0000978 (most specific to Pol II cis-elements for STA-2 targets like nlp-29) with both IBA (phylogenetic) and IDA (PMID:21575913 demonstrates nlp-29 binding). Rows 10-11 are broader parent terms; acceptable but less informative than row 6.

#### ISSUE 6: Generic Regulatory Annotations
**Annotations present:**
- GO:0006351 (DNA-templated transcription) - row 14 (IEA)
- GO:0006355 (regulation of DNA-templated transcription) - row 15 (IEA)
- GO:0007165 (signal transduction) - row 16 (IEA via InterPro)

**Recommendation:**
- Action: MODIFY or REMOVE
- Rationale: These are too generic for a specific transcription factor. STA-2's function is not general signal transduction or transcription regulation, but specifically regulation of antimicrobial peptide genes in response to infection. Prefer GO:0002804 (antifungal peptide production) or similar specific terms.

#### ISSUE 7: IEA Annotations - General Quality
**Annotations:** Rows 10-17 (IEA from various sources: UniProt-KW, InterPro)

**Recommendation:**
- Action: ACCEPT with notes
- Rationale: IEA annotations are appropriate for general transcription factor functions (DNA binding, nuclear localization) inferred from domain structure. However, prioritize IMP/IDA annotations for core epidermal immunity function.

### Recommended Actions Summary for STA-2

| Action | Count | GO Terms | Evidence |
|--------|-------|----------|----------|
| ACCEPT (core immune) | ~6 | GO:0050832, GO:0002804, GO:0009611, GO:0010628 | IMP, IDA |
| KEEP_AS_NON_CORE | ~5 | Hemidesmosome localization, trafficking, proliferation | IDA, IEA, IBA |
| MODIFY | ~3 | JAK-STAT pathway (note C. elegans difference), broad regulatory terms | IBA, IEA |
| CONSOLIDATE | ~3 | Multiple DNA binding terms (keep GO:0000978 primarily) | IBA, IDA, IEA |

---

## 4. NIPI-3 (G5EED4) - Tribbles Pseudokinase Adapter (18 annotations)

### Gene Summary
NIPI-3 is a Tribbles family pseudokinase that functions as a regulatory adapter in innate immune signaling and developmental pathways. Despite containing a kinase domain, it lacks catalytic activity (pseudokinase). NIPI-3 functions upstream of p38 MAPK (pmk-1/sek-1) pathway in epidermal antifungal immunity and negatively regulates CEBP-1 in intestinal immunity against bacteria. NIPI-3 directly interacts with CEBP-1 transcription factor. Developmentally, loss of nipi-3 causes larval arrest, indicating essential developmental role.

### Overall Assessment
The 18 annotations appropriately capture NIPI-3's adapter functions in immunity and development. The collection is well-balanced, but requires careful distinction between core immune functions and developmental roles.

### Key Curation Issues

#### ISSUE 1: Nuclear Localization Annotation
**Annotation present:**
- GO:0005634 (nucleus) is_active_in - row 2 (IBA)
- GO:0005634 (nucleus) located_in - row 8 (IEA)

**Recommendation:**
- Action: ACCEPT and CONSOLIDATE
- Rationale: NIPI-3 is nuclear-localized in epidermis, intestine, and neurons (PMID:27927209). Both annotations are correct; IBA (phylogenetic) and IEA (subcellular location prediction) are consistent. Could consolidate to single IDA entry if available from PMID:27927209.

#### ISSUE 2: MAPK Kinase Binding Annotation
**Annotation present:**
- GO:0031434 (mitogen-activated protein kinase kinase binding) - row 3 (IBA)

**Recommendation:**
- Action: ACCEPT with caveats
- Rationale: IBA annotation is phylogenetically reasonable (mammalian Tribbles proteins bind MAPK components). Genetic evidence (PMID:27927209 shows sek-1 suppresses nipi-3 lethality) supports functional interaction with MAPKK. Direct physical binding not demonstrated in C. elegans but phylogenetically inferred and functionally supported.

#### ISSUE 3: Proteasome Regulation Annotation
**Annotation present:**
- GO:0032436 (positive regulation of proteasomal ubiquitin-dependent protein catabolic process) - row 4 (IBA)

**Recommendation:**
- Action: KEEP_AS_NON_CORE or REMOVE
- Rationale: Mammalian Tribbles do promote C/EBP degradation via ubiquitin-proteasome. However, in C. elegans, NIPI-3 regulates CEBP-1 transcriptionally rather than post-translationally (PMID:27927209). A translational reporter showed no differences in nipi-3 mutants, indicating proteasomal degradation is NOT the primary mechanism. Mark as non-core or remove as not demonstrated for C. elegans NIPI-3.

#### ISSUE 4: ATP/Nucleotide Binding Annotations
**Annotations present:**
- GO:0000166 (nucleotide binding) - row 5 (IEA)
- GO:0004672 (protein kinase activity) - row 6 (IEA)
- GO:0005524 (ATP binding) - row 7 (IEA)

**Recommendation:**
- Action: MODIFY or REMOVE
- Rationale: NIPI-3 is a pseudokinase lacking catalytic residues. While it contains kinase domain topology and ATP binding pocket (row 7 IEA based on InterPro kinase domain), it does NOT have kinase activity (row 6 should be removed). The nucleotide binding is predicted from domain structure but unclear if ATP actually binds functionally. Recommend:
  - Row 7 (ATP binding): KEEP as structural feature but note that kinase activity is absent
  - Row 6 (kinase activity): REMOVE (pseudokinase, not active)
  - Row 5 (nucleotide binding): KEEP but note as predicted, not experimentally validated

#### ISSUE 5: Immune Response Annotations - Core Functions
**Annotations to ACCEPT:**
- GO:0010468 (regulation of gene expression) - row 9 (IMP, PMID:27927200)
- GO:0010629 (negative regulation of gene expression) - rows 10, 13 (IMP)
- GO:0050829 (defense response to Gram-negative bacterium) - row 11 (IMP, PMID:27927200)
- GO:0050830 (defense response to Gram-positive bacterium) - row 12 (IMP, PMID:34407394)
- GO:0010628 (positive regulation of gene expression) - row 15 (IMP, PMID:18394898)
- GO:0050832 (defense response to fungus) - rows 16, 18 (IMP, PMID:18394898 and PMID:22470487)
- GO:0061760 (antifungal innate immune response) - row 17 (IMP, PMID:18394898)

**Recommendation:**
- Action: ACCEPT all
- Rationale: These are core NIPI-3 immune functions with solid IMP evidence. The annotations appropriately capture both epidermal antifungal immunity (GO:0061760) and intestinal bacterial defense (GO:0050829, GO:0050830).

#### ISSUE 6: Transcription Factor Binding Annotation
**Annotation present:**
- GO:0140297 (DNA-binding transcription factor binding) - row 14 (IPI, PMID:27927209 with UniProtKB:Q18909)

**Recommendation:**
- Action: ACCEPT
- Rationale: This is the well-documented NIPI-3-CEBP-1 interaction. PMID:27927209 demonstrates direct interaction with CEBP-1 (Q18909). This is a core mechanistic annotation.

#### ISSUE 7: Developmental (Non-core) Annotations
**Note:** The provided GOA file only shows up to row 18. Based on context in existing review, there may be developmental annotations related to larval lethality/arrest that would be KEEP_AS_NON_CORE.

### Recommended Actions Summary for NIPI-3

| Action | Count | GO Terms | Evidence |
|--------|-------|----------|----------|
| ACCEPT (core immune) | ~7 | GO:0050829, GO:0050830, GO:0050832, GO:0061760, antifungal pathway | IMP |
| KEEP_AS_NON_CORE | ~2 | ATP binding (domain), possibly developmental | IEA |
| REMOVE | ~2 | Kinase activity (pseudokinase), proteasome regulation | IEA |
| MODIFY | ~2 | Nucleotide binding (note pseudokinase context), MAPKK binding (note c. elegans specificity) | IEA, IBA |

---

## 5. LYS-7 (O16202) - Lysozyme-like Protein (18 annotations)

### Gene Summary
LYS-7 is a protist-type (Entamoeba-like) lysozyme belonging to glycosyl hydrolase family 25. Despite containing a Ch-type lysozyme domain, LYS-7 lacks conserved catalytic residues and likely lacks enzymatic activity. It functions as a key antimicrobial effector in C. elegans immunity. LYS-7 is expressed in intestine, rectal glands, and neurons, induced by diverse pathogens (S. marcescens, M. nematophilum, S. typhimurium), and provides resistance against Gram-positive bacteria (B. thuringiensis) and fungi (C. neoformans). Paradoxically, lys-7 knockout animals show increased tolerance to S. typhimurium, suggesting complex immunological trade-offs. Expression is regulated by p38 MAPK and DAF-2/DAF-16 insulin signaling.

### Overall Assessment
The 18 annotations appropriately capture LYS-7's role as a core antimicrobial effector. The collection is well-curated with good balance of molecular function, biological process, and cellular component annotations. Most annotations are appropriately specific to immunity function.

### Key Curation Issues

#### ISSUE 1: Phylogenetic Inference Annotation - Signal Transduction
**Annotation present:**
- GO:0007165 (signal transduction) - row 2 (IBA, GO_REF:0000033)

**Recommendation:**
- Action: REMOVE
- Rationale: LYS-7 is an antimicrobial effector molecule whose EXPRESSION is regulated by signal transduction pathways (p38 MAPK, insulin signaling), but the protein itself does NOT participate in signal transduction. It's a DOWNSTREAM EFFECTOR, not a signaling component. This annotation is incorrect even though based on phylogenetic inference to other lysozymes. The annotation likely results from broad InterPro/PANTHER inference that doesn't distinguish between regulatory inputs and functional outputs.

#### ISSUE 2: IBA Annotations Quality Check
**Annotations present:**
- GO:0045087 (innate immune response) - row 3 (IBA, GO_REF:0000033)
- Same term, row 9 (IEA, UniProt-KW)

**Recommendation:**
- Action: ACCEPT (keep both or consolidate to IBA as primary)
- Rationale: IBA is phylogenetically sound for a lysozyme in immune context. The duplication (rows 3, 9) is redundant. Consolidate to keep one entry with strongest evidence.

#### ISSUE 3: Enzyme Activity Annotations
**Annotations present:**
- GO:0003796 (lysozyme activity) - row 5 (IEA, InterPro:IPR002053)

**Recommendation:**
- Action: MODIFY or REMOVE
- Rationale: LYS-7 contains a lysozyme domain (IPR002053) but LACKS key catalytic residues. It's non-catalytic. The IEA annotation should be MODIFIED to note that the domain is present but non-functional, OR remove the annotation as enzymatic activity annotation is misleading. This is a critical issue. If keeping, annotate with evidence qualifier noting lack of catalytic activity.
- Alternative: Replace with GO:0051183 (auxin binding) if applicable, but more likely this should be removed entirely or replaced with a binding-related term that doesn't imply catalytic function.

#### ISSUE 4: Catabolic Process Annotations
**Annotations present:**
- GO:0009253 (peptidoglycan catabolic process) - row 7 (IEA, InterPro:IPR002053)
- GO:0016998 (cell wall macromolecule catabolic process) - row 8 (IEA, InterPro:IPR002053)

**Recommendation:**
- Action: REMOVE or MODIFY
- Rationale: These annotations infer that LYS-7 CATALYZES peptidoglycan breakdown based on domain similarity to active lysozymes. However, LYS-7 lacks catalytic activity. These annotations are MISLEADING. Either:
  a) REMOVE entirely (LYS-7 likely functions through non-catalytic mechanisms like binding/agglutination)
  b) MODIFY to GO:0030246 (carbohydrate binding) if it binds but doesn't cleave bacterial cell walls
  c) Annotate to broader GO:0050826 (natural killer cell mediated immunity) or similar if function is opsonization-like

This is a critical curation point where domain-based inference leads to incorrect annotation.

#### ISSUE 5: Core Immune Response Annotations
**Annotations to ACCEPT:**
- GO:0050830 (defense response to Gram-positive bacterium) - rows 10-12 (IMP, multiple studies)
- GO:0050832 (defense response to fungus) - row 13 (IMP, PMID:21399680)
- GO:0050829 (defense response to Gram-negative bacterium) - rows 14, 18 (IMP, IGI)
- GO:0045087 (innate immune response) - rows 3, 9, 16 (IBA, IEA, IMP)

**Recommendation:**
- Action: ACCEPT all
- Rationale: These are well-supported by multiple independent studies (PMID:16809667, PMID:21931778, PMID:21399680, PMID:19023415, PMID:18927620). These represent core LYS-7 functions and should be retained.

#### ISSUE 6: Response to Stress Annotation
**Annotation present:**
- GO:0006950 (response to stress) - row 6 (IEA, ARBA:ARBA00026300)

**Recommendation:**
- Action: KEEP_AS_NON_CORE
- Rationale: LYS-7 expression is stress-responsive (up-regulated during pathogen exposure), but "response to stress" is a broad parent term. More specific immune response annotations (rows 10-18) are preferred. Keep but note as redundant with more specific child terms.

#### ISSUE 7: Immune System Process vs. Innate Immune Response Redundancy
**Annotations present:**
- GO:0002376 (immune system process) - row 4 (IEA, UniProt-KW:KW-0391)
- GO:0045087 (innate immune response) - rows 3, 9, 16 (IBA, IEA, IMP)

**Recommendation:**
- Action: ACCEPT both or CONSOLIDATE
- Rationale: GO:0002376 is a parent term of GO:0045087. The IEA annotation to GO:0002376 is correct but less specific. Keep both or consolidate to GO:0045087. Given that more specific immune annotations exist, row 4 is somewhat redundant but acceptable.

### Recommended Actions Summary for LYS-7

| Action | Count | GO Terms | Evidence |
|--------|-------|----------|----------|
| ACCEPT (core immune) | ~8-10 | GO:0050830, GO:0050832, GO:0050829, GO:0045087 | IMP, IEA, IBA |
| REMOVE | ~3 | Signal transduction (not effector role), lysozyme activity (non-catalytic), peptidoglycan catabolic (non-catalytic) | IBA, IEA |
| MODIFY | ~1 | Catabolic annotations to binding term if applicable | IEA |
| KEEP_AS_NON_CORE | ~2 | Stress response (redundant), immune system process (parent term) | IEA |

---

## 6. CLEC-60 (Q23564) - C-type Lectin (1 annotation)

### Gene Summary
CLEC-60 is a secreted C-type lectin domain-containing protein with a von Willebrand factor type A (VWA) domain that functions as an antimicrobial effector in C. elegans innate immunity. It is strongly upregulated (8.3-fold) in intestinal epithelial cells during Staphylococcus aureus infection and provides protective effects through overexpression. Contains a signal peptide for secretion and is classified as an antimicrobial effector with predicted carbohydrate-binding function. Also induced by other pathogens including P. aeruginosa and M. nematophilum.

### Overall Assessment
Only 1 GOA annotation exists, making this the least-annotated gene in this set. The existing annotation is well-supported. This gene requires expansion of annotations to capture its full function. The existing review file (clec-60-ai-review.yaml) proposes NEW annotations that should be integrated into the GOA.

### Existing Annotation Assessment

#### Current Annotation:
- GO:0050830 (defense response to Gram-positive bacterium) - row 2 (IGI, PMID:20617181, with UniProtKB:Q23565)

**Status:** ACCEPT
**Rationale:** Well-supported by PMID:20617181 showing clec-60 upregulation and overexpression protection during S. aureus infection. IGI evidence is appropriate (genetic interaction with clec-61).

### Proposed Annotations from Existing Review

The clec-60-ai-review.yaml file proposes 3 NEW annotations worth implementing:

1. **GO:0030246 (carbohydrate binding)** - NEW (IEA, InterPro domain)
   - Rationale: C-type lectin domain is characterized by carbohydrate-binding activity
   - Mechanism: Calcium-dependent recognition of pathogen surface carbohydrates
   - Status: RECOMMEND ADDING

2. **GO:0140367 (antibacterial innate immune response)** - NEW (IMP, PMID:20617181)
   - Rationale: Broader characterization of CLEC-60's immune function
   - Evidence: Transcriptional induction, overexpression protection
   - Status: RECOMMEND ADDING

3. **GO:0005576 (extracellular region)** - NEW (IEA, signal peptide)
   - Rationale: Signal peptide indicates secretion
   - Mechanism: Consistent with antimicrobial effector function
   - Status: RECOMMEND ADDING

### Recommended Actions Summary for CLEC-60

| Action | Count | GO Terms | Evidence |
|--------|-------|----------|----------|
| ACCEPT | 1 | GO:0050830 | IGI |
| ADD (NEW) | 3 | GO:0030246, GO:0140367, GO:0005576 | IEA, IMP |

---

## Cross-Gene Patterns and General Recommendations

### Pattern 1: Generic "Protein Binding" Annotations Should Be Removed or Specified
**Affected genes:** DAF-16 (8-9 entries), possibly others
**Recommendation:** Systematically replace GO:0005515 with specific binding terms or remove if not mechanistically relevant. Examples of specific alternatives:
- GO:0071889 (14-3-3 protein binding)
- GO:0140297 (DNA-binding transcription factor binding)
- GO:0008013 (beta-catenin binding)
- GO:0019899 (enzyme binding)
- GO:0031625 (ubiquitin protein ligase binding)

### Pattern 2: Phylogenetic (IBA) vs. Experimental Evidence Priority
**Recommendation:** For all genes, prioritize IMP/IGI/IDA evidence when available over IBA. Flag IBA annotations that lack experimental support or that might not translate to C. elegans-specific functions (e.g., sta-2 lacks JAK-STAT machinery).

### Pattern 3: Developmental/Pleiotropic Roles Should Be Categorized as NON-CORE for Immunity-Focused Review
**Affected genes:** DAF-16 (extensive), DBL-1 (growth), NIPI-3 (larval arrest)
**Recommendation:** Use KEEP_AS_NON_CORE action for well-documented developmental roles to distinguish core immune functions.

### Pattern 4: Over-annotation of Broad Process Terms
**Affected genes:** DAF-16, DBL-1, STA-2
**Pattern:** GO:0010468 (regulation of gene expression), GO:0006355 (regulation of DNA-templated transcription), GO:0006351 (DNA-templated transcription)
**Recommendation:** These are too general for specific regulatory proteins. Prefer specific process terms (e.g., GO:0002804 for antifungal peptide production rather than GO:0010468).

### Pattern 5: Domain-Based Inference for Inactive/Catalytic Annotations
**Affected genes:** LYS-7 (lysozyme activity, catabolic processes), NIPI-3 (kinase activity)
**Pattern:** InterPro/domain-based (IEA) annotations for enzymatic activity in pseudoenzymes/non-catalytic proteins
**Recommendation:**
- Systematically review all IEA annotations based on enzyme domains for pseudoenzymes
- Remove catalytic annotations for proteins confirmed to lack catalytic activity
- Replace with binding or regulatory annotations if appropriate
- This is a critical quality control point

### Pattern 6: Localization Annotations - Standardize Relationships
**Affected genes:** DAF-16 (multiple nucleus/cytoplasm entries), STA-2 (hemidesmosome)
**Pattern:** Multiple relationship types (is_active_in, located_in, colocalizes_with) for same location
**Recommendation:** Consolidate and standardize relationship types:
- Use is_active_in for functional compartments (nucleus for transcription factors)
- Use located_in for structural/steady-state localization
- Consolidate redundant entries, preferring IDA over IEA/NAS

### Pattern 7: Duplicate Entries Across Genes
**Affected:** DBL-1 (rows 15-16 both GO:0050829)
**Recommendation:** Systematic deduplication pass. Keep one entry per unique GO term + evidence combination.

### Pattern 8: Evidence Code Quality Check
**Specific recommendations:**
- **IMP (Mutant Phenotype):** Generally high quality; check that phenotypes are specific to target gene
- **IGI (Genetic Interaction):** Generally high quality; verify that With/From genes are correctly identified
- **IPI (Protein Interaction):** Verify interactions are mechanistically relevant and not high-throughput noise
- **IDA (Direct Assay):** Highest quality; prioritize these when available
- **IEA (Electronic Annotation):** Lower priority unless no manual evidence exists
- **IEP (Expression Pattern):** Generally weak; use only when combined with other evidence
- **NAS (Narrative Statement):** Weak; should be backed up by more rigorous evidence codes

---

## Implementation Recommendations

### Phase 1: High-Priority Critical Fixes (Week 1)
1. **CLEC-60:** Add 3 proposed NEW annotations (GO:0030246, GO:0140367, GO:0005576)
2. **LYS-7:** Remove signal transduction annotation (GO:0007165); review and fix lysozyme activity and catabolic annotations
3. **NIPI-3:** Remove kinase activity annotation (GO:0004672); review proteasome annotation
4. **DAF-16:** Remove/consolidate 8-9 generic protein binding annotations
5. **DBL-1:** Consolidate duplicate rows 15-16 (GO:0050829)

### Phase 2: Comprehensive Curation (Week 2-3)
1. **DAF-16:**
   - Consolidate 13+ lifespan annotations
   - Categorize developmental annotations as NON-CORE
   - Standardize localization annotations
   - Replace broad gene regulation terms with specific processes

2. **STA-2:**
   - Modify JAK-STAT pathway annotation to note C. elegans-specific mechanism
   - Consolidate DNA binding annotations
   - Categorize hemidesmosome localization as NON-CORE

3. **NIPI-3:**
   - Flag ATP binding annotation as pseudokinase context
   - Evaluate developmental annotations

4. **DBL-1:**
   - Categorize growth/development as NON-CORE
   - Consolidate regulatory process annotations

### Phase 3: Quality Control & Validation (Week 4)
1. Cross-check all evidence codes against cited publications
2. Validate that GeneIDs in With/From fields are correct (especially IGI entries)
3. Ensure relationship types (involved_in, enables, acts_upstream_of, etc.) are correct
4. Final review of immunity vs. non-core categorization consistency across all 6 genes

---

## Summary Table: Recommended Actions by Gene

| Gene | Annotations | ACCEPT | REMOVE | MODIFY | KEEP_NON_CORE | CONSOLIDATE | NEW |
|------|-------------|--------|--------|--------|---------------|-------------|-----|
| **daf-16** | 144 | 15-18 | 5-8 | 5 | 20 | 15 | 0 |
| **dbl-1** | 32 | 8-10 | 0-1 | 1 | 10 | 2 | 0 |
| **sta-2** | 27 | 6 | 0 | 3 | 5 | 3 | 0 |
| **nipi-3** | 18 | 7 | 2 | 2 | 2 | 1 | 0 |
| **lys-7** | 18 | 8-10 | 3 | 1 | 2 | 1 | 0 |
| **clec-60** | 1 | 1 | 0 | 0 | 0 | 0 | 3 |
| **TOTAL** | 238 | ~45-53 | 10-14 | 12 | ~39 | 22 | 3 |

---

## File Paths for Review Updates

### GOA TSV Files (Read-only reference):
- `/Users/cjm/repos/ai-gene-review/genes/worm/daf-16/daf-16-goa.tsv`
- `/Users/cjm/repos/ai-gene-review/genes/worm/dbl-1/dbl-1-goa.tsv`
- `/Users/cjm/repos/ai-gene-review/genes/worm/sta-2/sta-2-goa.tsv`
- `/Users/cjm/repos/ai-gene-review/genes/worm/nipi-3/nipi-3-goa.tsv`
- `/Users/cjm/repos/ai-gene-review/genes/worm/lys-7/lys-7-goa.tsv`
- `/Users/cjm/repos/ai-gene-review/genes/worm/clec-60/clec-60-goa.tsv`

### AI Review YAML Files (To be updated):
- `/Users/cjm/repos/ai-gene-review/genes/worm/daf-16/daf-16-ai-review.yaml` (2765 lines)
- `/Users/cjm/repos/ai-gene-review/genes/worm/dbl-1/dbl-1-ai-review.yaml` (827 lines)
- `/Users/cjm/repos/ai-gene-review/genes/worm/sta-2/sta-2-ai-review.yaml` (527 lines)
- `/Users/cjm/repos/ai-gene-review/genes/worm/nipi-3/nipi-3-ai-review.yaml` (521 lines)
- `/Users/cjm/repos/ai-gene-review/genes/worm/lys-7/lys-7-ai-review.yaml` (492 lines)
- `/Users/cjm/repos/ai-gene-review/genes/worm/clec-60/clec-60-ai-review.yaml` (207 lines)

### Supporting Resources:
- Deep research files: `*-deep-research-falcon.md` for each gene
- UniProt records: `*-uniprot.txt` for each gene
- Publication files: `/Users/cjm/repos/ai-gene-review/publications/PMID_*.md`

---

## Key References Consulted

This review synthesizes information from:
- Existing GO annotation files (GOA TSV format)
- Existing AI review YAML files
- Deep research summaries (Falcon provider)
- UniProt protein records
- Relevant primary literature in publications/ directory

Key primary studies cited multiple times across genes:
- **Innate immunity:** PMID:19198592, PMID:19454349, PMID:21575913, PMID:22470487
- **Dauer/development:** PMID:11747825, PMID:11381260, PMID:23665919
- **BMP/Growth:** PMID:9847238, PMID:12397107, PMID:12717735
- **Lysozymes:** PMID:16809667, PMID:21931778, PMID:21399680
- **Tribbles/NIPI:** PMID:18394898, PMID:27927200, PMID:27927209
- **C-type lectins:** PMID:20617181

---

## Final Notes

This curation review emphasizes:

1. **Domain-based inference is error-prone for pseudoenzymes and inactive proteins.** The most critical issues are LYS-7 lysozyme activity and NIPI-3 kinase activity annotations that infer function from domain similarity despite lack of catalytic activity.

2. **Phylogenetic inference (IBA) must be validated experimentally in C. elegans context.** Several IBA annotations (e.g., sta-2 JAK-STAT pathway, NIPI-3 proteasome regulation) assume conservation that doesn't hold for C. elegans-specific biology.

3. **Generic binding annotations reduce annotation informativeness.** Systematic replacement of GO:0005515 with specific interactions improves curation quality.

4. **Pleiotropic gene functions require careful prioritization.** DAF-16 and DBL-1 have legitimate developmental roles that should be retained but clearly marked as NON-CORE in immunity-focused curation.

5. **Duplicate and redundant annotations should be consolidated.** The large annotation sets (especially daf-16 with 144) contain systematic redundancy that could be reduced without loss of information.
