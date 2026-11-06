# AZOBR fruB1: evidence review, 2026-11-06

The normal fetched seed is preserved in the shared seed-baseline.yaml. Every original annotation payload and row order is retained. No new annotation rows were added.

Identity: A0A0P0ES92; see the explicit strain and complete-sequence bridge in analysis/module_audits/bacterial_fructose_pts_catabolism/alpha-identity.yaml. Published Sp7 gene aliases fruA1/fruB1/fruK1 are retained. Current source names ptsP/pfkB/SIM66 loci do not override the exact protein-to-AMK58 mapping or establish a nitrogen-related pathway. Current UniProt uses species taxon192; source culture ATCC29145 equals Sp7. PMID39817736 tests native induction, FruA disruptions/complementation, growth and spent-medium fructose consumption. Those are not purified FruB1/FruK1 catalysis or site-specific phosphotransfer assays.

Interpretation: FruB1 is the soluble multiphosphoryl-transfer protein of the fructose-inducible Fru-PTS1 system of Azospirillum brasilense Sp7. Its N-to-C domain order is EIIA–HPr–EI, while phosphate flows from phosphoenolpyruvate through EI, HPr and EIIA before transfer to the membrane FruA component. The fused architecture supplies both PEP entry and the downstream protein phosphorelay. The native locus is AMK58_25885; the current database symbol ptsP does not establish a nitrogen-specific PTS role.

FruA net phosphohistidine-to-sugar and immediate phosphocysteine-to-sugar terms describe different reaction boundaries. The latter is the core residue-level function; net histidine claims are not removed merely because the internal donor is cysteine. Proton symport mappings are rejected as the wrong energy-coupling mechanism. Broad true activities are refined only through justified specificity; FruB kinase is retained because its definition says usually, not exclusively, ATP and GO0008965 lacks that ancestry. Phosphoryl flow EI→HPr→EIIA differs from N-to-C domain order EIIA–HPr–EI. PTHR46244:SF6 alone does not establish fusion.

No NEW BP is inferred from necessity or adjacency. Existing FruK carbohydrate-process claims refine to its catalytic role in fructose catabolism. FruB downstream relay is an explicitly proposed MF, not a manufactured GO identifier or transport role.

Research: genuine `just deep-research AZOBR fruB1 --provider falcon` failed HTTP403 authentication; no provider report was written. Manual primary/source research supports this review. Logs are in ignored .cache/module-audit-logs/fructose-pts-20261106/alpha-review/. Existing publications remain byte-identical. Rhodobacter primary caches are abstract-only; attempted EuropePMC PDF endpoints returned403 and PMC supplied a browser challenge; the alternate Citeseer FruK PDF returned404. No unavailable full-text kinetics or negative assays are claimed.

- PMID:39817736: "Although the membrane-bound FruA consists of EIIB and EIIC domains, the cytosolic FruB is a larger polyprotein and consists of EIIA-HPr-EI domains (15)."
- file:analysis/module_audits/bacterial_fructose_pts_catabolism/alpha-identity.yaml: "A0A0P0ES92"
- file:AZOBR/fruB1/fruB1-uniprot.txt: "IPR006318; PTS_EI-like."
