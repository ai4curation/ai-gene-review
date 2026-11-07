# lspA consultation notes

## 2026-11-07 — source-qualified KT2440 review

Reviewed all original annotations and the core function against frozen UniProt/HAMAP features, genuine existing OpenScientist research and the primary sources summarized in [the consultation evidence](../../../analysis/module_audits/bacterial_lipoprotein_maturation/psepk-consultation/evidence.md). Provider files and source payloads remain unchanged. No direct KT2440 biochemical assay or essentiality result was located in the consulted sources; experimental statements from E. coli/P. aeruginosa retain their species scope.

[PMID:26912896, "Mutagenesis studies identify LspA as an aspartyl peptidase."] The accessible primary abstract specifies P. aeruginosa; publisher full text returned403. GO0006508 changes from MAOA to ACCEPT because direct signal-peptide hydrolysis is proteolysis. Retain the inherited NEW lipoprotein-biosynthesis row on actual reaction participation. Fresh GO0009003 is active/reinstated and now supplies the core MF; existing0004190 remains correct for the catalytic mechanism. The narrower proposed lipoprotein-specific term remains, with corrected parent/rationale. No additional NEW row is added. D126/D145 are target catalytic annotations; global alignment of the first Asp is parameter-sensitive, explicitly documented rather than treated as a loss.

PAINT-loss tooling could not inspect a target lineage because the accession is absent from its cached family tree. No verified loss-free ancestry or invented PTN is claimed. Conserved enzyme work supports the biosynthetic process; necessity alone and pathway-neighbor annotations are not used as participation evidence.


## PR 6184 source adjudication, 2026-11-07

GO:0006508 is refined to GO:0016485 protein processing, consistently with ECOLI/BACSU LspA. QuickGO confirms the is_a relationship. The product performs peptide cleavage itself; it is not merely the substrate of processing. Curated target membership and mechanism inference remain distinct from direct KT2440 assay evidence. No annotation rows were added.
