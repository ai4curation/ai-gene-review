# CANAL BCY1 review notes

## 2026-10-11

### Setup

- Created the seeded review with `UV_FROZEN=1 just fetch-gene CANAL BCY1`.
- The first PMID fetch hit an NCBI 429 for PMID:14871949, then a retry with
  `UV_FROZEN=1 just fetch-gene-pmids CANAL BCY1` succeeded and fetched the 2004
  Cassola paper as full text from PMC.
- Attempted deep research with
  `UV_FROZEN=1 just deep-research-falcon CANAL BCY1 --fallback perplexity-lite`.
  This failed locally because `agentapi` was absent from `PATH` and the fallback
  provider API keys were not configured, so this review was completed from GOA,
  UniProt, PANTHER/PAINT, cached publications, and manual PubMed searches.

### Newer literature search

- Searched PubMed for newer Candida BCY1 papers. The strongest recent direct
  hit was the 2025 Hossain et al. subcellular-localization paper, already in
  the GOA rows and cached as PMID:39998251.
- Added Ding et al. 2016, PMID:28105026, which constructed a full `bcy1/bcy1`
  null mutant in a wild-type C. albicans background and showed that BCY1
  deletion causes hyperfilamentation in several media.
- Added Parashar et al. 2026, PMID:42506221, which showed that high iron
  downregulates BCY1 in ras1-null cells and that forced BCY1 expression blocks
  Ras1-independent high-iron hyphal formation.
- Fetched PMID:39742531, a 2025 zingerone paper, but excluded it from the review
  because it is an antifungal perturbation study that only reports BCY1
  transcript downregulation after drug treatment. That observation is too
  indirect for Bcy1 function curation.

### IBA review

- PANTHER family PTHR11635 places cAMP-dependent protein kinase complex
  membership, cAMP-dependent protein kinase inhibitor activity, cAMP binding,
  and protein kinase A catalytic subunit binding at root node
  `PANTHER:PTN004280545`. These are all correct for Candida Bcy1: native C.
  albicans PKA was purified as a tetramer with two regulatory subunits
  [PMID:9523695, "two regulatory (R) subunits of 64 kDa"], and Bcy1
  coimmunoprecipitates with Tpk1-GFP in cells [PMID:14871949,
  "Coimmunoprecipitation of Tpk1-GFP with Bcy1p in ASM1 and ASM2 strongly
  suggests interaction of the two proteins inside the cell."].
- The cytosol IBA from `PANTHER:PTN000180782` is also sound. Functional
  Bcy1-GFP imaging reports that the holoenzyme is mainly cytosolic
  [PMID:39998251, "the PKA holoenzyme is mainly cytosolic"].
- The adenylate cyclase-activating GPCR pathway IBA from
  `PANTHER:PTN000180782` is appropriate for BCY1. Bcy1 is the cAMP-responsive
  PKA regulatory subunit in the GPCR-to-cAMP cassette, so the row was accepted
  and Bcy1's receptor-neutral cAMP/PKA pathway participation was retained via
  the `GO:0046580` Ras-signaling replacement terms.
- The fungi-level nuclear-localization IBA from `PANTHER:PTN000908765` is left
  unresolved. The 2006 abstract supports the older C. albicans Bcy1-GFP nuclear
  model [PMID:16473139, "nuclear localization of the regulatory subunit"], but
  a 2025 full-text paper with a functional Bcy1-GFP allele reports that Bcy1 is
  largely excluded from the nucleus [PMID:39998251, "Bcy1 is largely excluded
  from the nucleus under both conditions"].

### Main curation calls

- Accepted the core PKA regulatory activity, cAMP binding, PKA catalytic-subunit
  binding, PKA complex membership, and cytosol rows.
- Kept P-body, stress-granule, and vacuolar-membrane localization as non-core
  conditional localizations from the 2025 direct imaging paper.
- Replaced generic or mis-scoped pathway rows with negative regulation of
  cAMP/PKA signal transduction or negative regulation of filamentous growth
  where the source evidence supported Bcy1's inhibitory PKA role.
- Removed S. cerevisiae-specific or unsupported electronic transfers to
  chromatin, plasma membrane, nitrogen/glucose starvation, bud-neck localization,
  P-body assembly, and positive regulation of RNA polymerase II transcription.
  These are either not seen in the direct C. albicans Bcy1-GFP localization
  study or describe downstream processes not executed by Bcy1 itself.
