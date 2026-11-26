# Prkcz (rat, UniProt P09217) - manual literature synthesis

No deep-research provider was available for this review; this synthesis was written by
the reviewer from the cached publications in `publications/` and the UniProt record
(`Prkcz-uniprot.txt`). Provenance is given inline.

## Identity and domain architecture

- Rat Prkcz encodes protein kinase C zeta (PKCzeta), an atypical PKC (aPKC) of the AGC
  Ser/Thr kinase family [UniProt P09217: "Belongs to the protein kinase superfamily. AGC
  Ser/Thr protein kinase family. PKC subfamily."].
- Domains: N-terminal PB1 domain (15-98), a single atypical C1 domain (130-180) that does
  not bind DAG, the kinase domain (252-518) and the AGC-kinase C-terminal tail (519-590)
  [UniProt FT lines; "The C1 domain does not bind the diacylglycerol (DAG)." PMID:9177193].
- Activity regulation: aPKCs "are not regulated by diacylglycerol, phosphatidylserine,
  phorbol esters or calcium ions"; full activation requires phosphorylation at Thr-410
  (activation loop) and Thr-560 (turn motif) [UniProt ACTIVITY REGULATION]. PDK1
  phosphorylates Thr-410: "PDK-1 phosphorylates and activates PKC zeta in vivo, and we have
  shown that this is due to phosphorylation of threonine 410 in the PKC zeta activation
  loop" [PMID:9768361]. PI 3-kinase products stimulate activity in rat adipocyte
  immunoprecipitates [PMID:9374484].

## Two isoforms from alternative promoters

- Isoform 1 = full-length PKCzeta (ubiquitous). Isoform 2 = PKMzeta, an N-terminally
  truncated, constitutively active catalytic fragment transcribed from an internal promoter
  in intron 4 and expressed specifically in brain [UniProt ALTERNATIVE PRODUCTS, CAUTION;
  PMID:12857744 per UniProt].
- PKMzeta "increased in the cytosol during the maintenance phase" of LTP in CA1 [PMID:8378304].
- "Protein kinase Mzeta is necessary and sufficient for LTP maintenance" [PMID:11914719,
  title; abstract only].
- PKMzeta maintains late-LTP "through persistent N-ethylmaleimide-sensitive factor
  (NSF)/glutamate receptor subunit 2 (GluR2)-dependent trafficking of AMPA receptors" to
  the synapse [PMID:18667614].
- Persistent phosphorylation by PKMzeta maintains late-phase LTP [PMID:15728837, full text].
- EM localisation: "electron microscopy highlights the kinase at postsynaptic densities and
  in clusters within spines" [PMID:24298142].
- Memory: "long-term associative memories vanished rapidly after local application of an
  inhibitor" of PKMzeta in rat cortex [PMID:17702943]. Caveat (reviewer knowledge, not in
  cache): the specificity of the ZIP inhibitor peptide and the persistence of memory in
  Prkcz knockout mice (compensation by PKCiota/lambda) are debated; UniProt cites RNAi
  knockdown in rat hippocampus impairing late LTP and long-term memory (PMID:27498875).

## Polarity (PAR complex)

- In migrating rat astrocytes, integrin engagement activates Cdc42, "which in turn recruits
  and activates a cytoplasmic mPar6/PKCzeta complex. Localized PKCzeta activity, acting
  through the microtubule motor protein dynein, is required for all aspects of induced
  polarity in these cells" [PMID:11525734].
- In migrating NRK cells, aPKCs (zeta and iota) are recruited to the leading edge with the
  exocyst via Kibra and control local JNK1 activation and paxillin phosphorylation; siRNA to
  PKCzeta inhibits wound-healing migration [PMID:19885391, full text].

## Insulin / metabolic signaling

- Insulin activates PKCzeta through PI3K in rat adipocytes; constitutive PKCzeta stimulates
  GLUT4 translocation, dominant-negative partially inhibits it [PMID:9374484].
- In L6 myotubes, PKCzeta "mediates insulin effect on glucose transport through actin
  remodeling"; insulin relocates PKCzeta from LDM to plasma membrane and into cortical actin
  structures, whereas at stress fibres "the staining pattern of PKCzeta was diffuse"
  [PMID:16525020, full text].
- PKCzeta regulates insulin-stimulated PKB activation and AMPK in muscle cells [PMID:20570724].
- PKCzeta interacts with 80K-H (PRKCSH) and munc18c in GLUT4 vesicle trafficking
  [PMID:15707389, full text].
- PKCzeta is activated by cAMP via PI3K in hepatocytes and is required for Ntcp translocation
  [PMID:15007074] and for microtubule-based motility of Ntcp vesicles [PMID:16734659].

## Mitogenic / inflammatory signaling

- Active PKCzeta activates MEK and MAPK; kinase-dead PKCzeta impairs MEK/MAPK activation by
  serum and TNF [PMID:8557035].
- In rat VSMCs, "ANG-induced ERK activation at early time points (<5 min) was significantly
  decreased in cells transfected with PKCzeta siRNA" while beta-arrestin-dependent ERK
  activation by SII was unaffected [PMID:19254952, full text]. Conclusion: "PKCzeta, at
  least partially, mediates ANG-induced early ERK activation".
- ANG II activates PKCzeta upstream of PLD2 in VSMC; inhibition reduces adhesion to
  collagen, spreading and hypertrophy [PMID:16113073]; antisense reduces neointima after
  balloon injury [PMID:16679391].
- PKCzeta overexpression increases IGF-1-dependent thymidine incorporation in RIN beta cells
  via MAPK [PMID:11779137].
- IL-1 and TNF induce PKCzeta kinase activity (in vitro kinase assay on immunoprecipitates)
  and PKCzeta drives MMP-9 transcription via NF-kB in C6 glioma cells [PMID:12130632].
- PKCzeta overexpression protects from UV-C apoptosis by inhibiting acid sphingomyelinase
  [PMID:17346242]; ceramide recruits PKCzeta into caveolin-rich microdomains and reduces its
  association with 14-3-3 [PMID:17308302].

## Scaffolds and ion channels

- ZIP (SQSTM1/p62) binds PKCzeta [PMID:9177193]; ZIP1/2 link PKCzeta to Kvbeta2 and
  stimulate its phosphorylation [PMID:10477520]; ZIP3 binds GABA-C rho3 [PMID:12431995].
- NGF-induced shift of Kv activation in PC12 cells requires PKCzeta activity and p62
  [PMID:15062979]; TNF/ceramide depolarise FRTL-5 cells via PKCzeta-dependent inhibition of
  a K+ current [PMID:15381257].
- PKCzeta catalytic domain phosphorylates A6-related protein (twinfilin-2) in vitro
  [PMID:10406962].

## Summary judgment

Core: DAG/Ca2+-independent Ser/Thr protein kinase activated by PI3K/PDK1, acting (i) in the
PAR6-PAR3-aPKC polarity complex downstream of Cdc42 at the cell cortex/leading edge, (ii)
downstream of PI3K in insulin and growth-factor signaling (GLUT4 translocation, ERK
activation), and (iii) as the brain-specific constitutively active PKMzeta isoform at
postsynaptic sites, where it sustains late-LTP via NSF/GluR2-dependent AMPA receptor
trafficking.
