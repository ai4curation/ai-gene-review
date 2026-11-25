# Ryr2 (rat) — manual literature research (no deep-research provider available in this environment)

UniProt: B0LPN4 (RYR2_RAT, reviewed), 4955 aa, RGD:620314, GeneID 689560.

## Core picture

RyR2 is the cardiac ryanodine receptor: a homotetrameric, Ca2+-activated Ca2+ release
channel of the sarcoplasmic reticulum (SR) membrane. The pore is formed by the
C-terminal region of the four subunits; the bulk of each subunit is a cytoplasmic
scaffold that carries the regulatory sites.

UniProt B0LPN4 FUNCTION: "Cytosolic calcium-activated calcium channel that mediates the
release of Ca(2+) from the sarcoplasmic reticulum into the cytosol and thereby plays a
key role in triggering cardiac muscle contraction" ... "In cardiac myocytes, calcium
release is triggered by increased Ca(2+) cytosolic levels due to activation of the
L-type calcium channel CACNA1C" ... "The calcium channel activity is modulated by
formation of heterotetramers with RYR3" (ECO:0000269|PubMed:20431056,
ECO:0000269|PubMed:20471962).

DOMAIN: "The calcium release channel activity resides in the C-terminal region while the
remaining part of the protein resides in the cytoplasm."

SUBCELLULAR LOCATION: "Sarcoplasmic reticulum membrane ... Multi-pass membrane protein".

SUBUNIT: "Homotetramer. Can also form heterotetramers with RYR3. Identified in a complex
composed of RYR2, FKBP1B, PKA catalytic subunit, PRKAR2A, AKAP6, and the protein
phosphatases PP2A and PP1."

ACTIVITY REGULATION: activated by cytosolic Ca2+, NO, caffeine and ATP; modulated by
ryanodine (low = open, high = inhibited); regulated by calmodulin; "Channel activity is
inhibited by magnesium ions, possibly by competition for calcium binding sites"
(ECO:0000250|UniProtKB:P11716).

## Rat-specific experimental evidence (cached publications)

- **Localization in ventricular myocytes.** [PMID:11053140 "Every image showed a
  well-ordered array of fluorescent spots, indicating that all of the proteins examined
  were distributed in discrete clusters throughout the cell"; dyads "contained only
  ryanodine receptors, L-type Ca(2+) channels, and calsequestrin"] — junctional SR at the
  Z-line/dyad, i.e. junctional SR membrane.
- **Extradyadic RyR2 pools.** [PMID:17627991 "in addition to the junctional SR, a small
  number of RyR2s can be localized at the middle of the sarcomere and in the zone of
  perinuclear mitochondria"; "about 20% of Ca2+ sparks were not colocalized with the zone
  of the junctional or corbular SR (Z-line zone)"] — supports both Z disc and A band rows.
- **Caveolin-3-adjacent RyR pool.** [PMID:15980179 "caveolin-3 shows a marked
  colocalization with a population of ryanodine receptors that are separate from those
  within the dyad"].
- **Nuclear envelope pool / mAKAP complex.** [PMID:11590243 "the mAKAP signaling complex
  also includes nuclear envelope-resident ryanodine receptors and protein phosphatase 2A";
  "the ryanodine receptor is present at both the sarcoplasmic reticulum and nuclear
  envelope intracellular membrane compartments"] — this is the IDA for nuclear envelope,
  sarcoplasmic reticulum and AKAP6 (Q9WVC7) scaffold binding.
- **mAKAP complex and hypertrophy.** [PMID:16306226 "One function of the mAKAP complex is
  to facilitate cAMP-dependent protein kinase A-catalyzed phosphorylation of the ryanodine
  receptor Ca2+-release channel"] — the IDA for protein-containing complex.
- **Mg2+ regulation.** [PMID:16971497 "Addition of 0.3-1 mM Mg(2+) unexpectedly increased
  the binding two- to threefold and enhanced the affinity for [(3)H]ryanodine at 10-100
  microM Ca(2+)"] — direct response of RyR2 in SR vesicles to Mg2+.
- **Redox regulation.** [PMID:21807619 "the CG digitoxin (DGT) increased the incidence of
  arrhythmogenic spontaneous Ca(2+) waves, decreased the sarcoplasmic reticulum (SR) Ca(2+)
  load, and increased both ROS and RyR2 thiol oxidation"]; [PMID:18799678 "Ischemia reduced
  [3H]ryanodine binding and total RyR protein content by 35%, and increased at least
  twofold endogenous RyR2 S-nitrosylation and S-glutathionylation"; "we propose that
  ischemia, by enhancing RyR2 S-glutathionylation, allows RyR2 to sustain CICR"] — brain
  cortex RyR2/RyR3 channels in bilayers; direct CICR demonstration.
- **Diabetic myocytes.** [PMID:17027851 "residual functional RyR2 from diabetic rat hearts
  exhibited increased sensitivity to Ca(2+) activation (EC(50activation) decreased from 80
  microM to 40 microM"] — response to calcium ion (direct Ca2+ activation of the channel).
- **Smooth muscle / non-cardiac RyR2.** [PMID:15870112 "an antisense strategy revealed that
  the ryanodine receptor subtype 2 alone was required to initiate the Ca2+ oscillations
  induced by acetylcholine and also by cyclic adenosine diphosphoribose"] — rat duodenum
  myocytes, IMP for regulation of cytosolic calcium ion concentration.
- **Pulmonary artery SR store segregation.** [PMID:20177054 "In cells labeled for RyR2
  (Fig. 3B), the distribution of labeling by density was different. Labeling by density was
  lowest in the perinuclear region"; RyR2 labelling "lay in between these two regions of
  the cell"] — RyR2 occupies an intermediate (extraperinuclear) SR compartment, NOT the
  subplasmalemmal compartment, which is RyR1's. This is the reference GOA used for
  GO:0031234 extrinsic component of cytoplasmic side of plasma membrane — the paper does
  not support a plasma-membrane location for RyR2, and RyR2 is a multi-pass SR membrane
  protein, not an extrinsic peripheral membrane protein.
- **Plasma-membrane RyR2 in beta cells.** [PMID:19116207 "we showed that RyR2 mediates
  both the Ca(2+) entry and the plasma membrane currents evoked by agonists of RyR"; "small
  numbers of RyR2 are selectively expressed in the plasma membrane of RINm5F pancreatic
  beta-cells"; "the effect of 4CmC on Mn2+ entry was almost abolished in cells treated with
  RNAi to RyR2"] — rat insulinoma; RNAi-based IMP for ion/Ca2+/Mn2+ transmembrane transport.
  Note the channel here is integral to the PM, not extrinsic.
- **TRPV4-RyR2 coupling under chronic hypoxia.** [PMID:22962011 "Western blotting
  experiments revealed the expression of TRPV4 and RyR2 with an increase in both receptors
  in pulmonary arteries from CH rats vs. Nx rats"] — expression change under hypoxia (IEP).
- **Nutritional / drug expression responses.** [PMID:17224993 "RYR2 mRNA was significantly
  decreased in the left ventricle of the food-restricted group"]; [PMID:15916736 "the levels
  of mRNA expression of SERCA and RyR2 were elevated compared with the control"].
- **NR2B interaction at Z-bands.** [PMID:15010472 "the NR2B antigen was localized at the
  sarcomeric Z-bands"; "ryanodine receptor 2 was identified as a molecular interaction
  partner of the cardiac NR2B polypeptide"].
- **FKBP12.6 binding at Z-lines.** [PMID:20431056 "Both FKBP12.6 and FKBP12 concentrate at
  Z-lines, consistent with RyR2 and Ca spark initiation sites"; "only FKBP12.6 inhibits
  resting RyR2 activity"].
- **Islet-type RyR2 splice variant.** [PMID:20471962 "we isolated a novel RyR cDNA (the
  islet-type RyR), which is generated from the RyR2 gene by alternative splicing of exons 4
  and 75"; "Intracellular Ca(2+) release in the islet-type RyR2-transfected cells was
  enhanced in the presence of cADPR"] — basis of isoform B0LPN4-2.
- **Critical illness myopathy (skeletal muscle).** [PMID:21474431 "the majority of the
  increase was due to increased expression of the skeletal muscle-specific RYR1 isoform,
  which was the most predominant RYR expressed in both control and CIM skeletal muscle"] —
  this paper is about skeletal muscle RYR1/CaV1.1; RyR2 was measured by Western blot and
  immunostaining but the paper does not establish a sarcolemmal location for RyR2. The
  GO:0042383 sarcolemma IDA from this reference is weakly supported.

## Curation judgements

- Core MF: ryanodine-sensitive calcium-release channel activity (GO:0005219), which is
  a subclass of calcium-induced calcium release activity (GO:0048763) — verified with OAK.
  The homotetramer forms the pore; each subunit contributes but the functional channel is
  the tetramer, so the activity is written both as `molecular_function` (the
  subunit is the channel-forming protein and the homotetramer is of identical subunits)
  and is reflected in `in_complex` GO:1990425.
- Core CC: sarcoplasmic reticulum membrane (GO:0033017), specifically junctional SR
  (GO:0014701 is_a GO:0033017, checked with OAK) at dyads in cardiomyocytes.
- Core BP: release of sequestered calcium ion into cytosol by sarcoplasmic reticulum
  (GO:0014808) and cardiac muscle contraction / regulation thereof.
- GO:0031234 (extrinsic component of cytoplasmic side of plasma membrane) is wrong on
  topology grounds for a multi-pass channel and is not supported by PMID:20177054 →
  source defect, REMOVE for the ARBA IEA, and the IDA row flagged as a wrong-term defect
  while using UNDECIDED (full text read: the paper places RyR2 away from the subplasmalemmal
  region).
- Expression-change IEP rows (hypoxia, nutrient, xenobiotic) are kept as non-core; they
  record responsiveness, not a function RyR2 performs in those processes.
