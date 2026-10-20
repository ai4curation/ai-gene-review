# dyn-1 (dynamin) curation notes

UniProt P39055 (DYN1_CAEEL, Swiss-Prot). The single classical dynamin of
C. elegans. Module role: dynamin fission tier of
modules/synaptic_vesicle_endocytosis.yaml (GTPase activity GO:0003924;
GO:0016185 synaptic vesicle budding).

## Synaptic / endocytic core (fission GTPase)

- Founding ts mutant, shibire-like
  [PMID:9294229 "We isolated a recessive temperature-sensitive dyn-1 mutant containing an alteration within the GTPase domain that becomes uncoordinated when shifted to high temperature and that recovers when returned to lower temperatures, similar to D. shibire mutants."]
  [PMID:9294229 "Using a dyn-1::lacZ gene fusion, a high level of dynamin expression was observed in motor neurons, intestine, and pharyngeal muscle."].
- Synaptic and apical localization
  [PMID:9802908 "Indirect immunofluorescence showed that dynamin is concentrated along the dorsal and ventral nerve cords and in the synapse-rich nerve ring."]
  [PMID:9802908 "Furthermore, this chimera was detected along the apical membrane of intestinal cells, in spermathecae, and in coelomocytes."].
- Receptor-mediated yolk endocytosis
  [PMID:10588660 "dyn-1 (RNAi) animals and dyn-1(ky51ts) mutants, at the nonpermissive temperature of 25°C, showed high-level accumulation of YP170::GFP in the pseudocoelomic space and strongly reduced accumulation of YP170::GFP within oocytes and embryos."].
- Genetic interaction with ehs-1/Eps15 in SV recycling
  [PMID:11483962 "Impairment of EHS-1 function in dyn-1(ky51) worms, which express a mutant form of dynamin and display a temperature-sensitive locomotion defect, resulted in a worsening of the dyn-1 phenotype and uncoordination at the permissive temperature."].
- GTPase biochemistry
  [PMID:20016007 "In our GTP hydrolysis assay, with the addition of negatively charged lipids, a drastic increase of the GTPase activity of wild-type DYN-1 was detected, at the same rate and level as detected from rat dynamin (Figure 3B)."]
  [PMID:20016007 "As expected for mutant DYN-1 molecules that are severely defective for GTP binding, DYN-1(G40E) and DYN-1(K46A) displayed greatly reduced GTP hydrolysis activities in comparison with wild-type DYN-1 (Figure 3C)."].
- Periciliary membrane compartment
  [PMID:22342749 "RESULTS: Here we show that localization of the clathrin light chain, AP-2 clathrin adaptor, dynamin, and RAB-5 endocytic proteins overlaps with a morphologically discrete periciliary membrane compartment associated with sensory cilia."].

## Apoptotic cell clearance / phagosome maturation (second core function)

- [PMID:16740477 "We identified 14 loss-of-function alleles of the C. elegans dynamin gene, dyn-1, that are defective in the removal of apoptotic cells."]
- [PMID:16740477 "DYN-1 transiently accumulates to the surface of pseudopods in a manner dependent on ced-1, ced-6, and ced-7, but not on ced-5, ced-10, or ced-12."]
- [PMID:18425118 "DYN-1 is required for efficient recruitment of RAB-5 and RAB-7 to phagosomes containing engulfed apoptotic cells in the C."]
- [PMID:18425118 "However, our studies suggested no obvious defect in corpse internalization per se but instead that DYN-1 may act during phagosome maturation."]
- [PMID:21494661 "DYN-1 is recruited to nascent phagosomes and subsequently recruits VPS-34."]
- SH3 partner LST-4/SNX9
  [PMID:21148288 "In addition, LST-4 interacts with DYN-1 (Dynamin) and stabilizes its association with phagosome, which recruits and stabilizes the association of RAB-7 with phagosomes."].

## SH3 interactome

- [PMID:23549480 "Both domains are predicted to bind to the proline-rich motif PRGGPGAPPPPGMRP (residues 783–797) of dynamin (DYN-1) (Supplementary Figure 7B)."]
- [PMID:23549480 "More generally, of the 34 worm SH3-mediated PPIs involving two endocytosis proteins, only two consist of proteins with both yeast orthologs involved in endocytosis: ITSN-1 (Ede1p in yeast) and SDPN-1 (Bzz1p in yeast) interacting with DYN-1 (Vps1p in yeast—interactions are not known to take place in yeast)."]

## Cytokinesis (non-core)

- [PMID:12498685 "In Caenorhabditis elegans, dynamin localized to newly formed cleavage furrow membranes and accumulated at the midbody of dividing embryos in a manner similar to dynamin localization in mammalian cells."]

## Review decisions (47 rows)

- ACCEPT 27; KEEP_AS_NON_CORE 4 (embryo development, locomotion, midbody,
  cleavage furrow); MODIFY 8 (necroptotic process -> programmed necrotic cell
  death; programmed cell death IEA -> apoptotic cell clearance; 6 protein
  binding rows from the SH3 interactome / LST-4 co-IP -> SH3 domain binding);
  REMOVE 3 (generic protein binding from interactome Y2H screens with
  B0303.7, WWP-1, GEI-18); MARK_AS_OVER_ANNOTATED 3 (microtubule IBA,
  microtubule binding IBA, cytoskeleton IEA: legacy in vitro microtubule
  association of mammalian dynamin); UNDECIDED 2 (presynaptic active zone
  from the abstract-only cilia paper; spindle microtubule from the
  abstract-only cytokinesis paper whose spindle-midzone statement concerns
  mammalian cells).
- No NEW rows: GO:0016185 already carries the synaptic budding role by IBA.

## Deep research (falcon) addendum

- Succeeded. Agrees with the review: [file:worm/dyn-1/dyn-1-deep-research-falcon.md "Direct worm evidence is especially strong for intestinal clathrin-coated-pit scission, recycling-endosome tubule fission, and CED-1/CED-6-linked phagosome maturation."]
  and notes that [file:worm/dyn-1/dyn-1-deep-research-falcon.md "The synaptic ultrafast-endocytosis measurements retrieved here were physiological but not DYN-1-specific."].
- It also cites newer work (2019-2024: EHBP-1/SID-3/DYN-1 axis, injury-induced
  axonal fusion, dendrite branching) not represented in GOA; not reviewed here.
