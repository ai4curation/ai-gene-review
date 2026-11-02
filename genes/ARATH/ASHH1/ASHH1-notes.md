# ASHH1 curation notes


## 2026-10-26 complete annotation audit

All 16 original rows preserved; one conservative NEW molecular activity is added: GO:0003690 double-stranded DNA binding, from purified target fragment EMSA in PMID:35766439 Figure 3. This is not a new process claim. The original SDG25-titled reference PMID:19726574 was read in full and explicitly discusses SDG26 biochemical evidence; no title-based misattribution is alleged. Normal retrieval of PMID:18070919 retrieval recovered its direct-target abstract. H3K36 activity is retained as conserved SET2 inference plus target evidence; H3K4 trimethylation specificity remains unresolved because SOC1 ChIP dependence alone cannot identify the direct catalyst. The Y118A rescue assay uses a conserved catalytic-site substitution and does not independently measure the mutant enzyme reaction. Centromeric location remains unresolved rather than rejected from nuclear localization. UV-B damage functions are retained as contextual.

All seeded rows were reviewed, with original term, evidence, source, supporting-entity and qualifier/NOT payloads preserved. The shared normal Falcon attempt and perplexity-lite fallback both failed; logs are retained under `.cache/module-audit-logs/autonomous-flowering-fetch/ARATH-ASHH1-provider.log`. No provider report was fabricated. Manual primary-literature assessment and normal publication fetching supplied this review. Source access limits are stated per reference/claim. Generic protein binding follows the current informative-function policy; its removal does not reject the physical interactions. Nuclear localization does not by itself exclude additional compartments.


## PR #5574 prose and justification follow-up

Corrected citation spacing in reviewer-authored prose without altering original annotation payloads, source quotations, raw source files or prior histories. The two histone-methyltransferase refinements now distinguish the SDG26 evidence discussed within the original SDG25 paper from the domain-derived assertion. H3K36 specificity is retained as combined biochemical/family inference, not recast as an uninspected residue-specific assay. The completed review status is COMPLETE.
