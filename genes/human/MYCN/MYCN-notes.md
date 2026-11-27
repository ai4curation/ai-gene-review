# MYCN notes

Automated deep research was attempted for this review with `just deep-research-falcon human MYCN --fallback perplexity-lite`,
but the local Falcon provider was unavailable and the Perplexity fallback was not configured. These notes therefore summarize
the cached primary literature, Reactome summaries, UniProt record, and PANTHER PAINT data used for the manual review.

## Evidence reviewed

- **Conserved Myc transcription-factor core.** MYCN is on the same `PTHR45851` PAINT node as MYC and MYCL for nucleus,
  Pol II cis-regulatory DNA binding, Pol II-specific DNA-binding transcription-factor activity, and regulation of
  transcription by RNA polymerase II. The rows have no reported PAINT loss event in human MYCN. The older human
  biochemical paper already showed that N-myc encoded unstable phosphoproteins that "were located in the nucleus of cells,
  and bound to both single- and double-stranded DNA" [PMID:3796607].
- **Direct promoter binding and activation.** Beierle et al. identified N-MYC sites in the FAK promoter and "showed
  binding of N-MYC transcription factor to the FAK promoter through electrophoretic mobility shift, chromatin
  immunoprecipitation, and dual luciferase assays" [PMID:17327229].
- **MAX and NMI interactions.** Bannasch et al. reported that "Both Max and Nmi also bind to MycN" and mapped the
  MycN region responsible for NMI binding; the same abstract records that endogenous MycN in Kelly neuroblastoma cells
  "appears to be localized exclusively in the nuclei" [PMID:10597290].
- **Other curated protein-binding rows.** YAF2 binding was detected by yeast two-hybrid, in vitro, and in vivo assays
  [PMID:11593398]. p14ARF "associates in vivo with the N-Myc" [PMID:17289033]. N-Myc recruitment of HDAC1 to the TG2
  promoter was assayed by dual-step ChIP and protein co-IP [PMID:18003922]. Aurora A, MAX, and FBXW7 interactions were
  curated from studies of N-Myc stabilization by Aurora A and kinase inhibitors [PMID:19111882; PMID:23792191;
  PMID:25175806; PMID:27728805; PMID:27837025]. The 2022 SPOP, AKT1, and FBXW7 rows came from a quantitative
  high-throughput differential PPI screen for cancer mutation-directed interactions [PMID:35512704]. These are real or
  plausible physical-interaction observations, but the GO:0005515 rows are bare protein-binding annotations and are
  removed under the project protein-binding policy.
- **Regulatory outputs.** MYCN directly induced a FAK promoter [PMID:17327229], directly transactivated NCYM and its
  own promoter in the MYCN/NCYM locus [PMID:24391509], directly induced the SIRT1 promoter [PMID:21698133], and
  induced the miR-17-92 cluster that represses DKK3 expression [PMID:21796614]. These support the core positive
  transcriptional function plus context-specific cancer or miRNA outputs.
- **MYCLP1 contrast.** MYCN and MYCL are ordinary intron-containing Myc paralogs with experimental function or
  localization evidence. MYCLP1/MYCL2 is a processed, X-linked MYCL-related sequence whose protein product remains
  uncertain, so the MYCLP1 sequence-based rows were not used to reinforce MYCN/MYCL.
