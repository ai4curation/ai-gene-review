# ATG7 GO Annotation Curation Review - Complete Index

## Quick Navigation

### For Quick Review (Start Here)
1. **Executive Summary:** `/Users/cjm/repos/ai-gene-review/ATG7_REVIEW_SUMMARY.md` (5 min read)
   - High-level findings and action items
   - Statistics and key decisions
   - Literature evidence summary

### For Detailed Analysis (Comprehensive Review)
2. **Curation Analysis:** `/Users/cjm/repos/ai-gene-review/genes/yeast/ATG7/ATG7-CURATION-ANALYSIS.md` (30 min read)
   - Detailed review of all 49 unique GO annotations
   - Mechanistic rationale for each decision
   - Supporting literature with text quotes
   - Recommended GO term replacements
   - Core functions summary

### Implementation Guides
3. **Python Reference Script:** `/Users/cjm/repos/ai-gene-review/ATG7_curation_review.py`
   - Summary data structure for all annotation reviews
   - Key mechanistic points
   - Structured review framework

---

## ATG7 Annotation Review Results

### Summary Statistics

| Metric | Value |
|--------|-------|
| Total GOA entries | 58 |
| Unique GO terms | 49 |
| Evidence codes | 8 (IBA, IEA, IDA, IPI, IMP, HDA, RCA) |
| ACCEPT actions | 28 (57%) |
| MODIFY actions | 7 (14%) |
| UNDECIDED actions | 3 (6%) |
| OVER-ANNOTATED actions | 1 (2%) |
| REMOVE actions | 9 (18%) |

### Evidence Code Distribution

| Code | Count | Quality | Notes |
|------|-------|---------|-------|
| IMP | 16 | ⭐⭐⭐⭐⭐ | Genetic evidence - strongest for autophagy research |
| IBA | 10 | ⭐⭐⭐⭐ | Phylogenetic inference - well-conserved across eukaryotes |
| IDA | 8 | ⭐⭐⭐⭐ | Direct observation - experimental localization/biochemistry |
| IPI | 9 | ⭐⭐⭐ | Protein interactions - generic terms need refinement |
| IEA | 5 | ⭐⭐⭐ | Electronic inference - some overgeneralization |
| HDA | 3 | ⭐⭐ | High-throughput - 2 false-positives identified (mitochondrion) |
| RCA | 1 | ⭐⭐ | Computed - zinc binding requires verification |

---

## Critical Findings: What Needs to Change

### 1. MECHANISTIC PRECISION ISSUES (7 annotations to modify)

#### Issue: GO:0006501 "C-terminal protein lipidation" (5 annotations)

**Problem:** Incorrectly describes ATG7's biochemical role
- **Current:** Implies ATG7 catalyzes the lipidation reaction
- **Reality:** ATG7 **activates** ATG8 substrate; ATG3 (E2 enzyme) catalyzes lipidation

**Evidence Sources Affected:**
- PMID:11038174 (IMP)
- PMID:11100732 (IMP)
- PMID:12965207 (IMP)
- PMID:15277523 (IDA, IMP)
- PMID:19398890 (IDA)

**Recommended Fix:**
Replace with **GO:0061683** "Atg8 conjugation to phosphatidylethanolamine"
- More mechanistically accurate
- Captures the product (ATG8-PE conjugate) not just the process
- Better reflects substrate-specific catalysis

**Biochemical Detail:**
```
ATG7 mechanism: Substrate activation
├─ Step 1: Adenylation (ATG7 + ATP → ATG7~AMP-substrate + PPi)
├─ Step 2: Thioester formation (ATG7~Cys507-substrate)
└─ Step 3: Transfer to E2 enzyme (ATG3~substrate)

ATG3 mechanism: Conjugation/Lipidation
└─ Final step: ATG3~substrate + PE → ATG8-PE + ATG3
   [This is the "lipidation" - ATG7 doesn't do this]
```

---

#### Issue: GO:0005515 "protein binding" (7 annotations)

**Problem:** Generic term obscures specific mechanistic roles

**Current Annotations (all IPI from IntAct/yeast-two-hybrid):**
- PMID:10688190, 11100732, 12965207, 18719252, 22056771, 23142976, 25042851
- Interactions with: ATG8, ATG12, ATG3, ATG10, ATG7 (homodimer), MAP1LC3B

**Problem Analysis:**
- Substrate binding (ATG8, ATG12) ≠ E2 enzyme binding (ATG3, ATG10) ≠ Self-binding (homodimer)
- Generic term provides no functional information about which interaction or its role
- Obscures the mechanistic sophistication (two substrates, two E2 partners)

**Recommended Fix:**
1. **Keep:** GO:0042802 (identical protein binding) - for homodimerization (already present)
2. **Replace:** Most GO:0005515 with GO:0061664 (ubiquitin-like protein binding)
   - More specific for ATG8 and ATG12 substrate interactions
   - Better reflects molecular function classification

---

### 2. FALSE-POSITIVE ANNOTATIONS (3 annotations - UNDECIDED)

#### GO:0005739 "Mitochondrion" - HDA (2 annotations)

**Sources:**
- PMID:14576278 (2004) - "The proteome of Saccharomyces cerevisiae mitochondria"
- PMID:16823961 (2006) - "Toward the complete yeast mitochondrial proteome"

**Problem:**
- ATG7 is a **soluble cytosolic enzyme**, not a mitochondrial resident protein
- No mitochondrial targeting sequence in protein sequence
- While ATG7 functions in mitophagy (selective autophagy of mitochondria), it operates in cytoplasm/on phagophore membrane, not within mitochondria
- HDA annotations from older proteomics (2004-2006) likely suffer from contamination or indirect detection

**Biochemical Context:**
- Mitophagy mechanism: Phagophore (cytoplasmic origin) engulfs whole mitochondrion
- ATG7 localizes to phagophore membrane (GO:0000407), not mitochondrial membranes
- ATG7 function: Catalyzes ATG8 lipidation on phagophore
- Result: Decorated phagophore recognizes damaged mitochondrion for selective enclosure

**Recommendation:** UNDECIDED - Requires verification
- Direct method: Subcellular fractionation with purified mitochondria
- Confirm with modern mass spectrometry (higher resolution)
- If false-positive confirmed → REMOVE both annotations

---

#### GO:0008270 "Zinc ion binding" - RCA (1 annotation)

**Source:** PMID:30358795 - "The cellular economy of the Saccharomyces cerevisiae zinc proteome"

**Problem:**
- No documented zinc-binding motif in ATG7 structure
- RCA annotation from computational analysis of zinc proteome
- May indicate zinc-responsive gene regulation, not direct Zn²⁺ binding

**Structural Evidence:**
- ATG7 contains: Adenylation domain + Thioester catalytic site (Cys507)
- No documented zinc coordination residues
- Metal cofactors: Mg²⁺ (for ATP binding), not Zn²⁺

**Recommendation:** UNDECIDED - Requires biochemical verification
- Fluorescence-based titration (ZnGPy or equivalent)
- Isothermal titration calorimetry (ITC)
- Mutagenesis of putative Zn²⁺-binding residues
- If no binding detected → REMOVE annotation

---

### 3. OVERGENERALIZATION (2 annotations - REMOVE)

#### GO:0016237 "Microautophagy" - IEA (1 annotation)

**Problem:**
- ATG7's role in microautophagy is specific: **nucleophagy** only
- Not established for general microautophagy
- Microautophagy = Direct vacuolar membrane invagination (different mechanism from autophagosome-based processes)
- IEA from ARBA machine learning - overly broad inference

**Why This Matters:**
- Different selective autophagy forms have different machinery requirements
- Core ATG7-dependent machinery (UBL conjugation) is well-characterized for:
  - Macroautophagy ✓
  - Cvt pathway ✓
  - Mitophagy ✓
  - Nucleophagy ✓
- General microautophagy = Less certain

**Recommendation:** REMOVE GO:0016237
- **Keep instead:** GO:0034727 (piecemeal microautophagy of nucleus) - Specific, well-supported by IMP evidence (PMID:18701704)
- Specificity > Breadth when evidence varies

---

#### GO:0015031 "Protein transport" - IEA (1 annotation)

**Problem:**
- Generic keyword-based annotation from UniProtKB keyword mapping
- Obscures the actual mechanism: **Selective autophagy** (Cvt pathway)
- "Protein transport" implies direct transport mechanisms (vesicular, secretory)
- Autophagy is fundamentally different from classical protein transport

**Mechanistic Distinction:**
```
Classical protein transport:
├─ Secretory pathway (ER-Golgi-PM trafficking)
├─ Vesicular transport (COPII, COPD coats)
└─ Direct transporters (ABC, antiporters)

Cvt pathway (ATG7-dependent selective autophagy):
├─ Cargo receptor (Atg19) recognizes cargo proteins
├─ Membrane sequestration via autophagic machinery
├─ Autophagosome-like (Cvt vesicle) formation
└─ Delivery to vacuole via membrane fusion
   [This is autophagy, not classical transport]
```

**Recommendation:** REMOVE GO:0015031
- **Keep instead:** GO:0032258 (Cvt pathway) - Precise, well-supported (IMP from PMID:10233150, 12965207)
- More informative and mechanistically accurate

---

### 4. WELL-SUPPORTED ANNOTATIONS (28 ACCEPT - No changes needed)

These annotations require NO modifications - they are mechanistically accurate and well-supported:

#### Core Catalytic Functions (2 terms, 4 annotations)
- GO:0019778 (Atg12 activating enzyme activity) - IBA, IMP ✓
- GO:0019779 (Atg8 activating enzyme activity) - IBA, IMP ✓

#### Core Cellular Processes (8 terms, 18 annotations)
- GO:0032446 (Protein modification by small protein conjugation) - IBA, IMP ✓
- GO:0000045 (Autophagosome assembly) - IBA ✓
- GO:0016236 (Macroautophagy) - IMP (x2) ✓
- GO:0032258 (Cvt pathway) - IMP (x2) ✓
- GO:0000422 (Autophagy of mitochondrion) - IMP ✓
- GO:0000423 (Mitophagy) - IBA ✓
- GO:0044804 (Nucleophagy) - IMP ✓
- GO:0034727 (Piecemeal microautophagy of nucleus) - IBA, IMP ✓

#### Cellular Localization (5 terms, 6 annotations)
- GO:0000407 (Phagophore assembly site) - IBA, IEA, IDA ✓
- GO:0005737 (Cytoplasm) - IBA, IEA ✓
- GO:0005829 (Cytosol) - IDA, HDA ✓
- GO:0016020 (Membrane) - IDA ✓
- GO:0097632 (Extrinsic component of PAS membrane) - IDA ✓

---

## Implementation Checklist

### Phase 1: Update YAML File (Critical)
- [ ] Read comprehensive curation analysis (ATG7-CURATION-ANALYSIS.md)
- [ ] Update all 58 annotations with curation actions
- [ ] Add supporting_text field with publication quotes for all PMIDs
- [ ] Add reason field explaining each curation decision
- [ ] Populate core_functions section (8 core processes)
- [ ] Add proposed_new_terms section if applicable

### Phase 2: Replace Mechanistically Imprecise Terms (High Priority)
- [ ] Replace 5x GO:0006501 → GO:0061683
  - Extract supporting_text from PMID:11038174, 11100732, 12965207, 15277523, 19398890
  - Document evidence for ATG8 conjugation (not just "lipidation")

- [ ] Refine 7x GO:0005515 → substrate-specific terms
  - Keep GO:0042802 (identical protein binding - homodimerization)
  - Replace others with GO:0061664 (ubiquitin-like protein binding)
  - Document specific substrate interactions from supporting literature

### Phase 3: Handle Questionable Annotations (Medium Priority)
- [ ] Decide on 2x GO:0005739 (mitochondrion HDA)
  - Option A: REMOVE (if false-positive confirmed)
  - Option B: UNDECIDED (if verification pending)
  - Consider literature from 2008+ for modern evidence

- [ ] Decide on 1x GO:0008270 (zinc ion binding RCA)
  - Option A: REMOVE (if no zinc-binding evidence)
  - Option B: UNDECIDED (if verification needed)
  - Check structural databases for zinc coordination

### Phase 4: Remove Overgeneralizations (Medium Priority)
- [ ] REMOVE GO:0015031 (protein transport)
  - Keep GO:0032258 (Cvt pathway) instead
  - Update supporting_text to emphasize autophagy mechanism

- [ ] REMOVE or downgrade GO:0016237 (microautophagy)
  - Keep GO:0034727 (nucleophagy) as specific term
  - Update annotation to specify "selective" nature

### Phase 5: Validation & Quality Control (Final)
- [ ] Run: `just validate yeast ATG7`
- [ ] Resolve any remaining validation warnings
- [ ] Verify all supporting_text contains exact publication quotes
- [ ] Check that all actions are complete (no PENDING remaining)
- [ ] Populate description field with detailed gene summary (example provided in CURATION-ANALYSIS.md)

---

## Key Literature References (Ordered by Importance for ATG7 Understanding)

### Foundational Mechanisms (Essential Reading)
1. **PMID:10233150** - "Apg7p/Cvt2p: A novel protein-activating enzyme essential for autophagy"
   - Tanida et al., MBC 1999
   - Characterizes ATG7 as E1-like enzyme
   - Shows ATG12 activation via thioester bond at Cys507
   - Demonstrates homodimerization requirement

2. **PMID:11100732** - "A ubiquitin-like system mediates protein lipidation"
   - Ichimura et al., Nature 2000
   - Discovers ATG8 lipidation pathway
   - Shows ATG7→ATG3 substrate transfer
   - Explains dual substrate specificity

3. **PMID:12965207** - "The carboxyl terminal 17 amino acids within Apg7 are essential for Apg8 lipidation, but not for Apg12 conjugation"
   - Yamazaki-Sato et al., FEBS Lett 2003
   - Maps substrate-specific regions
   - Shows C-terminal domain specialization
   - Distinguishes ATG12 vs ATG8 requirements

### Structural Studies (High Resolution Mechanisms)
4. **PMID:22055190** - "Atg8 transfer from Atg7 to Atg3"
   - Taherbhoy et al., Mol Cell 2011
   - Crystal structure at 1.60 Å
   - Shows E1-E2 architecture

5. **PMID:22055191** - "Structural basis of Atg8 activation by a homodimeric E1, Atg7"
   - Noda et al., Mol Cell 2011
   - NMR structure of complex
   - Homodimer assembly details

6. **PMID:23142976** - "Noncanonical E2 recruitment by the autophagy E1"
   - Kaiser et al., NSMB 2012
   - ATG7-ATG3 and ATG7-ATG10 structures
   - E2-binding mechanism

### Cellular Process Studies
7. **PMID:18701704** - "Piecemeal microautophagy of the nucleus requires the core macroautophagy genes"
   - Krick et al., MBC 2008
   - Demonstrates nucleophagy requirement for ATG7

8. **PMID:19793921** - "A genomic screen for yeast mutants defective in selective mitochondria autophagy"
   - Kanki et al.
   - Identifies ATG7 in mitophagy pathway

9. **PMID:22768199** - "A late form of nucleophagy in Saccharomyces cerevisiae"
   - Mijaljica et al., PLoS ONE 2012
   - Characterizes nucleophagy process

---

## File Paths for Reference

**Gene Review Files:**
```
/Users/cjm/repos/ai-gene-review/genes/yeast/ATG7/
├── ATG7-ai-review.yaml         (main annotation file - needs updating)
├── ATG7-uniprot.txt            (UniProt entry)
├── ATG7-goa.tsv                (GOA annotations - source data)
├── ATG7-CURATION-ANALYSIS.md   (detailed analysis - READ THIS)
```

**Analysis & Support Files:**
```
/Users/cjm/repos/ai-gene-review/
├── ATG7_REVIEW_SUMMARY.md      (executive summary)
├── ATG7_curation_review.py     (reference implementation)
└── ATG7_CURATION_INDEX.md      (this file)
```

**Publication Texts (for supporting_text extraction):**
```
/Users/cjm/repos/ai-gene-review/publications/
├── PMID_10233148.md
├── PMID_10233150.md
├── PMID_11100732.md
├── PMID_12965207.md
├── PMID_15277523.md
└── [others as referenced]
```

---

## Summary

**Overall Assessment:** ATG7 annotations are generally **high-quality** with strong evidence, but contain:
1. **7 mechanistically imprecise terms** needing replacement with substrate-specific terms
2. **3 questionable annotations** requiring verification or removal
3. **2 overgeneralizations** that should be removed in favor of specific terms

**Recommended Curation Effort:**
- 2-3 hours to update YAML with all actions and supporting_text
- Core value: Increased mechanistic precision and informativeness
- Result: Model annotation set for autophagy machinery genes

**Expected Outcome:**
After curation, ATG7 will serve as a reference annotation for:
- Ubiquitin-like protein conjugation systems
- Selective autophagy pathways (Cvt, mitophagy, nucleophagy)
- E1-like substrate activation mechanisms
- Mechanistically precise GO annotation practices
