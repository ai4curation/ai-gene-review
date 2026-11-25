# ric-3 notes

## 2026-11-21

- Fetched `worm/ric-3` with UniProt Q22472, cached the WormBase hand-written
  MOD description, and checked PAINT: `just paint-losses worm ric-3` reported
  no IRD or IKR loss on this gene's lineage.
- `just fetch-gene-pmids worm ric-3` cached all five GOA PMID sources.
  `PMID:15932871`, `PMID:16466809` and `PMID:19899809` are abstract-only
  locally; `PMID:11867529` and `PMID:20027209` are full text.
- Deep research was attempted with `just deep-research-falcon worm ric-3
  --fallback perplexity-lite`, but both providers were unavailable in this
  environment. The review therefore used the cached primary papers, the
  WormBase MOD description, UniProt, and the local PTHR21723 RIC-3 family
  slice.
- RIC-3 is an ER-membrane nicotinic acetylcholine receptor maturation factor.
  Halevi et al. showed that RIC-3 is "specifically required for the maturation
  of acetylcholine receptors" [PMID:11867529, "Together, these data suggest
  that RIC-3 is specifically required for the maturation of acetylcholine
  receptors"]. Ben-Ami et al. then localized the key DEG-3/DES-2 determinant
  to RIC-3's transmembrane domains [PMID:15932871, "the effects of RIC-3 on
  functional expression and on receptor properties are mediated by the
  transmembrane domains"], and Cohen Ben-Ami et al. mapped conserved
  second-transmembrane residues needed for interactions with DEG-3/DES-2 and
  ACR-16 [PMID:19899809, "conserved residues in the second RIC-3
  transmembrane domain are needed for its interactions"].
- The positive cholinergic-transmission and protein-localization rows are
  both treated as core outputs of the same ER activity: ric-3 mutants retain
  DEG-3 in cell bodies rather than processes, and a separate live-labeling
  assay found that ric-3 mutations "strongly reduce or even abolish nAChR cell
  surface expression" [PMID:16466809].
- RIC-3 is also needed for the neuronal ACR-2 receptor. The ACR-2R
  reconstitution paper showed that ric-3; acr-2(n2420gf) double mutants have a
  dramatically lower convulsion frequency, and that adding `acr-3` to the
  `acr-2`, `acr-12`, `unc-38`, `unc-63`, `unc-50`, `unc-74`, `ric-3` oocyte
  injection mix gave robust acetylcholine-gated current [PMID:20027209, "When
  the acr-3 cRNA was added to the previous injection mix, robust expression of
  an acetylcholine-gated ion channel was observed"].
- The direct `GO:0043005 neuron projection` row was kept as non-core after
  refreshing Halevi et al. to full text: functional RIC-3::GFP is strongest in
  neuronal somata, but weak signal is also visible in the ventral cord and
  nerve ring. The PAINT `GO:0043005` row was still marked over-annotated
  because its `is_active_in` qualifier overstates this weak direct location as
  the function-bearing compartment of RIC-3-family chaperone activity; the
  supported active RIC-3 compartment is the ER. The logical `GO:0045202
  synapse` row was marked over-annotated because the supported
  synaptic/cell-surface molecules are the nAChR clients rather than RIC-3
  itself.
- The WormBase MOD description correctly captures the core
  two-transmembrane nAChR maturation role. Its BATH-42/CUL-3 regulation
  sentence was not traced to primary literature in this pass and was left out
  of the core review.
