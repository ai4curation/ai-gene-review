# pdeL: c-di-GMP module member review

## 2026-11-05

PdeL/YahA has two demonstrated activities: EAL-domain c-di-GMP hydrolysis [PMID:15995192; PMID:24451384] and DNA-binding transcriptional activation [PMID:26553851]. The existing DNA-binding rows are refined to GO:0001216, so an additional NEW row for the same MF would be redundant.

The older 2005 abstract described catalysis as independent of oligomerization. The later 2014 quantitative study instead finds that “the domain is active only in its dimeric state” [PMID:24451384]. Catalytic activity is retained; the oligomerization mechanism follows the later direct measurements.

PMID:26553851 full text was inspected online at https://pmc.ncbi.nlm.nih.gov/articles/PMC4719445/ and explicitly calls PdeL soluble/cytoplasmic. Standard cache refreshes for PMID:26553851 and PMID:15995192 remained abstract-only; no fabricated full-text cache is supplied. The inherited membrane location is marked over-annotated. `paint-losses` found no lineage IRD/IKR.

PdeL activation mutants reduce biofilm formation, but this does not establish universal activity of wild-type PdeL in standard conditions; the downstream biofilm process is retained non-core.

Falcon deep research was attempted with the standard recipe and failed with HTTP 403 authentication. No provider report was authored manually. This review uses primary-source retrieval and cached papers. Original GOA annotation payloads and UniProt/GOA files were preserved.


## PR #6062 review follow-up — 2026-11-06

Corrected the evidence scope of the plasma-membrane IBA assessment: the accessible PMID:26553851 abstract establishes transcriptional autoregulation, not soluble/cytoplasmic localization. Added its exact result quote and qualified the architecture-based concern in the reason and propagation review. No replacement compartment is asserted.
