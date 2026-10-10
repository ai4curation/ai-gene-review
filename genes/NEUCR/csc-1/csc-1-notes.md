# NEUCR csc-1 review notes

## Literature and source search

- `just deep-research-falcon NEUCR csc-1 --fallback perplexity-lite` could not run in this workspace
  because no `agentapi` executable or Falcon/Perplexity/OpenAI API keys were available.
- The seeded GOA rows for Q7SB92 contained only PAINT/GO-Central and UniProt SubCell references,
  so `just fetch-gene-pmids NEUCR csc-1` had no literature PMIDs to fetch from GOA.
- Manual PubMed/web searches for `Neurospora csc-1 NCU05720`, `CSE-7 CHS-4`, and `NCU05720
  CHS-4` found one direct csc-1/CSE-7 paper and one newer CSE-8 paralog paper; no newer
  direct CSE-7 trafficking or enzymology paper was found.
- PMID:29601947 is the key direct paper for csc-1. The cached record is abstract-only, but
  the abstract explicitly reports that CSE-7 is the N. crassa Chs7 ortholog, that CHS-4-GFP
  fails to accumulate at the Spitzenkorper and septa in the cse-7 deletion strain, that
  complementation with cse-7 restores CHS-4-GFP localization, and that CSE-7 is detected in
  ER-associated compartments and identified as a putative ER receptor for CHS-4.
- PMID:39926406 is a newer full-text paper on the second N. crassa Chs7 paralog, CSE-8/NCU01814.
  Its direct experiments assign CSE-8 to CHS-3 trafficking, not to csc-1, but the introduction
  and discussion are useful family context: filamentous fungi can encode two Chs7-like proteins,
  with CSE-7 dedicated to CHS-4 and CSE-8 dedicated to CHS-3.

## PAINT and GOA interpretation

- `interpro/panther/PTHR35329/PTHR35329-entries.csv` places N. crassa CSE-7/Q7SB92, S.
  cerevisiae CHS7/P38843, and C. albicans CHS7/Q5AA40 in subfamily `PTHR35329:SF2`.
- `interpro/panther/PTHR35329/PTHR35329-paint.tsv` has a single fungal CHS7 ancestor,
  `PTN002175570`, with IBD assertions for endoplasmic reticulum membrane, chitin biosynthetic
  process, protein folding, and protein folding chaperone activity. This is the relevant PAINT
  node for all three inherited csc-1 IBA rows in GOA.
- The current PAINT cache has advanced beyond the downloaded csc-1 GOA by placing
  `GO:0044183 protein folding chaperone` at `PTN002175570`. That activity is a better
  synthesized molecular-function term for CSE-7 than the obsolete `GO:0051082` term used by
  older CHS7-family propagation.

## Curation decisions

- Accepted the `GO:0005789 endoplasmic reticulum membrane` IBA and IEA rows because they are
  consistent with both UniProt and the direct CSE-7 localization data.
- Accepted `GO:0006031 chitin biosynthetic process`: CSE-7 is not the catalytic chitin synthase,
  but it performs a direct client-specific export-chaperone step required to deliver CHS-4 to
  chitin-synthesis sites.
- Accepted `GO:0006457 protein folding` as a CHS7-family PAINT assertion. The direct N. crassa
  abstract demonstrates CHS-4 ER export and receptor biology rather than a biochemical folding
  assay, so no separate NEW row for `GO:0044183` was added from the Neurospora abstract alone.
