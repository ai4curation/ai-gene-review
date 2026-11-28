# PIP4K2A manual review notes

Automated deep research was not available without starting an extra worker, so this review uses the seeded GOA references, UniProt, and the existing PTHR23086 family review directly.

## Evidence notes

- PIP4K2A is a type II phosphatidylinositol-5-phosphate 4-kinase: it phosphorylates PI5P at the 4-position to make PI(4,5)P2, in contrast to type I PIP5Ks that phosphorylate PI4P at the 5-position. Rameh 1997 explicitly corrected the historical substrate assignment by showing that the type II enzyme phosphorylates PtdIns-5-P at the D-4 position rather than PtdIns-4-P at the D-5 position (PMID:9367159).
- The existing PTHR23086 family review places PIP4K2A/B/C in the type-II clade PTN001132453 and records that older PI4P 5-kinase annotations on these enzymes come from the period before the type-II substrate was correctly identified. This supports keeping GO:0016309 and removing GO:0016308 on PIP4K2A.
- PIP4K2A has the highest PI5P 4-kinase activity among the mammalian type-II isoforms. Mathre 2019 found that all three mammalian isoforms can rescue Drosophila PIP4K null salivary-gland size in vivo, but this rescue is a heterologous model and should be treated as support for conserved PI5P 4-kinase function rather than for a human salivary-gland process (PMID:30718367).
- PIP4K2A and PIP4K2B mediate autophagosome-lysosome fusion under nutrient stress, most likely through lysosomal PI(4,5)P2 synthesis. Lundquist 2018 directly supports the PIP4K2A/PIP4K2B fusion rows (PMID:29727621).
- The PI(5)P autophagy paper perturbed all three PI5P4K2 isoforms and localized PIP4K2 proteins to autophagosomes. It supports the broad regulation-of-autophagy and autophagosome-location rows as non-core, but its autophagosome-biogenesis data support negative rather than positive regulation of autophagosome assembly (PMID:25578879).
- PIP4K2A regulates LDL-derived cholesterol transport from lysosomes to peroxisomes by modulating peroxisomal PI(4,5)P2 and lysosome-peroxisome membrane contacts in human SV-589 fibroblasts (PMID:29353240).
- The PIP4K family suppresses insulin-stimulated PI3K signaling by a catalytic-independent interaction with PIP5K1A; all three PIP4K isoforms could directly inhibit PIP5K1A in vitro, and PIP4K2A or PIP4K2C rescue reversed the enhanced insulin sensitivity of triple PIP4K-depleted cells (PMID:31091439).
- PIP4K2A is found in cytosol, nucleus and plasma-membrane contexts, with specialized photoreceptor-segment localization inferred from mouse Pip4k2a. Those specialized retinal annotations should be non-core for the broadly expressed human kinase.
- The MEIS3 AP-MS interaction is from a broad interactome map and is a bare protein-binding row; it does not establish a PIP4K2A molecular function beyond physical association (PMID:32296183).
