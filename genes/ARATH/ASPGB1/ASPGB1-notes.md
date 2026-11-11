# ASPGB1 evidence audit

UniProt Q8GXG1 has no GN primary symbol; ASPGB1 is mapped explicitly to At3g16150 in primary PMID:21800258. Primary study PMID:16705405 directly demonstrates K+-enhanced asparaginase activity and autocatalytic cleavage exposing catalytic Thr. Primary study PMID:22127737 revises the original no-dipeptidase claim: ASPGB1 hydrolyzes beta-Asp-His as well as Asn, while showing much greater Asn activity than ASPGA1. Thus retain beta-aspartyl-peptidase capacity without inventing a native protein-degradation pathway. Full text of PMID:21800258 author-uploaded primary reproduction inspected at https://www.researchgate.net/publication/51531651_Arabidopsis_mutants_lacking_asparaginases_develop_normally_but_exhibit_enhanced_root_inhibition_by_exogenous_asparagine : independent single mutants enhance root inhibition by Asn; many seed/pool phenotypes concern the double mutant. Normal growth under tested conditions does not establish absent catabolic function.

All original annotation payloads retained; only review objects were curated. Falcon and perplexity-lite fallback were attempted concurrently with publication caching and failed (403/401 provider errors); no provider report was fabricated. FEBA is not applicable to this plant panel.

All annotations were assessed as biological claims. Specific true functions were retained across evidence codes; broad terms were refined; unresolved compartment/affinity-screen claims were not converted into negative evidence. No NEW annotations were added solely to fill module coverage.

Supplementary-table provenance and exact target rows are in `../ASP2/ASP2-source-analysis/` (or the local ASP2-source-analysis directory for ASP2). PMID:28887381 is a mixed-fraction protein-correlation study, not automatic evidence of every annotated compartment. PMID:21533090 S3 peptide detection and S4 targeting classification were inspected; S5 merely lists prior GO assertions and was not used as independent evidence.


## PR #5568 follow-up, 2026-10-26

Repaired authored citation spacing and fused numeric prose while preserving original annotation payloads, every action, raw UniProt/GOA records and all existing supporting quotations. Source-cited passages in notes were protected from rewriting. Replaced generic compartment boilerplate with the concrete question of whether the beta-Asp-His activity measured in PMID:22127737 contributes detectable native substrate flux. No protein-degradation pathway is asserted.
