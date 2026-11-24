# pfd-2 (H20J04.5, UniProt Q9N5M2) notes

## Deep research status
`just deep-research-falcon worm pfd-2 --fallback perplexity-lite` was run on 2026-10-08. The client reported a timeout, and the perplexity fallback is not available in this environment, but Falcon later wrote `pfd-2-deep-research-falcon.md`. Its claims drawn from Lundin's 2008 thesis are not verified against primary text. Primary claims in the review are based on cached publications (PMID:9630229, PMID:18062952 [abstract only], PMID:21611156, PMID:20554764, PMID:30478249) and UniProt. A PubMed search for "prefoldin AND elegans" returned PMID:18062952, PMID:20554764, PMID:30478249 and PMID:16436622 (URI-1).

## Summary
- beta-class prefoldin subunit, ortholog of human PFDN2. Prefoldin is a heterohexamer of two alpha and four beta subunits [file:worm/pfd-2/pfd-2-uniprot.txt "Heterohexamer of two PFD-alpha type and four PFD-beta type subunits."].
- Prefoldin captures unfolded actin and tubulin and passes them to cytosolic chaperonin [PMID:9630229 "Prefoldin binds specifically to cytosolic chaperonin (c-cpn) and transfers target proteins to it."].
- C. elegans: prefoldin RNAi causes embryonic lethality through lower alpha-tubulin levels and slower microtubule growth [PMID:18062952 "Our analyses suggest that these defects result mainly from a decrease in alpha-tubulin levels and a subsequent reduction in the microtubule growth rate."]. PMID:18062952 is abstract-only in the cache, so its IDA/IMP rows defer to the curator.
- C. elegans prefoldin = PFD-1..PFD-6 [PMID:30478249 "The prefoldin complex is composed of PFD-1 through PFD-6 and acts as a chaperone for the proper folding of many essential proteins, including actins and tubulins"].
- Body-wall muscle GFP screen: H20J04.5 in category 6 'Dense bodies, Thick filaments and/or M-lines, ER/SR' [PMID:21611156 "D2013.9*, F55C10.1§, H20J04.5, K08E3.5"]. The three HDA rows (ER, sarcomere, dense body) are kept as non-core: a single overexpression observation for a cytosolic chaperone.
- pfd-2 RNAi modestly reduced daf-2 longevity, like the R2TP/prefoldin-like components [PMID:30478249 "We also found that knockdown of pfd-2 modestly decreased the longevity conferred by daf-2 mutations"]. In mammals PFDN2 and PFDN6 are shared with the prefoldin-like complex.
- IBA GO:0030674 protein-macromolecule adaptor activity: MODIFY to GO:0044183 protein folding chaperone.

## Core function
GO:0044183 protein folding chaperone, in GO:0016272 prefoldin complex, cytoplasm; BP GO:0006457 protein folding.
