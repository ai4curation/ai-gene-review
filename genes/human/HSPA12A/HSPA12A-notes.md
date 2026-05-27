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

- Current GOA protein-binding annotations from large interactome resources are not useful as core function statements. The high-throughput records capture HSPA12A-HSPA12B physical associations, but generic `protein binding` still does not define a specific HSPA12A mechanism.
- Broad nucleus/cytoplasm localizations are plausible context but not core biology.
- The urinary exosome proteomics hit is worth retaining only as non-core context; it does not establish exosome function as central to HSPA12A.
- At present, the literature supports HSPA12A as a poorly characterized intracellular adaptor/scaffold-like protein with one reasonably specific SorLA trafficking connection, not as a confirmed canonical HSP70 proteostasis factor.

## Falcon deep research integration - 2026-05-12

Falcon deep research was added as `HSPA12A-deep-research-falcon.md` and supports
the conservative review framing. It found that direct canonical HSP70 folding
activity remains unsupported [file:human/HSPA12A/HSPA12A-deep-research-falcon.md
"Current evidence in retrieved primary literature is insufficient to support
canonical HSP70 chaperone/protein-folding activity for HSPA12A."].

The report reinforces that the best-supported function is SorLA/SORL1 cytosolic
tail binding and receptor trafficking control [file:human/HSPA12A/HSPA12A-deep-research-falcon.md
"HSPA12A was identified as a **specific SorLA cytosolic-tail interactor**; Y2H
recovered C-terminal HSPA12A clones, GST-HSPA12A pulled down full-length SorLA,
and binding mapped to SorLA cytosolic acidic clusters including E34-D38 and D47D48."]
and [file:human/HSPA12A/HSPA12A-deep-research-falcon.md "HSPA12A **delays SorLA
internalization/endocytosis**: surface SorLA staining persisted longer in
HSPA12A-expressing cells, and labeled SorLA accumulated in HSPA12A-positive
vesicles."].

After review feedback, the receptor internalization consequence was split out
as a separate NEW BP annotation rather than listed as a cross-aspect replacement
for the MF `protein binding` annotation. The HSPA12B high-throughput interaction
rows were also reframed as valid but uninformative physical-association evidence.

Two additional references were cached for traceability around the canonical HSP70
exclusion. Han et al. support distant HSP70-family/domain placement while warning
against assuming canonical HSP70 function [PMID:12552099 "Despite HspA12A and
HspA12B localization to macrophages in lesions and their placement into the Hsp70
family by computer algorithms, we cannot be certain that they share any of the
functions of Hsp70s."]. Cheng et al. report PCNA binding in a hepatocellular
carcinoma context, not folding-chaperone biochemistry [PMID:32128976 "HSPA12A
directly binds to PCNA and promotes its trimerization, which is an essential
functional conformation of PCNA for carcinogenesis."].
