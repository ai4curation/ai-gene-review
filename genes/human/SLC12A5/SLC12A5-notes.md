# SLC12A5 (KCC2) curation notes

UniProt: Q9H2X9 (S12A5_HUMAN). Neuron-specific electroneutral K+-Cl- cotransporter 2 (KCC2).
Batch: canonical-surfaceome backfill batch 4 (SLC12 family).

## Core biology (synthesis)

- **Electroneutral K+:Cl- cotransport (efflux).** KCC2 mediates coupled K+ and Cl-
  cotransport out of mature neurons. Catalytic reaction (UniProt CATALYTIC ACTIVITY):
  "Reaction=K(+)(in) + chloride(in) = K(+)(out) + chloride(out)" with Rhea:RHEA:72427,
  ECO:0000269|PubMed:12106695. Functional oocyte evidence: [PMID:12106695 "Expression of
  hKCC2 cRNA in Xenopus laevis oocytes results in significant Cl(-)-dependent (86)Rb(+)
  uptake under isotonic conditions; cell swelling under hypotonic conditions causes a
  20-fold activation"], with KM for K+ 9.3 mM and Cl- 6.8 mM; "The K(m) for Cl(-) is close
  to the intracellular Cl(-) activity of mature neurons, as befits a neuronal efflux
  mechanism." Core MF = GO:0015379 potassium:chloride symporter activity.
- **Neuronal chloride homeostasis / inhibitory Cl- gradient.** As the major Cl- extruder,
  KCC2 keeps [Cl-]i low so GABA-A/glycine receptor opening causes Cl- influx and
  hyperpolarization. UniProt FUNCTION: "As major extruder of intracellular chloride, it
  establishes the low neuronal Cl(-) levels required for chloride influx after binding of
  GABA-A and glycine to their receptors, with subsequent hyperpolarization and neuronal
  inhibition." [PMID:12106695 "The expression level of the neuronal-specific K-Cl
  cotransporter KCC2 (SLC12A5) is a major determinant of whether neurons will respond to
  GABA with a depolarizing, excitatory response or a hyperpolarizing, inhibitory
  response."] Disease (DEE34/EIMFS): [PMID:26333769 "We demonstrate that the identified
  mutants negatively impact KCC2 protein expression and glycosylation, with impaired
  KCC2-mediated chloride extrusion."] Core BP = GO:0030644 intracellular chloride ion
  homeostasis, GO:1902476 chloride transmembrane transport, GO:0071805 potassium ion
  transmembrane transport.
- **Transport-INDEPENDENT structural role in dendritic spines.** Documented as a genuine
  second function. [PMID:24668262 "rodent KCC2 has (independently of its role as an ion
  transporter) been shown to play an important role as a structural protein required for
  the morphological and functional maturation of cortical dendritic spines"]; the human
  disease variant R952H "reduces neuronal Cl(-) extrusion and has a compromised ability to
  induce dendritic spines in vivo and in vitro" and shows "reduced surface expression".
  GO:0060996 dendritic spine development (IDA PMID:24668262). Treated as KEEP_AS_NON_CORE
  (real, distinct from the core transport activity).
- **Localization.** Plasma membrane, enriched on dendrites/soma; UniProt SUBCELLULAR
  LOCATION "Cell membrane; Multi-pass membrane protein. Cell projection, dendrite.
  Note=Detected on dendrites, but not on axons ... and at GPHN-positive inhibitory
  synapses." Also reported at excitatory (glutamatergic) synapses/spines.
- **Regulation.** Inhibited by WNK-SPAK/OSR1 phosphorylation at Thr929/Thr1030
  (PubMed:19665974); activated by cell swelling (hypotonicity). Homodimer (domain-swapped);
  can heterodimerize with SLC12A6/SLC12A7 (cryo-EM PubMed:33199848, PubMed:33310850).

## Secondary / promiscuous activities

- **Ammonium.** KCCs carry NH4+ in place of K+. BP GO:0072488 ammonium transmembrane
  transport (IEA, rat ortholog) = genuine secondary cotransport -> KEEP_AS_NON_CORE. But
  MF GO:0008519 "ammonium channel activity" is mechanistically WRONG: OLS def = "facilitated
  diffusion of ammonium through a transmembrane aqueous pore or channel." KCC2 is a
  secondary-active electroneutral symporter, not a channel -> MARK_AS_OVER_ANNOTATED.
- GO:0051452 intracellular pH reduction (IEA, rat ortholog): electroneutral K-Cl
  cotransport does not directly acidify; likely an NH4+-linked inference -> MARK_AS_OVER_ANNOTATED.
- GO:0006971 hypotonic response (IDA PMID:12106695): real swelling-activation property of
  KCCs, but peripheral to the neuronal core -> KEEP_AS_NON_CORE.

## Over-propagation flags

- GO:0016324 apical plasma membrane (IBA): propagated from epithelial SLC12 members
  (NKCC2/NCC etc.); KCC2 is neuronal, not epithelial apical -> MARK_AS_OVER_ANNOTATED.
  The plasma-membrane claim itself is captured by GO:0005886.

## Too-general (entailed by accepted specific terms)

- GO:0006811 monoatomic ion transport; GO:0006813 potassium ion transport; GO:0006821
  chloride transport; GO:0055085 transmembrane transport; GO:0022857 transmembrane
  transporter activity; GO:0015377 chloride:monoatomic cation symporter activity;
  GO:0015108 chloride transmembrane transporter activity; GO:0032502 developmental process.
- membrane / cell periphery -> MODIFY to GO:0005886 plasma membrane.

## Synapse / receptor organization (IEA from rat ortholog, documented KCC2 biology)

- GO:0098970 postsynaptic neurotransmitter receptor diffusion trapping; GO:0150052
  regulation of postsynapse assembly; GO:0098978 glutamatergic synapse; GO:0099634
  postsynaptic specialization membrane -> KEEP_AS_NON_CORE (KCC2 C-terminal scaffolding
  role; no cached primary paper to quote, kept per curated ortholog IEA + known biology).
