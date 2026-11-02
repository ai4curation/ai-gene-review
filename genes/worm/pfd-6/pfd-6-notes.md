# pfd-6 (F21C3.5, UniProt P52554) notes

## Deep research status
`just deep-research-falcon worm pfd-6 --fallback perplexity-lite` was run on 2026-10-08. The client reported a timeout, and the perplexity fallback is not available in this environment, but Falcon later wrote `pfd-6-deep-research-falcon.md`. Its claims drawn from Lundin's 2008 thesis are not verified against primary text. Primary claims in the review are based on cached publications (PMID:9630229, PMID:18062952 [abstract only], PMID:21611156, PMID:20554764, PMID:30478249) and UniProt. A PubMed search for "prefoldin AND elegans" returned PMID:18062952, PMID:20554764, PMID:30478249 and PMID:16436622 (URI-1).

## Summary
- beta-class prefoldin subunit, ortholog of human PFDN6. Prefoldin is a heterohexamer of two alpha and four beta subunits [file:worm/pfd-6/pfd-6-uniprot.txt "Heterohexamer of two PFD-alpha type and four PFD-beta type subunits."].
- Prefoldin captures unfolded actin and tubulin and passes them to cytosolic chaperonin [PMID:9630229 "Prefoldin binds specifically to cytosolic chaperonin (c-cpn) and transfers target proteins to it."].
- C. elegans: prefoldin RNAi causes embryonic lethality through lower alpha-tubulin levels and slower microtubule growth [PMID:18062952 "Our analyses suggest that these defects result mainly from a decrease in alpha-tubulin levels and a subsequent reduction in the microtubule growth rate."]. PMID:18062952 is abstract-only in the cache, so its IDA/IMP rows defer to the curator.
- C. elegans prefoldin = PFD-1..PFD-6 [PMID:30478249 "The prefoldin complex is composed of PFD-1 through PFD-6 and acts as a chaperone for the proper folding of many essential proteins, including actins and tubulins"].
- PFD-6 is required for daf-2 longevity in the intestine and hypodermis, and HSF-1 raises PFD-6 levels [PMID:30478249 "We found that PFD-6 was specifically required for reduced IIS-mediated longevity by acting in the intestine and hypodermis."].
- PFD-6 binds DAF-16/FOXO (Y2H and split GFP) and binds UXT and PFD-5 [PMID:30478249 "We then showed that PFD-6 bound to DAF-16/FOXO by using yeast two-hybrid and split GFP system assays"]. The authors attribute the longevity role to the R2TP/prefoldin-like complex, not canonical prefoldin [PMID:30478249 "These data suggest that the R2TP/prefoldin-like complex, rather than the prefoldin complex, contributes to the long life span of daf-2(−) mutants."].
- Localization in cytosol and nuclei [PMID:30478249 "PFD-6::GFP fusion protein was localized in both the cytosol and nuclei of intestinal, hypodermal, muscle, and neuronal cells throughout the developmental stages"]. Added NEW nucleus (IDA).
- No NEW process term (e.g. determination of adult lifespan) was added. The effect runs through DAF-16 activity, and its mechanism is not established. It is raised in suggested_questions instead.

## Core function
GO:0044183 protein folding chaperone, in GO:0016272 prefoldin complex, cytoplasm; BP GO:0006457 protein folding.
