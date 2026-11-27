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
## 2026-11-23 ORGANELLES endosome batch 1

- Two GO:0005768 rows: IEA from ARBA00028568 (a 115-condition-set ML rule for endosome, unvetted; checked via the UniProt REST API 2026-11-23) and Reactome TAS R-HSA-8983335 (a black-box IL15/IL15RA recycling event; JAK1 is included because the whole receptor complex was modelled).
- Line found and cached: [PMID:20028207 "Shortly after IFN stimulation, robustly ubiquitinated IFNAR1 and a small amount of IFNAR2 were found in this endosomal compartment, which also contained tyrosine-phosphorylated Tyk2 and Jak1."] Endogenous, IFN-stimulated Daudi cells, EEA1 immunoisolation (abstract only, no PMC).
- Both rows KEEP_AS_NON_CORE (unchanged): recruited, ligand-driven pool of a receptor-bound kinase. EEA1 is one line, so no GO:0005769 row. JAK family rule applied to JAK1-3: keep a JAK endosome row only where a readable source places that JAK itself in endosomes.
