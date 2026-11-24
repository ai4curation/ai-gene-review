# SCL27 review notes

## 2026-11-24

- Ran `just fetch-gene ARATH SCL27` in the isolated SCL27 child worktree.
  QuickGO returned no GOA rows, but the UniProt record for Q7XJM8 lists TAIR
  and GO_Central annotations as leads: nucleus, DNA-binding/transcriptional
  activity, regulation of transcription, cell differentiation, cell division and
  root hair cell tip growth.
- Re-ran the fetch with `ai-gene-review fetch-gene ARATH SCL27 --force` after
  the first SCL27 PR review. QuickGO then returned 13 GOA rows, covering the
  UniProt leads plus separate GO_Central IBA rows for root hair cell tip growth
  and cell division. I rewrote `SCL27-ai-review.yaml` to audit those real GOA
  rows, dropped the provisional `NEW` rows that had restated existing
  annotations, and kept `NEW` only for negative transcription regulation,
  positive transcription regulation and regulation of meristem development.
- Ran `just deep-research-falcon ARATH SCL27 --fallback perplexity-lite`.
  The configured `deep-research-client` reported that both `falcon` and
  `perplexity` were unavailable, with only `claude_code` available, so I wrote
  `SCL27-deep-research-manual.md` instead.
- Cached four SCL27/HAM/LOM primary papers:
  - PMID:20720155, Wang et al. 2010, abstract only.
  - PMID:21070418, Schulze et al. 2010, abstract only.
  - PMID:21173022, Engstrom et al. 2011, abstract only despite a PMCID because
    the fetcher could not retrieve usable full text.
  - PMID:25101599, Ma et al. 2014, full text from PMC.
- Kept PMID:18500650 from the pre-existing publication cache. It is a useful
  Arabidopsis GRAS-family survey and UniProt's source for the SCL27 nuclear
  localization statement, but the cached abstract does not name SCL27's
  localization specifically.
- The GO-CAM SCL27 activity is inconsistent with the gene literature. Model
  `67e5e74400000148` enables `GO:0043995 histone H4K5 acetyltransferase
  activity` with `AT2G45160/SCL27`; the reviewed AT2G45160 product is a
  HAM/LOM GRAS DNA-binding transcription factor, not the unrelated MYST-family
  H4K5 acetyltransferase HAM1 at `AT5G64610`.
- The refetch exposed two existing `GO:0048768 root hair cell tip growth` rows.
  They trace to PMID:21173022 via TAIR and a HAM-clade PAINT node. The local
  PMID cache is abstract-only despite a PMCID, but the public full text reports
  that Atham1,2,3 root hairs have elevated branching and transient swelling, so
  I ran a QuickGO comparator check before retaining the rows: TAIR currently
  annotates the upstream root-hair transcription factor RHD6 to GO:0048768 but
  not the downstream RHD6 target RSL4. I therefore kept the root-hair rows as
  non-core existing assertions rather than treating GO:0048768 as part of
  SCL27's direct nuclear transcription-factor core.
