# yeast BCY1 review notes

## 2026-10-11

### Setup

- Created the seeded review with `UV_FROZEN=1 just fetch-gene yeast BCY1`.
  The fetch created 56 seeded review rows from 58 current GOA rows, reused the
  existing PTHR11635 PAINT cache, and fetched eight PMIDs that were not already
  cached.
- Attempted deep research with
  `UV_FROZEN=1 just deep-research-falcon yeast BCY1 --fallback
  perplexity-lite`. This failed locally because `agentapi` was absent from
  `PATH` and the fallback provider API keys were not configured, so this review
  needs to be completed from GOA, UniProt, PANTHER/PAINT, cached publications,
  and manual PubMed searches.

### Literature search

- Read the primary BCY1/PKA regulatory-subunit evidence:
  - PMID:6292221: `CYR3` mutant characterization linking altered cAMP
    requirement to the regulatory subunit of yeast cAMP-dependent protein
    kinase.
  - PMID:3037314: cloning and characterization of `BCY1` as the regulatory
    subunit of the cyclic AMP-dependent protein kinase.
  - PMID:3288487: early subcellular fractionation and immunofluorescence
    localization of the cAMP-dependent protein kinase regulatory subunit.
  - PMID:2831892: immunoblot evidence for a plasma-membrane-associated form of
    the regulatory subunit and cAMP-dependent protein kinase activity.
  - PMID:11134339: carbon-source regulation of Bcy1 localization, with
    glucose-grown cells mostly nuclear and carbon-source-derepressed cells
    distributed between nucleus and cytoplasm through Yak1- and
    Zds1-dependent regulation.
  - PMID:16924114: direct PKA regulation by Gpa2-associated kelch-repeat
    proteins, including stimulation of association between the catalytic and
    regulatory PKA subunits in vivo.
  - PMID:26403272: stress-dependent association of PKA catalytic and regulatory
    subunits with promoters and coding regions of stress-responsive genes.
  - PMID:26947009: PKA- and TORC1-dependent regulation of Ams1 under glucose and
    nitrogen starvation.
  - PMID:38865242: 2024 analysis of heat-stress-induced changes in binding of
    Tpk1-3 to Bcy1 and Bcy1-independent reversible sequestration of Tpk3 into
    cytoplasmic granules.
- Confirmed that the PTHR11635 PAINT placements are the same as for `cgs1` and
  `mcb`: root `PTN004280545` carries the core inhibitor, cAMP-binding,
  catalytic-subunit-binding, and PKA-complex assertions; fungal `PTN000908765`
  carries nucleus; the broad `PTN000180782` node carries cytosol and the
  legacy GPCR-pathway process row.
- Inspected high-throughput interaction and localization references. Most
  IntAct rows are generic `protein binding` assertions to TPK1/TPK2/TPK3 or to
  the prolyl isomerase ESS1; only the catalytic-subunit interactors can be
  narrowed to `GO:0034236 protein kinase A catalytic subunit binding`.
- Left the PMID:16683188 `BCY1` identical-protein-binding row undecided: the
  abstract-only cache foregrounds a human Siva/PMP22 interaction, and the
  IntAct-specific evidence for Bcy1 self-interaction cannot be verified locally.

### Curation decisions

- Accepted the core PTHR11635 IBA rows at `PTN004280545` for PKA inhibitor
  activity, cAMP binding, PKA catalytic-subunit binding, and PKA-complex
  membership. Accepted the fungal `PTN000908765` nuclear-localization IBA and
  the `PTN000180782` cytosol IBA. As in the `cgs1`, `mcb`, and *C. albicans*
  `BCY1` sibling reviews, changed the `PTN000180782` `GO:0007189` IBA to
  `GO:0141162 negative regulation of cAMP/PKA signal transduction` because the
  PAINT node groups the right PKA-regulatory family but the GO term describes
  the upstream GPCR/adenylate-cyclase segment.
- Accepted direct and high-throughput nuclear/cytoplasmic localization rows;
  kept chromatin and plasma membrane as non-core condition-specific pools.
- Changed all generic `GO:0005515 protein binding` rows whose partners are
  Tpk1, Tpk2, or Tpk3 to `GO:0034236 protein kinase A catalytic subunit
  binding`; removed the Ess1 rows because they are generic high-throughput
  edges to a non-PKA partner with no specific replacement term.
- Kept glucose-starvation, nitrogen-starvation, and P-body assembly rows as
  non-core pathway outputs of Bcy1-mediated PKA regulation. Marked the broad
  RNA polymerase II transcription row as over-annotated.
- Removed both Ras/Lte1 bud-neck localization rows from PMID:12782684. The
  paper used `bcy1` deletion only to bypass the essential Ras-cAMP branch in a
  `ras1 ras2` background; Ras proteins, not Bcy1, are the actors that recruit
  Lte1 to the bud cortex.
- Left the PMID:16683188 Bcy1 self-interaction row undecided because only an
  abstract was cached; kept the two yeast high-throughput self-interaction rows
  as non-core support for regulatory-subunit dimerization.
