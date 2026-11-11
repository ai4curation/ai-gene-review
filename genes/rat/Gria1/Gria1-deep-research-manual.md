# Gria1 (rat, UniProt P19490) - manual literature synthesis

No deep-research provider was available for this session. This synthesis was
written by the reviewer from the cached publications in `publications/` and the
UniProt record, with provenance inline. It is not an automated deep-research report.

## Identity

Gria1 encodes GluA1 (GluR1, GluR-A, GluR-K1), a 907-residue pore-forming subunit of
AMPA-type ionotropic glutamate receptors (RGD:621531, GeneID 50592). Flip and flop
splice isoforms differ in a short extracellular segment that tunes desensitization
[PMID:1699275 "These modules, designated \"flip\" and \"flop,\" are encoded by adjacent exons of the receptor genes and impart different pharmacological and kinetic properties on currents evoked by L-glutamate or AMPA, but not those evoked by kainate."].

## Channel activity

- Cloned from rat brain by functional expression as a kainate-gated channel
  [PMID:2480522 "The cDNA encodes a single protein of relative molecular mass (Mr) 99,800 which on expression in oocytes forms a functional ion channel"],
  then recognised as AMPA-selective
  [PMID:2166337 "Functional expression of the cDNAs in cultured mammalian cells generated receptors displaying alpha-amino-3-hydroxy-5-methyl-4-isoxazole propionic acid (AMPA)-selective binding pharmacology"].
- GluA1 carries a genomically encoded Gln at the Q/R site and is not edited; GluA1
  homomers and GluA1/GluA3 receptors are Ca2+-permeable, while co-assembly with
  edited GluA2 abolishes Ca2+ permeability
  [PMID:1709304 "At physiological resting potentials, KA and AMPA elicited inward calcium currents in oocytes expressing GluR1, GluR3, and GluR1 plus GluR3."]
  [PMID:1709304 "In contrast, oocytes expressing GluR1 plus GluR2 or GluR3 plus GluR2 showed no such permeability."].
  Quantitative Ca2+ permeability of GluR-A(Q) channels was measured by Jatzke et al.
  [PMID:11773314 "For GluR-A(Q) channels, P(Ca)/P(Na) derived from all three approaches was concentration independent"].
- Auxiliary subunits: TARPs and cornichons co-assemble with GluA1-containing
  receptors and modulate gating and surface expression
  [PMID:19265014 "Coassembly with cornichon homologs 2 and 3 affects AMPARs in two ways: Cornichons increase surface expression of AMPARs, and they alter channel gating by markedly slowing deactivation and desensitization kinetics."]
  [PMID:17409242 "the extent of TARP-mediated increase in agonist-induced responses is highly dependent on both the AMPA receptor subunit and the coexpressed TARP"].
- Structure: the principal hippocampal AMPAR is a GluA1/GluA2 heteromer with TARP
  gamma-8 [PMID:30872532 "Here, we present a cryo-electron microscopy structure of the heteromeric GluA1/2 receptor associated with two transmembrane AMPAR regulatory protein (TARP) γ8 auxiliary subunits, the principal AMPAR complex at hippocampal synapses."].
  N-terminal domains drive assembly
  [PMID:21317873 "the extracellular, membrane-distal AMPAR N-terminal domains (NTDs) orchestrate selective routes of heteromeric assembly"]
  [PMID:19461580 "Here we show that AMPA receptor GluR1- and GluR2-ATDs form tightly associated dimers"].

## Trafficking and plasticity

- GluA1 carries a C-terminal type I PDZ ligand that binds SAP97
  [PMID:16634638 "Synaptic delivery of GluR-A (GluR1) subunit-containing glutamate receptors depends on a C-terminal type I PDZ binding motif in GluR-A."].
- LTP and CaMKII drive GluA1-containing receptors into synapses by a PDZ-dependent
  mechanism [PMID:10731148 "These results show that LTP and CaMKII activity drive AMPA-Rs to synapses by a mechanism that requires the association between GluR1 and a PDZ domain protein."];
  GluA1/GluA2 receptors are added during plasticity, whereas GluA2/GluA3 receptors
  cycle constitutively [PMID:11348590 "GluR1/GluR2 receptors are added to synapses during plasticity; this requires interactions between GluR1 and group I PDZ domain proteins."].
- PKA phosphorylation (Ser845 in the mature-protein numbering used by most papers;
  Ser-863 in the UniProt precursor numbering of P19490) controls
  synaptic incorporation [PMID:12536214 "We found that PKA phosphorylation of the AMPA receptor subunits GluR4 and GluR1 directly controlled the synaptic incorporation of AMPA receptors in organotypic slices from rat hippocampus."].
  A beta2-adrenergic receptor/Gs/adenylyl cyclase/PKA complex is assembled with GluA1
  through stargazin and PSD-95 [PMID:19942860 "which is linked to the beta(2)AR through stargazin and PSD-95 and their homologues"].
- Loop1 CaMKII site S567 regulates synaptic targeting
  [PMID:21135237 "We also identified a CaMKII phosphorylation site (S567) in the GluA1 Loop1, which is phosphorylated in vitro and in vivo."].
- Endocytosis: AMPA- and insulin-induced internalization depend on GluA1 and GluA2
  tail determinants [PMID:11100149 "insulin- and AMPA-induced AMPA receptor internalization are differentially dependent on protein phosphatases and sequence determinants within the cytoplasmic tails of GluR1 and GluR2 subunits"];
  ubiquitinated GluA1 is internalised via Eps15
  [PMID:25023288 "Knockdown of Eps15 suppresses the internalization of GluA1 but not the mutant GluA1 that lacks ubiquitination sites"].
- Transient insertion of GluA2-lacking (GluA1-containing, Ca2+-permeable) receptors
  after LTP-inducing stimuli [PMID:22915106 "Here, we show that endogenous GluA1 is rapidly inserted at the synaptic plasma membrane of rat hippocampal neurons immediately after stimulation with elevated glycine, a treatment known to induce LTP."].
- Oxygen/glucose deprivation removes GluA2 but leaves surface GluA1 unchanged
  [PMID:19321442 "GluR1 surface expression was unaffected by OGD at all time points tested"].
- Palmitoylation by zDHHC3 restrains activity-dependent GluA1 surface delivery
  [PMID:29222408 "The excess of palmitic acid along with higher zDHHC3 levels causes hyper-palmitoylation of AMPA glutamate receptor subunit GluA1, hindering its activity-dependent trafficking to the plasma membrane."].

## Localization

Somatodendritic; concentrated at the postsynaptic density membrane of dendritic
spines of glutamatergic synapses, with endosomal, ER and smaller presynaptic pools
[PMID:15610164 "Immunoreactive gold particles for AMPA receptor subunits GluR1 and GluR2/3 were frequently found not only on postsynaptic but also on presynaptic profiles"]
[PMID:16903873 "All of the subunits were enriched in the postsynaptic fraction but were also present in the presynaptic and non-synaptic synaptosome fractions."].
UniProt notes GluA1 is excluded from axons (by similarity to mouse).

## Behaviour and drug-response literature

Many rat annotations come from expression studies in drug, stress, diet or toxin
paradigms (cocaine, morphine, ethanol, lithium, tributyltin, sucrose, leptin, BDNF,
glucocorticoid/miR-132, IL-10 under hypoxia). These report changes in GluA1 protein,
phosphorylation or surface level as a readout; they do not show that GluA1 executes
the "response" process. Knockdown/overexpression studies (CeA GluA1 in morphine CPP,
VTA GluA1 in cocaine motivation, hippocampal GluA1 ASO in inhibitory-avoidance memory)
show necessity of GluA1-containing AMPARs for drug- and memory-related plasticity
[PMID:23345231 "Adenoviral shRNA-mediated downregulation of CeA GluA1 produced opposite effects, inhibiting the processes of both CPP acquisition and CPP extinction."]
[PMID:19547753 "inhibiting GluR1 translation at any of both time points caused amnesia when the animals were tested 24 h after training"].
