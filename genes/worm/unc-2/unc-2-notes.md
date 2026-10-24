# unc-2 (C. elegans CaV2 alpha1 subunit, UniProt G5EFB0) - curation notes

## Identity
- The scaffold for this review was fetched as TrEMBL entry G5EFB0_CAEEL (1523 aa, ORF T02C5.5),
  annotated as "Voltage-dependent calcium channel type A subunit alpha-1" and belonging to the
  calcium channel alpha-1 subunit (TC 1.A.1.11) family, multi-pass membrane protein
  [file:worm/unc-2/unc-2-uniprot.txt]. This is an alternative UniProt entry for the same gene as
  A0A1N7SYT0, the accession used for unc-2 in modules/synaptic_vesicle_exocytosis.yaml; the review is
  filed under the accession in the scaffold.
- unc-2 encodes the worm CaV2 (N/P/Q-type-related) channel alpha1 subunit
  [PMID:7723846 "unc-2 encodes a homologue of a voltage-sensitive"].

## Core biology: presynaptic calcium channel supplying Ca2+ for release
- UNC-2 is the presynaptic CaV2 channel of C. elegans, required for evoked release at the
  neuromuscular junction [PMID:18721860 "The calcium channel alpha subunit, UNC-2 is required for evoked responses at the C. elegans NMJ"],
  and unc-2 mutants are uncoordinated with evoked-release defects
  [PMID:19718034 "unc-2 mutants are uncoordinated, with defects in evoked neurotransmitter release at the neuromuscular junction"].
- Localization: GFP-tagged UNC-2 is at presynaptic active zones of sensory and motor neurons
  [PMID:19718034 "is localized to presynaptic active zones of sensory and motor neurons"], and
  immunoEM places UNC-2 gold particles on the membrane within 90 nm of the presynaptic density,
  overlapping UNC-10/RIM [PMID:18721860 "overlapping the subcellular distribution of UNC-10(Rim)"].
- Channel assembly and trafficking: synaptic delivery requires the alpha2delta subunit UNC-36 and
  the ER protein CALF-1; in calf-1 mutants UNC-2 is retained in the ER while other active-zone
  components still arrive
  [PMID:19718034 "Synaptic localization of CaV2 requires the alpha(2)delta subunit UNC-36 and CALF-1"].
  This establishes UNC-2 as a subunit of a voltage-gated calcium channel complex.
- Functional coupling to the release machinery: release in unc-10 and rab-3 mutants is more
  calcium-sensitive, and UNC-2 colocalizes with UNC-10 at presynaptic densities, i.e. the active-zone
  scaffold positions vesicles near UNC-2 [PMID:18721860 "Together these results suggest that Rim may target a subset of SVs via RAB-3 interactions to regions in which calcium influx is enhanced"].

## Additional (non-core) roles
- Neuromodulator adaptation and egg laying: unc-2 is required for adaptation to dopamine and
  serotonin, and is expressed in neurons controlling egg laying
  [PMID:7723846 "the Caenorhabditis elegans gene unc-2 is required for adaptation to two neurotransmitters, dopamine and serotonin"].
- AWC left/right asymmetry: unc-2 (CaV2) acts with egl-19 (CaV1) to stimulate CaMKII and the MAP
  kinase pathway, opposed by olrn-1, in the stochastic AWC asymmetry decision
  [PMID:17986337 "olrn-1 opposes the action of two voltage-activated calcium channel homologs, unc-2 (CaV2) and egl-19 (CaV1), which act together to stimulate the calcium/calmodulin-dependent kinase CaMKII and the MAP kinase pathway"].
- Movement rate and serotonergic signalling: UNC-2 antagonizes a TGF-beta pathway that influences
  movement rate and is needed for normal serotonin levels and stress-induced tph regulation in ADF
  [PMID:14675154 "established an epistasis pathway showing that UNC-2 function antagonizes a"].
  The cached record is abstract-only and does not specify heat or starvation as the stressor, so the
  response-to-heat and response-to-starvation rows citing it are left UNDECIDED.

## GO decisions (summary)
- Core: voltage-gated calcium channel activity (GO:0005245) in the voltage-gated calcium channel
  complex (GO:0005891) at the presynaptic active zone membrane (GO:0048787), mediating calcium ion
  transmembrane transport (GO:0070588) for synaptic vesicle exocytosis.
- Automatic UniProt-rule terms transferred from vertebrate CaV paralogs that act in epithelia or in
  sensory transduction (epithelial fluid transport, basolateral plasma membrane, neuron remodeling,
  the detection-of-stimulus terms) are flagged as over-annotations for a presynaptic worm CaV2.
