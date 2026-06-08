# rqh1 (Q09811, SPAC2G11.12) — curation notes

Rqh1 (aka rad12, hus2, rec9) is the single RecQ-family ATP-dependent 3'-5' DNA helicase of
*Schizosaccharomyces pombe*, ortholog of *S. cerevisiae* Sgs1 and human BLM/WRN/RECQL4.

## Identity / domain architecture
- 1328 aa. Helicase ATP-binding domain (528-707), Helicase C-terminal (728-876), HRDC (1115-1195),
  DEAH box motif (651-654), Walker A ATP-binding (555-562). RecQ Zn-binding and RQC domains
  (InterPro). [UniProt Q09811]
- EC 5.6.2.4 (DNA helicase coupling ATP hydrolysis to 3'-5' translocation). [UniProt; PMID:12724426]

## Helicase activity / biochemistry
- Rqh1 is a 3'-to-5' DNA helicase that exists with Top3 in a high-MW complex
  [PMID:12724426 "Rqh1, the single Schizosaccharomyces pombe homologue, is a 3'-to-5' helicase and exists with Top3 in a high-molecular-weight complex."]
- Helicase activity confirmed biochemically; T543I (rad12 allele) and K547A/R abolish helicase activity
  [UniProt MUTAGEN 543, 547; PMID:12724426]
- Rqh1p displays 3' to 5' DNA helicase activity but helicase activity is only PARTIALLY required for function in recovery from S-phase arrest/DNA damage
  [PMID:12478586 "the Rqh1p protein displays 3' to 5' DNA helicase activity. Interestingly, however, unlike other RecQ family members, the helicase activity of Rqh1p is only partially required for its function in recovery from S-phase arrest or DNA damage."]

## Top3 interaction / RecQ-Top3 complex
- top3 deletion is inviable; suppressed by loss of rqh1 helicase activity or recombination functions
  [PMID:12724426 "top3 deletion is inviable, and this is suppressed by concomitant loss of rqh1 helicase activity or loss of recombination functions."]
- N-terminal region (first 322 aa) of Rqh1 binds Top3; binding correlates with Rqh1 function
  [PMID:15702347 "Topoisomerase III (Top3) binds to a site within the first 322 N-terminal amino acids of Rqh1 and that this binding correlates with Rqh1 function."]
- ComplexPortal/PomBase: RecQ family helicase-topoisomerase III complex (GO:0031422)

## Subcellular localization
- Nucleus; nuclear chromosome; nucleolus [PMID:12724426; PMID:12023299]
- Site of double-strand break, nucleolus [PMID:12023299 IDA]
- Nuclear replication fork inferred (IC from RecQ-Top3 complex) [PMID:12724426]

## Recombination control / fork processing (core)
- Rqh1 acts after Rad51 (Rhp51) focus formation, downstream of strand invasion
  [PMID:12724426 "Rqh1 functions after Rad51 focus formation during DNA repair"]
- Negatively regulates recombination; rqh1Δ shows hyper-recombination, HU and UV sensitivity; DNA damage
  sensitivity alleviated by disrupting recombination
  [PMID:19037101 "the helicase Rqh1, which are implicated in replication fork stability and the negative regulation of recombination"]
  [PMID:19037101 "Cells lacking Rqh1 display phenotypes attributed to inappropriate, ectopic recombination including hyper-recombination, sensitivity to replication arrest and sensitivity to UV-induced DNA damage"]
- Prevents blocked forks from collapsing; rqh1- → dramatic increase in deletion events + one-sided DSBs at RTS1 RFB
  [PMID:15889146 "In the absence of the RecQ family DNA helicase Rqh1, deletion events increase dramatically, which correlates with the detection of one-sided DNA double-strand breaks at or near RTS1. These data indicate that Rqh1 acts to prevent blocked replication forks from collapsing"]
- Rqh1 limits gross chromosomal rearrangements (GCRs) at collapsed forks by preventing inappropriate ectopic recombination during fork recovery
  [PMID:23093942 "Rqh1 limits GCRs at collapsed forks by preventing inappropriate ectopic recombination during the process of fork recovery by recombination proteins."]
- Rqh1 counteracts D-loop disassembly (template switch) — antagonized by CAF-1
  [PMID:25313826 "CAF-1 promotes template switch by counteracting D-loop disassembly by Rqh1"]
- Rqh1 (with Fbh1, Srs2, Pfh1) strongly suppresses template switching during recombination-restarted replication
  [PMID:30667359 "A further three conserved helicases (Fbh1, Rqh1 and Srs2) strongly suppress TS"]

## DSB repair / resection
- Rqh1 (Sgs1 ortholog) has a minor role in long-range DSB end resection; Exo1 dominant
  [PMID:21931565 "Exo1 is largely responsible for extended resection up to 3.1 kb from a DSB, with an activity dependent on Rqh1 (Sgs1) DNA helicase having a minor role."]
- HR repair of IR-induced DSBs in G2; Rqh1-Top3 processes recombination intermediates downstream of Rhp51 foci; controlled by Cdc2-cyclin B via Crb2
  [PMID:12023299 "Rqh1, in association with Top3, processes recombination intermediates that are channeled into this pathway"]
- fbh1Δ rqh1Δ double mutant is lethal (suppressed by rhp57Δ) — overlapping roles in processing toxic recombination intermediates
  [PMID:16135799 "fbh1 is essential for viability in stationary-phase cells and in the absence of either Srs2 or Rqh1 DNA helicase. In each case, lethality is suppressed by deletion of the recombination gene rhp57."]

## S-phase checkpoint
- Mus81, Rhp51, Rqh1 form an epistatic pathway required for the S-phase DNA damage checkpoint (replication slowing)
  [PMID:19037101 "Mus81, Rhp51(Rad51), and Rqh1 form an epistatic pathway required for the S-phase DNA damage checkpoint."]
  Original gene cloning: rqh1+ required for reversible S phase arrest [PMID:9184215 title]

## rDNA maintenance / chromosome segregation
- Deletion of Slx1 or Rqh1 provokes rDNA contraction; slx1 rqh1 double is lethal
  [PMID:14528010 "Deletion of Slx1 or Rqh1 RecQ-like DNA helicase provokes rDNA contraction, whereas simultaneous elimination of Slx1-Slx4 endonuclease and Rqh1 is lethal."]
- rqh1Δ delayed in anaphase, lagging chromosomal DNA esp. at rDNA; relieving rDNA fork arrest (reb1Δ) partially suppresses
  [PMID:16303848 "cells lacking Rqh1 are delayed in anaphase progression, and show lagging chromosomal DNA, which is particularly apparent in the rDNA locus ... relieving replication fork arrest in the rDNA repeat by deletion of reb1+ partially suppresses rqh1delta phenotypes ... consistent with the function of the Top3-RecQ complex in maintenance of the rDNA structure"]

## UV damage tolerance / excision repair controversy
- Rqh1 is required for UV damage tolerance/survival during S phase (bypass of damage by replication fork), requires recombination + checkpoint genes + Cds1
  [PMID:9372918 "Rqh1 operates during S phase as part of a mechanism which prevents DNA damage causing cell lethality. This process may involve the bypass of DNA damage sites by the replication fork."]
- CONTROVERSY: rad12-502 was reported to lack SPDE UV-dimer endonuclease (alternative excision repair)
  [PMID:7623848 "the UV-sensitive S. pombe rad12-502 mutant lacks SPDE activity ... the rad12 gene product functions in a DNA repair pathway distinct from NER"]
  BUT the gene's identifiers later refuted this: [PMID:9372918 "in contrast with the reported literature, we do not find that rqh1 (rad12) mutant cells are defective in UV dimer endonuclease activity."]
  => GO:0070914 UV-damage excision repair (from PMID:7623848) is likely an over-annotation/historic
     misattribution of a distinct excision-repair endonuclease function to Rqh1. Treated as
     MARK_AS_OVER_ANNOTATED (the SPDE activity is not a property of the RecQ helicase; the true
     UV phenotype is recombination/replication-bypass based per PMID:9372918).

## Core function synthesis
- MF: ATP-dependent 3'-5' DNA helicase activity (EC 5.6.2.4); ATP binding; ATP hydrolysis; DNA binding.
- CC: nucleus / nuclear chromosome / nucleolus; RecQ-Top3(-Rmi1) complex; site of DSB; nuclear replication fork.
- BP: suppression of inappropriate/hyper-recombination; processing of stalled/collapsed replication forks
  and recovery from replication stress; dissolution of recombination intermediates (double HJ / D-loops)
  with Top3; DSB repair via HR (resection minor role; intermediate processing major role); S-phase DNA
  damage checkpoint (replication slowing); rDNA maintenance & chromosome segregation.
