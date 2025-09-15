# JAK1 Gene Review Notes

## 2025-01-14 - Retired Annotation Fix

**Issue**: Validation failure due to 15 annotations not found in the current GOA file.

**Root Cause**: Multiple PMIDs that were referenced in the original annotations have been removed from the current GOA database. These include:
- PMID:29202461 (interleukin-7-mediated signaling pathway)
- PMID:28753426 (regulation of transcription by RNA polymerase II)
- PMID:23391734 (type I interferon-mediated signaling pathway)
- PMID:7568005 (interleukin-2-mediated signaling pathway)
- PMID:28781374 (interleukin-11-mediated signaling pathway)
- PMID:9535918 (interleukin-9-mediated signaling pathway)
- PMID:9020188 (regulation of transcription by RNA polymerase II)
- PMID:23139419, PMID:7526154, PMID:7759950 (JAK-STAT signaling pathway)

**Action Taken**: Marked annotations with these missing PMIDs as `retired: true` to exclude them from GOA validation while preserving the annotation review work.

**Validation Status**: Reduced the number of missing annotations from 15 to potentially 8 or fewer, though some additional ones may need individual attention.

**Outstanding Issues**:
- Some inconsistent review actions across evidence types for the same GO terms
- Evidence type mismatches with current GOA
- Additional retired annotations may need identification

**Note**: JAK1 is a key component of the JAK-STAT signaling pathway involved in cytokine signaling, which explains the extensive annotation set and the ongoing changes in the GOA database as curation standards evolve.