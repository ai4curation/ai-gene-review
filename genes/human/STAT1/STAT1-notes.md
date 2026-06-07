# STAT1 Gene Review Notes

## 2025-01-14 - Retired Annotation Fix

**Issue**: Validation failure due to 1 annotation not found in the current GOA file.

**Root Cause**: PMID:16257975 that was referenced in one annotation (GO:0046427 - positive regulation of receptor signaling pathway via JAK-STAT) has been removed from the current GOA database.

**Action Taken**: Marked the annotation with PMID:16257975 as `retired: true` to exclude it from GOA validation while preserving the annotation review work.

**Validation Status**: After marking the retired annotation, the gene now passes validation with only warnings about PENDING annotations and an invalid PMID:34521819 that couldn't be fetched.

**Outstanding Issues**:
- PMID:34521819 cannot be verified - may need manual checking or correction
- Large number of PENDING annotations require review

**Note**: STAT1 is a key transcription factor in the JAK-STAT signaling pathway, particularly important for interferon signaling and immune responses. The single retired annotation represents ongoing curation changes in the GOA database.

## 2026-05-29 - PROTEOSTASIS PN autophagy-gene-expression pass

The PN workbook places STAT1 under `Autophagy-Lysosome Pathway > Autophagy gene expression > Transcriptional repressor` with the note that STAT1 binds a regulatory sequence in the ULK1 5' flanking region; mutating that sequence increased ULK1 promoter activity and made the promoter unresponsive to mTOR inhibition.

The underlying paper supports a real, context-specific STAT1 role in suppressing ULK1 expression and autophagic activity, but it should not be promoted to a generic core STAT1 proteostasis function. It also does not cleanly support group-level propagation to `GO:0003714 transcription corepressor activity` for STAT1, because STAT1 is a DNA-binding transcription factor and the evidence is specific to ULK1/autophagy regulation rather than generic corepressor activity. [PMID:28011640 "STAT1-deficient human fibrosarcoma cells exhibited enhanced autophagic flux"; PMID:28011640 "STAT1 bound a putative regulatory sequence in the ULK1 5'-flanking region"; PMID:28011640 "These results demonstrate a novel mechanism by which STAT1 negatively regulates ULK1 expression and autophagy."]

Working curation conclusion: keep the PN placement as useful context for evaluating autophagy-gene-expression biology, but do not automatically propagate `GO:0003714` from the PN group to STAT1. A gene-level annotation, if pursued, should capture the specific ULK1/autophagy repression evidence rather than a broad corepressor claim.
