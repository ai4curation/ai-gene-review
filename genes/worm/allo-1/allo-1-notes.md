# allo-1 (R102.5; UniProt Q9U389) review notes

## Deep research status
`just deep-research-falcon worm allo-1 --fallback perplexity-lite` failed on 2026-10-08 (falcon timeout; perplexity unavailable). No deep-research file was created. The review is based on the UniProt record, cached publications and PubMed searches.

## Key findings
- ALLO-1 is the allophagy receptor and binds LGG-1 through its LIR [PMID:29255173 "ALLO-1 is essential for autophagosome formation around paternal organelles and directly binds to the worm LC3 homologue LGG-1 through its LC3-interacting region (LIR) motif."]. The 2018 paper is abstract-only in the cache.
- IKKE-1 binds and phosphorylates ALLO-1 [PMID:29255173 "IKKE-1 interacts with ALLO-1, and the IKKE-1-dependent phosphorylation of ALLO-1 is important for paternal organelle clearance."]
- The two isoforms prefer different cargo. ALLO-1b (Q9U389-1, the canonical UniProt isoform) mainly targets paternal mitochondria; ALLO-1a (Q9U389-2) mainly targets membranous organelles [PMID:38368448 "In contrast to ALLO-1a, the expression of GFP-ALLO-1b efficiently rescued the defective degradation of paternal mitochondria"]
- ALLO-1 recruits the ULK complex (UNC-51, EPG-7) to the cargo [PMID:38368448 "indicating that ALLO-1 is required for recruitment of the ULK complex around cargo"]
- The ALLO-1a C-terminus is a parallel coiled-coil that binds K48/K63 polyubiquitin [PMID:41234204] (abstract only).

## Curation decisions
- Core MF: GO:0160247 autophagy cargo adaptor activity, which matches the module annotation.
- NEW: mitophagy (GO:0000423). The comparator check passes (FUNDC1, BNIP3 in GO:0000423; OPTN in GO:0061734).
- The HDA muscle-localizome locations (ER, sarcomere, dense body) [PMID:21611156] come from a large-scale GFP survey in a tissue where ALLO-1 has no known function. They are kept as non-core.
- Protein binding: the LGG-1 row is modified to the cargo adaptor term; the IKKE-1 (substrate) and TRPP-3 (Y2H) rows are removed.
- Possible future NEW: polyubiquitin modification-dependent protein binding (GO:0031593) for ALLO-1a, from PMID:41234204, once the full text is available.
