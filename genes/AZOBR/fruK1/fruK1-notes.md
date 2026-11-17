# AZOBR fruK1: evidence review, 2026-11-06

The normal fetched seed is preserved in the shared seed-baseline.yaml. Every original annotation payload and row order is retained. No new annotation rows were added.

Identity: A0A0P0F764; see the explicit strain and complete-sequence bridge in analysis/module_audits/bacterial_fructose_pts_catabolism/alpha-identity.yaml. Published Sp7 gene aliases fruA1/fruB1/fruK1 are retained. Current source names ptsP/pfkB/SIM66 loci do not override the exact protein-to-AMK58 mapping or establish a nitrogen-related pathway. Current UniProt uses species taxon192; source culture ATCC29145 equals Sp7. PMID39817736 tests native induction, FruA disruptions/complementation, growth and spent-medium fructose consumption. Those are not purified FruB1/FruK1 catalysis or site-specific phosphotransfer assays.

Interpretation: FruK1 is the fructose-1-phosphate kinase of the fructose-inducible Fru-PTS1 locus in Azospirillum brasilense Sp7. It phosphorylates fructose 1-phosphate with ATP to form fructose 1,6-bisphosphate, connecting fructose PTS uptake to central carbon metabolism. It belongs to the PfkB carbohydrate-kinase family; this membership does not make it a fructose-6-phosphate kinase. The specific reaction is inferred from its FruK classification and native pathway context, rather than a purified FruK1 assay in the 2025 study.

FruA net phosphohistidine-to-sugar and immediate phosphocysteine-to-sugar terms describe different reaction boundaries. The latter is the core residue-level function; net histidine claims are not removed merely because the internal donor is cysteine. Proton symport mappings are rejected as the wrong energy-coupling mechanism. Broad true activities are refined only through justified specificity; FruB kinase is retained because its definition says usually, not exclusively, ATP and GO0008965 lacks that ancestry. Phosphoryl flow EI→HPr→EIIA differs from N-to-C domain order EIIA–HPr–EI. PTHR46244:SF6 alone does not establish fusion.

No NEW BP is inferred from necessity or adjacency. Existing FruK carbohydrate-process claims refine to its catalytic role in fructose catabolism. FruB downstream relay is an explicitly proposed MF, not a manufactured GO identifier or transport role.

Research: genuine `just deep-research AZOBR fruK1 --provider falcon` failed HTTP403 authentication; no provider report was written. Manual primary/source research supports this review. Logs are in ignored .cache/module-audit-logs/fructose-pts-20261106/alpha-review/. Existing publications remain byte-identical. Rhodobacter primary caches are abstract-only; attempted EuropePMC PDF endpoints returned403 and PMC supplied a browser challenge; the alternate Citeseer FruK PDF returned404. No unavailable full-text kinetics or negative assays are claimed.

- PMID:39817736: "Fructose-1-phosphate, the product of PTSFru reactions, enters the glycolytic pathway for further catabolism after its conversion to fructose-1,6-bisphosphate by 1-phosphofructokinase (1-PFK) (16, 17)."
- file:analysis/module_audits/bacterial_fructose_pts_catabolism/alpha-identity.yaml: "A0A0P0F764"
- file:AZOBR/fruK1/fruK1-uniprot.txt: "IPR022463; 1-PFruKinase."


## 2026-11-07 PR #6144 review follow-up

The primary reference now separates native PTS1 FruK induction from the introductory pathway chemistry and inferred target substrate specificity. No purified FruK1 kinetic measurement is attributed to this paper. [PMID:39817736 "Fructose-1-phosphate, the product of PTSFru reactions, enters the glycolytic pathway for further catabolism after its conversion to fructose-1,6-bisphosphate by 1-phosphofructokinase (1-PFK) (16, 17)."]

Original GOA annotation payloads, actions and order are unchanged. See `analysis/module_audits/bacterial_fructose_pts_catabolism/round1-review-response.md` for the six-findings disposition, including the retained current GO:0006001 preferred label.
