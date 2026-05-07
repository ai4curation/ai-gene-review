# CLPB1/HSP101 (AT1G74310) Curation Notes

## Current Review Position

CLPB1/HSP101 is reviewed as an ATP-dependent Hsp100/ClpB protein disaggregase that
supports recovery from heat-damaged protein aggregation and acquired thermotolerance.
The strongest supported core function is disaggregation/remodeling of aggregated
proteins in cooperation with the plant chaperone network.

## Supported Conclusions

- `GO:0140545 ATP-dependent protein disaggregase activity` is the core molecular
  function.
- `GO:0034605 cellular response to heat` and heat-response annotations are retained
  where supported by HSP101 thermotolerance evidence.
- `GO:0042026 protein refolding` is proposed only as the downstream outcome enabled
  by disaggregation and cooperation with sHsp/Hsp70 systems, not as HSP101 performing
  all refolding steps alone.
- The existing `GO:0045727 positive regulation of translation` annotation is retained
  as non-core. PMID:23439916 supports HSP101-dependent HSA32 accumulation and a
  post-transcriptional feedback loop for long-term heat acclimation memory, but it
  does not establish broad translation recovery as a core HSP101 function.
- The generic `protein binding` IPI annotation from PMID:19452453 is recommended for
  modification to `GO:0071889 14-3-3 protein binding`, matching the GOA bait
  `AGI_LocusCode:At1g78300`.

## Non-Retained Draft Claims

Earlier draft notes treated stress granule disassembly and global translation recovery
as a core CLPB1 function. The final review does not retain that framing because the
available primary support in this batch is narrower.
