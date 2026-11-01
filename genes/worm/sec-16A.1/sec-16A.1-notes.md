# sec-16A.1 review notes

## 2026-10-28 session

- Fetched P34643 (SC161_CAEEL, ZK512.5, WBGene00013985). fetch-gene needed retries
  (UniProt REST read timeouts) but resolved to P34643. 12 GOA rows.
- Literature: only two worm papers study the protein directly (PMID:21478858 Witte
  et al. 2011; PMID:23840591 Ackema et al. 2013). See sec-16A.1-deep-research-manual.md.
- Core picture: SEC16-family ERES scaffold. Marks ER exit sites in germline
  [PMID:21478858 "We conclude that TFG-1 localizes to ER exit sites with both SEC-16 and COPII machinery."],
  binds TFG-1 directly [PMID:21478858 "These data confirm a direct biochemical association between SEC-16 and TFG-1."],
  is needed for COPII (SEC-13) puncta and Golgi RAB-6 distribution.
- Decisions:
  - protein binding (IPI, TFG-1): REMOVE per protein-binding policy; the interaction is real
    and captured in core_functions text. No GO term for a TFG-1-specific binding.
  - ER (EXP, IEA): ACCEPT; ERES (GO:0070971) is already present as the sub-compartment.
  - ERGIC (EXP from PMID:23840591, IEA SubCell): MARK_AS_OVER_ANNOTATED. Full text of
    PMID:23840591 uses SEC-16 only as an ERES marker; ERGIC is not mentioned. Recorded a
    PROBABLE source defect for UniProt.
  - ER to Golgi transport vesicle membrane (IBA): MARK_AS_OVER_ANNOTATED; metazoan Sec16
    is a stable ERES-resident scaffold, worm data show it only at ERES.
  - ERES (IBA, IDA x2), ER-to-Golgi transport (IBA, IMP), protein-membrane adaptor (IBA):
    ACCEPT.
- No NEW terms proposed.
