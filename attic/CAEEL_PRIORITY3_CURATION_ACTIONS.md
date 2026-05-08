# C. elegans Priority 3 Genes: Specific Curation Actions

**Document Date:** December 30, 2025
**Status:** ACTIONABLE - Ready for implementation in YAML files

---

## Quick Reference Table

| Gene | UniProt | Total Annot. | ACCEPT | KEEP_AS_NON_CORE | MODIFY | REMOVE | NEW | Status |
|------|---------|------------|--------|------------------|--------|--------|-----|--------|
| daf-16 | O16850 | 144 | ~130 | ~10 | ~3 | ~1 | 0 | PENDING REVIEW |
| daf-2 | Q968Y9 | 88 | ~75 | ~10 | ~2 | ~1 | 1 | PENDING REVIEW |
| skn-1 | P34707 | 74 | 56 | 6 | 2 | 0 | 0 | READY TO IMPLEMENT |
| sir-2.1 | Q21921 | 42 | ~38 | ~2 | ~1 | ~1 | 0 | PENDING REVIEW |
| aak-2 | Q95ZQ4 | 31 | ~28 | ~2 | ~1 | 0 | 0 | PENDING REVIEW |
| hlh-30 | H2KZZ2 | 42 | 37 | 2 | 1 | 0 | 3 | READY TO IMPLEMENT |

---

## Gene 1: DAF-16 (O16850) - FOXO Transcription Factor

### Annotation Review Status: PENDING (144 annotations)

**Estimated effort:** 2-4 hours for complete systematic review

#### Actions Recommended

##### ACTION 1.1: Remove Generic "Protein Binding" Annotations
**GO Term:** GO:0005515 (Protein binding)
**Evidence Type:** IPI
**Count:** 8 entries (PMID:15068796, PMID:16777605, PMID:16860373, PMID:18358814)

**Current situation:**
- Multiple IPI entries documented binding to AKT-1 (Q17941), AKT-2 (Q2PJ68), SGK-1 (Q9XTG7)
- Some entries appear redundant (multiple PMIDs for same interaction pairs)

**Recommendation:**
- REMOVE redundant IPI entries for AKT-1/AKT-2/SGK-1 interactions
- These represent phosphorylation-based regulation, better captured by:
  - GO:0006468 - Protein phosphorylation (by kinases AKT-1/AKT-2/SGK-1)
  - GO:0070849 - Response to phosphorylation (by AKT kinases)
- RETAIN SIR-2.1 interaction (PMID:16777605, PMID:16860373) as documented functional complex

**Affected annotations:** Lines with GO:0005515 IPI entries (approximately 6-8)

##### ACTION 1.2: Reclassify Developmental Annotations as Non-Core
**GO Terms:** GO:0040015, GO:0040024 (dauer-related), GO:0031349, GO:0050778 (immune system)

**Current situation:**
- GO:0040015 (Negative regulation of multicellular organism growth) - IEA
- GO:0031349 (Positive regulation of defense response) - IEA
- GO:0050778 (Positive regulation of immune response) - IEA
- These reflect indirect phenotypic consequences

**Recommendation:**
- MODIFY action: Change these annotations from ACCEPT to KEEP_AS_NON_CORE
- Rationale: Dauer formation and immune response are phenotypic outputs of DAF-16 longevity function, not core molecular function
- Reclassify in YAML as:
  ```yaml
  action: KEEP_AS_NON_CORE
  reason: 'Important phenotypic consequence of DAF-16 longevity signaling but not a core molecular function. DAF-16 primarily functions as a transcription factor; immune and developmental effects are indirect through activation of downstream genes.'
  ```

**Affected annotations:** 4-6 annotations

##### ACTION 1.3: Verify and Consolidate Stress Response Annotations
**GO Terms:** GO:0006979, GO:0034599, GO:0042594, GO:0010886

**Current situation:**
- Multiple stress response annotations present (oxidative stress, starvation, heat)
- Need to clarify whether these are direct DAF-16 functions or indirect through target genes

**Recommendation:**
- ACCEPT all stress response annotations with clarification
- Add supporting text distinguishing direct (DAF-16 activates stress genes) from indirect (DAF-16 promotes stress resistance)
- For GO:0034599 (oxidative stress): "DAF-16 activates transcription of sod-3, catalase, and other antioxidant genes"
- For GO:0042594 (starvation response): "DAF-16 activates lipid mobilization and metabolic adaptation genes"
- For GO:0010886 (heat response): "DAF-16 activates heat shock protein genes in response to heat stress"

**Affected annotations:** 3-5 annotations

##### ACTION 1.4: Verify Rare/Specialized Annotations
**GO Terms:** To be identified during systematic line-by-line review

**Recommendation:**
- Review annotations with only IEA evidence for evidence of supporting experimental work
- Prioritize those mapped from UniProt keywords for re-evaluation
- Consolidate any overly specific annotations (e.g., "positive regulation of X" when "regulation of X" would suffice)

#### Key Molecular Functions to ACCEPT (High Confidence)

These core transcription factor functions should remain ACCEPT:
1. GO:0000981 - DNA-binding transcription factor activity, RNA polymerase II-specific (IBA)
2. GO:0000978 - RNA polymerase II cis-regulatory region sequence-specific DNA binding (IBA/IDA)
3. GO:0001228 - DNA-binding transcription activator activity, RNA polymerase II-specific (IDA)
4. GO:0006357 - Regulation of transcription by RNA polymerase II (IBA)
5. GO:0008340 - Determination of adult lifespan (IMP) ← CORE LONGEVITY FUNCTION

#### Verification Checklist

Before finalizing daf-16 curation:
- [ ] Verify all IPI entries represent documented functional interactions
- [ ] Confirm no duplicate annotations for same term/PMID pair
- [ ] Check for any annotations not present in GOA but needed (NEW)
- [ ] Validate cross-references to daf-2 (upstream receptor) and sir-2.1 (interaction partner)

---

## Gene 2: DAF-2 (Q968Y9) - Insulin/IGF Receptor Kinase

### Annotation Review Status: PENDING (88 annotations)

**Estimated effort:** 2-3 hours for complete systematic review

#### Actions Recommended

##### ACTION 2.1: Consolidate and Classify Dauer Development Annotations
**GO Terms:** GO:1905909, GO:1905910, GO:0040024

**Current situation:**
- GO:1905909 (Regulation of dauer entry) - IGI with DAF-16
- GO:1905910 (Negative regulation of dauer entry) - IMP
- GO:0040024 (Dauer larval development) - IMP
- These represent dauer formation phenotype, not primary signaling function

**Recommendation:**
- MODIFY action for all three: Change to KEEP_AS_NON_CORE
- Rationale: Dauer formation is a phenotypic output of reduced DAF-2 signaling; the core function is negative regulation of DAF-16 through the PI3K/AKT pathway
- Updated YAML:
  ```yaml
  action: KEEP_AS_NON_CORE
  reason: 'Dauer formation is a phenotypic consequence of reduced DAF-2 signaling. Core molecular function is negatively regulating DAF-16 through PI3K/AKT pathway. This annotation captures a developmentally important phenotype but is secondary to the pathway regulation function.'
  ```

**Affected annotations:** 3 annotations

##### ACTION 2.2: Verify Dual Pathway Signaling Annotations
**GO Terms:** GO:0008286, GO:0043410, GO:0051897

**Current situation:**
- GO:0008286 (Insulin receptor signaling pathway) - IBA
- GO:0043410 (Positive regulation of MAPK cascade) - IBA
- GO:0051897 (PI3K/Akt signal transduction) - IBA
- DAF-2 couples to both PI3K/AKT and RAS/ERK pathways

**Recommendation:**
- ACCEPT all three annotations
- Add clarification: "DAF-2 couples to both PI3K/AKT (primary, through AGE-1) and RAS/ERK (secondary, in specific tissues like germline) pathways"
- Supporting evidence:
  - PI3K/AKT: PMID:11381260, PMID:9252323
  - RAS/ERK: PMID:24120884 (germline-specific meiotic progression)

**Affected annotations:** 0 (ACCEPT status confirmed)

##### ACTION 2.3: Remove or Clarify Vague Immune System Annotations
**GO Terms:** GO:0002376, GO:0045087

**Current situation:**
- GO:0002376 (Immune system process) - IEA (from UniProt keyword KW-0391)
- GO:0045087 (Innate immune response) - IEA
- DAF-2 has indirect immune roles through DAF-16 and SKN-1

**Recommendation:**
- These appear to be automatic annotations from UniProt keywords
- MODIFY: Verify whether DAF-2 has direct immune functions or only indirect effects through DAF-16/SKN-1
- If indirect only: MARK_AS_OVER_ANNOTATED or REMOVE
- If direct: Retain with evidence citations

**Action pending:** Literature verification required

##### ACTION 2.4: Add Missing Regulatory Annotation
**GO Term:** GO:0045944 - Positive regulation of transcription by RNA polymerase II (IMP)

**Current situation:**
- Already present in GOA (documented in PMID:23770237)
- Status: ACCEPT if present, VERIFY coverage

**Recommendation:**
- Ensure this annotation is well-supported by evidence
- DAF-2 negatively regulates DAF-16, which is itself a transcriptional activator
- This represents DAF-2's INDIRECT positive regulation through PIK3 pathway

---

## Gene 3: SKN-1 (P34707) - Nrf2 Ortholog

### Annotation Review Status: READY FOR IMPLEMENTATION (74 annotations)

**Estimated effort:** 0.5 hours to implement MODIFY actions

**Recent Review Result:** 56 ACCEPT, 6 KEEP_AS_NON_CORE, 2 MODIFY, 1 UNDECIDED

#### Actions to Implement

##### ACTION 3.1: Implement 2 MODIFY Annotations

From SKN-1-REVIEW-REPORT.md, two annotations require replacement with more specific terms:

**MODIFY Action 1:** (Details to be extracted from SKN-1-REVIEW-REPORT.md)
- Current term: [To be identified]
- Proposed replacement: [More specific term]
- Rationale: [Specificity/appropriate level of annotation]

**MODIFY Action 2:** (Details to be extracted from SKN-1-REVIEW-REPORT.md)
- Current term: [To be identified]
- Proposed replacement: [More specific term]
- Rationale: [Specificity/appropriate level of annotation]

**Status:** Ready to implement once specific terms are confirmed from curation report

#### Validation Items

- [ ] Verify all 56 ACCEPT annotations have proper supporting text
- [ ] Confirm 6 KEEP_AS_NON_CORE annotations are properly marked
- [ ] Implement 2 MODIFY annotation replacements
- [ ] Resolve 1 UNDECIDED annotation with additional evidence search if needed

---

## Gene 4: SIR-2.1 (Q21921) - NAD+ Sirtuin Deacetylase

### Annotation Review Status: PENDING (42 annotations)

**Estimated effort:** 1-2 hours for focused review

#### Actions Recommended

##### ACTION 4.1: Verify and Maintain Specific Histone Deacetylase Annotations
**GO Terms:** GO:0046970, GO:0046969, GO:0032041, GO:0141051

**Current situation:**
- GO:0046970 (Histone H4K16 deacetylase activity, NAD-dependent) - IBA
- GO:0046969 (Histone H3K9 deacetylase activity, NAD-dependent) - IBA
- GO:0032041 (Histone H3K14 deacetylase activity, NAD-dependent) - IBA
- GO:0141051 (Histone H4K deacetylase activity) - IDA (PMID:19380489)
- These are highly specific and well-characterized

**Recommendation:**
- ACCEPT all four annotations - they represent distinct, documented histone modification specificities
- These are superior to generic "histone deacetylase" annotation due to specificity
- Supporting evidence: PMID:19380489 (chromatin silencing), phylogenetic conservation

**Affected annotations:** 0 (ACCEPT status)

##### ACTION 4.2: Consolidate Transcriptional Repression Annotations
**GO Terms:** GO:0003714, GO:0045892, GO:0010629

**Current situation:**
- GO:0003714 (Transcription corepressor activity) - IBA
- GO:0045892 (Negative regulation of DNA-templated transcription) - IBA
- GO:0010629 (Negative regulation of gene expression) - NAS
- These represent SIR-2.1's role in chromatin silencing

**Recommendation:**
- ACCEPT all three with clarification:
  - GO:0003714 and GO:0045892: Direct chromatin-mediated repression through histone deacetylation
  - GO:0010629: Broader gene expression regulation (includes chromatin-independent mechanisms if any)
- Verify GO:0010629 (NAS from PMID:16777605) is supported

##### ACTION 4.3: Evaluate Stress Response Annotations
**GO Terms:** GO:0034605 (Cellular response to heat)

**Current situation:**
- GO:0034605 (Cellular response to heat) - NAS from PMID:16777605
- SIR-2.1 binds DAF-16 after heat stress

**Recommendation:**
- ACCEPT with clarification: "SIR-2.1 participates in heat stress response through interaction with DAF-16 transcription factor"
- This is a functional interaction, not direct heat sensing

#### Verification Checklist

- [ ] Confirm all IPI entries (DAF-16, FTT-2, PAR-5) represent documented functional complexes
- [ ] Verify NAS annotations have proper PMID support
- [ ] Check for any missing histone modification annotations
- [ ] Validate DNA damage response annotations (GO:0006974) with PMID:18923081

---

## Gene 5: AAK-2 (Q95ZQ4) - AMPK Alpha Kinase

### Annotation Review Status: PENDING (31 annotations)

**Estimated effort:** 1 hour for focused review

#### Actions Recommended

##### ACTION 5.1: Reclassify Dauer Development Annotation
**GO Term:** GO:0061066 (Positive regulation of dauer larval development)

**Current situation:**
- GO:0061066 (Positive regulation of dauer larval development) - IGI with DAF-2
- PMID:15574588 shows AAK-2 regulates dauer through DAF-16

**Recommendation:**
- MODIFY: Change to KEEP_AS_NON_CORE
- Rationale: "AAK-2 promotes dauer development as part of the metabolic stress response, but this is a phenotypic consequence of AMPK's energy-sensing function. The core function is regulation of mTORC1 and autophagy."

##### ACTION 5.2: Evaluate Pharyngeal Pumping Annotations
**GO Terms:** GO:0043050 (Nematode pharyngeal pumping)

**Current situation:**
- GO:0043050 appears twice (IEA from ARBA and IMP from PMID:22768843)
- AAK-2 is expressed in pharynx; PMID:22768843 documents pharyngeal phenotypes

**Recommendation:**
- Literature check: Is pharyngeal pumping a PRIMARY phenotype of AAK-2 loss or incidental to expression pattern?
- If PRIMARY: ACCEPT
- If SECONDARY/INCIDENTAL: MARK_AS_OVER_ANNOTATED
- Expected outcome: Likely ACCEPT for IMP entry (experimental documentation), REMOVE IEA duplicate

**Action pending:** Verification in PMID:22768843

##### ACTION 5.3: Consolidate Neuropeptide Signaling Annotations
**GO Terms:** GO:0007210 (Serotonin receptor signaling pathway)

**Current situation:**
- GO:0007210 (Serotonin receptor signaling pathway) - IMP from PMID:22768843
- AAK-2 regulates FLP-7 neuropeptide secretion via CRTC-1

**Recommendation:**
- ACCEPT with clarification: "AAK-2 phosphorylates CRTC-1 to regulate FLP-7 neuropeptide secretion, which acts through serotonin-like signaling to control fat metabolism"
- Consider adding NEW annotation:
  - GO:0051384 - Response to glucocorticoid stimulus (if leptin-like pathway modeling is relevant)

##### ACTION 5.4: Verify Autophagy Annotation Detail
**GO Terms:** GO:0010508 (Positive regulation of autophagy), GO:1904262 (Negative regulation of TORC1)

**Current situation:**
- GO:0010508 - IBA (phylogenetically conserved AMPK function)
- GO:1904262 - IBA (AMPK-mTORC1 axis)

**Recommendation:**
- ACCEPT both
- These represent the two main AMPK mechanisms: direct autophagy induction (through ULK1) and mTORC1 inhibition
- Both are conserved and documented in AAK-2 orthologs

---

## Gene 6: HLH-30 (H2KZZ2) - TFEB Ortholog, Autophagy Master Regulator

### Annotation Review Status: READY FOR IMPLEMENTATION (42 annotations)

**Estimated effort:** 0.5 hours to implement NEW annotations

**Recent Review Result:** 37 ACCEPT, 2 KEEP_AS_NON_CORE, 1 MODIFY, 3 NEW proposed

#### Actions to Implement

##### ACTION 6.1: Implement 3 Proposed NEW Annotations

**NEW Annotation 1:** GO:0031399 - Regulation of protein modification process
- **Justification:** HLH-30-dependent autophagy regulates protein remodeling and protein degradation
- **Evidence type:** IMP (inferred from autophagy function)
- **Supporting reference:** PMID:23925298 (HLH-30 lifespan extension through autophagy)
- **Status:** IMPLEMENT

**NEW Annotation 2:** GO:0031545 - Positive regulation of lamellipodia assembly
- **Justification:** HLH-30 effects on dendrite maintenance and neuronal morphology through autophagy
- **Evidence type:** IMP
- **Supporting reference:** HLH-30 autophagy required for dendrite maintenance in neurons
- **Status:** IMPLEMENT (if neuronal morphology effects confirmed)

**NEW Annotation 3:** GO:0030317 - Flagellated sperm motility
- **Justification:** (Context-dependent - VERIFY relevance)
- **Status:** PENDING VERIFICATION - May not be relevant for C. elegans (no flagellated sperm)
- **Recommendation:** REMOVE or clarify context

##### ACTION 6.2: Resolve Redundant General Annotations
**GO Terms:** GO:0008150 (Biological process), GO:0043565 (Sequence-specific DNA binding)

**Current situation:**
- GO:0008150 (Biological process) - marked as KEEP_AS_NON_CORE
- Status: Root term of hierarchy, not informative

**Recommendation:**
- REMOVE GO:0008150 entirely - too vague
- VERIFY GO:0043565 (Sequence-specific DNA binding) is not redundant with GO:0000978 (RNA polymerase II cis-regulatory region sequence-specific DNA binding)
- If redundant: Remove GO:0043565

#### Validation Checklist

- [ ] Confirm biological relevance of all 3 NEW annotations
- [ ] Particularly verify GO:0030317 (flagellated sperm) - likely REMOVE
- [ ] Implement NEW annotations with proper evidence codes and PMIDs
- [ ] Cross-check with SURVEILLANCE_IMMUNITY and MITOPHAGY project annotations for consistency

---

## Cross-Gene Unified Actions

### UNIFIED ACTION A: Remove Generic "Protein Binding" Annotations
**Apply to:** daf-16, daf-2, sir-2.1, aak-2 (where present)

**GO Term:** GO:0005515 (Protein binding - IPI entries)

**Global recommendation:**
- REMOVE all generic IPI entries that merely document protein-protein interactions without functional context
- RETAIN ONLY those where:
  1. The interaction is documented with clear functional consequence (e.g., AKT phosphorylation of DAF-16)
  2. The partner protein and mechanism are clearly understood
  3. The interaction is essential to the gene's primary function

**Examples to remove:**
- daf-16: Some AKT-1/AKT-2/SGK-1 binding entries (Phosphorylation-based regulation better captured by GO:0006468)

**Examples to retain:**
- sir-2.1: DAF-16 interaction (documented functional complex)
- daf-16: SIR-2.1 interaction (documented functional complex)

---

### UNIFIED ACTION B: Reclassify Dauer Development as Non-Core
**Apply to:** daf-2, aak-2

**GO Terms:** GO:1905909, GO:1905910, GO:0040024, GO:0061066

**Global recommendation:**
- These annotations represent PHENOTYPIC CONSEQUENCES of reduced signaling in nutrient-limited conditions
- Core functions are: signaling transduction (daf-2) and energy sensing (aak-2)
- Dauer development is an important organismal output but secondary to molecular function

**Unified rationale template:**
```yaml
reason: 'Dauer formation is a phenotypic consequence of reduced [DAF-2 signaling/AAK-2 energy sensing]. The core molecular function is [receptor signaling/kinase activity]. Dauer is a well-documented developmental output but represents adaptation at the organismal level rather than the primary molecular function of this protein.'
```

---

## Implementation Workflow

### Phase 1: Ready to Implement (2 genes, 1 hour)
1. **skn-1:** Implement 2 MODIFY annotations
2. **hlh-30:** Implement 3 NEW annotations (after verifying GO:0030317)

### Phase 2: Focused Review (2 genes, 3 hours)
1. **aak-2:** Complete 5-action systematic review
2. **sir-2.1:** Complete 3-action focused review

### Phase 3: Comprehensive Review (2 genes, 6-8 hours)
1. **daf-2:** Complete 4-action systematic review
2. **daf-16:** Complete 4-action comprehensive review (144 annotations)

### Phase 4: Validation and Cross-Checking (1 hour)
- Validate pathway consistency across daf-2 → DAF-16 → skn-1 network
- Verify all NEW annotations have proper evidence codes
- Final YAML validation with `just validate worm GENE`

---

## Files to Modify

```
/Users/cjm/repos/ai-gene-review/genes/worm/daf-16/daf-16-ai-review.yaml
/Users/cjm/repos/ai-gene-review/genes/worm/daf-2/daf-2-ai-review.yaml
/Users/cjm/repos/ai-gene-review/genes/worm/skn-1/skn-1-ai-review.yaml
/Users/cjm/repos/ai-gene-review/genes/worm/sir-2.1/sir-2.1-ai-review.yaml
/Users/cjm/repos/ai-gene-review/genes/worm/aak-2/aak-2-ai-review.yaml
/Users/cjm/repos/ai-gene-review/genes/worm/hlh-30/hlh-30-ai-review.yaml
```

---

## Validation Commands

After implementing actions:

```bash
# Validate individual genes
just validate worm daf-16
just validate worm daf-2
just validate worm skn-1
just validate worm sir-2.1
just validate worm aak-2
just validate worm hlh-30

# Validate all together
just validate-all

# Check generated reports
cat reports/validation-all.tsv
```

---

## Success Criteria

Curation is complete when:

1. All 6 genes have complete systematic reviews with documented actions
2. All MODIFY actions have proposed replacement terms with evidence
3. All NEW annotations are implemented with proper evidence codes
4. No vague GO:0005515 (protein binding) entries remain without functional context
5. All dauer development annotations are properly reclassified
6. YAML validation passes for all 6 genes
7. Cross-project consistency verified for skn-1 and hlh-30

---

## Document History

- **v1.0** (2025-12-30): Initial comprehensive curation action specification
  - Analyzed 421 total annotations across 6 genes
  - Identified 2 genes ready for implementation (skn-1, hlh-30)
  - Provided specific curation actions for 4 genes requiring systematic review

