# GGP1 (At4g30530, Q9M0A7) review notes

## Summary of biology
- Cytosolic gamma-glutamyl peptidase (peptidase C26 / class-I GATase-like fold). Identified by reconstituting benzylglucosinolate production in N. benthamiana [PMID:19483696 "gamma-glutamyl peptidase 1 (GGP1), which substantially increased glucosinolate production by metabolizing an accumulating glutathione conjugate"].
- ggp1-1 ggp3-1 knockdown accumulates up to 10 glucosinolate-related GSH conjugates; recombinant GGP1/GGP3 process 9 of 10 plus GS-IAN; YFP fusions are cytosolic [PMID:21712415 "which showed that both protein fusions were cytosolic"].
- Camalexin: ggp1 has reduced camalexin and accumulates GS-IAN [PMID:23449503 "ggp1 mutants have reduced end-product (camalexin) levels and accumulate the expected intermediates"].
- GSH degradation (primary S metabolism): [PMID:35932489 "Recombinant proteins of GGP1, as well as GGP3, showed high degradation activity of GSH, but not of oxidized glutathione (GSSG), in vitro"]; ggp1 mutants accumulate more GSH. Km ~5 mM, matching cytosolic GSH.
- Crystal structure: Cys100 nucleophile, His192 catalytic base; covalent gamma-Glu intermediate trapped with H192N [PMID:41176694 "The intermediate structure, in which γ-Glu is covalently linked to the catalytic nucleophile cysteine (C100), was trapped by mutating the catalytic histidine to asparagine (H192N)."].

## Decisions
- peptidase activity (IDA, IEA) -> MODIFY to GO:0034722 (consistent across evidence codes).
- glucosinolate metabolic process (IDA, IMP, IEA) -> MODIFY to GO:0019761 glucosinolate biosynthetic process (GGP1 catalyses a biosynthetic step).
- Plasma membrane / secretory vesicle HDA -> MARK_AS_OVER_ANNOTATED (conflict with targeted cytosolic localization; HT datasets).
- Stress granule IDA -> KEEP_AS_NON_CORE.
- NEW GO:0006751 glutathione catabolic process (IDA, PMID:35932489). Participation: GGP1 itself hydrolyses GSH. Comparator check (QuickGO, taxon 3702, GO:0006751): GGCT2;1, GGCT2;2, GGCT2;3, GGT1, GGT2, GGT3, GGT4 and OXP1 all carry the term; GGP1 lacks it only because the 2022 paper is uncurated.
- Deep research file was not present at time of review.


## Module-member evidence audit — 2026-10-25

Reviewed every original row (15) and core function using review/annotation-reviewer instructions, current cached primary publications and the existing research. Preserved all source annotation fields and all pre-existing proposed rows. Reused the existing genuine Falcon provider report and its artifacts. These plant targets do not require bacterial FEBA retrieval.

Full PMID21712415 explicitly says it is unknown whether the SUR1 substrate is the Cys-Gly or further processed Cys conjugate. GGP1 directly generates Cys-Gly products, so description/core now qualify this handoff. The same paper supplies purified-enzyme activity on multiple GSH conjugates and camalexin GS-IAN. PMID35932489 and41176694 support genuine free-GSH hydrolysis; retained the pre-existing NEW GSH-catabolism proposal, removed speculation that its absence necessarily means the paper was not curated. Native processing order remains a chemistry gap.

Broad and substrate-specific terms were assessed consistently across evidence codes. No NEW rows were added. Previously proposed rows were evaluated for direct participation rather than filled from pathway adjacency. Experimental cohort calls whose protein-level data were not verified were left UNDECIDED; full-text availability alone was not treated as proof of a target-specific assay. Original sources and provider reports were not hand-edited.


## 2026-10-26 — PR #5550 source-level correction

Revisited review findings 1–3 against the actual publication cache and the primary sources. Removed generic source-unresolved boilerplate where the assay design is adjudicable. Restored relevant verbatim biochemical and localization evidence; did not restore label-only CHAIN features, unrelated introductory statements, or quotations that no longer support the revised claim. Existing source annotation fields were preserved.

Read PMID:28887381 full text, especially "Identification of True Membrane-associated Proteins" and Fig. 7: washed microsomes and sucrose gradients distinguish membrane association but do not separate organelles; named compartments are imported from SUBAcon/GFP knowledge. The paper states "no organelle fell in a single cluster". Mark the specific compartment claim as over-annotated while preserving proteomic detection. This applies projects/ORGANELLES.md at the actual resolution of the assay.
