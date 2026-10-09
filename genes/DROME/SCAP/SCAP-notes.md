# SCAP (CG33131; UniProt A1Z6J2) notes

- ER membrane escort of SREBP (UniProt function by similarity; WD40 + sterol-sensing domain).
- In flies SREBP processing is controlled by phosphatidylethanolamine, not sterols
  [PMID:11988566 "The finding that SREBP processing is controlled by different lipids in mammals and flies (sterols and phosphatidylethanolamine, respectively)"].
- Insects are sterol auxotrophs [PMID:9632664 "This is notable, since insects are reportedly incapable of de novo sterol biosynthesis."]
  -> IBA "positive regulation of cholesterol biosynthetic process" REMOVED (taxon mismatch; propagation_review added); IEA sterol binding marked over-annotated.
- Core MF chosen: protein carrier activity (GO:0140597; "Directly binding to a protein and delivering it either to an acceptor molecule or to a specific location") for the SREBP escort role; no existing GOA MF row.
- Deep research: falcon run killed in the first attempt (exit 137, memory pressure on the shared host); a sequential retry was queued. Notes from cached publications.
