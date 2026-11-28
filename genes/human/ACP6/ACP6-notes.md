# ACP6 notes

## Manual literature review

- Deep research could not be generated for this family because the configured `falcon` and `perplexity` providers were unavailable in the local runner (`agentapi not found`; fallback providers unavailable). I reviewed the fetched UniProt, GOA, PANTHER/PAINT, Reactome, and cached PMID records manually.
- ACP6 is lysophosphatidic acid phosphatase type 6. PMID:10506173 cloned LPAP/ACP6, localized endogenous LPAP to mitochondria, and connected LPAP to mitochondrial lipid metabolism; PMID:23807634 describes crystal structures and LPA substrate recognition for human ACP6.
- The Reactome event `R-HSA-8878654` supports LPA hydrolysis but only states a mitochondrial location, not mitochondrial matrix. The matrix TAS row was therefore treated as over-specific.
- The Reactome pathway `R-HSA-1483166` describes phosphatidic acid synthesis through GPAT/AGPAT/PLD reactions. ACP6 hydrolyzes LPA rather than acylating it to PA, so its PA-biosynthesis row was removed and flagged for Reactome to check.
- `GO:2001311 lysobisphosphatidic acid metabolic process` appears to be a lipid-name overreach from ACP6 lysophosphatidic acid phosphatase activity; no direct human evidence reviewed here establishes lysobisphosphatidic-acid metabolism.
