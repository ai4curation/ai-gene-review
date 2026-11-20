# acoC research notes


## 2026-10-26 source-specific annotation audit

Normal exact-accession seeding retrieved reviewed Q59695, gene acoC, taxon 303, with G2/PpG2 nucleotide sequence linked to PMID:7813883 and EMBL L35343/AAB58981.1. The curated E2 reaction/pathway plus locus and lipoyl-domain evidence support acetyl transfer and acetoin catabolism; no isolated-enzyme assay is claimed from crude-cell E2 measurements. Original membrane IEA node PANTHER:PTN008685320 remains unresolved: no exact native localization experiment or justified node-loss argument was recovered. A soluble-looking architecture does not prove absence of membrane association. Keep UNDECIDED rather than rejecting from an unrelated family name or nuclear/peroxisomal analog. Sequence comparison to KT2440 is documented without inventing a phylogeny.

Acquisition and preservation: the complete original review payloads and raw UniProt/GOA hashes were captured before editing in the audit baseline. All rows, including inherited proposals and retirement flags, are preserved. Actual Falcon and perplexity-lite fallback attempts failed; no provider report was fabricated. Normal gene-publication acquisition succeeded, and actual FEBA/fitness attempts failed without generating usable data. Logs are in `.cache/module-audit-logs/acetoin-pseudomonas-fetch/`; this manual research note records the independent review. PMID:7813883 remains abstract-only after normal force, publisher-page and PDF recovery attempts; the publisher minimal page adds references but not full text. Full PMID:34513815/36482024/42046433 were read where relevant. Existing provider artifacts are discovery aids, not substitutes for source verification. The annotation-reviewer consultation agreed with separating component activity from isolated-subunit catalysis, native catabolism from engineering, and condition-limited negative assays from universal absence.

## 2026-11-02 — acetoin/butanediol module completion pass

- Deep research: no provider deep-research file exists for this gene, and none could be generated
  in this session (no deep-research provider API keys were configured). No deep-research file was
  written by hand. The review rests on the cached primary publications, the UniProt record and the
  PANTHER/PAINT family files cited in the review.
- Resolved the former UNDECIDED TreeGrafter membrane (GO:0016020) row as MARK_AS_OVER_ANNOTATED:
  the membrane IBD sits at the deep PTHR43798 alpha/beta-hydrolase node PTN000177089; AcoC is a
  lipoyl-domain E2 with no transmembrane segment or signal peptide in its record.
