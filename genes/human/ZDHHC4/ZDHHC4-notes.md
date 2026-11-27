# ZDHHC4 notes

## 2026-11-25 GO-CAM 65bc474400000029 review

The local `deep-research-falcon` recipe was attempted with a `perplexity-lite`
fallback, but neither `falcon` nor `perplexity` was available in this runtime.
These notes therefore summarize the cached publications and UniProt record used
for the manual review.

### Core biology

- ZDHHC4 is a multi-pass DHHC S-acyltransferase with ER, Golgi and plasma
  membrane pools. ER residence is constrained by a C-terminal KXX signal
  [PMID:21926431, "we have identified and characterized lysine-based sorting
  signals that determine the restricted localization of DHHC4 and DHHC6 to ER
  membranes"].
- ZDHHC4 catalyzes protein-cysteine S-palmitoylation on several substrates:
  DRD2 [PMID:26535572, "D2Rs in which C443 was deleted showed significantly
  reduced palmitoylation levels, plasma membrane expression, and protein
  stability"], CD36 [PMID:30605677, "DHHC4 and DHHC5 function at different
  subcellular localizations to control the palmitoylation, plasma membrane
  localization, and fatty acid uptake activity of the scavenger receptor CD36"],
  GSK3B in glioblastoma stem cells [PMID:35606353, "GSK3β can be
  palmitoylated by ZDHHC4"], and MAVS [PMID:38016475, "CPT1A recruits the
  endoplasmic reticulum-localized ZDHHC4 to catalyze MAVS
  Cys79-palmitoylation"].
- The two high-throughput HuRI `GO:0005515` rows from PMID:32296183 should be
  removed under the protein-binding policy. They record reported interactome
  edges, not an informative ZDHHC4 molecular function.

### GO-CAM consistency notes

- The 65bc GO-CAM models the ZDHHC4 activity as `GO:0016409
  palmitoyltransferase activity`; the gene review refines the ZDHHC4 rows to
  `GO:0019706 protein-cysteine S-palmitoyltransferase activity`, which matches
  the MAVS Cys79 reaction and the existing Rhea/EC mapping.
- The GO-CAM review already flagged the ZDHHC4-to-MAVS evidence as miscited to
  PMID:35606353. In GOA, the UniProt row for `GO:0045089 positive regulation of
  innate immune response` has the same issue: PMID:35606353 is the GSK3B paper;
  PMID:38016475 is the MAVS paper.
