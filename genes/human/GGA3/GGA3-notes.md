# GGA3 review notes

UniProt: **Q9NZ52** → **GGA3** (Golgi-localized, gamma-adaptin ear-containing, ARF-binding protein 3). Taxon: 9606. Monomeric clathrin adaptor.

## Core function (standalone summary)

GGA3 is a **monomeric clathrin adaptor** sorting cargo between the TGN and endosomes. Its VHS
domain recognises DXXLL acidic-cluster-dileucine motifs (e.g. mannose-6-phosphate receptors);
its GAT domain binds ARF-GTP (membrane recruitment) and ubiquitin (ubiquitinated cargo); the
hinge/GAE recruits clathrin. GGA3 directs cargo to endosomes/lysosomes, mediates surface export
of receptors (ADRA2B, NTRK1), and regulates BACE1 trafficking and stability.

## Key evidence (provenance)

- [PMID:17116753]: Nedd4/GGA3 cooperate in LAPTM5 sorting to lysosome — "via interactions with
  GGA3 and cargo (LAPTM5), regulates cargo trafficking to the lysosome without requiring cargo
  ubiquitination." Basis for GO:0140312 cargo adaptor activity (core), GO:0043130 ubiquitin
  binding, GO:0006622 protein targeting to lysosome.
- [PMID:10749927]: GGA family are ARF effectors with a gamma-adaptin "ear" domain localising to
  the TGN — basis for GO:0031267 small GTPase (ARF) binding and TGN localisation.
- [PMID:17553422, PMID:20484053]: GGA3 regulates BACE1 degradation/stability (non-core, disease).

## Annotation landscape (GOA, 65 rows)

- Core MF: GO:0140312 cargo adaptor activity; companions GO:0031267 small GTPase binding (ARF),
  GO:0043130 ubiquitin binding. Core locations: TGN, Golgi, early/endosome membrane.
- 19 bare protein-binding IPI rows -> REMOVE per policy (interactome; ARF/ubiquitin/cargo captured
  by specific MF terms). BACE1/amyloid, recycling, surface-export rows -> KEEP_AS_NON_CORE.
