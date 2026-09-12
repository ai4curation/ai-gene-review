# dcr1 (Dicer) — S. pombe — Curation Notes

UniProt: Q09884 (DCR1_SCHPO). PomBase: SPCC188.13c. 1374 aa. NCBITaxon:284812.

## Summary
Dcr1 is the sole Dicer (ribonuclease III enzyme) of fission yeast. It is the
endoribonuclease that initiates RNAi by processing double-stranded RNA into ~22-23 nt
siRNA duplexes that are loaded onto Argonaute (Ago1). It is essential for
RNAi-directed heterochromatin formation at centromeres (and the mating-type locus,
telomeres), and hence for accurate chromosome segregation. It has additional reported
roles in co-transcriptional gene silencing (CTGS) at euchromatic loci, RNA Pol II/I/III
release / transcription termination at sites of replication stress (genome stability),
and in cell cycle / quiescence (G0).

## Domain architecture
N-terminal DExD/H-box ATP-dependent RNA helicase (ATP-binding 32-MRTGAGKT-39; DECH box
145-DECH-148), Platform/PAZ-like region, tandem RNase III domains (RIIIa/RIIIb), and a
C-terminal extended dsRNA-binding fold with a novel zinc-binding (CHCC) motif important
for nuclear retention. Catalytic-dead allele D937A/D1127A abolishes siRNA generation.

## Key evidence (verbatim)

### RNase III / dsRNA processing into ~23 nt siRNA (MF core)
[PMID:12482946 "As Dicer in other species, Dcr1p degraded double-stranded RNA into ≈23 nucleotide fragments in vitro"]
[PMID:12482946 "an ≈23-nt band was produced by Dcr1-HA immunoprecipitates when incubated with the human let-7 microRNA precursor"]
RNase III activity IDA from PMID:12482946.

### Helicase / ATP-binding (domain-based, MF)
[PMID:12482946 "a protein of 1,374 aa with an N-terminal helicase domain containing an ATP-binding site motif 32 M RTGAGKT 39 and a 145 DECH 148 box, and tandem C-terminal ribonuclease (RNase) III signatures"]
Note: helicase activity and ATP binding are domain/keyword-based; no direct demonstration of helicase catalysis in pombe Dcr1 found. Treat ATP binding as supported (structural motif), helicase activity as plausible but uncertain for catalysis.

### dsRNA binding / dsDNA binding / zinc binding (MF)
[PMID:21847092 "the isolated domain (Figure 4A) binds rather strongly to a regular A-form RNA helix (Kd=0.8 μM, with two dsRBDs bound per 24 bp dsRNA helix)"]
[PMID:21847092 "the extended dsRBD of Dcr1 showed a fairly strong affinity to a regular B-form DNA helix (Kd=1.5 μM)"]
[PMID:21847092 "the Dcr1 C-terminal domain containing the dsRBD and the C33 indeed include one zinc ion per molecule"]
Important caveat: [PMID:21847092 "Surprisingly, we found that dsRNA binding through the dsRBD is also dispensable for heterochromatin silencing and siRNA generation"] — the C-terminal dsRBD dsRNA/dsDNA binding is dispensable for RNAi; the zinc motif's role is nuclear retention. So dsDNA binding is a real biochemical property but not the core functional contribution.

### siRNA-mediated pericentric heterochromatin formation / H3K9me (BP core)
[PMID:12193640 "Deletion results in the aberrant accumulation of complementary transcripts from centromeric heterochromatic repeats. This is accompanied by transcriptional de-repression of transgenes integrated at the centromere, loss of histone H3 lysine-9 methylation, and impairment of centromere function."]
[PMID:21847092 "Deletions of any of the three genes encoding the RNAi proteins Dicer, Argonaute and RNA-dependent RNA polymerase (dcr1+, ago1+ and rdp1+, respectively) result in loss of CTGS, chromosome segregation defects, and greatly reduced levels of H3K9 methylation (H3K9me) at centromeric repeats"]
[PMID:15615848 amplification loop — Rdp1/Dicer self-enforcing loop coupling siRNA production to heterochromatin]
[PMID:22895252 "siRNA is amplified by the RNA-dependent RNA polymerase complex (RDRC) and the endoribonuclease Dcr1, which synthesizes dsRNA and processes the dsRNA, respectively. The amplification is essential for stable heterochromatin formation."]

### Chromosome segregation (BP, core/keep)
[PMID:12482946 "Deletion of the Dicer (dcr1+) gene caused slow growth, sensitivity to thiabendazole, lagging chromosomes during anaphase, and abrogated silencing of centromeric repeats."]

### Co-transcriptional gene silencing (CTGS) at euchromatin (BP)
[PMID:21151114 "we show that the RNAi proteins Dcr1 and Rdp1 physically associate with some euchromatic genes, noncoding RNA genes and retrotransposon long terminal repeats, and that this association is independent of the Clr4 histone methyltransferase. Physical association of RNAi with chromatin is sufficient to trigger a silencing response but not to assemble heterochromatin."]
[PMID:22431512 "RNAi components interact with chromatin at nuclear pores to keep stress response genes in check ... RNAi-mediated CTGS represses stress-inducible genes by degrading mRNAs under noninduced conditions. Under chronic heat stress conditions, a Dicer thermoswitch deports Dicer to the cytoplasm"]

### Subcellular location
[PMID:21847092 "disruption of zinc coordination renders Dcr1 mainly cytoplasmic and leads to remarkable changes in gene expression and loss of heterochromatin assembly"] (nucleus is functionally important)
[PMID:22431512] euchromatin / cytosol / nuclear periphery IDA
[PMID:21151114] chromatin / pericentric heterochromatin IDA
[PMID:16823372] HDA cytoplasm/cytosol (global localization screen)

### Transcription termination / Pol II,I,III release at replication stress (BP)
[PMID:25417108 "Dcr1, but not other components of the canonical RNAi pathway, promotes the release of Pol II from the 3? end of highly transcribed genes, and, surprisingly, from antisense transcription of rRNA and tRNA genes, which are normally transcribed by Pol I and Pol III. These Dcr1-terminated loci correspond to sites of replication stress and DNA damage"]
[PMID:25417108 "Dcr1 is required for rDNA copy number maintenance"]
Caveat: this is Dcr1-specific and independent of canonical RNAi/Ago1; the GO terms "termination of RNA polymerase I/II/III transcription" capture this. Catalytic-dead and ago1Δ do NOT phenocopy at these loci.

### Cell cycle / G0 quiescence (BP)
[PMID:27738016 "We identify RNA interference (RNAi) as a major requirement for quiescence (G0 phase of the cell cycle) in Schizosaccharomyces pombe. RNAi mutants lose viability at G0 entry and are unable to maintain long-term quiescence."]
UniProt FUNCTION: "Required for G1 arrest and mating in response to nitrogen starvation."

### Post-transcriptional regulation (BP, peripheral)
[PMID:17981703 "Analysis of part of the soluble proteomes identified eight cellular proteins whose expression is under Dcr1 control ... compatible with the existence of a post-transcriptional gene regulatory mechanism involving Dcr1"]

### Stress robustness / Hsp104 feedback (BP, peripheral)
[PMID:25543137 "environmentally induced discontinuous phenotypic variation is buffered by a negative feedback loop that involves the RNase Dicer and the protein disaggregase Hsp104"]

### Mating-type silencing
[PMID:16246721 "Clr3 ... acts in a distinct pathway parallel to RNAi-directed heterochromatin nucleation to recruit Clr4 and mediate H3K9 methylation at the silent mating-type region and centromeres."] (RNAi-directed nucleation at mat locus)

## Curation decisions
- Core MF: ribonuclease III activity (IDA, ACCEPT), and the more specific GO:0016891
  RNA endonuclease activity producing 5'-phosphomonoesters (ACCEPT - mechanistically correct for RNase III).
- dsRNA binding: ACCEPT (IDA). dsDNA binding: KEEP_AS_NON_CORE (real but dispensable). zinc binding: ACCEPT.
- ATP binding: ACCEPT (domain motif). helicase activity not in GOA explicitly (only IEA keyword in uniprot DR); RNA binding IBA generalize/accept.
- DNA binding IEA (GO:0003677) is generic InterPro from helicase domain — MARK as over-general/MODIFY. Actually dsDNA binding is experimentally shown; generic DNA binding IEA is weak. MARK_AS_OVER_ANNOTATED.
- RNA processing IEA / gene expression IEA / hydrolase IEA: over-general, KEEP_AS_NON_CORE or accept as generic parents.
- BP core: siRNA-mediated pericentric heterochromatin formation; siRNA processing; CTGS; regulatory ncRNA-mediated gene silencing; chromosome segregation (keyword), silent mating-type cassette heterochromatin formation.
- Transcription termination Pol I/II/III: ACCEPT (well-supported, Dcr1-specific, PMID:25417108).
- G0 to G1 / quiescence: KEEP_AS_NON_CORE.
- negative regulation of gene expression (CACAO, PMID:17981703): KEEP_AS_NON_CORE (PTGS, peripheral).
