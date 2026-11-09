# AZOBR fruA1: evidence review, 2026-11-06

The normal fetched seed is preserved in the shared seed-baseline.yaml. Every original annotation payload and row order is retained. No new annotation rows were added.

Identity: A0A0P0F8C9; see the explicit strain and complete-sequence bridge in analysis/module_audits/bacterial_fructose_pts_catabolism/alpha-identity.yaml. Published Sp7 gene aliases fruA1/fruB1/fruK1 are retained. Current source names ptsP/pfkB/SIM66 loci do not override the exact protein-to-AMK58 mapping or establish a nitrogen-related pathway. Current UniProt uses species taxon192; source culture ATCC29145 equals Sp7. PMID39817736 tests native induction, FruA disruptions/complementation, growth and spent-medium fructose consumption. Those are not purified FruB1/FruK1 catalysis or site-specific phosphotransfer assays.

Interpretation: FruA1 is the principal membrane fructose phosphotransferase-system permease in Azospirillum brasilense Sp7 under fructose sole-carbon growth conditions. It couples fructose entry to formation of fructose 1-phosphate using phosphate supplied by the soluble fused FruB relay. The EIIB cysteine-dependent mechanism is inferred from conserved PTS domains and the characterized E. coli homolog; the duplicated N-terminal B-like region is not evidence for a second catalytic phosphoacceptor. Its paralog FruA2 has a different, secondary contribution under the tested conditions.

FruA net phosphohistidine-to-sugar and immediate phosphocysteine-to-sugar terms describe different reaction boundaries. The latter is the core residue-level function; net histidine claims are not removed merely because the internal donor is cysteine. Proton symport mappings are rejected as the wrong energy-coupling mechanism. Broad true activities are refined only through justified specificity; FruB kinase is retained because its definition says usually, not exclusively, ATP and GO0008965 lacks that ancestry. Phosphoryl flow EI→HPr→EIIA differs from N-to-C domain order EIIA–HPr–EI. PTHR46244:SF6 alone does not establish fusion.

No NEW BP is inferred from necessity or adjacency. Existing FruK carbohydrate-process claims refine to its catalytic role in fructose catabolism. FruB downstream relay is an explicitly proposed MF, not a manufactured GO identifier or transport role.

Research: genuine `just deep-research AZOBR fruA1 --provider falcon` failed HTTP403 authentication; no provider report was written. Manual primary/source research supports this review. Logs are in ignored .cache/module-audit-logs/fructose-pts-20261106/alpha-review/. Existing publications remain byte-identical. Rhodobacter primary caches are abstract-only; attempted EuropePMC PDF endpoints returned403 and PMC supplied a browser challenge; the alternate Citeseer FruK PDF returned404. No unavailable full-text kinetics or negative assays are claimed.

- PMID:39817736: "Figure 1B and C shows that inactivation of the fruA1 led to a complete loss of the ability of the fruA1::km mutant to grow on fructose as sole carbon source suggesting its primary role in supporting growth on fructose."
- file:analysis/module_audits/bacterial_fructose_pts_catabolism/alpha-identity.yaml: "A0A0P0F8C9"
- file:AZOBR/fruA1/fruA1-uniprot.txt: "IPR006327; PTS_IIC_fruc."


## 2026-11-07 PR #6144 review follow-up

Architecture-dependent rows now cite the publication's membrane-bound EIIB/EIIC sentence, while transport/process phenotype rows retain the growth result. The phosphocysteine refinement additionally cites the target fructose-specific EIIB signature IPR003353, rather than only EIIC. These support a conserved-mechanism inference; no site-resolved phosphocysteine assay or direct localization experiment is claimed. The primary reference now distinguishes native locus induction and mutant physiology from those chemical inferences. [PMID:39817736 "Although the membrane-bound FruA consists of EIIB and EIIC domains, the cytosolic FruB is a larger polyprotein and consists of EIIA-HPr-EI domains (15)."]

Original GOA annotation payloads, actions and order are unchanged. See `analysis/module_audits/bacterial_fructose_pts_catabolism/round1-review-response.md` for the six-findings disposition, including the retained current GO:0006001 preferred label.
