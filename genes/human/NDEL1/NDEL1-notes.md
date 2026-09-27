# NDEL1 review notes

Journal for the NDEL1 (Q9GZM8, NudE-like 1, formerly NUDEL) GO annotation review.

## Sources used
- UniProt Q9GZM8 (`NDEL1-uniprot.txt`).
- Cached publications (GOA-cited plus additional papers cached for this review after PubMed eutils
  verification: PMID:12556484, PMID:14970193, PMID:16291865, PMID:16203747, PMID:20403325,
  PMID:37730751, PMID:37086789).
- Deep research (`NDEL1-deep-research-falcon.md`) was not present when the review was written;
  see the end of this file for the final check.

## Biology summary (with provenance)
- Coiled-coil NudE-family protein; the N-terminal coiled coil forms a parallel homodimer that binds LIS1
  [PMID:17997972 "our structures reveal how the Ndel1 coiled coil forms a stable parallel homodimer"].
  The C-terminal region binds dynein and DISC1 [PMID:22843697 "The C-terminal domain of each protein,
  required for interaction with key protein partners dynein and DISC1"].
- Core mechanism: tethers LIS1 to cytoplasmic dynein and regulates dynein. Rat/mouse cortical RNAi:
  [PMID:15473966 "positively regulates dynein activity by facilitating the interaction between LIS1 and dynein"].
  Single-molecule: [PMID:20403325 "We find that NudE stably recruits LIS1 to the dynein holoenzyme molecule"].
  Dynein IC N-terminus binds Ndel1, which recruits LIS1 [PMID:37730751 "the latter of which recruits LIS1 to drive complex assembly"].
  With purified human proteins Ndel1 can also inhibit dynein-dynactin-adaptor assembly
  [PMID:37086789 "we observed that Ndel1 inhibits dynein activation in two distinct ways"]. So "cytoskeletal
  motor regulator activity" (GO:0140659) captures the activity better than any activator/inhibitor term.
- Neuronal migration / nucleokinesis (mouse): [PMID:20007476 "Complete loss of Lis1 or Ndel1 resulted in the
  total inhibition of nuclear movement in cortical slice assays"]; [PMID:15473966 "causes the uncoupling of the
  centrosome and nucleus"].
- CDK5/p35 substrate [PMID:11163260 "NUDEL is a substrate of Cdk5"]; phospho-NDEL1 recruits katanin p60
  [PMID:16203747 "phosphorylation of NDEL1 by Cdk5 facilitates interaction between NDEL1 and p60"]; Cdk5
  phosphorylation switches Lis1/Ndel1/dynein axonal transport [PMID:22114287].
- Centrosome: mother-centriole protein, needed for centrosomal MT nucleation/anchoring (human HeLa/Cos7)
  [PMID:16291865 "Silencing Nudel also represses centrosomal MT nucleation and anchoring."].
- Mitosis: kinetochore via CENP-F; Ndel1-depleted cells have lagging chromosomes [PMID:17600710]; spindle
  localization and M-phase phosphorylation [PMID:12556484]. UniProt notes NDEL1 is dispensable for mitosis in
  cortical progenitors (NDE1 dominant), so mitotic roles treated as non-core.
- Membrane traffic: dynein-driven lysosome minus-end motility and Golgi integrity [PMID:14970193].
- Peripheral: Dyn2 GTPase enhancement [PMID:21283621]; paxillin/nascent adhesions [PMID:19492042];
  DISC1-NDEL1 neurite outgrowth [PMID:17035248].

## Decisions
- 118 GO:0005515 protein binding rows: REMOVE as uninformative (per project policy). The informative
  functions (dynein regulation via LIS1 recruitment) are captured by NEW GO:0140659 and core_functions.
- Kinesin complex (IBA): REMOVE -- NDEL1 is kinesin-1 cargo (via DISC1/14-3-3), not a kinesin subunit.
- Insulin receptor signaling (IEA) and synaptic vesicle (IEA): MARK_AS_OVER_ANNOTATED.
- Identical protein binding from structural papers: MODIFY to protein homodimerization activity.
- NEW: GO:0140659 cytoskeletal motor regulator activity (human proteins in vitro, PMID:37086789);
  GO:0030473 nuclear migration along microtubule (comparator: LIS1/PAFAH1B1 carries GO:0007097; NDEL1
  contributes regulator activity to the dynein step, so passes the participation test).
