# lexA2 (PP_3116, P59479) curation notes

- Status set to COMPLETE during ImuABC module curation. All rows already carried vetted
  quotes from the UniProt record, PMID:15458417, PMID:17933893 and the falcon deep-research
  report; the terse cross-reference reasons were expanded to state the argument.
- LexA2 is not the canonical SOS repressor of KT2440: LexA1 controls 18 transcriptional
  units, LexA2 only its own lexA2-imuA-imuB-dnaE2 operon plus the prophage-associated
  PP_3901. That is why GO:0009432 (SOS response) is MARK_AS_OVER_ANNOTATED here while it is
  ACCEPTed on recA and kept as non-core on imuA.
- The serine-type endopeptidase activity (GO:0004252) rests on the curated HAMAP rule
  MF_00015 (the LexA autocleavage reaction, EC 3.4.21.88); no KT2440 cleavage assay exists.


## 2026-11-07 — comparative ImuABC annotation audit

Direct KT2440 promoter-binding and regulon experiments support repression by a narrow SOS branch; they do not justify excluding SOS merely because LexA1 controls more genes. SOS and functional operator-bound complex are core. Curated LexA-family autoproteolysis remains explicitly inferred; no purified target cleavage experiment was identified. The scoped primary-reading file records full-source access separately from unchanged abstract-only caches.

The genuine existing provider research was read and preserved unchanged; primary sources control conclusions where reports are stale. PAINT-loss checking completed sequentially, but the target is not a leaf in the available cached family tree: loss status is unavailable, not demonstrated absent. Original ordered annotation payloads and historical NEW actions are preserved; no new row is added. Existing notes above are historical and superseded only where this dated audit explains a correction. All original raw, provider and publication bytes remain unchanged.

## 2026-11-07 PR6169 review follow-up

Refine the original GO:0006508 proteolysis row to GO:0016540 protein autoprocessing, and associate the already-supported autoprotease core with this specific process. Fresh QuickGO definition and is_a/part_of ancestry establish the refinement. Original source payload and quote support are unchanged; no new annotation is created. The narrow regulon participates in SOS signaling, so the family cross-reference must no longer say this review rejects SOS response.
