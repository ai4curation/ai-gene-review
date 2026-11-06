# cysK (E. coli K-12, P0ABK5) curation notes

## 2026-11-03 first full review

Deep research: no provider output exists for this gene and no provider API keys
are available in this session, so no `-deep-research-*.md` file was generated.
The review rests on the UniProt record, PAINT data for PTHR10314 and the cached
publications for every GOA row (all abstract-only except PMID:18304323).

- Core activity: CysK (OASS-A) makes L-cysteine from O-acetyl-L-serine and
  sulfide [UniProtKB:P0ABK5, "Reaction=O-acetyl-L-serine + hydrogen sulfide =
  L-cysteine + acetate;"]. cysK mutants lack the activity [PMID:338862 "cysK
  mutants, deficient in O-acetylserine sulphydrylase A"].
- Cysteine synthase complex with CysE [PMID:22179612 "The complex is comprised
  of the two enzymes that catalyze the final steps in cysteine biosynthesis"];
  the SAT C-terminus is needed for complex formation [PMID:10052138 "SAT delta
  C20 did not form a complex with O-acetylserine sulfhydrylase-A (OASS-A)"].
  Complex formation lowers OASS-A Vmax [PMID:10993149].
- Secondary cysteine desulfhydrase activity [PMID:16000837 "three additional
  proteins having L-cysteine desulfhydrase activity were identified as
  O-acetylserine sulfhydrylase-A"], with tryptophanase dominant. Kept non-core.
- S-carboxymethylcysteine synthase (3-chloro-L-alanine + thioglycolate) is a
  measured in vitro beta-replacement with KM 40 mM for 3-chloro-L-alanine;
  marked over-annotated as an in vitro activity of unknown physiological
  relevance (CLAUDE.md promiscuous-activity tiers).
- CdiA-CT toxin activation (PubMed:22333533, PubMed:27531961 in UniProt) is a
  moonlighting role during contact-dependent growth inhibition and is not in
  GOA; no NEW row proposed.
- PANTHER: P0ABK5 is classified in PTHR10314:SF194, whose official name is
  CYSTATHIONINE BETA-SYNTHASE and which also holds human CBS and yeast CYS4.
  The subfamily name does not describe CysK; PAINT's cysteine synthase node
  PTN000034535 (taxon:2) is the relevant bacterial node.

## 2026-11-03 PR #5929 review round

- Core function no longer asserts `in_complex: GO:0009333`. PMID:10993149
  shows that complex formation lowers the maximum velocity of bound OASS-A
  ["the maximum velocity for OASS-A was lowered"], so the productive
  sulfhydrylase is free CysK; complex membership is a regulatory/structural
  association. The GO:0009333 annotation rows stay ACCEPT.
- Removed a duplicated references block (second copies of the UniProt and
  PTHR10314 PAINT entries).
- The CDI toxin-activation claim in the description is now sourced: PMID:22333533
  ["tRNase that requires activation by the biosynthetic enzyme CysK (O-acetylserine
  sulfhydrylase A)."] and PMID:27531961 ["CysK significantly increases
  CdiA-CT(EC536) thermostability and is required for toxin interaction with tRNA
  substrates."]; a suggested question was added.
