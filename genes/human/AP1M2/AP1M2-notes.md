# AP1M2 (AP-1 complex subunit mu-1B) review notes

UniProt: **Q9Y6Q5** → **AP1M2**. Taxon: 9606. Medium (mu) subunit of clathrin adaptor AP-1 (mu1B).

## Core function (standalone summary)

AP1M2 is the **medium (mu-type) subunit mu1B of clathrin-associated adaptor protein complex 1
(AP-1)**. AP-1 recruits clathrin to the trans-Golgi network and endosomes and recognises
tyrosine-based sorting signals in the cytosolic tails of transmembrane cargo. The mu1B isoform
is expressed in polarized epithelial cells and directs **basolateral** protein sorting (the
epithelial AP-1B complex), distinguishing it from the ubiquitous mu1A/AP-1A.

## Key evidence (provenance)

- [PMID:10338135 title]: "Mu1B, a novel adaptor medium chain expressed in polarized epithelial
  cells." — basis for GO:0035615 clathrin-cargo adaptor activity (core) and the mu1B identity.
- [PMID:27057418]: AP-1B basolateral sorting role.
- UniProt Q9Y6Q5: subunit of AP-1 that functions in TGN/endosome protein sorting; recognition
  of sorting signals in cargo cytosolic tails.

## Annotation landscape (GOA, 44 rows)

- Core MF: GO:0035615 clathrin-cargo adaptor activity; part_of GO:0030121 AP-1 adaptor complex.
- Core locations: Golgi/TGN membrane (GO:0032588), cytosol, Golgi membrane, vesicle membranes.
- GO:0030131 clathrin adaptor complex -> TOO_GENERAL (parent of the asserted GO:0030121).
- Bare protein binding IPI (AP2B1 interactome) -> REMOVE per policy.
