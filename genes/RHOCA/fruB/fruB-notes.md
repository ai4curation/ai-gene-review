# RHOCA fruB: evidence review, 2026-11-06

The normal fetched seed is preserved in the shared seed-baseline.yaml. Every original annotation payload and row order is retained. No new annotation rows were added.

Identity: P23388; see the explicit strain and complete-sequence bridge in analysis/module_audits/bacterial_fructose_pts_catabolism/alpha-identity.yaml. The original sequence record X53150 and curated primary references identify DSM938/37b4, not SB1003. PMID2193161 predicts phosphorylation sites from homology; PMID2254279 presumes the conserved cysteine to be active. These words are retained as evidence limits rather than upgraded to direct phosphosite assays.

Interpretation: FruB(HI) is the soluble multiphosphoryl-transfer protein of the Rhodobacter capsulatus fructose PTS. Its N-to-C domain order is EIIA–HPr–EI, while phosphate flows from phosphoenolpyruvate through EI, HPr and EIIA before transfer to the membrane FruA component. The fused architecture supplies both PEP entry and the downstream protein phosphorelay. The three histidine phosphoacceptor sites were predicted by sequence comparison, rather than individually established by site-specific phosphorylation assays in the 1990 sequence study.

FruA net phosphohistidine-to-sugar and immediate phosphocysteine-to-sugar terms describe different reaction boundaries. The latter is the core residue-level function; net histidine claims are not removed merely because the internal donor is cysteine. Proton symport mappings are rejected as the wrong energy-coupling mechanism. Broad true activities are refined only through justified specificity; FruB kinase is retained because its definition says usually, not exclusively, ATP and GO0008965 lacks that ancestry. Phosphoryl flow EI→HPr→EIIA differs from N-to-C domain order EIIA–HPr–EI. PTHR46244:SF6 alone does not establish fusion.

No NEW BP is inferred from necessity or adjacency. Existing FruK carbohydrate-process claims refine to its catalytic role in fructose catabolism. FruB downstream relay is an explicitly proposed MF, not a manufactured GO identifier or transport role.

Research: genuine `just deep-research RHOCA fruB --provider falcon` failed HTTP403 authentication; no provider report was written. Manual primary/source research supports this review. Logs are in ignored .cache/module-audit-logs/fructose-pts-20261106/alpha-review/. Existing publications remain byte-identical. Rhodobacter primary caches are abstract-only; attempted EuropePMC PDF endpoints returned403 and PMC supplied a browser challenge; the alternate Citeseer FruK PDF returned404. No unavailable full-text kinetics or negative assays are claimed.

- PMID:2193161: "MTP consists of three moieties: a fructose-specific enzyme III
(IIIfru)-like N-terminal moiety (residues 1 to 143) followed by an FPr(HPr)-like
moiety (residues 157 to 245) and an enzyme I-like moiety (residues 273 to 827)."


## 2026-11-07 PR #6144 review follow-up

Aligned the EIIA-to-EIIB proposal definition and ontology boundary with PSEPK and AZOBR. The sequence-matched locus architecture and curated domain statement remain the target-specific support; purified pairwise transfer kinetics or phosphosite assays are not asserted. [PMID:2193161, reported IIIfru/HPr/EI residue ranges; file:RHOCA/fruB/fruB-uniprot.txt, CC:DOMAIN.]

Original GOA annotation payloads, actions and order are unchanged. See `analysis/module_audits/bacterial_fructose_pts_catabolism/round1-review-response.md` for the six-findings disposition, including the retained current GO:0006001 preferred label.
