# mus81 (Drosophila melanogaster, Q9V3T1) - manual literature research

No deep-research API keys were available for this session, so this summary was
assembled manually from PubMed searches (query "Drosophila mus81", 6 hits) and the
cached full texts in `publications/`.

## Identity and domain architecture

- Q9V3T1 (CG3026, FBgn0040347) is an unreviewed TrEMBL entry, 426 aa, PE 3
  (inferred from homology). It carries an ERCC4 (XPF-type) nuclease domain
  (SMART SM00891, residues 154-252), an HhH DNA-binding region (Pfam HHH_8) and the
  EME1/MUS81 C-terminal winged-helix region (Pfam EME1-MUS81_C); PANTHER PTHR13451:SF0.
  It lacks the N-terminal HhH/XPF-binding portion found in longer vertebrate MUS81
  (human MUS81 is 551 aa).
- UniRule (RU369042) assigns the MUS81 family function: heterodimer with EME1/MMS4,
  structure-selective endonuclease preferring 3'-flaps, D-loops, replication forks and
  nicked Holliday junctions.

## Experimental work on Drosophila MUS81

- Trowbridge et al. 2007 [PMID:17603121] generated mus81 (mus81Nhe) and mms4 mutants.
  Drosophila MMS4 interacts with MUS81 in yeast two-hybrid ["After confirming that the
  product of this gene interacts with MUS81 in a yeast two-hybrid assay"].
  No role in meiotic crossing over ["Unlike the case in fungi, we did not find any role
  for MUS81-MMS4 in meiotic crossing over."]. Hypersensitive to camptothecin only
  ["mus81 and mms4 mutants are hypersensitive to camptothecin; however, these mutants
  are not hypersensitive to other agents that generate lesions that slow or block DNA
  replication"]. Synthetic lethality with mus309 (Blm), partially suppressed by spn-A
  (Rad51) mutation; mus81 mutants are hyposensitive to HU.
- Andersen et al. 2011 [PMID:22022278] compared double mutants of mus309 with mus81,
  Gen and mus312/slx1: "MUS81 is the catalytic subunit of a heterodimeric endonuclease
  (MUS81–MMS4)." and "Therefore, three putative HJ resolvases – MUS81–MMS4, GEN, and
  MUS312–SLX1 are essential in the absence of DmBLM." mus81; Gen double mutants show
  elevated apoptosis in wing discs. The authors interpret the lethality as failure to
  process replication-fork structures ["This suggests that synthetic lethality between
  Gen and mus309 and between mus81 and mus309 are not due to inability to dissolve dHJs
  or disrupt D-loops, but to inability to process replication fork structures."].
  This paper is the source of the FlyBase IGI DNA repair annotation (with mus309).
- Kuo et al. 2014 [PMID:25205745]: "Spontaneous mitotic crossovers that occur in the
  absence of FANCM require the MUS312 nuclease scaffold protein and either MUS81 or
  SLX1"; crossovers were nearly absent in mus81; Slx1 Fancm triple mutants.
- Bellendir et al. 2017 [PMID:28369583]: in flies GEN is the predominant structure-
  selective endonuclease; mus81 single mutants are only weakly sensitive (HN2), but
  "The increased sensitivity of mus81 Gen double mutants indicates that in flies, Mus81
  plays a secondary role to DmGen." Double mutants are more IR-sensitive than Gen alone.
  Mus81 "may exacerbate problems caused by HU".
- Johnson-Schlitz & Engels 2006 [PMID:17075047] used mus81 with DmBlm in premeiotic
  germline DSB repair assays (abstract only consulted).

## Gaps

- No biochemical characterisation of Drosophila MUS81-MMS4 has been published; all
  molecular-function claims rest on homology.
- No direct localisation data for fly MUS81.
