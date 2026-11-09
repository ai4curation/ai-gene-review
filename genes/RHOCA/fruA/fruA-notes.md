# RHOCA fruA: evidence review, 2026-11-06

The normal fetched seed is preserved in the shared seed-baseline.yaml. Every original annotation payload and row order is retained. No new annotation rows were added.

Identity: P23387; see the explicit strain and complete-sequence bridge in analysis/module_audits/bacterial_fructose_pts_catabolism/alpha-identity.yaml. The original sequence record X53150 and curated primary references identify DSM938/37b4, not SB1003. PMID2193161 predicts phosphorylation sites from homology; PMID2254279 presumes the conserved cysteine to be active. These words are retained as evidence limits rather than upgraded to direct phosphosite assays.

Interpretation: FruA is the membrane EIIB'BC fructose phosphotransferase-system permease of Rhodobacter capsulatus. It couples fructose entry to formation of fructose 1-phosphate using phosphate supplied by the soluble fused FruB relay. The EIIB cysteine-dependent mechanism is inferred from conserved PTS domains and the characterized E. coli homolog; the duplicated N-terminal B-like region is not evidence for a second catalytic phosphoacceptor. The protein sequence was characterized from strain DSM938/37b4.

FruA net phosphohistidine-to-sugar and immediate phosphocysteine-to-sugar terms describe different reaction boundaries. The latter is the core residue-level function; net histidine claims are not removed merely because the internal donor is cysteine. Proton symport mappings are rejected as the wrong energy-coupling mechanism. Broad true activities are refined only through justified specificity; FruB kinase is retained because its definition says usually, not exclusively, ATP and GO0008965 lacks that ancestry. Phosphoryl flow EI→HPr→EIIA differs from N-to-C domain order EIIA–HPr–EI. PTHR46244:SF6 alone does not establish fusion.

No NEW BP is inferred from necessity or adjacency. Existing FruK carbohydrate-process claims refine to its catalytic role in fructose catabolism. FruB downstream relay is an explicitly proposed MF, not a manufactured GO identifier or transport role.

Research: genuine `just deep-research RHOCA fruA --provider falcon` failed HTTP403 authentication; no provider report was written. Manual primary/source research supports this review. Logs are in ignored .cache/module-audit-logs/fructose-pts-20261106/alpha-review/. Existing publications remain byte-identical. Rhodobacter primary caches are abstract-only; attempted EuropePMC PDF endpoints returned403 and PMC supplied a browser challenge; the alternate Citeseer FruK PDF returned404. No unavailable full-text kinetics or negative assays are claimed.

- PMID:2254279: "This gene codes for the fructose
permease (molecular weight, 58,575; 578 aminoacyl residues), the fructose enzyme
II (IIFru) of the phosphoenolpyruvate-dependent phosphotransferase system."
