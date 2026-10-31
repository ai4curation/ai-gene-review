# nrde-2 (G5EG51) review notes

Deep research: falcon timed out (exit 137) and the perplexity-lite fallback is
unavailable. No deep-research file was generated. The review is based on cached
publications.

## Key facts with provenance
- NRDE-2 is recruited by NRDE-3/siRNA to nascent transcripts [PMID:20543824 "NRDE-2 associates with the Argonaute protein NRDE-3 within nuclei and is recruited by NRDE-3/siRNA complexes to nascent transcripts that have been targeted by RNAi."].
- It inhibits RNAP II elongation [PMID:20543824 "We conclude that siRNAs-direct a NRDE-2/3-dependent inhibition of RNAP II activity that occurs during the elongation phase of transcription."].
- It is required for NRDE-1 loading and for H3K9me [PMID:21901112 "NRDE-3 and NRDE-2 are required for the association of NRDE-1 with pre-mRNA and chromatin."].
- It is required for the dsRNA-induced H3K9me3 footprint [PMID:22231482].
- In the germline, HRDE-1 recruits NRDE-2 [PMID:22810588].
- It moves to the nucleolus and inhibits RNAP I when risiRNAs are present [PMID:34365510 "In the presence of risiRNAs, NRDE-2 accumulated in the nucleolus and colocalized with RNA polymerase I."].
- H3K27me3 is also directed through the Nrde pathway (PMID:26365259; abstract only, not
  quoted in the review).
- Human NRDE2 is an MTR4/exosome inhibitor in speckles [PMID:30842217]. This has not been
  tested in worm.

## Decisions
- protein binding (NRDE-3 IPI): REMOVE (uninformative).
- Post-transcriptional silencing IMP: MODIFY to GO:0031047 (the mechanism is
  co-transcriptional).
- mRNA stabilization ISS: MARK_AS_OVER_ANNOTATED. Nuclear speck and negative regulation
  of RNA catabolic process: kept as non-core.
- No core MF assigned. The direct molecular activity of NRDE-2 is unknown.
- I considered a NEW negative regulation of transcription elongation by RNA polymerase II
  (GO:0034244) and rejected it: the comparator check failed, because no other NRDE
  factor carries this term.
