# PIP4K2C manual review notes

Automated deep research was not available without starting an extra worker, so this review uses the seeded GOA references, UniProt, and the existing PTHR23086 family review directly.

## Evidence notes

- PIP4K2C is the gamma type-II phosphatidylinositol-5-phosphate 4-kinase. It belongs to the same PTN001132453 type-II clade as PIP4K2A/B, but biochemical assays report very low activity compared with PIP4K2A and PIP4K2B.
- The existing PTHR23086 family review records that older PI4P 5-kinase annotations on PIP4K2A/B/C come from the period before the type-II substrate was correctly identified. This supports keeping GO:0016309 and removing GO:0016308 on PIP4K2C.
- Mathre 2019 found that PIP4K2C is much less active than PIP4K2A in vitro but can still rescue Drosophila PIP4K null salivary-gland size, implying that its weak PI5P 4-kinase chemistry can be functional in vivo (PMID:30718367).
- The PI(5)P autophagy paper perturbed all three PI5P4K2 isoforms and localized PIP4K2C most prominently to autophagosomes. It supports the broad regulation-of-autophagy and autophagosome-location rows as non-core, but its autophagosome-biogenesis data support negative rather than positive regulation of autophagosome assembly (PMID:25578879).
- The PIP4K family suppresses insulin-stimulated PI3K signaling by a catalytic-independent interaction with PIP5K1A; PIP4K2C directly inhibited PIP5K1A in vitro, and PIP4K2C rescue reversed enhanced insulin sensitivity of triple PIP4K-depleted cells (PMID:31091439).
- The CCDC88A and KRAS AP-MS interactions are bare protein-binding assertions; they do not establish more informative PIP4K2C molecular functions. The PIP5K1A binding row from PMID:31091439 is functionally meaningful but is still represented only as bare protein binding in GOA.
- The exosome HDA rows come from broad extracellular-vesicle proteomics papers; the cached abstracts do not name PIP4K2C, so those locations need the supplemental protein tables before they can be confirmed.
