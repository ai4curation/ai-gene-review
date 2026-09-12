# tax-4 (Q03611, CNG_CAEEL) research notes

Research journal for the *C. elegans* gene **tax-4** (WormBase WBGene00006526; ZC84.2;
UniProt Q03611). Provenance is recorded inline as `[PMID:xxxx "verbatim quote"]`.

## Identity / one-line

TAX-4 is the **alpha (principal, pore-forming) subunit of a cyclic nucleotide-gated
(CNG) cation channel**. It is directly gated by intracellular cGMP (and, less
sensitively, cAMP), conducts Ca2+/Na+/K+ cations, and localizes to the sensory cilia
(and dendrites) of many ciliated sensory neurons, where it is the effector channel of
cGMP-based sensory transduction. TAX-4 forms functional **homotetramers** in vitro and
in structural studies, and in vivo partners with the modulatory beta subunit **TAX-2**
to form the native heteromeric sensory channel.

## KNOWN (well supported)

### Molecular function: cGMP-gated cation channel (alpha subunit)
- TAX-4 alone forms a functional, highly cGMP-sensitive channel when expressed in
  mammalian cells; TAX-2 alone does not.
  [PMID:10064800 "TAX-4 has previously been shown to form a highly sensitive cGMP-gated channel when expressed in human HEK293 cells. Here we show that TAX-4 and TAX-2 form a heteromeric channel when expressed in HEK293 cells, but TAX-2 does not form a channel on its own."]
- TAX-4 = alpha subunit, TAX-2 = modifying beta subunit; the native channel is a
  hetero-oligomer.
  [PMID:10064800 "with TAX-4 as the alpha subunit and TAX-2 acting as a modifying beta subunit."]
- The heteromeric channel is ~25-fold less cGMP-sensitive than the TAX-4 homomer but
  stays cGMP-selective; the two forms also differ in divalent-cation block and single-
  channel properties.
  [PMID:10064800 "The heteromeric TAX-4/TAX-2 channel is 25-fold less sensitive to cGMP than the TAX-4 channel, but it remains highly selective for cGMP over cAMP. The heteromeric channel and the TAX-4 homomeric channel differ in their blockage by divalent cations and in their single channel properties."]
- Original genetic/expression characterization: tax-4 mutants fail multiple sensory
  behaviors; TAX-4 is homologous to vertebrate CNG channels and functions as a CNG
  channel in cultured cells; cGMP is the intracellular messenger.
  [PMID:8893027 "We show that the predicted tax-4 gene product is highly homologous to vertebrate cyclic nucleotide-gated channels. Tax-4 protein expressed in cultured cells functions as a cyclic nucleotide-gated channel."]

### Structure (all solved on the C. elegans TAX-4 protein)
- cryo-EM of the C. elegans CNG channel in the cGMP-bound open state; homotetramer with
  an unusual voltage-sensor-like domain (deficient voltage dependence); C-linker gating
  ring couples cyclic-nucleotide binding to the gate; selectivity filter lined by a
  functionally important glutamate + backbone carbonyls.
  [PMID:28099415 "Here we report a 3.5-Å-resolution single-particle electron cryo-microscopy structure of a cyclic-nucleotide-gated channel from Caenorhabditis elegans in the cyclic guanosine monophosphate (cGMP)-bound open state."]
  [PMID:28099415 "The selectivity filter is lined by the carboxylate side chains of a functionally important glutamate and three rings of backbone carbonyls."]
- Mechanism of ligand (cGMP) activation; open/closed states; central-gate residues
  (F403, V407) and CNBD contacts characterized by mutagenesis.
  [PMID:32483338 "Mechanism of ligand activation of a eukaryotic cyclic nucleotide-gated channel."]
- UniProt SUBUNIT: `Homotetramer. {ECO:0000269|PubMed:28099415, ...:32483338, ...:35233102}`.
  Note the IPI `identical protein binding` GOA annotations (PMID:28099415, PMID:32483338)
  reflect this homotetramer self-association.

### Cellular localization
- Expressed at the sensory endings of thermosensory, gustatory, and olfactory neurons;
  TAX-4::GFP partly localized to sensory endings.
  [PMID:8893027 "The Tax-4::GFP fusion is partly localized at the sensory endings of these neurons."]
- Localizes to (non-motile) sensory cilia; ciliary trafficking/localization of the
  TAX-4 CNGA and TAX-2 CNGB subunits is cell- and subunit-specific.
  [PMID:23886944 "identify sequences required for efficient ciliary targeting and localization of the TAX-2 CNGB and TAX-4 CNGA subunits."]
- In AFD, the cGMP-gated channel is anchored within the proximal ciliary region by
  NPHP-2/inversin — the ciliary "inversin compartment".
  [PMID:25335890 "requires NPHP-2 (known as inversin in mammals) to anchor a cGMP-gated ion channel within the proximal ciliary region."]
- Cilia membrane composition/morphogenesis context (TUB-1/Tubby); CNG channel is a
  ciliary signaling cargo. [PMID:31259686] (localization/tissue-specificity reference in
  UniProt; SUBCELLULAR LOCATION Cell projection, cilium.)

### Biological processes (cGMP sensory transduction as effector channel)
- **Thermosensation / thermotaxis:** tax-4 mutants fail temperature responses; TAX-4 is
  required for AFD thermosensitivity and isothermal tracking.
  [PMID:8893027 "they fail to respond to temperature or to water-soluble or volatile chemical attractants."]
  [PMID:21315599 "Mutations in the tax-4 cyclic nucleotide-gated (CNG) channel have been shown to abolish AFD thermosensitivity and IT"]
- **AFD gene expression / neuron function:** CMK-1 and TAX-4 regulate AFD gene
  expression, morphology and function; TAX-4 needed in larval stages to maintain adult
  gene expression; acts cell-autonomously.
  [PMID:14711416 "the CMK-1 Ca2+/calmodulin-dependent protein kinase I (CaMKI) and the TAX-4 cyclic nucleotide-gated channel regulate gene expression, morphology, and functions of the AFD thermosensory neurons."]
- **O2 sensation / aerotaxis / hyperoxia avoidance:** high-O2 avoidance requires the
  tax-2/tax-4 CNG channel + sGC gcy-35.
  [PMID:15220933 "Avoidance of high oxygen levels by C. elegans requires the sensory cGMP-gated channel tax-2/tax-4 and a specific soluble guanylate cyclase homologue, gcy-35."]
- **O2-evoked cGMP/Ca2+ dynamics:** cGMP rise → sustained Ca2+ response that depends on
  cGMP-gated ion channels (negative-feedback architecture).
  [PMID:23940325 "Increased cGMP leads to a sustained Ca2+ response in the neuron that depends on cGMP-gated ion channels."]
- **CO2 sensation / avoidance:** CO2-evoked Ca2+ responses in AFD and BAG neurons
  require cGMP-gated ion channels; CO2 avoidance requires channels containing TAX-2/TAX-4.
  [PMID:21435556 "CO2-evoked Ca2+ responses in AFD and BAG neurons require cGMP-gated ion channels."]
  [PMID:21435556 "Avoidance requires cGMP-gated ion channels containing the TAX-2 and TAX-4 subunits"]
- **Phototransduction (ASJ):** light → G-protein → cGMP → opening of cGMP-sensitive CNG
  channels in ASJ photoreceptor neuron.
  [PMID:20436480 "opening of cGMP-sensitive CNG channels and stimulation of photoreceptor cells."]
- **Chemosensation / neuroendocrine signaling:** chemosensory detection in ASJ of P.
  aeruginosa metabolites induces daf-7/TGF-β expression (UniProt: TAX-4 up-regulates daf-7
  transcription in ASI/ASJ). [PMID:25303524] (positive regulation of gene expression).
- **Sensory axon maintenance:** tax-2/tax-4 required for maintenance of correct sensory
  axon structure (inappropriate late-larval axon outgrowth in mutants).
  [PMID:9486798 "tax-2 and tax-4 are required for the maintenance of correct axon structure"]

## NOT known / open questions (candidate knowledge_gaps)
1. **In vivo subunit stoichiometry of the native TAX-4/TAX-2 channel.** In vitro/structural
   work shows TAX-4 forms homotetramers [PMID:28099415], and TAX-4+TAX-2 form a heteromer
   in HEK293 [PMID:10064800], but the exact TAX-4:TAX-2 subunit ratio and arrangement of
   the *native* sensory channel in worm cilia is not established.
2. **Homomeric vs heteromeric gating in vivo.** The homomeric TAX-4 channel is ~25× more
   cGMP-sensitive than the TAX-4/TAX-2 heteromer [PMID:10064800]; which form operates in
   which neuron, and how the beta subunit tunes ligand sensitivity/selectivity in the
   physiological setting, is unresolved. Subunit composition may even vary across ciliary
   subcompartments within one cell [PMID:23886944].
3. **Ligand selectivity in vivo (cGMP vs cAMP).** TAX-4 is cGMP-selective but also cAMP-
   responsive (GO:0005222); whether cAMP-gating is ever physiologically used, and what sets
   in-vivo ligand tuning, is unclear.
4. **Ion selectivity / Ca2+ vs monovalent flux in vivo.** The channel conducts Ca2+, Na+,
   K+ (UniProt CATALYTIC ACTIVITY / Rhea); the relative in-vivo permeation and how Ca2+
   entry vs depolarization is apportioned across the many neuron types is not quantified.
5. **Mechanism of the non-channel/"regulatory" roles** (AFD gene-expression maintenance
   [PMID:14711416]; daf-7 induction [PMID:25303524]; axon-structure maintenance
   [PMID:9486798]) — presumably all downstream of channel-mediated Ca2+ signaling, but the
   causal chain from channel activity to transcriptional/morphological output is not fully
   defined.

## Annotation-review orientation (core vs non-core)
- **CORE molecular function:** cGMP-gated cation channel activity (GO:0005223,
  intracellularly cGMP-activated cation channel activity), cAMP-activated variant
  (GO:0005222), cGMP binding (GO:0030553); monoatomic cation transmembrane transport
  (GO:0098655).
- **CORE cellular component:** plasma membrane (GO:0005886); non-motile cilium
  (GO:0097730); cation channel complex / CNG channel complex (GO:0034703, GO:0017071);
  dendrite (GO:0030425); ciliary inversin compartment (GO:0097543).
- **CORE-ish process:** sensory perception of chemical stimulus (GO:0007606); detection of
  chemical stimulus involved in sensory perception (GO:0050907); the specific modalities
  (thermosensory behavior, thermotaxis, aerotaxis, response to hyperoxia/oxygen, detection
  of CO2, phototransduction, chemotaxis, olfactory behavior) are downstream sensory
  outputs — KEEP but as NON-CORE consequences of the one channel activity.
- **NON-CORE / pleiotropic consequences:** regulation of axon extension (GO:0030516),
  neuron projection morphogenesis (GO:0048812), regulation of neuron differentiation
  (GO:0045664), positive regulation of transcription/gene expression (GO:0045944,
  GO:0010628), positive regulation of growth rate (GO:0040010), calcium-mediated signaling
  (GO:0019722), negative regulation of receptor guanylyl cyclase signaling (GO:0010754).

## IEA over-annotations to flag (from InterPro/ARBA electronic mapping)
- **GO:0005249 voltage-gated potassium channel activity (IEA:InterPro)** — misleading.
  TAX-4 belongs to the CNG family within the voltage-gated-channel superfamily but has an
  *unusual voltage-sensor-like domain accounting for deficient voltage dependence*
  [PMID:28099415] and is a **non-selective cation** channel, not a K+-selective, voltage-
  gated K+ channel. Family-level InterPro (EAG/ELK/ERG signature) drags in this term.
- **GO:0006813 / GO:0071805 potassium ion transport / transmembrane transport (IEA)** and
  **GO:0006811 monoatomic ion transport (IEA)** — K+-specific process terms are an
  over-annotation of the same non-selective-cation reality; the channel does conduct K+ but
  is not a dedicated K+ transporter. General monoatomic cation transport (GO:0098655) is
  the accurate term.
