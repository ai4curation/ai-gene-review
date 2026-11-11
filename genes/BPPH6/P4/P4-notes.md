# P4 (P11125) — Pseudomonas phage phi6

## Overview
- **Gene symbol**: P4
- **UniProt ID**: P11125 (`P4_BPPH6`)
- **Product**: Packaging enzyme P4 (332 AA, 35.0 kDa), encoded on dsRNA segment L.

## Literature & Functional Evidence
- **Hexameric NTPase viral genome packaging motor**: Purified protein P4 is an unspecific nucleoside triphosphatase (hydrolyzing rNTPs, dNTPs, and ddNTPs to NDPs, stimulated by Ca2+/Mg2+ and ssRNA) that forms hexameric rings at the 12 five-fold vertices (portal sites) on the outer surface of the P1 procapsid and drives 5'-to-3' translocation of viral plus-strand ssRNA segments into the procapsid [PMID:7474083, "P4 is an unspecific NTPase hydrolyzing ribo-NTPs, deoxy NTPs, and dideoxy NTPs to the corresponding nucleoside diphosphates. The Km of the reaction for ATP, GTP, and UTP is around 0.2 to 0.3 mM."]; [PMID:7474083, "The nucleotide specificity and enzymatic properties of the P4 NTPase are similar to the NTP hydrolysis reaction conditions needed to translocate and condense the viral positive-sense RNAs to the procapsid particle."].
- **Procapsid localization**: Assembles in 72 copies (12 hexamers) on the outer procapsid surface at the 12 five-fold RNA portal vertices [PMID:23077625, "P4 is the hexameric nucleotide triphosphorylase (NTPase) packaging motor [6]. P4 is assembled on the outer PC surface at the 12 potential RNA portal sites."]; [file:BPPH6/P4/P4-uniprot.txt, "SUBCELLULAR LOCATION: Virion. Note=Capsid protein found in 72 copies. Prior to RNA packaging, localizes on the outer procapsid surface at the 12 potential RNA portal sites."].

## Curation Decisions
- **ACCEPT**:
  - `GO:0017111` (`ribonucleoside triphosphate phosphatase activity`, IDA `PMID:7474083` & IEA `GO_REF:0000120`): Core NTPase activity that powers RNA translocation.
  - `GO:0005524` (`ATP binding`, IEA): P4 binds and hydrolyzes ATP (Km ~0.2-0.3 mM) as well as other NTPs (`PMID:7474083`).
  - `GO:0019072` (`viral genome packaging`, IEA): Core biological process mediated by the P4 hexameric motor.
  - `GO:0046729` (`viral procapsid`, IDA `PMID:23077625`) and `GO:0019028` (`viral capsid`, IEA): P4 is a structural component of the procapsid and remains associated with the mature capsid in 72 copies.
- **TOO_GENERAL**:
  - `GO:0000166` (`nucleotide binding`, IEA): Subsumed by `GO:0005524` (`ATP binding`).
  - `GO:0016787` (`hydrolase activity`, IEA): Subsumed by `GO:0017111` (`ribonucleoside triphosphate phosphatase activity`).
