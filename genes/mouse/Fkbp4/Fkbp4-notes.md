# mouse Fkbp4: comparative annotation review

## Provenance and scope

Normal `just fetch-gene` seeded every annotation; machine-sourced fields are preserved. Falcon deep research failed with HTTP 403 and its perplexity-lite fallback failed with HTTP 401. This is manual literature research, not a provider-generated report. Source caches were obtained through normal fetch commands and were not edited. Primary publications and curated UniProt statements were read; abstract-only evidence is not treated as proof of a wrong gene. No new biological-process annotations were proposed.

## Mechanistic boundaries

PMID:17142810 compares native Fkbp4 and Fkbp5 knockouts. Fkbp4 loss impairs AR transcription and selected reproductive tissues, but AR ligand binding and nuclear translocation remain intact. Fkbp5-null males lack those reproductive defects. PMID:11751894 describes glucocorticoid receptor immunophilin exchange and dynein-associated import; it must not be used as proof that FKBP52 is obligatory for AR import. The earlier recombinant mouse FKBP52 study PMID:8341706 actually reports ATP/GTP binding; this was not dismissed on protein-family expectation. PMID:7542743 directly establishes recombinant mouse FKBP51 PPIase activity.

## Additional functions and uncertainty

PMID:20133804 supports Tau binding/microtubule and neurite effects for FKBP52. PMID:28147277 supports the FKBP51-AKT-PHLPP adaptor mechanism in mammalian cells. The mouse Fkbp5 UniProt FUNCTION/SUBUNIT text says dephosphorylation followed by activation, but its PTM section and the primary study indicate suppression; the review follows the primary mechanism. Fine localization, copper-related transfer and context-specific expression claims remain unresolved where independent evidence was insufficient. Seeded obsolete receptor-binding IDs were checked with QuickGO and preserved; replacement is reviewer-authored.


## Selected source passages

[file:mouse/Fkbp4/Fkbp4-uniprot.txt] “Immunophilin protein with PPIase and co-chaperone activities.”

[PMID:8341706] “The rFKBP-52 possesses an ATP/GTP binding activity that is stimulated by divalent cations.”

[file:mouse/Fkbp4/Fkbp4-uniprot.txt] “Colocalized with MAPT/TAU in the distal part of the primary cortical neurons.”

[PMID:8341706] “The rFKBP-52 can be assembled in vitro with the glucocorticoid receptor complex”
