# aceE (P0AFG8) curation notes

Curated by Claude (AI-assisted), 2026-11-11, as the experimental E. coli exemplar for the PDH E1
annoton of `modules/bacterial_pyruvate_metabolism.yaml`.

Deep research was not run in this session (no `-deep-research-*.md` file); the review rests on the
cached abstracts and the Swiss-Prot record.

- E1p is a ThDP-dependent homodimer with two active centres at the subunit interface
  [PMID:11955070 "The functional dimer contains two catalytic centers located at the interface between subunits."].
- His-407 inner-loop residue is needed for reductive acetylation of E2p
  [PMID:17635929 "We showed that residue His-407 on the inner loop has a key role in the mechanism, especially in the reductive acetylation of the E. coli dihydrolipoamide transacetylase component"].
- A covalent pre-decarboxylation intermediate analogue (PLThDP) orders two active-site loops
  [PMID:16531404 "the presence of PLThDP induces large scale conformational changes in the enzyme"].
- The 15+1 bare protein-binding rows (high-throughput) are removed under the protein-binding policy.
- GO:0060090 molecular adaptor activity (EXP, PMID:11955070) is flagged as over-annotation; the
  abstract describes a catalytic E1, and E2-binding is part of the E1 reaction.
- The HDA membrane row is flagged; the PDH complex is soluble.
