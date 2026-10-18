# unc-57 (endophilin A) curation notes

UniProt B1V8A0 (SH3GH_CAEEL, Swiss-Prot), WormBase T04D1.3. The single
C. elegans endophilin-A (N-BAR + SH3). Module role: BAR-domain membrane
curvature in synaptic vesicle endocytosis (modules/synaptic_vesicle_endocytosis.yaml).

## Identity and phenotype

- unc-57 encodes endophilin A and is required for synaptic vesicle recycling
  [PMID:14622579 "In this study, we demonstrate that the unc-57 gene encodes the Caenorhabditis elegans ortholog of endophilin A."]
  [PMID:14622579 "We demonstrate that endophilin is required in C. elegans for synaptic vesicle recycling."].
- Endophilin and synaptojanin (unc-26) act in the same pathway; endophilin
  stabilizes synaptojanin at synapses
  [PMID:14622579 "The electrophysiological phenotype of endophilin and synaptojanin double mutants are virtually identical to the single mutants, demonstrating that endophilin and synaptojanin function in the same pathway."]
  [PMID:14622579 "These data suggest that endophilin is an adaptor protein required to localize and stabilize synaptojanin at membranes during synaptic vesicle recycling."].
- unc-57 mutants mislocalize synaptobrevin, the classic synaptic vesicle
  endocytosis defect
  [PMID:18094048 "By contrast, SNB-1::GFP was mislocalized in the dorsal nerve cord of both unc-57-endophilin and fat-3 mutants"].

## Mechanism: membrane bending, not scaffolding (Bai et al. 2010, full text)

- [PMID:21029864 "First, Endophilin promotes SV endocytosis by acting as a membrane-bending molecule, not as a molecular scaffold."]
- [PMID:21029864 "Second, Endophilin functions on the plasma membrane, promoting an early step in endocytosis (prior to scission of endocytic vesicles)."]
- BAR-domain tubulation and dimerization mutants lose rescuing activity
  [PMID:21029864 "Both the dimerization mutant (ΔH1I) and the tubulation defective mutant (M70S/I71S) had significantly less rescuing activity for the unc-57 locomotion, SpH, and EPSC rate defects compared to the wild type rEndoA1 BAR domain (Fig."].
- SH3 domain: dispensable for endocytosis, required to localize UNC-26
  [PMID:21029864 "Expressing mutant UNC-57 proteins lacking the SH3 domain rescued the unc-57 endocytic defects but failed to rescue the UNC-26 Synaptojanin localization defects."]
  [PMID:21029864 "Endophilin’s SH3 domain robustly binds to proline-rich-domains (PRDs) in dynamin and synaptojanin."].
- Localization: mostly on the SV pool, released by exocytosis
  [PMID:21029864 "Despite acting at the plasma membrane, the majority of endophilin is targeted to the SV pool."]
  [PMID:21029864 "Photoactivation studies suggest that the soluble pool of endophilin at synapses is provided by unbinding from the adjacent SV pool and that the unbinding rate is regulated by exocytosis."].
- UniProt: "Localizes to neuromuscular junctions" (co-localizes with
  snb-1/synaptobrevin and rab-3 but not dyn-1 and apt-4).

## Non-core: necrotic neurodegeneration

- Endocytosis is required to execute degenerin-induced necrosis; endophilin
  depletion suppresses it
  [PMID:22157748 "Depletion of the key endocytic machinery components dynamin, synaptotagmin and endophilin suppresses necrotic neurodegeneration induced by diverse genetic and environmental insults in C. elegans."].
- GOA maps this to GO:0070266 necroptotic process, whose definition requires
  RIPK1/3 and MLKL signalling that C. elegans lacks; proposed replacement is
  GO:0097300 programmed necrotic cell death (MODIFY), and it is a non-core,
  endocytosis-mediated contribution.

## Review decisions

- 19 GOA rows: 16 ACCEPT (all IBA/IEA/EXP/IDA localization and endocytosis
  rows), 1 MARK_AS_OVER_ANNOTATED (glutamatergic synapse IBA: mammalian
  synapse-type context, worm data are from cholinergic/GABAergic NMJs),
  2 MODIFY (necroptotic process -> programmed necrotic cell death).
- 1 NEW: GO:0048488 synaptic vesicle endocytosis (IMP, PMID:21029864 +
  PMID:14622579). Participation: endophilin performs the membrane-bending
  step. Comparator: human SH3GL2, mouse Sh3gl2 and fly endoA carry the term.
- Core functions: (1) phospholipid binding / N-BAR membrane bending in
  synaptic vesicle endocytosis; (2) SH3 adaptor activity localizing
  synaptojanin. GO:0005543 is not in GOA for unc-57 (the amphiphysin
  ortholog carries it by IBA); left as a core-function term only because the
  liposome binding/tubulation assays were done with the rat BAR domain.
- Deep research (falcon): see report status in the handback.

## Addendum: endosomal vesicle regeneration (Yu et al. 2018, from deep research)

- [PMID:29962934 "Endophilin A and synaptojanin were not absolutely required for the ultrafast/bulk endocytosis step at the PM, because in unc-26 (encoding synaptojanin) and unc-57 mutants, LVs/endosomes were still formed after optogenetic stimulation."]
- [PMID:29962934 "At the same time, the breakdown of these LVs into new SVs was strongly attenuated in both unc-26 and unc-57 mutants, arguing that the two proteins act at the step of SV formation from the endosome."]
- [PMID:29962934 "In erp-1; chc-1 double mutants, only comparably mild phenotypes were apparent (Figures 9E,F), emphasizing that UNC-57 is the “main” player in both endocytosis and endosomal SV recycling."]
- Deep research (falcon) succeeded and pointed to this paper; the ERP-1
  (endophilin B) paralog has only a minor role.
