# NFYA5 review notes

- 2026-10-28: fetch-gene resolved Q9SYH4 (TAIR AT1G54160, GeneID 841856), as
  requested. 17 GOA rows. All primary GOA papers except PMID:27650334 and
  PMID:23118940 are abstract-only in the cache; PMC full text for PMID:18682547 and
  PMID:17322342 could not be retrieved (publisher restriction). Synthesis with
  provenance in NFYA5-deep-research-manual.md.
- Core MF: contributes_to GO:0000981 (NF-YA binds CCAAT only within the trimer
  [PMID:23118940 "the complete NF-YA/NF-YB/NF-YC heterotrimer is necessary to bind
  CCAAT-box containing promoters"]); enables rows queried upstream as WRONG_QUALIFIER
  (SUSPECTED), same treatment as NFYA7.
- Best-supported physiological role: drought response (knockout drought-sensitive,
  overexpressor resistant, required for drought-gene expression) [PMID:18682547].
  Accepted GO:0009414.
- Embryo/seed/somatic embryogenesis rows rest on overexpression with no single-mutant
  phenotype [PMID:22933713]; qualifier is acts_upstream_of_or_within, kept non-core.
- Blue light / ABA signalling rows from a single study (PMID:17322342); kept non-core.
- No NEW terms proposed: the only additional candidate processes (stomatal regulation,
  sucrose response) rest on phenotype/expression evidence.
