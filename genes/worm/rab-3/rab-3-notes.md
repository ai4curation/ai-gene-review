# rab-3 (C. elegans Rab3, UniProt Q94986) - curation notes

## Identity
- Reviewed Swiss-Prot entry RAB3_CAEEL, Q94986, 219 aa, ORF C18A3.6. Single worm Rab3 ortholog
  (vertebrates have RAB3A/B/C/D). Small GTPase superfamily, Rab family; C-terminal CxC
  geranylgeranylation motif for membrane attachment [file:worm/rab-3/rab-3-uniprot.txt].

## Core biology: synaptic-vesicle GTPase that recruits vesicles to the presynaptic density
- rab-3 mutants are viable with mild behavioural defects but impaired synaptic transmission:
  pharyngeal electrophysiology is impaired, animals are aldicarb-resistant (depressed
  cholinergic transmission), and synaptic vesicles are redistributed away from synapses
  [PMID:9334382 "In motor neurons, vesicle populations at synapses were depleted to 40%"; "we postulate that RAB-3 may regulate recruitment of"].
- RAB-3 is a monomeric G-protein that associates with synaptic vesicles in its GTP-bound state
  [PMID:18721860 "Rab3 is a monomeric G-protein that associates with SVs in its GTP-bound state and dissociates upon GTP hydrolysis"].
- Effector interaction: GTP-bound but not GDP-bound RAB-3 binds the zinc-finger domain of the
  active-zone protein UNC-10/RIM, selectively among worm Rabs
  [PMID:18721860 "C. elegans and vertebrate Rim both interacted with the activated C. elegans GTP-bound RAB-3(Q81L) mutant, but not the GDP-bound RAB-3(T36N) mutant"; "the C. elegans Rim-RAB-3 interaction was selective for RAB-3 as Rim failed to interact with wild-type or GTP-bound mutant forms of C. elegans RAB-1, -5, -8, -11, -27 and -37"].
- High-pressure-freeze EM: rab-3 mutants have normal vesicle numbers but a specific loss of
  vesicles contacting the membrane adjacent to the presynaptic density, phenocopying unc-10, and
  unc-10;rab-3 doubles are no worse - RAB-3 and UNC-10 act in one pathway to target vesicles to
  the presynaptic density [PMID:18721860 "there was a specific reduction in SVs contacting the plasma membrane near the presynaptic density, relative to the wild type"].
- Release in rab-3 mutants is reduced (evoked ~55%, mini frequency ~65% of WT) and shows reduced
  Ca2+ sensitivity, consistent with vesicles being positioned near UNC-2 Ca2+ channels by the
  RAB-3/UNC-10 interaction [PMID:18721860 "the evoked defects of unc-10 and rab-3 and single and double mutants where exacerbated when calcium was lowered from 5mM to 1mM"].
- Localization: RAB-3 (GFP) marks presynaptic puncta in motor-neuron axons
  [PMID:23527112 "Fluorescently-tagged RAB-3, SYD-2 and SNB-1 co-localize at punctate structures that correspond to presynaptic sites"].
- The GEF AEX-3 activates RAB-3; in aex-3 mutants RAB-3 is mislocalized to cell bodies
  [PMID:27116976 "in aex-3 mutant animals, RAB-3 as well as AEX-6 /Rab27 are mislocalized to the cell body"].

## Non-core / developmental role
- AVG pioneer axon navigation: rab-3 (but not aex-6/Rab27) enhances the AVG axon cross-over
  defect of nid-1 mutants; AEX-3 -> RAB-3 acts with exocytosis genes (unc-64, unc-31, ida-1) and
  the netrin receptor UNC-5, probably by delivering vesicles/UNC-5 to the growth cone
  [PMID:27116976 "We found that rab-3 but not aex-6 /Rab27 mutant animals have AVG axon cross-over defects in a nid-1 mutant background"].
  This is a developmental trafficking role, not the synaptic release function.

## GO decisions (summary)
- Core: G protein activity (GO:0003925) on the synaptic vesicle membrane, directly involved in
  synaptic vesicle exocytosis (vesicle recruitment/docking at the active zone via UNC-10).
  The GOA "exocytosis" IBA and GTPase-activity rows are accepted; the "protein binding" IPI
  (UNC-10) is better expressed as G protein activity (GTP-state-dependent effector binding).
- Obsolete GO:0016081 "synaptic vesicle docking" is not in the GOA rows for rab-3; the
  ontology now points to GO:0160321 vesicle docking activity / GO:7770062 vesicle membrane
  tethering activity, which are molecular functions of the tether (UNC-10/RIM) rather than of
  the vesicle GTPase.
- Behavioural terms (chemotaxis, mating behaviour, locomotion, pharyngeal pumping) and
  GABAergic-transmission regulation are downstream phenotypes of the release defect; kept as
  non-core or flagged as over-annotation. PMID:9334382 and PMID:19797046 are abstract-only in
  the cache.
- Endosome (IBA, broad Rab node) is not supported for worm RAB-3.
