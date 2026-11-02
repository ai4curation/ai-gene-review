# pfd-1 (C08F8.1, UniProt Q17827) notes

## Deep research status
`just deep-research-falcon worm pfd-1 --fallback perplexity-lite` was run on 2026-10-08. The client reported a timeout, and the perplexity fallback is not available in this environment, but Falcon later wrote `pfd-1-deep-research-falcon.md`. Its claims drawn from Lundin's 2008 thesis are not verified against primary text. Primary claims in the review are based on cached publications (PMID:9630229, PMID:18062952 [abstract only], PMID:21611156, PMID:20554764, PMID:30478249) and UniProt. A PubMed search for "prefoldin AND elegans" returned PMID:18062952, PMID:20554764, PMID:30478249 and PMID:16436622 (URI-1).

## Summary
- beta-class prefoldin subunit, ortholog of human PFDN1. Prefoldin is a heterohexamer of two alpha and four beta subunits [file:worm/pfd-1/pfd-1-uniprot.txt "Heterohexamer of two PFD-alpha type and four PFD-beta type subunits."].
- Prefoldin captures unfolded actin and tubulin and passes them to cytosolic chaperonin [PMID:9630229 "Prefoldin binds specifically to cytosolic chaperonin (c-cpn) and transfers target proteins to it."].
- C. elegans: prefoldin RNAi causes embryonic lethality through lower alpha-tubulin levels and slower microtubule growth [PMID:18062952 "Our analyses suggest that these defects result mainly from a decrease in alpha-tubulin levels and a subsequent reduction in the microtubule growth rate."]. PMID:18062952 is abstract-only in the cache, so its IDA/IMP rows defer to the curator.
- C. elegans prefoldin = PFD-1..PFD-6 [PMID:30478249 "The prefoldin complex is composed of PFD-1 through PFD-6 and acts as a chaperone for the proper folding of many essential proteins, including actins and tubulins"].
- pfd-1 mutants with maternal PFD-1 reach L4 with gonadogenesis defects including aberrant distal tip cell migration [PMID:18062952 "Prefoldin subunit 1 (pfd-1) mutant animals with maternally contributed PFD-1 develop to the L4 larval stage with gonadogenesis defects that include aberrant distal tip cell migration."]. The gonad development IMP is kept as non-core (indirect, via tubulin).
- Body-wall muscle GFP screen: C08F8.1 in category 13 'Other Cytoplasmic or Cytosol' [PMID:21611156 "13: B0001.6, C04F12.3, C08F8.1, C49H3.6"].

## Core function
GO:0044183 protein folding chaperone, in GO:0016272 prefoldin complex, cytoplasm; BP GO:0006457 protein folding.
