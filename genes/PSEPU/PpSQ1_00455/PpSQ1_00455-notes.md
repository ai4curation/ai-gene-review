# PpSQ1_00455 (P0DOV8) KDSG aldolase, Pseudomonas putida SQ1 — notes

## Provenance and access

- Deep research with perplexity failed in this environment (2026-11-10; "All providers failed").
  Sources: UniProt P0DOV8, PMID:26195800 (abstract only), PMID:41676062 (review, full text),
  PMID:41830472 (Kaur et al. 2026 Chemistry, KDSG aldolase structure; abstract only, no PMC).

## Function

- UniProt (ECO:0000269 PubMed:26195800): "Catalyzes the retro-aldol cleavage of
  2-dehydro-3,6-dideoxy-6-sulfo-D-gluconate to (2S)-3-sulfolactaldehyde and pyruvate."
  RHEA:47924, EC 4.1.2.58. Induced on SQ.
- [PMID:26195800 "The aldolase reaction yields pyruvate, which supports growth of P. putida, and
  3-sulfolactaldehyde (SLA)"].
- [PMID:41830472 "We report the biochemical and structural characterization of a metal-dependent
  KDSG aldolase from Pseudomonas putida using chemo-enzymatically synthesized KDSG."]; homohexamer
  (dimer of trimers), optimal with Co2+ or Mn2+, mM KM for KDSG, "modest cross-reactivity" with
  KDPG. The abstract does not give the strain or accession, so it is used as supporting context
  (the class II, metal-dependent HpcH/HpaI mechanism) and not as the basis of a new row.
- GO has no KDSG aldolase term (OLS 2026-11-10). Parent GO:0016832 aldehyde-lyase activity is
  the module's term.

## GOA rows

- GO:0003824 (InterPro2GO IPR005000) -> MODIFY to GO:0016832.
- GO:0016832 (TreeGrafter, with PTN007825897) -> ACCEPT. Current PTHR30502 PAINT slice:
  root PTN000766732 asserts GO:0016832 (seeds E. coli GarL P23522 and RhmA P76469); the root
  covers every member, so the claim is phylogenetically sound and matches the enzymology.
- GO:0005737 cytoplasm (TreeGrafter) -> KEEP_AS_NON_CORE; soluble catabolic enzyme with no
  signal peptide acting on intracellular pathway intermediates. Not in the current PAINT slice.
