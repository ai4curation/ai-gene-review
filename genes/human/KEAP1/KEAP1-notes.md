# KEAP1 notes

## 2026-11-05 ORGANELLES ER batch 2 (endoplasmic reticulum rows)

- Rows: one GO:0005783 row, IEA GO_REF:0000107 (Ensembl projection), located_in; previously KEEP_AS_NON_CORE with an unsupported NFE2L1 rationale.
- Projection source (QuickGO, mouse Q9Z2X8, GO:0005783): a single MGI IDA from PMID:14517290 (fetched; abstract only). The abstract calls the complexes cytoplasmic [PMID:14517290 "In unstressed cells, Nrf2 is maintained in the cytoplasm via association with Keap1."]. Full text PMC230321 could not be retrieved (PubMed MCP returned no body; NCBI efetch says the publisher does not allow it; Europe PMC returned an error).
- NFE2L1 rationale refuted: [PMID:16687406 "Nrf1 also resides normally in the cytoplasm of cells. Cytoplasmic localization however, is independent of Keap1."]
- UniProt curated location: cytoplasm and nucleus, "Mainly cytoplasmic" [file:human/KEAP1/KEAP1-uniprot.txt]; no ER.
- PubMed search: Keap1 AND ("endoplasmic reticulum membrane" OR "ER membrane") AND localization: 2 hits (16687406 on Nrf1; 42946668, a proteostasis-network survey, no KEAP1 localization result in its abstract), no human KEAP1 ER finding.
- Outcome: KEEP_AS_NON_CORE -> UNDECIDED (only source unreadable). If the source shows only a cytoplasmic pool, MARK_AS_OVER_ANNOTATED; if an ER fraction, KEEP_AS_NON_CORE. Root either way (soluble adaptor).
