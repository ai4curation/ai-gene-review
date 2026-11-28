# TRPV4 human review notes

## Session 1

- `just fetch-gene human TRPV4` resolved UniProt Q9HBA0 and seeded 142 GOA rows.
- `just paint-losses human TRPV4` reported no IRD or IKR loss on the TRPV4 lineage.
- `just deep-research-falcon human TRPV4 --fallback perplexity-lite` failed because
  the Falcon and Perplexity providers were not available in this environment. Manual
  synthesis is in `TRPV4-deep-research-manual.md`.
- Rat Trpv4 already had a merged review, so the human row decisions were aligned to
  the established rat calls where the same term and evidence source applied:
  calcium-channel and osmosensory terms are core; inherited actin/microtubule
  rows are real but peripheral; mouse adipocyte chemokine/ERK/JNK outputs are
  non-core; organismal diet/glucose/energy phenotypes are downstream
  over-annotations.

### Main decisions

- Core functions: `GO:0005262` calcium channel activity, directly involved in
  `GO:0098703` calcium ion import across plasma membrane; and `GO:0005034`
  osmosensor activity, directly involved in osmosensory signaling and cellular
  hypotonic response.
- `GO:0015275` stretch-activated, monoatomic cation-selective, calcium channel
  activity was accepted for the TRPV4 mechano-osmotic gating mode. Per the
  mechanosensation evidence guide and issue #7187, this asserts that TRPV4 is a
  stretch-activated cation channel that conducts Ca2+, not that it is selective
  for Ca2+.
- `GO:0009612` response to mechanical stimulus was kept as non-core from
  PMID:15753126. Human TRPV4 is sufficient for high-viscosity-evoked cation
  currents in HeLa cells, but the paper does not by itself establish a stronger
  mechanical-detection BP or purified force-from-lipids channel gating.
- The generic transport/process parents (`GO:0006811`, `GO:0006816`,
  `GO:0070509`, `GO:0070588`, `GO:0055085`, `GO:1902656`) were modified to
  `GO:0098703`.
- `GO:0006971` hypotonic response was modified to `GO:0071476` cellular
  hypotonic response, and `GO:0071477` cellular hypotonic salinity response was
  generalized to `GO:0071476`.
- `GO:0009986` cell surface and `GO:0016020` membrane were modified to
  `GO:0005886` plasma membrane.
- The inherited focal adhesion rows were marked over-annotated: the rat
  cytoskeleton paper describes actin-rich structures that resemble focal
  adhesions, not a focal-adhesion marker.
- The three bare `GO:0005515` protein binding rows, for AQP4 and DDX3X, were
  removed per the protein-binding policy. Both interactions are real regulatory
  contexts but do not define a more specific TRPV4 molecular function.
- `GO:0045989` positive regulation of striated muscle contraction and
  `GO:0097497` blood vessel endothelial cell delamination were left
  `UNDECIDED`: the accessible evidence does not substantiate those exact
  process terms.
