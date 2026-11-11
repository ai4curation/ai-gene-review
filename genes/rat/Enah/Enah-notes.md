# Enah (rat) review notes

## 2026-10-28 session

- Task named UniProt A0A0G2K6I4; `just fetch-gene rat Enah` resolved A0A8I6GMP8 instead.
  Both are TrEMBL entries for the same gene (Enah, RGD:1307666); A0A0G2K6I4 additionally
  carries GeneID 360891. GOA (37 rows) is keyed to A0A8I6GMP8; QuickGO shows only a few IEA
  rows on A0A0G2K6I4. Reviewed A0A8I6GMP8.
- No deep-research provider available; literature summary in Enah-deep-research-manual.md.
- Only rat experimental annotations: SynGO IDA rows from PMID:16376568 (abstract only):
  postsynapse, GABA-ergic synapse, postsynaptic cytoskeleton organization. Kept as non-core.
- PMID:21278383 (full text): rat testis Tes IP pulls down Arp7A and Mena; Mena in the
  subacrosomal layer of round spermatids [PMID:21278383 "Arp7A, Tes, and Mena are complexed
  to each other in rat testes extracts"]. Interaction is a protein-binding observation; no
  NEW row (bare protein binding is not informative and the IF localisation was on mouse
  testis sections).
- ISO rows from mouse: most come from Gertler 1996 (PMID:8861907), Lanier 1999
  (PMID:10069337), Menzies 2004 (PMID:15371503). Neural tube closure and axon guidance rows
  are acts_upstream_of_or_within phenotype annotations: kept as non-core.
- `cellular response to leukemia inhibitory factor` ISO rests on a mouse IEP from an ES-cell
  miRNA profiling paper (PMID:20439489); expression response, not Ena/VASP function:
  marked over-annotated.
- Core function: Ena/VASP actin filament barbed-end binding / anti-capping processive
  elongation, recruited by EVH1-FPPPP interactions, binding profilin-actin via the proline
  rich region; acts at lamellipodia, filopodium tips and focal adhesions.
- Added NEW actin filament binding (GO:0051015), ISS from Ena/VASP family biochemistry.
