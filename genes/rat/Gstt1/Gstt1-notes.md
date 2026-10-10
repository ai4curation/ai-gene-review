# Gstt1 review notes

## Evidence summary
- [UniProtKB:Q01579] UniProt describes GSTT1 as a glutathione-conjugating enzyme with dichloromethane dehalogenase activity.
- [PMID:20097269] The fetched GOA file uses this publication for glutathione transferase activity and glutathione metabolic process.
- [PMID:11453994] The fetched GOA file uses this publication for alkylhalidase activity and dichloromethane metabolic process.

## Curation decisions
- Core function: glutathione S-transferase theta-1 (glutathione transferase activity, GO:0004364).
- Specific catalytic activities and direct metabolic processes were accepted.
- Broad parent, localization, binding, and stimulus-response annotations were modified, kept non-core, or marked over-annotated according to support.

## Re-review 2026-10-04

**GOA changes.** Four new seeded rows, all donor splits: glutathione transferase activity (GO:0004364), cytosol (GO:0005829) and glutathione metabolic process (GO:0006749, involved_in) from human GSTT1 (UniProtKB:P30711), and glutathione metabolic process (involved_in) from mouse Gstt1 (MGI:MGI:107379, UniProt Q64471), which sits beside the existing acts_upstream_of_or_within row from the same donor. No retired rows. Total 29 rows.

**Actions.**
- GO:0004364 ISO (human GSTT1): PENDING -> ACCEPT, matching the mouse-donor row and the rat IDA rows (PMID:20097269, PMID:12588193).
- GO:0005829 ISO (human GSTT1): PENDING -> KEEP_AS_NON_CORE, as for the mouse-donor row; rat enzyme purified from liver cytosol.
- GO:0006749 ISO involved_in (mouse Gstt1; human GSTT1): PENDING -> ACCEPT, consistent with IBA/IDA rows.
- No action changed on existing rows. The IEA response to salicylic acid row (ARBA) cited a UniProt DR GO line no longer present in the refreshed flat file; it now cites the rat NSAID induction data [PMID:9729437 "Colonic GSTT1-1 levels were elevated by all NSAIDs tested except for relafen"] and stays MARK_AS_OVER_ANNOTATED as stimulus-response context. Donors are now named on the existing ISO rows.
- Description rewritten as standalone biology (removed "The review accepts ..." commentary).

**Open questions.** None new.
