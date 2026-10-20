# unc-26 (synaptojanin) curation notes

UniProt G5ECL2 (SYNJ_CAEEL, Swiss-Prot), WormBase JC8.10. Module role:
synaptojanin PI(4,5)P2 5-phosphatase in the uncoating tier of
modules/synaptic_vesicle_endocytosis.yaml (GO:0004439 -> GO:0016191).

## Founding phenotype (Harris et al. 2000, full text)

- [PMID:10931870 "Here, we demonstrate that the unc-26 gene encodes the Caenorhabditis elegans ortholog of synaptojanin."]
- [PMID:10931870 "Specifically, we observed defects in the budding of synaptic vesicles from the plasma membrane, in the uncoating of vesicles after fission, in the recovery of vesicles from endosomes, and in the tethering of vesicles to the cytoskeleton."]
- [PMID:10931870 "unc-26(s1710) animals contained an almost tenfold increase in the number of coated vesicles over the wild-type (Fig."]
- [PMID:10931870 "The accumulation of coated vesicles in diverse tissues indicated that, in the absence of synaptojanin, the uncoating process is blocked or delayed for synaptic vesicle endocytosis, as well as for other trafficking events."]
- [PMID:10931870 "Behavioral and pharmacological analyses indicate that unc-26 mutants possess a presynaptic disruption of cholinergic and GABA neurotransmission."]
- Golgi and non-neuronal coated vesicles
  [PMID:10931870 "The presence of coated vesicles at both the Golgi complex and the synapse in unc-26 mutants suggest similarities between uncoating mechanisms acting on AP1 and AP2 clathrin complexes."]
  [PMID:10931870 "We observed defects indicating that synaptojanin functions in general trafficking events in all tissues: coated vesicles accumulated in muscles, neurons, and the hypodermis."]
- Growth: [PMID:10931870 "By contrast, unc-26 mutants were relatively healthy with respect to body shape, brood size, and growth rate."]

## Domain function in vivo (Dong et al. 2015, full text)

- [PMID:25918845 "Surprisingly, we find that truncated synaptojanin lacking the PRD domain sustains normal synaptic transmission, indicating that synaptojanin's core function in vivo resides in the remaining two domains that contain phosphoinositide-phosphatase activities: an N-terminal Sac1 phosphatase domain and a 5-phosphatase domain."]
- [PMID:25918845 "The stimulus-evoked EPSC amplitudes were significantly reduced in worms carrying UNC-26∆PRD (D716A) mutant proteins."]
- [PMID:25918845 "We further show that the Sac1 domain plays an unexpected role in targeting synaptojanin to synapses."]
- [PMID:25918845 "In agreement with this notion, tethering synaptojanin 5-phosphatase to endophilin bypasses the requirement of the Sac1 domain and revives synaptojanin activity, suggesting that synaptojanin 5-phosphatase functions at sites where endophilin resides."]

## Relationship to endophilin and to ultrafast endocytosis

- [PMID:14622579 "Finally, endophilin is required to stabilize expression of synaptojanin at the synapse."]
- [PMID:21029864 "Expressing mutant UNC-57 proteins lacking the SH3 domain rescued the unc-57 endocytic defects but failed to rescue the UNC-26 Synaptojanin localization defects."]
- [PMID:29962934 "Endophilin A and synaptojanin were not absolutely required for the ultrafast/bulk endocytosis step at the PM, because in unc-26 (encoding synaptojanin) and unc-57 mutants, LVs/endosomes were still formed after optogenetic stimulation."]
- [PMID:29962934 "At the same time, the breakdown of these LVs into new SVs was strongly attenuated in both unc-26 and unc-57 mutants, arguing that the two proteins act at the step of SV formation from the endosome."]
- PUFA dependence of synaptic UNC-26
  [PMID:18094048 "The levels of GFP::UNC-26 fluorescence detected in the dorsal nerve cord were drastically reduced in fat-3(wa22) mutants in comparison to WT animals (26."]
- PIP2 homeostasis / ttx-7 suppression
  [PMID:22446320 "The unc-26 mutation substantially suppressed the localization defects of synaptic proteins in ttx-7 mutants (Figure 4 and Table1)."]

## Review decisions (37 rows)

- ACCEPT 20; KEEP_AS_NON_CORE 8 (protein localization to synapse IGI,
  PI(3,5)P2 5-phosphatase ISS, positive regulation of neurotransmitter
  secretion, cytoskeleton organization, locomotion x3, Golgi vesicle
  uncoating); MARK_AS_OVER_ANNOTATED 7 (IP3 5-phosphatase IBA, muscle
  contraction and its positive regulation, GABA transport, acetylcholine
  transport, positive regulation of growth, synaptic vesicle transport);
  MODIFY 1 (necroptotic process -> programmed necrotic cell death); REMOVE 1
  (IEA PI3P biosynthetic process chained from an ISS minor activity).
- Deep research (falcon) succeeded; it agrees that the 5-phosphatase reaction
  on PI(4,5)P2 is the essential activity and that Sac1 catalysis is largely
  dispensable.
