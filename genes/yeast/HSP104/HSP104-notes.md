# HSP104 review notes

## 2026-08-28 annotation audit

- HSP104 is the canonical cytosolic Hsp100/ClpB-family AAA+ disaggregase. Its
  defining activity is ATP-dependent extraction of proteins from aggregates,
  followed by Hsp70/Hsp40-dependent reactivation. The original resolubilization
  study states that Hsp104 “mediates the resolubilization of heat-inactivated
  luciferase from insoluble aggregates” [PMID:7984243, “Protein disaggregation
  mediated by heat-shock protein Hsp104.”]. The reconstitution study further
  reports that, with Hsp40 and Hsp70, Hsp104 reactivates proteins that were
  denatured and allowed to aggregate [PMID:9674429, “Hsp104, Hsp70, and Hsp40:
  a novel chaperone system that rescues previously aggregated proteins.”].
  These data justify a NEW annotation to GO:0140545, ATP-dependent protein
  disaggregase activity.

- All 45 unique non-NEW GOA signatures were reconciled exactly by GO term,
  evidence code, reference, and relation qualifier. The 67 GOA rows collapse to
  45 signatures because the two high-throughput protein-binding publications
  contain multiple WITH/FROM interaction partners. Those repeated partner rows
  do not represent distinct GO assertions in this review.

- The eight IBA rows were checked against the current PTHR11638 PAINT cache.
  Cytoplasm and ATP hydrolysis are asserted at PTN000181243. Protein refolding,
  protein unfolding, cytosol, unfolded protein binding, protein-folding
  chaperone binding, and cellular heat acclimation are asserted at the fungal
  node PTN007521008. S. cerevisiae HSP104 is itself an experimental descendant
  seed for several of these assertions; this is valid PAINT grounding, not
  circular evidence. The inherited biology is supported for HSP104. The
  GO:0051082 IBA correctly propagates substrate-binding biology but the term is
  obsolete. Neither official consider target preserves that assertion without
  adding foldase or carrier/holdase semantics, so it is UNDECIDED rather than
  branch-swapped to the separately established disaggregase activity.

- The PMID:16135516 IDA row is treated separately. The paper directly assays
  nucleotide-regulated binding to permanently unfolded RCMLa, but it does not
  assay folding, aggregation prevention/escort, or disaggregation. Live QuickGO
  records GO:0051082 as obsolete and offers GO:0044183 protein folding chaperone
  and GO:0140309 unfolded protein holdase activity as `consider` targets. Neither
  is evidence-matched to this assay, so the row is UNDECIDED rather than ACCEPT
  on an obsolete term or MODIFY to an activity that this paper did not test. The
  separate NEW GO:0140545 annotation retains direct disaggregation evidence.

- Generic protein-binding annotations from the global TAP and chaperone-network
  studies remain marked over-annotated. The full-text chaperone atlas explicitly
  cautions that its TAP-tag interactions are indirect rather than binary
  [PMID:19536198, “An atlas of chaperone-protein interactions in Saccharomyces
  cerevisiae: implications to protein folding pathways in the cell.”]. Specific
  homo-oligomerization and protein-folding-chaperone binding annotations are
  retained separately.

- Nuclear, nuclear-periphery, stress-granule, ER-folding, and TRC/ER-targeting
  annotations are retained as non-core context. Direct microscopy supports a
  nuclear pool [PMID:10467108, “At normal temperature (25 degrees C), a small
  amount of Hsp104 was located in the cytoplasm and nucleus.”], and stress-granule
  recovery requires Hsp104/Hsp70 activity [PMID:24291094, “Coordination of
  translational control and protein homeostasis during severe heat stress.”].
  These roles are credible consequences or specialized deployments of the core
  disaggregation machinery rather than separate defining activities.

- The trehalose-metabolism phenotype remains marked over-annotated: reduced
  trehalose enzyme activities in an hsp104 mutant establish an indirect
  proteostasis consequence, not a direct metabolic activity [PMID:9797333,
  “The activities of trehalose-synthesizing and -hydrolyzing enzymes are low in
  the HSP104 disruption mutant during heat shock.”]. The ARBA intracellular
  organelle lumen annotation is likewise over-annotated because HSP104 is a
  cytosolic/nuclear protein; an effect on repair within the ER does not establish
  luminal localization.

- Prion fibril fragmentation is a major yeast-specific function described by
  UniProt and the literature, but a current QuickGO ontology search did not find
  a GO term specifically representing prion propagation or fibril fragmentation.
  A term request for “prion fibril fragmentation activity” is therefore captured
  under `proposed_new_terms` without guessing an identifier; PMID:18312264 states
  that Hsp104-dependent fibril fragmentation creates infectious seeds.
