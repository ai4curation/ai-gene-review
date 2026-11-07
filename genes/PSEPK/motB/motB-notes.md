# motB (PP_4904, Q88DC3) notes

## 2026-11-03 re-review
- Deep research: `just deep-research PSEPK motB --provider perplexity` failed (provider 'perplexity' not available); `just mod-description-deep-research` skipped (no MOD provider configured for PSEPK). Existing falcon report used; every falcon quote was checked as a verbatim substring.
- UniProt quotes now cite the local flat file (file:PSEPK/motB/motB-uniprot.txt). ARBA-only, imported (ECO:0000313), DE-name and DR GO lines are not used as support.
- Replaced ARBA/imported UniProt quotes (cell membrane, "Flagellum", PANTHER name) with Phobius TRANSMEM and PROSITE OmpA-like domain lines.
- GO:0016020: REMOVE -> MODIFY to GO:0005886 (true but general). GO:0005886: KEEP_AS_NON_CORE -> ACCEPT.
- Added NEW rows for the core-function terms that had no annotation row: GO:0071973 (IMP, PMID:36409076 motAB deletion), GO:0120101 stator complex (IC), GO:0042834 peptidoglycan binding (IC, OmpA-like domain; subunit MF), GO:0015078 contributes_to (IC; module MF, complex level) [PMID:35572622 "MotB/PomB have a single TM segment at their N-termini and a large periplasmic C-terminal region that is anchored to the peptidoglycan (PG) layer."]. Status remains COMPLETE.
