# ASB10 review notes

## Sources
- Affinage: trust gates clear.
- Key papers:
  - PMID:34285210 (full text): ASB10 ubiquitylates TEM8 in breast cancer cells.
  - PMID:22156576 (full text): eye localization; outflow facility; glaucoma variants.
  - PMID:23901248 (full text): trabecular meshwork degradation machinery.
  - PMID:40399264 (full text): mouse heart; HSP70 stabilization.
- 5 Reactome cytosol rows from CRL5 neddylation/CAND1/CSN reactions. The cached summaries do not name ASB10; each row's summary names its own reaction.

## Decisions
- ACCEPT: nucleus, cytoplasm and cytosol (IDA, IEA, TAS).
- MARK_AS_OVER_ANNOTATED: intracellular signal transduction (InterPro SOCS-box IEA).
- KEEP_AS_NON_CORE: protein ubiquitination (broad UniPathway IEA).
- REMOVE: LCN2 and MEOX2 protein binding (policy).
- NEW: ubiquitin-like ligase-substrate adaptor activity (IMP, PMID:34285210), the core MF.
