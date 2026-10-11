# ANKRD12 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKRD12 (Q6UB98, ANCO-2) is the paralog of ANKRD11 (ANCO-1). A functional paper (PMID:18377363, abstract-only; see round 2 for PMID:15184363) maps the ADA3 interaction and P/CAF nuclear-dot co-localization for ANCO-1. ANCO-2 appears only in a transient reporter assay, where it represses ADA3 co-activation. Affinage attributes the ANCO-1 data to ANKRD12; corrected in its reference_review.
- **GOA rows:** nucleus (SubCell IEA), nucleoplasm (IBA) and nucleoplasm (HPA IDA), all accepted.
  - The IBA node PTN004675685 (Euarchontoglires) is seeded by ANKRD12's own HPA IDA and ANKRD11; the self-donor is expected, not circular. source_entities recorded.
- **No NEW corepressor term:** the evidence for ANCO-2 is one reporter assay, and ANKRD11 itself has no MF annotations to compare with.
- **PAINT:** PTHR24149 has 1 annotated node. Family files committed.
- **Knowledge gap:** MF_DARK.

## 2026-10-04 round 2 (reviewer comments on #4083)

- **Missed paper:** PMID:15184363 (Zhang 2004, ANCO family). UniProt credits it with ANKRD12's nuclear location and p160 PAS-region binding on this accession (ECO:0000269), so its full text covers ANCO-2. It is now cited, with the UniProt SUBCELLULAR, SUBUNIT and FUNCTION lines.
- **Location rows** now cite the UniProt experimental nucleus line rather than a compartment-free quote.
- **Over-correction fixed:** the ADA3 interaction is reported for both ANCO-1 and ANCO-2 (PMID:18377363). Only the domain mapping and P/CAF co-localization are ANCO-1-specific. The affinage reference_review is restored to VERIFIED with that scoping.
- **Still no NEW coregulator term.** The repo's ANKRD11 review proposes GO:0003712, but that rests on ANKRD11 shRNA and knockdown data. ANKRD12 has only interaction and overexpression-reporter data, so it stays MF_DARK; the argument is in the knowledge-gap boundary.
- The IBA source_entities now include ANKRD12's own self-donor (Q6UB98).
