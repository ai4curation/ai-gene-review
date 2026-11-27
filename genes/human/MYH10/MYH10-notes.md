# MYH10 review notes

## 2026-09-27 (claude-code)

- Identity: human MYH10 (P35580), non-muscle myosin heavy chain IIB (not MYO10).
- Motor: [PMID:15845534 "we characterized the in vitro activity of mutated and wild-type baculovirus-expressed heavy meromyosin (HMM) II-B and II-C"]; [PMID:24072716 "RLC phosphorylated NM IIB filaments are capable of binding to and translocating along actin filaments as a processive unit"].
- Cytokinesis: [PMID:15774463 "62.4 +/- 8.8% of the NMHC II-B RNAi-treated cells were multinucleated 72 h after transfection"].
- Neuronal migration: mouse motor-domain mutant [PMID:15034141 "These studies demonstrate that NMHC II-B is particularly important for normal migration of distinct groups of neurons during mouse brain development."] (cached, PubMed-verified); CGN leading process [PMID:19607793 "By immunocytochemistry, Myosin IIB localizes to the leading process of migrating CGNs in vitro and in vivo"]; blebbistatin blocks MGE nucleokinesis [PMID:15958735].
- Decisions: RNA stem-loop binding and mRNA 5'-UTR binding (PMID:20603131) REMOVE — full text says LARP6 is the only direct 5'SL binder and myosin is tethered via LARP6. Positive regulation of protein secretion MARK_AS_OVER_ANNOTATED (pharmacological, collagen-specific). Nucleus (sperm proteomics), exosome (HDA), spindle (IEA) marked over-annotated.
- NEW: GO:0001764 neuron migration (mouse Myh10 carries it by IMP; human lacks it because acts_upstream_of_or_within rodent rows are not propagated).
- Module check: GO:0000146 microfilament motor activity agrees. Paralog assignment for nucleokinesis rear contraction (IIA vs IIB) is not resolved by the pharmacological studies.
- Deep research (falcon) arrived later and was incorporated: consistent (tension-bearing NM2-B motor; neuronal soma/nuclear translocation).
