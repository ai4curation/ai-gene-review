# ADAR2 (sqADAR2a, C1JAR3) - Review Notes

## Gene identity

- C1JAR3 = sqADAR2a (786 aa, the longer splice variant with 3 dsRBDs)
- C1JAR4 = sqADAR2b (687 aa, the shorter variant with 2 dsRBDs, conventional ADAR2 architecture)
- Species: Doryteuthis opalescens (California market squid)
- Closely related to Doryteuthis pealeii (longfin inshore squid), where most functional studies were done

## Key literature

### Palavicini et al. 2009 (PMID:19390115)
- First cloning and characterization of sqADAR2a and sqADAR2b
- sqADAR2a has an "extra" dsRBD encoded by an optional exon
- Both variants active on duplex RNA, but sqADAR2a edits many more sites on K+ channel mRNAs
- Both expressed at comparable levels and extensively self-edited

### Palavicini et al. 2012 (PMID:22457361)
- Extra dsRBD confers resistance to high chloride environment of squid neurons
- Squid cells have ~3-fold higher ionic strength than vertebrate cells
- Extra dsRBD increases RNA binding affinity 30-fold (vertebrate conditions) or 100-fold (squid conditions)
- Site-directed mutagenesis confirmed the RNA binding activity of the extra dsRBD is directly responsible

### Alon et al. 2015 (PMID:25569156)
- 57,108 recoding sites in D. pealeii nervous system
- Majority of neural transcripts are edited
- Enriched in genes with neuronal and cytoskeletal functions
- Orders of magnitude more recoding than any other species

### Vallecillo-Viejo et al. 2020 (PMID:32201888)
- sqADAR2 is expressed outside the nucleus in squid neurons
- Purified axoplasm has A-to-I editing activity
- >70% of editing sites are more extensively edited in the giant axon than cell bodies
- First demonstration of spatially regulated RNA editing within a neuron

### Vallecillo-Viejo et al. 2023 (PMID:37342458)
- Full complement of squid ADARs: sqADAR1, sqADAR2, sqADAR/D-like
- Only sqADAR1 and sqADAR2 are catalytically active
- sqADAR/D-like shows no deaminase activity
- sqADAR1 has a novel serine-rich domain (SRD)
- sqADAR2 is predominant ADAR in non-neural tissues (gill)
- sqADAR1 is predominant in nervous system
- sqADAR2 mRNAs are extensively self-edited

### Voss & Rosenthal 2023 (PMID:37981860)
- Review of high-level RNA editing in coleoid cephalopods
- Coleoids are the only known animals to recode majority of expressed proteins via RNA editing
- Describes unique ADAR features contributing to high-level editing

### Birk et al. 2023 (PMID:37295402)
- Temperature-dependent RNA editing in octopus (O. bimaculoides)
- >13,000 codons affected by temperature-dependent editing
- Recoding tunes synaptotagmin Ca-binding and kinesin-1 transport velocity
- Seasonal sampling confirms temperature-dependent editing in wild populations

## Annotation review decisions

### Accepted (core):
- GO:0003725 double-stranded RNA binding - core MF, directly demonstrated
- GO:0003726 double-stranded RNA adenosine deaminase activity - defining catalytic activity
- GO:0005634 nucleus - canonical ADAR localization
- GO:0005737 cytoplasm - demonstrated in axoplasm (PMID:32201888)
- GO:0006382 adenosine to inosine editing - core BP

### Kept as non-core:
- GO:0003723 RNA binding - too general, subsumed by GO:0003725
- GO:0006396 RNA processing - too general, subsumed by GO:0006382

### Modified:
- GO:0004000 adenosine deaminase activity -> GO:0003726 (free adenosine vs RNA-embedded adenosine)

### Removed:
- GO:0008251 tRNA-specific adenosine deaminase activity - wrong enzyme family (ADAT, not ADAR)

### Marked as undecided:
- GO:0005730 nucleolus - no squid-specific evidence

### New annotations proposed:
- GO:0016556 mRNA modification - captures primary substrate class
- GO:0008270 zinc ion binding - conserved catalytic zinc coordination
- GO:1904115 axon cytoplasm - directly demonstrated (PMID:32201888)
