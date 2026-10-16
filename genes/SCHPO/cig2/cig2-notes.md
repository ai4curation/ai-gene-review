# cig2 (SPAPB2B4.03, P36630) review notes

## Identity / overview
Cig2 (synonym Cyc17) is the major S-phase (G1/S) B-type cyclin of fission yeast, cyclin A/B
subfamily (UniProt). Non-essential: Cig1, Puc1 and above all the mitotic cyclin Cdc13 can
substitute for it. UniProt still calls it "G2/mitotic-specific cyclin cig2" (the name comes from
the 1993 Bueno & Russell paper), but every subsequent study places its physiological role at
G1/S. Deep research (falcon provider) was present and was used; it draws mainly on
Martín-Castellanos et al. 1996 (EMBO J, not in the local publication cache), Fisher & Nurse 1996,
Pickering et al. 2017 (bioRxiv) and the Kawamukai 2024 review.

Interactor identities used in the GOA WITH/FROM columns (resolved from the repo's UniProt files):
- PomBase:SPBC11B10.09 / UniProtKB:P04551 = cdc2 (CDK1)
- PomBase:SPCC18B5.03 = rum1 locus id used by PomBase for the IGI; UniProtKB:P40380 = rum1
- PomBase:SPBC582.03 = cdc13
- PomBase:SPAC22F3.09c / UniProtKB:P41412 = res2; UniProtKB:P33520 = res1
- UniProtKB:P87060 = pop1 (F-box protein, SCF-Pop1)
- PomBase:SPBC2G2.09c (in the IBA MTOC donor list) = crs1, the meiosis-specific cyclin, NOT cig1

## Core function: S-phase cyclin that activates Cdc2 for Start / S-phase onset
- [PMID:8657126 "These studies indicate that Cig2 is the primary S-phase-promoting cyclin in S. pombe but that Cdc13 can effectively substitute for Cig2 in deltacig2 cells."]
- [PMID:8657126 "Cig2 protein and Cig2-associated kinase activity appear soon after the completion of M and peak during S"]
- [PMID:8657126 "Unlike deltacdc13 cells, double-mutant deltacdc13 deltacig2 cells are defective in undergoing multiple rounds of DNA replication."]
- [PMID:8631306 "Further deletion of cig1 and puc1 had no effect, but deletion of cig2/cyc17 caused a severe delay in re-replication. Deletion of cig1 and cig2/cyc17 together abolished re-replication completely and cells arrested in G1."]
- [PMID:9552380 "cig2 is the major G1 cyclin while cdc13 is the principal mitotic cyclin."]
- [PMID:9614176 "and with S-phase B-cyclins to trigger S-phase, usually cig2p in fission yeast"]
- Deep research: Cig2-HA immunoprecipitates carry histone H1 kinase activity that is lost in a
  cdc2-33 background, so the catalytic activity is Cdc2's (Martín-Castellanos et al. 1996; not cached).

## Regulation by Rum1 and cell size (Start control)
- [PMID:9552380 "the rum1 inhibitor, a protein present exclusively in G1, prevents premature activation of the cdc2/cig2 and the cdc2/cdc13 complexes until cells have reached the critical cell size required to pass Start and initiate a new cell cycle."]
- [PMID:9614176 "it binds both cdc13p and cig2p and is specifically required for cdc13p proteolysis"]
- [PMID:9614176 "cig2p cyclin degradation does not require rum1p, even though rum1p can associate with cig2p"]
- Deep research: cig2 deletion delays G1 exit particularly in small cells and in sensitized cdc2
  backgrounds (cdc2-56 cig2delta ~40% G1 arrest at 36.5C), consistent with the size-control term.

## Pheromone-induced G1 arrest acts on Cig2-Cdc2
- [PMID:9034336 "Pheromone inhibits the p34cdc2 kinase associated with both the G1-specific B-type cyclin p45cig2 and the B-type cyclin p56cdc13 and overexpression of p45cig2 or p47cdc13delta90 overcomes the pheromone-induced G1 arrest."]
- [PMID:9034336 "We suggest that onset of S-phase is controlled by pheromone inhibiting the B-cyclin-associated kinase in G1"]

## MBF transcription and the Cig2 feedback loop
- [PMID:11781565 "We report here that the cell-cycle-regulated expression of the cyclin cig2 gene is dependent on MBF."]
- [PMID:11781565 "Cig2p can bind to Res2p, promote the phosphorylation of Res1p and inhibit MBF-dependent gene transcription."]
- [PMID:11781565 "Cig2p thus forms an autoregulating feedback-inhibition loop with MBF which is important for normal regulation of the cell cycle."]
- [PMID:7909513 "Only the poly(A)+ species is expressed during vegetative growth and periodically with a peak in the G1 and S phases of the cell cycle."]

## Proteolysis (APC/C and SCF-Pop1/Pop2)
- [PMID:14970237 "Here we show that fission yeast S phase cyclin Cig2 is ubiquitylated and degraded via both the SCF and the APC/C. Cig2 instability during G(2) and M phase is dependent upon the SCF complex, whereas the APC/C is responsible for Cig2 destruction during anaphase and G(1), thereby ensuring a spike pattern of Cig2 levels, peaking only at S phase."]
- [PMID:14970237 "Pop1 binds Cig2 in vivo. An in vitro binding assay shows that an internal 93 amino acid residues comprising a part of the cyclin box are necessary and sufficient for this binding. Cig2 phosphorylation is also required for interaction with Pop1."]
- UniProt: destruction box 51-60 (R51A/L54A stabilises), Cdc2-binding residues R169/E170/I171
  (PMID:11163211, not cached).

## Sexual differentiation
- [PMID:7909513 "Deletion of cyc17+ markedly enhances conjugation, despite the presence of nitrogen source, and accelerates growth arrest in G1 upon nitrogen starvation. Conversely, overexpression of the cyc17+ gene strongly inhibits conjugation."]
- [PMID:7909513 "This cyclin, named Cyc17, is highly homologous with Cdc13, but has no detectable activity as a mitotic cyclin."]
- Cyc17 was isolated as an extragenic suppressor of pat1-114 (overexpression blocks the Pat1-inactivation-driven entry into meiosis).

## Meiosis
- [PMID:26804917 "During meiosis, Fkh2 is phosphorylated in a CDK/Cig2-dependent manner, decreasing its affinity for DNA, which creates a window of opportunity for Mei4 binding to its target genes."]
- [PMID:30640914 "Single deletion mutants of cig1 and cig2 were defective in recombination, with a moderate reduction in gene conversion (26% p value 0.004 and 27% p value 0.016, respectively), and without additive effects in the double cig1 cig2 mutant (33% reduction; p value 0.025), suggesting that both cyclins might act in the same genetic pathway"]
- [PMID:30640914 "we have found that cig1 and cig2 cyclin deletion mutants are indeed impaired in meiotic recombination, and NCOs reduced 26% compared to the control levels observed in wild-type strains. Correspondingly, DSB formation is also reduced to a similar extent at the hotspot of reference mbs1, 28% and 25% respectively."]
- The DSB reduction in cig2 alone is not statistically significant (p 0.21); crossovers are unchanged.

## Localization
- [PMID:16823372 ORFeome YFP screen; PomBase HDA: nucleus and mitotic spindle pole body.]
- [PMID:12419251 "We show that in fission yeast the mitotic B type cyclin Cdc13/Cdc2 kinase associates with replication origins in vivo."] The cached record is abstract-only and does not
  mention Cig2; PomBase's IDA chromatin annotation for cig2 rests on the full text (origin ChIP of
  Cig2), which is consistent with Cig2-Cdc2 acting at origins at S phase. Deferred to the curator.
- Deep research notes that direct high-resolution localization data for Cig2 are limited.

## Mitosis?
- [PMID:8455610 "Disruption of cig2 delays the onset of mitosis, to the degree that a cig2 null allele rescues mitotic catastrophe mutants"] and [PMID:8455610 "These data indicate that Cdc13 and Cig2 interact with Cdc2 to carry out different functions in mitosis."] - the 1993 interpretation;
  later work (Obara-Ishihara 1994; Mondesert 1996; Fisher & Nurse 1996) showed no mitotic cyclin
  activity in wild-type cells, but deregulated Cig2-Cdc2 can drive (catastrophic) mitosis when
  Wee1/Mik1 inhibitory phosphorylation is removed (Pickering et al. 2017, deep research).

## GO annotation decisions (summary)
- MF: GO:0061575 activator activity (IDA x2, IGI) and GO:0016538 regulator (IBA, IEA): ACCEPT, core.
- GO:0005515 protein binding (6 IPI rows): res1/res2 rows (PMID:11781565) and cdc2 row
  (PMID:8455610) MODIFY -> GO:0016538 (cyclin docking the kinase on Cdc2 / on its MBF substrate);
  pop1 row (PMID:14970237, Cig2 is the SCF substrate) and rum1 row (PMID:9614176, Cig2-Cdc2 is the
  CKI target) REMOVE as uninformative; the interactions themselves are not disputed.
- BP: G1/S transition (IBA), positive regulation of G1/S (IMP x3, IGI), traversing Start (IBA, IGI),
  G1 cell size control checkpoint signaling (IGI x2): ACCEPT, core. Mitotic cell cycle phase
  transition (IEA): ACCEPT (general). Negative regulation of conjugation (IMP), regulation of
  mitotic-to-meiotic switching (IMP), regulation of reciprocal meiotic recombination (IMP):
  KEEP_AS_NON_CORE.
- CC: CDK holoenzyme complex (EXP, IBA), nucleus (HDA, IBA, IEA), chromatin (IDA): ACCEPT.
  Mitotic SPB (HDA), SPB (IEA), MTOC (IBA): KEEP_AS_NON_CORE. Cytoplasm (IBA): KEEP_AS_NON_CORE
  (no cig2-specific cytoplasmic activity; only the SPB pool).
- No NEW terms proposed. The MBF feedback inhibition is described in core_functions (under the
  Start control point term GO:0007089) but no transcription-regulation process term is asserted:
  a QuickGO check (2026-09-26) shows that PomBase annotates neither cig2 nor cdc2 nor cdc13 to any
  transcription term, so the absence is a curation convention (the CDK regulates the transcription
  factor) rather than a gap; raised in suggested_questions instead.
