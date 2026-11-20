# hfq (PP_4894, Q88DD3) review notes

- Existing Falcon deep research (`hfq-deep-research-falcon.md`) plus cached primary literature.
- Core: Hfq is the RNA-binding component of the Crc/Hfq catabolite repression system
  [PMID:24803210 "Herein, we show that the Pseudomonas putida Hfq protein can recognize the CA motifs of RNAs through its distal face and that Crc facilitates formation of a more stable complex at these targets."];
  [PMID:24803210 "Inactivation of the hfq or the crc gene impaired catabolite repression to a similar extent."]
- Repression is antagonised by CrcZ/CrcY [PMID:27777366 "The effect of these two proteins is antagonized by the CrcZ and CrcY small RNAs (sRNAs), the levels of which vary greatly according to growth conditions."],
  and Hfq/Crc stabilise CrcZ [PMID:27777366 "In addition, we show that Crc and Hfq increase CrcZ stability, which supports the idea that these proteins can form a complex with CrcZ and protect it from degradation by RNases."]
- Translation repression measured directly for the P. aeruginosa ortholog
  [PMID:34139006 "In fact, the presence of Crc resulted in stronger translational repression in vitro and in a significantly reduced half-life of the target amiE mRNA in vivo."]
- 2026-10-23 completion pass: added verbatim support to all rows; NEW translation repressor activity (enables),
  negative regulation of translation, and carbon catabolite repression; core functions split into the Crc/Hfq
  repressor role and the general sRNA chaperone/RNA-stability role.

## 2026-11-16 — TF batch 2: RNA regulation and CrcZ stability

All five machine-seeded rows and three existing authored proposals were re-reviewed. RNA binding remains core because Hfq acts on mRNA and ncRNA; translation repression does not subsume RNA-stability activity. The transcription-regulation mapping is refined to its primary post-transcriptional mechanism without the categorical claim that Hfq cannot bind DNA. Indirect PcrcZ transcriptional effects are distinct from the Hfq RNA mechanism.

[PMID:27777366, Effect of Crc and Hfq proteins on the transcription, processing, and stability of the Pseudomonas putida CrcZ sRNA] full text provides the KT2440 CrcZ-stability experiment. Rifampicin-chase Northern blots compare KT2440-Z, KT2440Δhfq and KTCRC with p424-Z, after growth in LB plus 1 mM IPTG. Primary CrcZ half-life is about six minutes with Hfq/Crc versus 3.8 minutes without Hfq. This is stabilization of a transcript carrying 62 additional nucleotides, not activation of the crcZ promoter. Processed CrcZ was undetectable in Δhfq, so no processed-RNA half-life is inferred in that strain. Direct RNA contact was not measured in this experiment; physical directness remains unresolved. CrcY stability is not extrapolated.

The LinkML sidecar now explicitly distinguishes RNA stability from transcription and translation. CrcZ/CrcY antagonize CCR by protein titration, not by base-pairing with catabolic mRNAs. Description/core wording was narrowed accordingly. Translation-repressor MF and negative translation-regulation proposals retain their ISS donor Q9HUM0 and P. aeruginosa evidence [PMID:34139006, Stabilization of Hfq-mediated translational repression by the co-repressor Crc in Pseudomonas aeruginosa]. The P. aeruginosa structural study is not KT2440 localization microscopy. By contrast, Hfq itself performs the RNA-recognition/repression step of CCR, unlike upstream CbrB; its existing CCR proposal is retained.

No provider research or existing UniProt/GOA/publication text was changed. FEBA lookup failed without writing an artifact; PSEPK has no applicable MOD-description source.
