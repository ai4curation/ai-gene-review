# cheZ (PP_4339, Q88EW3) notes

## 2026-11-03 re-review
- Deep research: `just deep-research PSEPK cheZ --provider perplexity` failed (provider 'perplexity' not available); `just mod-description-deep-research` skipped (no MOD provider configured for PSEPK). Existing falcon report used; every falcon quote was checked as a verbatim substring.
- UniProt quotes now cite the local flat file (file:PSEPK/cheZ/cheZ-uniprot.txt). ARBA-only, imported (ECO:0000313), DE-name and DR GO lines are not used as support.
- Q88EW3 is a reviewed Swiss-Prot entry; FUNCTION, SUBUNIT and SUBCELLULAR LOCATION are curated by similarity (ECO:0000250) and SITE 181 "Enhances dephosphorylation of CheY-P". These are acceptable support.
- The earlier core-function quote attributed the UniProt FUNCTION text to PMID:12534463 (genome paper, abstract-only) and was not verbatim; replaced by the UniProt file quote.
- GO:0003824 MODIFY -> GO:0004721 (module MF); GO:0005737 ACCEPT; GO:0050920 ACCEPT; GO:0009288 bacterial-type flagellum changed from MARK_AS_OVER_ANNOTATED to REMOVE with a source_defects entry (InterPro2GO IPR007439 -> GO:0009288 is wrong for the CheZ family; aligned with the E. coli CheZ review).
- KT2440 support: CheZ co-purifies with CheA [PMID:40197389 "the response regulator CheY and the phosphatase CheZ (two proteins known to be associated with CheA) also showed high Log2(fold change) values"]. No KT2440 cheZ mutant or localization data (falcon report section 4-5). Status COMPLETE.
