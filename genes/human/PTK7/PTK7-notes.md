# PTK7 (human, Q13308) curation notes

Deep research providers were unavailable in this environment (falcon/perplexity-lite both failed);
findings below come from cached publications and the UniProt record.

## Pseudokinase
- [PMID:24107129 "they do not bind ATP"] — PTK7 is listed among pseudokinases that are not
  catalytically active and do not bind ATP; UniProt: "Inactive tyrosine kinase involved in the Wnt
  signaling pathway", "Does not bind ATP (PubMed:24107129, PubMed:32619402)".
- Consequence: the InterPro-derived `GO:0004672 protein kinase activity` IEA was REMOVEd; the NOT
  `GO:0005524 ATP binding` row was accepted.

## Localization
- Single-pass type I membrane protein, Cell membrane and Cell junction (UniProt, from
  PubMed:20837484); "Colocalizes with MMP14 at cell junctions. Also localizes at the leading edge of
  migrating cells."
- Focal-adhesion proteome hit [PMID:21423176] kept as non-core.
- Benchmark conclusion: plasma membrane, seven Ig-like domains extracellular and accessible; the
  ectodomain is shed by MT1-MMP [PMID:20837484 "MT1-MMP directly cleaves the exposed PKP(621)↓LI
  sequence of the seventh Ig-like domain of the full-length membrane PTK7"].

## Function
- Canonical Wnt: [PMID:21132015 "PTK7-deficient cells exhibit weakened β-catenin/T-cell factor
  transcriptional activity on Wnt3a stimulation."] and "PTK7 functions upstream from glycogen
  synthase kinase 3".
- Non-canonical Wnt/PCP: UniProt FUNCTION; convergent-extension defects in zebrafish on perturbing
  the MT1-MMP/PTK7 balance [PMID:20837484].
- Neuronal IBA terms (axon, neuronal cell body, synapse organization, axon guidance receptor
  activity) kept as non-core: the node is supported by Drosophila otk and rat data, but these are
  context-specific for the human protein.
- `GO:0007165 signal transduction` and `GO:0016020 membrane` modified to the specific Wnt-pathway and
  plasma-membrane terms; `GO:0070161 anchoring junction` modified to `GO:0005911 cell-cell junction`.
- Generic `GO:0005515` rows removed per the protein-binding policy (CTNNB1 interaction is captured by
  the Wnt process terms).
