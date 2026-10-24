# unc-10 (C. elegans RIM, UniProt Q22366) - curation notes

## Identity
- Swiss-Prot RIM_CAEEL, Q22366, 1563 aa, ORF T10A3.1; two splice isoforms (Q22366-1/-2). Sole worm
  RIM (vertebrates: RIMS1-4). Domain architecture: N-terminal Rab-binding/zinc-finger region
  (IPR010911), PDZ domain, two C2 domains [file:worm/unc-10/unc-10-uniprot.txt].

## Core biology: active-zone Rab3 effector that promotes vesicle priming
- unc-10 null mutants are viable but have behavioural and physiological defects more severe than
  rab-3 mutants; RIM is localized to synaptic sites, yet presynaptic density ultrastructure and
  docked-vesicle numbers are normal, while the pool of fusion-competent (primed) vesicles is
  reduced fivefold, and the defect is suppressed by constitutively open syntaxin
  [PMID:11559854 "Rim is localized to synaptic sites in C. elegans, but the ultrastructure of the presynaptic densities is normal in Rim"; "The level of fusion competent vesicles at release sites was reduced fivefold in Rim"].
  Hence RIM acts after docking, regulating priming via syntaxin conformation, and is explicitly not
  required for synapse development or structural organization
  [file:worm/unc-10/unc-10-uniprot.txt "Not required for the development or the structural organization of synapses"].
- Rab3 effector function: GTP-bound but not GDP-bound RAB-3 binds the UNC-10 zinc-finger region,
  selectively among worm Rabs [PMID:18721860 "C. elegans and vertebrate Rim both interacted with the activated C. elegans GTP-bound RAB-3(Q81L) mutant, but not the GDP-bound RAB-3(T36N) mutant"].
- Vesicle targeting to the presynaptic density: with high-pressure-freeze EM, unc-10 mutants lose
  vesicles contacting the membrane within 30 nm of the presynaptic density, and rab-3 phenocopies
  this without additivity in the double mutant
  [PMID:18721860 "docked SVs within 30nm of the PD were also significantly reduced"].
- Release physiology: evoked amplitude and mini frequency are strongly reduced in unc-10 (minis to
  ~20% of wild type), more severely than rab-3, and the defect worsens at low external Ca2+, with
  UNC-10 colocalizing with the UNC-2 Ca2+ channel at presynaptic densities
  [PMID:18721860 "overlapping the subcellular distribution of UNC-10(Rim)"].
- Active-zone localization and partners: RIM is an active-zone protein whose PDZ domain directly
  binds the C-terminal IWA motif of ELKS-1
  [PMID:15976086 "the ELKS protein bound to GST-PDZ"], but the two localize independently of one
  another [PMID:15976086 "ELKS immunostaining is unaltered in each of these mutant animals"], and
  the RIM PDZ domain is dispensable for RIM function
  [PMID:15976086 "indicating that the ELKS-interacting PDZ domain of RIM is not required for normal RIM function"].
- Cholinergic transmission: unc-10(md1117) animals are completely aldicarb resistant, the hallmark
  of strongly reduced acetylcholine release
  [PMID:15976086 "animals that lack RIM ( md1117 ) are completely aldicarb resistant"], consistent
  with unc-10 having been recovered among genes conferring resistance to acetylcholinesterase
  inhibitors [PMID:7498734 "recessive resistance to inhibitors of acetylcholinesterase"].

## Non-core roles
- Defecation interval is lengthened in unc-10(e102), and dauer formation in response to daumone is
  altered, with the F-box protein CFL-1 proposed to ubiquitinate UNC-10
  [PMID:30460068 "The e102 strain of unc-10 mutants showed increase in average time interval between defecations compared with that of the wild type N2"].
- Locomotion: unc-10 was defined as an uncoordinated mutant in the original genetic screen
  [PMID:4366476 "Mutations in 77 of these alter"].

## GO decisions (summary)
- Core: small GTPase binding (GO:0031267, Rab3-GTP effector) at the presynaptic active zone
  (GO:0048786), driving synaptic vesicle priming (GO:0016082) and positive regulation of synaptic
  vesicle exocytosis (GO:2000300).
- GO:0048790 maintenance of presynaptic active zone structure (IEA) is contradicted by the worm
  data (normal presynaptic density ultrastructure in unc-10 mutants) and is removed.
- GO:0098882 structural constituent of presynaptic active zone (IBA) is kept as non-core for the
  same reason: UNC-10 is an active-zone resident but dispensable for active-zone structure.
- GO:0008104 intracellular protein localization (IMP, PMID:15976086) is flagged as
  over-annotation: in that paper ELKS localization is normal in unc-10 mutants, and RIM's role in
  ELKS localization is auxiliary/redundant.
- GO:0006886 intracellular protein transport (InterPro Rab-binding-domain mapping) over-annotates:
  UNC-10 regulates vesicle priming, it does not transport protein cargo.
- Behavioural terms (locomotion, mating, pumping, defecation, dauer, growth) are retained as
  non-core or flagged, being downstream of the release defect.
