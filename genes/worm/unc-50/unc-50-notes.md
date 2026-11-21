# unc-50 notes

## 2026-11-21

- Fetched `worm` `unc-50` with `just fetch-gene worm unc-50`, yielding UniProtKB
  Q10045 and six seeded GOA rows: three Golgi membrane rows, one
  `GO:0097120` receptor-localization row, a generic `GO:0005515` IPI row and a
  `GO:0006937` ACR-2R genetic-interaction row.
- Automated deep research was unavailable: `just deep-research-falcon worm
  unc-50 --fallback perplexity-lite` failed because only `claude_code` was
  configured locally and the fallback also failed. I wrote
  `unc-50-deep-research-manual.md` from the local UniProt, GOA, WormBase,
  PAINT and publication evidence instead of creating a fake provider file.
- `just fetch-gene-pmids worm unc-50` cached PMID:17853888 and confirmed that
  PMID:20027209 was already cached. PMID:17853888 was abstract-only locally
  because PMC and Europe PMC full-text routes were unavailable; the EMBO PDF
  endpoint for doi:10.1038/sj.emboj.7601858 was reachable and used for the
  full-text checks.
- After the first PR review, `just fetch-pmid 17853888 --force` reached the
  PMCID HTML fallback and refreshed `publications/PMID_17853888.md` with full
  text from PMC2034668. The review now anchors Eimer et al. Golgi localization,
  L-AChR trafficking, lysosomal rerouting and Gea1p yeast-two-hybrid statements
  to the cached full text instead of the manual synthesis.
- Resolved the two WITH/FROM accessions exactly: UniProtKB:P47102 is S.
  cerevisiae `GEA1`, the yeast Arf GEF used in the UNC-50 yeast-two-hybrid
  assay, and UniProtKB:P48182 is C. elegans `acr-2`, the neuronal nAChR subunit
  assayed in the acr-2(n2420gf) suppressor screen.
- `just paint-losses worm unc-50` reported no IRD or IKR loss on the Q10045
  lineage, so the PANTHER PTN000303504 Golgi-membrane propagation from the
  UNC-50/GMH1 family was accepted. SGD:S000001738 was checked against SGD and
  resolves to the S. cerevisiae `GMH1` / `YKR030W` gene product.
- Accepted Golgi membrane and receptor localization to synapse as the core
  location and process for UNC-50, kept the ACR-2R suppressor row as a
  non-core physiological output of receptor trafficking, and removed the bare
  `GO:0005515` protein-binding row under the protein-binding policy.
