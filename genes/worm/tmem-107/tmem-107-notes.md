# tmem-107 (H2L2K0) notes

Deep research: `just deep-research-falcon worm tmem-107 --fallback perplexity-lite` failed (falcon timed out at 600 s; perplexity provider not available). No deep-research file was created. The review is based on cached publications and the PubMed MCP (the PMC full text of PMID:26595381 was read; the local cache holds the abstract only).

## Key findings
- TZ protein in the MKS module, expressed in ciliated cells and DAF-19 dependent [PMID:26595381 "identified TMEM107 as a TZ protein mutated in oral-facial-digital syndrome and JBTS patients"].
- Acts redundantly with NPHP-4 in cilium integrity, TZ docking and Y-link assembly [PMID:26595381 "functions redundantly with NPHP-4 to regulate cilium integrity, TZ docking and assembly of membrane to microtubule Y-link connectors"].
- Intermediate MKS layer; recruits MKS-1, TMEM-231, JBTS-14 and TMEM-17 [PMID:26595381 "by organizing recruitment of the ciliopathy proteins MKS-1, TMEM-231 (JBTS20) and JBTS-14 (TMEM237)"].
- Full text (PMC5580800, not cached): in tmem-107 mutants TRAM-1 leaks into cilia but RPI-2 does not (a selective barrier defect); tmem-107;nphp-4 double mutants have short phasmid dendrites.
- Immobile in the TZ membrane, with a periodic distribution [PMID:26595381 "MKS module membrane proteins are immobile and super-resolution microscopy in worms and mammalian cells reveals periodic localizations within the TZ"].

## Curation decisions
- All 8 GOA annotations were reviewed: 7 ACCEPT and 1 KEEP_AS_NON_CORE (dendrite development, IGI).
- One NEW annotation: GO:1903565 negative regulation of protein localization to cilium (IMP), for the ciliary gate, matching the sibling reviews mks-2, mks-3 and mksr-1.
