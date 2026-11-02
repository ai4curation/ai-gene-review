# osm-1 (Q22830, IFT172 ortholog) notes

## Deep research status
`just deep-research-falcon worm osm-1 --fallback perplexity-lite` was run on 2026-10-08. Falcon timed out (600 s) and the perplexity fallback was not installed in this environment, so there is no `osm-1-deep-research-*.md`. The review below was made by hand from the cached publications and PubMed.

## Summary with provenance
- OSM-1 is the worm IFT172 ortholog. It has WD and WAA repeats [PMID:16648645 "The daf-10 and osm-1 gene products resemble each other and contain WD and WAA repeats"] and is a complex B IFT component [PMID:16648645 "all of which encode complex B IFT components"].
- A rescuing OSM-1::GFP fusion [PMID:10545497 "The OSM-1::GFP fusion protein appears to be functional as it rescues the osm-1 mutant phenotype"] concentrates at the base of the transition zone and moves by IFT at the same rates as OSM-6 and kinesin-II [PMID:10545497 "OSM-1 and OSM-6, all move at approximately 1.1 microm/s in the retrograde direction along cilia and dendrites"].
- osm-1(p808) cilia have normal transition zones but severely shortened axonemes [PMID:2428682 "The cilia in che-13 (e1805), osm-1 (p808), osm-5 (p813), and osm-6 (p811) mutants have normal transition zones and severely shortened axonemes."].
- Dauer-defective phenotype is secondary to defective chemosensory cilia [PMID:1732156 "Dauer-defective mutations in nine genes cause structurally defective chemosensory cilia, thereby blocking chemosensation."].
- Ortholog: Chlamydomonas IFT172/FLA11 regulates IFT turnaround at the tip [PMID:15694311 "IFT172 is involved in regulating the transition between anterograde and retrograde IFT at the tip"]. No direct worm test of a tip-turnaround role was found in the cache.

## Curation decisions
- 23 GOA rows: 20 ACCEPT, 3 KEEP_AS_NON_CORE (dauer entry IGI rows).
- The ARBA IEA to GO:0030990 (generic IFT particle) is a correct parent of IFT-B, so it is accepted.
- No MF in core_functions: no worm molecular activity has been shown; the ND root row is accepted.
