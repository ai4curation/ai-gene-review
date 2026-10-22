# Dnmt3l (mouse, Q9CWR8) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Dnmt3l is the experimental donor (1:1 ortholog, PANTHER PTHR23068:SF13, DNMT3L
non-catalytic branch) for most ISS/IEA rows on human DNMT3L (Q9UJW3), and a donor at the IBA node
PTN001891074 (DNMT3L clade, enzyme activator activity). No ProtNLM2 files were opened or used.

### Deep research

`just deep-research-falcon mouse Dnmt3l --fallback perplexity-lite` failed. Falcon gave
"Exception: Failed to authenticate", and the perplexity-lite fallback returned HTTP 401
insufficient_quota. No deep-research file exists. The review is built from the cached
publications (`just fetch-gene-pmids`, 15/15 cached, plus PMID:11719692 and PMID:15671018), the
UniProt record, Reactome entries, and the human DNMT3L review for cross-species consistency.

### What is experimentally established in mouse (vs inferred)

Established with mouse protein or mouse genetics:
- No catalytic activity; catalytic motifs lost [PMID:11719692 "The key catalytic motifs characteristic of DNA cytosine methyltransferases have been lost from Dnmt3L"].
- Activates Dnmt3a/Dnmt3b by binding their catalytic domains via its C-terminal domain; about 15-fold
  stimulation; acts as a substrate exchange factor [PMID:15671018 "Dnmt3L stimulates the catalytic activity of the Dnmt3A and Dnmt3B enzymes by directly binding to their respective catalytic domains via its own C-terminal domain"]. UniProt cites this paper as ECO:0000269 for Q9CWR8.
- Endogenous tagged Dnmt3L co-purifies with DNMT3A2, DNMT3B and the four core histones in ES cells
  [PMID:17687327]; Dnmt3L co-purifies with Dnmt3a/3b from ES cells [PMID:17938196].
- Maternal imprint establishment in oocytes [PMID:11719692, PMID:11934864, PMID:16920095, PMID:22723905].
- De novo methylation and silencing of LTR and non-LTR retrotransposons in perinatal prospermatogonia
  [PMID:15318244 "Deletion of the Dnmt3L gene prevented the de novo methylation of both long-terminal-repeat (LTR) and non-LTR retrotransposons"];
  corroborated by RNA-seq [PMID:25503965]. Co-purifies with SPOCD1 in fetal testis (piRNA pathway) [PMID:32674113].
- ESC roles: gene-body methylation (positive), protection of bivalent promoters via EZH2/PRC2
  (negative), ESC-to-PGC differentiation via Rhox5 [PMID:24074865].

Inferred by orthology (human or heterologous data):
- H3K4me0 specificity and the ADD-domain binding site (co-crystal on human DNMT3L) [PMID:17687327];
  the Dnmt3a-Dnmt3L heterotetramer structure (human DNMT3L C-terminal domain) [PMID:17713477].
- HDAC1 binding and HDAC-dependent repression [PMID:12202768]. The abstract does not state the species of the constructs; the
  mouse rows are ISS/ISO from human.

### Key decisions
- Accepted as core: enzyme activator activity (IBA/IDA/ISO/IEA), genomic and autosome imprinting, and
  TE silencing (heterochromatin and piRNA-directed). Added NEW GO:0140006 histone H3 reader activity, as in
  the human review, noting that the binding specificity comes from human/structural data.
- Removed: male meiosis I (the abstract states that spermatocytes do not express Dnmt3L, so this is
  downstream); post-embryonic development (ectopic-overexpression transgene; KO mice develop normally).
- Over-annotated: placenta development, chorionic trophoblast differentiation, and epigenetic programming of
  the female pronucleus. These are maternal-effect consequences in the next generation, or zygotic processes
  after Dnmt3l has acted in the oocyte. Generic gene expression (knockdown screen).
- Protein binding: Dnmt3a/Dnmt3b rows changed (MODIFY) to enzyme activator activity; EZH2 and SPOCD1 rows removed
  under the policy (their biology is captured by the PRC2 colocalization and piRNA rows).
- Enzyme binding changed (MODIFY) to histone deacetylase binding; catalytic complex changed (MODIFY) to DNA methyltransferase
  complex (both match the human review).
- IBA rows from the DNMT3 node PTN002747444 (cytoplasm, negative regulation of transcription) are kept as
  non-core. PAINT placed only enzyme activator activity at the DNMT3L-specific node PTN001891074, and none of
  DNMT3A's catalytic terms. That omission is consistent with the loss of the catalytic motifs and is treated
  as deliberate.
