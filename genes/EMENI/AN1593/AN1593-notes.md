## 2026-10-24

Reviewed EMENI/AN1593 in `PTHR10572` after `just fetch-gene EMENI AN1593`.
Falcon deep research was not available because the local API credentials are not
configured, so this review used the cached UniProt record, GOA rows, PAINT cache,
full text for PMID:22506079, and a manual web/literature sweep.

### Literature

- The key direct paper is Bromann et al. 2012. It identifies an A. nidulans
  PbcR-activated eight-gene diterpene cluster from `AN1592.4` to `AN1599.4`,
  reports that pbcR overexpression strongly upregulated the cluster HMGR
  `AN1593.4`, and proposes that AN1593 provides mevalonate-derived isoprenoid
  precursors for ent-pimara-8(14),15-diene biosynthesis
  [PMID:22506079, "The highly upregulated genes were homologous to GGPP synthase;
  AN1592.4 (307,000-fold), HMG-CoA reductase; AN1593.4 (12,000-fold), diterpene
  synthase; AN1594.4 (21,700-fold)"; PMID:22506079, "Based on the data presented
  here, we suggest a model for ent-pimara-8(14),15-diene biosynthesis in
  Aspergillus nidulans. Specifically, HMG-CoA reductase (AN1593.4) functions in
  the mevalonate pathway, which produces isoprenoid precursors."].
- Bromann et al. 2016 was checked because UniProt cites it, but the cached record
  is abstract-only and mainly describes using A. nidulans as a heterologous
  monoterpene/diterpene host while referring back to the previously identified
  pbcR cluster [PMID:27098256, "Previously, we identified a novel diterpene gene
  cluster in A. nidulans and showed that overexpression of the cluster-specific
  transcription factor (pbcR) led to ent-pimara-8(14),15-diene (PD) production."].

### PAINT alignment

- Keep `GO:0004420` and broad `GO:0008299` from `PTN000060346`. AN1593 is a
  short HMGR, but it retains NCBIfam/PROSITE HMG-CoA reductase signatures and
  the annotated catalytic residues that argue against a pseudokinase-like loss
  of the catalytic domain.
- Remove the housekeeping-HMGR placements. `PTN000060347` places ER and
  peroxisomal membrane on long canonical HMG-CoA reductases, while AN1593 lacks
  the N-terminal sterol-sensing membrane region and the UniProt single-pass TM
  prediction overlaps the catalytic fold. `PTN000832055` is the fungal ergosterol
  node and belongs on the long sterol-pathway paralogs, not this
  pimaradiene-cluster paralog.
- Retain the two AspGD `GO:0019748 secondary metabolic process` rows. They are
  broad, but the pbcR overexpression evidence places AN1593.4 in a secondary
  diterpene cluster rather than in housekeeping sterol synthesis.
- Reviewer follow-up: added `source_defects` for UniProt's likely spurious
  single-pass membrane prediction; removed `membrane` from the core function;
  added Bromann et al. 2016 to `references`; added AN1593/PTHR10572 family
  exceptions for ER membrane and ergosterol biosynthesis.
