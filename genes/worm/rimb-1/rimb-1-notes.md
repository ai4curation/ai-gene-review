# rimb-1 (C. elegans RIM-binding protein, UniProt Q9N415) - curation notes

## Identity
- TrEMBL Q9N415_CAEEL, 1276 aa, ORF Y39A3CL.2, formerly tag-168; annotated as "Variant SH3 domain
  protein" belonging to the RIMBP family [file:worm/rimb-1/rimb-1-uniprot.txt]. Sole worm RIM-BP
  (vertebrates: RIMBP1/2/3). Two splice isoforms, with three SH3 and two FN3 domains
  [file:worm/rimb-1/rimb-1-deep-research-falcon.md "Both possess one N-terminal SH3 domain, two fibronectin type III-like domains, and two tandem C-terminal SH3 domains"].
- Caution when searching the literature: the historical tag-168 promoter is a widely used
  pan-neuronal driver, so many papers citing it say nothing about RIMB-1 function
  [file:worm/rimb-1/rimb-1-deep-research-falcon.md "the historical *tag-168* promoter is widely used as a pan-neuronal expression driver"].

## Core biology: redundant active-zone scaffold that positions the UNC-2/CaV2 channel
- RIMB-1 is an intracellular component of the presynaptic active zone: endogenously tagged RIMB-1
  forms puncta along motor-neuron neurites and colocalizes with UNC-10/RIM and with UNC-2/CaV2
  [file:worm/rimb-1/rimb-1-deep-research-falcon.md "Endogenous mScarlet-tagged RIMB-1 and GFP-tagged UNC-2 colocalized at all examined synaptic puncta in the dorsal nerve cord."].
- Its best-supported function is to help retain and position UNC-2 near release-ready vesicles,
  redundantly with UNC-10/RIM: rimb-1 single mutants have near-normal UNC-2 puncta, whereas
  rimb-1;unc-10 doubles lose presynaptic UNC-2 profoundly
  [file:worm/rimb-1/rimb-1-deep-research-falcon.md "Either single mutant retained relatively normal UNC-2 clusters in several assays, but the double mutant showed a profound loss of presynaptic UNC-2."].
- RIMB-1 puncta depend on CLA-1/Clarinet and partly on SYD-2/liprin-alpha, and UNC-2 itself refines
  RIMB-1's distribution
  [file:worm/rimb-1/rimb-1-deep-research-falcon.md "Complete loss of CLA-1 drastically reduced both the intensity and number of RIMB-1 puncta"].
- Consistent with this, the human ortholog review (genes/human/RIMBP2) assigns RIMBP2 the core
  molecular function GO:0098882 structural constituent of presynaptic active zone.

## The single existing GOA annotation
- The only GOA row is GO:0005515 protein binding (IPI, PMID:23549480) with interactor
  UniProtKB:Q17865 (C09G1.4), from a genome-scale SH3-domain interactome built by peptide phage
  display and stringent yeast two-hybrid
  [PMID:23549480 "We then mapped the worm SH3 interactome using stringent yeast two-hybrid"].
  The screen is enriched for endocytic proteins and makes no functional claim about RIMB-1
  [PMID:23549480 "it is significantly enriched for proteins with roles in endocytosis"]. Generic
  protein binding is uninformative, so the row is removed; nothing in the paper supports a more
  specific molecular function for RIMB-1.

## GO decisions (summary)
- Existing: the sole protein-binding IPI is removed as uninformative.
- Core function asserted from the family/ortholog evidence and the worm active-zone literature
  summarized in the deep-research report: structural constituent of the presynaptic active zone.
- No NEW process annotations are proposed: the worm evidence is redundancy-revealed
  (rimb-1;unc-10 doubles) and the primary sources are not cached here, so the channel-anchoring
  process claim is left for a future review with the primary papers in hand.
