# cbl1 (O94350) curation notes

## 2026-11-13 audit and promotion to COMPLETE
- Sources: UniProt O94350 (Swiss-Prot, PE 3, all functional statements ECO:0000250 by similarity). GOA has 11 rows,
  which matched a live QuickGO query. No S. pombe publication on cbl1 function or localisation was found; the UniProt
  entry cites only the genome paper.
- Literature search: QuickGO annotations for O94350 (all IBA/IEA/ISS) and the UniProt reference list (genome sequence only).
  No experimental paper on the S. pombe protein was found.
- Family: PANTHER PTHR11808:SF50 (CYSTATHIONINE BETA-LYASE), the same subfamily as Arabidopsis CBL (P53780) and S. cerevisiae STR3.
  E. coli MetC is in a different PANTHER family (PTHR43500).
- Peroxisome ISS (from Str3, P53101): Str3's peroxisomal location rests on a C-terminal -SKL PTS1 and membrane proteomics
  (see genes/yeast/STR3 review). Cbl1 ends ...ANFKQN, with no PTS1 or PTS2-like motif [file:SCHPO/cbl1/cbl1-bioinformatics/RESULTS.md].
  The row was changed from UNDECIDED to MARK_AS_OVER_ANNOTATED under the root-organelle policy (synthesis row whose donor mechanism is absent).
- Other rows re-audited: TOO_GENERAL (sulfur compound metabolic process; carbon-sulfur lyase activity) and MODIFY of obsolete
  transsulfuration to GO:0071269 were kept, as were the ACCEPT rows for cytoplasm and GO:0047804 and the non-core PLP binding rows.
