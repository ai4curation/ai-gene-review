# TSPOAP1 (RIM-BP1) notes

## Identity

- Active-zone RIM-binding protein 1 [PMID:33539324 "which encodes the active-zone RIM-binding protein 1 (RIMBP1)"].
- RIM-BP family defined by binding to RIMs [PMID:10748113 "RIM-BPs bind to RIM in yeast two-hybrid and GST pull-down assays"]
  and to calcium channel alpha1 subunits [PMID:11988172 "RBPs contain three Src homology 3 domains that bind to proline-rich motifs in alpha(1) subunits and Rab3-interacting molecules (RIMs)"].
- Core function set to structural constituent of presynaptic active zone (NEW, ISS) at the
  presynaptic active zone (NEW, ISS), matching the RIMBP2 and worm rimb-1 reviews.

## Human genetics

- Dystonia variants act in both directions on release
  [PMID:33539324 "In vitro analysis of the p.Gly1808Ser variant showed larger spike-evoked calcium transients and enhanced neurotransmission"].
  Regulation of neurotransmitter secretion (IMP) accepted.

## The TSPO / mitochondrion history

- Originally PRAX-1, a yeast two-hybrid partner of TSPO
  [PMID:9915832 "PRAX-1 is a cytoplasmic protein that also partially colocalizes with PBR in the mitochondria"].
- UniProt caution: a later rat study did not find it associated with TSPO in brain. I could
  not confirm this from the abstract of PMID:12435798 (an mRNA expression study), so I relied
  on the UniProt curated caution and did not cite that paper directly.
- Mitochondrion (IDA, IBA, IEA) and benzodiazepine receptor binding (IPI, IBA) marked
  over-annotated rather than removed: the in vitro results are not disputed, but a
  physiological mitochondrial/TSPO role is not supported. The IBAs are seeded by this protein's
  own annotations from the same study.

## Other calls

- Protein binding with CACNA1A (two IPI rows) modified to transmembrane transporter binding
  (GO:0044325). Protein binding with ADAM19 (SH3 array screen) removed as uninformative.
- Voltage-gated calcium channel activity (IEA from mouse) removed: RIM-BP1 has no
  transmembrane segment; the activity belongs to the channel it binds. The derived process row
  (regulation of presynaptic cytosolic calcium) kept as non-core on its own merits.
- Reactome cytosol rows kept as non-core; R-HSA-8951850 (TSPO:BZRAP1 cholesterol transport)
  rests on the disputed TSPO association.
- Paralog redundancy: RIM-BP2 dominates at hippocampal synapses (deep-research summary); a
  non-redundant RIM-BP1 site is an open question.
