# Cdc42 (Drosophila melanogaster, UniProt P40793) - manual literature synthesis

No deep-research API provider was available for this review. This file was written
by hand from the cached publications in `publications/` (GOA-cited papers plus
PMID:21690310) and the UniProt record. Quotes are verbatim; papers marked
"abstract only" were not available as full text in the cache.

## Identity and family

- Cdc42 homolog, 191 aa, small GTPase superfamily, Rho family, CDC42 subfamily; the
  C-terminal tripeptide (189-191) is removed in the mature, lipid-anchored form
  [file:genes/DROME/Cdc42/Cdc42-uniprot.txt "Belongs to the small GTPase superfamily. Rho family. CDC42 subfamily."].
- Domain signatures: InterPro IPR037874 (Cdc42), IPR003578 (Small_GTPase_Rho),
  Pfam PF00071, PROSITE PS51420 (RHO), PANTHER PTHR24072 (RHO FAMILY GTPASE).
- Effector region (switch I) at residues 32-40 (UniProt FT MOTIF).

## Molecular activity

- Cdc42 is a GDP/GTP molecular switch. A Drosophila GAP, RotundRacGAP, stimulates
  GTP hydrolysis by Dcdc42 in vitro [PMID:11468292 "Here we demonstrate that Drosophila RotundRacGAP is active in vitro on Drac1 and Dcdc42 but not Drho1"]
  (abstract only).
- In vivo FRET biosensors show that endogenous Cdc42 is kept inactive through most of
  embryogenesis and is then activated in restricted subcellular compartments
  [PMID:19498173 "Cdc42 guanosine triphosphatase (GTPase) remains inactive within Drosophila embryos during the first two-thirds of embryogenesis"].

## Effectors (GTP-dependent binding partners)

- Mbt (PAK-family kinase): GTP-Cdc42 binds the Mbt GTPase-binding domain, regulates
  its kinase activity and recruits it to adherens junctions of photoreceptors
  [PMID:12490550 "the GTPase binding domain, which specifically interacts with GTP-loaded Cdc42, are important for Mbt function"; "Besides regulation of kinase activity, another important function of Cdc42 is to recruit Mbt to adherens junctions"] (abstract only).
- DPAK (Pak): binds activated DRacA and Cdc42 [PMID:8628256 "DPAK bound to activated (GTP-bound) Drosophila Rac (DRacA) and Drosophila Cdc42"] (abstract only).
- Genghis Khan (Gek, MRCK-like kinase): binds Dcdc42 in a GTP- and effector-domain-dependent
  manner [PMID:9371783 "which binds to Dcdc42 in a GTP-dependent and effector domain-dependent manner"] (abstract only).
- Frl (FMNL formin): pull-downs show GTP-Cdc42 binding to the Frl GBD-DID region; genetic
  data place Cdc42 upstream of Frl in ommatidial rotation and mushroom body axon growth
  [PMID:26801180 "Coimmunoprecipitation and pull-down assays showed that Frl strongly binds to GTP-bound forms of Cdc42 and, more weakly, to Rac, but genetic interaction assays suggest that, in vivo , Frl is activated by Cdc42."].
- Par-6/aPKC (Par complex): GTP-Cdc42 binds the Par-6 CRIB-PDZ module; Cdc42 and Par-3
  (Baz) bind the Par complex with negative cooperativity [PMID:36436559 "Par-3 and Cdc42 bind to the Par complex with strong negative cooperativity."];
  binding allosterically raises Par-6 PDZ ligand affinity [PMID:22078569 "Association of Cdc42-GTP with the CRIB-PDZ130-255 module results in a ~10-fold increase in affinity for a C-terminal PDZ ligand peptide"].
- dCIP4 (F-BAR) and Nwk (F-BAR/SH3) cooperate with Cdc42 to activate WASp-Arp2/3 actin
  assembly at the NMJ [PMID:18701694 "functions together with Cdc42 to promote WASp-mediated actin polymerization in vitro and to regulate synaptic growth in vivo"].

## Cell polarity

- Neuroblasts: Cdc42 co-localizes with Par-6/aPKC at the apical cortex downstream of Baz,
  is required for Par-6/aPKC localization, and relieves Par-6 inhibition of aPKC
  [PMID:17726059 "In addition to regulating Par-6/aPKC localization, Cdc42 increases aPKC activity by relieving Par-6 inhibition."].
- Oocyte: Cdc42 localizes to the anterolateral oocyte cortex and is required to maintain
  oocyte polarity and Par protein localization [PMID:23250210 "We establish that Cdc42 localization itself is polarized to the anterolateral cortex of the oocyte"] (abstract only).
- Follicle epithelium: the aPKC-Par6-Cdc42 complex specifies the apical membrane
  [PMID:22658591 "apical membranes are specified by Crumbs (Crb), Stardust (Sdt), and the aPKC-Par6-cdc42 complex"] (abstract only).
- Hemocytes: Cdc42 mutants fail to maintain polarity during migration to wounds
  [PMID:15699212 "Although the failure to maintain polarity leads to a haphazard migratory route in Cdc42 mutants"].

## Actin cytoskeleton and protrusions

- Wing hair outgrowth requires Cdc42 for localized actin polymerization
  [PMID:8947551 "We find that Cdc42 is required for localized actin polymerization in the extending hair."] (abstract only).
- Tracheal bridge-cell contacts: filopodia-like extensions require Cdc42
  [PMID:12034756 "the formation of cell extensions require Cdc42-mediated Drosophila fibroblast growth factor activity"] (abstract only).
- Border cells: Cdc42 governs actin flows at protrusions and migration efficiency (PMID:36224221).
- Epithelial wound closure: Cdc42 mutants have three-fold fewer leading-edge protrusions and
  fail at the final zippering phase (PMID:23038780; PMID:12402048).
- Single-cell wound repair in the syncytial embryo: Cdc42 forms a ring overlapping the actin
  ring (PMID:24388847; PMID:28923977).

## Neuronal morphogenesis and synapses

- Loss of Cdc42 alters VS-neuron dendrite length, caliber and spine density (PMID:12716918);
  aCC dendrite initiation requires cell-autonomous Cdc42 (PMID:19498173).
- Constitutively active Cdc42 causes axon pathfinding errors and midline crossing
  (PMID:11880508, PMID:12453459, PMID:17568577); these are gain-of-function results.
- Presynaptic and postsynaptic Cdc42 restrain NMJ growth (PMID:18701694, PMID:20554864) and
  Cdc42 dosage modifies neurotransmitter release in cv-c and Dystrophin/Dystrobrevin mutants
  (PMID:21228159, PMID:30904609).

## Heart function (PMID:21690310; cache is abstract only, full text read via PMC3216339)

- Compound Cdc42/tinman heterozygotes and adult heart-specific dominant-negative Cdc42
  cause impaired cardiac output, arrhythmia and myofibrillar disarray
  [PMID:21690310 "adult heart-specific interference with Cdc42 function is sufficient to cause these same defects"].
- The Cdc42-Tinman interaction acts partly through K+ channel genes dSUR and slowpoke, and
  (in mouse) Cdc42 is a miR-1 target downstream of Nkx2-5. These are necessity / genetic
  interaction data; they do not show which step of cardiac contraction Cdc42 performs.

## Other phenotypes (pleiotropic, mostly genetic)

Dorsal closure (dominant-negative Cdc42; PMID:8946916, PMID:11997505), ommatidial rotation
(PMID:26801180), tracheal terminal-cell branching and exocyst localization (PMID:21750259,
PMID:24607370), anti-parasitoid encapsulation and phagocytosis via the RhoGEF Zir
(PMID:22634526, PMID:21947570), spermatid release from somatic cyst cells via Wsp
(PMID:21652648), and nephrocyte uptake in an RNAi screen (PMID:23291470, Cdc42 not named
in the abstract).
