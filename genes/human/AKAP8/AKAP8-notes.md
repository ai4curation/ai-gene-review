# AKAP8 notes

## Deep research

- 2026-11-25: `just deep-research-falcon human AKAP8 --fallback perplexity-lite` failed because the Falcon and Perplexity providers were unavailable in this checkout. No provider-named deep-research file was written. This review therefore used the seeded GOA rows, UniProt O43823, the cached primary publications, the PAINT/IBA support listing, and the GO-CAM 69b3372b00003343 source and review YAML.

## Functional synthesis

- AKAP8 encodes AKAP95, the nuclear A-kinase anchoring protein cloned in PMID:9473338. The founding paper showed RII-alpha binding by the C-terminal portion of human AKAP95, nuclear localization in interphase human fibroblasts, and cell-cycle-dependent co-immunoprecipitation of AKAP95 with RII-alpha from mitotic but not interphase HeLa cells.
- The best-supported conserved core is nuclear and mitotic. PMID:10601332 showed AKAP95 in the interphase nuclear matrix, redistribution to a mitotic chromatin fraction, recruitment of PKA RII-alpha to chromatin, and a PKA-independent requirement for AKAP95 in chromosome condensation. PMID:16980585 added the HDAC3 branch: AKAP95 and HA95 recruit HDAC3 to mitotic chromosomes and are required for deacetylation of histone H3 in mitosis.
- AKAP8 also has nuclear chromatin functions outside chromosome condensation. PMID:12740381 supports the direct MCM2 interaction and an MCM2-scaffolding role in DNA replication, PMID:23995757 supports association with MLL1/MLL2 histone methyltransferase complexes through DPY30/WDR5/ASH2L and enhancement of their H3K4 methyltransferase activity, and PMID:26683827 supports GC-rich DNA binding plus nucleolar localization on rDNA chromatin.
- The granulosa-cell activity in GO-CAM 69b3372b00003343 is biologically plausible as a contextual use of AKAP95: PMID:29397057 reports that AKAP8 knockdown or AKAP95 inhibition in KGN cells and primary human luteinised granulosa cells reduces nuclear PKA, FSH- or cAMP-induced CREB phosphorylation, FSH-induced CYP19A1 expression, and estrogen synthesis. This is not AKAP8's main conserved cell-biological role, so the ovarian follicle development row is kept as non-core.

## GO-CAM 69b3372b00003343 consistency notes

- The model places AKAP8 in the right part of the FSH to CYP19A1 chain: a nuclear anchoring/adaptor input upstream of PKA and CREB in granulosa cells, rather than a receptor-proximal FSHR output.
- The AKAP8 activity is typed `GO:0140777` protein-containing complex stabilizing activity. The cited paper supports nuclear PKA anchoring by AKAP95, not prevention of protein-complex dissociation, so `GO:0060090` molecular adaptor activity is a better model activity type.
- The model names PRKACA as the has_input molecule for the AKAP8 activity. AKAP95 biochemically binds the PKA regulatory subunit PRKAR2A/RII-alpha, while PRKACA is the catalytic subunit released from the anchored holoenzyme. This may be a modelling shortcut, but the direct input should be checked.
- The AKAP8 activity's `part_of` nesting repeats `GO:0001541` ovarian follicle development inside itself. The exported GOA row carries the same circular process extension, and the GO-CAM review already records this as a `CONFIRMED` duplicate assertion; the final GO-CAM consistency PR should not file a second request for the same model defect.
