# acnB (P36683, E. coli K-12) review notes

## Deep research status

Provider deep research (`just deep-research ECOLI acnB --provider ...`) could not be
run in this session because provider API credentials were unavailable. No
`*-deep-research-*.md` file was created. These notes are based on the cached
UniProt record and cached publications (mostly abstract-only; PMID:12486059 and
PMID:18304323 have full text). PMID:11992126, PMID:11932448, PMID:8000525 and
PMID:9202458 were fetched into `publications/` with `just fetch-pmid`.

## Catalytic function

- AcnB is the major TCA-cycle aconitase during exponential growth
  [PMID:10585860 "AcnB functions as the major citric-acid-cycle enzyme during exponential growth"];
  [PMID:9202458 "AcnB is the major aconitase, which is synthesized earlier in the growth cycle than AcnA"].
- acnAB double mutants cannot grow on unsupplemented glucose minimal medium
  [PMID:9202458 "The acnAB double mutant would not grow on unsupplemented glucose minimal medium"].
- First detected as residual activity in an acnA mutant
  [PMID:8000525 "This activity was due to an analogous unstable enzyme(s) designated aconitase B."].
- Monomer of ~93.5 kDa with rearranged domain order
  [PMID:8932712 "the domain organization of AcnA and related proteins (1-2-3-linker-4) is rearranged in AcnB (4-1-2-3)"].
- [4Fe-4S] cluster; [3Fe-4S] in oxidized inactive form
  [PMID:10585860 "The EPR and MCD spectra of the oxidized inactive form of AcnB confirmed the presence of a [3Fe-4S](1+) (S=1/2) cluster."].
- 2-methylcitrate cycle: AcnB is the 2-methyl-cis-aconitate hydratase, acting after PrpD
  [PMID:12473114 "AcnB was purified as 2-methylaconitate hydratase from E. coli cells grown on propionate and identified by its N-terminus."];
  [PMID:12473114 "The enzyme has an apparent Km of 210 micro m for (2R,3S)-2-methylisocitrate but shows no activity with (2S,3S)-methylcitrate."].

## Structure

- 2.4 A structure (PDB 1L5J) with an extra HEAT-like domain forming a substrate tunnel
  [PMID:11992126 "This domain packs against the remainder of the protein to form a tunnel leading to the aconitase active site, potentially for substrate channeling."].

## Regulatory (moonlighting) function

- Apo-AcnB binds acn mRNA 3'UTRs
  [PMID:10589714 "Affinity chromatography and gel retardation analysis showed that the AcnA and AcnB apo-proteins each interact with the 3' untranslated regions (3'UTRs) of acnA and acnB mRNA at physiologically significant protein concentrations."].
- AcnB lowers sodA transcript stability
  [PMID:11932448 "Quantitative Northern blotting indicated that AcnA enhances the stability of the sodA transcript, whereas AcnB lowers its stability."].
- Domains 5-4 mediate iron-dependent dimerization and ftsH mRNA binding
  [PMID:15882410 "the isolated AcnB5-4 polypeptide specifically recognized and bound to the ftsH transcript"].
- Cluster is labile to iron depletion and oxidants
  [PMID:12486059 "We observed that the [4Fe-4S] cluster of AcnB is in dynamic equilibrium with the surrounding iron pool, so that AcnB is rapidly demetallated when intracellular iron pools drop."].

## Curation decisions (summary)

- All catalytic, cofactor, TCA-cycle, propionate catabolism and cytosol rows accepted.
- Both mRNA binding rows and both mRNA 3'-UTR binding rows accepted (kept consistent).
- regulation of translation (IDA) kept as non-core; NEW `GO:0043488 regulation of
  mRNA stability` proposed because AcnB itself binds the target transcripts and
  changes how stable they are (acn up, sodA down).
- glyoxylate cycle (NAS) kept as non-core: aconitase does catalyse a step the
  glyoxylate cycle shares with the TCA cycle.
- Bare protein binding (thioredoxin TAP-MS, PMID:15004283) removed, per the
  protein-binding policy.
