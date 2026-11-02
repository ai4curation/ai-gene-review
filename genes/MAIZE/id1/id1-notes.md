# id1 (MAIZE) review notes

## Session 1 (2026-10-28)

- `just fetch-gene MAIZE id1` resolved UniProt O65215 (GeneID 541693), as requested. 9 GOA rows:
  2 IBA (DNA-binding TF activity, nucleus), 7 IEA (EnsemblPlants Compara projection from
  rice EHD2/OsId1 B1B534, plus one ARBA-combined row).
- No experimental GOA rows exist for maize ID1, although experimental papers do:
  Kozaki 2004 [PMID:15020707] (full text; in vitro DNA binding), Wong & Colasanti 2007
  [PMID:17307745] (abstract; nuclear immunolocalization). Added NEW IDA rows for
  sequence-specific DNA binding and nucleus from these.
- Photoperiodism rows (LD and SD flowering) come from rice. Maize ID1 is the
  autonomous-pathway regulator; its expression is photoperiod insensitive [PMID:17307745],
  and rice OsId1 acts "regardless of photoperiod" [PMID:18774969]. Photoperiodism
  ("change ... as a result of detection of ... a period of light or dark of a given length")
  is therefore an over-annotation; marked MARK_AS_OVER_ANNOTATED, not REMOVE (IEA from an
  experimental rice annotation; no maize experiment refutes it in tropical maize).
- Positive regulation of transcription: activation shown only for rice OsId1 in yeast
  [PMID:18774969]; maize ZCN8 regulation is probably indirect [PMID:21730358]. Kept as
  non-core.
- Rejected NEW BP terms: no 'positive regulation of flower development' etc.; mutant
  phenotype alone. GO:0048510 already covers the role.
- Lazakis 2011 [PMID:21730358] read in full: id1 upstream of ZCN8; ZCN8 is unlikely a
  direct target.
