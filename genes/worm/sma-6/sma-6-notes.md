# sma-6 (Q09488) review notes

- Deep research: the first run (falcon, 600 s timeout, perplexity-lite fallback unavailable) failed. A rerun with `--timeout 1500` produced `sma-6-deep-research-falcon.md`.
- Identity: the type I BMP receptor kinase of the DBL-1 Sma/Mab pathway [PMID:9847239 "We have cloned and characterized a novel type I receptor and show that it is encoded by sma-6"].
- Tissue: hypodermis is the key site [PMID:11784045 "hypodermal expression of SMA-6 is necessary and sufficient for the growth and maintenance of body length"].
- Localization and trafficking: basolateral plasma membrane; recycling through retromer [PMID:24550286 "localized to the basolateral plasma membrane, where they are in position to receive signaling molecules secreted by neurons"].
- Not dauer-constitutive [PMID:9847239 "However, mutations in sma-6, sma-2, sma-3, or sma-4 do not produce constitutive dauers"]. The dauer IGI rows are therefore kept as non-core crosstalk.
- IBA activin terms (PTN000583887) changed to their BMP equivalents. C. elegans has no activin, and the SMA-6 ligand is the BMP-like DBL-1.
- IEA nucleus removed: it was derived from the SMA-3 nuclear-retention phenotype, not from SMA-6 itself.
- Core MF: GO:0098821 BMP receptor activity (child of GO:0004675, which the module uses).
