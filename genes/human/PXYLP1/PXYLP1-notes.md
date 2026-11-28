# PXYLP1 notes

## Manual literature review

- Deep research could not be generated for this family because the configured `falcon` and `perplexity` providers were unavailable in the local runner (`agentapi not found`; fallback providers unavailable). I reviewed the fetched UniProt, GOA, PANTHER/PAINT, Reactome, and cached PMID records manually.
- PXYLP1 is a type II Golgi membrane enzyme that dephosphorylates 2-O-phosphorylated xylose in the glycosaminoglycan-protein linkage region of proteoglycans.
- PMID:24425863 is the central paper: it identifies XYLP/PXYLP1, assays dephosphorylation of the phosphorylated linker, localizes XYLP to the Golgi, shows B3GAT3 interaction, and shows reduced chondroitin/heparan sulfate chain formation after XYLP knockdown.
- GO lacks a precise 2-phosphoxylose phosphatase activity term, so I retained the generic phosphatase activity rows and added a proposed new term for the dedicated Rhea 56512 activity.
