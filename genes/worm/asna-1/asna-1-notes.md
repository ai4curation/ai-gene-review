# asna-1 review notes

- 2026-10-28: Created review. `just fetch-gene worm asna-1` timed out on the UniProt
  symbol search; re-ran with `--uniprot-id P30632`, which resolved correctly
  (ASNA_CAEEL, 342 aa, 17 GOA rows).
- No deep-research API keys; manual research in `asna-1-deep-research-manual.md`.
- PMID:23705068 was flagged by the workflow as a key paper. Full text read: it mentions
  asna-1 only as a control strain (Figure 4-figure supplement 3E) [PMID:23705068
  "asna-1 encodes a protein required for proper DAF-7/TGF-β function and an asna-1(−) mutation causes L1 arrest (Kao et al., 2007)."].
  Not used to support any annotation; relevance LOW.

## Decisions

- Core: ATP hydrolysis activity (IDA x2, IBA, IEA all ACCEPT); TA protein insertion into
  ER membrane (IBA, ISS ACCEPT; worm IMP-quality evidence in PMID:33883621); GET complex
  (IBA ACCEPT; WRB-1 co-IP in worm).
- protein binding (Y2H with CEE-1) x2: REMOVE per protein-binding policy.
- protein insertion into ER membrane (IEA): MODIFY -> GO:0071816 (already present).
- Insulin secretion IMP and neuronal localizations (axon, cell body): KEEP_AS_NON_CORE.
  The insulin role is genetically separable from TA targeting (wrb-1 mutants normal) and
  its mechanism is unknown.
- Arsenic detoxification IMP: KEEP_AS_NON_CORE; sensitivity phenotype real, but whether
  ASNA-1 itself performs detoxification (as bacterial ArsA does with ArsB) is not shown.
- NEW: GO:0140597 protein carrier activity (ISS to human/yeast GET3, plus worm SEC-61beta
  co-IP); GO:0005794 Golgi apparatus (IDA, PMID:36939052).
- Did not add NEW process terms for cisplatin response, L1 growth, etc. (phenotype only).
