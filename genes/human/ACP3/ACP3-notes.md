# ACP3 notes

## Manual literature review

- Deep research could not be generated for this family because the configured `falcon` and `perplexity` providers were unavailable in the local runner (`agentapi not found`; fallback providers unavailable). I reviewed the fetched UniProt, GOA, PANTHER/PAINT, Reactome, and cached PMID records manually.
- ACP3 encodes the secreted prostatic acid phosphatase isoform and the transmembrane TM-PAP isoform. The main retained functions are acid phosphatase activity, lysophosphatidic acid phosphatase activity in seminal plasma, ecto-5-prime-nucleotidase activity in dorsal-root-ganglion neurons, and protein tyrosine phosphatase activity toward ERBB2.
- PMID:17638863 is the direct TM-PAP localization paper. One UniProt plasma-membrane row cites PMID:17658863 instead; that PMID is a single-walled carbon nanotube antimicrobial paper and is recorded as a likely PubMed identifier transposition.
- The thiamine-monophosphate rows trace to the historical TMPase histochemical activity used to identify the DRG enzyme before it was assigned to TM-PAP. I treated them as over-annotations rather than as physiological thiamine-metabolism functions.
- The SEVI amyloid rows describe proteolytic fragments of secreted PAP in semen. I kept identical protein binding as non-core fragment self-assembly and marked whole-protein molecular adaptor activity as over-annotated.
