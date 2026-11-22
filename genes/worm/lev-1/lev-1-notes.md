# lev-1 review notes

## Session 1

- `just fetch-gene worm lev-1` resolved UniProtKB:Q27218 (ACH7_CAEEL), seeded 33 GOA rows, and reused the local PTHR18945 family data.
- `just mod-description-deep-research worm lev-1` fetched the WormBase hand-written description. Falcon and Perplexity Lite were unavailable locally, so this review was curated from cached UniProt, WormBase, PTHR18945, the levamisole-sensitive nAChR module, the existing `unc-29` review, and cached publications.
- Cached GOA PMIDs for this seed: PMID:11290716, PMID:15280391, PMID:15990870, and PMID:16466809. I also reused cached PMID:9221782 for the original lev-1/unc-29/unc-38 cloning and PMID:19020092 for the eight-factor L-AChR reconstitution.

### Core picture

LEV-1 is a non-alpha Cys-loop nAChR subunit of the levamisole-sensitive acetylcholine receptor. In native C. elegans extracts, LEV-1 copurifies with UNC-29, UNC-38, UNC-63, and LEV-8 [PMID:15990870 "Multiple peptides of each of the levamisole receptor subunits, UNC-29, UNC-38, UNC-63, LEV-8, and LEV-1, were identified in four different purifications"]. In Xenopus oocytes the five pore subunits plus RIC-3, UNC-50, and UNC-74 reconstitute the receptor, and omitting any pore subunit nearly eliminates function [PMID:19020092 "functional receptors were virtually eliminated when 1 or more of the 5 receptor subunits were omitted"]. Fleming et al. originally inferred from mutant phenotypes that UNC-38 and UNC-29, but not LEV-1, were necessary for nAChR function; I treat that as a useful caveat about milder lev-1 in vivo phenotypes that is superseded for robust five-subunit L-AChR function by the later reconstitution work.

LEV-1 is part of the body-wall muscle levamisole-sensitive receptor at neuromuscular junctions. Culetto et al. reported LEV-1 body-wall muscle expression and body-wall muscle electrophysiology showing that the levamisole-sensitive nAChR at the C. elegans NMJ requires LEV-1 [PMID:15280391 "requires both UNC-63 and LEV-1 subunits"]. The review therefore adds a conservative `NEW` neuromuscular synaptic transmission row.

### Decisions worth flagging

- The row pattern mirrors `unc-29`: generic InterPro2GO receptor/channel rows were refined to `GO:0022848`, generic transport rows to `GO:0098655`, broad membrane to `GO:0045211` plus `GO:0005886`, and broad membrane-potential regulation to `GO:0060079`.
- `GO:0006816` calcium ion transport is kept as non-core. Boulin et al. measured calcium permeability of the recombinant L-AChR, but Ca2+ flux is secondary to the receptor's main depolarizing cation-channel role.
- WB:WBVar00143038 remains an allele-level check because Fleming et al. described dominant lev-1 TM2 resistance alleles; if the WormBase IMP rows use one of those alleles, they are poison-subunit evidence rather than simple loss-of-function evidence.
- Neuron-projection and neuronal-cell-body locations are kept as non-core. The cached PMID:16466809 record is abstract-only but supports in vivo surface labeling of L-AChR subunits on neuron surfaces, and WormBase records LEV-1::GFP in body-wall muscle plus a subset of ventral-cord motor neurons.
- Egg-laying rows are kept as non-core. PMID:11290716 names lev-1 as essential for levamisole-stimulated egg laying, but egg laying is a secondary context of the same L-AChR channel function.
