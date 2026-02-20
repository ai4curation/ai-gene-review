# UNFOLDED_PROTEIN_BINDING Project - Curation Progress

**Last Updated**: 2026-02-21 (After analysis of 11 available publications)

## Summary

Comprehensive curation project for GO:0051082 "unfolded protein binding" annotations, including:
- Documentation updates for GO:0140309 February 20, 2026 official redefinition
- Automated conversion of retention entries → GO:0140309 recommendations  
- Systematic manual curation of unmatched annotations

## Progress Statistics

| Metric | Total | Filled | % |
|--------|-------|--------|-----|
| **Annotations** | 266 | 207 | 77.8% |
| **Remaining** | — | 59 | 22.2% |

### Session Breakdown

**Phase 1 - Documentation Updates** ✅ COMPLETED
- Updated UNFOLDED_PROTEIN_BINDING.md with Feb 20, 2026 official GO:0140309 date
- Fixed spreadsheet label: "unfolded protein carrier activity" → "unfolded protein holdase activity"
- Converted 18+ retention entries to GO:0140309 recommendations

**Phase 2 - Available Publication Analysis** ✅ COMPLETED
- Analyzed 11 PMIDs with cached publication files
- Generated detailed analysis in UNREVIEWED_ANNOTATIONS_ANALYSIS.md
- Applied 10 total recommendations to spreadsheet:

| #  | Gene | PMID | Action | Status |
|----|------|------|--------|--------|
| 1  | AIPL1 | 10615133 | DELETE | ✅ Applied |
| 2  | cct_yeast | 16762366 | GO:0044183 | ✅ Applied |
| 3  | HSPA5 | 14685163 | GO:0044183 | ✅ Applied |
| 4  | HSPA1A | 16130169 | GO:0044183 | ✅ Applied |
| 5  | lsc_yeast | 16873065 | GO:0140309 | ✅ Applied |
| 6  | HSPA5 | 22013210 | GO:0044183 | ✅ Applied |
| 7  | btt1-egd2_yeast | 26618777 | GO:0044183 | ✅ Applied |
| 8  | gimc_yeast | 9463374 | GO:0044183 | ✅ Applied |
| 9  | SSB2 | 9670014 | GO:0044183 | ✅ Applied |
| 10 | rac_yeast | 11274393 | GO:0044183 | ✅ Applied |
| 11 | Hsp90aa1 | 12855682 | MODIFY (co-chaperone) | ✅ Applied |

**Phase 3 - Pending Publication Analysis**  
- 59 annotations still require GO term recommendations
- 50 publications not yet retrieved (estimated 30-40 distinct PMIDs after deduplication)
- Approximately 20-30 additional annotations can be handled through targeted fetch

## Publication Analysis Status

### Available & Analyzed (11 PMIDs)
✅ 10615133 - AIPL1 (false annotation)  
✅ 14685163 - HSPA5 (ER chaperone)  
✅ 16130169 - HSPA1A (proteomics study)  
✅ 16762366 - CCT yeast (ATP-dependent foldase)  
✅ 16873065 - Kar2p ERAD (ER surveillance)  
✅ 22013210 - HSPA5 UPR (ER stress response)  
✅ 26618777 - NAC complex (cotranslational folding)  
✅ 9463374 - GIM proteins (tubulin folding)  
✅ 9670014 - SSB2 (nascent chain binding)  
✅ 11274393 - RAC complex (ribosome-tethered)  
✅ 12855682 - Hsp90aa1 (iNOS enhancer)

### Not Yet Fetched (≈50 PMIDs)
- Requires `just fetch-gene` or related publication fetch commands
- Estimated effort: 30-60 minutes for sequential fetching + analysis
- High yield: Should address remaining 59 unmatched annotations

## Recommendations by GO Term Type

### GO:0044183 "protein folding chaperone"
Applied to: cct_yeast, HSPA5 (×2), HSPA1A, gimc_yeast, SSB2, rac_yeast
- ATP-dependent folding assistance
- Direct client protein hydrophobic binding
- Nascent chain or misfolded protein substrate

### GO:0140309 "unfolded protein holdase activity"
Applied to: lsc_yeast (Kar2p)
- ATP-independent protein stabilization
- Prevents aggregation of misfolded proteins
- ER luminal surveillance function

### DELETE
Applied to: AIPL1
- False annotation (signal transduction protein, not chaperone)

### MODIFY (requires expert review)
Applied to: Hsp90aa1
- Co-chaperone regulatory enhancer role
- Allosteric client protein modulator
- May need specialized HSP90 activity term

## Next Steps (In Priority Order)

### Immediate (Can Execute Now)
1. ✅ **DONE**: Analyze 11 available publications
2. ✅ **DONE**: Apply 10 recommendations to spreadsheet
3. ✅ **DONE**: Commit changes to git

### Short Term (Recommended Next)
1. **Fetch remaining 50 publications** using project tools
2. **Analyze each retrieved publication** following established pattern
3. **Apply recommendations batch** to spreadsheet via updated_from_analysis.py
4. **Reach 95%+ completion target** (250+/266 annotations)

### Medium Term
1. Expert review of flagged entries (e.g., Hsp90aa1 "MODIFY")
2. Verification that recommended GO terms align with annotation guidelines
3. Final quality check against GO:0051082/GO:0031249 obsoletion deadline

### Documentation
- UNREVIEWED_ANNOTATIONS_ANALYSIS.md: Comprehensive analysis document (maintained live)
- CURATION_PROGRESS.md: This document (updated after each phase)
- update_from_analysis.py: Automated spreadsheet updater (ready for batch processing)

## Quality Metrics

- **Accuracy**: Based on publication text matching to protein function
- **Coverage**: 207/266 = 77.8% (target: 95%+ = 250+/266)
- **Completeness**: 11/61 unique PMIDs analyzed (likely 30-40 more retrievable)
- **Consistency**: All recommendations include supporting publication evidence

## Key Insights from Analysis

1. **Foldase consensus**: Most annotations correctly reference protein folding chaperones
   - GO:0044183 appropriate for ATP-dependent foldases
   - GO:0140309 appropriate for ATP-independent holdases

2. **False positives identified**: AIPL1 annotation unfounded (protein kinase, not chaperone)

3. **ER-specific variants**: HSPA5, HSPA1A, lsc_yeast all have ER-specific folding roles

4. **Ribosome-tethered complexes**: RAC, NAC, SSB shared cotranslational folding function

5. **Co-chaperone roles**: Hsp90 and other co-factors require careful distinction from direct foldases

## Technical Notes

- Spreadsheet format: TSV with bioentity_label, reference, and Suggested action columns
- Missing genes: HSPA1A had entry matched; SSB2 successfully updated
- Yeast gene nomenclature: Uses lowercase with underscores (e.g., rac_yeast)
- Publication caching: 11 PMIDs cached in publications/ folder; 50 pending

## Related Documentation

- [UNFOLDED_PROTEIN_BINDING.md](UNFOLDED_PROTEIN_BINDING.md) - Project overview and GO:0140309 details
- [UNREVIEWED_ANNOTATIONS_ANALYSIS.md](UNREVIEWED_ANNOTATIONS_ANALYSIS.md) - Detailed analysis of all 11 publications
- [update_from_analysis.py](update_from_analysis.py) - Automated spreadsheet updater script
