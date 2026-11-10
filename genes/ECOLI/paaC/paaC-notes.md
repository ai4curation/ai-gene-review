# paaC (E. coli K-12) notes

## Deep research

`just deep-research ECOLI paaC --provider falcon` was attempted once (2026-10-23) and failed
("Exception: Failed to authenticate"); perplexity/openai keys are not configured. No
deep-research file exists; the review is built from cached primary literature.

## Key sources (all cached in publications/)

- PMID:21247899 (Grishin et al. 2011, E. coli K-12; full text): reconstitution, (PaaAC)2 structure,
  PaaE cofactors. [PMID:21247899 "In vitro reconstitution of the oxygenase subunits showed that each of the PaaA, B, C, and E subunits are necessary for catalysis, whereas PaaD is not essential."]
- PMID:20660314 (Teufel et al. 2010; full text): product is ring 1,2-epoxyphenylacetyl-CoA. Note the
  oxygenase biochemistry used Pseudomonas sp. Y2 PaaABC(D)E, not the E. coli proteins.
  [PMID:20660314 "PaaABC(D)E thus functions as a ring 1,2-phenylacetyl-CoA epoxidase."]
- PMID:16997993 (Fernandez et al. 2006, E. coli W; full text): per-gene deletions/complementation.
- PMID:9748275 (Ferrandez et al. 1998; abstract only): paa cluster; IMP rows deferred to curator.
- PMID:20823522 (Grishin et al. 2010): PaaAC crystallization (fetched in this session).

## Gene-specific

- Structural beta subunit, PaaA paralog (17% identity), no tunnel/ligand/metal site.
- Three GO:0005515 rows REMOVED per policy (PaaA, PaaB; DpiA from Y2H screen PMID:24561554).
- IDA cytosol (PMID:17309111, abstract-only membrane proteomics) ACCEPTED, deferring to curator.
- NEW: contributes_to GO:0097266 (IDA, PMID:21247899).
