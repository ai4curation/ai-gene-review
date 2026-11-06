# sma-9 notes

Deep research: the wrapper reported a falcon timeout (600 s), and the perplexity fallback was unavailable. The review relies on the cached publications and UniProt Q7JM44.

- Schnurri homolog and a downstream DBL-1 pathway component [PMID:14627718 "sma-9 acts as a downstream component and is required in the DBL-1 signaling pathway"]
- Mainly a repressor in body size; both activator and repressor activity act in the male tail [PMID:17397820 "SMA-9 acts primarily as a transcriptional repressor in body size regulation in vivo"]
- Antagonizes BMP in the dorsal M lineage [PMID:16790477] by repressing unc-130 [PMID:29155044 "However, our data showed that SMA-9 actively represses BMP-dependent UNC-130 expression."]
- Annotations from PMID:25407930 (amyloid-beta model; abstract-only) cannot be verified. Lifespan, heat response and nuclear-localization rows are UNDECIDED.
- Note for the module: SMA-9 has an opposite sign in the M lineage (it antagonizes BMP), unlike its positive role in body size.

Deep research update: a falcon job eventually completed and wrote `sma-9-deep-research-falcon.md`. Points from it (primary papers not cached here):
- Vora et al. 2025 (eLife): SMA-9 ChIP-seq gave 7,065 peaks, 3,101 of them overlapping SMA-3. Direct targets are about equally up- and down-regulated, and most SMA-3/SMA-9 co-targets are activated by both. This tempers the 'mainly a repressor' conclusion, so a suggested question was added.
- Yin et al. 2010: a C-terminal isoform (D01) acts in ray patterning.
- Baccas et al. 2025: SMA-9 restrains SEM-2 and permits LET-381 in the dorsal M lineage.
- A review states that SMA-9 is not required for the DBL-1 antifungal AMP response.

## ROS and mitochondrial UPR statements in UniProt (2026-10-30)

- UniProt FUNCTION says SMA-9 is "Involved in production of reactive oxygen species (ROS)"
  and "Plays a role in the mitochondrial unfolded protein response (mtUPR)", citing
  PubMed:20687916. That paper is Wong et al. 2010 on mab-31 and male ray patterning; its
  cached full text contains no ROS, mitochondrial or nanopolystyrene data.
- The statements match a nanopolystyrene toxicology study [PMID:32758726 "intestinal SMA-9
  activated the mitochondrial unfolded protein response by affecting ELT-2 activity"]. The
  UniProt citation looks mis-keyed; recorded as a source defect on the UniProt reference.
- The finding is a response to a xenobiotic exposure, from one abstract-only study, and is
  peripheral to SMA-9's role as a Schnurri-family BMP pathway cofactor. Not annotated.
