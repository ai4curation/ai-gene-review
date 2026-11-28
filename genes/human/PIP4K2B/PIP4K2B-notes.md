# PIP4K2B manual review notes

Automated deep research was not available without starting an extra worker, so this review uses the seeded GOA references, UniProt, and the existing PTHR23086 family review directly.

## Evidence notes

- PIP4K2B is the beta type-II phosphatidylinositol-5-phosphate 4-kinase. It phosphorylates PI5P, can use ATP or GTP as phosphodonor, and is the human isoform characterized as an intracellular GTP sensor in Sumita 2016 (PMID:26774281).
- The existing PTHR23086 family review places PIP4K2A/B/C in the type-II clade PTN001132453 and records that older PI4P 5-kinase annotations on these enzymes come from the period before the type-II substrate was correctly identified. This supports keeping GO:0016309 and removing GO:0016308 on PIP4K2B.
- The PIP4K2B crystal structure paper described the type II beta enzyme as a disc-shaped homodimer with a basic membrane-facing surface; this supports the homodimer row as structural context for membrane interfacial catalysis rather than a separate core function (PMID:9753329).
- PIP4K2A and PIP4K2B mediate autophagosome-lysosome fusion under nutrient stress, most likely through lysosomal PI(4,5)P2 synthesis. Lundquist 2018 directly supports the PIP4K2A/PIP4K2B fusion rows (PMID:29727621).
- The PI(5)P autophagy paper perturbed all three PI5P4K2 isoforms and localized PIP4K2 proteins to autophagosomes. It supports the broad regulation-of-autophagy and autophagosome-location rows as non-core, but its autophagosome-biogenesis data support negative rather than positive regulation of autophagosome assembly (PMID:25578879).
- The PIP4K family suppresses insulin-stimulated PI3K signaling by a catalytic-independent interaction with PIP5K1A; all three PIP4K isoforms could directly inhibit PIP5K1A in vitro, and PIP4K2A or PIP4K2C rescue reversed the enhanced insulin sensitivity of triple PIP4K-depleted cells (PMID:31091439).
- Old PIP4K2B annotations to cell-surface receptor signaling derive from the 1997 p55 TNF-receptor binding paper. That paper showed interaction of PIP5KIIbeta with the receptor and an increase in bulk PIP5K activity after TNF-alpha, but it does not show PIP4K2B executing a receptor-signaling step (PMID:9038203).
- The AP-MS and yeast-two-hybrid protein-binding rows for PIP4K2B are bare protein-binding assertions; they do not establish more informative PIP4K2B molecular functions.
