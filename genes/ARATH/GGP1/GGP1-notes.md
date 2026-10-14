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
