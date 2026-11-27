# unc-32 (P30628) — V-type proton ATPase 116 kDa subunit a 1 — curation notes

## Identity

- UniProt P30628 (VPP1_CAEEL, reviewed), WormBase ZK637.8, 905 aa, nine putative TM
  segments; V-ATPase 116 kDa subunit a family (IPR002490, IPR026028). One of four C. elegans
  subunit a genes (vha-5, vha-6, vha-7, unc-32); unc-32 is the neuronal isoform and the
  orthologue of human ATP6V0A1 (the clathrin-coated-vesicle / synaptic-vesicle a1 isoform).
- Subunit a forms the two proton half-channels of the V0 sector and its N-terminal domain
  docks the V1 sector; unc-32 encodes six splice isoforms.

## Literature

### Pujol et al. 2001 (PMID:11110798, abstract only)

- "unc-32 corresponds to one of the four genes encoding a V-ATPase a subunit in the
  nematode" [PMID:11110798]; "unc-32 gives rise via alternative splicing to at least six
  transcripts" [PMID:11110798].
- Alleles: "We have isolated four new mutant alleles, the strongest of which is embryonic
  lethal" [PMID:11110798]. "In the uncoordinated alleles, the transcript unc-32 B is
  affected, suggesting that it encodes an isoform that is targeted to synaptic vesicles of
  cholinergic neurons, where it would control neurotransmitter uptake or release"
  [PMID:11110798]. "Other isoforms expressed widely during embryogenesis are mutated in the
  lethal alleles and would be involved in other acidic organelles" [PMID:11110798].
- NAS rows to "proton motive force-driven ATP synthesis" and "negative regulation of
  locomotion" cite this paper; neither is supported. The V-ATPase hydrolyses ATP (it does
  not synthesise it), and unc-32 mutants have a movement *defect*, i.e. unc-32 is required
  for, not a negative regulator of, locomotion.

### Oka et al. 2001 (PMID:11441002, abstract only)

- "We have identified four genes (vha-5, vha-6, vha-7, and unc-32) coding for vacuolar-type
  proton-translocating ATPase (V-ATPase) subunit a in Caenorhabditis elegans" [PMID:11441002].
  "Their products had nine putative transmembrane regions, exhibited 43-60% identity and
  62-84% similarity with the bovine subunit a1 isoform" [PMID:11441002]. "The similarities,
  together with the results of immunoprecipitation, suggest that these isoforms are
  components of V-ATPase" [PMID:11441002] (basis of IPI complex membership; UniProt: interacts
  with subunit C VHA-11).
- "unc-32 was strongly expressed in nerve cells" [PMID:11441002]; RNAi "caused embryonic
  lethality similar to that seen with other subunit genes" [PMID:11441002].

### Nguyen et al. 1995 (PMID:7498734, abstract only)

- unc-32 is one of 18 genes whose mutation confers resistance to acetylcholinesterase
  inhibitors: "Measurements of acetylcholine levels in these mutants suggest that some of the
  genes are involved in presynaptic functions" [PMID:7498734]. Basis of the IMP to
  cholinergic synaptic transmission.

### Syntichaki, Samara & Tavernarakis 2005 (PMID:16005300, abstract only)

- "the function of the vacuolar H(+)-ATPase, a pump that acidifies lysosomes and other
  intracellular organelles, is essential for necrotic cell death in C. elegans"
  [PMID:16005300]; "Intracellular acidification requires the vacuolar H(+)-ATPase, whereas
  alkalization of endosomal and lysosomal compartments by weak bases protects against
  necrosis" [PMID:16005300]. Uses unc-32(e189). UniProt adds: required for cell death induced
  by hypoxia. The GOA term "positive regulation of programmed cell death" is broader than the
  necrotic death studied; GO:0062100 positive regulation of programmed necrotic cell death is
  the current, more specific term (GO:0070265 necrotic cell death is obsolete).

### Ernstrom et al. 2012 (PMID:22426883, full text cached)

- "The unc-32 ( e189 ) mutation truncates a neural-specific isoform of the V o subunit a"
  [PMID:22426883]. "unc-32 ( e189 ) mutants were also significantly aldicarb resistant with
  only 8.5% (±9%, n = 5 assays) paralyzed after 2 hr exposure" [PMID:22426883]; "The V o
  mutant unc-32 ( e189 ) also exhibited comparable sensitivity to levamisole to that of
  wild-type animals" [PMID:22426883] (presynaptic defect).
- Synaptic vesicle pH: synaptobrevin-pHluorin puncta were threefold brighter in vha-12
  mutants and "Similar results were seen in the V o subunit a mutant unc-32 ( e189 )"
  [PMID:22426883], i.e. synaptic vesicles are less acidic without UNC-32. The authors
  frame this as "neurotransmitter loading into vesicles relies on exchange of protons for
  neurotransmitter molecules" [PMID:22426883]. This directly supports GO:0097401 synaptic
  vesicle lumen acidification as the process UNC-32 executes; the GOA term "positive
  regulation of neurotransmitter secretion" describes the downstream consequence.

### Irazoqui et al. 2010 (PMID:20617181, full text cached)

- unc-32(e189) appears only as the linked marker in the mpk-1,unc-32 double mutant (both
  genes on chromosome III). Figure legend: "Nomarski micrographs illustrating the Dar
  phenotype after 12 h of S. aureus infection in wild type (F), egl-5 (H), pmk-1 (I), and
  unc-32 (J) mutant animals in contrast to non-Dar bar-1 (G) and mpk-1,unc-32 (K) mutants"
  [PMID:20617181]. The unc-32 single mutant behaves like wild type; the IGI annotation to
  defense response to Gram-positive bacterium is an artefact of the marker strain.

## Assessment

- Core: V0 subunit a of the neuronal V-ATPase; contributes to rotary proton-pumping ATPase
  activity; proton transmembrane transport; synaptic vesicle lumen acidification (the step
  of the SV cycle that powers transmitter loading); vacuolar/organellar acidification more
  generally in non-neuronal isoforms.
- Non-core: embryonic and larval development, locomotion, necrotic cell death and hypoxia
  response phenotypes are downstream of organellar acidification.
- Remove: ATP synthesis (wrong direction of the reaction), negative regulation of
  locomotion (wrong direction of the phenotype), defense response to Gram-positive
  bacterium (marker artefact, visible in the full text).

## Deep research

- `unc-32-deep-research-falcon.md` independently reaches the same conclusions: UNC-32 is the
  neuronal V0 subunit a, the transported substrate is H+, and "The resulting acidification
  supports neurotransmitter loading into synaptic vesicles and degradative activity in
  endosomes, lysosomes, and autolysosomes." It confirms isoform specialization (exon-4b
  neuronal forms disrupted by e189) and reports newer work (lysosomal proteomics,
  Cry14A resistance) that is not part of the GOA set.
