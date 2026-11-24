# KIF3A notes

Deep research: not run. In this environment falcon times out after 600 s and perplexity-lite is not
installed. The review uses the cached GOA-cited publications, PMID:14603322 and the UniProt record.

## Key points
- Kinesin-II = KIF3A/KIF3B plus KAP3. [PMID:16298999 "Kinesin-2 is composed of two microtubule-based motor subunits, KIF3A/3B, and a kinesin-associated protein known as KAP3"]
- Anterograde IFT motor. [Reactome:R-HSA-5625416 "Anterograde trains travel along the axoneme of the cilium at an estimated rate of 2 micrometers per second in an ATP- and kinesin-2-dependent fashion"]
- IFT-independent role at subdistal appendages (mouse). [PMID:23386061 "Kif3a recruits p150(Glued) to the subdistal appendages of mother centrioles"]
- Ser690 phosphorylation (CaMKII/POPX2) regulates N-cadherin cargo trafficking. [PMID:24338362 "POPX2 affects trafficking by determining the phosphorylation status of KIF3A at serine 690."]

## Curation decisions
- NEW: GO:0035720 intraciliary anterograde transport. Human KIF3A had no IFT process annotation.
  KIF3A is the motor that performs the step, so the participation test passes. Comparator check:
  human KIF3B carries GO:0042073 (IMP, PMID:32386558), queried in QuickGO.
- All generic protein binding rows removed (most are KAP3/KIFAP3, captured by kinesin II complex).
- Organelle organization (TAS) changed to microtubule-based movement. Cytoskeletal protein binding
  changed to microtubule binding.
