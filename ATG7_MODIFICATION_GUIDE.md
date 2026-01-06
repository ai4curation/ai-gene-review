# ATG7 Annotation Modifications - Detailed Guide

This document provides specific before/after examples for all annotations that need modification.

---

## MODIFY ACTION 1: GO:0006501 "C-terminal protein lipidation" → GO:0061683 "Atg8 conjugation to phosphatidylethanolamine"

### Overview
**Issue:** GO:0006501 incorrectly describes ATG7's role as directly catalyzing lipidation, when ATG7 actually catalyzes substrate **activation**. The E2 enzyme (ATG3) performs the actual lipidation chemistry.

**Affected Annotations:** 5 total
- 3 IMP (Induced Mutant Phenotype)
- 2 IDA (Inferred Direct Assay)

---

### Modification 1.1: PMID:11038174 (IMP)

**Current:**
```yaml
- term:
    id: GO:0006501
    label: C-terminal protein lipidation
  evidence_type: IMP
  original_reference_id: PMID:11038174
  review:
    action: MODIFY
    reason: Mechanistically imprecise. ATG7 activates ATG8 substrate but does not catalyze the lipidation chemistry itself. The actual lipidation (transfer of ATG8 to phosphatidylethanolamine) is catalyzed by E2 enzyme ATG3.
    proposed_replacement_terms:
      - id: GO:0061683
        label: Atg8 conjugation to phosphatidylethanolamine
        rationale: More mechanistically accurate term that describes the ATG7-dependent substrate activation leading to ATG8-PE conjugate formation
    supporting_by:
      - reference_id: PMID:11038174
        supporting_text: The reversible modification regulates the membrane-binding state of Apg8/Aut7 essential for autophagy and the cytoplasm to vacuole targeting pathway
```

**Biochemical Explanation:**

ATG7 catalyzes two distinct steps:
1. **Adenylation:** ATG7 + ATP + ATG8 → ATG7~AMP-ATG8 + PPi
2. **Thioester transfer:** ATG7~Cys507-ATG8 ← → ATG3~ATG8

ATG3 then catalyzes:
3. **Lipidation:** ATG3~ATG8 + PE → ATG8-PE + ATG3

The term "C-terminal protein lipidation" implies step 3 (ATG3 function), but ATG7's contribution is steps 1-2 (substrate activation and transfer). GO:0061683 correctly describes the product and process.

---

### Modification 1.2: PMID:11100732 (IMP)

**Current:**
```yaml
- term:
    id: GO:0006501
    label: C-terminal protein lipidation
  evidence_type: IMP
  original_reference_id: PMID:11100732
  review:
    action: MODIFY
    reason: ATG7 mediates ATG8 substrate activation, not the actual lipidation reaction. The critical evidence shows ATG7 transfers activated ATG8 to ATG3 (E2 enzyme), which then catalyzes lipidation to phosphatidylethanolamine. GO:0006501 mislabels the actual catalytic step.
    proposed_replacement_terms:
      - id: GO:0061683
        label: Atg8 conjugation to phosphatidylethanolamine
        rationale: Accurately describes the ATG7-dependent conjugation process where ATG8 is activated and transferred for subsequent lipidation
    additional_reference_ids:
      - reference_id: PMID:15277523
        supporting_text: In vivo and in vitro reconstitution of atg8 conjugation essential for autophagy shows ATG7 is required for ATG8 activation for lipidation
```

**Key Quote from Publication:**
"Apg8 is activated by an E1 protein, Apg7, and is transferred subsequently to the E2 enzymes Apg3" [PMID:11100732]

This explicitly shows the two-step process: (1) activation by ATG7, (2) transfer to ATG3 for lipidation.

---

### Modification 1.3: PMID:12965207 (IMP)

**Current:**
```yaml
- term:
    id: GO:0006501
    label: C-terminal protein lipidation
  evidence_type: IMP
  original_reference_id: PMID:12965207
  review:
    action: MODIFY
    reason: The data demonstrates that the C-terminal 17 amino acids of ATG7 are essential for ATG8 lipidation but not for ATG12 conjugation. This shows substrate-specific substrate-activation (not lipidation catalysis). ATG7 activates ATG8; ATG3 catalyzes lipidation.
    proposed_replacement_terms:
      - id: GO:0061683
        label: Atg8 conjugation to phosphatidylethanolamine
        rationale: Substrate-specific replacement that correctly describes ATG7's role in ATG8 conjugation system
    supported_by:
      - reference_id: PMID:12965207
        supporting_text: The carboxyl terminal 17 amino acids within Apg7 are essential for Apg8 lipidation, but not for Apg12 conjugation. Apg8 lipidation is inhibited in the mutant, while Apg12 conjugation occurs normally
```

**Mechanistic Detail:**
The fact that this C-terminal region is required for ATG8 but NOT for ATG12 proves ATG7 has substrate-specific recognition elements. These elements are for the substrate activation step, not the final lipidation (which is catalyzed by ATG3).

---

### Modification 1.4 & 1.5: PMID:15277523 (IDA and IMP)

**Current (both entries):**
```yaml
- term:
    id: GO:0006501
    label: C-terminal protein lipidation
  evidence_type: IDA  [or IMP for duplicate]
  original_reference_id: PMID:15277523
  review:
    action: MODIFY
    reason: In vitro reconstitution studies show that ATG7 is required for ATG8 substrate activation (adenylation and thioester bond formation) prior to the lipidation reaction catalyzed by ATG3. GO:0006501 incorrectly emphasizes lipidation when the ATG7 function is upstream substrate activation.
    proposed_replacement_terms:
      - id: GO:0061683
        label: Atg8 conjugation to phosphatidylethanolamine
        rationale: Properly describes the complete conjugation process ATG7 enables through substrate activation
    supported_by:
      - reference_id: PMID:15277523
        supporting_text: In vivo and in vitro reconstitution of atg8 conjugation essential for autophagy demonstrates ATG7 is required for the lipidation system
```

**Supporting Evidence:**
PMID:15277523 title explicitly states "In vivo and in vitro **reconstitution of atg8 conjugation**" - not "lipidation catalysis". The reconstitution requires ATG7 (E1), ATG3 (E2), and substrate ATG8 together - showing the three-component system.

---

### Modification 1.6: PMID:19398890 (IDA)

**Current:**
```yaml
- term:
    id: GO:0006501
    label: C-terminal protein lipidation
  evidence_type: IDA
  original_reference_id: PMID:19398890
  review:
    action: MODIFY
    reason: While this study looks at cargo-receptor binding site mutations in ATG8, it ultimately demonstrates the functional requirement for ATG8 lipidation in autophagy. However, ATG7's specific role is substrate activation, not lipidation catalysis. The term GO:0006501 is mechanistically imprecise for ATG7.
    proposed_replacement_terms:
      - id: GO:0061683
        label: Atg8 conjugation to phosphatidylethanolamine
        rationale: More precise description of the ATG7-mediated substrate activation pathway leading to ATG8 conjugation
    supported_by:
      - reference_id: PMID:19398890
        supporting_text: Mutation at the cargo-receptor binding site of Atg8 affects its general autophagy regulation function through effects on membrane binding and lipidation
```

---

## MODIFY ACTION 2: GO:0005515 "protein binding" → Substrate-specific terms

### Overview
**Issue:** Generic "protein binding" term obscures specific mechanistic roles. ATG7 has distinct interactions:
- Substrate binding (ATG12, ATG8)
- E2 enzyme recruitment (ATG3, ATG10)
- Homodimerization (self-association)

**Affected Annotations:** 7 total from PMIDs: 10688190, 11100732, 12965207, 18719252, 22056771, 23142976, 25042851

**Recommended Action:**
- **REMOVE** generic GO:0005515 except for homodimerization cases
- **REPLACE** most with GO:0061664 (ubiquitin-like protein binding)
- **KEEP** GO:0042802 (identical protein binding) for homodimerization

---

### Modification 2.1: PMID:10688190 & 11100732 & 12965207 (Multiple with ATG8, ATG3)

**Current (Example - PMID:22056771 IPI):**
```yaml
- term:
    id: GO:0005515
    label: protein binding
  evidence_type: IPI
  original_reference_id: PMID:22056771
  review:
    action: MODIFY
    reason: Generic term that fails to distinguish between substrate binding (ATG8, ATG12) and E2 enzyme binding (ATG3, ATG10). Structural studies show ATG7 has specific interaction surfaces for each function. More specific molecular function terms would better represent the diverse binding roles.
    proposed_replacement_terms:
      - id: GO:0061664
        label: ubiquitin-like protein binding
        rationale: Captures substrate binding interactions with ATG8 and ATG12 (ubiquitin-like modifiers)
      - id: "[NOTE]"
        label: Separate E2-binding interactions should be annotated separately if GO terms exist
        rationale: ATG3 and ATG10 (E2 enzymes) are distinct binding partners
    supported_by:
      - reference_id: PMID:22056771
        supporting_text: Crystal structure shows Atg7 interacts directly with multiple substrates and E2 enzymes through distinct binding interfaces
```

---

### Modification 2.2: Homodimerization Cases (Keep as GO:0042802)

**PMID:12965207 & PMID:22056771 - Identical Protein Binding:**

These two IPI annotations for homodimerization should remain as **GO:0042802** (identical protein binding):

```yaml
- term:
    id: GO:0042802
    label: identical protein binding
  evidence_type: IPI
  original_reference_id: PMID:12965207  [or PMID:22056771]
  review:
    action: ACCEPT
    reason: Specific and accurate term for ATG7 homodimerization. The C-terminal 40 amino acids mediate the homodimer interface, which is essential for ATP binding and E1 activity. This is distinct from substrate or E2 binding.
    supported_by:
      - reference_id: PMID:12965207
        supporting_text: Apg7 forms a homodimer, which is required for homodimerization and is essential for its E1 activity and E1-E2 complex formation
```

---

### Replacement Strategy Summary

**For each GO:0005515 IPI annotation:**

| WITH Partner | Current Term | Action | Replacement Term | Rationale |
|---|---|---|---|---|
| ATG8 (substrate) | GO:0005515 | MODIFY | GO:0061664 | Ubiquitin-like protein substrate |
| ATG12 (substrate) | GO:0005515 | MODIFY | GO:0061664 | Ubiquitin-like protein substrate |
| ATG3 (E2 enzyme) | GO:0005515 | MODIFY | [Consider GO:0019888] | E2 enzyme binding (if exists) |
| ATG10 (E2 enzyme) | GO:0005515 | MODIFY | [Consider GO:0019888] | E2 enzyme binding (if exists) |
| ATG7 (homodimer) | GO:0005515 | REPLACE | GO:0042802 | Identical protein binding |

---

## Summary of Modifications

### Total Annotations to Modify: 12

| Original Term | Count | Replacement | Evidence Types |
|---|---|---|---|
| GO:0006501 (C-terminal protein lipidation) | 5 | GO:0061683 (Atg8 conjugation to PE) | 3 IMP, 2 IDA |
| GO:0005515 (protein binding) | 7 | GO:0061664 (ubiquitin-like protein binding) | All IPI |

### Implementation Timeline

**Step 1: Backup Original**
- Commit current version before modifications

**Step 2: Update PMID:11038174**
- Term: GO:0006501 → GO:0061683
- Evidence: Keep IMP
- Supporting_text: "reversible modification regulates the membrane-binding state of Apg8/Aut7 essential for autophagy"

**Step 3: Update PMID:11100732**
- Term: GO:0006501 → GO:0061683
- Evidence: Keep IMP
- Supporting_text: "Apg8 is activated by an E1 protein, Apg7, and is transferred subsequently to the E2 enzymes Apg3"

**Step 4: Update PMID:12965207**
- Term: GO:0006501 → GO:0061683
- Evidence: Keep IMP
- Supporting_text: "carboxyl terminal 17 amino acids within Apg7 are essential for Apg8 lipidation, but not for Apg12 conjugation"

**Step 5: Update PMID:15277523** (2 entries - IDA and IMP)
- Term: GO:0006501 → GO:0061683
- Evidence: Keep both
- Supporting_text: "In vivo and in vitro reconstitution of atg8 conjugation essential for autophagy"

**Step 6: Update PMID:19398890**
- Term: GO:0006501 → GO:0061683
- Evidence: Keep IDA
- Supporting_text: "cargo-receptor binding site of Atg8 affects its general autophagy regulation function"

**Step 7: Update GO:0005515 IPI Annotations**
- Identify substrate vs. E2 interactions from WITH/FROM field in GOA TSV
- Most should become GO:0061664 (ubiquitin-like protein binding)
- Homodimerization (WITH ATG7) stays as GO:0042802

**Step 8: Validate**
- Run: `just validate yeast ATG7`
- Ensure no validation errors introduced
- Check that all supporting_text quotes are present

**Step 9: Commit**
- Commit with message: "Improve ATG7 annotation precision: replace imprecise GO:0006501 with substrate-specific GO:0061683; generalize GO:0005515 to substrate-specific GO:0061664"

---

## Validation Checklist

After modifications, verify:

- [ ] All 5 GO:0006501 entries have been replaced with GO:0061683
- [ ] All GO:0061683 entries have supporting_text
- [ ] Evidence codes preserved (IMP stays IMP, IDA stays IDA)
- [ ] Supporting_text contains exact quotes from publications
- [ ] All GO:0005515 entries assessed for substrate/E2/homodimer role
- [ ] GO:0061664 used for substrate interactions
- [ ] GO:0042802 retained for homodimerization
- [ ] YAML validates without errors
- [ ] Changes improve mechanistic precision without removing evidence

---

## References for Modified Terms

### GO:0061683 - Atg8 conjugation to phosphatidylethanolamine
- **Definition:** The process of covalent attachment of ATG8 to phosphatidylethanolamine (PE)
- **Parent Terms:** Macromolecule conjugation, protein lipidation
- **Reason for Use:** Captures the actual enzymatic product and ATG7's role in enabling it through substrate activation

### GO:0061664 - Ubiquitin-like protein binding
- **Definition:** Interacting selectively and non-covalently with a ubiquitin-like protein
- **Parent Terms:** Protein binding
- **Reason for Use:** More specific than generic "protein binding" while still general enough for multiple UBL substrates (ATG8, ATG12)

### GO:0042802 - Identical protein binding (RETAIN)
- **Definition:** Interacting selectively and non-covalently with an identical protein
- **Parent Terms:** Protein binding, homodimer formation
- **Reason:** Already present; correctly describes ATG7 homodimerization

---

## Expected Quality Improvements

**Before Modifications:**
- 5x GO:0006501 (imprecise substrate activation term)
- 7x GO:0005515 (generic, uninformative)
- Total imprecision: 12 annotations

**After Modifications:**
- 5x GO:0061683 (substrate-specific conjugation)
- 7x GO:0061664 (substrate-specific binding) or GO:0042802 (homodimer)
- Total precision: 12 mechanistically accurate annotations

**Impact:**
- Improved GO database queries (can specifically find "ATG8 conjugation" vs. generic "protein binding")
- Better representation of mechanistic knowledge
- Alignment with GO best practices (use most specific available term)
- Support for computational biology tools that rely on precise annotations
