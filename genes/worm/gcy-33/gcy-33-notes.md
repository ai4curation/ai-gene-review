# gcy-33 (P90895) curation notes

Deep research: falcon and perplexity-lite both failed (exit 137) on 2026-10-08; no deep-research
file. Review is based on cached publications.

## Key findings
- Required with gcy-31 in BAG for O2-downshift responses [PMID:19323996 "BAG sensory neurons are activated by decreases in O2 levels, and require the sGCs gcy-31 and gcy-33."]
- Also expressed in URX/AQR/PQR [PMID:19323996 "an extended gcy-33::GFP reporter gene fusion was expressed in BAG, URX, AQR and PQR neurons"]
- H-NOX binds O2, NO, CO; rat beta1 chimera weakly activated [PMID:21491957 "Additionally, it was determined that Gcy-33 binds oxygen, in addition to NO and CO"]
- PDL-1-dependent dendritic-ending localization, colocalizes with GLB-5 [PMID:25505325]
- Quinine hypersensitivity of gcy-33 mutants, non-cell-autonomous, upstream of EGL-4 [PMID:23874221]

## Decisions
- CO sensor activity (IDA, chimera): MARK_AS_OVER_ANNOTATED.
- NO-cGMP-mediated signaling IBA: REMOVE (no NOS in worm).
- Quinine/chemosensory behavior: KEEP_AS_NON_CORE.
- NEW: detection of oxygen (GO:0003032; comparator GLB-5) and dendrite (IDA, PMID:25505325).
