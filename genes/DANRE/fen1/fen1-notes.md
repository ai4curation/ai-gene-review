# fen1 (Danio rerio) -- Research Notes

## Gene Overview

fen1 encodes Flap endonuclease 1 (FEN-1; EC 3.1.-.-), a structure-specific nuclease in the XPG/RAD2 endonuclease family. The zebrafish protein (UniProt Q6TNU4) is 380 amino acids and contains canonical XPG N-terminal and I-domains that form the nuclease active site, plus a C-terminal PCNA-interaction region (residues 336-344).

## Molecular Functions

### 5'-Flap Endonuclease Activity

FEN1 is a structure-specific endonuclease that cleaves 5'-flap structures at the junction between single-stranded and double-stranded DNA. It enters the flap from the 5'-end and tracks to the flap base to make a single endonucleolytic cut, leaving a ligatable nick [PMID:23451868, "a structure-specific endonuclease that evolved to cut at the base of single-stranded flaps"]. The enzyme threads the 5' end of the flap through its helical arch and active site [PMID:21335237, Human FEN1 structures show the double-base flipping mechanism].

### 5'-3' Exonuclease Activity

FEN1 also possesses 5'-3' exonuclease activity on nicked or gapped double-stranded DNA [PMID:23451868, "substrate specificity allowing FEN1 to process intermediates of Okazaki fragment maturation, long-patch base excision repair, telomere maintenance, and stalled replication fork rescue"]. The exonuclease activity requires occupancy of both the high- and low-affinity metal binding sites, whereas the endonuclease activity requires only the high-affinity site [PMID:18697748, three metal ions participate in the FEN reaction].

### RNA-DNA Hybrid Ribonuclease Activity

FEN1 exhibits RNase H-like activity, cleaving RNA from RNA-DNA hybrids. This is relevant to Okazaki fragment processing where RNA primers are displaced into flap structures [PMID:9501173, junction ribonuclease activity in Okazaki fragment processing]. FEN1 cleaves RNA endonucleolytically, removing an RNA flap and tracking along to the RNA-DNA junction.

### Metal Ion Requirements

FEN1 requires divalent metal ions for catalysis. It binds two magnesium ions per subunit that participate in the reaction. Mg2+ and Mn2+ are both effective cofactors [PMID:18697748, "three magnesium ions" participate, with an additional third magnesium ion bound after substrate binding]. The active site acidic residues coordinate these metal ions for phosphodiester bond hydrolysis.

### DNA Binding

FEN1 binds DNA through multiple contacts: the XPG N- and I-domains clamp the DNA and position the scissile phosphate, while the helix-hairpin-helix (HhH2) motif (residues 220-253 in zebrafish) provides non-sequence-specific DNA binding [UniProt Q6TNU4, binding sites at residues 47, 70, 158, 231, 233].

## Biological Processes

### Okazaki Fragment Processing in DNA Replication

During lagging-strand DNA replication, displacement synthesis by DNA polymerase delta generates 5'-flaps on downstream Okazaki fragments. FEN1 cleaves these flaps to enable ligation by DNA ligase I [PMID:23451868, "intermediates of Okazaki fragment maturation"]. FEN1 operates within a PCNA-coordinated complex: three FEN1 molecules bind one PCNA trimer, with each FEN1 binding one PCNA monomer. PCNA stimulates nuclease activity without altering cleavage specificity [UniProt Q6TNU4, HAMAP-Rule:MF_03140].

### Removal of RNA Primer

FEN1 participates in the removal of RNA primers from Okazaki fragments, working in concert with RNase H to process the RNA-DNA junctions that remain after primer displacement [UniProt Q6TNU4, GO:0043137].

### Long-Patch Base Excision Repair

In long-patch base excision repair (LP-BER), DNA polymerase beta or delta performs strand displacement synthesis after an AP site is incised, creating a 5'-flap. FEN1 trims these flaps to complete repair [PMID:15189154, "a central component of DNA metabolism"]. This pathway is critical for genomic integrity.

### Retina Development in Camera-Type Eye (Zebrafish-Specific)

The zebrafish fen1 insertional mutant (identified in the Hopkins lab large-scale mutagenesis screen) shows defects in retinal development [PMID:15716491, "Forty loci whose disruption resulted in defects in eye development and/or visual function were identified"]. The fen1 mutant has drastically smaller eyes with defects in the number and organization of retinal neurons at 5 dpf. Retinal patterning is severely affected with the most obvious defects in the outer retina. The mutant differentiates a population of retinal ganglion cells (RGCs) but with an optic nerve of significantly less diameter than wild-type siblings. This phenotype likely reflects the high proliferative demand of retinal progenitor cells, which require robust DNA replication and repair capacity. The fen1 gene was also identified as one of 315 genes essential for early zebrafish development [PMID:15256591, "Identification of 315 genes essential for early zebrafish development"].

## Subcellular Localization

FEN1 localizes to: (1) the nucleolus, where it maintains stability of ribosomal DNA tandem repeats [PMID:18443037, "Nucleolar localization and dynamic roles of flap endonuclease 1 in ribosomal DNA replication and damage repair"]; (2) the nucleoplasm, where it relocalizes upon DNA damage via phosphorylation-dependent mechanisms; and (3) mitochondria, where it participates in mitochondrial DNA replication and repair [PMID:19699691, "Evidence for a role of FEN1 in maintaining mitochondrial DNA integrity"].

## Conservation and Essentiality

FEN1 is highly conserved across eukaryotes. Mouse Fen1 knockout is embryonically lethal, with null blastocysts arrested in S phase [PMID:12861020, "Proliferation failure and gamma radiation sensitivity of Fen1 null mutant mice at the blastocyst stage"]. Haploinsufficiency leads to increased tumor susceptibility [PMID:12119409]. The zebrafish fen1 mutant shows essential developmental roles consistent with its fundamental functions in DNA replication and repair.

## Key References

- PMID:23451868 - Balakrishnan & Bambara 2013, Annual Review of Biochemistry, comprehensive FEN1 review
- PMID:15189154 - Shen et al. 2005, BioEssays, FEN1 as central component of DNA metabolism
- PMID:15716491 - Gross et al. 2005, Genetics, zebrafish visual system mutants (IMP evidence for fen1)
- PMID:15256591 - Amsterdam et al. 2004, PNAS, 315 essential zebrafish genes
- PMID:15520368 - Song et al. 2004, PNAS, zebrafish hematopoietic gene expression (fen1 sequence)
- PMID:18443037 - Guo et al. 2008, MCB, FEN1 nucleolar localization
- PMID:19699691 - Zheng et al. 2008, DNA Repair, FEN1 mitochondrial DNA role
- PMID:12861020 - Larsen et al. 2003, MCB, Fen1 null mouse lethality
- PMID:18697748 - Syson et al. 2008, JBC, three metal ions in FEN reaction
