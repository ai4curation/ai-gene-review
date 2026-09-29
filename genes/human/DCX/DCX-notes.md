# DCX review notes

Journal for the DCX (O43602, doublecortin) GO annotation review.

## Sources used
- UniProt O43602 (`DCX-uniprot.txt`).
- Cached GOA-cited publications, plus papers cached for this review after PubMed eutils verification:
  PMID:10399933, PMID:10399932, PMID:15200960, PMID:22727374, PMID:14625554, PMID:27238282.
  PMID:15173193 (Tanaka 2004) was already cached (module evidence).
- Deep research (`DCX-deep-research-falcon.md`) was not present when the review was first drafted; see the end of
  this file for the final check.

## Biology summary (with provenance)
- Neuronal microtubule-associated protein with two tandem doublecortin (DC) domains (UniProt DOMAIN 53..139,
  180..263). Mutations cause X-linked lissencephaly (males) and subcortical band heterotopia (females)
  [PMID:9489699].
- MAP that stabilizes microtubules and promotes polymerization
  [PMID:10399933 "DCX coassembles with brain microtubules, and recombinant DCX stimulates the polymerization of purified tubulin"],
  [PMID:10399933 "overexpression of DCX in heterologous cells leads to a dramatic microtubule phenotype that is resistant to depolymerization"].
- Binds between protofilaments, selective for 13-pf MTs [PMID:15200960 "doublecortin binds between the protofilaments"];
  cooperative binding and 13-pf nucleation in vitro [PMID:22727374]; recognizes the compacted GDP lattice and is not a +TIP
  in cells [PMID:27238282].
- Microtubule affinity is negatively regulated by PKA and MARK/PAR-1 phosphorylation [PMID:14741102].
- Required for radial migration in rat neocortex (in utero RNAi) [PMID:14625554]; mouse Dcx knockout has mild cortical
  phenotype (redundancy with DCLK1) [PMID:14625554 "genetic deletion of Dcx in mice does not cause neocortical malformation"].
- Nucleokinesis: in mouse cerebellar granule neurons DCX outlines the perinuclear microtubule cage converging on the
  centrosome, co-immunoprecipitates with dynein, and its overexpression rescues N-C coupling defects from Lis1 deficiency
  and dynein inhibition [PMID:15173193].
- Interacts with LIS1 [PMID:11001923] and USP9X (as interactor, not substrate) [PMID:24607389].

## Decisions
- Protein binding rows: REMOVE (uninformative; mostly proteome-scale screens), except USP9X row MODIFY to
  GO:1990381 ubiquitin-specific protease binding (paper explicitly states DCX is an interacting protein, not a substrate).
- InterPro2GO rows from IPR017302/IPR003533 for axoneme assembly, intracellular signal transduction and retina development:
  REMOVE -- the DC domain is a microtubule-binding module; ciliary/retinal functions belong to RP1/RP1L1 family members,
  and there is no evidence DCX acts in signal transduction.
- microtubule associated complex (TAS): MODIFY to GO:0005874 microtubule (DCX is a lattice-binding MAP, not a subunit of a
  defined complex).
- NEW: GO:0007026 negative regulation of microtubule depolymerization (PMID:10399933, PMID:15200960).
- Nucleokinesis module: supports DCX annoton function GO:0008017 microtubule binding. Did not add a NEW nuclear-migration
  process annotation: evidence is mouse-only and DCX acts on the track (MT stabilization), which is captured by the
  MT-stabilization process term; flagged as suggested question.

## Deep research check (final)
- `DCX-deep-research-falcon.md` appeared after the first draft and was read. It agrees with the MT-nucleating,
  lattice-stabilizing MAP model (Gleeson 1999, Moores 2004, Manka & Moores 2020), PKA/MARK/CDK5 regulation, and
  X-linked lissencephaly/SBH genetics. Cited in support of NEW GO:0007026.
- Not annotated (emerging/indirect): 2023 iPSC preprint on tubulin polyglutamylation and lysosome processivity;
  kinesin-3 (KIF1A/KIF1C) cargo effects; PKA-Ser47 -> Asef2/Rac1 actin coupling. CDK5 Ser297 control of
  perinuclear microtubule association raised as a suggested question (relevant to nucleokinesis).
