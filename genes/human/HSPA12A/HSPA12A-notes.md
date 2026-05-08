# HSPA12A Notes

## Proteostasis framing

- User-supplied PN context places HSPA12A under `Cytonuclear proteostasis > Chaperone > HSP70 system > HSP70`, but the accompanying PN project note treats HSPA12A/HSPA12B as family/domain-based inclusions whose true proteostasis functions are not yet known.
- Conservative implication for GO review: PN membership alone is not enough to assert ATP-dependent protein folding chaperone activity or another core proteostasis term for HSPA12A.

## Direct evidence that stands up best

- UniProt's curated function is specific and narrow: HSPA12A is an adapter protein for SORL1/SorLA rather than a general chaperone [file:human/HSPA12A/HSPA12A-uniprot.txt, "Adapter protein for SORL1, but not SORT1. Delays SORL1 internalization and affects SORL1 subcellular localization."]
- The strongest direct mechanistic paper likewise identifies a SorLA-specific interaction and does not demonstrate canonical HSP70 folding activity [PMID:30679749 "We have identified HSPA12A as a new adaptor protein that, among Vps10p-D receptors, selectively binds to SorLA in an ADP/ATP dependent manner."]
- The same paper explicitly notes that the HSPA12 proteins are atypical HSP70-family members with divergent nucleotide-binding domains and uncharacterized nucleotide-binding properties [PMID:30679749 "the two HSPA12 genes encoding divergent NBDs with uncharacterised nucleotide binding properties"]
- The direct cell-biology evidence in that paper is cytoplasmic rather than a broad proteostasis narrative [PMID:30679749 "Co-localisation of SorLA and HSPA12A is here only demonstrated to take place in cytoplasm."]

## Curation take

- Current GOA protein-binding annotations from large interactome resources are not useful as core function statements. They mostly recover generic `protein binding` and, for the high-throughput records here, mainly point to HSPA12B as the interactor rather than defining a specific HSPA12A mechanism.
- Broad nucleus/cytoplasm localizations are plausible context but not core biology.
- The urinary exosome proteomics hit is worth retaining only as non-core context; it does not establish exosome function as central to HSPA12A.
- At present, the literature supports HSPA12A as a poorly characterized intracellular adaptor/scaffold-like protein with one reasonably specific SorLA trafficking connection, not as a confirmed canonical HSP70 proteostasis factor.
