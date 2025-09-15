# Ctnnb1 Gene Review Notes

## 2025-01-14 - Major GOA Expansion Issue

**Issue**: Validation failure due to massive mismatch between review and current GOA file:
- 553 missing annotations from GOA
- 24 annotations not in GOA
- 190 new references needed

**Root Cause**: The Ctnnb1 GOA file has expanded dramatically from ~206 annotations to 816 lines since the original review. This represents one of the most significant updates in the dataset.

**Action Taken**: Used the GOA validator to seed all 553 missing annotations, which added 190 new references. However, this created a massive file (8099 lines) that may need manual curation.

**Outstanding Issues**:
1. Some annotations like GO:0019221 (cytokine-mediated signaling pathway) with PMID:19619491 appear to have been retired from GOA
2. The file now contains a mix of carefully reviewed annotations and newly seeded PENDING annotations
3. The validation is timing out due to the file size

**Recommendation**: This gene requires special attention in a future curation cycle to:
1. Review the 553 newly seeded annotations
2. Identify and mark retired annotations
3. Resolve evidence type mismatches
4. Streamline the review for better maintainability

**Note**: Beta-catenin is a highly studied protein involved in multiple pathways (Wnt signaling, cell adhesion, transcriptional regulation), which explains the extensive annotation expansion.