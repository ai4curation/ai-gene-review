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
