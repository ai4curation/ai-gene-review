# TRX1 (P22217, YLR043C) notes

## Identity and activity
- Cytoplasmic thioredoxin; paralog TRX2; mitochondrial TRX3 separate [UniProt:P22217 "Yeast has two cytoplasmic thioredoxins, TRX1 and TRX2, and one mitochondrial, TRX3."]
- TRX1/TRX2 78% identical, CGPC active site [PMID:1988444 "Thioredoxins I and II show 78% amino acid sequence identity"]
- Reduced thioredoxin is the cosubstrate of PAPS reductase [PMID:3060034 "Reduced thioredoxin is required as cosubstrate"]
- trx1 trx2 double mutant: methionine auxotroph, long S phase [PMID:2026619 "Surprisingly, the loss of both thioredoxins also leads to methionine auxotrophy"]
- One of TRX1/TRX2/GRX1/GRX2 required for viability; glutaredoxin backup for PAPS reductase under low ROS [PMID:10844700 "we present evidence for the existence of a novel yeast hydrogen donor for PAPS reductase"]
- GSSG reduction by Trx1 (structure/kinetics) [PMID:19362171 "These findings gave us the structural insights into GSSG reduction catalyzed by the Trx system"]
- Deglutathionylase [PMID:20074363 "thioredoxins, but not glutaredoxins, catalyse deglutathionylation of model glutathionylated substrates"]
- Overlapping redox homeostasis role with TRX2 [PMID:22561702 "demonstrating that the Trxs have overlapping roles in redox homeostasis"]

## LMA1 (redox-independent)
- Most Trx is in LMA1 [PMID:8603912 "Most of the thioredoxin of yeast is in this complex rather than the well-studied monomer"]
- LMA1 = thioredoxin + I(B)2/Pbi2; no redox chemistry needed [PMID:9015301 "the thioredoxin subunit is not acting through redox chemistry"]
- LMA1 binds vacuoles via Sec18, transfers to Vam3 complex [PMID:9657146 "Upon Sec18p ATP hydrolysis, LMA1 transfers to (and stabilizes) a Vam3p complex"]
- In vitro ER-Golgi and retrograde transport reconstitution uses purified LMA1 [PMID:9813082 "including Sec18p, the Lma1p complex, Uso1p, coatomer, and Arf1p"]

## Localization
- Cytosol/nucleus (GFP) [PMID:14562095]; IMS minor pool [PMID:22984289 "some proteins are likely dually localized between cytosol and mitochondrial IMS, including the cytoplasmic thioredoxin Trx1"]
- UniProt Golgi membrane EXP cites PMID:22984289, but that full text has no Golgi data -> UNDECIDED.

## Decisions
- Core: GO:0015035 in cytosol/nucleus; BP cell redox homeostasis, protein deglutathionylation; sulfate assimilation (added NEW: GOA has it for TRX2 only).
- Protein binding (Trx1-Trx2, HT) removed. ER/Golgi transport kept non-core (in vitro LMA1).
- YeastCyc: no gene on thioredoxin reactions in THIOREDOX-PWY or SO4ASSIM-PWY; no YeastPathways RCA rows for TRX1.
