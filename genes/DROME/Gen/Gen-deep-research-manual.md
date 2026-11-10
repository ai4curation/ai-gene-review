# Gen (CG10670, Q9VRJ0) — manual literature review

No deep-research provider was available for this session; this summary was compiled by hand
from the cached publications in `publications/` and PubMed searches
("Drosophila Gen endonuclease GEN1 mus324"; "Drosophila GEN Holliday junction resolvase").

## Identity and family

- Gen (DmGEN, "XPG-like endonuclease"; FBgn0263831; ORF CG10670) encodes a 726-aa member of the
  XPG/RAD2 structure-specific nuclease family, GEN subfamily (class IV), the ortholog of human GEN1 and
  budding-yeast Yen1. It has XPG-N and XPG-I nuclease domains positioned close together, as in FEN1/EXO1,
  followed by an H3TH (HhH2) DNA-binding region and a chromodomain-like region (UniProt Q9VRJ0; InterPro
  IPR041012 GEN_chromo).
  [PMID:15576351 "The encoded protein showed a relatively high degree of sequence homology with the RAD2 nucleases, especially XPG."]
- The original genetic name for the locus was *mus324*; the two mus324 alleles carry the same frameshift
  in Gen at codons 374–375.
  [PMID:22022278 "We conclude that mus324 is Gen and hereafter refer to these alleles as GenZ4325 and GenZ5997."]

## Biochemistry

- Ishikawa et al. 2004 first purified DmGEN and reported endonuclease and both 3'-5' and 5'-3' exonuclease
  activities [PMID:15576351 "In vitro, DmGEN showed endonuclease and 3'-5' exonuclease activities with both single-stranded DNA (ssDNA) and double-stranded DNA (dsDNA)"].
  UniProt considers the 3'-5' exonuclease probably artifactual (CAUTION in Q9VRJ0: contaminating nucleases).
- Kanai et al. 2007, using an E143A/E145A active-site mutant as a control, established 5'-flap endonuclease
  activity with a preference for blocked flaps, cleavage of the lagging strand of a model replication fork,
  weak nick-dependent 5'-3' exonuclease, and no bubble incision
  [PMID:17614965 "DmGEN preferred the blocked-flap structure as a substrate"].
  They reported (abstract-only in cache; via UniProt FUNCTION) no Holliday junction cleavage.
- Bellendir et al. 2017 (full text) showed with recombinant full-length and truncated DmGen that it cleaves
  5' flaps, replication-fork structures, splayed arms and fixed, mobile and nicked Holliday junctions, but not
  3' flaps, unbranched or nicked duplex [PMID:28369583 "We did not detect cleavage of unbranched dsDNA, nicked duplex DNA, or 3΄ flaps"].
  HJ cleavage is symmetric and yields ligatable nicked duplexes; DmGen binds HJs with sub-nanomolar affinity
  (EMSA, K1/2 ~0.2 nM) and forms dimers on HJs; flap cleavage is much faster than HJ cleavage because
  productive dimer assembly on the HJ is rate-limiting. This supersedes the 2007 report of no HJ cleavage.

## Localization

- Kanai 2007: anti-DmGEN immunostaining placed the protein in nuclei of proliferating early embryos
  [PMID:17614965 "revealed that DmGEN was present in the nucleus of actively proliferating"].
- Bellendir 2017: a different antibody and His-tagged overexpression in S2 cells showed predominantly or
  exclusively cytoplasmic localization in interphase, like human GEN1 (cytoplasmic until nuclear envelope
  breakdown) and yeast Yen1 [PMID:28369583 "DmGen, like Yen1 and HsGEN1, is primarily or exclusively cytoplasmic during interphase"].
  The two reports conflict; the more recent, better-controlled work favours interphase cytoplasmic
  sequestration with presumed access to DNA in mitosis.

## Genetics / in vivo roles

- Gen mutants are hypersensitive to MMS and nitrogen mustard (HN2) — more so than mus81 mutants
  [PMID:22022278] — and to camptothecin, hydroxyurea and ionizing radiation [PMID:28369583
  "Gen mutants were significantly more sensitive to both agents, with mus81 mutants showing sensitivity only to HN2"].
- mus81 Gen double mutants show elevated apoptosis in imaginal discs and stronger hypersensitivity than
  either single mutant: MUS81 is a backup to GEN in flies (reverse of yeast/human).
- Gen Blm (mus309) double mutants die as first-instar larvae; lethality is partially suppressed by loss of
  Rad51 (spn-A), implicating recombination intermediates [PMID:22022278 "Rather than dying at the first larval instar, the Gen mus309 spn-A mutants survive to the pupal stage"].
- Gen is also essential (together with MUS81 or SLX1) in Fancm mutants [PMID:25205745].
- In an I-SceI DSB repair screen (before mus324 was known to be Gen), mus324 modestly reduced
  single-strand annealing under a mild heat-shock regime only [PMID:17660539].

## Synthesis

Gen encodes the fly GEN1/Yen1 structure-selective endonuclease, cleaving 5' flaps, replication-fork-like
structures and Holliday junctions (symmetrically). It is the predominant structure-selective nuclease for
damage tolerance in Drosophila, acting in DNA repair (replication-associated damage, crosslinks, DSBs) with
MUS81-MMS4 as backup; it becomes essential when BLM or FANCM is absent. Whether its key in vivo substrates
are HJs or simpler branched intermediates remains unresolved.
