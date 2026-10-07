# ATG9B notes

## 2026-10-05 review (PAINT, affinage)

- Affinage refused to write because of a symbol-collision gate on "yeast". I checked it: a false positive, since the narrative calls ATG9B a functional ortholog of yeast Atg9p and is about human ATG9B. Written with `--force`.
- PMID:37938170 was a metadata stub in the cache. Re-fetched with full text, which I checked for content ("scramblase" 29 times; Results present).
- Key evidence [PMID:37938170 "We show that ATG9B can compensate for the absence of ATG9A in starvation-induced autophagy displaying similar subcellular trafficking and steady-state localization."]; [PMID:37938170 "Like ATG9A, ATG9B was mainly co-localized with the Golgi marker GOLGA2/GM130, to a lesser extent with early endosomes, positive for EEA1, and recycling endosomes labeled using RAB11 (Figure 6A)."].
- These calls follow the merged ATG9A review: obsolete PAS membrane → MODIFY to phagophore; piecemeal microautophagy and plasma membrane scrambling → over-annotated; mitophagy and reticulophagy → non-core.
- Bone morphogenesis and programmed necrotic cell death are ISS from mouse Atg9a (Q68FE2), a paralog phenotype, and are over-annotated (they are also over-annotated on ATG9A itself).
- Not used: the many uncached cancer, miRNA and infection papers; the 2026 mitochondrial ATG9B paper (PMID:41811769); and the 2024 neurodevelopmental-variant report.

## 2026-10-05 revision (reviewer round 1)

- Correction: Q68FE2 is **mouse** Atg9a (UniProt ATG9A_MOUSE), not rat. I had written "rat" in the review, the notes, the history record and the PR body; it is fixed here, in the review and in the PR body, and the history EDIT records the correction.
- Added propagation_review to all seven ISS rows. The Q68FE2-derived bone morphogenesis and necrosis rows carry failure_modes WRONG_ORTHOLOG_OR_PARALOG and CONTEXT_OR_TISSUE_MISMATCH; piecemeal microautophagy carries LINEAGE_OR_TAXON_MISMATCH.
- Added phagophore (GO:0061908) to the core_functions locations. The autophagosome assembly IDA row has qualifier acts_upstream_of_or_within, while core_functions uses directly_involved_in on the strength of the ATG9A-replacement and scramblase data.
- The ATG9A review's phagophore-membrane NTR is not duplicated here. The autophagy-independent CRC invasion role (PMID:34131310) is uncached and not used.
