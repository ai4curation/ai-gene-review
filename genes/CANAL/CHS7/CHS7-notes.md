# CHS7 Notes

## 2026-10-11

- Fetched the seeded `CANAL/CHS7` review and GOA/UniProt cache. The GOA
  snapshot contains direct CGD rows from PMID:16079341, three IBA rows from the
  fungal `PANTHER:PTN002175570` ancestor, and a stale `GO:0003674
  molecular_function` ND placeholder.
- Deep research with Falcon and the Perplexity Lite fallback failed because the
  local environment has neither `agentapi` nor the provider API keys. I used the
  cached primary CHS7 paper, the current PTHR35329 PAINT table, the curated
  `yeast/CHS7` and `NEUCR/csc-1` reviews, and the cached 2025 Neurospora
  CHS7-family paper instead.
- Web/PubMed search for newer direct Candida CHS7 papers found the 2007 Sanz,
  Valle, and Roncero promoter-heterozygosity follow-up, now cached as
  `PMID_17559412.md`. I did not find a newer paper that directly changes the
  molecular model for Candida Chs7; later hits were family/context papers or
  transcriptomic studies where CHS7 was one member of a larger wall-response
  gene set.
- Treated the `CGD:CAL0000175393` seed on `GO:0006031 chitin biosynthetic
  process` as expected PAINT self-seeding, not circularity. The C. albicans
  null mutant is one of the experimental descendant observations PAINT used to
  place chitin biosynthetic process at the fungal CHS7-family ancestor.
- Added a local `NEW` row for the current `PTN002175570` `GO:0044183 protein
  folding chaperone` assertion because the local GOA snapshot still has only a
  no-data molecular-function placeholder.
- Left both CGD flocculation rows undecided. The cached PMID:16079341 abstract
  supports CHS7-dependent chitin, septation, filamentation, and colony
  morphology phenotypes, but it does not expose the flocculation assay or
  reconcile the same-paper `GO:0000128` and `GO:0060257` directionality.
