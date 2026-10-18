---
title: "TreeGrafter on Unicellular Holozoans: Hippo Pathway Case Study"
autolink_gene_symbols: false
---
# TreeGrafter on Unicellular Holozoans: Hippo Pathway Case Study

[← back to TreeGrafter Inference Evaluation](../TREEGRAFTER.md)

> **In the main-page tables since the 2026-10-03 refresh.** These rows come
> from reviews added on 2026-09-30 and 2026-10-01 for the
> [Origins of Animal Multicellularity](../ORIGINS_OF_MULTICELLULARITY.md)
> project. They were not in the 2026-10-01 tables; at the 2026-10-03 refresh
> (`f81b9f300`) the sidecars on the main page include 65 TreeGrafter rows from
> *S. rosetta*, *Capsaspora* and *Oscarella* review files, 41 of them
> down-graded, and the failure-mode table classifies each down-graded row. The full audit,
> with a script that regenerates its tables, is the
> [propagation audit](../ORIGINS_OF_MULTICELLULARITY/propagation-audit.md).

**Bottom line:** choanoflagellates (*Salpingoeca rosetta*), *Capsaspora* and
sponges are not PANTHER reference genomes, so every tree-based GO annotation
they carry is a TreeGrafter IEA (`GO_REF:0000118`). The main TreeGrafter
sidecars now include the 65 live `GO_REF:0000118` rows from reviewed
*S. rosetta*, *Capsaspora* and *Oscarella* proteins, 41 of them down-graded.
The broader Origins propagation audit also scored 101 propagated rows: 53 in
literature-selected reviews and 48 in targeted follow-ups, the latter including
*M. brevicollis* IBA controls outside the TreeGrafter-only denominator. Together
they show the main page's failure modes in a new setting: genes from lineages
that the reference trees sample thinly.

| Case | Protein | Graft | Failure mode (main page numbering) | Rows down-graded |
|---|---|---|---|---|
| Warts grafted with citron/ROCK kinases | *Capsaspora* coWts, A0A0D2VGR4 | PTHR22988:SF71, node PTN001122925 | **4, mis-placement** (across families, not just within a superfamily) | cytoskeleton (over-annotated); actomyosin structure organization (removed). Also missed `hippo signaling` from the LATS node |
| Yorkie grafted with MAGI-related scaffolds | *S. rosetta* yorkie, F2UDK1 | PTHR10316:SF68, node PTN002569196 (ecdysozoan) | **4, mis-placement**; terms happened to be harmless | none (cytoplasm and signal transduction kept as non-core) |
| Animal-tissue IBDs inherited at a correct graft | *S. rosetta* warts, F2U943 | PTHR24356:SF418, leaf PTN001220369 under PTN002390470 | **inherited PAINT over-placement**, like the [rotary-ATPase leak](rotary-atpase-leak.md) | regulation of organ growth (removed); positive regulation of apoptotic process and G1/S transition (over-annotated) |
| Fungal pathway term on a choanoflagellate | *S. rosetta* couscous, F2UJ78 | node PTN001270341 (MNN2 family) | **3, out-of-context process** (pathway absent in host) | mannan biosynthetic process (removed) |
| Family node term | sponge TLN, A0A3G2LGI8 | node PTN001072690 | **1, granularity / sibling term** | cell-cell adhesion → cell-matrix adhesion |
| Graft onto a node PAINT restricts to Bilateria | three *S. rosetta* cadherins: F2UD23, F2UFV3, F2USU1 | PTHR24027:SF422, node PTN000616280 (`taxon:33213`) | **4-like, taxon-blind graft** | 30 current rows, ten on each of three *S. rosetta* cadherin gene reviews; none of the proteins has the beta-catenin-binding domain (PF01049). See the audit for the node-level spread check |
| Graft onto the vertebrate ITGBL1 node | *Capsaspora* integrin beta 2 (coITGB2, A0A0D2WRB3) and five other *Capsaspora* integrin-beta entries | PTHR10082:SF3, node PTN002560695 (Euteleostomi) | **4, mis-placement onto an animal-only node** | focal adhesion and cell-cell adhesion (over-annotated); cell-matrix adhesion → cell-substrate adhesion |
| Developmental term from an all-animal T-box node | *Capsaspora* Brachyury (CoBra, A0A0D2VUC6) | PTHR11267, node PTN000137774 (duplication node; 34 leaf organisms, all animals) | **3, out-of-context process** | cell fate specification (removed) |

## What is new relative to the main evaluation

1. **Placement errors here cross family boundaries.** The main page's mode-4
   cases are within-superfamily mis-placements, such as MDH grafted onto the
   L-LDH subfamily. Here, a LATS/Warts kinase lands in the citron/ROCK family,
   and a Yorkie candidate lands in the MAGI-related family.

   The Warts case points to a specific cause. UniProt's PANTHER classification
   also puts Drosophila wts (Q9VA38) in PTHR22988. But fly wts is a leaf of the
   reference tree, so its IBA rows come from the LATS node PTN002390470 in
   PTHR24356, and they are correct. Our working hypothesis is that the family
   HMMs prefer PTHR22988 for some Warts sequences. Reference proteomes are
   protected by their tree position; non-reference proteomes are grafted by
   the HMM call. *S. rosetta* Warts (F2U943) does classify into PTHR24356, so
   the effect is sequence-dependent. A rescoring test is listed below.

2. **A correct graft can still carry wrong terms when an IBD sits above a
   lineage split.** The four IBDs on PTN002390470 (hippo signaling, organ
   growth, apoptosis, G1/S) apply to a node that includes the
   choanoflagellate leaves. *M. brevicollis* (a reference genome) receives
   them as IBA; *S. rosetta* receives them through TreeGrafter.
   - Regulation of organ growth is the clearest error: choanoflagellates have
     no organs, and GO's taxon constraints do not catch it.
   - Hippo signaling at the same node is supported by the *Capsaspora* data.

   So the node is right for the pathway term and too deep for the tissue
   terms. This is the same shape as the rotary-ATPase leak, where an IBD on a
   duplication node reaches paralogs that do not share the function.

3. **Conserved signalling terms transfer well.** The three TreeGrafter rows on
   *Capsaspora* Yorkie (coYki) were all accepted, and the knockout and
   heterologous data support each one: coactivator activity, hippo signaling,
   and positive regulation of transcription by RNA polymerase II.

4. **TreeGrafter grafts onto taxon-restricted nodes, repeatedly.** PAINT records cadherin
   node PTN000616280 at Bilateria (`taxon:33213`), yet three choanoflagellate
   cadherins graft onto it and inherit its adherens-junction and catenin
   terms ([audit, Case 6](../ORIGINS_OF_MULTICELLULARITY/propagation-audit.md)).
   The main evaluation never tested this, because its corpus is
   bacterial-heavy. Two more cases followed. *Capsaspora* integrin betas
   graft onto the Euteleostomi ITGBL1 node, and *Capsaspora* T-box factors
   graft onto an all-animal T-box node that carries "cell fate specification"
   ([audit, Cases 7 and 8](../ORIGINS_OF_MULTICELLULARITY/propagation-audit.md)).
   With three of five graft errors in this corpus of the same kind, a cheap QC
   rule would pay off: suppress terms from a graft node whose PAINT taxon does
   not include the query organism.

## Where the findings are recorded

Each down-graded row carries a `propagation_review` in its gene review YAML,
naming the PANTHER source node with a `source_status`:

- [`genes/CAPO3/coWts/coWts-ai-review.yaml`](../../genes/CAPO3/coWts/coWts-ai-review.yaml)
- [`genes/SALRS/warts/warts-ai-review.yaml`](../../genes/SALRS/warts/warts-ai-review.yaml)
- [`genes/SALRS/yorkie/yorkie-ai-review.yaml`](../../genes/SALRS/yorkie/yorkie-ai-review.yaml)
- [`genes/SALRS/couscous/couscous-ai-review.yaml`](../../genes/SALRS/couscous/couscous-ai-review.yaml)
- [`genes/OSCPE/TLN/TLN-ai-review.yaml`](../../genes/OSCPE/TLN/TLN-ai-review.yaml)
- [`genes/CAPO3/CoBra/CoBra-ai-review.yaml`](../../genes/CAPO3/CoBra/CoBra-ai-review.yaml)
- [`genes/CAPO3/coITGB2/coITGB2-ai-review.yaml`](../../genes/CAPO3/coITGB2/coITGB2-ai-review.yaml)

The choanoflagellate cadherin graft and the *M. brevicollis* LATS IBAs are
recorded in reviews of those proteins (under `genes/SALRS/` and
`genes/MONBE/`).
