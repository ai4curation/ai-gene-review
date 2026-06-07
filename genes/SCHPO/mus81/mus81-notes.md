# mus81 (SPCC4G3.05c, P87231) — S. pombe — review notes

## Summary
Mus81 is the catalytic subunit of the Mus81-Eme1 structure-specific DNA endonuclease (XPF/ERCC4 nuclease family). With its obligate partner Eme1 it cleaves branched DNA substrates — nicked Holliday junctions, 3'-flaps, D-loops, model replication forks — using an ERCC4 nuclease domain and a Mg2+ cofactor. Two catalytic aspartates (D395/D396) are essential. In fission yeast it is the principal/essential resolvase for meiotic crossover formation (no MSH4-MSH5 backup pathway) and processes stalled/collapsed replication forks in mitosis. Activity is restrained by the Cds1 (Chk2) replication checkpoint kinase.

## Key evidence

### Endonuclease activity / Holliday junction resolvase
- [PMID:11719193 "We report that Mus81 and an associated protein Eme1 are components of an endonuclease that resolves Holliday junctions into linear duplex products."] Mus81-Eme1 are subunits of a nuclear Holliday junction resolvase; required at a late step of meiotic recombination; mus81 meiotic defect rescued by a bacterial HJ resolvase. Catalytic mutant DD->AA (D395/D396) abrogates endonuclease activity (UniProt MUTAGEN).
- [PMID:14527419 "a nicked HJ is the preferred substrate of endogenous and recombinant Mus81-Eme1. Cleavage occurs specifically on the strand that opposes the nick"] Nick-and-counternick mechanism; "HJs accumulate in a DNA polymerase alpha mutant that lacks Mus81, providing further evidence that the Mus81-Eme1 complex targets HJs in vivo."
- [PMID:17363897 "we report the purification of active forms of recombinant Schizosaccharomyces pombe Mus81-Eme1 ... which display robust HJ cleavage in vitro, which, in the case of Mus81-Eme1, is as good as the archetypal HJ resolvase RuvC"] Robust intact-HJ cleavage; proposed as a failsafe backup to its main nicked-HJ cleavage.
- [PMID:11741546 "Human Mus81 has associated endonuclease activity against structure-specific oligonucleotide substrates, including synthetic Holliday junctions."] Human Mus81 (XPF homolog) cleaves HJs; supports cross-species MF.

### Meiotic crossover / reciprocal recombination
- [PMID:14704204 "Schizosaccharomyces pombe mus81 mutants have normal or elevated frequencies of gene conversion but 20- to 100-fold reduced frequencies of crossing over ... Mus81 is required for crossing over"] Mus81 essential for meiotic crossovers but not gene conversion.
- [PMID:25414342 "Rad55-Rad57 and Rdl1-Rlp1-Sws1 together with Swi5-Sfr1 play a major role in antagonizing both the FANCM-family DNA helicase/translocase Fml1 and the RecQ-type DNA helicase Rqh1 to limit hybrid DNA formation and promote Mus81-Eme1-dependent COs"] IGI with rad55 (SPAC3C7.03c) — paralogs/mediators promote Mus81-Eme1-dependent crossovers.
- [PMID:15466419 "the swi5 deletion strongly suppressed the low viable spore yield of mutants lacking Mus81*Eme1, which resolves joint molecules such as Holliday junctions"] Mus81-Eme1 resolves meiotic joint molecules (TAS for joint molecule formation pathway).

### Replication fork processing / DSB repair / damage tolerance
- [PMID:11073977 "the forkhead-associated-1 (FHA1) protein-docking domain of Cds1 interacts with Mus81, an evolutionarily conserved damage tolerance protein"] Mus81 interacts with Cds1 FHA1; "Inactivation of Mus81 triggers a checkpoint-dependent delay of mitosis." Damage tolerance; required in absence of Rqh1.
- [PMID:19037101 "We have identified proteins downstream of Cds1 required for checkpoint-dependant slowing, including the structure-specific endonuclease Mus81 ... defining an epistatic pathway in which mus81 is epistatic to rhp51 and rhp51 is epistatic to rqh1"] Mus81 required for S-phase DNA damage checkpoint (replication slowing).
- [PMID:17307401 "Mus7 functions in the same pathway as Mus81 ... In Deltamus7 and Deltamus81 cells, the repair of MMS-induced DNA double-strand breaks (DSBs) is severely impaired."] mus81 required for repair of replication-associated DSBs (HR).
- [PMID:28586299 "loss of mus81 causes a > 2 fold reduction in SDDs ... indicating that Mus81-Eme1 specifically promotes SDDs"; "Mus81-Eme1 could indeed resolve an IFSA junction into two nicked/gapped linear duplex DNA products"] Mus81 processes replication-fork convergence junctions (replication fork processing IMP).
- [PMID:14993467 "Srs2 and the structure-specific endonuclease Mus81-Eme1 function in a sub-pathway of PRR for the tolerance/repair of UV-induced damage"] DNA damage tolerance (TAS).

### Localization / complex
- UniProt SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:11719193}.
- [PMID:16823372] Genome-wide YFP localization; PomBase derives both nucleus (HDA) and mitochondrion (HDA). Mitochondrial signal is from a high-throughput screen; not corroborated by any functional data — likely background/contaminant for a HJ resolvase. The IC "mitochondrial DNA metabolic process" (GO:0032042) is curator-inferred solely from that mitochondrial HDA + endonuclease activity, with no direct mtDNA evidence.
- ComplexPortal CPX-26589: MUS81-EME1 structure-specific endonuclease complex. PMID:17363897 supports complex + nuclear replication fork localization.

## Curation considerations
- "protein binding" (GO:0005515, IPI with eme1 SPAPB1E7.06c, PMID:11719193) is uninformative; the informative call is the Mus81-Eme1 complex (GO:0048476) and endonuclease MF. Mark over-annotated; complex membership captures the meaningful interaction.
- GO:0006308 (DNA catabolic process, IEA/InterPro) is an over-general parent; the specific endonuclease/resolution terms are better.
- GO:0032042 (mitochondrial DNA metabolic process, IC): weak; rests on a HT mitochondrial localization with no functional mtDNA data. Mark as over-annotated / non-core.
- Core: structure-specific (crossover junction / HJ) endonuclease; Mus81-Eme1 complex; nucleus; meiotic crossover/resolution of recombination intermediates; replication fork processing & DSB repair.
