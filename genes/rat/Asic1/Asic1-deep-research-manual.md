# Asic1 (rat, P55926) - manual literature synthesis

No deep-research API was available; this synthesis was compiled by hand from cached
publications in `publications/` and the UniProt record. Quotes are verbatim.

## Identity and family

- Rat Asic1 (Accn2, BNaC2) encodes acid-sensing ion channel 1, a member of the
  DEG/ENaC family: "Belongs to the amiloride-sensitive sodium channel (TC 1.A.6) family.
  ASIC1 subfamily." [file:rat/Asic1/Asic1-uniprot.txt]
- Topology: two transmembrane segments, a large extracellular domain and cytoplasmic
  N and C termini [PMID:19074149 "The structure shared by all Degenerins consists of two
  transmembrane segments, TM1 and TM2, a large extracellular domain, and short cytoplasmic
  amino and carboxyl termini."]
- Three rat splice isoforms: ASIC1a (displayed, P55926-1), ASIC1b/ASIC-beta (P55926-3)
  and ASIC-beta2 (P55926-2).

## Molecular function: proton-gated, Na+-selective cation channel

- Cloning paper (rat ASIC1a): [PMID:9062189 "Heterologous expression of ASIC induces an
  amiloride-sensitive cation (Na+ > Ca2+ > K+) channel which is transiently activated by
  rapid extracellular acidification."]
- ASIC1b: [PMID:9707631 "When expressed in COS-7 cells, ASIC-beta forms a functional
  channel with electrophysiological properties distinct from ASIC and DRASIC."] and
  [PMID:9707631 "unlike ASIC, the channel is not permeable to calcium"].
- [PMID:11448963 "Ca(2+) permeability of ASIC1a is low, whereas ASIC1b is impermeable to
  Ca(2+)."]
- Splice variants tune pH dependence: [PMID:12198124 "Compared with ASIC1a, steady-state
  inactivation and pH activation of ASIC1b are shifted to more acidic values by 0.25 and
  0.7 pH units, respectively, extending the dynamic range of ASIC1."]
- ASIC-beta2 is not a channel on its own: [PMID:11588592 "When expressed in Xenopus
  oocytes, ASIC-beta2 was inactive by itself."]
- Heteromers with ASIC2: [PMID:9360943 "coexpression of ASIC and MDEG subunits in Xenopus
  oocytes generates an amiloride-sensitive H+-gated Na+ channel with novel properties"].
- Gating mechanism (rat ASIC1a in oocytes): [PMID:19074149 "Substitution of any of them by
  Gly in rat ASIC1 makes channels unresponsive to pH as low as 4.0."]; non-functional
  mutants still reach the surface [PMID:19074149 "biotinylation of surface proteins
  revealed equal amounts of rASIC1 protein in the plasma membrane of cells expressing wild
  type or mutants Gly-72 or Gly-288"].
- Ca2+ permeability of ASIC1a matters for acidotic neuronal injury: [PMID:15369669
  "transfection of Ca2+ -permeable ASIC1a establishes sensitivity"].

## Location

- Plasma membrane of DRG neurons: [PMID:11842212 "ASIC1 localizes to the plasma membrane
  of small-, medium-, and large-diameter cells"].
- Surface expression of ASIC1a homomers requires the secreted protein PCYOX1L:
  [PMID:40712023 "Strikingly, in the absence of PCYOX1L, plasma membrane expression of
  ASIC1a was abolished, indicating that PCYOX1L is indispensable for proper assembly of
  homomeric ASIC1a."]
- Mouse: synaptosomes, dendrites, spines [PMID:11988176 "we found ASIC in hippocampus, in
  synaptosomes, and in dendrites localized at synapses"]; [PMID:17060608 "localized in
  dendritic spines where it functioned as a proton receptor"].
- Human ASIC1a: [PMID:32996060 "Surface hASIC1a was distributed throughout somata and
  dendrites, clustered in spine heads, and co-localized with postsynaptic markers."]

## Physiology (mostly mouse knockouts; downstream of the channel)

- Learning/memory: [PMID:11988176 "null mice displayed defective spatial learning and
  eyeblink conditioning"].
- Spine density: [PMID:17060608 "Decreasing ASIC1a reduced the number of spines, whereas
  overexpressing ASIC1a had the opposite effect."]
- Presynaptic release probability (indirect): [PMID:18094106 "neurons from ASIC1 knockout
  mice have an increased probability of neurotransmitter release"].
- Striatal neurons: [PMID:19376200 "a drop in pH induced calcium influx by activating
  homomeric ASIC1a channels"]; [PMID:19376200 "Activation of ASICs increased the membrane
  excitability of MSNs"].
- Fear/psychostimulant phenotypes are listed for Asic1a knockouts in [PMID:25828470 "ASIC4
  may modulate fear and anxiety by counteracting ASIC1a activity in the brain."]
- Sour taste: human evidence is correlative only [PMID:19812697 "These data suggest a role
  for ASICs and PKDs in human sour perception."].

## Human isoform caveat

- [PMID:21036899 "Human ACCN2 transcript variant 1 (hVariant 1) is not present in rodents
  and contains an additional 46 amino acids directly preceding the proposed channel
  gate."] and [PMID:21036899 "We report that hVariant 1 does not produce proton-gated
  currents under normal conditions when expressed in heterologous systems."]
  This is the basis of a human NOT annotation that RGD has propagated to rat by ISO.
