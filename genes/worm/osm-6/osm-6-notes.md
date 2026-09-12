# osm-6 (C. elegans) research notes

> Provenance note: `just deep-research-falcon worm osm-6 --fallback perplexity-lite`
> was attempted twice and both runs timed out with no output (SIGTERM, exit 143/144);
> no `-deep-research-*.md` file was produced and none was fabricated. This review is
> grounded directly in the UniProt record (G5EDF6), the QuickGO GOA export, and the 11
> cached primary publications (all listed below with verbatim provenance). All existing
> annotations could be adjudicated from primary literature, so no UNDECIDED calls were
> required.


UniProt: G5EDF6 (G5EDF6_CAEEL) · WormBase: WBGene00003886 / R31.3 · ORF R31.3 · Chromosome V
Ortholog: **IFT52** (human IFT52 / NGD5; Chlamydomonas IFT52/BLD1). Core structural subunit of the
intraflagellar transport complex B (IFT-B). PANTHER PTHR12969 (NGD5/OSM-6/IFT52), subfamily SF7.
ComplexPortal: CPX-1290 "Intraflagellar transport complex B".

Protein: 472 aa. Domain architecture (InterPro/Pfam): N-terminal IFT52 GIFT domain (PF23355, ~18-257,
a class-I glutamine-amidotransferase-like fold, SSF52317), IFT52 central domain (PF23352, ~274-357),
and IFT52 C-terminal domain (PF21178, ~368-417, CDD cd23683 IFT52_CTD). No catalytic residues / no EC;
the GATase-like fold is used structurally, not enzymatically (consistent with a scaffold subunit).

## Summary: what osm-6/IFT52 IS (KNOWN)

- **Structural subunit of the IFT-B complex.** In *Chlamydomonas*, the 16S IFT "raft" (IFT particle)
  contains ≥16 polypeptides, two of which are homologues of the *C. elegans* OSM-1 and OSM-6 proteins
  required for sensory ciliary function [PMID:10545497 "the basic subunit of IFT rafts is a 16S
  multiprotein complex containing at least 16 polypeptides, two of which share sequence homology with
  the OSM-1 and OSM-6 proteins that are required for sensory ciliary function in C. elegans"].
  OSM-6 is explicitly "the ortholog of human IFT52" and is used as the canonical GFP-tagged **IFT-B
  component** reporter [PMID:22922713 "the GFP-tagged IFT-B component OSM-6 (the ortholog of human
  IFT52)"].

- **Cargo of the IFT motors / moves by IFT.** OSM-6::GFP moves anterogradely (kinesin-II driven) and
  retrogradely along cilia. Kinesin-II and its cargo OSM-1 and OSM-6 all move at ~1.1 µm/s in the
  retrograde direction along cilia and dendrites [PMID:10545497 "OSM-1 and OSM-6, all move at
  approximately 1.1 microm/s in the retrograde direction along cilia and dendrites"]. Retrograde
  movement in cilia (but not dendrites) requires the CHE-3 (DHC1b/dynein-2) motor [PMID:10545497
  "the class DHC1b cytoplasmic dynein, CHE-3, is specifically responsible for the retrograde transport
  of the anterograde motor, kinesin-II, and its cargo within sensory cilia"]. Ciliary entry of dynein-2
  itself depends on an intact IFT-B complex [PMID:28479320 "Disruption of the dynein-2 tail domain,
  light intermediate chain, or intraflagellar transport (IFT)-B complex abolishes dynein-2's ciliary
  localization"].

- **Required for cilium (axoneme) assembly.** osm-6 mutants have normal transition zones but severely
  shortened axonemes with ectopic doublet microtubules assembling proximal to the cilium
  [PMID:2428682 "The cilia in che-13 (e1805), osm-1 (p808), osm-5 (p813), and osm-6 (p811) mutants have
  normal transition zones and severely shortened axonemes. Doublet-microtubules, attached to the
  membrane by Y links, assemble ectopically proximal to the cilia in these mutants"]. Cloning +
  transformation rescue + genetic mosaics show osm-6 acts **cell-autonomously** in ciliated sensory
  neurons [PMID:9475731 "we conclude from an analysis of genetic mosaics that osm-6 acts cell
  autonomously in affecting cilium structure"].

- **Localization.** OSM-6::GFP is expressed exclusively in ciliated sensory neurons; the fusion rescues
  the mutant and accumulates in cytoplasm including processes and dendritic endings where cilia sit
  [PMID:9475731 "The OSM-6::GFP protein was localized to cytoplasm, including processes and dendritic
  endings where sensory cilia are situated"]. Expression is controlled by the RFX transcription factor
  DAF-19: "in the case of daf-19, reduced OSM-6::GFP accumulation" [PMID:9475731]. Experimentally
  localized to: non-motile (sensory) cilium and transition zone [PMID:10545497], ciliary basal body
  [PMID:22922713], and neuronal cell body [PMID:9475731]. Used as a ciliary IFT marker in RAB-28 work
  [PMID:27930654].

## What osm-6 loss CAUSES downstream (KNOWN but not the core molecular role)

All of these are *sensory consequences of losing functional cilia*, not distinct molecular activities
of OSM-6:
- **Osmotic avoidance defect** — the gene is named for this ("OSMotic avoidance abnormal"); osm-6 was
  isolated among the osmotic-avoidance-defective mutants [PMID:730048 osmotic avoidance defective
  screen]. (Abstract-only; osm-6 not named in the cached abstract but this is the founding Osm screen
  and the IMP is a WormBase curator annotation.)
- **Chemotaxis / chemosensation defect** and dye-filling defect [PMID:2428682].
- **Mechanosensation defect** — nose-touch response requires intact ciliated sensory endings
  [PMID:8460126 "Mutant animals that have defective ciliated sensory endings ... fail to respond to
  touch to the nose"] (osm-6 mutants are among such ciliary-defective animals; WB IMP).
- **Dauer formation** — osm-6 is one of the cilium-structure genes acting at a single step in the
  chemosensory dauer pathway [PMID:1732156 "Dauer-defective mutations in nine genes cause structurally
  defective chemosensory cilia, thereby blocking chemosensation"]; IGI with a daf gene.
- **Salt-sensing circuit** — hypomorphic osm-6 mutants lack functional sensory cilia and therefore
  have greatly reduced ASEL/AWC salt responses; cell-autonomous cilium rescue restores sensing
  [PMID:24013594 "We analyzed hypomorphic osm-6 mutants that lack functional sensory cilia (dendritic
  endings) and found them to have greatly reduced ASEL salt responses and AWCON salt and odor
  responses"]. The GO:1902075 "cellular response to salt" IMP here reflects this indirect ciliary
  requirement, not a salt-signalling activity of OSM-6.

## What is NOT known (knowledge gaps)

- **No sub-molecular mechanism / no direct-partner map in C. elegans.** OSM-6/IFT52 is treated as a
  structural IFT-B subunit, but which IFT-B partners it contacts in the worm (in mammals IFT52 bridges
  IFT88/IFT70/IFT46 and links the IFT-B core to peripheral subunits) and how its GIFT/central/CTD
  domains are used has not been experimentally dissected in *C. elegans*. GO MF for such a subunit can
  only be expressed as generic "structural molecule activity" (an ontology-shadow gap).
- **No independent biochemical/enzymatic activity** is known or expected (GATase-like fold appears
  non-catalytic).

## Curation plan (actions)

Core (IFT-B structural subunit): intraciliary transport particle B (part_of), intraciliary transport,
cilium/non-motile cilium assembly, cilium/non-motile cilium localization, ciliary basal body,
transition zone — ACCEPT. centriole (IBA), cytoplasm, neuronal cell body — KEEP_AS_NON_CORE (real
but broad / not the functional site). Downstream sensory-phenotype BPs (chemotaxis, response to
osmotic stress, sensory perception of mechanical stimulus, cellular response to salt) —
KEEP_AS_NON_CORE (pleiotropic consequences of ciliary loss). GO:0003674 ND root MF — accept as
placeholder (superseded in spirit by proposed structural MF). Propose MF: structural molecule
activity (GO:0005198).
