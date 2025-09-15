# TRAF6 Gene Review Notes

## 2025-01-14 - Retired Annotation Fix

**Issue**: Validation failure due to 33 annotations not found in the current GOA file.

**Root Cause**: Multiple PMIDs that were referenced in the original annotations have been removed from the current GOA database. These include:
- PMID:1406630 (canonical NF-kappaB signal transduction)
- PMID:11460167 (defense response to bacterium, positive regulation of NF-kappaB)
- PMID:25038658 (negative regulation of NF-kappaB)
- PMID:27746020 (protein K48-linked ubiquitination)
- PMID:7479976 (toll-like receptor 4 signaling pathway)
- PMID:21931555 (cytoplasmic pattern recognition receptor signaling)
- PMID:20532808 (interleukin-33-mediated signaling pathway)
- PMID:31376257 (interleukin-17A-mediated signaling pathway)
- PMID:23202584 (autophagosome assembly)

**Action Taken**: Marked annotations with these missing PMIDs as `retired: true` to exclude them from GOA validation while preserving the annotation review work.

**Validation Status**: Reduced the number of missing annotations from 33 to approximately 27, though some complex annotations with multiple evidence types may still need individual attention.

**Outstanding Issues**:
- Some inconsistent review actions across evidence types for the same GO terms
- Evidence type mismatches with current GOA
- Additional retired annotations may need identification

**Note**: TRAF6 is a heavily studied immune signaling protein with extensive experimental literature, which explains the large number of annotations and the ongoing changes in the GOA database as curation standards evolve.