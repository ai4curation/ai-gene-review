# Syt1 (rat, UniProt P21707) - manual literature synthesis

No deep-research API was available for this review; this synthesis was written by hand
from the cached publications in `publications/`, the UniProt record
(`Syt1-uniprot.txt`) and PubMed searches. Every assertion carries its source.

## Identity and architecture

- Synaptotagmin-1 (p65), 421 aa, single-pass membrane protein of synaptic vesicles:
  short intravesicular N-terminus (1-57), one TM helix (58-79), a ~60-residue
  juxtamembrane linker, and tandem C2 domains (C2A 141-260, C2B 272-405)
  [Syt1-uniprot.txt FT TOPO_DOM/TRANSMEM/DOMAIN].
- First identified as a 65-kDa protein "exposed on the outer surface of brain synaptic
  vesicles" with wide distribution in neuronal and neurosecretory tissue
  [PMID:7298720].
- Its cytoplasmic domain carries an internally repeated sequence "homologous to the
  regulatory C2-region of protein kinase C" and "binds acidic phospholipids"
  [PMID:2333096].

## Ca2+ binding and Ca2+-dependent phospholipid binding

- Synaptotagmin "binds calcium at physiological concentrations in a complex with
  negatively charged phospholipids" and "acts as a cooperative calcium receptor in
  exocytosis" [PMID:1589771].
- A single C2A domain "by itself binds Ca2+ and phospholipids with high affinity
  (half-maximal binding at 4-6 microM free Ca2+) and exhibits strong positive
  cooperativity" [PMID:8253763].
- C2B crystal structures show conserved aspartates (D303, D309, D363, D365)
  coordinating two (and at high Ca2+ three) Ca2+ ions [PMID:15340165].
- C2A activates a Ca2+-triggered membrane-penetration activity of C2B; both Ca2+-binding
  loops dip into bilayers [PMID:11805296].
- PIP2 binds the C2B polybasic patch (Kd ~20 uM) and lowers the apparent Kd for Ca2+
  from ~250 to <5 uM [PMID:22447935].
- Syt1 C2 domains demix phosphatidylserine laterally in bilayers [PMID:21610074]; an
  excess of PS on the target-membrane side is required for the Ca2+-dependent
  stimulation of fusion [PMID:22229667]. Neither paper reports transbilayer lipid
  movement.

## SNARE binding

- Ca2+ promotes binding of Syt1 to t-SNAREs (syntaxin-1A/SNAP-25) and PS; this
  correlates with the ability of syt isoforms to stimulate fusion [PMID:18508778;
  PMID:20688915].
- Syntaxin interactions of the C2 domains [PMID:7791877; PMID:10397765; PMID:9570782];
  Ca2+ "induces binding of the synaptotagmin C(2) domains to SNARE proteins"
  [PMID:12526776].
- Atomic structures of Syt1-SNARE complexes reveal a large Ca2+-independent primary
  interface essential for evoked release [PMID:26280336]; smFRET model of the
  Syt1-SNARE complex [PMID:20173763]; C2B binds SNAREs and membranes simultaneously
  [PMID:27083046].
- Complexin (synaphin) directly binds Syt1 [PMID:19132534].

## Ca2+ sensor for fast synchronous release

- In Syt1 knockout mice "the fast component of both Ca(2+)- and Sr(2+)-induced release
  is selectively impaired" [PMID:12526776].
- Syt1 and Syt7 trigger fast and slow phases respectively and redundantly maintain the
  readily releasable pool [PMID:26437117].
- Polybasic patches in both C2 domains are required for evoked release [PMID:35701163].
- In reconstituted fusion, Syt1 stimulates SNARE-catalysed fusion in response to Ca2+
  while clamping fusion in its absence [PMID:18508778; PMID:20688915]; Syt1 strongly
  stimulates Munc18-1/Munc13-1-dependent fusion with few SNAREs, depending on Ca2+
  binding to both C2 domains [PMID:33468652].
- Purified rat synaptic vesicles fuse with t-SNARE bilayers; "Calcium boosts fusion
  through a combined general electrostatic and synaptotagmin-specific mechanism"
  [PMID:23663838].

## Docking / membrane tethering

- "vesicle docking by synaptotagmin 1 is a prerequisite for Munc18-1 to accelerate
  trans-SNARE complex (SNAREpin) assembly" [PMID:22810233].
- Syt1 "tethers synaptic vesicles to the presynaptic plasma membrane by binding to
  acidic membrane lipids and SNAREs" [PMID:22711810].
- The juxtamembrane linker is essential for "Ca2+-independent vesicle docking and
  Ca2+-dependent fusion pore opening" [PMID:24001110]; the linker mediates
  oligomerization and Ca2+-dependent vesicle capture [PMID:24973220] and drives
  liquid-liquid phase separation that negatively regulates Ca2+ sensitivity
  [PMID:38177243].

## Oligomerization

- Ca2+-triggered C2B-mediated dimerization [PMID:8621455]; hetero-oligomerization with
  Syt3/Syt4 [PMID:9830048; PMID:10397765].

## Endocytosis

- The C2B domain binds AP-2 [PMID:9830048; PMID:7791877]; internalization signal at the
  C-terminus regulated by C2B [PMID:11502761]; stonin 2 is an endocytic sorting adaptor
  for Syt1 [PMID:18166656; PMID:11454741]; juxtamembrane region binds dynamin 1 and
  regulates fission [PMID:25964652]; human SYT1 I368T variant alters exo- and
  endocytosis kinetics [PMID:25705886].

## Neuroendocrine dense-core vesicles

- In PC12 cells Syt1 and Syt9 function redundantly in LDCV Ca2+ sensing and fusion-pore
  dilation [PMID:17686463; PMID:11751925], although siRNA against Syt1 alone had no
  effect in one study [PMID:15015935]. Syt isoforms sort to DCV populations of different
  size [PMID:21551071]. Syt1 knockdown weakens Ca2+-dependent dopamine release from PC12
  cells [PMID:28370453].

## Other locations

- Postsynaptic spines (vesicles and PSD) by immunogold EM [PMID:28686803]; terminal
  boutons [PMID:24876496].

## Microbial

- Receptor for botulinum neurotoxins B and G via its intravesicular segment
  [Syt1-uniprot.txt CC FUNCTION].
