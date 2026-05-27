# Surveillance Immunity Gene Curation: Implementation Checklist

## Overview
This document provides a line-by-line implementation checklist for updating the 6 surveillance immunity gene reviews based on the comprehensive curation summary.

**Target genes:** daf-16, dbl-1, sta-2, nipi-3, lys-7, clec-60
**Total annotations to review:** 238
**Estimated effort:** 40-60 hours for complete implementation

---

## CLEC-60 (Q23564) - START HERE (SIMPLEST, 1 annotation + 3 NEW)

### Existing Annotations in GOA
```
Row 2: GO:0050830 | defense response to Gram-positive bacterium | IGI | PMID:20617181
```

### Actions Required

**Annotation 1: GO:0050830 (defense response to Gram-positive bacterium)**
- [ ] Status: ACCEPT (no changes needed)
- [ ] Verify PMID:20617181 is available in publications/ directory
- [ ] Confirm that Q23565 (clec-61) is correctly cited as With/From gene
- [ ] Ensure supporting text in review file includes: "clec-60 upregulation 8.3-fold during S. aureus infection"

**NEW Annotation 1: GO:0030246 (carbohydrate binding)**
- [ ] Action: ADD
- [ ] Evidence type: IEA
- [ ] Reference: GO_REF:0000002 (InterPro domain mapping)
- [ ] Supporting text: "C-type lectin domain (IPR001304) is characterized by calcium-dependent carbohydrate-binding activity"
- [ ] Summary: CLEC-60 contains C-type lectin-like domain enabling carbohydrate recognition
- [ ] Reason: Domain composition supports carbohydrate binding function consistent with pathogen recognition

**NEW Annotation 2: GO:0140367 (antibacterial innate immune response)**
- [ ] Action: ADD
- [ ] Evidence type: IMP
- [ ] Reference: PMID:20617181
- [ ] Supporting text: "Transgenic animals carrying clec-60,61 cluster extrachromosomal arrays survived longer (LT50 = 54.2 h) during S. aureus infection"
- [ ] Summary: CLEC-60 functions as an effector in innate immune response to bacterial infection
- [ ] Reason: Overexpression provides protection during S. aureus infection demonstrating functional role

**NEW Annotation 3: GO:0005576 (extracellular region)**
- [ ] Action: ADD
- [ ] Evidence type: IEA
- [ ] Reference: GO_REF:0000002 (SignalP prediction)
- [ ] Supporting text: "Signal peptide (residues 1-17) indicating secretion to extracellular space"
- [ ] Summary: CLEC-60 is secreted via N-terminal signal peptide
- [ ] Reason: Signal peptide consistent with role as secreted antimicrobial effector

### Checklist for CLEC-60
- [ ] Verify existing annotation matches GOA file
- [ ] Add 3 new annotations with evidence codes
- [ ] Update review section with supporting_text for each new annotation
- [ ] Add PMID:20617181 to references section if not already present
- [ ] Run validation: `just validate worm clec-60`
- [ ] Commit changes: "Review CLEC-60 surveillance immunity annotations"

---

## LYS-7 (O16202) - 18 annotations (Priority: HIGH - has critical errors)

### Critical Issues to Address

**ISSUE 1: Row 2 - GO:0007165 (signal transduction) - IBA**
- [ ] Action: REMOVE
- [ ] Reason: LYS-7 is an effector downstream of signaling pathways, not a signaling component itself
- [ ] Supported by: PMID:18927620 "repression of immune effector expression, such as...lys-7, may represent a virulence mechanism"
- [ ] Remove this line from review: "involved_in: GO:0007165"

**ISSUE 2: Row 5 - GO:0003796 (lysozyme activity) - IEA via InterPro**
- [ ] Action: REMOVE (or MODIFY with caveat)
- [ ] Reason: LYS-7 lacks conserved catalytic residues; is a pseudolysozyme
- [ ] Check UniProt record for mention of catalytic residue absence
- [ ] If must keep: Add annotation note "catalytically inactive pseudolysozyme"
- [ ] Recommend removal entirely

**ISSUE 3: Row 7 - GO:0009253 (peptidoglycan catabolic process) - IEA**
- [ ] Action: REMOVE
- [ ] Reason: Infers enzymatic activity that LYS-7 doesn't possess
- [ ] Supporting evidence: Lacks key catalytic residues for peptidoglycan cleavage
- [ ] Remove this annotation

**ISSUE 4: Row 8 - GO:0016998 (cell wall macromolecule catabolic process) - IEA**
- [ ] Action: REMOVE
- [ ] Reason: Same issue as above - non-catalytic protein
- [ ] Remove this annotation

### Annotations to ACCEPT

**Row 3: GO:0045087 (innate immune response) - IBA**
- [ ] Status: ACCEPT
- [ ] Keep as is
- [ ] Note: Phylogenetic inference supported by extensive IMP evidence below

**Row 9: GO:0045087 (innate immune response) - IEA via UniProt-KW**
- [ ] Status: CONSOLIDATE or REMOVE duplicate
- [ ] Option 1: Remove this entry (redundant with row 3 IBA)
- [ ] Option 2: Keep and mark as secondary evidence if IBA unavailable

**Rows 10-12: GO:0050830 (defense response to Gram-positive bacterium) - IMP**
- [ ] Status: ACCEPT (keep all 3 entries - multiple studies)
- [ ] PMID:16809667, PMID:22841995 (appears twice)
- [ ] Verify citations exist in publications/ directory

**Row 13: GO:0050832 (defense response to fungus) - IMP**
- [ ] Status: ACCEPT
- [ ] PMID:21399680
- [ ] Verify evidence of C. neoformans protection

**Rows 14-18: GO:0050829 (defense response to Gram-negative bacterium) - IMP/IGI**
- [ ] Status: ACCEPT (most entries)
- [ ] Row 14: PMID:18927620 (IMP) - ACCEPT
- [ ] Row 18: PMID:21399680 (IGI with WB:WBGene00000018) - ACCEPT
- [ ] Note duplicates if present

**Row 16: GO:0045087 (innate immune response) - IMP**
- [ ] Status: ACCEPT
- [ ] PMID:19023415
- [ ] Strongest evidence (IMP with manipulation)

### Checklist for LYS-7
- [ ] Remove GO:0007165 (signal transduction)
- [ ] Remove GO:0003796 (lysozyme activity) OR add catalytic inactivity caveat
- [ ] Remove GO:0009253 (peptidoglycan catabolic)
- [ ] Remove GO:0016998 (cell wall macromolecule catabolic)
- [ ] Consolidate duplicate GO:0045087 entries
- [ ] Verify all IMP/IGI references exist in publications/
- [ ] Update review sections to explain removals and why
- [ ] Run validation: `just validate worm lys-7`
- [ ] Commit changes: "Fix LYS-7 catalytic activity over-annotations"

---

## NIPI-3 (G5EED4) - 18 annotations (Priority: HIGH - pseudokinase issue)

### Critical Issues to Address

**ISSUE 1: Row 6 - GO:0004672 (protein kinase activity) - IEA**
- [ ] Action: REMOVE
- [ ] Reason: NIPI-3 is a pseudokinase; lacks catalytic residues; NOT a functional kinase
- [ ] Explanation: Domain similarity to kinases should not infer catalytic activity for pseudokinases
- [ ] Remove this annotation

**ISSUE 2: Row 7 - GO:0005524 (ATP binding) - IEA**
- [ ] Action: MODIFY or KEEP with caveat
- [ ] Reason: NIPI-3 contains ATP-binding pocket in kinase domain but kinase is inactive
- [ ] Option 1: Keep with annotation note "catalytically inactive pseudokinase; ATP binding predicted but functional relevance unclear"
- [ ] Option 2: Remove if no experimental evidence of ATP binding
- [ ] Recommendation: MODIFY to keep but flag as non-functional

**ISSUE 3: Row 4 - GO:0032436 (positive regulation of proteasomal ubiquitin-dependent protein catabolic process) - IBA**
- [ ] Action: KEEP_AS_NON_CORE (not REMOVE)
- [ ] Reason: Mammalian Tribbles promote C/EBP degradation, but C. elegans NIPI-3 regulates CEBP-1 transcriptionally
- [ ] Supporting evidence: PMID:27927209 shows translational reporter no differences in nipi-3 mutants
- [ ] Action: Mark as non-core function or secondary mechanism

### Annotations to ACCEPT

**Row 2: GO:0005634 (nucleus) is_active_in - IBA**
- [ ] Status: ACCEPT
- [ ] Supporting evidence: PMID:27927209 GFP localization shows nuclear predominance
- [ ] Keep as is

**Row 3: GO:0031434 (mitogen-activated protein kinase kinase binding) - IBA**
- [ ] Status: ACCEPT
- [ ] Phylogenetically reasonable and functionally supported by sek-1 genetic interaction
- [ ] Keep as is

**Row 5: GO:0000166 (nucleotide binding) - IEA**
- [ ] Status: KEEP with caveat
- [ ] Action: Add annotation note: "Predicted nucleotide binding in pseudokinase domain; functional relevance unclear"
- [ ] Keep but flag

**Rows 9-12: Immune Response Annotations (GO:0010468, GO:0010629, GO:0050829, GO:0050830)**
- [ ] All STATUS: ACCEPT
- [ ] These are core NIPI-3 functions with solid IMP evidence
- [ ] PMID:27927200 (rows 9, 11)
- [ ] PMID:34407394 (rows 10, 12)
- [ ] Keep all entries

**Rows 13-18: Additional Immune Annotations**
- [ ] Row 13: GO:0010629 (negative regulation of gene expression) - ACCEPT
- [ ] Row 14: GO:0140297 (DNA-binding transcription factor binding) - ACCEPT (CEBP-1 interaction)
- [ ] Row 15: GO:0010628 (positive regulation of gene expression) - ACCEPT
- [ ] Rows 16-18: GO:0050832 (defense response to fungus) - ACCEPT both entries

### Checklist for NIPI-3
- [ ] Remove GO:0004672 (kinase activity - pseudokinase)
- [ ] Modify GO:0005524 (ATP binding) with caveat about pseudokinase
- [ ] Reclassify GO:0032436 as non-core (proteasome regulation)
- [ ] Verify all IMP references (PMID:27927200, PMID:34407394, PMID:18394898, PMID:22470487)
- [ ] Update review to explain pseudokinase status
- [ ] Run validation: `just validate worm nipi-3`
- [ ] Commit changes: "Fix NIPI-3 pseudokinase activity annotations"

---

## STA-2 (Q20977) - 27 annotations (Priority: MEDIUM)

### Complex Annotations Requiring Review

**ISSUE 1: Row 8 - GO:0007259 (cell surface receptor signaling pathway via JAK-STAT) - IBA**
- [ ] Action: MODIFY or ADD_CAVEAT
- [ ] Problem: C. elegans lacks JAK kinases; sta-2 activated through SNF-12 transporter instead
- [ ] Recommendation: Keep annotation but add note that activation mechanism differs from JAK-STAT
- [ ] Supporting evidence: PMID:21575913, PMID:25692704
- [ ] Modify summary: "STA-2 functions similarly to mammalian STATs but through JAK-independent mechanism via SNF-12 transporter"

**ISSUE 2: Row 4 - GO:0042127 (regulation of cell population proliferation) - IBA**
- [ ] Action: KEEP_AS_NON_CORE
- [ ] Reason: Phylogenetically inferred from mammalian STATs but no C. elegans evidence for sta-2 role in proliferation
- [ ] Keep but mark as secondary, not core to surveillance immunity

**ISSUE 3: Redundant DNA Binding Annotations (Rows 6, 10, 11, 42)**
- [ ] Row 6: GO:0000978 (RNA pol II cis-regulatory region binding) IBA - KEEP PRIMARY
- [ ] Row 10: GO:0003677 (DNA binding) IEA - REMOVE or mark redundant
- [ ] Row 11: GO:0003700 (DNA-binding transcription factor activity) IEA - KEEP but secondary
- [ ] Row 42: GO:0000978 IDA - ADD if not already present
- [ ] Consolidate: Keep rows 6 and 11; remove row 10 as too generic

### Annotations to ACCEPT (Core Immune Functions)

**Row 21: GO:0050832 (defense response to fungus) - IMP**
- [ ] Status: ACCEPT
- [ ] PMID:22470487
- [ ] Core immune function

**Row 28: GO:0002804 (positive regulation of antifungal peptide production) - IMP**
- [ ] Status: ACCEPT
- [ ] PMID:21575913
- [ ] PRIMARY functional output of sta-2
- [ ] This is the most important annotation for surveillance immunity

**Row 19: GO:0009611 (response to wounding) - IMP**
- [ ] Status: ACCEPT
- [ ] PMID:22470487
- [ ] Part of epidermal damage response

**Row 20: GO:0010628 (positive regulation of gene expression) - IMP**
- [ ] Status: ACCEPT
- [ ] PMID:22470487
- [ ] Mechanistic description of AMP induction

**Row 3: GO:0006952 (defense response) - IBA**
- [ ] Status: ACCEPT
- [ ] Broad term supported by specific immune annotations below

**Rows 2, 5, 9: Localization/Activity (nucleus, TF activity)**
- [ ] All STATUS: ACCEPT
- [ ] IBA annotations phylogenetically appropriate
- [ ] Supported by IDA evidence in PMID:21575913, PMID:31735670

### Structural Annotations (Hemidesmosome - Non-core but keep)

**Rows 23-24: Hemidesmosome localization**
- [ ] Status: KEEP_AS_NON_CORE
- [ ] Mechanistically interesting (normal sequestration site) but not core immune function
- [ ] PMID:25692704 provides evidence
- [ ] Keep but label as developmental/structural context rather than immune function

**Rows 26-27: Endocytic vesicle and apical localization**
- [ ] Status: KEEP_AS_NON_CORE
- [ ] Likely represent trafficking during activation
- [ ] Keep but mark as supplementary cellular context

### Checklist for STA-2
- [ ] Modify JAK-STAT annotation (row 8) with caveat about SNF-12 mechanism
- [ ] Mark GO:0042127 (proliferation) as non-core
- [ ] Consolidate DNA binding annotations (remove row 10, keep rows 6, 11)
- [ ] Ensure GO:0002804 (antifungal peptide production) is ACCEPT status - PRIMARY FUNCTION
- [ ] Verify all IMP references exist
- [ ] Run validation: `just validate worm sta-2`
- [ ] Commit changes: "Review STA-2 annotations and clarify C. elegans-specific mechanism"

---

## DBL-1 (G5EEL5) - 32 annotations (Priority: MEDIUM)

### Critical Issue

**ISSUE 1: Rows 15-16 Duplicate**
- [ ] Row 15: GO:0050829 (defense response to Gram-negative bacterium) IMP PMID:17975555
- [ ] Row 16: GO:0050829 (same) IMP PMID:17975555 (exact duplicate)
- [ ] Action: CONSOLIDATE - Remove row 16, keep row 15
- [ ] Verify that consolidation doesn't lose any unique information (same ref, evidence, GO term)

### Growth/Development Annotations - Categorize as NON-CORE

**Rows 21, 26-27, 32: GO:0040018 (positive regulation of multicellular organism growth)**
- [ ] Status: KEEP_AS_NON_CORE (4 entries)
- [ ] Core to dbl-1 biology but peripheral to surveillance immunity
- [ ] Mark as developmental role, not immune

**Row 28: GO:0045138 (nematode male tail tip morphogenesis) - IMP**
- [ ] Status: KEEP_AS_NON_CORE
- [ ] Well-documented but not immune-related

**Row 30: GO:0045793 (positive regulation of cell size) - IMP**
- [ ] Status: KEEP_AS_NON_CORE

**Row 31: GO:0046622 (positive regulation of organ growth) - IMP**
- [ ] Status: KEEP_AS_NON_CORE

**Row 29: GO:0002119 (nematode larval development) - IMP**
- [ ] Status: KEEP_AS_NON_CORE

**Row 23: GO:0032877 (positive regulation of DNA endoreduplication) - IMP**
- [ ] Status: KEEP_AS_NON_CORE

**Row 12: GO:0042661 (regulation of mesodermal cell fate specification) - IGI**
- [ ] Status: KEEP_AS_NON_CORE

### Immune Response Annotations - ACCEPT

**Row 14: GO:0050832 (defense response to fungus) - IMP**
- [ ] Status: ACCEPT
- [ ] PMID:19198592
- [ ] Core immune function

**Rows 15-17: Bacterial Defense (Gram-negative and Gram-positive)**
- [ ] Row 15: GO:0050829 Gram-negative - ACCEPT
- [ ] Row 16: DUPLICATE - REMOVE
- [ ] Row 17: GO:0050830 Gram-positive - ACCEPT
- [ ] All IMP with PMID:17975555

**Row 22: GO:0045087 (innate immune response) - IMP**
- [ ] Status: ACCEPT
- [ ] PMID:19198592
- [ ] Core immune annotation

### Core TGF-beta/BMP Pathway - ACCEPT

**Row 2: GO:0005125 (cytokine activity) - IBA**
- [ ] Status: ACCEPT
- [ ] Phylogenetically appropriate for TGF-beta family

**Rows 4, 19: GO:0030509 (BMP signaling pathway) - IBA, ISS**
- [ ] Status: ACCEPT (both entries)
- [ ] Core molecular function

**Row 6: GO:0008083 (growth factor activity) - IEA**
- [ ] Status: ACCEPT

**Row 20: GO:0070700 (BMP receptor binding) - ISS**
- [ ] Status: ACCEPT
- [ ] Phylogenetically appropriate

**Rows 3, 5: Extracellular localization**
- [ ] Row 3: GO:0005615 (extracellular space) is_active_in IBA - ACCEPT
- [ ] Row 5: GO:0005576 (extracellular region) IEA - ACCEPT

### Miscellaneous Annotations

**Row 7: GO:0010628 (positive regulation of gene expression) - IMP**
- [ ] Status: ACCEPT (in immune context with PMID:18158917)

**Row 8: GO:0019216 (regulation of lipid metabolic process) acts_upstream_of - IMP**
- [ ] Status: KEEP_AS_NON_CORE
- [ ] Secondary metabolic role

**Row 9: GO:0022604 (regulation of cell morphogenesis) - IMP**
- [ ] Status: KEEP_AS_NON_CORE
- [ ] Non-immune context

**Row 10: GO:0045944 (positive regulation of transcription by RNA pol II) - IMP**
- [ ] Status: MODIFY or CONSOLIDATE
- [ ] Check if this is redundant with immune pathway activation (row 14 or 22)
- [ ] May consolidate if captured by more specific immune term

**Row 11: GO:0030511 (positive regulation of TGF-beta receptor signaling) - IGI**
- [ ] Status: ACCEPT
- [ ] Pathway component annotation

**Row 24-25: Growth regulation - IGI entries**
- [ ] Status: KEEP_AS_NON_CORE
- [ ] Genetic interaction evidence but developmental context

### Checklist for DBL-1
- [ ] Remove duplicate row 16 (GO:0050829)
- [ ] Categorize all growth annotations as NON_CORE (not REMOVE)
- [ ] Consolidate redundant transcription regulation terms if present
- [ ] Verify all IMP immunity references (PMID:19198592, PMID:17975555)
- [ ] Ensure core BMP pathway annotations retained
- [ ] Run validation: `just validate worm dbl-1`
- [ ] Commit changes: "Review DBL-1 annotations; consolidate duplicates and categorize developmental roles"

---

## DAF-16 (O16850) - 144 annotations (Priority: CRITICAL - LARGEST)

### Overview
With 144 annotations, this is the most complex review. Focus on:
1. Critical errors (generic protein binding, pseudokinase-like over-annotations)
2. Consolidation of redundant entries (lifespan appears 13+ times)
3. Categorization of core vs. non-core functions
4. Standardization of relationships (localization)

### CRITICAL ISSUE 1: Generic "Protein Binding" Annotations (8-9 entries)

**Rows 25-32: GO:0005515 (protein binding) - IPI**
- [ ] Total: 8 entries with IPI evidence
- [ ] Action: REVIEW AND REPLACE with specific binding interactions OR REMOVE

| Row | With/From Gene | PMID | Action | Replace with |
|-----|---|---|---|---|
| 25 | Q17941 | 15068796 | MAP or REMOVE | Specific binding term or remove |
| 26 | Q2PJ68 | 15068796 | MAP or REMOVE | Specific binding term or remove |
| 27 | Q9XTG7 | 15068796 | MAP or REMOVE | Specific binding term or remove |
| 28 | Q21921 | 16777605 | REVIEW | If FKH-1: keep as forkhead-forkhead interaction |
| 29 | Q21921 | 16860373 | REVIEW | If FKH-1: keep as forkhead-forkhead interaction |
| 30 | Q17941 | 18358814 | MAP or REMOVE | Specific binding term or remove |
| 31 | Q2PJ68 | 18358814 | MAP or REMOVE | Specific binding term or remove |
| 32 | Q9XTG7 | 18358814 | MAP or REMOVE | Specific binding term or remove |

**Additional protein binding entries:**
- [ ] Row 108: GO:0005515 IPI PMID:23255046 UniProtKB:Q17075 - REVIEW
- [ ] Row 140: GO:0005515 IPI PMID:11124266 UniProtKB:P63101 - KEEP (if 14-3-3)

**Action Plan:**
1. [ ] Check UniProt interaction database or cited publications for each with/from gene
2. [ ] For rows 25-27, 30-32: Likely high-throughput data; either REMOVE or annotate specifically
3. [ ] For rows 28-29: IF Q21921 is FKH-1, convert to GO:0140297 (DNA-binding transcription factor binding)
4. [ ] For row 140: IF P63101 is 14-3-3, already specific as GO:0071889 exists (rows 56, 76)
5. [ ] For rows 56, 76: GO:0071889 (14-3-3 protein binding) - KEEP both (PMID:17098225, PMID:21531333)

### CRITICAL ISSUE 2: Lifespan Annotation Consolidation (13+ entries)

**GO:0008340 (determination of adult lifespan) appears at rows:** 15, 50, 70, 84-86, 89, 95, 100, 111-112, 114, 133-134, 142-143

| Row | Evidence | PMID | Action |
|-----|----------|------|--------|
| 15 | IEA | - | REMOVE (weak, ARBA:ARBA00026742) |
| 50 | IMP | 11747825 | KEEP |
| 70 | IMP | 23665919 | KEEP |
| 84 | IMP | 17277769 | REVIEW - older but solid |
| 85 | IGI | 17277769 | KEEP (with gentic modifier) |
| 86 | IGI | 27001890 | KEEP (with WB:WBGene00001609) |
| 89 | IMP | 27564576 | KEEP |
| 95 | IMP | 23352664 | KEEP |
| 100 | IMP | 15905404 | KEEP |
| 111 | IDA | 22922647 | KEEP (direct assay) |
| 112 | IMP | 22560223 | REVIEW - may consolidate with others |
| 114 | IGI | 20523893 | KEEP |
| 133 | IMP | 11381260 | REVIEW - older but foundational |
| 134 | IMP | 11747821 | REVIEW - older but foundational |
| 142 | IMP | 11381260 | DUPLICATE of 133 (same PMID) |
| 143 | IGI | 11381260 | DUPLICATE source (same PMID as 142) |

**Action Plan:**
1. [ ] Remove row 15 (weak IEA evidence)
2. [ ] Remove row 142 (exact duplicate of row 133)
3. [ ] Consolidate rows 143 and other IGI entries with same PMID into single entry
4. [ ] Keep strongest evidence: rows 50, 70, 89, 95, 100, 111 (IMP/IDA)
5. [ ] Consolidate genetic interactions (IGI) to representative examples
6. [ ] Target: Reduce 13+ entries to 6-8 core entries maintaining evidence diversity

### ISSUE 3: Developmental Annotations - Categorize as NON-CORE (20 entries)

**Dauer-related (GO:0040024, GO:0061065, GO:0061066, GO:1905909):**
- [ ] Rows 68-69, 83, 92-93, 102, 105: All KEEP_AS_NON_CORE
- [ ] Mark as developmental role
- [ ] These are well-documented but not core to surveillance immunity

**Larval development (GO:0002119):**
- [ ] Row 125: KEEP_AS_NON_CORE
- [ ] PMID:11747821 (IMP)

**Synaptic assembly (GO:0008582, GO:0045887):**
- [ ] Rows 71-73: KEEP_AS_NON_CORE
- [ ] PMID:23665919 (IGI)
- [ ] Neuromuscular junction development

**Sleep (GO:0030431):**
- [ ] Rows 59-60: KEEP_AS_NON_CORE
- [ ] PMID:29523076 (IGI)

**Memory (GO:0007614):**
- [ ] Row 94: KEEP_AS_NON_CORE
- [ ] PMID:26675724 (IGI)

**Muscle development (GO:0060537):**
- [ ] Row 124: KEEP_AS_NON_CORE
- [ ] PMID:18397876 (IMP)

### ISSUE 4: Localization Annotations - Standardize (8-10 entries for nucleus/cytoplasm)

**Nuclear localization (GO:0005634):**
- [ ] Rows 3 (is_active_in, IBA)
- [ ] Rows 33, 43-47, 55, 77, 87, 109, 119, 127-128: Multiple IDA entries
- [ ] Row 10 (located_in, IEA)

**Action:**
1. [ ] Keep row 3 (is_active_in for transcriptional function)
2. [ ] Consolidate IDA entries to 2-3 strongest (PMID:11124266, PMID:11381260, PMID:11747821)
3. [ ] Remove redundant NAS entries (rows 33) if IDA exists
4. [ ] Remove IEA entries (row 10) if IBA/IDA exist

**Cytoplasmic localization (GO:0005737):**
- [ ] Rows 11 (IEA located_in)
- [ ] Rows 34-35 (NAS located_in)
- [ ] Row 78 (IDA located_in)
- [ ] Row 88 (colocalizes_with IDA)
- [ ] Row 129-130 (IDA located_in)

**Action:**
1. [ ] Keep IDA entries (rows 78, 129-130): empirical evidence
2. [ ] Consolidate NAS entries (rows 34-35) or remove if IDA available
3. [ ] Remove IEA entry (row 11)
4. [ ] Standardize: Use is_active_in for nucleus (transcription), located_in for both (subcellular)

### ISSUE 5: Broad Process Terms - Convert to Specific

**GO:0010468 (regulation of gene expression):**
- [ ] Row 58: MODIFY to more specific term
- [ ] PMID:32963007 (IMP)
- [ ] Replace with specific process (e.g., GO:0045087 innate immune, GO:0008286 insulin pathway, etc.)

**GO:0006355 (regulation of DNA-templated transcription):**
- [ ] Rows 13, 120, 131 (IEA or IDA)
- [ ] These are parent terms of more specific annotations
- [ ] KEEP row 13 (IBA broad parent term OK), REMOVE rows 120-131 (redundant with IDA annotations below)

**GO:0006351 (DNA-templated transcription):**
- [ ] Row 12 (IEA)
- [ ] Extremely generic; REMOVE or keep as parent term only

### ISSUE 6: Core Immune Annotations - ACCEPT (Priority to RETAIN)

**Innate immune response:**
- [ ] Row 23: GO:0045087 IEA - ACCEPT
- [ ] Row 115: GO:0045087 IMP PMID:19454349 - ACCEPT PRIMARY

**Defense response annotations:**
- [ ] Row 57: GO:0050829 (Gram-negative) IGI - ACCEPT
- [ ] Row 63: GO:0050829 IMP - ACCEPT
- [ ] Row 117: GO:0050829 IMP - ACCEPT
- [ ] Row 67: GO:0050830 (Gram-positive) IMP - ACCEPT
- [ ] Row 98: GO:1900426 (positive regulation of defense response to bacterium) IMP - ACCEPT

**Oxidative stress response:**
- [ ] Row 19: GO:0009896 (positive regulation of catabolic) - ACCEPT (stress metabolism)
- [ ] Row 39: GO:0034605 (cellular response to heat) NAS - ACCEPT
- [ ] Row 79: GO:0006979 (response to oxidative stress) IGI - ACCEPT
- [ ] Row 101: GO:0034599 (cellular response to oxidative stress) IGI - ACCEPT
- [ ] Row 138-139: GO:0034605 (cellular response to heat) IDA - ACCEPT

**Starvation response:**
- [ ] Row 21: GO:0042594 (response to starvation) IEA - ACCEPT
- [ ] Row 97: GO:0042594 IMP - ACCEPT

**UV response:**
- [ ] Row 80: GO:0009411 (response to UV) IGI - ACCEPT
- [ ] Row 135: GO:0009411 IDA - ACCEPT

**Apoptosis:**
- [ ] Row 122: GO:0043065 (positive regulation of apoptosis) IMP - ACCEPT (stress response)

**Positive regulation of immune response:**
- [ ] Row 18: GO:0031349 (positive regulation of defense response) IEA - ACCEPT
- [ ] Row 24: GO:0050778 (positive regulation of immune response) IEA - ACCEPT
- [ ] Row 116: GO:0045944 (positive regulation of transcription) IMP - ACCEPT

### ISSUE 7: DNA Binding Annotations - Consolidate (6-8 entries)

| Row | GO Term | Evidence | Action |
|-----|---------|----------|--------|
| 2 | GO:0000981 (Pol II TF activity) | IBA | KEEP PRIMARY |
| 5 | GO:0000978 (Pol II cis-reg binding) | IBA | KEEP |
| 8 | GO:0003677 (DNA binding) | IEA | REMOVE (parent) |
| 9 | GO:0003700 (TF activity) | IEA | KEEP as secondary |
| 22 | GO:0043565 (sequence-specific DNA binding) | IEA | KEEP (specific) |
| 41-42 | GO:0000978 | IDA | KEEP (2 entries with different studies) |
| 48 | GO:0001228 (activator activity Pol II) | IDA | KEEP |
| 53 | GO:0000978 | IDA | CONSOLIDATE with 41-42 |
| 54 | GO:0000981 | IMP | KEEP |
| 62 | GO:0000977 (TRR sequence-specific binding) | IDA | KEEP |
| 106 | GO:0003700 | IDA | REMOVE (duplicate of 9) |

**Action Plan:**
1. [ ] Keep rows 2, 5 (IBA core TF activities)
2. [ ] Remove row 8 (GO:0003677 too generic)
3. [ ] Keep row 22 (sequence-specific binding specific)
4. [ ] Consolidate IDA entries (41-42, 53, 62) into representative example(s)
5. [ ] Target: Reduce to 5-6 core DNA binding annotations

### Checklist for DAF-16 (PARTIAL - focusing on critical issues)
- [ ] Review and action 8-9 generic protein binding annotations
- [ ] Consolidate lifespan annotations from 13+ to 6-8 core entries
- [ ] Categorize 20 developmental annotations as NON_CORE
- [ ] Standardize localization annotations (nucleus/cytoplasm)
- [ ] Replace 3 broad process terms with specific terms
- [ ] Consolidate DNA binding annotations to 5-6 core
- [ ] Ensure all core immune annotations retained (ACCEPT)
- [ ] Run validation: `just validate worm daf-16`
- [ ] Expected result: Reduce from 144 to ~100-110 well-curated annotations

---

## Final Implementation Steps (All Genes)

### Step 1: Systematic Review (Week 1-2)
- [ ] Start with clec-60 (simplest - 1 annotation)
- [ ] Progress to lys-7, nipi-3 (high priority critical errors)
- [ ] Continue sta-2, dbl-1 (medium priority)
- [ ] Complete with daf-16 (largest and most complex)

### Step 2: Update Review YAML Files
For each gene, update the `existing_annotations` section:
- [ ] Add/modify `review` subsections with updated actions
- [ ] Update `summary` field to justify action
- [ ] Complete `reason` field with rationale
- [ ] Update `supported_by` with exact supporting text quotes

### Step 3: Add New Annotations (Only for clec-60 + identified gaps)
- [ ] CLEC-60: Add 3 new annotations
- [ ] Check for major gaps in other genes

### Step 4: Core Functions Update
- [ ] Verify `core_functions` section matches ACCEPT annotations
- [ ] Update descriptions to reflect prioritized immune function

### Step 5: Validation and Commit
- [ ] For each gene: `just validate worm <gene>`
- [ ] Fix any schema errors
- [ ] Commit: `git add genes/worm/<gene>/<gene>-ai-review.yaml`
- [ ] Commit message: "Review <gene> surveillance immunity annotations - [SUMMARY OF CHANGES]"

### Step 6: Final Review Pass
- [ ] Cross-check all inter-gene consistency (same annotation patterns treated consistently)
- [ ] Ensure immune vs. non-core categorization is consistent across genes
- [ ] Verify all cited PMIDs exist in publications/ directory

---

## Success Metrics

**Completion targets:**
- [ ] All 6 genes reviewed with detailed rationale for each action
- [ ] Critical errors fixed (protein binding, pseudokinase annotations, lysozyme activity)
- [ ] At least 30-40% reduction in low-quality annotations (generic terms, weak evidence)
- [ ] Core immune functions clearly identified and retained
- [ ] All changes documented and committed

**Quality indicators:**
- [ ] >80% of remaining annotations have IMP/IGI/IDA evidence or strong IBA support
- [ ] <5% of remaining annotations are generic terms (protein binding, regulation of transcription)
- [ ] Core immune functions well-represented across all 6 genes
- [ ] Non-core developmental roles clearly marked and organized

---

**Last Updated:** 2025-12-29
**Next Review Due:** After all YAML updates complete and validated
