# ARPC1A: literature and annotation assessment

## Scope and source access

ARPC1A is the human ARPC1A/PTHR10709:SF11 paralog of the WD-repeat p41 Arp2/3 subunit. ARPC1B is already reviewed separately as the human PTHR10709:SF10 paralog. The first configured Perplexity deep-research attempt failed before provider execution because that provider is not available in this runtime, so this review uses manual inspection of the cached UniProt, PAINT, InterPro/PANTHER, Reactome and publication sources.

The old SOP2 Hs paper supports human ARPC1A family conservation and fission-yeast Sop2p complex biology, not a direct actin-binding assay on human ARPC1A. The cached paper reports that a human cDNA related to S. pombe sop2+ complemented the yeast sop2-1 mutant, but its Arp3p/profilin/actin interaction and localization data concern fission-yeast Sop2p. The later human platelet p41 study is also not used as a direct ARPC1A source: it identified p41-Arc as a new human Sop2 family member and explicitly states that platelet p41-Arc is 67% identical to the previously identified Sop2Hs, meaning the native platelet p41 evidence is ARPC1B-like rather than ARPC1A-specific.

The complete PMID:26655834 abstract is the direct ARPC1A functional source in the normal cache. It compares mammalian Arp2/3 complexes containing ARPC1A/ARPC5 with those containing ARPC1B/ARPC5L in cells and in vitro. ARPC1B/ARPC5L complexes promote actin assembly more strongly and are stabilized by cortactin against coronin-mediated disassembly, but the comparison still places ARPC1A in assembled, actin-promoting Arp2/3 complexes. The full original Methods and figure-level reagent species were not recovered, so no claim rests on uninspected construct details.

The broad cytosol rows are retained because ARPC1A is a soluble Arp2/3 subunit with no signal peptide or transmembrane segment and acts in cytoplasmic actin nucleation. Reactome's many cytosol rows were read at the event-summary level and treated as event contexts for cytosolic actin remodeling, not as independent ARPC1A imaging or as evidence for myosin, dynamin, HSPA8 or receptor functions. The central R-HSA-2029466 event explicitly describes ARP2/3-driven branch nucleation and lists ARPC1 among the five non-Arp subunits.

The human DSB ChIP experiment uses Arpc2, while the all-seven-subunit chromatin proteomics was performed in Xenopus egg extracts; human ARPC1A versus ARPC1B nuclear occupancy remains unresolved. The Xenopus source is useful for the ARPC1A branch, so the human nucleus and site-of-DSB rows are not removed, but PMID:29925947 does not resolve which human p41 paralog occupies nuclear Arp2/3.

The exact mouse Q9R0Q6 donor annotations behind the muscle and synapse Ensembl transfers were not chased, so the human ARPC1A tissue-specific transfers stay UNDECIDED. Mouse Arpc1a is the correct orthologous donor, but this bounded review did not reconstruct the source publications or the human cell-context transfer boundary.

The urinary-exosome cache for PMID:19056867 is abstract-only despite a PMCID. It reports broad LC-MS/MS profiling of 1132 human urinary-exosome proteins, but not the exact ARPC1A peptide/protein table. The HDA extracellular-exosome row therefore remains UNDECIDED pending exact target verification.

All PAINT assertions in PTHR10709 are at PTN000076207 and there were no IRD or IKR losses on the ARPC1A lineage in the cached PAINT table. The three IBA rows for Arp2/3 protein complex, Arp2/3 complex-mediated actin nucleation and cortical actin cytoskeleton organization are accepted and documented in the family review.
