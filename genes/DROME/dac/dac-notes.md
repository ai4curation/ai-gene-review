# dac (Drosophila dachshund) notes

Automated deep research was unavailable for this review (falcon 402, OpenAI 401); notes compiled manually from cached publications and UniProt.

Canonical entry: Q8IP19 (unreviewed TrEMBL, "Dachshund, isoform B"; FBgn0005677; PANTHER PTHR12577:SF6). Domains: Ski_Sno_DHD (DD1/Dachbox-N) and DACH_C (DD2/Dachbox-C).

## Molecular function
- Ski/Sno-related nuclear protein: [PMID:15242803 "Dachshund (Dac) is a highly conserved nuclear protein that is distantly related to the Ski/Sno family of corepressor proteins"]
- DD1 is the essential domain and needed for nuclear localization: [PMID:15242803 "We show that only DD1 is essential for Dac function"]; DD2-Eya interaction is dispensable for synergy.
- Forms a complex with Eya: [PMID:9428513 "the Dachshund and Eyes Absent proteins can physically interact through conserved domains"]
- Binds CtBP directly (GST pull-down): [PMID:38528987 "Our present study shows that Dac and CtBP bind each other directly, as determined by GST pull-down assays."] The paper shows no DNA binding, so the TAS to DNA-binding TF activity was changed to transcription coregulator activity.
- No fly experiment shows sequence-specific DNA binding. Vertebrate DACH1 DD1 has a winged-helix-like DNA-binding fold [PMID:12057194] -- relevant by homology only. IBA DNA-binding/TF rows kept as non-core.

## Processes
- Eye: null flies are eyeless [PMID:7821215 "Null mutations in dachshund result in flies with no eyes and shortened legs."]; sufficient for ectopic eyes [PMID:9006066 "targeted expression of dachshund is sufficient to direct ectopic retinal development in a variety of tissues"]; cross-regulation with ey and eya.
- Leg PD patterning: [PMID:9729490 "In addition, we show that dac negatively regulates Dll."]
- Mushroom body: [PMID:10821764 "dachshund functions in the developing mushroom body neurons to ensure their proper differentiation"]; axon guidance [PMID:15818552].
- Lamina neurons [PMID:16242405]; antennal joints [PMID:11934862]; genital disc sex-specific [PMID:11290302].

## Module
Module annoton (retinal_determination_network, dach_coregulator) GO:0003712 transcription coregulator activity is consistent with this review. Proposed NEW GO:0010092 specification of animal organ identity (IMP, PMID:9006066), matching the module concept.
