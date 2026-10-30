# he1.2 notes

## 2026-05-09 review notes

Reviewed GOA, UniProt Q1LW01, PMID:19021768, PMID:20727360, and PANTHER family cache. The direct function is a secreted zinc metalloendopeptidase/hatching enzyme that proteolytically digests the chorion/egg envelope during hatching.

## Re-review 2026-09-29

Full rewrite of the templated review. All 14 GOA rows were re-reviewed against the cached
abstracts of the two primary papers and the UniProt record; PMID:9108332 (original zHCE cDNA
cloning) was cached and added as a background reference.

- Resolved the one PENDING row (GO:0005576 extracellular region, IBA, is_active_in) as ACCEPT:
  the astacin node is a secreted-enzyme clade and he1.2 has direct evidence
  [PMID:19021768 "one kind of hatching enzyme, ZHE1, was able to be purified from the hatching liquid"].
- Replaced every boilerplate summary/reason. Localization rows now cite the UniProt
  SUBCELLULAR LOCATION line and the hatching-liquid purification, not the FUNCTION line.
- GO:0004222 metalloendopeptidase activity (IBA/IEA/IDA): ACCEPT as the core activity. The
  cleavage sites are internal to ZP2/ZP3 [PMID:19021768 "The six ZHE1-cleaving sites were
  located in the N-terminal regions of egg envelope subunit proteins, ZP2 and ZP3, but not in
  the internal regions, such as the ZP domains."], and the structure defines the zinc
  active-site cleft [PMID:20727360 "The central cleft represents the active site of the enzyme
  that is crucial for substrate recognition and catalysis."].
- GO:0008237 metallopeptidase activity (IEA and ZFIN IDA): MODIFY to GO:0004222; the parent
  term is true but the same evidence supports the child, which the gene already carries.
- GO:0008270 zinc ion binding (IEA/IDA): KEEP_AS_NON_CORE (catalytic cofactor, UniProt
  "Binds 1 zinc ion per subunit").
- GO:0035188 hatching (IDA): ACCEPT; participation test passed because the enzyme performs the
  chorion digestion itself [PMID:19021768 "the hatching of zebrafish embryo is performed by a
  single enzyme"].
- GO:0006508 proteolysis (IEA and both IDA rows): ACCEPT as the direct process of the activity.
- Deep-research file retained as a secondary reference only; it states it could not map Q1LW01
  in the retrieved literature, so it is used once (EDTA sensitivity) and never as sole support.
- Description rewritten as standalone biology (single-enzyme hatching system, ZP2/ZP3 sites,
  hatching gland origin, crystal structure); reference_review added to all PMIDs; two
  suggested questions and one experiment added.
- Both primary papers are abstract-only in the cache; actions rely only on statements present
  in the abstracts. Validation: zero errors.
