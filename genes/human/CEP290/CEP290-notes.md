# CEP290 notes

Deep research: not run. In this environment falcon times out and perplexity-lite is not installed. The review
uses cached publications (`just fetch-gene-pmids human CEP290`) and the C. elegans TZ module literature.

## Key findings (with provenance)
- Direct microtubule binding by region M: [PMID:24051377 "Region M was found to directly and robustly bind to microtubules in a concentration-dependent manner"]
- Direct liposome binding by the N-terminal domain: [PMID:24051377 "CEP290 aa 1–580 associated with liposomes robustly"]
- Required for ciliogenesis; CP110 antagonizes it: [PMID:18694559 "Ablation of CEP290 prevents ciliogenesis without affecting centrosome function or cell-cycle progression"]
- Located at the TZ, centriolar satellites and connecting cilium: [PMID:23943788 "co-localizes with CEP290 to the transition zone (TZ) of primary cilia and centriolar satellites in ciliated cells"]
- Proximal TZ position: [PMID:28401750 "CEP290’s signal had a width close to that of the axoneme"]
- Worm CEP-290 is the MKS-module assembly factor downstream of MKS-5: [PMID:26982032 "central assembly factor that is specific for established MKS module components and depends on the coiled coil region of MKS-5"]
- NPHP5 partner and BBSome integrity: [PMID:25552655 "Depletion of Cep290, another transition zone protein that directly binds to NPHP5, causes additional dissociation of BBS8"]

## Curation decisions
- All 30 GO:0005515 rows REMOVE (no informative MF). NEW: microtubule binding (GO:0008017) and lipid binding
  (GO:0008289), both IDA from PMID:24051377.
- Reactome neutrophil-degranulation rows (extracellular region, specific granule lumen) REMOVE: a cytoplasmic
  coiled-coil protein with no signal peptide.
- protein transport (ISS) MODIFY -> protein localization to cilium.
- MKS complex (ISS) kept non-core: CEP290 is usually treated as its own TZ module.
