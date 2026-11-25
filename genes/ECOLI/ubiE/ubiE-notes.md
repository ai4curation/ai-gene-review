# ubiE review notes (E. coli K-12, P0A887)

Reviewed for the ubiquinone_biosynthesis module (ring C-methylation annoton).

## Provenance

- No deep-research provider was available (no API keys); no
  `-deep-research-<provider>.md` file exists or was fabricated. Built from the
  reviewed UniProt record, cached abstracts and the PTHR43591 PAINT table.

## Function

- UbiE is required for both quinone C-methylations. [PMID:9045837 "provide
  evidence that it is required for the C methylation reactions in both
  ubiquinone and menaquinone biosynthesis"]
- ubiE mutants accumulate the unmethylated precursors. [PMID:9045837 "E. coli
  strains containing either the disruption or the point mutation in ubiE
  accumulated 2-octaprenyl-6-methoxy-1,4-benzoquinone and demethylmenaquinone
  as predominant intermediates."]
- The ubiE mutant AN70 has DMK but no MK. [PMID:1444716 "In contrast to the
  wild-type, strain AN70 contained only DMK, but no MK."]
- UbiE is in the Ubi metabolon. [PMID:30686758 "we demonstrate that seven Ubi
  proteins form the Ubi complex"]

## Decisions

- Menaquinone biosynthesis and demethylmenaquinone methyltransferase are
  accepted as core for E. coli (which makes MK8); this differs deliberately
  from P. putida UbiE, where the organism makes no menaquinone.
- Aerobic respiration (UniRule): MARK_AS_OVER_ANNOTATED, end-product effect.
- Ketone biosynthetic process (ARBA): TOO_GENERAL, entailed by GO:0006744.
