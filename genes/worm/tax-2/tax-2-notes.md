# tax-2 (C. elegans) — Gene Review Notes

UniProt: G5EEE2 (G5EEE2_CAEEL) | WormBase: WBGene00006525 / F36F2.5 | 800 aa
Gene name origin: *tax* = **ta**xis abnormal / thermota**x**is-abnormal (isolated in chemotaxis/thermotaxis screens).

## One-line summary
TAX-2 is the **modulatory beta subunit** of the sensory cyclic-nucleotide-gated (CNG) cation
channel of *C. elegans*. It partners with the alpha (pore-forming) subunit **TAX-4** to form the
native heteromeric cGMP-gated channel in ciliated sensory neurons. TAX-2 **cannot form a channel
on its own**; it tunes the channel's ligand sensitivity and is required for its correct ciliary
localization.

## Protein architecture (from UniProt G5EEE2)
- Ion-transport (pore) domain: Pfam PF00520 (Ion_trans); TM helices predicted ~220-242, ~254-274 (Phobius).
- Cyclic-nucleotide-binding domain (CNBD): Pfam PF00027; PROSITE PS50042 at residues 538-642.
- InterPro family IPR050866 CNG_cation_channel; PANTHER PTHR45638 (Cyclic Nucleotide-Gated Cation Channel),
  subfamily PTHR45638:SF1 "CYCLIC NUCLEOTIDE-GATED ION CHANNEL SUBUNIT B" — i.e. classified as a **CNGB-type (beta)** subunit.
- TCDB 1.A.1.5.19 (voltage-gated ion channel VIC superfamily).
- Long disordered N- and C-terminal regions (21-75; 733-800, acidic).

## KNOWN (well-supported)

### Molecular function / complex — CORE
- TAX-4 (alpha) and TAX-2 (beta) form a **heteromeric CNG channel** when co-expressed in HEK293 cells;
  **TAX-2 does not form a channel on its own**. Native channels are likely TAX-4/TAX-2 hetero-oligomers,
  "with TAX-4 as the alpha subunit and TAX-2 acting as a modifying beta subunit."
  [PMID:10064800 "Here we show that TAX-4 and TAX-2 form a heteromeric channel when expressed in HEK293 cells, but TAX-2 does not form a channel on its own."]
  [PMID:10064800 "with TAX-4 as the alpha subunit and TAX-2 acting as a modifying beta subunit."]
- TAX-2 is "most closely related to the beta subunits of the rod phototransduction channels."
  [PMID:10064800 "TAX-2 is most closely related to the beta subunits of the rod phototransduction channels."]
- The heteromer **tunes ligand sensitivity**: "The heteromeric TAX-4/TAX-2 channel is 25-fold less sensitive
  to cGMP than the TAX-4 channel, but it remains highly selective for cGMP over cAMP." The heteromer and TAX-4
  homomer also differ in divalent-cation block and single-channel properties.
  [PMID:10064800 "The heteromeric TAX-4/TAX-2 channel is 25-fold less sensitive to cGMP than the TAX-4 channel, but it remains highly selective for cGMP over cAMP."]
- Original genetics: "The tax-2 and tax-4 genes of C. elegans encode two subunits of a cyclic nucleotide-gated
  channel that is required for chemosensation, thermosensation and normal axon outgrowth of some sensory neurons."
  [PMID:9486798 "The tax-2 and tax-4 genes of C. elegans encode two subunits of a cyclic nucleotide-gated channel that is required for chemosensation, thermosensation and normal axon outgrowth of some sensory neurons."]

### Localization — CORE
- Channel acts at the **plasma membrane / sensory cilia** of ciliated neurons. Ciliary targeting is
  subunit- and cell-specific; sequences required for ciliary targeting/localization of the TAX-2 CNGB and
  TAX-4 CNGA subunits have been mapped, and ciliary localization of the two subunits is interdependent.
  [PMID:23886944 "identify sequences required for efficient ciliary targeting and localization of the TAX-2 CNGB and TAX-4 CNGA subunits."]
  [PMID:23886944 "TAX-2 and TAX-4 are relatively immobile in specific sensory cilia subcompartments"]
- The alpha subunit TAX-4::GFP is "partly localized at the sensory endings of these neurons."
  [PMID:8893027 "The Tax-4::GFP fusion is partly localized at the sensory endings of these neurons."] (alpha subunit; supports plasma-membrane/sensory-ending localization of the channel)

### Sensory physiology / behavior (channel-dependent) — NON-CORE (downstream of channel activity)
- **Chemotaxis**: "tax-2 activity is required in the adult stage for normal chemotaxis to NaCl and odorants."
  [PMID:9486798 "tax-2 activity is required in the adult stage for normal chemotaxis to NaCl and odorants."]
- **Sensory axon maintenance**: "tax-2 and tax-4 are required for the maintenance of correct axon structure";
  a ts tax-2 allele shows tax-2 activity is required in the adult to preserve axon morphology.
  [PMID:9486798 "these results indicate that tax-2 and tax-4 are required for the maintenance of correct axon structure"]
- **Oxygen sensing / aerotaxis / hyperoxia**: "Avoidance of high oxygen levels by C. elegans requires the sensory
  cGMP-gated channel tax-2/tax-4 and a specific soluble guanylate cyclase homologue, gcy-35."
  [PMID:15220933 "Avoidance of high oxygen levels by C. elegans requires the sensory cGMP-gated channel tax-2/tax-4 and a specific soluble guanylate cyclase homologue, gcy-35."]
- **O2-evoked cGMP/Ca2+ dynamics & feedback**: "Increased cGMP leads to a sustained Ca(2+) response in the neuron
  that depends on cGMP-gated ion channels"; "Elevated levels of cGMP and Ca(2+) stimulate competing negative
  feedback loops that shape cGMP dynamics."
  [PMID:23940325 "Increased cGMP leads to a sustained Ca(2+) response in the neuron that depends on cGMP-gated ion channels."]
  [PMID:23940325 "Elevated levels of cGMP and Ca(2+) stimulate competing negative feedback loops that shape cGMP dynamics."]
- **Phototransduction (G-protein/cGMP pathway)**: light-evoked dark current in ASJ "was absent in the CNG channel
  mutants tax-2 and tax-4"; LITE-1-dependent photocurrent "also required the GC DAF-11 and the CNG channel TAX-2 and TAX-4."
  [PMID:20436480 "This dark current was apparently carried by CNG channels, as it can be blocked by the CNG channel-specific inhibitor L-cis-diltiazem and was absent in the CNG channel mutants tax-2 and tax-4"]
  [PMID:20436480 "the LITE-1-dependent photocurrent in ASI also required the GC DAF-11 and the CNG channel TAX-2 and TAX-4"]
- **Thermosensation/thermotaxis**: tax-2/tax-4 essential for thermosensation (PMID:10064800; PMID:9486798).
  PMID:7630402 (Mori & Ohshima 1995, the WormBase original ref for thermosensory behavior) is the thermotaxis
  neural-circuit paper; full text not in cache and the abstract centers on AFD/AIY/AIZ, but tax-2 was isolated
  as a thermotaxis-abnormal (*tax*) mutant and its thermosensory requirement is independently established.
- **Chemosensory control of gene expression / neuroendocrine signaling**: ASJ chemosensation of P. aeruginosa
  metabolites "induces expression of the neuromodulator DAF-7/TGF-β"; TAX-2/TAX-4 is the ASJ chemosensory channel upstream.
  [PMID:25303524 "induces expression of the neuromodulator DAF-7/TGF-β"]
- **Thermosensory-neuron gene expression / morphology**: CMK-1 and TAX-4 (the channel TAX-2 co-forms) "regulate
  gene expression, morphology, and functions of the AFD thermosensory neurons"; TAX-4 activity is required during
  larval stages to maintain adult gene expression. (Abstract foregrounds TAX-4; TAX-2 is the obligate partner subunit.)
  [PMID:14711416 "the TAX-4 cyclic nucleotide-gated channel regulate gene expression, morphology, and functions of the AFD thermosensory neurons"]

## NOT known / uncertain (knowledge gaps)
1. **Mechanism of beta-subunit modulation.** How TAX-2 lowers cGMP sensitivity ~25-fold and alters divalent-cation
   block / single-channel behavior of the heteromer, and whether it does so uniformly across neurons, is not
   mechanistically defined. [PMID:10064800]
2. **Does the TAX-2 CNBD bind cGMP?** TAX-2 has a CNBD (PS50042, 538-642) and carries an IBA cGMP-binding annotation,
   but direct biochemical cGMP binding by the TAX-2 CNBD (vs. a modulatory/non-canonical CNBD as in vertebrate CNGB)
   has not been demonstrated. Beta-subunit CNBDs are frequently ligand-non-functional or purely modulatory.
3. **In vivo stoichiometry & composition.** The endogenous TAX-4:TAX-2 ratio and whether composition varies between
   neurons or ciliary subcompartments is inferred, not measured; ciliary localization is subunit-interdependent
   and heterogeneous across the cilium. [PMID:23886944, PMID:10064800]
4. **tax-2 roles independent of tax-4.** Because TAX-2 forms no channel alone, an independent conductance is unlikely,
   but whether TAX-2 has tax-4-independent roles (e.g. partnering other alpha subunits such as CNG-1/CNG-3, or
   non-conducting/structural/trafficking roles) is unresolved. [PMID:10064800, PMID:23886944]

## Ligand-selectivity note (affects cAMP annotation)
The native worm heteromer "remains highly selective for cGMP over cAMP" [PMID:10064800]. The GOA IBA term
GO:0005222 (intracellularly cAMP-activated cation channel activity) is inherited from the PANTHER CNG family
(which contains cAMP-responsive vertebrate CNGA2) and over-states cAMP as a physiological ligand for the worm
TAX-2/TAX-4 channel → marked as over-annotated.

## Annotation plan (25 GOA annotations)
- CORE channel MF/CC/transport (ACCEPT): plasma membrane (IBA), cGMP binding (IBA), monoatomic cation
  transmembrane transport (IBA+IDA), intracellular cyclic-nucleotide-activated cation channel complex (IBA),
  monoatomic ion channel activity (IEA), intracellularly cyclic-nucleotide-activated monoatomic cation channel
  activity (IEA), monoatomic ion transport (IEA), transmembrane transport (IEA), membrane (IEA),
  **intracellularly cGMP-activated cation channel activity (IDA, contributes_to)**, cation channel complex (IDA, part_of).
- OVER-ANNOTATED: intracellularly cAMP-activated cation channel activity (IBA) — heteromer is cGMP-selective.
- NON-CORE (KEEP): positive regulation of gene expression, GPCR signaling coupled to cGMP, negative regulation of
  receptor guanylyl cyclase signaling, response to oxygen levels, thermosensory behavior, chemotaxis, regulation of
  axon extension, aerotaxis, response to hyperoxia, regulation of neuron differentiation, positive regulation of
  transcription by RNA Pol II, neuron projection morphogenesis. All are downstream sensory outputs of channel activity.

## Cross-reference
tax-4 (alpha subunit) review: PR #1716 (branch claude/worm-tax-4-review). Channel-complex modeling kept consistent:
in_complex = GO:0017071; native channel is TAX-4/TAX-2 heteromer. tax-2 modeled with contributes_to_molecular_function
to reflect its beta/modulatory (non-pore-forming-alone) role.
