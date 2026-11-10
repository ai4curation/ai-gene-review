# cac (cacophony; Dmca1A; nightblind A) -- manual literature synthesis

Manual synthesis written by the reviewer from cached publications (no deep-research
API was available). Quotes are verbatim from `publications/PMID_*.md`; papers marked
"abstract only" were assessed from the abstract.

## Identity and family

- UniProt P91645 (CAC1A_DROME), 1851 aa, FlyBase FBgn0263111. Sole Drosophila Cav2
  (N/P/Q/R-type) alpha1 subunit; the fly has one gene for each vertebrate Cav family
  (Cav1 = Ca-alpha1D, Cav2 = cac, Cav3 = Ca-alpha1T).
  [PMID:19004991 "In Drosophila, cac is the only Ca(v)2-type gene."]
- UniProt: four repeats of S1-S6 with S4 voltage sensors; "Belongs to the calcium
  channel alpha-1 subunit (TC 1.A.1.11) family"; InterPro IPR002077 (VDCCAlpha1),
  Pfam Ion_trans x4, Ca_chan_IQ, GPHH; PANTHER PTHR45628:SF7.
- Extensive alternative splicing (exon IS4A/B, I/II linker A/B) and Adar RNA editing.
  An alternative exon is differentially expressed in the eye (nbA^H18 stop codon)
  [PMID:9649530 "this mutant (originally nbAH18) has a stop codon in an alternative exon (within the cac ORF), which is differentially expressed in the eye"].

## Molecular function: voltage-gated Ca2+ channel pore subunit

- Cultured pupal brain neurons and adult antennal lobe projection neurons: CAC channels
  carry the slow-inactivating PLTXII-sensitive Ca2+ current
  [PMID:19004991 "CAC channels are the major contributors to the slow-inactivating PLTXII-sensitive current based on selective reduction of this component in hypomorphic cac mutants (NT27 and TS3)"] (abstract only).
- Adult motoneuron somatodendritic currents: Dmca1A carries HVA current and an
  amiloride-insensitive LVA component
  [PMID:22183725 "we show that Dmca1A underlies the HVA somatodendritic calcium currents in vivo"]
  [PMID:22183725 "We further demonstrated that the Ca(v)2 homolog, Dmca1A, mediated the amiloride-insensitive component of LVA current."] (abstract only).
- cac^TS2 (C-terminal missense) reduces presynaptic Ca2+ entry; the homologous mutation
  in rat Cav2.1 speeds inactivation
  [PMID:16820014 "Presynaptic Ca2+ signals evoked by single and multiple action potentials showed a temperature-dependent reduction."] (abstract only).
- UniProt: "Probably encodes a dihydropyridine-insensitive current." This matters for
  the Malpighian tubule work, which relies on dihydropyridine/phenylalkylamine
  pharmacology (below).

## Location: presynaptic active zone membrane

- GFP-Cac rescues lethality and localizes to active zones
  [PMID:14715960 "transgenic expression of a cac-encoded alpha1 subunit fused with enhanced green fluorescent protein efficiently rescues cac lethal mutations and allows in vivo analysis of calcium channel localization at active zones"].
- Bruchpilot (BRP) is required to cluster Cac at the AZ centre, beneath the T-bar
  [PMID:19596851 "Thus, the T-bar organized by BRP overlays the field of Ca2+ channels at the AZ center."]
  [PMID:19596851 "Thus, BRP seems to be directly required for Ca2+ channel clustering at AZs but not for its recruitment to the terminal."] (full text).
- Endogenous Cac at larval NMJ boutons co-localizes with BRP
  [PMID:24275199 "As expected cacophony immunofluorescence frequently co-localized with bruchpilot (Figure 4A)"].
- Malpighian tubule: an alpha1 antibody stains apical and basolateral membranes of
  principal cells [PMID:11208535 "Immunocytochemical evidence suggests localization of alpha1-subunits to both basolateral and apical surfaces of principal cells in the tubule main segment."] (abstract only; antibody specificity for Cac vs Ca-alpha1D not stated in the abstract).

## Process: evoked neurotransmitter release (core)

- cac^TS2 blocks release at restrictive temperature
  [PMID:10864946 "neurotransmitter release in cac(TS2) is markedly reduced at elevated temperatures, indicating that cac encodes a primary alpha1 subunit functioning in synaptic transmission"].
- Transgenic rescue
  [PMID:12122048 "Notably, rescue of rapid, calcium-triggered neurotransmitter release was achieved by neural expression of a single cDNA containing a subset of alternative exons and lacking any conserved synaptic-protein interaction sequence."] (full text).
- Exocytosis, not endocytosis, depends on Cac-mediated Ca2+ entry
  [PMID:14715138 "In a temperature-sensitive Ca(2+) channel mutant, cacophony(TS2), exocytosis induced by high K(+) decreased at nonpermissive temperatures, while endocytosis remained unchanged."].
- AP-independent (mini) release at central cholinergic synapses
  [PMID:19004991 "Another characteristic of cac mutant neurons both in culture and in whole brain recordings is a reduced cholinergic miniature excitatory postsynaptic current frequency that is mimicked in wild-type neurons by acute application of PLTXII."].
- Photoreceptor axon terminals (lamina)
  [PMID:22952921 "revealed depolarization-induced Ca(2+) increments mediated by cacophony"]
  [PMID:22952921 "Single synaptic boutons resolved in the lamina by FM4-64 fluorescence revealed that vesicle exocytosis depends on cacophony, TRP and TRPL."] (full text; note the immunostaining used an anti-alpha1-N-type antibody because no Cac-specific antibody was available; the cac^TS2 FM4-64 assay is the gene-specific evidence).
- Amacrine-cell feedback to photoreceptors
  [PMID:25831426 "These results suggest that Cac channels mediate synaptic glutamate release from ACs."] (full text).
- Presynaptic homeostatic potentiation converges on Cac
  [PMID:19249276 "These genetic data are consistent with a model in which the Cac channel resides downstream of Exn in a presynaptic, homeostatic signaling system at the Drosophila NMJ."] (full text).

## Other reported roles (non-core / downstream)

- Synaptic growth at the NMJ [PMID:12896973 "an allele of the N-type calcium channel locus (Dmca1A) was identified that caused synaptic undergrowth"].
- Dendrite pruning of class IV da neurons through local VGCC-mediated Ca2+ transients
  [PMID:23722427 "intrinsic excitability increased locally to activate calcium influx via the voltage-gated calcium channels (VGCCs), and blockade of the VGCC activities impaired pruning"] (abstract only).
- Autophagosome-lysosome fusion in photoreceptor terminals
  [PMID:25811491 "Here, we show that cac mutant photoreceptor terminals accumulate AV-lysosomal fusion intermediates, suggesting that Cac is necessary for the fusion of AVs with lysosomes, a poorly defined process."]
  Lysosomal localization was shown only for mouse CACNA1A in that paper
  [PMID:25811491 "Moreover, we find that CACNA1A is localized to the lysosomes and that loss of lysosomal Cacna1a in cerebellar cultured neurons leads to a failure of lysosomes to fuse with endosomes and autophagosomes."].
- Courtship song (cac^S): [PMID:9649530 "The cacS mutant, which exhibits defects in the patterning of courtship lovesong and a newly revealed but subtle abnormality in visual physiology, is mutated such that a highly conserved phenylalanine (in one of the quasi-homologous intrapolypeptide regions called IIIS6) is replaced by isoleucine."]
- Temperature-sensitive locomotor defects [PMID:9504928 "When exposed to high temperatures (37 degrees), cac flies show frequent convulsions and pronounced locomotor defects."]
- Heart rate [PMID:16076631 "Hearts of both cac(S) and cac(TS2) mutants beat significantly more rapidly than wild type and the heartbeat is more regular across temperature."]
- Dopaminergic neuron vulnerability [PMID:25445363 "DA neurons lacking functional Ca(2+) channels (i.e., cacophony mutant) are inherently protected against MPP(+) toxicity."]
- TDP-43/TBPH regulates cac levels [PMID:24275199 "Restoring the levels of cacophony in all neurons or selectively in motor neurons rescued these locomotion defects."]
