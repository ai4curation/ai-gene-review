# eat-4 (P34644) — vesicular glutamate transporter EAT-4 — curation notes

## Identity

- UniProt P34644 (EAT4_CAEEL, reviewed), 576 aa, major facilitator superfamily,
  sodium/anion cotransporter family, VGLUT subfamily (IPR011701 MFS; IPR020846 MFS domain).
  Orthologue of mammalian SLC17A6/7/8 (VGLUT1-3); the worm has a single VGLUT gene, so
  eat-4 expression defines glutamatergic neuron identity.
- Historical note: eat-4 was cloned as a homologue of rat BNPI (brain-specific Na+/Pi
  cotransporter I) before BNPI was shown to be VGLUT1; the Na-Pi cotransporter interpretation
  in the 1999 paper is superseded and later worm papers uniformly call EAT-4 the VGLUT.

## Literature

### Lee et al. 1999 (PMID:9870947, full text cached)

- "We find that eat-4 encodes a protein similar in sequence to a mammalian brain-specific
  sodium-dependent inorganic phosphate cotransporter I (BNPI)" [PMID:9870947].
- "Loss-of-function mutations in eat-4 cause defective glutamatergic chemical transmission
  but appear to have little effect on other functions of neurons" [PMID:9870947].
- "In eat-4 mutants, pharyngeal muscle relaxation is delayed because of dramatically reduced
  pharyngeal motor neuron M3 synaptic transmission" [PMID:9870947]; "This result indicates
  that eat-4 affects M3 transmission presynaptically" [PMID:9870947].
- "We demonstrated a similar presynaptic role of eat-4 in the synaptic transmission of the
  anterior touch cells ALM and AVM" [PMID:9870947].
- "Together, these observations suggest that the loss of eat-4 function specifically leads
  to a reduced capacity of glutamatergic neurons to release glutamate into synaptic
  junctions" [PMID:9870947]; the authors already raise vesicle loading: "the effect of eat-4
  mutations on glutamatergic neurotransmission could be explained by a reduction in the
  loading or the exocytosis of synaptic vesicles" [PMID:9870947].
- Expression: "eat-4 is expressed predominantly in a specific subset of neurons, including
  several proposed to be glutamatergic" [PMID:9870947]; in the pharynx in M3 and NSM.

### Kass et al. 2001 (PMID:11717360, full text cached)

- "All three ASH-mediated sensory behaviors are defective in eat-4 mutants ( Berger et al.,
  1998 ; Hart et al., 1999 ), which lack the vesicular glutamate transporter (VGLUT)"
  [PMID:11717360] (nose touch, osmotic avoidance, octanol avoidance). "The eat-4 VGLUT gene
  is expressed in the ASH neurons" [PMID:11717360].
- "We found that eat-4 VGLUT ;egl-3 PC2 double mutants were insensitive to nose touch (Fig.
  5 B ), suggesting that glutamate release is required for restoration of the nose touch
  response" [PMID:11717360]. Basis of the IMP/IGI rows for response to mechanical stimulus,
  hyperosmotic response and positive regulation of backward locomotion (nose touch evokes
  reversal).

### Keane & Avery 2003 (PMID:12750328, abstract only)

- "Tail tap of adults inhibits pharyngeal pumping via a pathway involving the innexin gene
  unc-7 and components of the glutamatergic pathway encoded by the genes avr-14 and avr-15"
  [PMID:12750328]. eat-4 is not in the abstract; the IMP/IGI rows for regulation of
  pharyngeal pumping presumably come from eat-4(ky5) tests in the full text. The eat-4
  pumping phenotype is independently established by Lee et al. 1999 (M3 transmission).

### Liu et al. 2007 (PMID:17611271, full text cached)

- "We found that eat-4(ky5) mutants displayed the male repetitive turning phenotype"
  [PMID:17611271]; "only the eat-4 glutamate signaling mutant exhibits the repetitive
  turning phenotype, suggesting that FLP and glutamate signaling coregulate male turning
  behavior" [PMID:17611271].

### Brockie et al. 2013 (PMID:24094107, full text cached)

- "Mutations in genes that disrupt glutamate release (eat-4) or the function of
  postsynaptic glutamate receptors (glr-1, sol-1 and stg-2) decrease reversal frequency"
  [PMID:24094107]; "Double mutants with cni-1 and eat-4, which encodes the vesicular
  glutamate transporter, were indistinguishable from eat-4 mutants alone" [PMID:24094107].

### Serrano-Saiz et al. 2017 (PMID:28065609, full text cached)

- "the expression of the vesicular glutamate transporter eat-4/VGLUT is strongly upregulated
  in PHC" [PMID:28065609] in males; "We found that male PHC becomes repurposed for male
  mating behavior since PHC silenced males show profound defects in vulva location behavior"
  [PMID:28065609]; "Similar defects can be observed upon genetically disrupting the
  neurotransmitter system, glutamate, used by all these neurons (PHB, PHC, HOA)"
  [PMID:28065609].

## Assessment

- Core: L-glutamate transmembrane transporter activity (GO:0005313) on the synaptic vesicle
  membrane, loading glutamate into synaptic vesicles (GO:0098700) for glutamatergic synaptic
  transmission (GO:0035249). All supported by IBA and by the worm loss-of-function data.
- The ISS row GO:0015501 glutamate:sodium symporter activity (template human SLC17A1/NPT1)
  is biologically wrong for a VGLUT: vesicular glutamate uptake is driven by the membrane
  potential component of the V-ATPase proton gradient, not by Na+ symport (Na+/glutamate
  symport is the EAAT/SLC1 mechanism).
- Plasma membrane (IEA from UniProt "Cell membrane") is a mis-placement; VGLUTs reside on
  synaptic vesicles, visiting the plasma membrane only transiently during exocytosis.
- Behavioural rows (osmotic avoidance, nose touch, reversal, pumping, male turning and
  mating) are downstream consequences of loss of glutamatergic transmission from specific
  neurons; kept as non-core.
- GO:0060076 excitatory synapse: in C. elegans several EAT-4-dependent glutamatergic synapses
  are inhibitory via glutamate-gated chloride channels (e.g. M3 -> pharyngeal muscle IPSPs
  via AVR-15), so "excitatory" is not universally correct for the worm VGLUT.

## Deep research

- `eat-4-deep-research-falcon.md` agrees on every point used here: EAT-4 is the worm VGLUT in
  the SLC17A6/7/8 lineage, its substrate is L-glutamate "which EAT-4 accumulates in synaptic
  vesicles so that exocytosis can produce glutamatergic transmission", its site of action is
  the presynaptic synaptic-vesicle membrane, and the 1999 Na-Pi cotransporter description is
  a historical mis-assignment that was never backed by a phosphate-transport assay.
