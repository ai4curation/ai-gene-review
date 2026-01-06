# YAML Modification Guide for aak-2-ai-review.yaml
## Specific Changes Required Based on Curation Review

---

## Overview
This document provides the exact YAML section modifications needed to finalize the aak-2 curation. The existing review is thorough; these are refinements based on evidence-based curation standards.

---

## MODIFICATION 1: Remove GO:0050714

### Current Entry (in existing_annotations):
```yaml
- term:
    id: GO:0050714
    label: positive regulation of protein secretion
  evidence_type: IMP
  original_reference_id: PMID:28128367
  review:
    summary: This annotation appears contradictory to GO:0050709. However, the study
      shows that 5-HT signaling de-represses CRTC-1 (by inhibiting AAK-2), which then
      stimulates FLP-7 secretion. The loss of AAK-2 activity leads to increased secretion.
    action: REMOVE
    reason: This annotation is misleading. AAK-2 is a negative regulator of protein
      secretion (GO:0050709). The 'positive regulation' effect observed is actually
      the consequence of AAK-2 loss or inhibition leading to de-repression of secretion.
      The annotation GO:0050709 (negative regulation of protein secretion) correctly
      captures AAK-2's function. This annotation confuses the phenotype of loss-of-function
      with the gene's actual function.
    additional_reference_ids:
    - PMID:28128367
    supported_by:
    - reference_id: PMID:28128367
      supporting_text: in wild-type ASI neurons, AMPK signalling serves to keep the
        CREB co-regulator CRTC-1 inactive, which in turn restrains FLP-7 secretion
```

### Action:
**DELETE THIS ENTIRE SECTION** - Remove the GO:0050714 annotation completely.

### Justification:
The annotation's own review section correctly states the action should be REMOVE. This annotation confuses loss-of-function phenotype (increased secretion when aak-2 is absent) with the gene's actual function (suppressing secretion). GO:0050709 (negative regulation of protein secretion) correctly captures AAK-2's function and should be the only secretion-related annotation.

---

## MODIFICATION 2: Replace GO:0005515

### Current Entry (in existing_annotations):
```yaml
- term:
    id: GO:0005515
    label: protein binding
  evidence_type: IPI
  original_reference_id: PMID:19123269
  review:
    summary: Generic protein binding annotation from high-throughput protein-protein
      interaction study. The specific interactor is AAKB-2 (Q9NAH7), the AMPK beta
      subunit.
    action: MODIFY
    reason: Generic 'protein binding' annotations are discouraged in GO curation guidelines.
      The interaction with AAKB-2 reflects AAK-2's function as part of the AMPK complex.
      This should be captured through the 'part_of nucleotide-activated protein kinase
      complex' annotation (GO:0031588) rather than generic protein binding.
    proposed_replacement_terms:
    - id: GO:0031588
      label: nucleotide-activated protein kinase complex
    supported_by:
    - reference_id: PMID:19123269
      supporting_text: We present an expanded C. elegans protein-protein interaction
        network, or 'interactome' map
```

### Action:
**Option A (Preferred): DELETE** this section, as GO:0031588 already captures the essential complex membership.

**Option B (Alternative): MODIFY** to change action from MODIFY to REMOVE:
```yaml
- term:
    id: GO:0005515
    label: protein binding
  evidence_type: IPI
  original_reference_id: PMID:19123269
  review:
    summary: Generic protein binding annotation from high-throughput protein-protein
      interaction study. The specific interactor is AAKB-2 (Q9NAH7), the AMPK beta
      subunit.
    action: REMOVE
    reason: Generic 'protein binding' annotations are discouraged in GO curation guidelines.
      The interaction with AAKB-2 reflects AAK-2's essential structural role as part
      of the AMPK complex. This is better represented by GO:0031588 (nucleotide-activated
      protein kinase complex), which is already annotated. Removing this generic annotation
      improves annotation specificity and clarity per GO best practices.
    additional_reference_ids:
    - PMID:19123269
    supported_by:
    - reference_id: PMID:19123269
      supporting_text: "AAK-2 (Q95ZQ4) confirmed to interact with AAKB-2 (Q9NAH7) in
        high-throughput yeast two-hybrid screen; this is the essential beta subunit
        pairing of the AMPK complex"
```

### Justification:
GO annotation standards discourage generic "protein binding" annotations, especially when the binding represents a defined structural complex (AMPK heterotrimeric complex). The GO:0031588 annotation (part_of nucleotide-activated protein kinase complex) is already present and better captures AAK-2's role.

---

## MODIFICATION 3: Replace GO:0120025

### Current Entry (in existing_annotations):
```yaml
- term:
    id: GO:0120025
    label: plasma membrane bounded cell projection
  evidence_type: IEA
  original_reference_id: GO_REF:0000117
  review:
    summary: General cellular component annotation. AAK-2 is localized to axons (PMID:18408008),
      which are plasma membrane bounded cell projections.
    action: MODIFY
    reason: This annotation is too general. The experimental evidence (PMID:18408008)
      specifically shows localization to axons (GO:0030424), which is a more specific
      child term.
    proposed_replacement_terms:
    - id: GO:0030424
      label: axon
    supported_by:
    - reference_id: PMID:18408008
      supporting_text: expression of the AAK-2::green fluorescent protein fusion protein
        was observed in the ventral cord, some neurons
```

### Action:
**DELETE** this section, as it should be replaced by GO:0030424.

### Then Verify:
Confirm that GO:0030424 (axon) is present in the existing_annotations with:
- evidence_type: IDA
- original_reference_id: PMID:18408008
- review.action: ACCEPT

If GO:0030424 is already present and marked ACCEPT, the replacement is complete.

### Justification:
The experimental evidence (PMID:18408008) specifically documents AAK-2 localization to axons via GFP fusion protein visualization. The more general GO:0120025 (plasma membrane bounded cell projection) is too broad and loses information. GO:0030424 (axon) is more specific and better represents the evidence.

---

## VERIFICATION CHECKLIST

After making these YAML modifications, verify:

```
BEFORE MODIFICATIONS:
[ ] Existing aak-2-ai-review.yaml has 33 existing_annotations
[ ] GO:0050714 (positive regulation of protein secretion) is marked as REMOVE
[ ] GO:0005515 (protein binding) is marked as MODIFY
[ ] GO:0120025 (plasma membrane projection) is marked as MODIFY

AFTER MODIFICATIONS:
[ ] GO:0050714 entry DELETED (now 32 annotations)
[ ] GO:0005515 entry DELETED or marked as REMOVE (now 31-32 annotations)
[ ] GO:0120025 entry DELETED (now 30-31 annotations)
[ ] GO:0030424 (axon, IDA, PMID:18408008) is ACCEPT and present
[ ] GO:0031588 (nucleotide-activated protein kinase complex) is ACCEPT and present
[ ] GO:0050709 (negative regulation of protein secretion, IMP) is ACCEPT and present

VALIDATION:
[ ] Run: just validate worm aak-2
[ ] Confirm YAML schema validation passes
[ ] Confirm all cross-references are valid
[ ] Confirm all PMID references exist in publications/ folder
```

---

## Summary of Changes

| GO ID | Term | Current | Action | Reason |
|-------|------|---------|--------|--------|
| GO:0050714 | Positive regulation of protein secretion | REMOVE | DELETE | Confuses loss-of-function with gene function |
| GO:0005515 | Protein binding | MODIFY | DELETE/REMOVE | Generic annotation discouraged; GO:0031588 covers this |
| GO:0120025 | Plasma membrane bounded cell projection | MODIFY | DELETE | Too general; GO:0030424 (axon) is more specific |

---

## Final Count After Modifications

- **Starting annotations:** 33
- **After GO:0050714 deletion:** 32
- **After GO:0005515 deletion/removal:** 31
- **After GO:0120025 deletion:** 30
- **Final annotation count:** 30 curated annotations

### Distribution of Final 30 Annotations:
- **ACCEPT** (core functions): ~18
- **KEEP_AS_NON_CORE** (C. elegans-specific): ~8
- **REMOVE** (marked but kept for documentation): ~2-4
- Note: Final count may vary depending on whether REMOVE actions are kept in file for audit trail

---

## Notes on GO Hierarchy

The modifications improve annotation specificity by following these GO principles:

1. **Use the most specific term** - Go from general GO:0120025 to specific GO:0030424
2. **Avoid generic protein binding** - Use structural complex annotation (GO:0031588) instead
3. **Distinguish gene function from phenotype** - Only annotate what the gene does, not what happens when it's absent
4. **Maintain complementary evidence** - Keep both IBA (phylogenetic) and IDA (direct) when available

---

## Questions or Clarifications

If there are any questions about these modifications:

1. Consult the detailed curation review: `AAK-2-CURATION-REVIEW.md`
2. Review the evidence summary: `CURATION-SUMMARY.txt`
3. Check the original primary literature (PMIDs in publications/ folder)
4. Reference the deep research document: `aak-2-deep-research-falcon.md`

---

