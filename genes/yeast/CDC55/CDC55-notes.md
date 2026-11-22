# CDC55 (Saccharomyces cerevisiae, UniProt Q00362) - curation notes

## Identity and biochemistry

- Cdc55/YGL190C, 526 aa, seven WD40 repeats (UniProt FT REPEAT 23-62 ... 495-525), disordered loop 390-458,
  phospho-Ser124. PR55/B55 family (InterPro IPR000009); orthologue of human PPP2R2A/B55-alpha. Non-catalytic:
  the two-metal active site is in Pph21/Pph22. Deep research: "Pph21/Pph22 supply the metal-dependent
  catalytic activity, while Cdc55 governs substrate engagement and localization."
  [file:yeast/CDC55/CDC55-deep-research-falcon.md]
- Holoenzyme: Tpd3 (A) + Pph21 or Pph22 (C) + Cdc55 (B). Only two B-type subunits in yeast (Cdc55 = B,
  Rts1 = B'); Rts1 is 10-14x more abundant than Cdc55 and Tpd3 is limiting
  [PMID:12388751 "there is at least 10 times more of one of the regulatory subunits (Rts1p) than the other
  (Cdc55p)"]. Cdc55 localises normally without A or C subunit, so Cdc55 fluorescence does not prove
  assembled holoenzyme at that site [PMID:12388751 "Cdc55p achieved its normal localization in the absence of
  either an A or C subunit"].
- Holoenzyme assembly with Cdc55 is coupled to Rrd2/Tpd3-dependent maturation and Ppm1 methylation of the C
  subunit [PMID:17550305 "deletion of PPE1 in an rrd1Δ/rrd2Δ strain increases holoenzyme assembly with the
  B-type subunit CDC55 without generation of the active C subunit"]. The cdc55Δ rts1Δ double mutant (no
  B-type subunits) is the comparator in that paper - basis of the IGI GO:0019888 row (WITH RTS1).
- The 1996 ceramide paper (PMID:8600023) is the source of the IDA/IMP PP2A-complex rows. It reports
  Tpd3 + Cdc55 as regulatory subunits of a ceramide-activated phosphatase but assigns the catalytic subunit
  to Sit4 ("a catalytic subunit encoded by SIT4"), which is not the later consensus (Pph21/22). Graded ACCEPT
  for the complex term on the totality of evidence, with the caveat recorded in reference_review.
- TOR link: Cdc55/Tpd3 compete with phosphorylated Tap42 for the C subunit and promote Tap42
  dephosphorylation [PMID:10329624 "phosphorylated Tap42 effectively competes with Cdc55/Tpd3 for binding to
  the phosphatase 2A catalytic subunit"]. Source of the Complex Portal IPI row.

## Localisation (all from functional, chromosomally integrated GFP fusions)

- Nucleus in >90% of cells at all stages [PMID:12388751 "GFP-Cdc55p localized to the nucleus in >90% of all
  cells"]; more nuclear in G1/G2 than in mitosis [PMID:21536748 "In wild-type cells, Cdc55-GFP was more
  concentrated in the nucleus for cells both in G1 and G2 than cells in mitosis"].
- Bud tip (smallest to medium buds), bud neck (53% of post-telophase cells), shmoo tip, vacuolar membrane
  (FM4-64 colocalisation) [PMID:12388751]. Tpd3 needs Cdc55 to reach the bud tip
  [PMID:12388751 "Most strikingly, in cdc55Δ cells, GFP-Tpd3p was rarely found at bud tips"].
- Cytoplasmic/cortical pool requires Zds1/Zds2; without them Cdc55 accumulates in the nucleus
  [PMID:21536748 "Cortical and cytoplasmic localization of Cdc55 requires Zds1/Zds2, and Cdc55 accumulates in
  the nucleus in the absence of Zds1/Zds2."]. Igo1/2 deletion also increases nuclear Cdc55 (Juanes 2013).

## Regulators that act through Cdc55

- Zds1/Zds2: bind Cdc55 directly via the C-terminal ZH4 domain [PMID:20980617 "ZH4 is shown by protein
  affinity assays to be necessary and sufficient for interaction with Cdc55p"]; stoichiometric, constitutive
  complex [PMID:18762578 "Zds1 immunoprecipitates from cells released into synchronous anaphase contained
  similar amounts of Cdc55 and Tpd3 compared with immunoprecipitates in metaphase"]. They keep Cdc55 in
  the cytoplasm (promoting entry) and out of the nucleus (permitting exit) [PMID:21536748].
- Separase (Esp1): interacts with Cdc55 independently of Zds1/2 and down-regulates PP2A-Cdc55 at anaphase
  onset [PMID:16713564 "The sister chromatid-separating protease separase, activated at anaphase onset,
  interacts with and downregulates PP2A(Cdc55)"; PMID:18762578 "Therefore separase interacts with Cdc55
  independently of Zds1 and Zds2."]. These are the two Esp1 "protein binding" IPI rows (REMOVED as
  uninformative; interaction itself is not disputed).
- Rim15 -> Igo1/Igo2 (endosulfines): phospho-Igo1 binds Cdc55 in late S/G2 and inhibits PP2A-Cdc55 in vitro
  [PMID:23861665 "Phosphorylated Igo1 inhibits PP2A(Cdc55) activity in vitro and induces mitotic entry in
  Xenopus egg extracts"]; in quiescence, Rim15-phosphorylated endosulfines directly inhibit PP2A-Cdc55 to
  keep Gis1 phosphorylated [PMID:23273919]. Paradox: igo1Δ igo2Δ cells have LESS PP2A-Cdc55 activity
  [PMID:23861665 "Surprisingly, deletion of IGO1 and IGO2 in yeast cells leads to a decrease in PP2A
  phosphatase activity, suggesting that endosulfines act also as positive regulators of PP2A in yeast."].
- Myo5: three IntAct-derived protein-binding rows (Gavin 2002, Gavin 2006, Tonikian 2009 SH3 interactome).
  Tonikian full text does not mention Cdc55. All REMOVED under the protein-binding policy.

## Mitotic entry (sign is opposite to metazoa)

- PP2A-Cdc55 PROMOTES G2/M: dephosphorylates/activates Mih1 and opposes initial Cdk1 phosphorylation of Swe1
  [PMID:23861665 "In stark contrast to other organisms, budding yeast PP2ACdc55 promotes, rather than
  prevents, timely entry into mitosis by participating in the positive feedback loop for Cdk1 activation";
  "In addition, PP2ACdc55 dephosphorylates and activates Mih1"]. cdc55Δ, zds1Δ zds2Δ and cdc55-NLS are
  elongated with Tyr19-phosphorylated Cdc28; rescued by swe1Δ [PMID:21536748 "Our genetic data suggest that
  the critical target of Cdc55 in mitotic entry is Swe1 ..."]; cdc55-NES is fully competent and bypasses
  Zds1/2 [PMID:21536748 "we showed that Cdc55 promotes mitotic entry when in the cytoplasm"].
- The Yasutis 2010 IGI rows (GO:0044818 mitotic G2/M transition checkpoint, WITH ZDS1 / ZDS2) read the same
  circuit with the opposite sign: cdc55Δ rescues zds1Δ zds2Δ elongation, GAL-ZDS1/2 cannot bypass the
  cdc24-1 checkpoint in cdc55Δ, and their model states "Cdc55p normally inhibits mitotic progression and the
  Zds proteins inhibit Cdc55p." Rossio 2011 reinterprets the zds1Δ zds2Δ phenotype as loss of the
  cytoplasmic pool ("The G2 delay is not caused by the nuclear accumulation of Cdc55 because the elongated
  bud morphology of cdc55-NLS was rescued by an extra copy of CDC55"). Decision: GO:0010971 IMP = ACCEPT
  (core); GO:0044818 IGI x2 = KEEP_AS_NON_CORE (curator read full text; sign is context-dependent);
  ARBA IEA GO:0010972 (negative regulation, transferred from metazoan B55) = MODIFY -> GO:0010389
  (sign-neutral parent), propagation_review REGULATORY_SIGN_INVERSION + LINEAGE_OR_TAXON_MISMATCH.

## Mitotic exit, FEAR and the spindle assembly checkpoint (core)

- PP2A-Cdc55 keeps Net1 underphosphorylated in metaphase, retaining Cdc14 in the nucleolus
  [PMID:16713564 "Here, we show that PP2A(Cdc55) phosphatase keeps Net1 underphosphorylated in metaphase."].
  Separase + Zds1/2 down-regulate it at anaphase onset [PMID:18762578 "Ectopic Zds1 expression in turn is
  sufficient to down-regulate PP2A(Cdc55) and promote Net1 phosphorylation."]. Nuclear Cdc55 blocks exit
  [PMID:21536748 "On the other hand, nuclear Cdc55 prevents mitotic exit."].
- Yellman & Burke: cdc55Δ suppresses lte1 spo12 lethality; releases Cdc14 prematurely in nocodazole, with
  bub2Δ-like Pds1 degradation and cohesion loss; unperturbed cycle timing is normal
  [PMID:16314395 "We show that Cdc55 is a negative regulator of mitotic exit."; "The loss of Cdc55 did not
  disrupt the timing of mitosis in an unperturbed cell cycle."; "This suggested that the checkpoint role of
  Cdc55 was not direct inhibition of APC Cdc20 as it is for Mad2."]. -> GO:0001100 IMP ACCEPT (core).
- Rossio 2013 (abstract only): nuclear PP2A-Cdc55 keeps APC-Cdc20 dephosphorylated during SAC arrest; SAC-
  specific alleles; Zds1/2 restrain SAC by excluding Cdc55 from the nucleus [PMID:23886942 "APC-Cdc20 is
  kept inactive by dephosphorylation by nuclear PP2A-Cdc55 when spindle is damaged"]. Sake strain K1801
  SAC defect = Cdc55 R48P [PMID:27191586]. -> GO:0090266 IMP x2 ACCEPT; GO:0005634 is_active_in ACCEPT.
- Meiosis: FEAR-independent role in reductional segregation revealed only in spo11Δ spo12Δ
  [PMID:27455870 "We suggest that Cdc55 is required for reductional chromosome segregation during
  achiasmate meiosis and this is independent of its FEAR function."; "they have no effect on chromosome
  segregation during wild type meiosis."]. GO:0045143 IGI = KEEP_AS_NON_CORE. GO:0000705 "achiasmate
  meiosis I" is defined for constitutive absence of chiasmata (organism-level), so spo11Δ yeast is out of
  scope -> MODIFY to GO:0045143.

## Nutrient signalling branch (non-core rows)

- Autophagy: PP2A-Cdc55 and PP2A-Rts1 redundantly dephosphorylate Atg13 after TORC1 inactivation
  [PMID:27973551 "These indicated that PP2A-Cdc55 and PP2A-Rts1 have a redundant function in induction of
  TORC1 inactivation-induced (nonselective) autophagy."] -> GO:2000786 IGI (WITH RTS1) KEEP_AS_NON_CORE.
- Microautophagy / ESCRT-0: [PMID:32029270 "Loss of PP2A-Cdc55 compromised vacuolar localization of Hse1,
  but not Vps27."] -> GO:0016237 and GO:1905477 KEEP_AS_NON_CORE (no "regulation of microautophagy" child in
  GO; no "positive regulation of protein localization to vacuolar membrane" term).
- Msn2/4 stress transcription: sustained nuclear retention + chromatin recruitment, Hog1-independent, Msn2
  phosphosites unchanged [PMID:23275436 "Thus, based on our analyses, the initial dephosphorylation of Msn2
  is not controlled by PP2A-Cdc55."] -> GO:0061586, GO:1900182, GO:0071475 all KEEP_AS_NON_CORE.
- Quiescence: Rim15/Igo1-2 inhibition of PP2A-Cdc55 preserves Gis1 phosphorylation [PMID:23273919]. Not in
  GOA; covered in core function 3 and the description, no NEW term proposed.

## Not cached (from deep research only; not used as supporting_text)

- Baro 2018 (GigaScience) SILAC phosphoproteome: 62 significant Cdc55-dependent phosphopeptides on 55
  proteins, Cdk1-Tyr19 hyperphosphorylated in cdc55, Slk19/Lte1/Zeo1 candidates.
- Philip 2022 (eLife): PP2A-Cdc55 removes Cdc6 Thr7/Thr23 phosphorylation ahead of origin licensing.
- Kruse 2024 (Sci Adv): conserved B55 helix-docking patches; Zds1 C-terminal helix modelled into the pocket.
- Watanabe 2019 (AEM): CDC55 deletion abolishes the enhanced fermentation of rim15-deficient sake strains.
- Pal 2008 / Wicky 2011: Mih1 hyperphosphorylated in cdc55Δ; Zds1 binds PP2A exclusively through Cdc55.

## Decision summary

- ACCEPT 16, KEEP_AS_NON_CORE 13, REMOVE 5 (all GO:0005515), MODIFY 3 (GO:0000705 -> GO:0045143;
  GO:0010972 IEA -> GO:0010389; GO:1902531 IEA -> GO:0090266). No UNDECIDED, no NEW.
- Core functions: (1) nuclear substrate adaptor for Net1/APC-Cdc20 - negative regulation of mitotic exit and
  SAC maintenance; (2) Zds-anchored cytoplasmic regulator activity promoting G2/M via Mih1/Swe1;
  (3) endosulfine-gated TORC1-downstream phosphatase regulator (Tap42, Atg13, ESCRT-0, quiescence).
- Validator warnings left: GO:0140767 and GO:0006470 in core_functions have no existing_annotations row
  (deliberate; the MF adaptor term is the same choice made in the human PPP2R2A review).
