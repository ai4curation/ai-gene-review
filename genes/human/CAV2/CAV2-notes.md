# CAV2 notes

## Manual review notes

Automated deep research was attempted with `just deep-research-falcon human CAV2 --fallback perplexity-lite` on 2026-11-26. Falcon was not available locally and the fallback Perplexity provider was also unavailable, so no provider-authored `CAV2-deep-research-*.md` file was created.

The manual review used the seeded human UniProt and GOA records, the PTHR10844 PAINT export, the existing human CAV1 and CAV3 reviews, and the cached CAV2 publications. `CAV2-goa.tsv` has the header plus 77 annotation rows; the completed `existing_annotations` list preserves one entry per GOA row, including the two PMID:31980649 protein-binding rows that differ only by partner.

## Functional synthesis

CAV2 is the CAV1-associated caveolin paralog. The core claim kept in this review is that CAV2 is an accessory molecular adaptor and hetero-oligomeric caveolin partner that supports CAV1-dependent targeting and caveola assembly. The CAV2 discovery and tissue studies placed the protein with CAV1 in caveolae and stable hetero-oligomeric complexes [PMID:8552590; PMID:9361015]. The CAV2 phosphorylation study in caveolin-deficient LNCaP cells showed that CAV2 positively regulates CAV1-dependent caveola formation and that the Ser23/Ser36 phosphostate changes the balance between subplasmalemmal smooth vesicles and plasma-membrane-attached caveolae [PMID:12743374]. HeLa caveolar coat purification recovered CAV2 with CAV1 and cavins in the coat complex [PMID:24013648].

CAV2 has context-specific signaling pools that are kept as non-core rather than promoted into the core function. Tyr19-phosphorylated CAV2 is a focal-adhesion-proximal, SH2-protein-associated pool [PMID:12091389]. CAV2 can support insulin-specific ERK activation and phospho-ERK targeting to the nuclear envelope in HEK293T cells [PMID:20455999]. CAV2 cofractionates and coimmunoprecipitates with D1 dopamine receptors and influences fenoldopam-stimulated cAMP in HEK293 or renal proximal tubule cell experiments [PMID:15569306]. RSV matrix protein binds CAV2, colocalizes with CAV1/CAV2 at viral filaments, and CAV2 knockdown reduces infectious RSV production [PMID:25556234]; those viral rows are kept as host-exploitation contexts.

The broad PAINT root terms need branch care. `GO:0005901` caveola and `GO:0070836` caveola assembly are coherent across human CAV1, CAV2 and CAV3. `GO:0042383` sarcolemma and `GO:0051480` regulation of cytosolic calcium ion concentration are less clear for human CAV2: the sarcolemma node is a mixed caveolin ancestral call and the calcium row is CAV1-seeded. The CAV2 review therefore leaves sarcolemma unresolved and marks the calcium row over-annotated rather than requesting a precise PAINT edit without a narrower branch audit.

## Module and GO-CAM fit

No CAV2-specific GO-CAM is listed in `gocams/index.tsv`. The only indexed human caveolin activity is a CAV1 event in GO-CAM `645d887900001414`, so no GO-CAM review was added in this focused CAV2 PR.

No module review was added. The caveolar coat is a real CAV1/CAV2/cavin assembly, but PTHR10844 itself supplies one caveolin role with CAV3 as a tissue-specialized alternative; a defensible caveola-coat module needs a broader CAVIN-family pass and should be done as a separate multi-family module review rather than as a one-gene CAV2 tail.
