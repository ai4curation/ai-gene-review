# msl-2 (P50534) review notes

## Identity and regulation
- RING-finger protein; male-specific; ectopic expression assembles MSL on female X. [PMID:7781064 "Ectopic expression of msl-2 in females results in the appearance of the other MSL dosage compensation regulators on the female X chromosomes and decreased female viability."]

## DNA recognition / targeting
- CXC domain binds DNA [PMID:20139418 "We now show that recombinant MSL2, through its CXC domain, directly binds DNA with low nanomolar affinity."]
- CXC recognizes MRE [PMID:25452275 "we identified the CXC domain of MSL2 specifically recognizing the MRE motif"]; PionX [PMID:27580037 "Specificity is provided by the CXC domain, which binds a novel motif defined by DNA sequence and shape."]
- CLAMP interaction redundancy [PMID:31320325 "proper MSL2 positioning requires an interaction with either CLAMP or DNA to initiate dosage compensation in Drosophila males"]

## roX binding / condensates
- [PMID:33208948 "roX non-coding RNAs and the MSL2 CTD form a stably condensed state"]
- [PMID:23870142 "MLE RNA helicase and MSL2 ubiquitin ligase, bind evolutionarily conserved domains containing tandem stem-loops in roX1 and roX2 RNAs in vivo"]

## E3 ligase
- [PMID:23084834 "MSL2 is an E3 ligase that ubiquitylates itself and the other associated components when their stoichiometry is unbalanced"]
- H2B K34 [PMID:21726816 "MSL2, together with MSL1, has robust histone ubiquitylation activity that mainly targets nucleosomal H2B on lysine 34 (H2B K34ub)"]
- MOF substrate [PMID:28510597 "MSL2 ubiquitylates itself as well as MOF, MSL1 and MSL3."]

## Curation decisions
- DNA binding rows MODIFY -> GO:1990837 (already IDA).
- GO:0046536 MODIFY -> GO:0016456.
- E3 ligase GO:0061630 ACCEPT on all rows (histone + non-histone substrates); H2B-specific activity captured by GO:0141054 (ACCEPT).
- Shared MSL convention: MSL complex + GO:0016456 ACCEPT; chromosome MODIFY -> X chromosome; nuclear chromosome and nucleus ACCEPT (free nuclear MSL pool, PMID:21551218; autosomal 4th-chromosome binding, PMID:25501352); chromatin binding KEEP_AS_NON_CORE.

## Deep research (falcon, added after initial review)
- `msl-2-deep-research-falcon.md` agrees: MSL2 initiates and organizes the MSL complex on the male X; its CXC domain reads GA-rich MREs ["Its CXC zinc-binding domain recognizes GA-rich MSL recognition elements (MREs) at chromosomal entry or high-affinity sites (CES/HAS)."]. It notes the fly H2B acceptor is proposed to be K31 (K34 characterized mainly with mammalian MSL1-MSL2), and that MSL2 ubiquitylates MSL1, MOF, MSL3 and itself. No annotation decisions changed.
