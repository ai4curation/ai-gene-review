# GEOSL PutA manual review

## 2026-11-06

Reviewed all 9 pristine rows, preserving every non-review payload and original ordering. Default Falcon was genuinely attempted and failed 403; no provider report was fabricated. Both catalytic activities and channeling were assessed from primary studies, not inferred from a single gene label. No NEW annotation rows are needed.

Q746X3 is explicitly named in PMID34506758 as 1004-residue PCA PutA. Frozen taxonomy is Thermodesulfobacteriota. Recombinant wild type is distinguished from A206W, whose coupled defect includes impaired PRODH flavin reduction. The membrane-side assignment is a structural/functional inference, not direct native localization.

- GO:0003700 (IEA): REMOVE. This bifunctional architecture does not support the mapped transcriptional-repressor role.
- GO:0003842 (IBA): ACCEPT. The GSALDH active site oxidizes glutamate semialdehyde with NAD+.
- GO:0003842 (IEA): ACCEPT. The GSALDH active site oxidizes glutamate semialdehyde with NAD+.
- GO:0004657 (IEA): ACCEPT. The PRODH active site catalyzes quinone-linked proline oxidation.
- GO:0006355 (IEA): REMOVE. This bifunctional architecture does not support the mapped transcriptional-repressor role.
- GO:0006562 (IBA): ACCEPT. PutA directly performs the two oxidation steps of L-proline catabolism.
- GO:0006562 (IEA): ACCEPT. PutA directly performs the two oxidation steps of L-proline catabolism.
- GO:0009898 (IBA): ACCEPT. The cytoplasmic membrane face is supported as the peripheral catalytic location.
- GO:0016491 (IEA): MODIFY. The broad oxidoreductase annotation resolves into the two measured PutA activities.

Model quinone assays support the generic GO4657 reaction but not a named endogenous respiratory partner. P5C hydrolysis and GSAL oxidation are distinct steps; no separate hydration MF is invented. The broad IPR025703 transcription mapping overreaches the solved type A/B architecture. No PutP partner, native proline-growth phenotype, or universal oligomeric assembly is asserted. PAINT lineage checks were run; the Corynebacterium entry is absent from the cached tree, while Geobacter has no detected lineage loss.
