# Syt4 (rat, UniProt P50232) - manual literature synthesis

No deep-research API was available for this review. This file is a manual synthesis
written by the reviewer from the cached publications in `publications/` and the UniProt
record (`Syt4-uniprot.txt`). Every claim carries its source.

## Identity and architecture

- Synaptotagmin-4 (Syt IV), 425 aa, single-pass membrane protein with a short
  intravesicular N-terminus, one TM helix (17-37) and a cytoplasmic region carrying two C2
  domains (C2A 153-274, C2B 287-420) [UniProt P50232 FT TRANSMEM/DOMAIN].
- Belongs to the synaptotagmin family; PANTHER PTHR10024:SF114 (SYNAPTOTAGMIN-4).
- Immediate early gene: mRNA induced in PC12 cells by depolarization, Ca2+ ionophore, ATP and
  forskolin, and in hippocampus/piriform cortex after kainate seizures [PMID:7892240 "SytIV mRNA
  accumulation is transiently induced in PC12 cells by potassium depolarization, calcium
  ionophore, ATP, and forskolin"]. Protein is labile (t1/2 about 2 h) [PMID:10217258].

## Ca2+ binding: lost in mammals

- C2A carries an Asp-to-Ser substitution (Ser244) of a Ca2+ ligand; wild-type rat Syt4 C2A has
  no Ca2+-dependent phospholipid binding, and S244D restores it [PMID:9162066 "wild type
  C2A-domains of synaptotagmins IV and XI exhibited no Ca2+-dependent phospholipid binding"].
- C2A of Syt IV unable to bind Ca2+ [PMID:7993622 "whereas that of synaptotagmin IV is unable to
  bind Ca2+"]; not among the C2As that bind phospholipids Ca2+-dependently [PMID:7791877].
- Crystallography: rat Syt4 C2B also cannot form full Ca2+-binding sites; neither rat C2 domain
  binds Ca2+ or phospholipids efficiently, while fly Syt4 does [PMID:15311271 "neither C(2)
  domain of rat synaptotagmin 4 binds Ca(2+) or phospholipids efficiently"].
- Contrary older data: Thomas et al. reported Ca2+-dependent C2B-mediated homo- and
  hetero-oligomerization with Syt I [PMID:10397765], and Chapman et al. reported Ca2+-promoted
  Syt I/IV hetero-oligomerization [PMID:9830048].

## Molecular function: Ca2+-independent SNARE binding; inhibitory isoform in fusion

- Syt4 C2A binds syntaxin isoforms (1A, 2, 3, 4) Ca2+-independently [PMID:10397765 "the C2A domain
  of Syt IV binds syntaxin isoforms in a calcium-independent manner"].
- Syt4 binds syntaxin 6 on immature secretory granules [PMID:16618809].
- Reconstituted fusion: Syt IV binds t-SNAREs and PS without Ca2+ enhancement, fails to stimulate
  fusion, inhibits SNARE-only fusion and inhibits Syt I-stimulated fusion partly by displacing
  Syt I from t-SNAREs [PMID:18508778 "Here, we demonstrate that syt IV itself inhibits
  SNARE-catalyzed membrane fusion"].
- Rat versus fly Syt4: rat protein inhibits fusion with or without Ca2+, binds t-SNARE
  heterodimers strongly and Ca2+-independently, and in a co-sedimentation assay fails to bind PS;
  reversing S244D converts it into a Ca2+ sensor [PMID:20688915 "rat SYT4 serves as an inhibitory
  isoform, whereas fly SYT4 is a bona fide Ca(2+) sensor"].
- The two Chapman-lab papers disagree on PS binding (some Ca2+-independent PS binding in
  co-flotation in PMID:18508778, none in co-sedimentation in PMID:20688915).
- Syt IV inhibits liposome fusion driven by Syt I, VII or IX with different efficacies
  [PMID:21551071].

## Cellular roles

- Negative regulator of dense-core vesicle exocytosis in PC12 cells: overexpression reduces the
  basal rate of Ca2+-induced fusion and alters fusion and fission pores [PMID:20303854]; inhibits
  catecholamine release, more strongly when Syt I is knocked down [PMID:20735850]; inhibits
  exocytosis of Syt I- and Syt IX-bearing DCVs [PMID:21551071]. A microinjected C2A fragment
  inhibits Ca2+-triggered release [PMID:10397765].
- Positive role in immature secretory granule (ISG) homotypic fusion and granule maturation in
  PC12 cells (siRNA) [PMID:16618809 "We conclude that Syt IV is an essential component for
  secretory granule maturation"].
- Mouse: Syt4 localises to BDNF-containing vesicles and inhibits BDNF release in axons and dendrites;
  effects on presynaptic SV exocytosis are indirect, via BDNF [PMID:19448629]. In posterior pituitary
  terminals Syt IV is on micro- and dense-core vesicles; knockout changes exocytosis in a
  Ca2+-dependent way and speeds endocytosis [PMID:19136969]. Knockout mice show enhanced CA1
  short-term plasticity and memory deficits [PMID:15390175].
- DCV trafficking: Syt4 links DCVs to KIF1A; JNK phosphorylation of Ser135 weakens Syt4-KIF1A
  binding and leads to DCV capture at synapses [PMID:29166604 "Phosphorylation of serine 135 of
  Syt4 by JNK steers DCV trafficking by destabilizing Syt4-Kif1A interaction"]. KIF1A pulls down
  Syt4 in a Ca2+-dependent way [PMID:30021165].
- NGF/JNK-dependent phosphorylation at Ser135 moves Syt4 from immature to mature secretory vesicles
  and is needed for NGF enhancement of Ca2+-evoked release in PC12 cells [PMID:18046461].
- Astrocytes: Syt IV in astrocyte processes; RNAi reduces Ca2+-dependent glutamate release
  [PMID:15197251].
- Pancreatic beta cells: SYT4 silencing reduced GSIS in INS1-832/13 cells [PMID:22939844,
  abstract only].

## Localisation

- Golgi and tips of neurites in PC12 cells and hippocampal neurons [PMID:10646502]; mouse neurons:
  dendrites, axons and Golgi, not synaptic vesicles [PMID:12135783].
- Synaptic-like microvesicles and secretory granules in PC12 cells (fractionation) [PMID:10217258];
  ISG and Golgi fractions [PMID:16618809].
- Neuronal DCV membrane, co-localised with chromogranin A [PMID:29166604].
