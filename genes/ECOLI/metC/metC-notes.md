# metC (P06721) curation notes

## Sources checked (2026-11-13)
- UniProt P06721 (Swiss-Prot), GOA via QuickGO (19 rows, live QuickGO query matched the cached GOA file).
- Cached publications, all abstract-only: PMID:7049234, 3513164, 8831789, 8663055, 12883870, 29592871.
  Also fetched PMID:21193606 (Kang 2011, alanine racemase coactivity) and used the already cached PMID:16000837.
- Full text was not obtainable: PMC322971 (PMID:3513164) is a scanned article; EuropePMC has no full text
  for the others.
- No deep-research provider file was generated; these notes are a manual literature pass.

## Key facts
- Core reaction: L-cystathionine + H2O = L-homocysteine + pyruvate + NH4+ [PMID:7049234 via UniProt
  "Primarily catalyzes the cleavage of cystathionine to homocysteine, pyruvate and ammonia during methionine biosynthesis"].
- Broad S-substituted cysteine range: KM 0.04 mM cystathionine and 0.25 mM cystine, with similar Vmax
  [UniProt BIOPHYSICOCHEMICAL PROPERTIES, from PMID:7049234]; the structure paper says MetC "cleaves C beta-S bonds
  of a broad variety of substrates" [PMID:8831789].
- Homotetramer, PLP at Lys210 [PMID:8831789].
- GO term status: GO:0004121 is obsolete as an equivalent of GO:0047804, and 'cystathionine beta-lyase activity'
  is a synonym of GO:0047804 (OLS/QuickGO checked). GO:0019346 transsulfuration is obsolete, with consider tags
  GO:0071269 and GO:0019344. GO:0019279 is obsolete, replaced by GO:0071266.

## Side activities (ENZYME_SPECIFICITY tiers)
- L-cysteine desulfhydrase: in vivo phenotype (metC disruption raises cysteine) [PMID:12883870]. Tryptophanase
  is the main contributor [PMID:16000837]. KEEP_AS_NON_CORE.
- Alanine racemase: in vitro [PMID:29592871], and an in vivo rescue of alr dadX only when metJ is mutated
  [PMID:21193606]. Dedicated racemases exist, so this is latent but real. KEEP_AS_NON_CORE (judgement call; the
  abstracts give no rate relative to Alr).
- Serine dehydratase in vitro [PMID:29592871]: not annotated in GOA, not proposed.

## Family
- PANTHER PTHR43500 / PTHR43500:SF1 (UniProt DR line). This is not PTHR11808, the family of the eukaryotic CBLs
  (AT3G57050, S. pombe cbl1).
- PAINT node PTN000211746 asserts GO:0047804 and GO:0019448. For MetC, L-cysteine catabolism has direct support
  from gene disruption, so the IBA row is kept as non-core.
