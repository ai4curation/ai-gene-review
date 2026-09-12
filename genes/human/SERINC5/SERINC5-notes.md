# SERINC5 curation notes

## 2026-07-18 evidence log

- Ran `just fetch-gene human SERINC5`: 18 GOA rows were seeded and grouped one-to-one in the review.
- Ran `just fetch-gene-pmids human SERINC5`: all five GOA PMIDs were present in the publication cache.
- Attempted `just deep-research-falcon human SERINC5 --fallback perplexity-lite`. Falcon failed with HTTP 402 and the fallback failed with HTTP 401; no provider-named failed output was retained. Manual research is recorded in `SERINC5-deep-research-manual.md`.
- Read reviewed UniProtKB Q86VE9, all 18 GOA rows, cached Reactome R-HSA-8932980, and every cached GOA publication: PMID:16120614, PMID:19056867, PMID:26416733, PMID:26416734, and PMID:37474505.
- Located and cached the later mechanistic primary study PMID:38785977 because it directly tests whether PS exposure explains restriction.

## Annotation decisions

- Core MF/BP/location: GO:0017128 phospholipid scramblase activity; GO:0017121 plasma membrane phospholipid scrambling; GO:0140374 antiviral innate immune response; GO:0005886 plasma membrane.
- Generic GO:0016020 membrane rows are MODIFY to plasma membrane.
- GO:0140104 molecular carrier activity is MODIFY to phospholipid scramblase activity; the older family-level paper does not directly establish free-serine transport by human SERINC5.
- Perinuclear localization is KEEP_AS_NON_CORE because it is chiefly the result of viral Nef/GlycoGag antagonism.
- HPA cytosol is UNDECIDED: the primary imaging record is not locally available and the term conflicts with an obligate multipass-membrane topology.
- Urinary extracellular exosome is UNDECIDED: PMID:19056867 is abstract-only locally, and the accessible text does not identify SERINC5.
- Phosphatidylserine metabolic process is KEEP_AS_NON_CORE: the ISS/older family evidence supports a possible lipid-synthesis consequence, but the direct human molecular activity is scrambling.
- No NEW rows are proposed because the defining molecular function, process, antiviral role, and location are already represented.

## Mechanistic boundary

SERINC5-dependent PS scrambling is experimentally established, but PS exposure alone is not sufficient to explain HIV-1 restriction [PMID:38785977, "PS externalization is likely not the key driver for infectivity reduction by SER5."]. Avoid descriptions that state scrambling directly causes restriction as settled fact.

## Experimental priorities

1. Separate scrambling from restriction with mutations that preserve folding, surface abundance, Nef sensitivity, and virion incorporation.
2. Determine the physiological regulation and non-viral consequences of SERINC5 scrambling in uninfected human cells.
3. Compare all four UniProt isoforms for topology, localization, lipid specificity, Nef-mediated downregulation, virion incorporation, and restriction potency.
