# atg-16.2 (Q09406, K06A1.5) review notes

## Provenance / process
- Q09406 is the Swiss-Prot entry (534 aa); used.
- Deep research failed (falcon timeout; perplexity-lite fallback killed, exit 137). No deep-research file; review based on cached publications, UniProt and PubMed. PMC full text for PMID:24185444 could not be retrieved via PubMed MCP (empty full_text), and the cache lacks Results.

## Key evidence [PMID:24185444]
- "We showed that atg-16.2 mutants exhibit a stronger autophagic defect than atg-16.1 mutants."
- "In atg-16.2; atg-16.1 double mutants, the lipidated form of LGG-1 accumulates, but LGG-1 puncta are completely absent."
- "ATG-16.2 ectopically expressed on the plasma membrane provides novel sites of LGG-1 puncta formation."
- "the C-terminal WD repeats are dispensable for the role of atg-16.2 in aggrephagy"
- "Lipidation of LGG-1 increases rather than reduces in atg-16.2; atg-16.1 mutants." - i.e. worm ATG-16 is a site-specifier, not required for lipidation per se.
- LGG-2 (not LGG-1) binds ATG-16.1/ATG-16.2 [PMID:27046254].
- Germline: "ATG-16.2/ATG16L all promote cell-cycle progression" via DAF-16 [PMID:28285998].

## Decisions
- Core MF: protein-membrane adaptor activity (GO:0043495, IBA accepted) in Atg12-Atg5-Atg16 complex.
- Plasma membrane EXP/IEA marked over-annotated: the visible evidence is engineered PM targeting. Not removed because Results were not visible.
- GO:0034045 (obsolete; replaced_by GO:7770114) rows MODIFY to phagophore membrane.
- Autophagosome membrane IBA kept non-core (complex acts on phagophore).
- protein binding IPI rows REMOVE; germline and S. aureus IEP rows kept non-core.
