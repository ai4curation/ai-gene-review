# C3H15 (CDM1, AtC3H15, At1g68200) — curation notes

UniProt Q9C9F5 (C3H15_ARATH), 308 aa. UniProt primary gene name is C3H15; CDM1
(CALLOSE DEFECTIVE MICROSPORE 1) is the synonym from Lu et al. 2014. Folder named
C3H15 to follow the UniProt `GN Name=` convention used for other ARATH reviews.

## Identity and family

- Tandem CCCH zinc-finger (TZF) protein; two C3H1-type fingers (UniProt FT ZN_FING
  222..250 and 260..288, PROSITE-ProRule PRU00723). InterPro IPR045877 ZFP36-like;
  PANTHER PTHR12547:SF162.
- Closest Arabidopsis paralog: C3H14 (At1g66810). Duplicated pair
  [PMID:18221561 "AtC3H14 and AtC3H15, AtC3H30 and AtC3H56"].
- Sequence-similar to human TIS11D/TTP TZF domains
  [PMID:18221561 "AtC3H14, AtC3H15, OsC3H9 and OsC3H39 share high amino acid sequence identities with TIS11D"].
- Comparator check (QuickGO, 2026-10-23): human ZFP36 and ZFP36L1 carry P-body
  (GO:0000932) by IDA; ZFP36L2 carries 3'-UTR-mediated mRNA destabilization
  (GO:0061158) by IMP. So the RNA-decay terms proposed for C3H15 are the terms GO
  uses for this family.

## Literature, chronological

### Lu et al. 2014 (PMID:24567187, full text cached)
- CDM1 transcript ≥100-fold higher in stage 4–7 anthers than other tissues; in situ
  signal in meiocytes and tapetum.
- SALK_065040 (cdm1): T-DNA in exon 2, after the first CCCH finger;
  [PMID:24567187 "potentially producing a truncated protein lacking the second CCCH domain"].
  Homozygotes completely male sterile, female fertile; recessive.
- Phenotype: callose wall between microspores thin; callose dissolution abnormal;
  exine defective. Expression changes: CalS5, CalS12 down; A6, MYB80 up at stages
  4–7, then A6 down after stage 8.
- **Discrepancy:** Chai et al. 2015 (PMID:25732536) and later papers report that
  single c3h14 or c3h15 T-DNA mutants are fertile and only double mutants lose
  pollen. Lu et al. may have used a different allele; the truncated protein from
  SALK_065040 might behave differently from a null. Not resolved from abstracts;
  I have not seen which c3h15 allele Chai 2015 used.

### Kim et al. 2014 (PMID:25228083, abstract only) — about C3H14
- C3H14 binds ssDNA, dsDNA and ribohomopolymers; RIP identified target mRNAs;
  yeast activation assay showed transactivation. C3H15 is only in the UniProt
  tissue-specificity line citing this paper; the abstract does not describe C3H15
  experiments.

### Chai et al. 2015 (PMID:25732536, abstract only)
- C3H14/C3H15 redundantly regulate secondary wall thickening and anther
  development. Double mutants: few pollen grains, thinner stem secondary walls.
  Overexpression of either: thicker walls, ectopic secondary wall deposition.

### Chai et al. 2022 (PMID:35139225, full text cached) — source of EXP nucleus/cytoplasm
- C3H15 negative regulator of BR signalling downstream of BRI1; c3h14 c3h15
  suppresses bri1-5 dwarfism.
- BIN2 phosphorylates C3H15 at Ser111 (UniProt MOD_RES 111); cytoplasmic
  retention; BR causes dephosphorylation and nuclear accumulation (fractionation +
  GFP imaging).
- DNA binding: EMSA identifies G-rich CHRE motif (GGGAGA); ChIP-qPCR on BZR1, BES1,
  SAUR15, XTH33 etc. promoters; BR increases binding in vivo.
- Protoplast proSAUR15:GUS repressed by C3H15.
  [PMID:35139225 "C3H15 acts as a transcriptional repressor and inhibits cell elongation by binding to the CHRE sites"]

### Wang et al. 2020 (PMID:32279333), Wang et al. 2022 (PMID:35736512) — abstracts
- Defence phenotypes mostly studied for C3H14; c3h14 c3h15 double mutant more
  susceptible to Botrytis, more resistant to Pst DC3000. MPK4 phosphorylation shown
  for C3H14. Not annotated for C3H15 (paralog-focused, double-mutant only).

### Chai et al. 2024 (PMID:38865085, abstract only)
- Heat suppresses C3H15 transcription; C3H15 represses HSFA2; MBR2 (RING E3)
  ubiquitinates phosphorylated C3H15 in cytoplasm; heat → C3H15 in stress granules.

### Andrés-Bordería et al. 2024 (PMID:39276674, abstract only)
- Proposes C3H15 as post-transcriptional modulator of Cu/Zn homeostasis (SPL7,
  PETE2 expression). Correlative; not annotated.

### Xue et al. 2026 (PMID:41758611, abstract only)
- C3H14/15 highly expressed in microspore mother cells at zygotene–pachytene, bind
  highly expressed mRNAs; double loss → DNA:RNA hybrids, pachytene arrest, cell
  death. C3H15 in P-bodies through DCP1 interaction.

### Chen et al. 2026 (PMID:42711403, abstract only)
- C3H14/C3H15 maintain meiocyte identity by eliminating archesporial/tapetal
  transcripts; interact with P-body proteins and CCR4-NOT; conserved in soybean and
  rice.

### Gao et al. 2026 (PMID:42844995, full text cached)
- RNA-EMSA: recombinant C3H15 binds the poly(U) region of the IAMH2 3' UTR; LUC
  reporter with IAMH2 3' UTR repressed by C3H15 co-expression; IAMH2 mRNA elevated
  in c3h14 c3h15; IAMH2 epistatic for hypocotyl length.

## GOA reference papers (screens)
- PMID:21245844 (Brady 2011) and PMID:30356219 (Gaudinier 2018) are Y1H network
  screens; IPI rows "with" AT2G03500 (EFM/HHO4) and AT3G26810 (AFB2) = promoters
  bound. AT1G68200 is not named in the cached main text of PMID:21245844
  (supplementary tables not examined); PMID:30356219 is abstract only.
- PMID:11118137 (Riechmann 2000) is a genome-wide TF catalogue; it classified C3H
  proteins as TFs by domain. Abstract only; C3H15 not discussed in the abstract.

## Synthesis
Two well-supported activities:
1. Sequence-specific mRNA 3'-UTR binding that promotes mRNA decay (P-body, DCP1,
   CCR4-NOT), conserved TZF mechanism. Strongest direct evidence for C3H15 itself:
   RNA-EMSA + reporter (PMID:42844995). Biological contexts: male meiocyte
   transcript clearance (microsporogenesis), IAMH2 in hypocotyls.
2. Nuclear, BR-gated DNA binding to G-rich CHRE elements and transcriptional
   repression (PMID:35139225), opposing BZR1/BES1.
Which activity underlies the secondary-wall, heat, defence and metal phenotypes is
not established.

## Deep research
`just deep-research-falcon` failed: falcon and perplexity providers not configured
in this environment ("Provider 'falcon' not available. Available: openscientist").
OpenScientist was launched instead.
