# MYC notes

This file was created during the ORIGINS_OF_MULTICELLULARITY pass. Automated
deep research was not run for this section; the existing review drew on
`MYC-deep-research-falcon.md`. Every source below was PubMed-verified, fetched
with `just fetch-pmid`, and read in its cached full text.

## Premetazoan origin (ORIGINS_OF_MULTICELLULARITY, 2026-10-01)

### Evidence

- **Choanoflagellate Myc and Max (Monosiga brevicollis), biochemistry.**
  Young et al. 2011 (PMID:21571926):
  - [PMID:21571926 "We find that Myc and Max from M. brevicollis heterodimerize and bind to both canonical and noncanonical E-boxes"]
  - [PMID:21571926 "MbMyc in most cells was concentrated in the nucleus"]
  - Their conclusion: [PMID:21571926 "core features of metazoan Myc function, including heterodimerization with Max, binding to E-box sequences in DNA, and localization to the nucleus, predate the origin of metazoans"]
  - The partner interface has diverged: [PMID:21571926 "cross-species dimerization between Mb and human Myc and Max proteins was not observed"], and [PMID:21571926 "we have been unable to detect any biological or transcriptional activity of MbMyc or MbMax in mammalian cells"].
  - N-terminal Myc boxes: [PMID:21571926 "MBI and MBIV were not detected in either MbMyc or C. owczarzaki Myc"]; [PMID:21571926 "Like MBII, the MBIII domain is conserved from vertebrates to sponges to C. owczarzaki"]. MBI contains the T58/S62 phosphodegron that FBXW7 recognises in human MYC, so this layer of MYC turnover control has no detectable counterpart in the unicellular homologs.
  - Antagonists: [PMID:21571926 "M. brevicollis contains homologs of Myc and Max but seemingly lacks the Max-binding partners Mxd or Mnt"]. The authors speculate that [PMID:21571926 "the regulation of critical cellular processes like apoptosis, growth, and proliferation that are under the auspices of bilaterian Myc proteins are not part of MbMyc function"] (stated as one possibility, not tested).
- **Ribosome biogenesis regulon (computational).** Brown, Cole & Erives 2008 (PMID:18816399):
  [PMID:18816399 "a distinct mode of RiBi regulation co-evolved with the E(CG)-binding, Myc:Max bHLH heterodimer complex in a stem-holozoan"];
  the regulon [PMID:18816399 "has primordial roots in the evolution of an inducible growth regime in a protozoan ancestor of animals"].
  Loss tracks Myc loss: [PMID:18816399 "this holozoan RiBi promoter signature is absent in nematode genomes, which have not only secondarily lost Myc"].
  Young et al. cite this as a prediction only: [PMID:21571926 "A previous survey of the M. brevicollis genome predicted the presence of Myc-binding sites upstream of ribosome biogenesis genes, suggesting that MbMyc might regulate their transcription"].
- **Capsaspora repertoire.** Sebé-Pedrós et al. 2011 (PMID:21087945):
  [PMID:21087945 "Our data reveals that a basic Myc, MAX, Mxd/Mnt network of bHLH TFs was already present in the common ancestor of metazoans and Capsaspora"];
  [PMID:21087945 "Interestingly, Capsaspora bHLH proteins are all homologs of those implicated in cell cycle and metabolism and none of those are involved in differentiation"].
- **Capsaspora regulatory genome.** Sebé-Pedrós et al. 2016 (PMID:27114036). A Myc-like motif enriched in ATAC-seq sites
  [PMID:27114036 "appears to be strongly associated with regulatory sites that show higher ATAC-seq signal in the filopodial stage"]
  (the proliferative stage), and [PMID:27114036 "Moreover, Myc regulates genes mainly involved in ribosome biogenesis and translation (Figure 6O), similar to what is known for animal Myc networks"].
  Caveat: this is motif inference, not ChIP, and is stated as conditional: [PMID:27114036 "Assuming that the motifs represent the consensus motifs for these Capsaspora orthologs"].
  Authors' synthesis: [PMID:27114036 "These findings suggest that core downstream target networks of some developmental TF evolved long before the advent of animal multicellularity"].
- **Early-branching animal comparator (Hydra).** Hartl et al. 2010 (PMID:20142507):
  [PMID:20142507 "A recombinant Hydra Myc/Max complex binds to the consensus DNA sequence CACGTG with high affinity"];
  [PMID:20142507 "Hydra myc is specifically activated in all stem cells and nematoblast nests"];
  Hydra Myc alone is weak in transformation assays ([PMID:20142507 "Hydra Myc1 induced only a marginal increase in cell proliferation"]),
  but [PMID:20142507 "Hybrid proteins composed of segments from the retroviral v-Myc oncoprotein and the Hydra Myc protein display oncogenic potential in cell transformation assays"].

### Classification of the core functions in the existing review

| Core function (review) | Call | Basis |
|---|---|---|
| DNA-binding TF activity as a MAX heterodimer (GO:0000981; Myc-Max complex GO:0071943) | **Ancestral** (at least Choanozoa; Filozoa by gene content) | MbMyc-MbMax heterodimer binds E-boxes and MbMyc is nuclear (PMID:21571926); Capsaspora has Myc, Max, Mnt (PMID:21087945). Transactivation by a unicellular Myc has not been shown directly. |
| E-box binding (GO:0070888) | **Ancestral** | CACGTG and non-canonical E-box binding by MbMyc-MbMax (PMID:21571926); Hydra Myc-Max binds CACGTG (PMID:20142507) |
| Protein dimerization with MAX (GO:0046983) | **Ancestral**, with a lineage-specific interface | Heterodimerization in M. brevicollis, but no cross-species dimerization with human proteins (PMID:21571926) |
| Growth control via ribosome biogenesis genes (in description; not a separate core function) | **Ancestral (inferred; not directly tested)** | E-box RiBi promoter signature in Monosiga (PMID:18816399); Myc-like motif sites at ribosome biogenesis and translation genes in Capsaspora (PMID:27114036) |
| Positive regulation of cell population proliferation; apoptosis; developmental and tissue-specific roles; oncogenic transformation | **Animal-specific as far as documented; unresolved for proliferation** | Stem-cell and proliferating-cell expression first documented in Hydra (PMID:20142507). No proliferation, apoptosis or knockout phenotype reported for any unicellular holozoan Myc. Monosiga lacks Mxd/Mnt (PMID:21571926). Hydra Myc1 alone is barely transforming (PMID:20142507). |
| Repression via MIZ1 (ZBTB17); FBXW7/MBI phosphodegron control | **Unresolved / likely animal-specific** | MBI (holding the T58/S62 degron) is not detected in MbMyc or Capsaspora Myc (PMID:21571926). No unicellular data on MIZ1-type partners found. |

Bottom line: the biochemical core (Max heterodimer, E-box binding, nuclear
transcription factor) is ancestral to choanoflagellates and animals. Regulating
ribosome biogenesis genes is the best-supported candidate for the ancestral
output, but the evidence is computational (promoter motifs, ATAC motif
enrichment). The proliferation, apoptosis, stem-cell and oncogenic roles are
documented only in animals. None of the existing review actions changes.

### Track C (IBA nodes and unicellular holozoans), queried 2026-10-01

QuickGO `annotation/search?withFrom=PANTHER:<PTN>&taxonId=<T>&taxonUsage=descendants`
for T = 28009 (Choanoflagellata), 2687318 (Filasterea), 127916 (Ichthyosporea).

| Node | Human IBA terms | Choanoflagellata | Filasterea | Ichthyosporea |
|---|---|---|---|---|
| PTN001691821 | GO:0000978, GO:0000981, GO:0006357 | 4 rows, all on M. brevicollis MbMyc (A9V5B4): GO:0000978, GO:0000981, GO:0006357, GO:0005634 (is_active_in nucleus) | 0 | 0 |
| PTN002912196 | GO:0008284 positive regulation of cell population proliferation | 0 | 0 | 0 |

- The terms that reach MbMyc are all transcription-factor and nuclear terms,
  which match the experimental data on MbMyc (PMID:21571926). No animal
  tissue, organ or developmental process term reaches a unicellular organism.
- PTN002912196 (proliferation) is placed on a vertebrate-only node. All 58 of
  its GOA rows, without a taxon filter, are on vertebrate taxa. That placement
  agrees with the absence of evidence for a proliferative role outside animals.
- Capsaspora has no Myc rows from either node. Capsaspora is not a PANTHER
  reference genome, so it gets no IBA rows; TreeGrafter IEAs were not checked here.
