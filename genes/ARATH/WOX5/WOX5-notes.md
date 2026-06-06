# WOX5 (Arabidopsis thaliana) curation notes

UniProt: Q8H1D2 (WOX5_ARATH), AT3G11260. 182 aa. WUS-type homeobox/homeodomain
(DNA_BIND 20..84). Belongs to the WUS homeobox family. Evidence at transcript
level (PE 2).

## Core biology

- WOX5 is a homeodomain transcription factor specifically expressed in the
  quiescent center (QC) of the Arabidopsis root apical meristem
  [UniProt: "Specifically expressed in the central cells of a quiescent center
  (QC) of the root."]. During embryogenesis it marks the hypophysis-derived
  lens-shaped cell / QC lineage [UniProt DEVELOPMENTAL STAGE].
- WOX5 acts largely as a transcriptional **repressor**. It moves from the QC
  into the adjacent columella (distal) stem cells and directly represses the
  transcription factor gene CDF4
  [PMID:26028217 "the WOX5 protein moves from the root niche organizer, the
  quiescent center, into the columella stem cells, where it directly represses
  the transcription factor gene CDF4. This creates a gradient of CDF4
  transcription, which promotes differentiation opposite to the WOX5 gradient,
  allowing stem cell daughter cells to exit the stem cell state."].
- Mechanism of repression: recruitment of TPL/TPR co-repressors and the histone
  deacetylase HDA19, inducing histone deacetylation at the CDF4 regulatory
  region [PMID:26028217 "WOX5 represses CDF4 transcription by recruiting TPL/TPR
  co-repressors and the histone deacetylase HDA19, which consequently induces
  histone deacetylation at the CDF4 regulatory region."]. This supports the
  molecular functions: DNA-binding transcription repressor activity (GO:0001217)
  and transcription corepressor binding (GO:0001222); and BP negative regulation
  of transcription (GO:0045892).
- Loss of WOX5 (wox5-1) → premature differentiation of the columella/distal stem
  cells (e.g., ectopic starch granule accumulation in the DSC layer)
  [PMID:25631790 "substantial amounts of starch granules accumulated in the DSC
  layer ... suggesting that these cells underwent premature differentiation."],
  and "QC expression of WOX5 is essential for maintenance of DSC activity"
  [PMID:25631790]. Supports negative regulation of cell differentiation
  (GO:0045596) and positive regulation of stem cell population maintenance
  (GO:1902459).

## Regulation and context

- WOX5 expression is confined to the QC by the PHD-finger protein ROW1, which
  binds H3K4me3 in the WOX5 promoter and represses WOX5 in the proximal meristem
  [PMID:25631790 "ROW1 specifically binds trimethylated histone H3 lysine 4
  (H3K4me3) in the WOX5 promoter region to repress its transcription."]. wox5-1
  is epistatic to row1-3 [PMID:25631790]. ROW1 may act downstream of auxin in
  regulating WOX5.
- WOX5 expression is auxin- and turanose-inducible; a tin (WOX5 loss-of-function)
  mutant shows altered auxin homeostasis [PMID:16262712 "We found that WOX5 is
  both turanose- and auxin-inducible."; "a role for WOX5 in the root apical
  meristem as a negative trigger of IAA homeostatic mechanisms allowing the
  maintenance of a restricted area of auxin maximum"]. Treated as non-core
  (upstream/contextual regulation) → response to auxin (GO:0009733)
  KEEP_AS_NON_CORE.
- WOX5/QC sits within the SHR/SCR and PLETHORA (PLT) networks
  [PMID:29352064 "The QC and adjacent stem cells are specified by two parallel
  routes directed by the transcription factors PLETHORA (PLT) and SHORTROOT
  (SHR)/SCARECROW (SCR)."]. GIF coregulators independently control QC identity
  [PMID:29352064 "combinations of GIF mutants cause the loss of QC identity."].
  WUS is not expressed in the root; WOX5 is the root counterpart of WUS
  [PMID:25631790].

## Annotation decisions (summary)

GOA has 13 lines. Actions:
- GO:0006355 regulation of DNA-templated transcription (IBA) → ACCEPT (generic
  but correct; repressor specificity added as NEW).
- GO:0003677 DNA binding (IEA) → MODIFY → GO:0043565 sequence-specific DNA
  binding (homeodomain TF; more informative child).
- GO:0003700 DNA-binding transcription factor activity (IEA) → ACCEPT.
- GO:0005634 nucleus (IEA) → ACCEPT.
- GO:0099402 plant organ development (IEA) → MARK_AS_OVER_ANNOTATED (too broad;
  specific root meristem terms already present).
- GO:0005515 protein binding (IPI, PMID:29352064 GIF) → REMOVE (uninformative).
- GO:0005634 nucleus (ISM) → ACCEPT (duplicate).
- GO:0043565 sequence-specific DNA binding (IPI, PMID:26028217) → ACCEPT (core).
- GO:0005515 protein binding (IPI, PMID:26028217, TPL/TPR/HDA19) → REMOVE; the
  informative replacement is NEW GO:0001222 transcription corepressor binding.
- GO:1902459 positive regulation of stem cell population maintenance (IMP) →
  ACCEPT (core).
- GO:0010078 maintenance of root meristem identity (IMP) → ACCEPT (core).
- GO:0009733 response to auxin (IEP) → KEEP_AS_NON_CORE.
- GO:0003700 DNA-binding transcription factor activity (ISS) → ACCEPT (duplicate).

NEW annotations added:
- GO:0001217 DNA-binding transcription repressor activity (IDA, PMID:26028217)
- GO:0001222 transcription corepressor binding (IPI, PMID:26028217)
- GO:0045892 negative regulation of DNA-templated transcription (IDA,
  PMID:26028217)
- GO:0045596 negative regulation of cell differentiation (IMP, PMID:26028217)

## GO ID verification (no OLS MCP available; verified via web/AmiGO)

- GO:0001217 DNA-binding transcription repressor activity (generic MF; child of
  GO:0003700). Chose generic over RNA-pol-II-specific child GO:0001227 because
  plant repressor annotations conventionally use the generic term.
- GO:0001222 transcription corepressor binding (binding to a corepressor;
  distinct from GO:0001221 coregulator binding).
- GO:0045892, GO:0045596, GO:0043565, GO:0010078, GO:1902459 are standard terms;
  the latter two already present in GOA.

## Open questions / suggested experiments

- Genome-wide direct WOX5 targets (ChIP-seq / DAP-seq) in QC vs columella.
- Precise WUS-type homeodomain binding motif; monomer vs complex (e.g., with PLT).
- Requirement of WOX5 cell-to-cell movement for CDF4 repression in vivo.

## Deep research synthesis (Falcon / Edison Scientific, 2026-06-06)

The Falcon deep-research report (`file:ARATH/WOX5/WOX5-deep-research-falcon.md`)
corroborates and extends the existing review without overturning any decision:

- **Transcription factor / DNA binding** corroborated: WOX5 "binds cis-regulatory
  DNA elements and controls transcription of developmental regulators" and shows
  "WOX5 enrichment at a cis-regulatory region upstream of CDF4 containing TAAT
  motifs," supporting GO:0043565 (sequence-specific DNA binding) and GO:0003700.
- **Repressor mode** corroborated: a 1 h induction assay found 17/18 genes
  downregulated ("highlighting strong repressor activity"), reinforcing
  GO:0001217 and GO:0045892. Mechanism confirmed: "WOX5 interacts with TPL/TPR;
  via TPL/TPRs it recruits HDA19, reducing histone H3 acetylation at the CDF4
  regulatory region" → GO:0001222 transcription corepressor binding.
- **Stem cell maintenance / negative regulation of differentiation** corroborated:
  WOX5 "promotes QC mitotic quiescence and maintains the underlying columella
  stem cells (CSCs) in an undifferentiated state," and "Loss of WOX5 causes CSC
  differentiation beneath the QC and ectopic QC divisions" → GO:1902459,
  GO:0045596, GO:0010078.
- **Auxin context** corroborated (non-core): WOX5 "promotes local auxin
  biosynthesis in the QC" (WOX5–HAN–CDF4 cFFL, TAA1 output; Sharma 2024) →
  GO:0009733 KEEP_AS_NON_CORE retained.

New nuances NOT yet annotated (no verifiable GO ID in current GOA/UniProt, so left
unannotated; flagged for follow-up):

- **Bifunctional activator/repressor**: Zhang et al. 2024 (EMBO J,
  doi:10.1038/s44318-024-00302-2) report WOX5 functions "as both transcriptional
  repressor and activator," with 1,423 activated and 947 repressed genes in
  sorted QC nuclei, and broad effects on histone marks (H3K9ac, H3K4me3,
  H3K27me3) and chromatin accessibility. The activator role lacks a specific
  validated direct activated target in the curated set, so no positive-regulation
  NEW term was added; recorded here as a candidate.
- **QC quiescence via CYCD3;3 repression**: Forzani et al. 2014 (Curr Biol,
  doi:10.1016/j.cub.2014.07.019) show WOX5 represses D-type cyclin activity
  (89% extra QC divisions in wox5-1, suppressed to 8% in wox5 cycd1;1 cycd3;3;
  ectopic CYCD3;3 forces QC divisions in 100% of embryos). Supports a role in
  negative regulation of QC cell division — candidate for a future
  cell-cycle/quiescence BP annotation.
- **Cell-type-specific TF complexes** with BRAVO and PLT3 (Strotmann 2024,
  FRET-FLIM) — relevant to protein-complex/coregulator function.
- **WOX5 movement requirement** is now debated: a 2024 reassessment (Vikram
  thesis) suggests movement may not be strictly required for CSC maintenance,
  cautioning against over-stating the "mobile signal" framing in core_functions
  (currently phrased as "partly mobile signal," which remains defensible).
