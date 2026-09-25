# MIH1 (YMR036C, UniProt P23748) curation notes

## 2026-09-25 — first full review

### Identity
- Sole budding-yeast Cdc25 homolog; MPI phosphatase family, rhodanese fold, PROSITE
  rhodanese domain 261-373, active-site Cys320 (UniProt, by similarity). 554 aa,
  63 kDa (the 1989 paper predicted 54 kDa from a partial/erroneous ORF).
- PANTHER PTHR10828:SF17. PAINT nodes used in the IBA rows: PTN000089071 (G2/M
  process node, MIH1 itself among the descendant evidences) and PTN000850864
  (PTP activity / localisation node).
- The repository module `modules/g2_m_transition.yaml` uses Mih1 as the
  budding-yeast exemplar of the Cdc25 annoton.

### Core biology (cached sources)
- Founding paper: MIH1 cloned as the gene counteracting fission-yeast wee1+ in
  S. cerevisiae [PMID:2649252 "The wee1+ activity is counteracted in S. cerevisiae
  by the gene product of MIH1, a newly identified gene capable of encoding a
  protein of MW 54,000, which is a structural and functional homolog of the cdc25+
  mitotic inducer of fission yeast"]; [PMID:2649252 "Expression of wee1+ in a mih1-
  strain prevents the initiation of mitosis"].
- The mih1 G2 delay is entirely Swe1-dependent [PMID:8253069 "deletion of SWE1 did
  not alter the cell cycle but did eliminate the G2 delay observed in mih1-
  mutants"].
- Reaction: Cdc28-pTyr19 -> Cdc28-Tyr19 [PMID:16688214 "cells unable to activate
  Cdc28 by tyrosine 19 dephosphorylation (Y19) catalyzed by Mih1 (homolog of Cdc25
  phosphatase)"]; [PMID:21536748 "Mih1 phosphatase (Cdc25 homologue) removes this
  inhibitory phosphorylation to promote mitotic entry"].
- Not essential, unlike pombe cdc25 [PMID:22918234 "The S. cerevisiae Cdc25
  phosphatase homolog, Mih1, antagonizes Swe1 Cdk1-Y19 phosphorylation but is not
  essential for mitotic progression, unlike its counterpart in Schizosaccharomyces
  pombe"].
- Morphogenesis checkpoint: [PMID:8930890 "The timing of nuclear division in cells
  that cannot make a bud is exquisitely sensitive to the dosage of SWE1 and MIH1
  genes, which control phosphorylation of Cdc28 at tyrosine 19"]; septin mutants
  [PMID:10805747 "deletion of MIH1 exacerbated the elongated-bud phenotype (Fig. 1
  , panel 6), and these cells arrested permanently with a single nucleus"]; hsl1
  mih1 and hsl7 mih1 double mutants inviable [PMID:10805747 "hsl1Δ mih1 Δ and
  hsl7Δ mih1 Δ strains, which are inviable and arrest in G 2 with extremely
  elongated buds"]; MIH1 overexpression suppresses GAL-SWE1 lethality
  [PMID:9744879 "GAL1::MIH1 rescues the lethality of a GAL1::SWE1 strain grown on
  galactose media"].
- Regulation: hyperphosphorylated in interphase, dephosphorylated at mitotic entry
  [PMID:22918234 "Mih1 is hyperphosphorylated early in the cell cycle and
  dephosphorylated as cells enter mitosis"]; PP2A-Cdc55 is the phosphatase
  [PMID:23861665 "PP2ACdc55 dephosphorylates and activates Mih1"]; cdc55 / zds1
  zds2 mutants keep Mih1 hyperphosphorylated and are rescued by MIH1 overexpression
  [PMID:21536748 "the hyperelongated morphology of cdc55Δ and zds1Δ zds2Δ is
  rescued either by deletion of SWE1 (McMillan et al., 1999a; Yang et al., 2000),
  by overexpression of MIH1 (McMillan et al., 1999a)"]. Cdc5 targets Mih1
  [PMID:20126259 "Cdc5 has recently been shown to target MIH1, the budding yeast
  orthologue of the fission yeast cdc25 phosphatase"]. Mck1 co-precipitates with
  Mih1 [PMID:22918234 "we identify a physical interaction between Mck1 and both
  Clb2 and Mih1"].
- Spindle: [PMID:30072442 "Swe1 and the Polo-like kinase Cdc5 control the balance
  between phosphorylated and unphosphorylated forms of Mih1, which is, in turn,
  important for mitotic spindle elongation"]; [PMID:30072442 "Swe1 and Mih1 are
  both involved in controlling phosphorylation of Bik1"]. Abstract only cached.
- Meiosis (2026, full text cached): [PMID:41927924 "meiosis I entry depends on
  removal of inhibitory phosphorylation controlled by the opposing activities of
  Swe1 and the Mih1 phosphatase"]; [PMID:41927924 "Cdc5 promotes Cdk1 activation
  by inducing Swe1 degradation and facilitating Mih1 nuclear translocation"];
  localisation: [PMID:41927924 "during meiotic prophase I, Mih1 was predominantly
  cytoplasmic and largely excluded from the nucleus. As cells transitioned from
  prophase I to metaphase I, Mih1 progressively accumulated in the nucleus,
  coinciding with SPB separation"].

### Key papers not in the publications cache (PMIDs verified by PubMed esearch/esummary, 2026-09-25)
- Kennedy et al. 2016 Genetics 202:903 "Redundant Regulation of Cdk1 Tyrosine
  Dephosphorylation in Saccharomyces cerevisiae" — PMID:26715668. Per the falcon
  deep-research summary: purified Mih1 directly dephosphorylates Swe1-phosphorylated
  Cdc28-Clb2 in vitro; mih1Δ retains ~65% mitotic Cdk1 activity; Ptp1 and PP2A-Rts1
  are redundant Tyr19 phosphatases; mih1Δ ptp1Δ rts1Δ is lethal unless SWE1 is
  deleted. This is the direct-assay evidence that would justify upgrading the SGD
  ISS PTP row to IDA.
- Keaton et al. 2008 Mol Biol Cell 19:4006 "Nucleocytoplasmic trafficking of G2/M
  regulators in yeast" — PMID:18562688. Mih1-12Myc mostly cytoplasmic; nuclear in
  ~75% of post-anaphase cells; K31-33A blocks nuclear entry, cytoplasm-restricted
  Mih1 is less effective, SV40 NLS rescues.
- Pal, Paraz and Kellogg 2008 J Cell Biol "Regulation of Mih1/Cdc25 by protein
  phosphatase 2A and casein kinase 1" — PMID:18316413. PP2A-Cdc55 dephosphorylates
  Mih1 at mitotic entry; CK1 (Yck1/2) phosphorylates it.
- Harvey et al. 2011 Mol Biol Cell "A phosphatase threshold sets the level of Cdk1
  activity in early mitosis in budding yeast" — PMID:21849476.
- Galli et al. 2021 Front Cell Dev Biol "Haspin Modulates the G2/M Transition Delay
  in Response to Polarization Failures in Budding Yeast" — PMID:33585466. Alk1 loss
  allows premature nuclear division in cdc24-1; MIH1 deletion restores the delay.

### Decisions
- All GO:0004725 rows (IBA, IEA, two ISS): ACCEPT. Core MF, directly demonstrated.
- GO:0000086 IBA + IMP and GO:0010971 IBA: ACCEPT (core process).
- GO:1902751 IEA (InterPro2GO): MODIFY -> GO:0010971, mirroring the SCHPO cdc25
  review; the generic parent adds nothing.
- Nucleus / cytoplasm (HDA x2, IBA x2): ACCEPT. Shuttling enzyme; both pools
  functional (Keaton 2008), nuclear pool more effective.
- GO:0051231 spindle elongation IMP (acts_upstream_of_or_within): KEEP_AS_NON_CORE;
  genuine phenotype, indirect via Cdc28/Bik1; GO:0000022 would be the more precise
  mitotic child if SGD refines.
- GO:0110032 meiotic G2/MI IBA: KEEP_AS_NON_CORE; now backed by direct
  S. cerevisiae evidence (PMID:41927924), same activity deployed in meiosis.
- No NEW terms. Considered "morphogenesis checkpoint" type terms (Mih1 is the
  dosage-sensitive output of the checkpoint), but Mih1 is the regulated effector
  rather than a signalling component and SGD has not annotated it; raised in
  suggested_questions/experiments instead.
- No bare protein-binding IPI rows exist in GOA for MIH1, so the protein-binding
  policy did not need to be applied.
