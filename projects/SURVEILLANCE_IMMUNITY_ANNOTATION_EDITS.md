# Specific Annotation Edit Recommendations
## C. elegans Surveillance Immunity Genes (Priority 2)

This document provides specific edit recommendations for the AI review YAML files based on systematic curation of all annotations.

---

## GENE 1: ZIP-2 (Q21148) - Priority Changes

### File: `/Users/cjm/repos/ai-gene-review/genes/worm/zip-2/zip-2-ai-review.yaml`

#### Change 1: Replace GO:0005515 (protein binding) with ATF-2 interaction
**Current YAML location:** Line ~219-240

**Current:**
```yaml
- term:
    id: GO:0005515
    label: protein binding
  evidence_type: IPI
  original_reference_id: PMID:23661758
  review:
    summary: This annotation records physical interaction between ZIP-2 and ATF-2...
    action: MODIFY
    reason: While the physical interaction with ATF-2 is experimentally demonstrated, the generic "protein binding" term is uninformative. As a bZIP transcription factor, ZIP-2 forms dimers with other bZIP proteins...
    proposed_replacement_terms:
    - id: GO:0046983
      label: protein dimerization activity
```

**Status:** Already CORRECT in YAML - MODIFY action with GO:0046983 replacement already specified. No change needed.

#### Change 2: Replace GO:0005515 (protein binding) with CEBP-2 interaction
**Current YAML location:** Line ~241-264

**Status:** Already CORRECT in YAML - MODIFY action with GO:0046983 replacement already specified. No change needed.

#### Change 3: Replace GO:0005515 (protein binding) with Q21361 interaction
**Current GOA entry:** Line 13 of goa.tsv
**Current YAML:** Not yet in YAML (should be added)

**Recommendation:** Add to existing_annotations in ZIP-2 YAML file:
```yaml
- term:
    id: GO:0005515
    label: protein binding
  evidence_type: IPI
  original_reference_id: PMID:23661758
  review:
    summary: This annotation records physical interaction between ZIP-2 and Q21361 (another bZIP protein), demonstrated by in vitro protein-protein interaction assays studying bZIP dimerization networks.
    action: MODIFY
    reason: While the physical interaction is experimentally demonstrated, the generic "protein binding" term is uninformative. bZIP proteins form obligate dimers through their leucine-zipper domains.
    proposed_replacement_terms:
    - id: GO:0046983
      label: protein dimerization activity
    supported_by:
    - reference_id: PMID:23661758
      supporting_text: We studied the basic region-leucine zipper (bZIP) transcription factors and quantified bZIP dimerization networks for five metazoan and two single-cell species
```

#### Summary for ZIP-2
- **Status:** YAML file is well-curated and up-to-date
- **Minor addition:** One IPI annotation (Q21361) may be missing from YAML review section
- **All protein binding MODIFYs already present:** ZIP-2 review already contains correct MODIFY recommendations

---

## GENE 2: CEBP-2 (Q8IG69) - Priority Changes

### File: `/Users/cjm/repos/ai-gene-review/genes/worm/cebp-2/cebp-2-ai-review.yaml`

#### Critical Issue: Redundant GO:0005515 Annotations

**Problem:** CEBP-2 has 8+ separate "protein binding" IPI annotations from PMID:23661758 listing different bZIP interaction partners:
- Line 12: UniProtKB:A0A1I6CMA8
- Line 13: UniProtKB:Q21148 (ZIP-2)
- Line 14: UniProtKB:Q21361
- Line 15: UniProtKB:Q22156
- Line 16: UniProtKB:Q23272
- Line 17: UniProtKB:Q94126
- Line 18: UniProtKB:Q9N5A8
- Line 19: UniProtKB:Q9XUK2
- Plus additional partners from PMID:23791784

**Current YAML status:** These are marked as MARK_AS_OVER_ANNOTATED in some cases (lines 201-234 of YAML)

**Recommended action:** Either:

**Option A: Consolidate into single annotation**
Replace all 8 "protein binding" annotations from PMID:23661758 with single entry:
```yaml
- term:
    id: GO:0046983
    label: protein dimerization activity
  evidence_type: IEA (or change to IPI with PMID:23661758)
  original_reference_id: PMID:23661758
  review:
    summary: CEBP-2 forms heterodimers with multiple bZIP transcription factors including ZIP-2, ZIP-3, ZIP-9, ZIP-11, ATF-2, ATF-4, ATFS-1, CES-2, and others as demonstrated by comprehensive bZIP protein-protein interaction network study.
    action: ACCEPT
    reason: bZIP proteins are obligate heterodimerizers. CEBP-2 interacts with multiple partners through its leucine-zipper domain. GO:0046983 better captures the specific mechanism (dimerization) than the generic "protein binding" term.
    supported_by:
    - reference_id: PMID:23661758
      supporting_text: We studied the basic region-leucine zipper (bZIP) transcription factors and quantified bZIP dimerization networks for five metazoan and two single-cell species, measuring interactions in vitro for 2891 protein pairs
    - reference_id: UniProtKB:Q8IG69
      supporting_text: 'INTERACTION WITH: Q21148 (zip-2), Q21361, Q22156, Q23272, Q94126, Q9N5A8, Q9XUK2'
```

**Option B: Keep specific functionally important interactions**
Keep only CEBP-2 interactions with ZIP-2 and ZIP-11 (documented to work together in immunity) and mark the others as MARK_AS_OVER_ANNOTATED:

```yaml
# Functionally important: ZIP-2 partnership in surveillance immunity
- term:
    id: GO:0046983
    label: protein dimerization activity
  evidence_type: IPI
  original_reference_id: PMID:23791784
  review:
    summary: CEBP-2 forms obligate heterodimers with ZIP-2, essential for surveillance immunity.
    action: ACCEPT
    reason: Functionally validated interaction central to innate immunity pathway.
    proposed_replacement_terms: N/A (GO:0046983 is appropriate)

# Functionally important: ZIP-11 partnership in immunity
- term:
    id: GO:0046983
    label: protein dimerization activity
  evidence_type: IPI
  original_reference_id: PMID:34804026
  review:
    summary: CEBP-2 forms heterodimers with ZIP-11 to mediate immune responses.
    action: ACCEPT
    reason: ZIP-11/CEBP-2 partnership mediates immune responses independently of PMK-1/p38 pathway.
```

**Current YAML Status:** Review already contains appropriate MODIFY/MARK_AS_OVER_ANNOTATED actions for these annotations (lines 197-253). Consolidation or simplification recommended but not critical.

#### Change for GO:0019216 (Lipid Metabolism)
**Current YAML location:** Line 348-367

**Current action:** KEEP_AS_NON_CORE ✓

**Status:** CORRECT - Already marked as non-core; no change needed.

#### Summary for CEBP-2
- **Status:** YAML review is comprehensive and largely correct
- **Main recommendation:** Consider consolidating 8 redundant "protein binding" annotations from PMID:23661758 into single GO:0046983 annotation for clarity
- **Existing YAML already marks these appropriately:** MODIFY or MARK_AS_OVER_ANNOTATED actions already present

---

## GENE 3: IRG-1 (O16327) - Priority Changes

### File: `/Users/cjm/repos/ai-gene-review/genes/worm/irg-1/irg-1-ai-review.yaml`

**Status:** EXCELLENT - YAML review is comprehensive and well-reasoned. Minimal changes needed.

#### No critical changes recommended

**Assessment:**
- All 7 GOA annotations appropriately reviewed
- ND (No Data) annotations for molecular_function and cellular_component correctly justified
- Expression-based annotations (IEP) appropriately justified
- Well-balanced between accepting what is known and acknowledging unknowns

#### Optional Enhancement: Add speculative molecular function annotation
**If investigators wish to flag potential NADAR domain activity:**

```yaml
proposed_new_terms:
- term:
    id: GO:0003950
    label: NAD(+) ADP-ribosyltransferase activity
  evidence_type: SPECULATION (not standard GO evidence)
  reasoning: irg-1 contains NADAR domain (IPR012816) characteristic of ADP-ribosylhydrolases, but enzymatic activity has not been experimentally confirmed. Represents a testable hypothesis for future experiments.
```

**Current YAML Status:** proposed_new_terms is empty (line 296) - addition above is optional pending experimental validation.

---

## GENE 4: ELT-2 (Q10655) - Priority Changes

### File: `/Users/cjm/repos/ai-gene-review/genes/worm/elt-2/elt-2-ai-review.yaml`

#### Critical Changes: Remove Over-Annotated Generic Terms

The following 6 GO terms are superseded by more specific child terms and should be marked MARK_AS_OVER_ANNOTATED:

##### Over-annotation 1: GO:0006351 (DNA-templated transcription)
**GOA line:** Line 12 in goa.tsv
**Evidence:** IEA GO_REF:0000120

**Action:** Add to YAML existing_annotations section:
```yaml
- term:
    id: GO:0006351
    label: DNA-templated transcription
  evidence_type: IEA
  original_reference_id: GO_REF:0000120
  review:
    summary: This IEA annotation from combined automated annotation methods captures ELT-2's involvement in transcription but is superseded by more specific regulatory terms.
    action: MARK_AS_OVER_ANNOTATED
    reason: GO:0006357 (regulation of transcription by RNA polymerase II) and GO:0045944 (positive regulation of transcription by RNA polymerase II) are more specific and better characterize ELT-2's transcriptional role. The parent term adds little value.
    supported_by:
    - reference_id: GO_REF:0000120
      supporting_text: Combined automated annotation from InterPro and UniProtKB keywords
```

##### Over-annotation 2: GO:0006355 (regulation of DNA-templated transcription)
**GOA line:** Line 13 in goa.tsv
**Evidence:** IEA GO_REF:0000002

**Action:** Add to YAML:
```yaml
- term:
    id: GO:0006355
    label: regulation of DNA-templated transcription
  evidence_type: IEA
  original_reference_id: GO_REF:0000002
  review:
    summary: This InterPro-derived annotation is superseded by more specific regulatory terms.
    action: MARK_AS_OVER_ANNOTATED
    reason: GO:0006357 (regulation of transcription by RNA polymerase II) provides more specificity. Both parent and child terms are present, making parent term redundant.
    supported_by:
    - reference_id: GO_REF:0000002
      supporting_text: InterPro domain mapping for GATA transcription factor
```

##### Over-annotation 3: GO:0009888 (tissue development)
**GOA line:** Line 16 in goa.tsv
**Evidence:** IEA GO_REF:0000117

**Action:** Add to YAML:
```yaml
- term:
    id: GO:0009888
    label: tissue development
  evidence_type: IEA
  original_reference_id: GO_REF:0000117
  review:
    summary: This broad developmental term is superseded by more specific process.
    action: MARK_AS_OVER_ANNOTATED
    reason: GO:0007492 (endoderm development) is much more specific to ELT-2's role. The intestine (derived from endoderm) is ELT-2's exclusive expression site. GO:0007492 with experimental evidence better captures this core developmental function.
    supported_by:
    - reference_id: PMID:9659934
      supporting_text: elt-2 is essential for specific cell fate decisions in the early embryo
```

##### Over-annotation 4: GO:0030154 (cell differentiation)
**GOA line:** Line 17 in goa.tsv
**Evidence:** IEA GO_REF:0000043

**Action:** Add to YAML:
```yaml
- term:
    id: GO:0030154
    label: cell differentiation
  evidence_type: IEA
  original_reference_id: GO_REF:0000043
  review:
    summary: This broad differentiation term is superseded by more specific terms.
    action: MARK_AS_OVER_ANNOTATED
    reason: GO:0030856 (regulation of epithelial cell differentiation) is much more specific. ELT-2's role is specifically in epithelial (intestinal) cell fate and differentiation, not general cell differentiation.
    supported_by:
    - reference_id: PMID:9659934
      supporting_text: ELT-2 regulates intestinal epithelial cell differentiation through control of lineage-specific genes
```

##### Over-annotation 5: GO:0000976 (transcription cis-regulatory region binding)
**GOA line:** Line 8 in goa.tsv
**Evidence:** IEA GO_REF:0000117

**Action:** Add to YAML:
```yaml
- term:
    id: GO:0000976
    label: transcription cis-regulatory region binding
  evidence_type: IEA
  original_reference_id: GO_REF:0000117
  review:
    summary: This generic DNA binding term is superseded by more specific sequence-specific binding terms.
    action: MARK_AS_OVER_ANNOTATED
    reason: GO:0000978 (RNA polymerase II cis-regulatory region sequence-specific DNA binding) provides more specificity and is well-documented in literature with direct binding studies (PMID:15733671, PMID:15734735).
    supported_by:
    - reference_id: PMID:15733671
      supporting_text: The gut-specific GATA factor ELT-2 binds to this site in vitro
    - reference_id: PMID:10518545
      supporting_text: Direct visualization of ELT-2 binding in living embryos using GFP fusions
```

##### Over-annotation 6: GO:0010468 (regulation of gene expression)
**GOA line:** Line 32 in goa.tsv
**Evidence:** IMP PMID:26016853

**Action:** Add to YAML:
```yaml
- term:
    id: GO:0010468
    label: regulation of gene expression
  evidence_type: IMP
  original_reference_id: PMID:26016853
  review:
    summary: This very broad regulation term is superseded by more specific transcriptional terms.
    action: MARK_AS_OVER_ANNOTATED
    reason: GO:0045944 (positive regulation of transcription by RNA polymerase II) better captures the specific mechanism. ELT-2 functions as a transcriptional activator, not through other gene expression regulatory mechanisms.
    supported_by:
    - reference_id: PMID:26016853
      supporting_text: ELT-2-dependent transcriptional activation of intestinal genes during immune response
```

#### Summary for ELT-2
- **Current YAML Status:** Does not yet contain reviews for all 52+ GOA annotations
- **Priority additions:** Add MARK_AS_OVER_ANNOTATED reviews for the 6 generic parent terms listed above
- **Existing annotations in YAML:** Core annotations appear well-reviewed; focus additions on the generic terms not yet addressed
- **Overall assessment:** Well-documented gene with strong experimental evidence; removing 6 redundant annotations will improve clarity

---

## GENE 5: HLH-30 (H2KZZ2) - Priority Changes

### File: `/Users/cjm/repos/ai-gene-review/genes/worm/hlh-30/hlh-30-ai-review.yaml`

#### Changes: Remove 3 Over-Annotated Generic Terms

##### Over-annotation 1: GO:0003677 (DNA binding)
**GOA line:** Line 6 in goa.tsv
**Evidence:** IEA GO_REF:0000043

**Action:** Add to YAML:
```yaml
- term:
    id: GO:0003677
    label: DNA binding
  evidence_type: IEA
  original_reference_id: GO_REF:0000043
  review:
    summary: Generic DNA binding annotation is superseded by more specific transcription factor binding terms.
    action: MARK_AS_OVER_ANNOTATED
    reason: GO:0000978 (RNA polymerase II cis-regulatory region sequence-specific DNA binding) and GO:0000981 (DNA-binding transcription factor activity, RNA polymerase II-specific) are more informative for HLH-30 as a bHLH transcription factor. The generic DNA binding term adds little functional information.
    supported_by:
    - reference_id: GO_REF:0000043
      supporting_text: UniProtKB keyword mapping for DNA-binding bHLH protein
```

##### Over-annotation 2: GO:0006351 (DNA-templated transcription)
**GOA line:** Line 9 in goa.tsv
**Evidence:** IEA GO_REF:0000043

**Action:** Add to YAML:
```yaml
- term:
    id: GO:0006351
    label: DNA-templated transcription
  evidence_type: IEA
  original_reference_id: GO_REF:0000043
  review:
    summary: This broad transcription process term is superseded by more specific regulatory terms.
    action: MARK_AS_OVER_ANNOTATED
    reason: GO:0006357 (regulation of transcription by RNA polymerase II) is more specific and IBA-supported. HLH-30 functions as a transcriptional regulator, not just in DNA-templated transcription generally.
    supported_by:
    - reference_id: GO_REF:0000043
      supporting_text: UniProtKB keyword mapping for transcription factor
```

##### Over-annotation 3: GO:0007165 (signal transduction)
**GOA line:** Line 8 in goa.tsv (likely position - verify in actual GOA file)
**Evidence:** IEA GO_REF:0000043

**Action:** Add to YAML (if present in GOA):
```yaml
- term:
    id: GO:0007165
    label: signal transduction
  evidence_type: IEA
  original_reference_id: GO_REF:0000043
  review:
    summary: Very broad signal transduction term is overly general for HLH-30's specific roles.
    action: MARK_AS_OVER_ANNOTATED
    reason: HLH-30 functions primarily as a transcriptional regulator of stress-response genes, not as a general signal transduction component. Specific annotations to GO:0006357, GO:0045944, GO:0016239 (autophagy) better capture its functions. This generic term adds little value beyond more specific regulatory annotations.
    supported_by:
    - reference_id: PMID:28198373
      supporting_text: HLH-30 acts as a transcription factor to activate autophagy genes in response to stress
```

#### Special Note: Dual Localization Annotations
**Current YAML assessment:** Multiple annotations to both GO:0005634 (nucleus) and GO:0005737 (cytoplasm) are APPROPRIATE and should be KEPT

**Rationale:**
- HLH-30 shows stress-dependent nuclear import
- Multiple IDA studies document both localizations
- Different experimental conditions show different ratios
- This complexity should be preserved in annotations

**Examples of appropriate dual localization:**
- PMID:27875098: Both nucleus and cytoplasm (separate IDA annotations)
- PMID:27184844: Both nucleus and cytoplasm
- PMID:24882217: Both nucleus and cytoplasm
- PMID:28198373: Nucleus during starvation stress

#### Summary for HLH-30
- **Current YAML Status:** Appears to be well-reviewed for core functions
- **Priority additions:** Add MARK_AS_OVER_ANNOTATED reviews for 3 generic terms
- **No changes needed for:** Localization annotations, autophagy annotations, immune annotations (all well-supported)
- **Overall assessment:** Complex gene with multiple integrated functions; existing comprehensive annotation appropriate

---

## GENE 6: FSHR-1 (L8EC40) - Priority Changes

### File: `/Users/cjm/repos/ai-gene-review/genes/worm/fshr-1/fshr-1-ai-review.yaml`

#### Critical Recommendation: Validate Immune Annotations

**Current Status:** YAML review (lines 1-end) does not appear to address immune annotations in detail

**Annotations requiring validation:**
1. **GO:0050829** (defense response to Gram-negative bacterium) - IMP PMID:19196974
2. **GO:0045087** (innate immune response) - IMP PMID:26360906
3. **GO:0006979** (response to oxidative stress) - IMP PMID:26360906
4. **GO:1990170** (stress response to cadmium ion) - IMP PMID:26360906

**Recommendation:** Before finalizing YAML review:
1. Retrieve and read PMID:19196974 to understand basis of Gram-negative defense annotation
2. Retrieve and read PMID:26360906 to understand basis of immune/stress annotations
3. Determine whether FSHR-1 has direct role or indirect effect
4. Verify mechanism: Is immune function through G-protein/cAMP signaling? Hormone-dependent?

#### Conditional Recommendations Based on Validation

**If immune function is robustly documented:**
```yaml
- term:
    id: GO:0050829
    label: defense response to Gram-negative bacterium
  evidence_type: IMP
  original_reference_id: PMID:19196974
  review:
    summary: [Description of FSHR-1 role in immune defense based on paper content]
    action: ACCEPT
    reason: [Mechanistic explanation of how FSHR-1 GPCR signaling contributes to immune defense]
    supported_by:
    - reference_id: PMID:19196974
      supporting_text: [Direct quote from paper]
```

**If immune function is ambiguous or indirect:**
```yaml
- term:
    id: GO:0050829
    label: defense response to Gram-negative bacterium
  evidence_type: IMP
  original_reference_id: PMID:19196974
  review:
    summary: [Description of phenotype observed]
    action: UNDECIDED
    reason: FSHR-1 is a GPCR with functions in hormone sensing and signal transduction. The connection between FSHR-1 and innate immunity is not clear. The immune phenotype observed may be indirect (e.g., through effects on other signaling pathways or organismal stress). Direct mechanistic role in immune defense is unclear. Recommend additional literature review and potentially re-categorization of this annotation.
    additional_reference_ids:
    - PMID:19196974
    - PMID:26360906
```

#### Summary for FSHR-1
- **Current YAML Status:** Appears to contain reviews but should be validated
- **Priority action:** Literature validation of immune annotations before finalizing
- **Confidence in GPCR annotations:** HIGH - Structure and basic signaling functions well-established
- **Confidence in immune annotations:** MEDIUM-LOW - Sparse evidence, mechanism unclear
- **Recommendation:** Conditional acceptance pending evidence review

---

## SUMMARY OF EDITS REQUIRED

| Gene | File | Type | Count | Status | Priority |
|------|------|------|-------|--------|----------|
| ZIP-2 | YAML | MODIFY | 1-3 | Already done | None |
| CEBP-2 | YAML | CONSOLIDATE | 8 | Partial | Medium |
| IRG-1 | YAML | NONE | 0 | Complete | Low |
| ELT-2 | YAML | ADD MARK_OVER | 6 | Needed | High |
| HLH-30 | YAML | ADD MARK_OVER | 3 | Needed | High |
| FSHR-1 | YAML | VALIDATE | 4 | Needed | High |

---

## VALIDATION WORKFLOW

1. **ELT-2:** Add 6 MARK_AS_OVER_ANNOTATED entries for generic transcription terms
2. **HLH-30:** Add 3 MARK_AS_OVER_ANNOTATED entries for generic terms
3. **CEBP-2:** Consider consolidating 8 redundant protein binding annotations
4. **FSHR-1:** Retrieve and analyze PMID:19196974 and PMID:26360906; decide on ACCEPT vs UNDECIDED for immune annotations
5. **Run validation:** `just validate-all` to ensure YAML files pass schema validation
6. **Review in files:** Spot-check ELT-2 and HLH-30 YAML against GAO files to ensure all annotations are covered

---

## FILE PATHS FOR REFERENCE

```
/Users/cjm/repos/ai-gene-review/genes/worm/zip-2/zip-2-ai-review.yaml
/Users/cjm/repos/ai-gene-review/genes/worm/cebp-2/cebp-2-ai-review.yaml
/Users/cjm/repos/ai-gene-review/genes/worm/irg-1/irg-1-ai-review.yaml
/Users/cjm/repos/ai-gene-review/genes/worm/elt-2/elt-2-ai-review.yaml
/Users/cjm/repos/ai-gene-review/genes/worm/hlh-30/hlh-30-ai-review.yaml
/Users/cjm/repos/ai-gene-review/genes/worm/fshr-1/fshr-1-ai-review.yaml
```

---

## NEXT STEPS

1. **Immediate:** Share this document with curation team for review
2. **Validation round 1:** Edit ELT-2 and HLH-30 YAML files with MARK_AS_OVER_ANNOTATED entries
3. **Validation round 2:** Run schema validation tests
4. **Validation round 3:** Manually review FSHR-1 literature
5. **Final:** Finalize all 6 gene YAML files for project completion
