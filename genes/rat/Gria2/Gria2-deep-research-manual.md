# Gria2 (rat GluA2, UniProt P19491) - manual literature synthesis

No deep-research API was available for this review; this file is a manual synthesis
built from the cached publications in `publications/` and the UniProt record
(`Gria2-uniprot.txt`). Every claim carries its source.

## Identity and architecture

- GluA2 (GluR2, GluR-B) is the AMPA-type ionotropic glutamate receptor subunit 2;
  UniProt: "Ionotropic glutamate receptor that functions as a ligand-gated cation channel,
  gated by L-glutamate and glutamatergic agonists such as alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic
  acid (AMPA), quisqualic acid, and kainic acid" [file:rat/Gria2/Gria2-uniprot.txt CC FUNCTION].
- Member of the glutamate-gated ion channel family (TC 1.A.10.1); PANTHER PTHR18966;
  domains: amino-terminal domain (ANF receptor, PF01094), ligand-binding S1/S2 (PF10613),
  pore/transmembrane region (PF00060) [file:rat/Gria2/Gria2-uniprot.txt DR lines].
- Topology: extracellular N-terminus (22-543), M1, re-entrant pore loop M2 (592-607),
  M3, extracellular S2 loop, M4, cytoplasmic C-tail (834-883) [UniProt FT].
- Crystal structure of homotetrameric rat GluA2 [PMID:19946266 "Here we report the crystal
  structure of the alpha-amino-3-hydroxy-5-methyl-4-isoxazole propionic acid (AMPA)-sensitive,
  homotetrameric, rat GluA2 receptor at 3.6 A resolution in complex with a competitive antagonist."].
  The receptor is a dimer of dimers with symmetry mismatch between extracellular and pore layers.
- In heteromeric GluA1/2-TARP gamma8 receptors "the core subunits arrange to give the GluA2
  subunit dominant control of gating" [PMID:30872532].
- ATD (NTD) drives subfamily-specific and heteromeric assembly: "AMPA receptor GluR1- and
  GluR2-ATDs form tightly associated dimers" [PMID:19461580]; "Heteromerization is dominant,
  occurs at the level of the dimer, and results in a preferential incorporation of the
  functionally critical GluA2 subunit" [PMID:21317873].

## Channel function and the Q/R site

- Q/R site in M2 controls Ca2+ permeability [PMID:1653450 "Mutation of a certain amino acid that
  results in a net charge change (from glutamine to arginine or vice versa) alters both the
  current-voltage relation and the calcium permeability of non-NMDA receptors."].
- RNA editing (Q607R): "Heteromerically expressed edited GLUR2 (R) receptor complexes are
  impermeable to calcium, whereas the unedited (Q) forms are highly permeable to divalent cations"
  [UniProt RNA EDITING, PMID:1653450]. So native (edited) GluA2 renders AMPARs Ca2+-impermeable;
  Ca2+-permeable AMPA channel activity is a property of GluA2-lacking receptors or of the
  unedited/mutant GluA2 constructs used experimentally (GluR-B(Q), GluR-B(N)) [PMID:11773314].
- Flip/flop splicing tunes desensitization; edited homomeric GluA2(R) gives almost no current,
  so kinetics were measured on unedited GluR2Q [PMID:10704491 "we expressed the unedited form of
  GluR2 (GluR2Q) in oocytes, which produced large current responses sufficient for analysis of the
  kinetic properties."].
- Kainate is a weak partial agonist of GluA2 (structural impediment to lobe closure)
  [PMID:21846932 full text]; GluA2 is not a kainate-selective receptor.
- Auxiliary subunits: TARPs (gamma-2, gamma-5, gamma-7, gamma-8) [PMID:18817736, PMID:19234459,
  PMID:21172611, PMID:30872532] and cornichons CNIH2/3 [PMID:19265014 "the majority of AMPARs in
  the rat brain are coassembled with two members of the cornichon family of transmembrane
  proteins, rather than with the TARPs"].

## Trafficking via the C-terminal tail

- PDZ ligand (-SVKI) binds class II PDZ proteins GRIP1/ABP/GRIP2 and PICK1
  [PMID:9069286, PMID:9768844 "ABP binds to the GluR2/3 C-terminal VKI-COOH motif via class II
  hydrophobic PDZ interactions", PMID:10027300, PMID:10340301].
- Ser880 phosphorylation by PKC decreases GRIP1 binding but not PICK1 binding and promotes
  internalization [PMID:11007883]; occurs during cerebellar LTD [PMID:10856222].
- Tyr876 phosphorylation strengthens GRIP1 binding and gates homeostatic upscaling
  [PMID:32071234 "AMPAR trafficking during homeostatic upscaling can be gated by a single
  phosphorylation site on the GluA2 subunit."]; GRIP1-GluA2 interaction needed for LTP-related
  insertion [PMID:32948689] and scaling up [PMID:26109571].
- NSF binds residues Lys844-Gln853 (Asn851 critical); NSF-binding peptide reduces AMPAR EPSCs
  [PMID:9697854]; GluR2-NSF-SNAP complex is ATP-hydrolysis reversible [PMID:9697855];
  NSF/SNAPs disassemble GluR2-PICK1 [PMID:11931741]; Plk2 displaces NSF and promotes GluA2 loss
  [PMID:20802490].
- AP-2 mu2 binds a basic motif in the tail and drives clathrin-dependent endocytosis
  [PMID:17289840]; Syt3 binds GluA2 and drives activity-dependent endocytosis [PMID:30545844].
- GluA2-3Y peptide (blocks regulated endocytosis) blocks LTD in NAc and VTA and LTD-dependent
  behaviours [PMID:16311338, PMID:21187978, PMID:37190555].
- PICK1 restricts GluA2 from synapses after OGD, producing Ca2+-permeable GluA2-lacking AMPARs
  and delayed cell death [PMID:19321442, full text: surface biotinylation shows "a time-dependent
  reduction in GluR2 surface expression by OGD"]; glycine chemLTP produces a transient
  PICK1-dependent switch [PMID:22915106].

## Localization

- Postsynaptic density of asymmetric synapses, dendrites and dendritic spines; essentially absent
  presynaptically in hippocampus [PMID:10701825]; spines of thalamo-amygdaloid synapses with a
  large cytoplasmic pool [PMID:17207780].
- Presynaptic pools in some circuits: axonal growth cones and synaptic vesicle membranes
  [PMID:12554656], corticostriatal/thalamostriatal terminals [PMID:15610164], GABAergic terminals
  in dorsal horn [PMID:15844209], presynaptic active zone and small vesicles of Schaffer
  collaterals [PMID:28057533], presynaptic synaptosome fraction [PMID:16903873].

## Disease/pathology context (non-core)

- Abeta oligomers (ADDLs) bind preferentially to GluA2-containing complexes [PMID:20032460].
- GluA2 down-regulation by tributyltin increases glutamate vulnerability [PMID:19591855].
