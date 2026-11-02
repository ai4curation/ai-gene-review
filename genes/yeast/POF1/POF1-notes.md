# POF1 (YCL047C, P25576) notes

Module context: `nad_de_novo_and_salvage_fungal`, variant pof1_nmn_adenylyltransferase_variant (family PANTHER:PTHR31285 with S. pombe SPAC694.03), MF GO:0000309. Module notes POF1 is not listed by YeastCyc; confirmed: POF1 is absent from the YeastPathways summary (no RCA rows). No S. cerevisiae GO-CAM; the S. pombe NAD+ GO-CAM (698e557b00000821) types SPAC694.03 as GO:0000309 in cytosol, consistent.

## Evidence
- [PMID:24759102 "Unlike other yeast NMNATs, Pof1 exhibits NMN-specific adenylyltransferase activity."]; kinetics [PMID:24759102 "A steady-state kinetic study was conducted on the conversion of NMN to NAD + by rPof1."]; Km NMN 2.26 mM, pH optimum 10 [UniProt:P25576].
- Not NaMN: [PMID:24759102 "In addition, if Pof1 could adenylylate NaMN, the nma1 Δ nma2 Δ mutant would not be lethal without NR supplement ( Fig."].
- Genetics: [PMID:24759102 "In the nma1 Δ nma2 Δ mutant, Pof1 is essential for growth on NR ( Fig."]; [PMID:24759102 "Deletion of POF1 significantly lowers NAD(+) levels and decreases the efficiency of NR utilization, resistance to oxidative stress, and NR-induced life span extension."].
- Location: [PMID:24759102 "Similar to Nma1, Nma2, and other salvage enzymes ( 25 ), Pof1 is localized both in the cytoplasm and the nucleus ( Fig."].
- ATPase/ERAD (Costa 2011): weak ATPase [PMID:22204397 "Besides, Pof1p presented an ATPase-specific activity of 5 nmol of released phosphate per hour per μM enzyme (Figure 5A)."]; Ubc7 co-IP; stress sensitivity. No ERAD substrate turnover measured (full text checked).
- Filamentation: high-copy suppressor of kss1 [PMID:21460040 "Overexpression of PTC1 , CAF16 , POF1 , and NSL1 each partially suppressed the phenotype of kss1Δ cells, suggesting that they function independently of or downstream from Kss1."].

## Decisions
- Core: GO:0000309, GO:0034355, cytoplasm + nucleus.
- ATP hydrolysis (IBA self-seeded, IDA) and ERAD (IMP, IPI) -> MARK_AS_OVER_ANNOTATED. Filamentation IGI -> non-core.
- Module: the variant has no `locations` and no `processes`; GO:0034355 (NAD+ salvage) and cytoplasm/nucleus could be added. The module variant's description of NMN coming from NR (Nrk1) fits the evidence.
