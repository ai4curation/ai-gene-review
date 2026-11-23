# erg8 notes

## 2026-10-17 fungal PAINT/IBA re-review

- Target: S. pombe erg8 / SPAC343.01c / UniProt Q9UT88.
- Family context: PTHR31814:SF2, fungal GHMP phosphomevalonate kinase. The accepted PAINT node
  PTN001274235 carries phosphomevalonate kinase activity and the IPP mevalonate-pathway process;
  PTN001274236 carries the fungal ergosterol-biosynthesis process.
- The peroxisome IBA comes from PTN000781523. The PTHR31814 family review marks that node
  `NEEDS_PRUNING`; I retained `REMOVE` on S. pombe erg8 and changed the propagation source from the
  Arabidopsis seed to `PANTHER:PTN000781523`.
- The only cached PMID for this review is Matsuyama et al. 2006 [PMID:16823372 "Next, we determined
  the localization of 4,431 proteins, corresponding to approximately 90% of the fission yeast
  proteome, by tagging each ORF with the yellow fluorescent protein."], and it is abstract-only.
  Therefore the high-throughput cytoplasm/cytosol calls are accepted, nucleus is kept as non-core,
  and mitochondrion is left `UNDECIDED` rather than removed.
- A fresh web search for newer direct S. pombe erg8 / SPAC343.01c / Q9UT88 functional papers did not
  find a newer gene-specific biochemical or localization paper.
