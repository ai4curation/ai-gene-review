# atg-5 (Q3V5I7, Y71G12B.12) review notes

## Provenance / process
- Q3V5I7 is the Swiss-Prot entry (275 aa, three isoforms a/b/c); used.
- Deep research failed (falcon unavailable; perplexity-lite fallback reported "Provider 'perplexity' not available"). No deep-research file; review based on cached publications, UniProt and PubMed.
- PMID:24185444 cache contains abstract, introduction and discussion only (no Results/figures).

## Key evidence
- "Here we demonstrate that loss of function of atg-5 abolishes LGG-1 lipidation and puncta formation." [PMID:24185444]
- "ATG-16.1 and ATG-16.2 interact with themselves and each other and also directly associate with ATG-5." [PMID:24185444]
- Background: "The Atg12–Atg5 conjugate possesses an E3-like activity for Atg8 lipidation by promoting the transfer of Atg8 from Atg3 to PE." [PMID:24185444]
- UniProt: conjugation with lgg-3/ATG12 via atg-7 (E1) and atg-10 (E2) is essential (by similarity).

## Decisions
- Core MF: contributes_to Atg8-family ligase activity (GO:0019776) in Atg12-Atg5-Atg16 complex (GO:0034274).
- GO:0034045 phagophore assembly site membrane is obsolete in current GO (QuickGO, replaced_by GO:7770114 phagophore membrane; OLS/local cache not yet updated): MODIFY all three rows to GO:7770114, following the human ATG12 review precedent.
- protein binding IPI rows REMOVE (interaction captured by complex membership).
- regulation of autophagy (IMP) MODIFY to autophagosome assembly; vacuole organization (ARBA) MODIFY to autophagosome assembly; transferase complex (NAS) MODIFY to Atg12-Atg5-Atg16 complex.
